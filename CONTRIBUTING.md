# Contributing

This list is opinionated on purpose. It is not a directory of everything that exists - it is what one founder actually uses or would send to another founder.

## Suggesting a link

Open an issue. One link per issue. The issue must say:

1. The URL (a GitHub repo, a video, a post, a doc - anything public and stable).
2. What it is, in one plain sentence.
3. Why it earned its place: what did it change in how you build, ship or run a company with Claude Code? "It is popular" is not a reason. "It cut my review time in half because X" is.
4. Which section it belongs to (see the README table of contents).

Links that will not be accepted: paywalled course material, affiliate or tracking links, anything that requires a login to read, and tools that have not been used for real work.

## Fixing a description or a dead link

The README is generated - do not edit it directly, the next build overwrites it.

- Wrong or weak name/description: add an entry to `data/overrides.json` keyed by the entry `id` from `data/links.csv`:

  ```json
  {"1a2b3c4d": {"name": "Better name", "description": "One honest sentence about what it does."}}
  ```

- Dead link with a known new home: set `"url"` in the same override (the id stays the same until the next sync).
- Then run `python3 tools/build.py && python3 tools/lint.py` and open a pull request with the diff.

## Style

Plain hyphen `-` only, never em or en dashes. Short sentences. No hype words. Describe what the thing does, not how amazing it is.

## License

Content contributions are accepted under CC BY 4.0, code under MIT (see `LICENSE` and `LICENSE-CODE`).
