<div align="center">

<sub><strong>L0NE-6 · DAILY SIGNAL</strong></sub>

# 🐒 MonkeyCode Daily

**MonkeyCode 中国版 / 国際版 · 複数アカウント毎日チェックイン · 単一 Python ファイル**

> バージョン：**v1.0.0**（2026-11-24）

[简体中文](../README.md) · [English](README.en.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)

</div>

## クイックスタート

```bash
export MONKEYCODE_CN_TOKENS='メイン|monkeycode_ai_session=xxxxx'
export MONKEYCODE_INTL_TOKENS='国際|yyyyy'
python3 monkeycode_daily.py
```

1 行につき 1 アカウントです。`ラベル|セッション`、完全な Cookie、またはセッション値のみを指定できます。改行または `&` で区切ります。

## 成功判定

最初に今日の状態を読み取り、未チェックインの場合のみ Cap challenge、ローカル PoW、redeem、チェックイン送信を実行します。最後に再度状態を読み、`checked_in=true` を確認できた場合だけ成功です。

## デプロイ

Qinglong：

```bash
pip3 install -r requirements.txt
task monkeycode_daily.py
```

GitHub Actions：`MONKEYCODE_CN_TOKENS` / `MONKEYCODE_INTL_TOKENS` を Secrets に登録し、Actions を有効化して一度手動実行します。

## 通知

`MONKEYCODE_NOTIFY=always|fail|0`。PushPlus、Bark、Server酱、WxPusher、WeCom、DingTalk に対応します。

## テスト

```bash
python -m unittest discover -s tests -v
python -m compileall -q monkeycode_daily.py tests
```

## セキュリティ

Cookie、Session、Token、電話番号、認証情報を含むログを Git、Issue、公開スクリーンショットへ投稿しないでください。

## 利用範囲

公式版は無料です。有料再配布、集客目的の転載、作者のなりすまし、認証情報の悪用を禁止します。詳細は [NOTICE.md](../NOTICE.md) を参照してください。

## サポート

<p align="center">
  <img src="../assets/donate-wechat.png" width="240" alt="WeChat 投げ銭 QR" />
  &nbsp;&nbsp;
  <img src="../assets/donate-alipay.jpg" width="240" alt="Alipay 投げ銭 QR" />
</p>

QR コードは作者への任意の投げ銭専用です。
