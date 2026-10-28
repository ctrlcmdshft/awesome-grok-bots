# Changelog

## 2026-10-27

Initial import of the curated third-party Grok Bot list.

- 177 bots, each with the name, creator, description, category, link, date added, and source recorded in `data/bots.yaml`. Every entry uses `2026-10-27` as the date added.
- Category pages, a short README (quick start, recently added, and links to the guides), and guides for stacks, working together, tips, best practices, and where to find more bots.
- A generator (`scripts/generate.py`) rebuilds the README counts and category pages from the data file. GitHub Actions checks for duplicate links and stale pages without fetching x.ai.

The October 27, 2026 master list footer counted 143 bots (84 earlier + 59 new). The tables contain 177 bot rows: 118 without a "new this round" marker and 59 with one. This repo follows the tables. Round markers were removed. Twelve names also carried an undefined sparkle marker; that marker was removed and the bots were kept.

Shared-folder examples in the guides use a generic path. The disclaimer says these bots are unofficial and not made or endorsed by xAI.
