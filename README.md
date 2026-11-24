<div align="center">

<sub><strong>L0NE-6 · DAILY SIGNAL</strong></sub>

# 🐒 MonkeyCode Daily

**MonkeyCode 国内版 / 国际版 · 多账号每日签到 · 单文件 Python**

> 当前版本：**v1.0.0**（2026-11-24）

[简体中文](README.md) · [English](docs/README.en.md) · [繁體中文](docs/README.zh-Hant.md) · [日本語](docs/README.ja.md) · [한국어](docs/README.ko.md) · [Português (BR)](docs/README.pt-BR.md)

🔐 Cookie 隔离 · 🌍 CN / Intl 双站 · 🧠 Cap PoW · ✅ 服务端回读 · 👥 多账号 · 📢 多渠道推送 · 🐧 青龙友好 · ☁️ GitHub Actions

<img src="https://img.shields.io/badge/version-v1.0.0-2ea44f?style=for-the-badge" />
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20%E9%9D%92%E9%BE%99-4EAA25?style=for-the-badge" />
<img src="https://img.shields.io/badge/Deploy-Actions%20%7C%20Qinglong-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />
<img src="https://img.shields.io/badge/License-MIT-F472B6?style=for-the-badge" />

[✨ 速览](#-30-秒速览) · [🚀 青龙部署](#-青龙面板) · [☁️ Actions](#-github-actions) · [🔧 环境变量](#-环境变量) · [🧪 测试](#-离线测试) · [🚫 使用边界](#-使用边界) · [✦ 星轨](#-星轨-star-trail)

</div>

---

## ✨ 30 秒速览

| 维度 | 说明 |
| :--- | :--- |
| **做什么** | 为 MonkeyCode 国内版和国际版账号执行每日签到。 |
| **输入** | `MONKEYCODE_CN_TOKENS`、`MONKEYCODE_INTL_TOKENS`，每条是 Session 或完整 Cookie。 |
| **流程** | 查询今日状态 → 获取 Cap challenge → 本地求解 → redeem → 提交签到 → 再查服务端状态。 |
| **成功判据** | 提交后 `GET /api/v1/users/wallet/checkin` 返回 `checked_in=true`；HTTP 200 不算成功。 |
| **部署** | Windows / Linux / 青龙 / GitHub Actions。 |
| **依赖** | Python 3.8+，仅 `requests`。 |

---

## 🚀 功能

- **CN / Intl 双站**：国内站与国际站分别配置、分别执行、分别汇总。
- **多账号**：每行一个账号，支持自定义备注；单账号失败不会中断其他账号。
- **Cap 计算验证**：本地完成 challenge、PoW、redeem，不依赖浏览器。
- **严格回读**：签到提交后必须再次读取服务端状态，确认 `checked_in=true`。
- **幂等**：执行前先查状态，今天已签到直接返回 `done`，不重复领取。
- **安全日志**：日志不输出 Session、Cookie 或 Cap token。
- **通知可选**：PushPlus、Bark、Server酱、WxPusher、企业微信、钉钉。

---

## 🔐 账号格式

### 国内版

```text
主号|monkeycode_ai_session=xxxxx
备用|yyyyy
```

### 国际版

```text
Intl-1|monkeycode_ai_session=xxxxx
Intl-2|yyyyy
```

规则：

1. 每行一个账号，也支持用 `&` 分隔。
2. `备注|凭据` 可省略备注。
3. 凭据可以是 `monkeycode_ai_session=...` 完整 Cookie，也可以只粘贴 Session 值。
4. 不要把真实 Cookie 写进脚本、README、Issue 或公开日志。

---

## 🔧 环境变量

| 变量 | 必填 | 说明 |
| :--- | :---: | :--- |
| `MONKEYCODE_CN_TOKENS` | ⬜ | 国内版多账号，换行或 `&` 分隔。 |
| `MONKEYCODE_INTL_TOKENS` | ⬜ | 国际版多账号，换行或 `&` 分隔。 |
| `MONKEYCODE_CN_TOKEN` | ⬜ | 国内版单账号兼容变量。 |
| `MONKEYCODE_INTL_TOKEN` | ⬜ | 国际版单账号兼容变量。 |
| `MONKEYCODE_NOTIFY` | ⬜ | `always`（默认）/ `fail` / `0`。 |
| `PUSHPLUS_TOKEN` | ⬜ | PushPlus Token。 |
| `BARK_URL` | ⬜ | Bark 完整地址。 |
| `SERVERCHAN_SENDKEY` | ⬜ | Server酱 SendKey。 |
| `WXPUSHER_APP_TOKEN` | ⬜ | WxPusher App Token。 |
| `WXPUSHER_UID` | ⬜ | WxPusher UID，多个用逗号或分号分隔。 |
| `WECOM_WEBHOOK` | ⬜ | 企业微信群机器人 Webhook。 |
| `DINGTALK_WEBHOOK` | ⬜ | 钉钉机器人 Webhook。 |
| `DINGTALK_SECRET` | ⬜ | 钉钉加签密钥。 |

至少配置一个 CN 或 Intl 账号变量。

---

## 🐧 青龙面板

```bash
pip3 install -r requirements.txt
python3 monkeycode_daily.py
```

青龙定时任务命令建议使用运行器：

```bash
task monkeycode_daily.py
```

建议时间：

```text
23 7 * * *
```

脚本使用本地时间；青龙面板通常已经设置 `Asia/Shanghai`。

---

## ☁️ GitHub Actions

仓库内置：

- `.github/workflows/monkeycode.yml`：每天北京时间约 07:23 执行。
- `.github/workflows/test.yml`：push / PR 自动运行离线测试。

### 配置 Secrets

在仓库 `Settings → Secrets and variables → Actions` 添加：

- `MONKEYCODE_CN_TOKENS`
- `MONKEYCODE_INTL_TOKENS`
- 可选通知变量

然后进入 Actions，手动运行一次 **🐒 MonkeyCode Daily**。

> Actions 的 cron 使用 UTC；工作流已经设置为北京时间 07:23。GitHub 的定时触发可能延迟，不能保证准点。

---

## ✅ 严格成功判据

每个账号按以下顺序执行：

```text
GET  /api/v1/users/wallet/checkin
POST /api/v1/public/captcha/challenge
本地计算 Cap PoW
POST /api/v1/public/captcha/redeem
POST /api/v1/users/wallet/checkin
GET  /api/v1/users/wallet/checkin
```

结果分类：

| 结果 | 含义 |
| :--- | :--- |
| `done` | 执行前服务端已确认今日签到。 |
| `claimed` | 提交后服务端回读 `checked_in=true`。 |
| `failed` | 网络、协议、Cap、提交或回读未通过。 |

不会把以下情况报成成功：

- 只拿到 HTTP 200；
- 只完成 Cap redeem；
- 签到 POST 返回 2xx，但回读仍为未签到；
- 服务端返回字段不完整。

---

## 🧾 输出示例

```text
🐒 MonkeyCode Daily v1.0.0
账号数: 2
✅ CN-1 · MonkeyCode 国内版 · claimed · 服务端已确认签到
   {"checked_in": true, "streak": 1}
✅ INTL-1 · MonkeyCode 国际版 · done · 服务端确认今天已经签到，未重复提交
   {"checked_in": true}
结果: 2/2 成功
```

---

## 🧪 离线测试

```bash
python -m unittest discover -s tests -v
python -m compileall -q monkeycode_daily.py tests
```

测试覆盖：

- CN / Intl 账号解析；
- Cap PRNG 固定向量；
- PoW 求解与过期拒绝；
- 已签到短路；
- 完整 challenge → redeem → 提交 → 回读；
- 回读未签到必须失败；
- 业务错误不得伪装成功；
- 日志不泄露 Session。

---

## 🔒 隐私与凭据

- 脚本不包含任何账号、Cookie、Token、手机号或设备信息。
- Cookie 只保存在环境变量 / GitHub Secrets 中。
- 日志与推送只包含备注、站点、结果和脱敏后的状态字段。
- 不要把凭据提交到 Git、Issue、截图或公开日志。

---

## 🚫 使用边界

> **官方版本永久免费。** 未经作者书面许可，禁止付费包装、搬运引流、冒充作者，或使用作者身份与二维码制造官方授权假象。违规内容可能被要求下架；作者可暂停更新、归档或删除仓库及相关 Release。

完整规则见 [NOTICE.md](NOTICE.md)。

---

## ☕ 支持与投喂

如果这个脚本帮你省了时间，欢迎自愿赞赏。赞赏不影响功能，也不影响 Issue 处理。

<p align="center">
  <img src="assets/donate-wechat.png" width="260" alt="微信赞赏码" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/donate-alipay.jpg" width="260" alt="支付宝收款码" />
</p>
<p align="center"><sub>💚 微信支付（左） &nbsp;|&nbsp; 💙 支付宝（右）</sub></p>

> 收款码仅用于向作者自愿赞赏。任何第三方以代下载、代部署、内部资源或会员群为由收费，均与作者无关。

---

## ✦ 星轨 Star Trail

<a href="https://star-history.com/#L0NE-6/MonkeyCode-Daily&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=L0NE-6/MonkeyCode-Daily&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=L0NE-6/MonkeyCode-Daily&type=Date" />
    <img alt="MonkeyCode Daily Star Trail" src="https://api.star-history.com/svg?repos=L0NE-6/MonkeyCode-Daily&type=Date" />
  </picture>
</a>

---

<div align="center">
  <sub>L0NE-6 · DAILY SIGNAL &nbsp;|&nbsp; 点个 <b>Star</b>，让下一轮自动化有迹可循 ✨</sub>
</div>
