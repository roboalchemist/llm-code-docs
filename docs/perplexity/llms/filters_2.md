# Source: https://docs.perplexity.ai/docs/sonar/filters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Filters

> Control and customize Sonar API search results with filters

Control which websites appear in search results, filter by date and location, target specific languages, and fine-tune search behavior using Sonar API filters.

## Domain Filters

Control which websites are included or excluded from search results using `search_domain_filter`. Supports both domain-level and URL-level filtering.

**Key parameters:**

* `search_domain_filter`: Array of domains or URLs (max 20)
* **Allowlist mode**: Include only specified domains (no prefix)
* **Denylist mode**: Exclude domains (prefix with `-`)

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

# Allowlist: Only search specific domains
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Tell me about space discoveries."}],
    search_domain_filter=["nasa.gov", "wikipedia.org", "space.com"]
)

# Denylist: Exclude specific domains
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "What are renewable energy advances?"}],
    search_domain_filter=["-reddit.com", "-pinterest.com"]
)
```

<Warning>
  You can add a maximum of 20 domains or URLs. Use either allowlist OR denylist mode, not both simultaneously.
</Warning>

## Date & Time Filters

Filter search results by publication date, last updated date, or recency using date range parameters.

**Key parameters:**

* `search_after_date_filter`: Filter by publication date (format: `%m/%d/%Y`)
* `search_before_date_filter`: Filter by publication date (format: `%m/%d/%Y`)
* `last_updated_after_filter`: Filter by last updated date
* `last_updated_before_filter`: Filter by last updated date
* `search_recency_filter`: Predefined periods (`"day"`, `"week"`, `"month"`, `"year"`)

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

# Publication date range
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Show me tech news from this week."}],
    search_after_date_filter="3/1/2025",
    search_before_date_filter="3/5/2025"
)

# Last updated date range
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Show me recently updated articles."}],
    last_updated_after_filter="3/1/2025",
    last_updated_before_filter="3/5/2025"
)

# Recency filter (convenient relative dates)
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Latest AI developments?"}],
    search_recency_filter="week"
)
```

<Info>
  Date filters must use `%m/%d/%Y` format (e.g., `"3/1/2025"`). `search_recency_filter` cannot be combined with other date filters.
</Info>

## Location Filters

Customize search results based on geographic location using `user_location` within `web_search_options`.

**Key parameters:**

* `country`: Two-letter ISO 3166 country code (required with coordinates)
* `region`: State, province, or administrative division
* `city`: City name
* `latitude`: Latitude coordinate (-90 to 90)
* `longitude`: Longitude coordinate (-180 to 180)

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

# Full location specification (recommended)
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "What are good coffee shops nearby?"}],
    web_search_options={
        "user_location": {
            "country": "US",
            "region": "California",
            "city": "San Francisco",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    }
)

# Country code only
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Summarize today's news."}],
    web_search_options={
        "user_location": {
            "country": "US"
        }
    }
)
```

<Tip>
  For best accuracy, provide as many location fields as possible. City and region significantly improve location precision.
</Tip>

## Language Filter

Filter search results by language using ISO 639-1 language codes.

**Key parameters:**

* `search_language_filter`: Array of 2-letter language codes (max 10)

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

# Single language
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Tell me about AI developments."}],
    search_language_filter=["en"]
)

# Multiple languages
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Renewable energy in Europe?"}],
    search_language_filter=["en", "fr", "de"]
)
```

<Info>
  Language codes must be valid ISO 639-1 codes (e.g., `"en"`, `"fr"`, `"de"`). You can filter by up to 10 languages per request.
</Info>

## Academic Filter

Prioritize scholarly sources and peer-reviewed content by setting `search_mode` to `"academic"`.

**Key parameters:**

* `search_mode`: Set to `"academic"` to target academic sources

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "What is the scientific name of lion's mane mushroom?"}],
    search_mode="academic",
    web_search_options={"search_context_size": "low"}
)

# Combine with date filters for recent research
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Latest findings on neural networks?"}],
    search_mode="academic",
    search_after_date_filter="1/1/2023"
)
```

## SEC Filings Filter

Target U.S. Securities and Exchange Commission filings and official financial documents.

**Key parameters:**

* `search_mode`: Set to `"sec"` to target SEC filings

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Prepare me for markets opening."}],
    search_mode="sec"
)

# Combine with date filters for recent filings
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Summarize latest 10-K filings for Apple Inc."}],
    search_mode="sec",
    search_after_date_filter="1/1/2023"
)
```

## Context Size Control

Control how much search context is retrieved to balance cost and comprehensiveness.

**Key parameters:**

* `search_context_size`: Set to `"low"` (default), `"medium"`, or `"high"` within `web_search_options`

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

# Low context (cost-efficient, default)
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "How many stars in our galaxy?"}],
    web_search_options={"search_context_size": "low"}
)

# High context (comprehensive)
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Explain the 2008 financial crisis."}],
    web_search_options={"search_context_size": "high"}
)
```

<Warning>
  Selecting `"high"` increases search costs due to more extensive web retrieval. Use `"low"` when cost efficiency is critical.
</Warning>

## Search Control

Control when web search is performed using the search classifier or by disabling search entirely.

**Key parameters:**

* `enable_search_classifier`: Let AI decide when to search (boolean)
* `disable_search`: Disable web search completely (boolean)

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

# Search classifier (AI decides when to search)
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "What are latest quantum computing developments?"}],
    enable_search_classifier=True
)

# Disable search completely
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "What is 2 + 2?"}],
    disable_search=True
)
```

<Warning>
  Pricing remains the same regardless of whether search is triggered. Search control is for performance optimization, not cost reduction.
</Warning>

## Combining Filters

You can combine multiple filters for precise control over search results:

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

# Combine domain, language, date, and context size filters
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Recent quantum computing breakthroughs?"}],
    search_domain_filter=["nature.com", "science.org", "arxiv.org"],
    search_language_filter=["en", "de"],
    search_recency_filter="month",
    web_search_options={"search_context_size": "high"}
)
```

## Next Steps

<Card title="Sonar Quickstart" icon="rocket" href="/docs/sonar/quickstart">
  Get started with the Sonar API and learn the basics
</Card>


Built with [Mintlify](https://mintlify.com).