# llm-code-docs-writer Skill Reference

This file documents the path conventions and workflow for the `llm-code-docs` Claude skill.
It is a copy of the skill reference committed to the repo for discoverability.

Source of truth: `~/.claude/skills/llm-code-docs/` (symlinked from `~/gitea/jset/claude/skills/llm-code-docs/`)

---

## Repository Structure

Docs use a **library-centric** layout: `docs/{lib}/{source-type}/`

```
~/github/llm-code-docs/
├── docs/
│   └── {lib}/           # One directory per library
│       ├── llms/        # llms.txt content (HIGHEST PRIORITY)
│       ├── github/      # GitHub repo /docs extractions
│       ├── web/         # Custom scrapers (last resort)
│       ├── docs-rs/     # Rust crates (docs.rs)
│       ├── hexdocs/     # Elixir/Erlang (hexdocs.pm)
│       ├── go-native/   # Go modules (gomarkdoc)
│       ├── pkg-go-dev/  # Go packages (pkg.go.dev)
│       ├── readthedocs/ # Python (ReadTheDocs epub)
│       ├── rubydoc/     # Ruby gems (rubydoc.info)
│       └── javadoc/     # Java/JVM (javadoc.io)
├── scripts/             # Extraction and update tools
└── index.yaml           # Index of all sources
```

## Source Types

| Source Type | Target Directory | When to Use |
|------------|-----------------|-------------|
| `llms` | `docs/<name>/llms/` | Library has llms.txt — highest quality |
| `github` | `docs/<name>/github/` | GitHub repo with /docs folder |
| `docs-rs` | `docs/<name>/docs-rs/` | Rust crate on crates.io |
| `hexdocs` | `docs/<name>/hexdocs/` | Elixir/Erlang package on hex.pm |
| `go-native` | `docs/<name>/go-native/` | Go module (via gomarkdoc) |
| `pkg-go-dev` | `docs/<name>/pkg-go-dev/` | Go package (pkg.go.dev) |
| `readthedocs` | `docs/<name>/readthedocs/` | Python project on ReadTheDocs |
| `rubydoc` | `docs/<name>/rubydoc/` | Ruby gem (rubydoc.info) |
| `javadoc` | `docs/<name>/javadoc/` | Java/JVM library (javadoc.io) |
| `web` | `docs/<name>/web/` | Custom scraper — last resort |

## Workflow Summary

1. Check if already exists: `ls docs/ | grep -i "<topic>"`
2. Parallel discovery: Tavily search, registry APIs, GitHub search, domain cross-reference
3. Probe llms.txt on candidate domains
4. Decide using priority: llms >5KB > language-specific host > GitHub 5+ docs > web scraper
5. Fetch using the appropriate method (see fetch patterns below)
6. Validate with markdownlint (disabled: MD013 MD033 MD034 MD055 MD056 MD059 MD060)
7. Update index: `python3 scripts/update-index.py`
8. Commit and push to master

## Fetch Patterns

### llms

```bash
# 1. Add to scripts/llms-sites.yaml (alphabetical order):
#    - name: <project-name>
#      base_url: https://<domain>/
#      description: <brief description>
cd ~/github/llm-code-docs
python3 scripts/llms-txt-scraper.py --site <project-name>
ls -la docs/<project-name>/llms/
```

### github

```bash
# 1. Add to scripts/repo_config.yaml:
#    - name: <project-name>
#      repo_url: https://github.com/<owner>/<repo>
#      source_folder: docs/
#      target_folder: docs/<project-name>/github
#      branch: main
cd ~/github/llm-code-docs
python3 scripts/extract_docs.py
ls -la docs/<project-name>/github/
```

### web (last resort)

Create a scraper in `scripts/<project>-docs.py`. Output to `docs/<project>/web/`. All output must be Markdown.

### readthedocs (Python)

```bash
PROJECT="<project-name>"
mkdir -p ~/github/llm-code-docs/docs/$PROJECT/readthedocs
curl -sL "https://$PROJECT.readthedocs.io/_/downloads/en/stable/epub/" \
  -o /tmp/$PROJECT.epub
any2md /tmp/$PROJECT.epub ~/github/llm-code-docs/docs/$PROJECT/readthedocs/
```

### go-native (gomarkdoc)

```bash
MODULE="<module-path>"
SAFE=$(echo $MODULE | tr '/' '-')
git clone --depth=1 https://$MODULE /tmp/go-$SAFE
mkdir -p ~/github/llm-code-docs/docs/$SAFE/go-native
gomarkdoc /tmp/go-$SAFE/... > ~/github/llm-code-docs/docs/$SAFE/go-native/index.md
rm -rf /tmp/go-$SAFE
```

## Commit Format

```bash
git commit -m "Add <project> documentation

- Source: <source-type> (<url>)
- Files: <count> files"
```
