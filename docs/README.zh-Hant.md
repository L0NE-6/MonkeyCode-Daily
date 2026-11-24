<div align="center">

<sub><strong>L0NE-6 · DAILY SIGNAL</strong></sub>

# 🐒 MonkeyCode Daily

**MonkeyCode 國內版 / 國際版 · 多帳號每日簽到 · 單檔 Python**

> 版本：**v1.0.0**（2026-11-24）

[简体中文](../README.md) · [English](README.en.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)

</div>

## 快速開始

```bash
export MONKEYCODE_CN_TOKENS='主號|monkeycode_ai_session=xxxxx'
export MONKEYCODE_INTL_TOKENS='國際|yyyyy'
python3 monkeycode_daily.py
```

每行一個帳號，支援 `備註|憑證`、完整 Cookie 或裸 Session；換行與 `&` 都可分隔。

## 驗收方式

先查詢今日狀態；未簽到時取得 Cap challenge，於本機計算 PoW、redeem、提交簽到，最後再次查詢服務端狀態。只有回讀 `checked_in=true` 才回報成功。

## 部署

青龍：

```bash
pip3 install -r requirements.txt
task monkeycode_daily.py
```

GitHub Actions：加入 `MONKEYCODE_CN_TOKENS`、`MONKEYCODE_INTL_TOKENS` Secrets，啟用 Actions 後手動執行一次。

## 通知

`MONKEYCODE_NOTIFY=always|fail|0`，並可設定 PushPlus、Bark、Server醬、WxPusher、企業微信或釘釘。

## 測試

```bash
python -m unittest discover -s tests -v
python -m compileall -q monkeycode_daily.py tests
```

## 安全

不要把 Cookie、Session、Token、手機號或含憑據的日誌提交到倉庫、Issue 或公開截圖。

## 使用邊界

官方版本永久免費。禁止收費包裝、搬運引流、冒充作者與濫用憑據。詳見 [NOTICE.md](../NOTICE.md)。

## 支持

<p align="center">
  <img src="../assets/donate-wechat.png" width="240" alt="微信讚賞碼" />
  &nbsp;&nbsp;
  <img src="../assets/donate-alipay.jpg" width="240" alt="支付寶收款碼" />
</p>

收款碼僅用於自願讚賞。
