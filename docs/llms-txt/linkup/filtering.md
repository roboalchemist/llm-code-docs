# Source: https://docs.linkup.so/pages/documentation/development/filtering.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Source Filtering

> How to filter your search on sources.

<Info>
  **Date filtering** information can be found [here](../api-reference/endpoint/post-search#body-from-date).
</Info>

## Overview

You can fine-tune your search results by:

* **including**
* **excluding**
* **prioritizing**

specific domains or URLs, ensuring more control over where your answers are retrieved from.

<Warning>
  If you use `excludeDomains` and `includeDomains`, the results will logically only include URLs that match the inclusion.
</Warning>

### Exclude Domains/URLs

To filter your search results by exclusively excluding some URLs or domains, you can add the `excludeDomains` parameter to your API request. Currently, the parameter supports up to 50 URLs to exclude.

**Example Request with excludeDomains**

<CodeGroup>
  ```shell curl theme={null}
  curl --request POST \
    --url https://api.linkup.so/v1/search \
    --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
    --header 'Content-Type: application/json' \
    --data '{
    "q": "Latest developments in AI",
    "depth": "standard",
    "outputType": "sourcedAnswer",
    "excludeDomains": ["apple.com"]
  }'
  ```

  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="{{LINKUP_API_KEY}}")

  query = """Latest developments in AI"""

  search_response = client.search(
    query=query,
    depth="standard",
    output_type="sourcedAnswer",
    exclude_domains=["apple.com"]
  )
  print(search_response)
  ```

  ```javascript js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '{{LINKUP_API_KEY}}',
  });

  const query = `Latest developments in AI`;

  client.search({
    query,
    depth: "standard",
    outputType: "sourcedAnswer",
    excludeDomains: ["apple.com"]
  }).then(console.log);
  ```
</CodeGroup>

**Example Response**

```json  theme={null}
{
  "answer": "AI agents are the dominant innovation in 2025, focusing on autonomous AI programs that can independently complete projects...",
  "sources": [
    {
      "name": "AI Agents in 2025: Expectations vs. Reality | IBM",
      "snippet": "For 2025, the dominant innovation narrative is the AI agent...",
      "url": "https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality"
    }
  ]
}
```

### Include Domains/URLs

To filter your search results by exclusively consulting some URLs or domains, you can add the `includeDomains` parameter to your API request. Currently, the parameter supports up to 50 URLs to include.

**Example Request with includeDomains**

<CodeGroup>
  ```shell curl theme={null}
  curl --request POST \
    --url https://api.linkup.so/v1/search \
    --header 'Authorization: Bearer {{LINKUP_API_KEY}}' \
    --header 'Content-Type: application/json' \
    --data '{
    "q": "How to build MCP server",
    "depth": "standard",
    "outputType": "sourcedAnswer",
    "includeDomains": ["dev.to"]
  }'
  ```

  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="{{LINKUP_API_KEY}}")

  query = """How to build MCP server?"""

  search_response = client.search(
    query=query,
    depth="standard",
    output_type="sourcedAnswer",
    include_domains=["dev.to"]
  )
  print(search_response)
  ```

  ```javascript js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '{{LINKUP_API_KEY}}',
  });

  const query = `How to build MCP server?`;

  client.search({
    query,
    depth: "standard",
    outputType: "sourcedAnswer",
    includeDomains: ["dev.to"]
  }).then(console.log);
  ```
</CodeGroup>

**Example Response**

```json  theme={null}
{
  "answer": "Steps to build an MCP server in 2025:[...]",
  "sources": [
    {
      "name": "🚀Top 10 MCP Servers for 2025 (Yes, GitHub’s Included!) - DEV Community",
      "snippet": "Enter the Model Context Protocol ... ",
      "url": "https://dev.to/fallon_jimmy/top-10-mcp-servers-for-2025-yes-githubs-included-15jg"
    }
  ]
}
```

### Prioritize Domains

To **Prioritize** some domains, you can use the `<guidance>` XML structure in your query.

**Example Request with Prioritize**

<CodeGroup>
  ```bash curl theme={null}
  curl -X POST 'https://api.linkup.so/v1/search' \
    -H 'Authorization: Bearer {{LINKUP_API_KEY}}' \
    -H 'Content-Type: application/json' \
    -d '{
      "q": "<guidance>Use only the sources listed here. Do not rely on any external references.\n  - wikipedia.org\n  - lvmh.com\n<priority>\n  - wikipedia.org\n</priority></guidance>Who is the CEO of LVMH?",
      "outputType": "sourcedAnswer",
      "depth": "standard"
    }'
  ```

  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="{{LINKUP_API_KEY}}")

  query = """
  <guidance>
  Use only the sources listed here. Do not rely on any external references.
      - wikipedia.org
      - lvmh.com
    <priority>
      - wikipedia.org
    </priority>
  </guidance>
  Who is the CEO of LVMH?
  """

  search_response = client.search(
    query=query,
    depth="standard",
    output_type="sourcedAnswer"
  )
  print(search_response)
  ```

  ```javascript js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '{{LINKUP_API_KEY}}',
  });

  const query = `
  <guidance>
      Use only the sources listed here. Do not rely on any external references.
      - wikipedia.org
      - lvmh.com
    <priority>
      - wikipedia.org
    </priority>
  </guidance>
  Who is the CEO of LVMH?`;

  client.search({
    query,
    depth: "standard",
    outputType: "sourcedAnswer"
  }).then(console.log);
  ```
</CodeGroup>

**Example Response**

```json  theme={null}
{
  "answer": "The CEO of LVMH is Bernard Arnault.",
  "sources": [
    {
      "name": "Actual CEO of LVMH",
      "url": "https://www.wikipedia.org/wiki/lvmh",
      "snippet": "LVMH Moët Hennessy Louis Vuitton SE, commonly known as LVMH, is a French multinational luxury goods conglomerate. The current CEO is Bernard Arnault."
    },
    {
      "name": "The CEO of LVMH is Bernard Arnault",
      "url": "https://lvmh.com/about-us",
      "snippet": "Bernard Arnault is the CEO of LVMH, a leading luxury goods company. Under his leadership, LVMH has seen significant growth and expansion in the luxury market."
    }
  ]
}
```


Built with [Mintlify](https://mintlify.com).