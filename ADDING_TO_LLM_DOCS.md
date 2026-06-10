# Using Awesome Lists to Expand llm-code-docs

## Purpose

**We are NOT adding awesome lists themselves to llm-code-docs.**

Awesome lists are **discovery tools** - curated indexes that point to high-quality projects. We use them to find things we should grab documentation for.

```
Awesome Lists → Discover Projects → Add Project Docs to llm-code-docs
     ↓                  ↓                      ↓
  (seed)            (filter)              (target)
```

## The Pipeline

### Step 1: Crawl Awesome Lists
Extract all linked projects from awesome lists:
- 846 awesome lists discovered
- Thousands of project links within them
- Each link is a potential documentation source

### Step 2: Filter for Documentation Sources
Not every linked project has docs worth adding. Filter for:
- Projects with llms.txt support (priority 1)
- Projects with comprehensive `/docs` folders (priority 2)
- Projects with detailed READMEs (priority 3)

### Step 3: Add to llm-code-docs
Add qualifying projects using existing llm-code-docs patterns:
- `docs/llms-txt/{project}/` - If site has llms.txt
- `docs/github-scraped/{project}/` - If repo has good docs folder
- `docs/web-scraped/{project}/` - If needs custom scraping

## Example Workflow

```
awesome-python
    ├── Links to FastAPI → Already in llm-code-docs ✓
    ├── Links to Textual → Already in llm-code-docs ✓
    ├── Links to Pydantic → Check for llms.txt... add if found
    ├── Links to Rich → Check docs/ folder... add if good
    └── Links to Typer → Check docs/ folder... add if good

awesome-go
    ├── Links to Fiber → Check for llms.txt...
    ├── Links to Gin → Check docs/ folder...
    └── ...
```

## What We're Building

### 1. Project Extractor
Script to extract all project URLs from awesome list READMEs:
```python
# Input: awesome-python README
# Output: List of project URLs
[
    "https://github.com/tiangolo/fastapi",
    "https://github.com/pallets/flask",
    "https://github.com/django/django",
    ...
]
```

### 2. Documentation Checker
Script to check each project for documentation availability:
```python
# For each project URL, check:
# 1. Does {docs-url}/llms.txt exist?
# 2. Does repo have /docs folder with .md/.rst files?
# 3. Is README substantial enough?
```

### 3. Candidate Reporter
Generate report of projects worth adding:
```markdown
## High Priority (llms.txt available)
- pydantic: https://docs.pydantic.dev/llms.txt ✓
- httpx: https://www.python-httpx.org/llms.txt ✓

## Medium Priority (good docs folder)
- rich: github.com/Textualize/rich/docs/ (15 .md files)
- typer: github.com/tiangolo/typer/docs/ (23 .md files)

## Already in llm-code-docs
- fastapi ✓
- flask ✓
- textual ✓
```

## Coverage Analysis

Current llm-code-docs has 328 sources. By mining awesome lists, we can:

1. **Find gaps** - Popular projects not yet in llm-code-docs
2. **Prioritize additions** - Focus on most-linked projects
3. **Discover llms.txt sites** - Many may have added support recently
4. **Track ecosystem** - Keep llm-code-docs comprehensive

## Data We Collect

From each awesome list:
```yaml
source: awesome-python
projects:
  - name: FastAPI
    url: https://github.com/tiangolo/fastapi
    docs_url: https://fastapi.tiangolo.com
    category: Web Frameworks
    in_llm_docs: true

  - name: Pydantic
    url: https://github.com/pydantic/pydantic
    docs_url: https://docs.pydantic.dev
    category: Data Validation
    in_llm_docs: false
    has_llms_txt: true  # ← This is a candidate!
```

## Next Steps

1. **Extract projects** - Parse all 846 awesome lists for project URLs
2. **Deduplicate** - Many projects appear in multiple lists
3. **Check coverage** - Compare against existing llm-code-docs sources
4. **Check llms.txt** - Probe each project's docs site for llms.txt
5. **Generate candidates** - List of projects to add, prioritized
6. **Update configs** - Add candidates to llms-sites.yaml or repo_config.yaml

## Output Files

```
awesome-meta/
├── output/
│   ├── all_projects.json        # Every project from awesome lists
│   ├── candidates.json          # Projects worth adding
│   ├── has_llms_txt.json        # Projects with llms.txt support
│   ├── has_docs_folder.json     # Projects with good docs/
│   └── coverage_report.md       # Gap analysis vs llm-code-docs
```

## Summary

Awesome lists = **seed data** for finding things to grab documentation for.

We use them to systematically discover projects worth documenting, then fetch their docs for llm-code-docs - prioritizing those with llms.txt support or comprehensive documentation folders.
