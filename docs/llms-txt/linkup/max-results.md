# Source: https://docs.linkup.so/pages/changelog/max-results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# maxResults parameter

> _Released: November 14, 2025_

We're excited to introduce the new `maxResults` parameter for the `/search` endpoint, which allows you to specify the maximum number of search results returned in a single API call. This feature is designed to give you more control on the size of the context passed to downstream LLMs.

### How to Use

To specify a maximum number of search results, add the `maxResults` parameter to your API request.

**Example Request**

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
    "maxResults": 10
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
    max_results=10,
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
    maxResults: 10
  }).then(console.log);
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).