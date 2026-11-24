<div align="center">

<sub><strong>L0NE-6 · DAILY SIGNAL</strong></sub>

# 🐒 MonkeyCode Daily

**MonkeyCode 중국판 / 국제판 · 다중 계정 일일 체크인 · 단일 Python 파일**


[简体中文](../README.md) · [English](README.en.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · **한국어** · [Português (BR)](README.pt-BR.md)
> 버전: **v1.0.0** (2026-11-24)

</div>

## 빠른 시작

```bash
export MONKEYCODE_CN_TOKENS='메인|monkeycode_ai_session=xxxxx'
export MONKEYCODE_INTL_TOKENS='국제|yyyyy'
python3 monkeycode_daily.py
```

한 줄에 계정 하나입니다. `라벨|세션`, 전체 Cookie 또는 세션 값만 사용할 수 있으며 줄바꿈 또는 `&`로 구분합니다.

## 성공 판정

먼저 오늘 상태를 조회합니다. 미체크인일 때만 Cap challenge, 로컬 PoW, redeem, 체크인 제출을 수행하고 마지막에 상태를 다시 읽어 `checked_in=true`인 경우에만 성공으로 보고합니다.

## 배포

Qinglong:

```bash
pip3 install -r requirements.txt
task monkeycode_daily.py
```

GitHub Actions: `MONKEYCODE_CN_TOKENS` / `MONKEYCODE_INTL_TOKENS` Secrets를 추가하고 Actions를 활성화한 뒤 한 번 수동 실행합니다.

## 알림

`MONKEYCODE_NOTIFY=always|fail|0`. PushPlus, Bark, Server酱, WxPusher, WeCom, DingTalk을 지원합니다.

## 테스트

```bash
python -m unittest discover -s tests -v
python -m compileall -q monkeycode_daily.py tests
```

## 보안

Cookie, Session, Token, 전화번호 또는 자격 증명이 포함된 로그를 Git, Issue, 공개 스크린샷에 올리지 마세요.

## 사용 범위

공식 버전은 무료입니다. 유료 재배포, 트래픽 유도, 작성자 사칭, 자격 증명 악용을 금지합니다. 자세한 내용은 [NOTICE.md](../NOTICE.md)를 참고하세요.

## 후원

<p align="center">
  <img src="../assets/donate-wechat.png" width="240" alt="WeChat 후원 QR" />
  &nbsp;&nbsp;
  <img src="../assets/donate-alipay.jpg" width="240" alt="Alipay 후원 QR" />
</p>

QR 코드는 작성자에 대한 자발적 후원에만 사용됩니다.
