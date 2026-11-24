import contextlib
import io
import os
import unittest
from unittest import mock

import monkeycode_daily as daily


class FakeResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def json(self):
        return self._payload


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []
        self.closed = False

    def request(self, method, url, **kwargs):
        self.calls.append(
            {
                "method": method,
                "url": url,
                "json": kwargs.get("json"),
                "timeout": kwargs.get("timeout"),
            }
        )
        if not self.responses:
            raise AssertionError("unexpected request")
        return self.responses.pop(0)

    def close(self):
        self.closed = True


class MonkeyCodeDailyTests(unittest.TestCase):
    def test_parse_accounts_supports_labels_and_cookie_headers(self):
        accounts = daily.parse_accounts(
            "一号|raw-session\n二号|monkeycode_ai_session=abc; other=1",
            "cn",
            "CN",
        )
        self.assertEqual([item.label for item in accounts], ["一号", "二号"])
        self.assertEqual(accounts[0].cookie, "monkeycode_ai_session=raw-session")
        self.assertEqual(
            accounts[1].cookie,
            "monkeycode_ai_session=abc; other=1",
        )
        self.assertEqual(accounts[0].origin, "https://monkeycode-ai.com")

    def test_parse_accounts_supports_ampersand_separator(self):
        accounts = daily.parse_accounts("a&b&c", "intl", "INTL")
        self.assertEqual(len(accounts), 3)
        self.assertEqual(accounts[0].label, "INTL-1")
        self.assertEqual(accounts[0].cookie, "monkeycode_ai_session=a")

    def test_prng_and_solver_vectors(self):
        self.assertEqual(daily._prng("0123456789abcdef1", 16), "75209df8b56a7857")
        self.assertEqual(daily._prng("0123456789abcdef1d", 4), "5e47")
        challenge = {
            "challenge": {"c": 1, "s": 16, "d": 4},
            "token": "0123456789abcdef",
            "expires": 1_700_000_060_000,
        }
        self.assertEqual(
            daily.solve_cap(challenge, now=1_700_000_000),
            [235771],
        )

    def test_solver_returns_one_solution_per_challenge_item(self):
        challenge = {
            "challenge": {"c": 2, "s": 12, "d": 3},
            "token": "deadbeef",
            "expires": 1_700_000_060_000,
        }
        self.assertEqual(
            daily.solve_cap(challenge, now=1_700_000_000),
            [1858, 835],
        )

    def test_session_headers_are_site_scoped(self):
        account = daily.Account(
            "intl",
            "INTL-1",
            "monkeycode_ai_session=x",
            daily.ORIGINS["intl"],
        )
        session = daily.make_session(account)
        try:
            self.assertEqual(session.headers["Origin"], daily.ORIGINS["intl"])
            self.assertEqual(session.headers["Referer"], daily.ORIGINS["intl"] + "/console/")
            self.assertEqual(session.headers["Cookie"], "monkeycode_ai_session=x")
        finally:
            session.close()

    def test_solver_rejects_expired_challenge(self):
        challenge = {
            "challenge": {"c": 1, "s": 8, "d": 2},
            "token": "abc123",
            "expires": 1_700_000_000_000,
        }
        with self.assertRaises(daily.ProtocolError):
            daily.solve_cap(challenge, now=1_700_000_001)

    def test_solver_rejects_bad_shape(self):
        with self.assertRaises(daily.ProtocolError):
            daily.solve_cap({"challenge": {"c": 0, "s": 8, "d": 2}, "token": "aa"})

    def test_already_checked_in_does_not_claim(self):
        session = FakeSession(
            [
                FakeResponse({"code": 0, "data": {"checked_in": True, "streak": 7}}),
            ]
        )
        account = daily.Account("cn", "CN-1", "monkeycode_ai_session=x", daily.ORIGINS["cn"])
        result = daily.run_account(account, session=session)
        self.assertTrue(result.ok)
        self.assertEqual(result.outcome, "done")
        self.assertEqual(len(session.calls), 1)
        self.assertEqual(session.calls[0]["method"], "GET")
        self.assertEqual(session.calls[0]["url"], daily.ORIGINS["cn"] + daily.CHECKIN_PATH)

    def test_full_checkin_requires_server_readback(self):
        expires = 1_700_000_060 * 1000
        session = FakeSession(
            [
                FakeResponse({"code": 0, "data": {"checked_in": False}}),
                FakeResponse(
                    {
                        "challenge": {"c": 1, "s": 8, "d": 2},
                        "token": "abc123",
                        "expires": expires,
                    }
                ),
                FakeResponse({"success": True, "token": "captcha-token"}),
                FakeResponse({"code": 0, "data": {}}),
                FakeResponse({"code": 0, "data": {"checked_in": True, "streak": 1, "reward": 10}}),
            ]
        )
        account = daily.Account(
            "intl",
            "INTL-1",
            "monkeycode_ai_session=x",
            daily.ORIGINS["intl"],
        )
        result = daily.run_account(account, session=session, now=1_700_000_000)
        self.assertTrue(result.ok)
        self.assertEqual(result.outcome, "claimed")
        self.assertEqual(len(session.calls), 5)
        self.assertEqual(session.calls[1]["method"], "POST")
        self.assertEqual(session.calls[1]["url"], daily.ORIGINS["intl"] + daily.CHALLENGE_PATH)
        self.assertEqual(session.calls[2]["json"]["solutions"], [94])
        self.assertEqual(session.calls[3]["json"], {"captcha_token": "captcha-token"})
        self.assertEqual(session.calls[4]["method"], "GET")

    def test_after_readback_false_is_failure(self):
        expires = 1_700_000_060 * 1000
        session = FakeSession(
            [
                FakeResponse({"code": 0, "data": {"checked_in": False}}),
                FakeResponse(
                    {
                        "challenge": {"c": 1, "s": 8, "d": 2},
                        "token": "abc123",
                        "expires": expires,
                    }
                ),
                FakeResponse({"success": True, "token": "captcha-token"}),
                FakeResponse({"code": 0, "data": {}}),
                FakeResponse({"code": 0, "data": {"checked_in": False}}),
            ]
        )
        account = daily.Account("cn", "CN-1", "monkeycode_ai_session=x", daily.ORIGINS["cn"])
        result = daily.run_account(account, session=session, now=1_700_000_000)
        self.assertFalse(result.ok)
        self.assertEqual(result.outcome, "failed")
        self.assertIn("回读仍为未签到", result.message)

    def test_business_error_is_not_success(self):
        session = FakeSession([FakeResponse({"code": 10811, "message": "task busy", "data": {}})])
        account = daily.Account("cn", "CN-1", "monkeycode_ai_session=x", daily.ORIGINS["cn"])
        with self.assertRaises(daily.ApiError):
            daily.get_status(session, account)

    def test_summary_does_not_contain_session(self):
        account = daily.Account(
            "cn",
            "CN-1",
            "monkeycode_ai_session=super-secret",
            daily.ORIGINS["cn"],
        )
        result = daily.AccountResult(account, True, "done", "ok")
        self.assertNotIn("super-secret", daily.format_summary([result]))

    def test_load_accounts_reads_both_regions(self):
        with mock.patch.dict(
            os.environ,
            {
                "MONKEYCODE_CN_TOKENS": "cn-a",
                "MONKEYCODE_INTL_TOKENS": "intl-a",
            },
            clear=True,
        ):
            accounts = daily.load_accounts()
        self.assertEqual([item.provider for item in accounts], ["cn", "intl"])

    def test_main_keeps_processing_after_one_account_fails(self):
        first = daily.Account("cn", "CN-1", "monkeycode_ai_session=a", daily.ORIGINS["cn"])
        second = daily.Account(
            "intl",
            "INTL-1",
            "monkeycode_ai_session=b",
            daily.ORIGINS["intl"],
        )
        success = daily.AccountResult(second, True, "done", "already checked in")
        with mock.patch("monkeycode_daily.load_accounts", return_value=[first, second]):
            with mock.patch(
                "monkeycode_daily.run_account",
                side_effect=[daily.NetworkError("network down"), success],
            ) as run_account:
                with mock.patch("monkeycode_daily.send_notification") as notify:
                    with contextlib.redirect_stdout(io.StringIO()) as output:
                        with contextlib.redirect_stderr(io.StringIO()):
                            code = daily.main(["--no-notify"])
        self.assertEqual(code, 1)
        self.assertEqual(run_account.call_count, 2)
        notify.assert_not_called()
        self.assertIn("network down", output.getvalue())


if __name__ == "__main__":
    unittest.main()
