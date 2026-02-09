# Source: https://exa.ai/docs/changelog/february-2026-api-updates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Highlights, content freshness, and MCP updates

> New maxCharacters for highlights, maxAgeHours for content freshness control, and Exa MCP free tier limits.

***

**Date: February 2, 2026**

This release includes several improvements to give you more control over content extraction and search filtering.

## Highlights: maxCharacters Replaces numSentences

The `numSentences` parameter for highlights has been replaced with `maxCharacters`. This returns a single token-efficient excerpt from the page, ideal for agentic use cases where context overflow and latency matter.

<CodeGroup>
  ```python Python theme={null}
  result = exa.search_and_contents(
      "latest AI research",
      highlights={"max_characters": 2000}
  )
  ```

  ```javascript JavaScript theme={null}
  const result = await exa.searchAndContents(
      "latest AI research",
      {
          highlights: { maxCharacters: 2000 }
      }
  );
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.exa.ai/search \
    -H "x-api-key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "latest AI research",
      "contents": {
        "highlights": { "maxCharacters": 2000 }
      }
    }'
  ```
</CodeGroup>

## Content Freshness: maxAgeHours

The new `maxAgeHours` parameter in `/contents` gives you fine-grained control over content freshness:

* `maxAgeHours: 0` - Always livecrawl for fresh content
* `maxAgeHours: -1` - Cache only, never livecrawl
* `maxAgeHours: 24` - Use cache if content is less than 24 hours old, otherwise livecrawl

This replaces the boolean `livecrawl` options with more precise age-based control.

<CodeGroup>
  ```python Python theme={null}
  # Get content no older than 6 hours
  result = exa.get_contents(
    urls = ["tesla.com"],
    max_age_hours = 24,
    text = True
  )
  ```

  ```javascript JavaScript theme={null}
  // Get content no older than 6 hours
  const result = await exa.getContents(
      urls,
      { maxAgeHours: 6, text: true }
  );
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.exa.ai/contents \
    -H "x-api-key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "urls": ["https://example.com"],
      "maxAgeHours": 6
    }'
  ```
</CodeGroup>

## Exa MCP Free Tier Limits

Unauthenticated users can now try the Exa MCP for free with the following limits:

* **3 QPS** rate limit
* **150 free calls per day**

To exceed these limits, add your API key to unlock full access.

## Need Help?

If you have any questions about these updates, please reach out to [hello@exa.ai](mailto:hello@exa.ai).
