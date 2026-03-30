# Source: https://docs.linkup.so/pages/changelog/urlfiltering.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# URL Filtering

> _Released: jun 20, 2025_

We're excited to introduce URL filtering capabilities for your search results. This new feature allows you to exclude or obligate some URLs on your search results, making it easier to find the most relevant information.

### How to Enable

To filter your search results by URLs or domains, add the `excludeDomains` or `includeDomains` parameters to your API request.

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

The URLs filtering parameters accept an Array of strings. You can use:

* `excludeDomains`: Don't use those Domains/URLs in the results
* `includeDomains`: Only use those Domains/URLs in the results

<Warning>
  If you use `excludeDomains` and `includeDomains`, the results will logically only include Domains/URLs that match the inclusion.
</Warning>


Built with [Mintlify](https://mintlify.com).