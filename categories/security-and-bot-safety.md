# Security & Bot Safety

[← Back to README](../README.md)

Vet third-party bots before you add them, lock down accounts, catch scams, and watch for vulnerabilities that touch what you run.

**42** bots. Third-party and unofficial. Read the template before you add it.

## On this page

- [Vet bots & protect your bot fleet](#vet-bots) (11)
- [Account security, breaches & identity](#account-security) (8)
- [Scams, phishing & imposters](#scams-phishing) (9)
- [Vulnerabilities, patches, domains & code](#vulnerabilities) (14)
  - [Patch Alert](#bot-GJ6wSFte1rfQRD8oZVrpK)
  - [Vuln Scout](#bot-IiV3YZZ2TAF63sPORZmWy)
  - [Heimdall](#bot-aYIBdTMOCAAdiLsN1iY5o)
  - [Mr. Rigz (PC Steward)](#bot-TeEdtOdobgymTchbFqzzW)
  - [CVE Desk](#bot-xzULzM6Gx3SpDRVrJdjdv)
  - [Security](#bot--qkf41F4R1MtZRetyUrxW)
  - [Cyber Checkup](#bot-583RQ4Q20Bz6QxGGS2L3e)
  - [Dmarc Specialist](#bot-pEUC21J4T7tQ3ORZx8w05)
  - [Domain Tracker](#bot-SwaSdg0XhIa_IliAWggYE)
  - [Dependency & Secret Audit](#bot-IqXV0I1hK8sXPfyrsOZDA)
  - [Security Audit Bot](#bot-ksa8bHwOSris1UoZtCUhU)
  - [Web Security Audit](#bot-Xdx94lJlv-xK14WF6yzVR)
  - [App Security Tester](#bot-3h643OPVhZDt5iS_mKw_7)
  - [Mood Security](#bot-CJvgkBx_INfugO8TtH7gp)

## <a id="vet-bots"></a>Vet bots & protect your bot fleet

| Bot | What it does | Creator | Link |
| --- | --- | --- | --- |
| <a id="bot-o2OyTjWlNOUdYwr61prw_"></a>**Bouncer** | Paste an x.ai/bot link before you Add; it shows what's inside and says CLEAN, WARN, or BLOCK | @bradshannon | [Add](https://x.ai/bot/o2OyTjWlNOUdYwr61prw_) |
| <a id="bot-8JbRKMaD-VrcN_QyitMXN"></a>**Template Safety Checker** | Paste any Grok Bot template, link, or JSON to see what it can access and any red flags. Read-only | @Jorhan | [Add](https://x.ai/bot/8JbRKMaD-VrcN_QyitMXN) |
| <a id="bot-bDhYfDe0sPlaVI9zMmZ4e"></a>**Doorcheck** | Reads another bot template's recipe (instructions, skills, routines, plugins) before you add it and returns a reject/accept-style verdict | @the\_Arow\_H | [Add](https://x.ai/bot/bDhYfDe0sPlaVI9zMmZ4e) |
| <a id="bot-bTuuNK785OULBheQ5rPZ-"></a>**RepoBeagle** | Paste a repo link and get a safety verdict before you trust or clone it | @jvr0x | [Add](https://x.ai/bot/bTuuNK785OULBheQ5rPZ-) |
| <a id="bot-wJTXth8eiaaJpayeryWEd"></a>**Watchtower (beta)** | Security officer for your bot roster: watches the shared computer and vets templates and skills before they are installed | @Ken\_LinkWell | [Add](https://x.ai/bot/wJTXth8eiaaJpayeryWEd) |
| <a id="bot-cym0KqdWV_3AguYOphSBv"></a>**Sentinel** | Read-only guard for the shared computer your bots run on: watches for exposed secrets and pre-screens tools before install | Daniel | [Add](https://x.ai/bot/cym0KqdWV_3AguYOphSBv) |
| <a id="bot-jw-g2H0t8ddd54NW2kCmG"></a>**Guardian** | Read-only watcher that keeps an inventory and least-privilege policy for each bot and reviews what they actually did | Knom | [Add](https://x.ai/bot/jw-g2H0t8ddd54NW2kCmG) |
| <a id="bot-oQxAmMC8N8HCKqP2Tz85n"></a>**Security Bot** | Audits every bot in your setup against the OWASP GenAI Top 10s; read-only until you approve a fix | Jeremy | [Add](https://x.ai/bot/oQxAmMC8N8HCKqP2Tz85n) |
| <a id="bot-Y3xV-T0yxz2UihvOrlIK6"></a>**Security Warden** | Second opinion before risky bot actions: reviews proposed sends, deletes and shell commands for secrets and personal info | @myrrazor | [Add](https://x.ai/bot/Y3xV-T0yxz2UihvOrlIK6) |
| <a id="bot-DWcrUM2ZY3g7lhp0pPA5l"></a>**Security (gatekeeper)** | Your other bots pass it incoming emails and outside data first, and it checks for prompt injection | @Johnson20062123 | [Add](https://x.ai/bot/DWcrUM2ZY3g7lhp0pPA5l) |
| <a id="bot-1YzVIsTRcLxaqlLZouJiB"></a>**BotSec** | Head of security for a home with several bots: checks email for phishing and social-engineering tells, headers and links | @scardinafineart | [Add](https://x.ai/bot/1YzVIsTRcLxaqlLZouJiB) |

## <a id="account-security"></a>Account security, breaches & identity

| Bot | What it does | Creator | Link |
| --- | --- | --- | --- |
| <a id="bot-XoYfr_5me3IicLxWfpP3n"></a>**Tripwire** | Read-only security watcher that learns your stack (repos, hosting, domains, accounts, devices) and alerts only when an exploited vuln, cert/CA issue, breach, scam or leaked key touches you; Monday roundup, quarterly 2FA audit | @ssbrouhard | [Add](https://x.ai/bot/XoYfr_5me3IicLxWfpP3n) |
| <a id="bot-IryynPCY3xK65akHLcubp"></a>**CSO** | Finds leaked keys, walks credential rotations, tightens access to least privilege, audits MFA | @xenappblog | [Add](https://x.ai/bot/IryynPCY3xK65akHLcubp) |
| <a id="bot-C5EIiTZZL2pPpsb_po7Zs"></a>**Lockdown** | Guided teammate that finds your online accounts and walks you through locking each one down on the official pages, one step at a time | @liam\_fallen | [Add](https://x.ai/bot/C5EIiTZZL2pPpsb_po7Zs) |
| <a id="bot-Y8zQlQDtzwGFBrKVWlqCa"></a>**Bourne Bot** | Personal security (OPSEC) advisor for your identity, devices, accounts, communications, location, money and family | @MichaelGannotti | [Add](https://x.ai/bot/Y8zQlQDtzwGFBrKVWlqCa) |
| <a id="bot-YZXOpjwJcGp1Owgm7PKir"></a>**Footprint** | Finds every online account you've made (Gmail evidence, breach data, username checks), then helps you remove the ones you pick | Seth | [Add](https://x.ai/bot/YZXOpjwJcGp1Owgm7PKir) |
| <a id="bot-v5MedUVzGQEty_TkPMpyL"></a>**MyPeople Bot** | Give it your email and it shows which breaches you're in, with the three fixes that matter most | @StuyBoyNY | [Add](https://x.ai/bot/v5MedUVzGQEty_TkPMpyL) |
| <a id="bot-xWzmqrAs6JGivQQskJyNy"></a>**Privacy Sentinel** | Household privacy check: breached emails, data-broker listings and exposed details, then a short ranked fix list | @MinocrisyHQ | [Add](https://x.ai/bot/xWzmqrAs6JGivQQskJyNy) |
| <a id="bot-5_zmKmejS35jcMfnGOErj"></a>**Vault Tidy** | Scans Grok Bot Vault metadata for duplicate logins and contacts, messy labels and expired cards without exposing passwords | @lisamausa | [Add](https://x.ai/bot/5_zmKmejS35jcMfnGOErj) |

## <a id="scams-phishing"></a>Scams, phishing & imposters

| Bot | What it does | Creator | Link |
| --- | --- | --- | --- |
| <a id="bot-Jc3Eh6tRUvTLYqdGjTm7q"></a>**Is This a Scam?** | Send any text, email, link, DM, job offer or screenshot that feels off; get a plain verdict and the safe next step | @dcostaverage | [Add](https://x.ai/bot/Jc3Eh6tRUvTLYqdGjTm7q) |
| <a id="bot-t9mlx--OQnQ2itHxQYQmd"></a>**Scam Check** | Calm second opinion on a suspicious text, email or voicemail transcript you forward or paste | @Biggs237 | [Add](https://x.ai/bot/t9mlx--OQnQ2itHxQYQmd) |
| <a id="bot-n6bSJ2vt2rZuIQahc6G1h"></a>**Inbox Guardian** | Watches your Gmail, Outlook or Proton inbox for phishing and scam emails, moves high-confidence scams to spam and flags the rest | @nft\_dreww | [Add](https://x.ai/bot/n6bSJ2vt2rZuIQahc6G1h) |
| <a id="bot-6kHbobtMr8SAM91KgxHcw"></a>**Scam Guard (inbox)** | Scans Gmail or Outlook twice a day for phishing and scam emails and labels them with the reason; never deletes or moves mail | @0xarthurzs | [Add](https://x.ai/bot/6kHbobtMr8SAM91KgxHcw) |
| <a id="bot-JpyZ_4XxyarEASAyt4OWJ"></a>**Mailman** | Sorts every email in your Grok Bot inbox to the right bot; never replies or clicks, and flags phishing and prompt injection first | @ManaEngineer | [Add](https://x.ai/bot/JpyZ_4XxyarEASAyt4OWJ) |
| <a id="bot-4FhgQWGMAq25XrprzX6Dh"></a>**Columbo** | Watches public X for imposters and scammers, shows you the proof, and files a report only for the accounts you pick | Timothy | [Add](https://x.ai/bot/4FhgQWGMAq25XrprzX6Dh) |
| <a id="bot-n1-T2WUHMQ9YfkdD-raZU"></a>**𝕏 Imposter Account Checker** | Searches X daily for accounts impersonating you, writes them up for you to report, and tells you when X suspends them | @TeslaAIBot | [Add](https://x.ai/bot/n1-T2WUHMQ9YfkdD-raZU) |
| <a id="bot-ZsgeyFyAlUtxHbRgDBZqx"></a>**Botman** | Detective bot that vets your followers, DMs, lists and inbox and writes evidence-backed case files on scammers, bots and impersonators | @Rune\_King\_Jake | [Add](https://x.ai/bot/ZsgeyFyAlUtxHbRgDBZqx) |
| <a id="bot-yu5DTLbi2VHKOSGJdZ6zk"></a>**Crypto Scam Shield** | Friendly coach that teaches how to spot crypto scams, with quizzes, examples, and link or message checks | @allthemoney | [Add](https://x.ai/bot/yu5DTLbi2VHKOSGJdZ6zk) |

## <a id="vulnerabilities"></a>Vulnerabilities, patches, domains & code

| Bot | What it does | Creator | Link |
| --- | --- | --- | --- |
| <a id="bot-GJ6wSFte1rfQRD8oZVrpK"></a>**Patch Alert** | Tell it what software you run; checks CISA's Known Exploited Vulnerabilities list daily and alerts only when something you use is hit | @howdyollie | [Add](https://x.ai/bot/GJ6wSFte1rfQRD8oZVrpK) |
| <a id="bot-IiV3YZZ2TAF63sPORZmWy"></a>**Vuln Scout** | Tracks public CVE and patch advisories and posts short digests to Pages | @thecsguy | [Add](https://x.ai/bot/IiV3YZZ2TAF63sPORZmWy) |
| <a id="bot-aYIBdTMOCAAdiLsN1iY5o"></a>**Heimdall** | Dependency security watch for a GitHub repo; checks advisory feeds twice a day and opens a fix PR only after you approve | @magnus72 | [Add](https://x.ai/bot/aYIBdTMOCAAdiLsN1iY5o) |
| <a id="bot-TeEdtOdobgymTchbFqzzW"></a>**Mr. Rigz (PC Steward)** | Keeps a Windows PC fast and safe: weekday read-only health checks, Defender/firewall watch, approval-gated fixes | @JonnyCakeSouza | [Add](https://x.ai/bot/TeEdtOdobgymTchbFqzzW) |
| <a id="bot-xzULzM6Gx3SpDRVrJdjdv"></a>**CVE Desk** | Read-only CVE desk: breaks down advisories, triages public PoCs without running them, and ranks what to patch | @\_h4xin | [Add](https://x.ai/bot/xzULzM6Gx3SpDRVrJdjdv) |
| <a id="bot--qkf41F4R1MtZRetyUrxW"></a>**Security** | Read-and-report teammate: GitHub security alerts, leaked secrets, your domains and email setup, Cloudflare and Linux weak spots | @PerWendelboe | [Add](https://x.ai/bot/-qkf41F4R1MtZRetyUrxW) |
| <a id="bot-583RQ4Q20Bz6QxGGS2L3e"></a>**Cyber Checkup** | Weekly no-login checkup of your website and email: HTTPS, security headers, SPF/DMARC, blocklists, lookalike domains | @ZyMoProfit | [Add](https://x.ai/bot/583RQ4Q20Bz6QxGGS2L3e) |
| <a id="bot-pEUC21J4T7tQ3ORZx8w05"></a>**Dmarc Specialist** | Reviews DMARC aggregate reports, separates real fails from gateway noise, and guides SPF/DKIM/DMARC policy | @brettev | [Add](https://x.ai/bot/pEUC21J4T7tQ3ORZx8w05) |
| <a id="bot-SwaSdg0XhIa_IliAWggYE"></a>**Domain Tracker** | Watches expiry, DNS and mail settings for domains you own, plus a watchlist of names you want; public WHOIS/RDAP/DNS only | @sdrth | [Add](https://x.ai/bot/SwaSdg0XhIa_IliAWggYE) |
| <a id="bot-IqXV0I1hK8sXPfyrsOZDA"></a>**Dependency & Secret Audit** | Paste a GitHub repo, get a ranked fix list: vulnerable packages with upgrade commands and leaked keys (masked) with rotate steps | Thuong | [Add](https://x.ai/bot/IqXV0I1hK8sXPfyrsOZDA) |
| <a id="bot-ksa8bHwOSris1UoZtCUhU"></a>**Security Audit Bot** | Reviews code you own and returns a private security report that opens with up to five plain-English fixes | @Phil\_Holland | [Add](https://x.ai/bot/ksa8bHwOSris1UoZtCUhU) |
| <a id="bot-Xdx94lJlv-xK14WF6yzVR"></a>**Web Security Audit** | Defensive reviewer for websites and repos you own; P0/P1/P2 findings with evidence, no exploit PoCs, no auto-fixes | @pareshdesai | [Add](https://x.ai/bot/Xdx94lJlv-xK14WF6yzVR) |
| <a id="bot-3h643OPVhZDt5iS_mKw_7"></a>**App Security Tester** | Threat-models and security-tests your own web and mobile apps like an attacker would, then ranks the fixes | @OutworkVentures | [Add](https://x.ai/bot/3h643OPVhZDt5iS_mKw_7) |
| <a id="bot-CJvgkBx_INfugO8TtH7gp"></a>**Mood Security** | (Spanish) Weekly read-only audit of your GitHub repos: leaked secrets incl. history, vulnerable dependencies, branch protection | @bdvd\_25 | [Add](https://x.ai/bot/CJvgkBx_INfugO8TtH7gp) |

---

[← Back to README](../README.md) · [Suggested stacks](../guides/suggested-stacks.md) · [Tips](../guides/tips-and-tricks.md)
