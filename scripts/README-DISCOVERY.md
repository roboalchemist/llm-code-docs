# llms.txt Site Discovery

Automated discovery of llms.txt-compliant sites using multiple search APIs.

## Available Search APIs

The script uses all available API keys from your environment:

| API | Environment Variable | Features | Rate Limits (Free Tier) |
|-----|---------------------|----------|------------------------|
| **Brave Search** | `BRAVE_API_KEY` | Web search, pagination support | 1 query/second, 2,000/month |
| **Exa AI** | `EXA_API_KEY` | AI-powered search, up to 100 results | Varies by plan |
| **Tavily** | `TAVILY_API_KEY` | Research-focused search, up to 20 results | Varies by plan |
| **Serper** | `SERPER_API_KEY` | Google Search API, up to 100 results | Varies by plan (blocks some operators) |
| **GitHub CLI** | `gh` tool | Searches GitHub repositories and awesome lists | GitHub API limits apply |

## Usage

### Basic Usage

```bash
# Discover new sites with default settings
python3 scripts/discover-llms-txt-sites.py

# Limit results per API
python3 scripts/discover-llms-txt-sites.py --limit 20

# Control pagination depth (default: 5 pages per API)
python3 scripts/discover-llms-txt-sites.py --max-pages 3

# Custom output file
python3 scripts/discover-llms-txt-sites.py --output new-sites.json

# Custom search queries
python3 scripts/discover-llms-txt-sites.py --queries "llms.txt documentation" "llms-full.txt api"
```

### Default Queries

The script uses these queries by default:
1. `inurl:/llms.txt filetype:txt`
2. `llms-full.txt`
3. `llms.txt documentation`

### GitHub Search

The script automatically searches GitHub for:
- README files mentioning llms.txt
- Awesome lists (thedaviddias/llms-txt-hub, SecretiveShell/Awesome-llms-txt)
- Code containing llms.txt URLs

**Note:** Requires `gh` CLI tool to be installed and authenticated.

## Output

The script generates a JSON file (`discovered-llms-txt-sites.json` by default) containing:

```json
[
  {
    "url": "https://example.com/llms.txt",
    "title": "Example Site",
    "description": "Example documentation",
    "source": "brave",
    "base_url": "https://example.com/",
    "name": "example",
    "description": "Example documentation platform"
  }
]
```

### Fields

- `url`: Original llms.txt URL found
- `title`: Page title from search result
- `description`: Brief description from search
- `source`: Which API found this site (brave, exa, tavily, etc.)
- `base_url`: Extracted base URL (without /llms.txt)
- `name`: Generated kebab-case name for YAML config
- `description`: Cleaned up description for YAML

## Deduplication

The script automatically:
1. Loads existing sites from `llms-sites.yaml`
2. Filters out any sites already in the config
3. Deduplicates results across different search APIs
4. Normalizes URLs for comparison (removes www, trailing slashes, etc.)

## Integration with llms-sites.yaml

After running the discovery script, review the results and manually add promising sites to `llms-sites.yaml`:

```bash
# Run discovery
python3 scripts/discover-llms-txt-sites.py

# Review results
cat discovered-llms-txt-sites.json | jq '.[:10]'

# Manually add sites to llms-sites.yaml
# Then test with the scraper
python3 scripts/llms-txt-scraper.py --site new-site-name
```

## Rate Limiting

The script implements smart rate limiting to respect API limits:

### Brave Search (Free Tier)
- **Hard limit:** 1 query/second, 2,000 queries/month
- **Implementation:** 1.1 second delay between pagination requests
- **429 handling:** Gracefully stops pagination when rate limit hit

### Other APIs
- **Exa AI:** Rate limits vary by plan
- **Tavily:** Rate limits vary by plan
- **Serper:** Rate limits vary by plan, blocks `inurl:` and `filetype:` operators
- **GitHub CLI:** Respects GitHub API rate limits

### Script Delays
- 1 second delay between different search APIs
- 1.1 seconds between Brave pagination requests
- 0.5-1 second delays for GitHub API calls

To avoid hitting monthly limits on free tiers:
```bash
# Reduce max pages per query
python3 discover-llms-txt-sites.py --max-pages 1

# Use fewer queries
python3 discover-llms-txt-sites.py --queries "llms.txt"
```

## API Key Setup

To maximize results, ensure you have API keys configured:

```bash
# Check which keys are available
env | grep -i "api.*key\|key.*api" | cut -d= -f1

# Set missing keys in your shell rc file (~/.bashrc, ~/.zshrc)
export BRAVE_API_KEY="your-key-here"
export EXA_API_KEY="your-key-here"
export TAVILY_API_KEY="your-key-here"
export SERPER_API_KEY="your-key-here"
```

## Example Output

```
======================================================================
llms.txt Site Discovery
======================================================================
Output: discovered-llms-txt-sites.json
Queries: ['inurl:/llms.txt filetype:txt', 'llms-full.txt']

Loaded 75 existing sites from YAML

Query: 'inurl:/llms.txt filetype:txt'
----------------------------------------------------------------------
  Brave: Searching 'inurl:/llms.txt filetype:txt'...
    ✓ Found 18 results
  Exa: Searching 'inurl:/llms.txt filetype:txt'...
    ✓ Found 42 results
  Tavily: Searching 'inurl:/llms.txt filetype:txt'...
    ✓ Found 15 results
  Serper: Searching 'inurl:/llms.txt filetype:txt'...
    ⚠ Serper doesn't allow this query (contains restricted operators)

Searching GitHub repositories...
----------------------------------------------------------------------
  GitHub CLI: Searching for llms.txt files...
    ✓ Found 34 results

======================================================================
Processing Results
======================================================================
Total results found: 151
Unique new sites: 28

By source:
  brave: 6
  exa: 12
  github-cli: 5
  serper: 3
  tavily: 2

✓ Saved 28 new sites to discovered-llms-txt-sites.json

Top 10 discovered sites:
  1. notion (https://developers.notion.com/)
  2. replicate (https://replicate.com/docs/)
  3. anthropic (https://docs.anthropic.com/)
  ...
```

## Troubleshooting

### GitHub CLI not working

```bash
# Install gh CLI
# See: https://cli.github.com/

# Authenticate
gh auth login

# Test
gh search code "llms.txt" --limit 5
```

### Missing API keys

If an API key is not found, the script will skip that search source and continue with others.

### No results found

Try:
1. Different queries (`--queries "your custom query"`)
2. Higher limits (`--limit 100`)
3. Check API key validity
4. Verify network connectivity

## Advanced Usage

### Filter by source

After running, you can filter the JSON results:

```bash
# Show only GitHub results
jq '[.[] | select(.source == "github-cli")]' discovered-llms-txt-sites.json

# Show only new .ai domains
jq '[.[] | select(.base_url | contains(".ai/"))]' discovered-llms-txt-sites.json

# Count by source
jq '[.[] | .source] | group_by(.) | map({source: .[0], count: length})' discovered-llms-txt-sites.json
```

### Batch processing

```bash
# Run with multiple query sets
for query in "llms.txt ai" "llms.txt api" "llms.txt docs"; do
    python3 scripts/discover-llms-txt-sites.py \
        --queries "$query" \
        --output "discovered-${query// /-}.json"
    sleep 60  # Rate limiting between runs
done

# Merge results
jq -s 'add | unique_by(.base_url)' discovered-*.json > all-discovered.json
```

## Future Improvements

Potential enhancements:
- Direct scraping of llmstxt.site directory
- Sitemap parsing for large doc sites
- Domain pattern detection (docs.*, api.*, developers.*)
- Automatic validation of discovered sites (check if llms.txt actually exists)
- Integration with YAML updater (auto-add validated sites)
