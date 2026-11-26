# Awesome Grok Bots

[![Bots](https://img.shields.io/badge/bots-328-2563eb?style=flat-square)](#categories)
[![Updated November 26, 2026](https://img.shields.io/badge/updated-2026--11--26-64748b?style=flat-square)](CHANGELOG.md)

A curated list of **328** third-party Grok Bots. Privacy and cleanup come first: people-search removals, spam, inboxes, and old posts. The rest cover security, home network, money, shopping, productivity, and everyday life.

These bots are unofficial and third-party. They are not made or endorsed by xAI. Review each bot before you add it. Most ask before they send email, file a form, delete, or block anything.

Counts and category pages are generated from [`data/bots.yaml`](data/bots.yaml). Guides below cover stacks, using bots together, tips, best practices, and where to find more.

<a id="contents"></a>
## Contents

- [Top picks / Quick start](#top-picks)
- [Recently added](#recently-added)
- [Categories](#categories)
  - [Privacy and cleanup](#privacy)
    - [People-Search & Data Broker Removal](categories/people-search-and-data-brokers.md) (16)
    - [Spam Calls & Do Not Call](categories/spam-calls-and-do-not-call.md) (9)
    - [Email, Newsletters, Subscriptions & Physical Mail](categories/email-newsletters-and-mail.md) (17)
    - [X (Twitter) Cleanup](categories/x-cleanup.md) (12)
    - [Bonus / Adjacent](categories/bonus-and-adjacent.md) (5)
  - [Security and home network](#security)
    - [Security & Bot Safety](categories/security-and-bot-safety.md) (51)
    - [Home Network, Smart Home & Tech Help](categories/home-network-and-tech.md) (38)
  - [Money and shopping](#money)
    - [Money, Bills & Insurance](categories/money-bills-and-insurance.md) (24)
    - [Renters, Legal & Benefits](categories/renters-legal-and-benefits.md) (5)
    - [Shopping, Deals & Packages](categories/shopping-deals-and-packages.md) (13)
  - [Work and tools](#work)
    - [Productivity, Research & News](categories/productivity-research-and-news.md) (21)
    - [Small Business & Freelance](categories/small-business-and-freelance.md) (14)
    - [Developer & Power-User](categories/developer-and-power-user.md) (16)
    - [Bot Tools (Manage Your Bots)](categories/bot-tools.md) (18)
  - [Home and life](#life)
    - [Home, Car & Household](categories/home-car-and-household.md) (16)
    - [Family, School & Learning](categories/family-school-and-learning.md) (8)
    - [Health, Fitness & Food](categories/health-fitness-and-food.md) (9)
    - [Travel](categories/travel.md) (11)
    - [Career & Job Search](categories/career-and-job-search.md) (5)
    - [X Creators & Content](categories/x-creators-and-content.md) (13)
    - [Fun & Lifestyle](categories/fun-and-lifestyle.md) (7)
- [Guides](#guides)
  - [Suggested Stacks](guides/suggested-stacks.md)
  - [Making Bots Work Together](guides/making-bots-work-together.md)
  - [Tips & Tricks](guides/tips-and-tricks.md)
  - [General Best Practices](guides/best-practices.md)
  - [Where to Find More Bots](guides/where-to-find-more-bots.md)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

<a id="top-picks"></a>
## Top picks / Quick start

Start with one pair, watch a few runs, then add more.

1. [Spam-Call Scrubber (Arash)](categories/people-search-and-data-brokers.md#bot-fUj6TYhiW_cjtzWvbsFgz) ([@MinimalDuck](https://x.com/MinimalDuck)) or [Call List Remover](categories/spam-calls-and-do-not-call.md#bot-eGVcE2autG0u6UcAwE3py) + [Privacy Scrubber](categories/people-search-and-data-brokers.md#bot-ZSQK72Iear_ykfnpTIOHQ) — highest impact for spam calls
2. [Data Deletion Bot](categories/email-newsletters-and-mail.md#bot-ZvdSYibMw2oruiQX-3DSA) + [Unsubscribe Bot](categories/email-newsletters-and-mail.md#bot-YJAP3CUaR3i5F2mhN69tM) — clean up years of signups
3. [Old Posts Auditor](categories/x-cleanup.md#bot-KPK89zuI30cV2Cz35s71s) or [Delete My Tweets!](categories/x-cleanup.md#bot-8xSL_TV4XPZZufWeQrgmv) — reduce historical exposure on X
4. [Bouncer](categories/security-and-bot-safety.md#bot-o2OyTjWlNOUdYwr61prw_) ([@bradshannon](https://x.com/bradshannon)) or [Template Safety Checker](categories/security-and-bot-safety.md#bot-8JbRKMaD-VrcN_QyitMXN) ([@Jorhan](https://x.com/Jorhan)) — vet any third-party bot link before you hit Add
5. [Remove Me](categories/people-search-and-data-brokers.md#bot-qlDBDdHjGkHD9pka-9fRy) ([@OutworkVentures](https://x.com/OutworkVentures)) + [Junk Mail Stopper](categories/email-newsletters-and-mail.md#bot-F1XZoNusJXMm92YTTT6kR) ([@Kevin\_Logan](https://x.com/Kevin_Logan)) — data-broker removals plus physical junk mail, with rechecks
6. [Net Watch](categories/home-network-and-tech.md#bot-0vuunQUBFlb4SnStUCtLt) ([@bradshannon](https://x.com/bradshannon)) — home network map and monitor, plus alerts when software you run is actively exploited
7. [Bill Buster](categories/money-bills-and-insurance.md#bot-ji90nMN5S8qAPDtyVyjfi) ([@oliverparsons](https://x.com/oliverparsons)) + [Last Call](categories/email-newsletters-and-mail.md#bot-YuGzbyI7jVfZedsRUOLCm) ([@thecsguy](https://x.com/thecsguy)) + [Claimed](categories/money-bills-and-insurance.md#bot-wIxb391-9pDKoWXQ8xrbD) ([@liam\_fallen](https://x.com/liam_fallen)) — cut bills, stop trials before they charge, and find money you may be owed
8. [Burn Watch](categories/bot-tools.md#bot-JEpich3S4Dlid1ACt3I6v) ([@CaliLumberJack](https://x.com/CaliLumberJack)) — keep a growing bot fleet from burning usage
9. [Tripwire](categories/security-and-bot-safety.md#bot-XoYfr_5me3IicLxWfpP3n) ([@ssbrouhard](https://x.com/ssbrouhard)) + [UniFi Network Admin](categories/home-network-and-tech.md#bot-mFhBFJhKItbV4FyUl96Za) ([@cadena\_gus](https://x.com/cadena_gus)) — alerts for software you actually run, and read-only daily health checks for people who use UniFi

More combinations are on [Suggested Stacks](guides/suggested-stacks.md).

<a id="recently-added"></a>
## Recently added

1 bot with `date_added` on November 26, 2026.

| Bot | What it does | Creator | Category | Link |
| --- | --- | --- | --- | --- |
| [Mangrove](categories/money-bills-and-insurance.md#bot-VOfh5y4jlFGbZQMxbGsyh) | A trading agent with guardrails that backtests and paper trades first, and sends a live order only after the user approves that exact order. | [@Mangrove\_AI](https://x.com/Mangrove_AI) | [Money, Bills & Insurance](categories/money-bills-and-insurance.md) | [Add](https://x.ai/bot/VOfh5y4jlFGbZQMxbGsyh) |

<a id="categories"></a>
## Categories

<a id="privacy"></a>
### Privacy and cleanup

Removing personal data, stopping spam, cleaning inboxes, and shrinking an online footprint.

- [**People-Search & Data Broker Removal**](categories/people-search-and-data-brokers.md) (16) — Find people-search and data-broker listings, file removals, and recheck.
- [**Spam Calls & Do Not Call**](categories/spam-calls-and-do-not-call.md) (9) — Get a number off telemarketer lists, report scam calls, and screen suspicious calls.
- [**Email, Newsletters, Subscriptions & Physical Mail**](categories/email-newsletters-and-mail.md) (17) — Unsubscribe, cancel recurring charges, triage inboxes, and stop junk mail.
- [**X (Twitter) Cleanup**](categories/x-cleanup.md) (12) — Audit old posts and clean followers, following, and spam accounts on X.
- [**Bonus / Adjacent**](categories/bonus-and-adjacent.md) (5) — Nearby privacy jobs: credit-report errors, phishing checks, account lockdown, and refunds.

<a id="security"></a>
### Security and home network

Vetting bots, account security, scams, patches, and the home network.

- [**Security & Bot Safety**](categories/security-and-bot-safety.md) (51) — Vet third-party bots before you add them, lock down accounts, catch scams, and watch for vulnerabilities that touch what you run.
- [**Home Network, Smart Home & Tech Help**](categories/home-network-and-tech.md) (38) — Homelab and self-hosted helpers, UniFi and Tailscale admins, Wi-Fi fixes, Home Assistant, and everyday tech help.

<a id="money"></a>
### Money and shopping

Bills, insurance, shopping, and packages.

- [**Money, Bills & Insurance**](categories/money-bills-and-insurance.md) (24) — Cut bills, find money you may be owed, and track spending, taxes, and insurance.
- [**Renters, Legal & Benefits**](categories/renters-legal-and-benefits.md) (5) — Leases and deposits, consumer-rights letters, property-tax appeals, and veterans' claims.
- [**Shopping, Deals & Packages**](categories/shopping-deals-and-packages.md) (13) — Compare prices, watch drops, track packages, and shop for cars or resale.

<a id="work"></a>
### Work and tools

Research, developer tools, and bots that manage other bots.

- [**Productivity, Research & News**](categories/productivity-research-and-news.md) (21) — Research, news, reading, and learning.
- [**Small Business & Freelance**](categories/small-business-and-freelance.md) (14) — Bookkeeping, month-end close, and chasing unpaid invoices.
- [**Developer & Power-User**](categories/developer-and-power-user.md) (16) — Shell, local models, Mac tools, and bridges from other assistants.
- [**Bot Tools (Manage Your Bots)**](categories/bot-tools.md) (18) — Build plugins, cut routine usage, and back up bot setups.

<a id="life"></a>
### Home and life

Home, health, travel, work, and everything else.

- [**Home, Car & Household**](categories/home-car-and-household.md) (16) — Warranties, maintenance, home search, and contractor bids.
- [**Family, School & Learning**](categories/family-school-and-learning.md) (8) — School portals, IEPs, co-parenting, homework help, library cards, and languages.
- [**Health, Fitness & Food**](categories/health-fitness-and-food.md) (9) — Training, meals, insurance claims, and appointment prep.
- [**Travel**](categories/travel.md) (11) — Road trips, flights, parks, packing, and snow.
- [**Career & Job Search**](categories/career-and-job-search.md) (5) — Find roles, tailor a resume, and practice interviews.
- [**X Creators & Content**](categories/x-creators-and-content.md) (13) — See what posted well, cut clips, and draft replies.
- [**Fun & Lifestyle**](categories/fun-and-lifestyle.md) (7) — Sports, skywatching, tabletop games, and voting.

<a id="guides"></a>
## Guides

- [**Suggested Stacks**](guides/suggested-stacks.md) — Combos made only from bots on this list. Add one stack at a time.
- [**Making Bots Work Together**](guides/making-bots-work-together.md) — Shared computer, hand-offs between bots, and one job per bot.
- [**Tips & Tricks**](guides/tips-and-tricks.md) — Vetting, approvals, usage, routines, and the sourced tips.
- [**General Best Practices**](guides/best-practices.md) — Habits for adding third-party bots and letting them act.
- [**Where to Find More Bots**](guides/where-to-find-more-bots.md) — Directories, feeds, and where the entries in this list came from.

<a id="contributing"></a>
## Contributing

Append a bot to [`data/bots.yaml`](data/bots.yaml) and run `python scripts/generate.py`. [CONTRIBUTING.md](CONTRIBUTING.md) has the fields and how to suggest a bot.

Category pages are generated. Guides are written by hand.

<a id="disclaimer"></a>
## Disclaimer

This is an independent, community-curated list of links to Grok Bots made by other people. It is not affiliated with or endorsed by xAI. I don't build, run, or control the listed bots and am not responsible for what they do, their accuracy, or any outcome from using them. Review a bot's instructions and permissions before using it, especially for money, legal, health, or account access. Nothing here is financial, legal, or medical advice. Listings are provided as-is; to report a problem or request removal, open an issue.

This list is released under [CC0](LICENSE).
