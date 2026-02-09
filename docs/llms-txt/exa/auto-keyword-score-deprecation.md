# Source: https://exa.ai/docs/changelog/auto-keyword-score-deprecation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Score Deprecation in Auto Search

> We're deprecating relevance scores in Auto search due to architectural improvements. Scores will remain available in Neural search.

***

**Date: July 21, 2025**

We're launching a big update to Auto search in our API. The new system cannot create useful scores for results. Because of this, we're removing scores from Auto search.

<Info>
  Scores in Neural search results will remain unchanged and continue to work exactly as before.
</Info>

## What Changed

Previously, Auto and Neural search types returned relevance scores - a number from 0 to 1 representing similarity between the query and each result. With our new Auto search architecture, we can no longer generate meaningful scores for Auto search results.

The search functionality works exactly the same way as it did before - you'll still get the same high-quality results, just without the `score` field in the response.

## What This Means for You

1. **Auto search**: The `score` field will no longer be returned in search results
2. **Neural search**: Scores continue to work exactly as before with no changes
3. **Migration needed**: If your application relies on scores from Auto search, you should migrate as soon as possible

## How to Update Your Code

If you currently use scores from Auto search, here is what you can do:

### Remove Score Dependencies

```python Python theme={null}
# Before: Code that depends on scores
result = exa.search("AI startups", type="auto")
sorted_results = sorted(result.results, key=lambda x: x.score, reverse=True)

# After: Use results in the order returned (already optimally ranked)
result = exa.search("AI startups", type="auto")
# Results are already ranked by relevance, no need to sort by score
for item in result.results:
    print(f"Title: {item.title}")
```

## Response Structure Changes

### Auto Search (New)

```json  theme={null}
{
  "results": [
    {
      "title": "Example AI Startup",
      "url": "https://example-startup.com",
      "id": "abc123",
      "publishedDate": "2024-01-15",
      "author": "John Doe"
      // Note: No 'score' field
    }
  ]
}
```

### Neural Search (Unchanged)

```json  theme={null}
{
  "results": [
    {

      "title": "Example AI Startup", 
      "url": "https://example-startup.com",
      "id": "abc123",
      "publishedDate": "2024-01-15",
      "author": "John Doe"
    }
  ]
}
```

## Need Help with Migration?

If you have questions about migrating from Auto search scores or need help determining the best search type for your use case, please reach out to [hello@exa.ai](mailto:hello@exa.ai). We're here to help ensure a smooth transition.
