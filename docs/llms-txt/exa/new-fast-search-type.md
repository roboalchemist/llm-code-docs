# Source: https://exa.ai/docs/changelog/new-fast-search-type.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# New Fast Search Type

> Introducing Exa Fast: The world's fastest search API.

***

**Date: July 29, 2025**

We're excited to introduce **Exa Fast** - the fastest search API in the world. Exa Fast uses streamlined versions of our search models with p50 latency below 425ms.

<Info>
  Fast search is available immediately on all API plans. [Try Fast search in the dashboard →](https://dashboard.exa.ai/playground/search?q=blog%20post%20about%20AI\&filters=%7B%22text%22%3A%22true%22%2C%22type%22%3A%22fast%22%2C%22livecrawl%22%3A%22never%22%7D)
</Info>

## What's New

The Fast search type provides:

* **Speed**: p50 latency below 425ms - that's 30% faster than other search APIs
* **Exa Index**: Uses the same index of high quality content as our neural search
* **Customization**: Full compatibility with all the same parameters as our other search types

## When to Use Fast Search

Fast search is ideal for:

1. **Fast web grounding**: Integrate real-time web information into responses without sacrificing speed and impacting user experience
2. **Agentic workflows**: AI agents like deep research that use dozens or hundreds of search calls where milliseconds add up
3. **Low-latency AI products**: Latency-sensitive applications like AI voice companions where every millisecond matters

## How to Use Fast Search

Using Fast search is simple - just add `type="fast"` to your search requests:

<CodeGroup>
  ```python Python theme={null}
  result = exa.search_and_contents(
      "latest AI news",
      type="fast",
      livecrawl="never",
  )
  ```

  ```javascript JavaScript theme={null}
  const result = await exa.searchAndContents(
      "latest AI news",
      {
          type: "fast",
          livecrawl: "never"
      }
  );
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.exa.ai/search \
    -H "x-api-key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "latest AI news",
      "type": "fast",
      "livecrawl": "never"
    }'
  ```
</CodeGroup>

## Options That Impact Latency

While Fast search is optimized for speed, certain options can increase response times:

* **Live crawling**: Fetching content live requires real-time web requests. Set `livecrawl="never"` to use cached content and maintain optimal speed.
* **AI summaries**: Requesting AI-generated summaries requires LLM processing, which adds significant latency to your requests.
* **Complex date filters**: Using wide date ranges or multiple date constraints requires additional filtering that can slow down results.
* **Include/exclude text**: Text-based content filtering requires scanning through results, which impacts response times.
* **Subpages**: Including subpages in your search requires additional processing and can significantly increase latency.

For the fastest possible performance, use Fast search with minimal parameters and rely on cached content.
