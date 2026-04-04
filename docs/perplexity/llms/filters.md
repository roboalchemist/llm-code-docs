# Source: https://docs.perplexity.ai/docs/agent-api/filters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Filters

> Control and customize Agent API search results with filters

Control which search results are returned by applying filters to your web search queries. Filters help you focus on specific domains, time periods, or geographic locations to get more relevant results.

## Domain Filters

Domain filters allow you to include or exclude specific domains or URLs from search results. Use allowlist mode to restrict results to trusted sources, or denylist mode to filter out unwanted domains.

<Warning>
  You can add a maximum of 20 domains or URLs to the `search_domain_filter` list. The filter works in either allowlist mode (include only) or denylist mode (exclude), but not both simultaneously.
</Warning>

**Allowlist mode**: Include only the specified domains/URLs (no `-` prefix)\
**Denylist mode**: Exclude the specified domains/URLs (use `-` prefix)

You can filter at the domain level (e.g., `wikipedia.org`) or URL level (e.g., `https://en.wikipedia.org/wiki/Chess`) for granular control.

```python Python theme={null}
from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    preset="fast-search",
    input="Tell me about the James Webb Space Telescope discoveries.",
    instructions="You are a helpful assistant.",
    tools=[
        {
            "type": "web_search",
            "filters": {
                "search_domain_filter": [
                    "nasa.gov",
                    "wikipedia.org",
                    "space.com"
                ]
            }
        }
    ]
)

print(response.output_text)
```

## Date & Time Filters

Date and time filters help you find content published or updated within specific time periods. You can filter by publication date, last updated date, or use recency filters for relative time periods.

**Publication date filters**: Filter by when content was originally published

* `search_after_date_filter`: Include content published after this date
* `search_before_date_filter`: Include content published before this date

**Last updated filters**: Filter by when content was last modified

* `last_updated_after_filter`: Include content updated after this date
* `last_updated_before_filter`: Include content updated before this date

**Recency filter**: Filter by relative time periods

* `search_recency_filter`: Use `"day"`, `"week"`, `"month"`, or `"year"` for content from the past 24 hours, 7 days, 30 days, or 365 days

<Info>
  Specific date filters must be provided in the "%m/%d/%Y" format (e.g., "3/1/2025"). Recency filters use predefined values like "day", "week", "month", or "year".
</Info>

```python Python theme={null}
from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    preset="pro-search",
    input="What are the latest AI developments?",
    instructions="You are an expert on current events.",
    tools=[
        {
            "type": "web_search",
            "filters": {
                "search_recency_filter": "week"
            }
        }
    ]
)

print(response.output_text)
```

## Location Filters

Location filters tailor search results based on geographic context. This is useful for finding local businesses, regional news, or location-specific information.

You can specify location using:

* **Country code**: Two-letter ISO 3166-1 alpha-2 code (e.g., `"US"`, `"FR"`)
* **City and region**: Improve accuracy with city and region names
* **Coordinates**: Latitude and longitude for precise location targeting

<Tip>
  The `city` and `region` fields significantly improve location accuracy. We strongly recommend including them alongside coordinates and country code for the best results.
</Tip>

<Warning>
  Latitude and longitude must be provided alongside the country parameter—they cannot be provided on their own.
</Warning>

```python Python theme={null}
from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    preset="pro-search",
    input="What are some good coffee shops nearby?",
    instructions="You are a helpful local guide.",
    tools=[
        {
            "type": "web_search",
            "user_location": {
                "country": "US",
                "region": "California",
                "city": "San Francisco",
                "latitude": 37.7749,
                "longitude": -122.4194
            }
        }
    ]
)

print(response.output_text)
```

## Combining Filters

You can combine multiple filter types in a single request to create highly targeted searches. For example, you might restrict results to specific domains published within a recent time period, or filter by location and date range together.

```python Python theme={null}
from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    preset="pro-search",
    input="Latest tech news from trusted sources.",
    instructions="You are an expert on technology.",
    tools=[
        {
            "type": "web_search",
            "filters": {
                "search_domain_filter": ["techcrunch.com", "theverge.com"],
                "search_recency_filter": "week"
            },
            "user_location": {
                "country": "US"
            }
        }
    ]
)

print(response.output_text)
```

## Next Steps

<CardGroup cols={2}>
  <Card title="Agent API Quickstart" icon="rocket" href="/docs/agent-api/quickstart">
    Get started with the Agent API.
  </Card>

  <Card title="Models" icon="brain" href="/docs/agent-api/models">
    Explore direct model selection and third-party models.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).