# _meta.yaml Schema

Each library directory under `docs/{source-type}/{library}/` may contain a `_meta.yaml` file
that describes the library, its documentation sources, and quality metadata.

## File Location

```
docs/
  llms-txt/
    slack/
      _meta.yaml    <-- per-library metadata
      ...
  github-scraped/
    tornado/
      _meta.yaml
      ...
  web-scraped/
    apple-developer-docs/
      _meta.yaml
      ...
```

## Schema

```yaml
# _meta.yaml schema - one per library in docs/{source-type}/{library}/
name: string           # library identifier (matches directory name)
primary_source: enum   # llms | github | web
sources:               # all sources fetched for this library
  - type: llms | github | web
    url: string        # source URL
    last_fetched: ISO8601 datetime
description: string    # human-readable description of the library
quality_score: int     # 0-100, computed by scripts/quality-check.py
```

## Field Descriptions

### `name`

**Type:** string
**Required:** yes

The library identifier. Must match the directory name exactly. Used as the canonical
identifier for cross-referencing in `index.yaml` and search indexes.

Example: `slack`, `tornado`, `apple-developer-docs`

### `primary_source`

**Type:** enum
**Required:** yes
**Values:** `llms` | `github` | `web`

The primary documentation source type:

| Value | Description |
|-------|-------------|
| `llms` | Fetched via `llms.txt` protocol from the library's official site |
| `github` | Scraped from a GitHub repository's docs folder |
| `web` | Scraped from a web URL via HTTP crawler |

When a library has multiple sources, `primary_source` indicates the most authoritative one.

### `sources`

**Type:** list of source objects
**Required:** yes
**Min length:** 1

Each source object has the following fields:

#### `sources[].type`

**Type:** enum (`llms` | `github` | `web`)

The source type for this entry. Matches the `primary_source` enum values.

#### `sources[].url`

**Type:** string (URL)

The URL from which documentation was fetched:
- For `llms`: the base URL of the site (e.g., `https://docs.slack.dev/`)
- For `github`: the GitHub repository URL (e.g., `https://github.com/tornadoweb/tornado`)
- For `web`: the root URL of the scraped site or page

#### `sources[].last_fetched`

**Type:** string (ISO 8601 datetime)
**Format:** `YYYY-MM-DDTHH:MM:SSZ`

Timestamp of the most recent successful fetch for this source.

### `description`

**Type:** string
**Required:** yes

A human-readable description of the library. Should be 1-3 sentences describing what the
library does and its primary use case. This field is surfaced in search results and the
web UI.

### `quality_score`

**Type:** integer
**Required:** yes
**Range:** 0-100

A quality score computed by `scripts/quality-check.py`. Higher scores indicate better
documentation quality. The scoring rubric considers:

- Completeness (coverage of major topics)
- Formatting (valid markdown, code blocks with language tags)
- Content density (meaningful prose vs. boilerplate)
- Link health (no broken internal references)

Scores are recomputed when documentation is re-fetched.

## Validation Rules

1. `name` must match the parent directory name.
2. `primary_source` must match the `type` of exactly one entry in `sources`.
3. All `last_fetched` values must be valid ISO 8601 datetimes.
4. `quality_score` must be in the range 0-100 inclusive.
5. Each entry in `sources` must have a non-empty `url`.

## Notes

- `_meta.yaml` files are created and updated automatically by the fetch scripts.
- Manual edits to `description` and `quality_score` are preserved across re-fetches.
- Libraries with multiple source types (e.g., both `llms` and `github`) list all sources
  but designate one as `primary_source`.
- The `_meta.yaml` schema is intentionally minimal; additional fields may be added in
  future schema versions with a `schema_version` field.
