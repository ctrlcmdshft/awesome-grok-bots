#!/usr/bin/env python3
"""Rebuild README.md and categories/*.md from data/bots.yaml.

Usage:
  python scripts/generate.py
  python scripts/generate.py --check

--check validates the data file (including duplicate links) and exits
non-zero if the generated pages differ from what is committed. It does
not fetch x.ai or any other site.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "PyYAML is required. Install it with: pip install -r requirements.txt\n"
    )
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "bots.yaml"

# Above this many bots on the newest date_added, the README summarizes by category.
RECENT_LIST_MAX = 20
# Flat category pages get a bot table of contents at this size.
FLAT_TOC_MIN = 12
# Long subsections nest their bots under the page table of contents.
NESTED_TOC_MIN = 12

BOT_ID_RE = re.compile(r"^[A-Za-z0-9_-]+$")
HANDLE_RE = re.compile(r"^[A-Za-z0-9_]{1,30}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
BOT_REF_RE = re.compile(r"\]\(bot:([A-Za-z0-9_-]+)\)")
BOT_PAGE_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((?:\.\./)?categories/[a-z0-9-]+\.md#bot-([A-Za-z0-9_-]+)\)"
)
ROUND_MARKERS = ("🆕", "✨")

BOT_FIELDS = (
    "name",
    "creator",
    "creator_handle",
    "description",
    "category",
    "subcategory",
    "link",
    "date_added",
    "source",
)
TOP_LEVEL = {"groups", "categories", "bots", "quick_start"}
GROUP_FIELDS = {"id", "title", "blurb"}
CATEGORY_FIELDS = {"slug", "title", "group", "blurb", "subsections"}
SUB_FIELDS = {"slug", "title"}

GUIDES = (
    (
        "guides/suggested-stacks.md",
        "Suggested Stacks",
        "Combos made only from bots on this list. Add one stack at a time.",
    ),
    (
        "guides/making-bots-work-together.md",
        "Making Bots Work Together",
        "Shared computer, hand-offs between bots, and one job per bot.",
    ),
    (
        "guides/tips-and-tricks.md",
        "Tips & Tricks",
        "Vetting, approvals, usage, routines, and the sourced tips.",
    ),
    (
        "guides/best-practices.md",
        "General Best Practices",
        "Habits for adding third-party bots and letting them act.",
    ),
    (
        "guides/where-to-find-more-bots.md",
        "Where to Find More Bots",
        "Directories, feeds, and where the entries in this list came from.",
    ),
)


def as_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.date().isoformat()
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def bot_id(link: str) -> str:
    return link.rstrip("/").rsplit("/", 1)[-1]


def anchor(link: str) -> str:
    return "bot-" + bot_id(link)


def human_date(iso: str) -> str:
    day = datetime.strptime(iso, "%Y-%m-%d")
    return f"{day.strftime('%B')} {day.day}, {day.year}"


def cell(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("*", "\\*")
        .replace("_", "\\_")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def creator_link(handle: str) -> str:
    visible = "@" + handle.replace("_", "\\_")
    return f"[{visible}](https://x.com/{handle})"


def creator_cell(bot) -> str:
    handle = bot.get("creator_handle", "").strip()
    creator = bot.get("creator", "").strip()
    if handle:
        return creator_link(handle)
    if creator:
        return cell(creator)
    return "—"


def load_data():
    if not DATA_PATH.is_file():
        sys.exit(f"Missing {DATA_PATH.relative_to(ROOT)}")
    with DATA_PATH.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        sys.exit("data/bots.yaml must be a mapping")
    return data


def _unknown(fields, allowed, label, errors):
    extra = sorted(set(fields) - allowed)
    if extra:
        errors.append(f"{label} has unknown fields: {', '.join(extra)}")


def validate(data):
    errors = []
    _unknown(data.keys(), TOP_LEVEL, "data/bots.yaml", errors)

    groups = data.get("groups")
    categories = data.get("categories")
    bots = data.get("bots")
    quick = data.get("quick_start")

    if not isinstance(groups, list) or not groups:
        errors.append("groups must be a non-empty list")
        groups = []
    if not isinstance(categories, list) or not categories:
        errors.append("categories must be a non-empty list")
        categories = []
    if not isinstance(bots, list) or not bots:
        errors.append("bots must be a non-empty list")
        bots = []
    if not isinstance(quick, list) or not quick:
        errors.append("quick_start must be a non-empty list")
        quick = []

    norm_groups = []
    group_ids = []
    for index, group in enumerate(groups, 1):
        label = f"groups[{index}]"
        if not isinstance(group, dict):
            errors.append(f"{label} must be a mapping")
            continue
        _unknown(group.keys(), GROUP_FIELDS, label, errors)
        item = {
            "id": as_text(group.get("id")).strip(),
            "title": as_text(group.get("title")).strip(),
            "blurb": as_text(group.get("blurb")).strip(),
        }
        if not item["id"] or not item["title"] or not item["blurb"]:
            errors.append(f"{label} needs id, title, and blurb")
        if item["id"] in group_ids:
            errors.append(f"duplicate group id: {item['id']}")
        group_ids.append(item["id"])
        norm_groups.append(item)

    norm_categories = []
    cat_by_slug = {}
    for index, category in enumerate(categories, 1):
        label = f"categories[{index}]"
        if not isinstance(category, dict):
            errors.append(f"{label} must be a mapping")
            continue
        _unknown(category.keys(), CATEGORY_FIELDS, label, errors)
        slug = as_text(category.get("slug")).strip()
        item = {
            "slug": slug,
            "title": as_text(category.get("title")).strip(),
            "group": as_text(category.get("group")).strip(),
            "blurb": as_text(category.get("blurb")).strip(),
            "subsections": [],
        }
        label = f"category {slug or index}"
        if not item["slug"] or not item["title"] or not item["blurb"]:
            errors.append(f"{label} needs slug, title, and blurb")
        if item["group"] not in group_ids:
            errors.append(f"{label} has unknown group {item['group']!r}")
        if item["slug"] in cat_by_slug:
            errors.append(f"duplicate category slug: {item['slug']}")
        raw_subs = category.get("subsections") or []
        if not isinstance(raw_subs, list):
            errors.append(f"{label} subsections must be a list")
            raw_subs = []
        sub_ids = []
        for sub_index, sub in enumerate(raw_subs, 1):
            sub_label = f"{label} subsection {sub_index}"
            if not isinstance(sub, dict):
                errors.append(f"{sub_label} must be a mapping")
                continue
            _unknown(sub.keys(), SUB_FIELDS, sub_label, errors)
            sid = as_text(sub.get("slug")).strip()
            stitle = as_text(sub.get("title")).strip()
            if not sid or not stitle:
                errors.append(f"{sub_label} needs slug and title")
            if sid in sub_ids:
                errors.append(f"duplicate subsection {sid} in {item['slug']}")
            sub_ids.append(sid)
            item["subsections"].append({"slug": sid, "title": stitle})
        item["sub_ids"] = sub_ids
        cat_by_slug[item["slug"]] = item
        norm_categories.append(item)

    seen_links = {}
    norm_bots = []
    by_id = {}
    for index, raw in enumerate(bots, 1):
        label = f"bots[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{label} must be a mapping")
            continue
        _unknown(raw.keys(), set(BOT_FIELDS), label, errors)
        missing = [key for key in BOT_FIELDS if key not in raw]
        bot = {key: as_text(raw.get(key)).strip() for key in BOT_FIELDS}
        if bot["name"]:
            label = bot["name"]
        if missing:
            errors.append(f"{label} missing {', '.join(missing)}")
        if not bot["name"] or not bot["description"] or not bot["link"] or not bot["source"] or not bot["category"]:
            errors.append(f"{label} needs name, description, category, link, and source")
        handle = bot["creator_handle"]
        creator = bot["creator"]
        if handle and not HANDLE_RE.match(handle):
            errors.append(f"{label} creator_handle {handle!r} is not an X handle")
        if creator.startswith("@"):
            expected = creator[1:]
            if handle != expected:
                errors.append(
                    f"{label} creator_handle must be {expected!r} to match {creator}"
                )
        for marker in ROUND_MARKERS:
            if marker in bot["name"]:
                errors.append(
                    f"{label} still has a round marker in the name; record that on date_added"
                )
                break
        if bot["link"] and not bot["link"].startswith("https://x.ai/bot/"):
            errors.append(f"{label} link must start with https://x.ai/bot/")
        bid = bot_id(bot["link"]) if bot["link"] else ""
        if bid and not BOT_ID_RE.match(bid):
            errors.append(f"{label} has an unexpected bot id {bid!r}")
        if bot["link"]:
            if bot["link"] in seen_links:
                errors.append(
                    f"duplicate link {bot['link']} ({seen_links[bot['link']]} and {label})"
                )
            else:
                seen_links[bot["link"]] = label
        if not DATE_RE.match(bot["date_added"]):
            errors.append(f"{label} date_added must be YYYY-MM-DD")
        else:
            try:
                datetime.strptime(bot["date_added"], "%Y-%m-%d")
            except ValueError:
                errors.append(f"{label} date_added is not a real date")
        category = cat_by_slug.get(bot["category"])
        if category is None:
            errors.append(f"{label} has unknown category {bot['category']!r}")
        else:
            sub = bot["subcategory"]
            if category["sub_ids"]:
                if sub not in category["sub_ids"]:
                    errors.append(
                        f"{label} subcategory {sub!r} is not in {bot['category']}"
                    )
            elif sub:
                errors.append(
                    f"{label} has subcategory {sub!r} but {bot['category']} has no subsections"
                )
        bot["id"] = bid
        if bid:
            if bid in by_id:
                errors.append(f"duplicate bot id {bid}")
            by_id[bid] = bot
        norm_bots.append(bot)

    for index, item in enumerate(quick, 1):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"quick_start[{index}] must be a non-empty string")
            continue
        for bid in BOT_REF_RE.findall(item):
            if bid not in by_id:
                errors.append(f"quick_start[{index}] references unknown bot {bid}")
        if "](bot:" in BOT_REF_RE.sub("", item):
            errors.append(f"quick_start[{index}] has a bot reference the generator cannot resolve")

    return errors, norm_groups, norm_categories, norm_bots, by_id


def render_table(bots) -> str:
    lines = [
        "| Bot | What it does | Creator | Link |",
        "| --- | --- | --- | --- |",
    ]
    for bot in bots:
        name = f'<a id="{anchor(bot["link"])}"></a>**{cell(bot["name"])}**'
        link = f'[Add]({bot["link"]})'
        lines.append(
            f"| {name} | {cell(bot['description'])} | {creator_cell(bot)} | {link} |"
        )
    return "\n".join(lines)


def render_category(category, bots) -> str:
    mine = [bot for bot in bots if bot["category"] == category["slug"]]
    noun = "bot" if len(mine) == 1 else "bots"
    lines = [
        f"# {category['title']}",
        "",
        "[← Back to README](../README.md)",
        "",
        category["blurb"],
        "",
        f"**{len(mine)}** {noun}. Third-party and unofficial. Read the template before you add it.",
        "",
    ]
    subs = category["subsections"]
    show_toc = len(subs) > 1 or len(mine) >= FLAT_TOC_MIN
    if show_toc:
        lines.extend(["## On this page", ""])
        if subs:
            for sub in subs:
                rows = [bot for bot in mine if bot["subcategory"] == sub["slug"]]
                lines.append(f"- [{sub['title']}](#{sub['slug']}) ({len(rows)})")
                if len(rows) >= NESTED_TOC_MIN:
                    for bot in rows:
                        lines.append(f"  - [{cell(bot['name'])}](#{anchor(bot['link'])})")
        else:
            for bot in mine:
                lines.append(f"- [{cell(bot['name'])}](#{anchor(bot['link'])})")
        lines.append("")

    if subs:
        for sub in subs:
            rows = [bot for bot in mine if bot["subcategory"] == sub["slug"]]
            lines.extend([f'## <a id="{sub["slug"]}"></a>{sub["title"]}', ""])
            if rows:
                lines.extend([render_table(rows), ""])
            else:
                lines.extend(["No bots in this subsection yet.", ""])
    elif mine:
        lines.extend([render_table(mine), ""])
    else:
        lines.extend(["No bots in this category yet.", ""])

    lines.extend(
        [
            "---",
            "",
            "[← Back to README](../README.md) · "
            "[Suggested stacks](../guides/suggested-stacks.md) · "
            "[Tips](../guides/tips-and-tricks.md)",
            "",
        ]
    )
    return "\n".join(lines)


def rewrite_bot_refs(text: str, by_id) -> str:
    def repl(match):
        bot = by_id[match.group(1)]
        return f"](categories/{bot['category']}.md#{anchor(bot['link'])})"

    return attach_creator_links(BOT_REF_RE.sub(repl, text), by_id)


def attach_creator_links(text: str, by_id) -> str:
    """Add an X profile link after a bot link when that bot has a handle."""
    parts = []
    last = 0
    for match in BOT_PAGE_LINK_RE.finditer(text):
        parts.append(text[last:match.end()])
        bot = by_id.get(match.group(2))
        handle = bot["creator_handle"] if bot else ""
        already = text[match.end():].startswith(" ([@")
        if handle and not already and handle not in match.group(1):
            parts.append(" (" + creator_link(handle) + ")")
        last = match.end()
    parts.append(text[last:])
    return "".join(parts)


def render_quick(items, by_id) -> str:
    lines = [
        '<a id="top-picks"></a>',
        "## Top picks / Quick start",
        "",
        "Start with one pair, watch a few runs, then add more.",
        "",
    ]
    for index, item in enumerate(items, 1):
        lines.append(f"{index}. {rewrite_bot_refs(item.strip(), by_id)}")
    lines.extend(
        [
            "",
            "More combinations are on [Suggested Stacks](guides/suggested-stacks.md).",
            "",
        ]
    )
    return "\n".join(lines)


def render_recent(bots, categories) -> str:
    latest = max(bot["date_added"] for bot in bots)
    recent = [bot for bot in bots if bot["date_added"] == latest]
    when = f"on {human_date(latest)}"
    lines = ['<a id="recently-added"></a>', "## Recently added", ""]
    if len(recent) <= RECENT_LIST_MAX:
        noun = "bot" if len(recent) == 1 else "bots"
        lines.extend(
            [
                f"{len(recent)} {noun} with `date_added` {when}.",
                "",
                "| Bot | What it does | Creator | Category | Link |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        cat_title = {category["slug"]: category["title"] for category in categories}
        for bot in recent:
            name = (
                f"[{cell(bot['name'])}]"
                f"(categories/{bot['category']}.md#{anchor(bot['link'])})"
            )
            category = f"[{cell(cat_title[bot['category']])}](categories/{bot['category']}.md)"
            lines.append(
                f"| {name} | {cell(bot['description'])} | {creator_cell(bot)} | {category} | [Add]({bot['link']}) |"
            )
        lines.append("")
        return "\n".join(lines)

    lines.extend(
        [
            (
                f"{len(recent)} bots have `date_added` {when}. "
                f"This section lists each bot when that date has {RECENT_LIST_MAX} or fewer. "
                "This one is larger, so here is the count by category."
            ),
            "",
            "| Category | Bots |",
            "| --- | --- |",
        ]
    )
    for category in categories:
        count = sum(1 for bot in recent if bot["category"] == category["slug"])
        if count:
            lines.append(
                f"| [{category['title']}](categories/{category['slug']}.md) | {count} |"
            )
    lines.append("")
    return "\n".join(lines)


def render_readme(groups, categories, bots, quick, by_id) -> str:
    count = len(bots)
    latest = max(bot["date_added"] for bot in bots)
    badge_bots = (
        f"https://img.shields.io/badge/bots-{count}-2563eb?style=flat-square"
    )
    badge_updated = (
        "https://img.shields.io/badge/updated-"
        f"{latest.replace('-', '--')}-64748b?style=flat-square"
    )
    lines = [
        "# Awesome Grok Bots",
        "",
        f"[![Bots]({badge_bots})](#categories)",
        f"[![Updated {human_date(latest)}]({badge_updated})](CHANGELOG.md)",
        "",
        (
            f"A curated list of **{count}** third-party Grok Bots. "
            "Privacy and cleanup come first: people-search removals, spam, inboxes, and old posts. "
            "The rest cover security, home network, money, shopping, productivity, and everyday life."
        ),
        "",
        (
            "These bots are unofficial and third-party. They are not made or endorsed by xAI. "
            "Review each bot before you add it. Most ask before they send email, file a form, delete, or block anything."
        ),
        "",
        (
            "Counts and category pages are generated from [`data/bots.yaml`](data/bots.yaml). "
            "Guides below cover stacks, using bots together, tips, best practices, and where to find more."
        ),
        "",
        '<a id="contents"></a>',
        "## Contents",
        "",
        "- [Top picks / Quick start](#top-picks)",
        "- [Recently added](#recently-added)",
        "- [Categories](#categories)",
    ]
    for group in groups:
        lines.append(f"  - [{group['title']}](#{group['id']})")
        for category in categories:
            if category["group"] == group["id"]:
                n = sum(1 for bot in bots if bot["category"] == category["slug"])
                lines.append(
                    f"    - [{category['title']}](categories/{category['slug']}.md) ({n})"
                )
    lines.extend(["- [Guides](#guides)"])
    for path, title, _blurb in GUIDES:
        lines.append(f"  - [{title}]({path})")
    lines.extend(["- [Contributing](#contributing)", ""])
    lines.append(render_quick(quick, by_id).rstrip())
    lines.append("")
    lines.append(render_recent(bots, categories).rstrip())
    lines.append("")
    lines.extend(
        [
            '<a id="categories"></a>',
            "## Categories",
            "",
        ]
    )
    for group in groups:
        lines.extend(
            [
                f'<a id="{group["id"]}"></a>',
                f"### {group['title']}",
                "",
                group["blurb"],
                "",
            ]
        )
        for category in categories:
            if category["group"] != group["id"]:
                continue
            n = sum(1 for bot in bots if bot["category"] == category["slug"])
            lines.append(
                f"- [**{category['title']}**](categories/{category['slug']}.md) ({n}) — {category['blurb']}"
            )
        lines.append("")
    lines.extend(['<a id="guides"></a>', "## Guides", ""])
    for path, title, blurb in GUIDES:
        lines.append(f"- [**{title}**]({path}) — {blurb}")
    lines.extend(
        [
            "",
            '<a id="contributing"></a>',
            "## Contributing",
            "",
            (
                "Append a bot to [`data/bots.yaml`](data/bots.yaml) and run `python scripts/generate.py`. "
                "[CONTRIBUTING.md](CONTRIBUTING.md) has the fields and how to suggest a bot."
            ),
            "",
            "Category pages are generated. Guides are written by hand. This list is released under [CC0](LICENSE).",
            "",
        ]
    )
    return "\n".join(lines)


def render_files(groups, categories, bots, quick, by_id):
    files = {
        ROOT / "README.md": render_readme(groups, categories, bots, quick, by_id),
    }
    for category in categories:
        path = ROOT / "categories" / f"{category['slug']}.md"
        files[path] = render_category(category, bots)
    return files


def write_files(files) -> None:
    categories_dir = ROOT / "categories"
    categories_dir.mkdir(parents=True, exist_ok=True)
    expected = {path.resolve() for path in files}
    for path in categories_dir.glob("*.md"):
        if path.resolve() not in expected:
            path.unlink()
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")


def check_files(files) -> list[str]:
    problems = []
    categories_dir = ROOT / "categories"
    expected_categories = {
        path.name for path in files if path.parent == categories_dir
    }
    if categories_dir.is_dir():
        for path in sorted(categories_dir.glob("*.md")):
            if path.name not in expected_categories:
                problems.append(f"unexpected category page: {path.relative_to(ROOT)}")
    for path, content in files.items():
        rel = path.relative_to(ROOT)
        if not path.is_file():
            problems.append(f"missing generated file: {rel}")
            continue
        disk = path.read_text(encoding="utf-8")
        if disk != content:
            diff = difflib.unified_diff(
                disk.splitlines(),
                content.splitlines(),
                fromfile=f"{rel} (committed)",
                tofile=f"{rel} (generated)",
                lineterm="",
            )
            preview = "\n".join(list(diff)[:120])
            problems.append(f"out of date: {rel}\n{preview}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate data and confirm generated files match, without writing",
    )
    args = parser.parse_args()
    data = load_data()
    errors, groups, categories, bots, by_id = validate(data)
    if errors:
        sys.stderr.write(f"{len(errors)} data error(s):\n")
        for error in errors:
            sys.stderr.write(f"- {error}\n")
        return 1
    files = render_files(groups, categories, bots, data["quick_start"], by_id)
    if args.check:
        problems = check_files(files)
        if problems:
            sys.stderr.write("Generated files are out of date. Run: python scripts/generate.py\n\n")
            sys.stderr.write("\n\n".join(problems))
            sys.stderr.write("\n")
            return 1
        print(f"OK: {len(bots)} bots, {len(files)} generated files, no duplicate links")
        return 0
    write_files(files)
    print(f"Wrote {len(files)} files for {len(bots)} bots")
    return 0


if __name__ == "__main__":
    sys.exit(main())
