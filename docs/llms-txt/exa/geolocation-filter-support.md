# Source: https://exa.ai/docs/changelog/geolocation-filter-support.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Geolocation Filter Support

> `userLocation` added to the search API to bias search results based on geographic location.

***

**Date: July 30, 2025**

We're excited to announce a new `userLocation` parameter that lets you bias search results based on a user's geographic region. The location is passed as an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code (e.g., "fr" for France, "us" for the United States).

If this field is provided, search will return results that are more relevant to users in the provided region.

## When to Use Geolocation Filter

The `userLocation` parameter is particularly useful for:

1. **Multi-regional applications**: Show users content that's relevant to their region
2. **Language-specific content**: Prioritizing content in regional languages
3. **Local discovery**: Surface products or businesses relevant to the users region

Consider using geolocation filtering when the user's physical location or regional context significantly impacts the relevance of search results.

## How To Use Geolocation Filter

Here's how to implement the new `userLocation` parameter:

<CodeGroup>
  ```python Python theme={null}
  result = exa.search_and_contents(
      "football rules",
      type="auto",
      livecrawl="never",
      userLocation="us", # ISO 3166-1 alpha-2 country code
      num_results=10
  )
  ```

  ```javascript JavaScript theme={null}
  const result = await exa.searchAndContents(
      "football rules",
      {
          type: "auto",
          livecrawl: "never",
          userLocation: "us", // ISO 3166-1 alpha-2 country code
          numResults: 10
      }
  );
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.exa.ai/search \
    -H "x-api-key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "football rules",
      "type": "auto",
      "userLocation": "us",
      "numResults": 10
    }'
  ```
</CodeGroup>

## Response Structure Changes

The response structure remains unchanged - geolocation filtering affects result ranking and relevance scoring, but doesn't modify the response format.

## Need Help?

If you have any questions about location filtering or need help with your specific use case, please reach out to [hello@exa.ai](mailto:hello@exa.ai).
