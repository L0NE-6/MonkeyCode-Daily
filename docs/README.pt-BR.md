<div align="center">

<sub><strong>L0NE-6 · DAILY SIGNAL</strong></sub>

# 🐒 MonkeyCode Daily

**MonkeyCode China / Internacional · check-in diário multiconta · Python em arquivo único**


[简体中文](../README.md) · [English](README.en.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Português (BR)**
> Versão: **v1.0.0** (2026-11-24)

</div>

## Início rápido

```bash
export MONKEYCODE_CN_TOKENS='principal|monkeycode_ai_session=xxxxx'
export MONKEYCODE_INTL_TOKENS='intl|yyyyy'
python3 monkeycode_daily.py
```

Cada linha representa uma conta. Use `rótulo|sessão`, um cabeçalho Cookie completo ou apenas o valor da sessão. Linhas e `&` funcionam como separadores.

## Critério de sucesso

O script consulta o estado antes de qualquer escrita. Se ainda não houver check-in, ele obtém o Cap challenge, resolve o PoW localmente, faz redeem e envia o check-in. Depois lê o estado novamente. Só há sucesso quando a leitura final retorna `checked_in=true`.

## Implantação

Qinglong:

```bash
pip3 install -r requirements.txt
task monkeycode_daily.py
```

GitHub Actions: adicione `MONKEYCODE_CN_TOKENS` e/ou `MONKEYCODE_INTL_TOKENS` aos Secrets, habilite Actions e execute uma vez manualmente.

## Notificações

`MONKEYCODE_NOTIFY=always|fail|0`, com suporte opcional a PushPlus, Bark, Server酱, WxPusher, WeCom e DingTalk.

## Testes

```bash
python -m unittest discover -s tests -v
python -m compileall -q monkeycode_daily.py tests
```

## Segurança

Não envie cookies, sessões, tokens, telefones ou logs com credenciais para Git, Issues ou capturas públicas.

## Política de uso

A versão oficial é gratuita. São proibidos empacotamento pago, desvio de tráfego, personificação do autor e abuso de credenciais. Consulte [NOTICE.md](../NOTICE.md).

## Apoio

<p align="center">
  <img src="../assets/donate-wechat.png" width="240" alt="QR de gorjeta WeChat" />
  &nbsp;&nbsp;
  <img src="../assets/donate-alipay.jpg" width="240" alt="QR de gorjeta Alipay" />
</p>

Os QR codes servem apenas para gorjetas voluntárias ao autor.
