# Making Bots Work Together

[← Back to README](../README.md)

## On this page

- [How it works](#how-it-works)
- [Practical patterns](#practical-patterns)
- [Community tips on multi-bot setups](#community-tips-on-multi-bot-setups)

## How it works

- **One shared computer.** All your bots share one computer, so a file one bot saves in a shared folder can be read by the others. Bots can hand off work through shared files such as a ledger, a CSV, or a list.
- **Bots can message each other.** In a bot's chat, ask it to message or loop in another of your bots by name. An **@ mention** of a bot's name in chat shows a chip that opens that bot's chat.
- **Some memory is shared.** Lasting facts about you (your name, time zone, old emails to scrub) are visible to all your bots. Each bot also keeps its own private memory.
- **Skills are shared.** A skill (saved reusable how-to) is available to all your bots, so a workflow one bot saves can be run by another.
- **Own desktop, shared logins.** Each bot gets its own desktop and browser window, but browser logins on the shared computer carry over to every bot.

## Practical patterns

- **Finder → Doer via a shared file.** One bot finds things and writes them to a shared file (for example `shared/privacy/broker-hits.csv` on the computer the bots share); another bot reads that file and acts on each row. Example: **Login Ledger** ([@agent\_nick\_](https://x.com/agent_nick_)) builds the account list, **Data Deletion Bot** drafts deletion emails from it.
- **One master ledger for removals.** Keep a single removals ledger (site, date filed, status, recheck date) that every privacy bot reads before filing, so **two bots never file the same opt-out twice**. Assign each site family to one bot (for example people-search → Remove Me ([@OutworkVentures](https://x.com/OutworkVentures)), phone lists → Spam-Call Scrubber, mail → Junk Mail Stopper ([@Kevin\_Logan](https://x.com/Kevin_Logan))).
- **Weekly routine that pings another bot.** For example, a weekly routine on a finder bot ends with "message my removal bot with this week's new hits." The receiving bot works only from that hand-off.
- **One clear job per bot.** Small, single-purpose bots are easier to trust and debug than one bot that does everything. Write each bot's job in one line.
- **Save once, reuse everywhere.** When a workflow works on one bot, save it as a skill so any bot can run it without re-explaining.
- **Store shared facts once.** Put facts every bot needs (old emails, old addresses, old phone numbers to scrub) in shared memory instead of repeating them to each bot.
- **Sign in once.** Log into a site once in the browser and every bot can use that login. Stick to the logins those bots actually need.

## Community tips on multi-bot setups

Sourced from public posts:

- Talk to one "chief of staff" bot that only routes work to specialists, and let bots hand findings to each other. ([@heyrobinai](https://x.com/heyrobinai/status/2111806812148437333))
- Give every bot exactly one job; "one bot doing every job gets messy fast." ([@heyrobinai](https://x.com/heyrobinai/status/2111806812148437333))
- Give each bot a fixed job and written rules, and save every workflow that works as a skill. ([@CalvinHollywood](https://x.com/CalvinHollywood/status/2113886246468546699))
- Move routines off the bot you chat with, and duplicate any bot whose chat has run for days, to save usage. ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2111513393538732162))
- Have your chief-of-staff bot audit new routines daily and run a weekly efficiency check on all of them. ([@_ketsana](https://x.com/_ketsana/status/2112729510491656604))

[← Back to README](../README.md)
