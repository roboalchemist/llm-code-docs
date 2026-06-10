# Awesome Meta

Recursive discovery of all "awesome" lists on GitHub.

## Quick Results

From 11 seed repos, we discovered **846 unique awesome lists**:

**Primary seeds:**
- `sindresorhus/awesome` - The original comprehensive list
- `bayandin/awesome-awesomeness` - Meta-list of awesome lists

**Additional seeds:**
- `vinta/awesome-python`
- `avelino/awesome-go`
- `dzharii/awesome-typescript`
- `brillout/awesome-react-components`
- `awesome-selfhosted/awesome-selfhosted`
- `numetriclabz/awesome-db`
- `officialrajdeepsingh/awesome-nextjs`
- `bytefer/awesome-nextjs`
- `gribouille/awesome-python`

Results are in `output/`:
- `awesome_urls_from_seeds.txt` - Plain list of 846 URLs
- `awesome_from_seeds.json` - JSON with metadata
- `awesome_from_seeds.md` - Markdown formatted list

## Tools

### extract_local.py
Fast extraction from locally cloned repos:
```bash
python3 extract_local.py
```

### crawler.py
Recursive crawler that fetches READMEs from GitHub:
```bash
# Depth 1 (recommended, ~800 repos)
python3 crawler.py --max-depth 1 --delay 0.3

# Depth 2 (slower, may find a few more)
python3 crawler.py --max-depth 2 --delay 0.5
```

## How It Works

1. **Link Extraction**: Parse markdown files for GitHub repo links using regex
2. **Awesome Detection**: Filter to repos with "awesome", "curated", "list", etc. in name
3. **Deduplication**: Track visited repos to avoid cycles
4. **Recursive Crawl**: Fetch READMEs and extract more links up to max depth

## Key Finding

The two seed repos already comprehensively link to nearly all awesome lists. At depth 1, the crawler found zero new lists - they were all already referenced from the seeds. This means:

- **sindresorhus/awesome** is the definitive index
- Most awesome lists follow the convention of being listed there
- Recursive crawling beyond depth 0 has diminishing returns

## Stats

Top maintainers by number of awesome lists:
1. sindresorhus: 10 lists
2. benedekrozemberczki: 6 lists
3. kikobeats: 4 lists
4. kdeldycke: 4 lists
5. johnjago: 4 lists
