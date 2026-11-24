<div align="center">

<sub><strong>L0NE-6 · DAILY SIGNAL</strong></sub>

# 🐒 MonkeyCode Daily
[简体中文](../README.md) · **English** · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)
> Version: **v1.0.0** (2026-11-24)

**MonkeyCode China / International · multi-account daily check-in · one-file Python**



</div>

## Quick start

Set one or both account variables:

```bash
export MONKEYCODE_CN_TOKENS='main|monkeycode_ai_session=xxxxx'
export MONKEYCODE_INTL_TOKENS='intl|yyyyy'
python3 monkeycode_daily.py
```

Each line is one account. Use `label|session`, a full cookie header, or a bare session value. Lines and `&` both work as separators.

## Check-in contract

The script checks the server status before doing any write:

```text
GET  /api/v1/users/wallet/checkin
POST /api/v1/public/captcha/challenge
solve Cap PoW locally
POST /api/v1/public/captcha/redeem
POST /api/v1/users/wallet/checkin
GET  /api/v1/users/wallet/checkin
```

Success is reported only when the final read returns `checked_in=true`. An HTTP 200, a successful redeem, or a successful POST is not enough.

## Deployment

Qinglong:

```bash
pip3 install -r requirements.txt
task monkeycode_daily.py
```

GitHub Actions:

1. Add `MONKEYCODE_CN_TOKENS` and/or `MONKEYCODE_INTL_TOKENS` under repository Secrets.
2. Enable Actions.
3. Run **🐒 MonkeyCode Daily** manually once.

The daily workflow runs at 07:23 Beijing time. GitHub schedules are best effort.

## Optional notifications

`MONKEYCODE_NOTIFY=always|fail|0`, plus any of:

- `PUSHPLUS_TOKEN`
- `BARK_URL`
- `SERVERCHAN_SENDKEY`
- `WXPUSHER_APP_TOKEN` + `WXPUSHER_UID`
- `WECOM_WEBHOOK`
- `DINGTALK_WEBHOOK` + optional `DINGTALK_SECRET`

## Tests

```bash
python -m unittest discover -s tests -v
python -m compileall -q monkeycode_daily.py tests
```

## Security

Never commit cookies, sessions, tokens, phone numbers, or logs containing credentials. The script prints only account labels and non-secret status fields.

## Usage policy

The official repository and releases are free. Paid repackaging, traffic diversion, identity impersonation, and credential abuse are not permitted. See [NOTICE.md](../NOTICE.md).

## Support

<p align="center">
  <img src="../assets/donate-wechat.png" width="240" alt="WeChat tip QR" />
  &nbsp;&nbsp;
  <img src="../assets/donate-alipay.jpg" width="240" alt="Alipay tip QR" />
</p>

The QR codes are only for voluntary tips to the author.
