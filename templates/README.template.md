# Claude Code field guide

{{header_line}}

One founder's field guide to running a company on Claude Code: the skills I install, the setups I copied, the rules I keep, and the people worth learning from. It is not a directory of everything that exists - if something is here, it earned its place in real work. Suggest a link by opening an issue (see [CONTRIBUTING.md](CONTRIBUTING.md)).

Descriptions are my own notes where I wrote one. Where I only saved a link, the description is the repository's or the post's own summary. Ratings like `(Matt: 8/10)` are my personal scores.

## Contents

{{toc}}

{{start_here}}

{{sections}}

## Other useful lists

This list is deliberately short and opinionated. When you want the exhaustive version, these are the ones I actually open:

- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - the reference directory for Claude Code itself: slash commands, hooks, status lines, tooling, plugins. Generated from a curated CSV, so it stays consistent. Go here when you want everything that exists, not just what one person kept.
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) - skills as a category, with the skill folders committed in the repo so you can read a SKILL.md before installing it. Useful for seeing how other people structure a skill.
- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) - a large catalogue of subagent definitions by domain. Worth a skim when you are designing an agent team and want prior art for the role split.

The difference is intent, not quality: those are directories of what exists, this is a record of what I kept after using it. If a link appears in both, theirs will be more complete and mine will tell you whether it survived contact with real work.

## How this list is built

The source is a private Notion page where I keep notes while I work. A sync script in my workspace (`awesome-sync.py`, not in this repo) reads that page through the Notion API and keeps only the sections that are explicitly mapped as public - everything else stays private by default. It canonicalizes every URL (https only, tracking parameters dropped, `youtu.be` and `twitter.com` rewritten), drops links to private places (Notion, Google Drive, course platforms), scans every string for secrets and private names, and writes three files: `data/links.csv` (one row per link), `data/notes.json` (the field notes) and `data/_report.md` (what was excluded and why).

From there everything is automated and reproducible from this repo alone:

- `tools/enrich.py` checks every link and writes `data/enrichment.json`: stars, license, last push and archive state from the GitHub API (renamed repositories are followed), titles from YouTube and X oEmbed, and a plain HTTP check with a browser user agent for everything else.
- `tools/build.py` renders this README from `data/` + `config/sections.json` + `templates/README.template.md`. Entries are sorted by name inside each section; the build is deterministic, so running it twice produces the same file.
- `tools/lint.py` fails on dead links, descriptions under 30 characters, duplicate names or URLs, non-https links, tracking parameters, links to private hosts, long dashes, placeholders, thin sections and broken table-of-contents anchors. Whatever it cannot fix on its own is listed under "Open decisions" in `data/_report.md`.
- A weekly GitHub Action (`.github/workflows/links.yml`) re-runs the checks and opens a pull request when the README changes. `data/_dead.md` lists what needs a human look.

Nothing in this README is edited by hand. Fixes go to `data/overrides.json` (keyed by the entry id in `data/links.csv`) and the next build picks them up.

{{stats}}

## License

The content of this list (README and the files in `data/`) is licensed under [CC BY 4.0](LICENSE) - share and adapt it with attribution. The scripts in `tools/` are MIT licensed ([LICENSE-CODE](LICENSE-CODE)).
