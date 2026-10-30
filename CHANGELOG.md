# Changelog

## 2026-10-29

Added 38 bots. Each new entry keeps `date_added: 2026-10-29`. Category and subcategory slugs already matched this list, so none were remapped. Creators with an empty `creator_handle` stay plain text: Pierce, Troy, SoCalFSD, Brian, and EVOO. Privacy Cleanup names no creator.

- People-Search & Data Broker Removal (1): Arthur
- Spam Calls & Do Not Call (1): UK Spam-Call Scrubber
- Email, Newsletters, Subscriptions & Physical Mail (1): Karen the Canceller of Paid Subs
- X (Twitter) Cleanup (2): X List Blocker, Sweep · X Hygiene
- Bonus / Adjacent (1): Privacy Cleanup
- Security & Bot Safety (5): Scam Email Detector, Canary, Zero-Day Desk, Box Inspector, Vibe Check
- Home Network, Smart Home & Tech Help (5): TV Tamer, Cloudflare Admin, MikroTik Auditor, Media Center Engineer, Pulse · Gaming Laptop Tech
- Money, Bills & Insurance (5): Utility Eugene, Bill & Letter Explainer, Credit Card Max, X Money Deep Report Bot, Payout Pilot
- Shopping, Deals & Packages (4): Order Aftercare, Black Friday Bot, Warranty & Returns Keeper, Page Watcher
- Bot Tools (Manage Your Bots) (5): Future-Proof, Backup Bot, Save Usage Bot, Archivist, Penny DOGE
- Home, Car & Household (6): Outage Watch, Recall Radar, Appliance Fix Annie, Grease Monkey Wally, Prepper, Rent Scout
- Health, Fitness & Food (1): Sobriety Bot
- Travel (1): Starlink Scout

Seven sourced tips from the official docs (pages last updated October 28, 2026) went into [Tips & Tricks](guides/tips-and-tricks.md): routine hourly caps, event triggers that do not backfill, checking a routine's time zone and When to run, a chat dry run when there is no Test button, updating or retiring a shared template, browsing templates inside the app, and six steps from a role to a durable bot.

What's New's link currently opens What's New by Matt. Home Scout's link currently opens Realtor by Nick. Neither name was changed.

## 2026-10-27

Initial import of the curated third-party Grok Bot list.

- 177 bots, each with the name, creator, description, category, link, date added, and source recorded in `data/bots.yaml`. Every entry uses `2026-10-27` as the date added.
- Category pages, a short README (quick start, recently added, and links to the guides), and guides for stacks, working together, tips, best practices, and where to find more bots.
- A generator (`scripts/generate.py`) rebuilds the README counts and category pages from the data file. GitHub Actions checks for duplicate links and stale pages without fetching x.ai.
- Creator X handles are stored as `creator_handle` and rendered as profile links. Names with no handle stay plain text.
- Confirmed X handles for 26 creators who previously had only a name. Five unconfirmed names stay plain text: Sentinel (Daniel), TV Tuner (Brandon), Number Scrubber (Crypto), Spam-Call Scrubber (RG), and Delete My Tweets! (Jay).
- Privacy Scrub's link currently opens Reno Planner by the same creator (althetime, [@madmenai](https://x.com/madmenai)).
- Phishing Email Checker's page names the creator Marckenley ([@milkydarkstar](https://x.com/milkydarkstar)).

The October 27, 2026 master list footer counted 143 bots (84 earlier + 59 new). The tables contain 177 bot rows: 118 without a "new this round" marker and 59 with one. This repo follows the tables. Round markers were removed. Twelve names also carried an undefined sparkle marker; that marker was removed and the bots were kept.

Shared-folder examples in the guides use a generic path. The disclaimer says these bots are unofficial and not made or endorsed by xAI.
