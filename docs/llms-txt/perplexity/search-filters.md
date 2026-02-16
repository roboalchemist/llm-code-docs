# Search Filters
Source: https://docs.perplexity.ai/docs/sonar/filters

Control and customize Sonar API search results with filters

Control which websites appear in search results, filter by date and location, target specific languages, and fine-tune search behavior using Sonar API filters.

## Domain Filters

Control which websites are included or excluded from search results using `search_domain_filter`. Supports both domain-level and URL-level filtering.

**Key parameters:**

* `search_domain_filter`: Array of domains or URLs (max 20)
* **Allowlist mode**: Include only specified domains (no prefix)
* **Denylist mode**: Exclude domains (prefix with `-`)

```python theme={null}
from perplexity import Perplexity

client = Perplexity()
