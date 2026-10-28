# Contributing

This list is public. Every bot on it is a third-party template. Review a bot before you add it, and before you suggest it.

## Suggest a bot

Open a [bot suggestion](https://github.com/ctrlcmdshft/awesome-grok-bots/issues/new?template=suggest-a-bot.yml) or a pull request. Include:

- Bot name, as shown on the template
- Creator, if the template lists one (handle or name). Leave it blank if the template does not
- One sentence on what it does
- Category and, for Security & Bot Safety or Home Network, the subsection
- The `https://x.ai/bot/...` link
- Where you found it (a directory, a post, or another public page)
- The date you are adding it (`YYYY-MM-DD`)

One link per bot. Check `data/bots.yaml` first so the link is not already listed.

## Add a bot in a pull request

1. Append an entry under `bots:` in [`data/bots.yaml`](data/bots.yaml). Keep these fields:

```yaml
  - name: "Example Bot"
    creator: "@example"
    description: "What it does, in one sentence."
    category: people-search-and-data-brokers
    subcategory: ""
    link: "https://x.ai/bot/EXAMPLE"
    date_added: "2026-11-03"
    source: "Where you found it. Include a URL when you have one."
```

2. `category` must match a `slug` under `categories`. If that category has `subsections`, `subcategory` must match one of those slugs. Otherwise `subcategory` is `""`.
3. `creator` is `""` when the template does not name one. Do not put round markers such as 🆕 in the name. The Recently added section reads `date_added`.
4. Install PyYAML and regenerate the pages:

```bash
pip install -r requirements.txt
python scripts/generate.py
```

5. Commit `data/bots.yaml` plus the regenerated `README.md` and `categories/*.md`. Do not hand-edit those generated files.
6. Add a dated entry to [CHANGELOG.md](CHANGELOG.md).

`python scripts/generate.py --check` validates the data and confirms the generated files match. It checks for duplicate links, missing fields, and unknown categories. It does not fetch x.ai. GitHub Actions runs the same check.

## Recently added

The README lists bots that share the newest `date_added` in the file. When that date has more than 20 bots, it shows a count by category instead of every bot. The initial import is one of those larger dates. A later date with 20 or fewer bots is listed bot by bot. The limit lives at the top of `scripts/generate.py`.

## What to leave out

Keep entries generic. Do not add notes about one person's home network, private bots, or machine-specific paths. Descriptions should say what the bot does, not where a particular computer stores its files.
