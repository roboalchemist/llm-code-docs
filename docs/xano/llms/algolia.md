# Source: https://docs.xano.com/xanoscript/function-reference/cloud-services/algolia.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Algolia

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> Algolia: Request

```js  theme={null}
cloud.algolia.request {
  application_id = ""
  api_key = ""
  url = ""
  method = "POST"
  payload =
} as x1
```

| Parameter       | Purpose                 | Example                          |    |
| --------------- | ----------------------- | -------------------------------- | -- |
| application\_id | Algolia application ID  | `"ABCDEF123456"`                 |    |
| api\_key        | Algolia API key         | `"1234567890abcdef"`             |    |
| url             | Algolia API endpoint    | `"/1/indexes/products/search"`   |    |
| method          | HTTP method for request | `"POST", "GET", "PUT", "DELETE"` |    |
| payload         | Request body data       | `{query: "search term"}`         |    |
| as              | Alias for response      | `x1, search_results`             | \\ |

<Accordion title="Example">
  ```js  theme={null}
  cloud.algolia.request {
    application_id = $env.ALGOLIA_APP_ID
    api_key = $env.ALGOLIA_API_KEY
    url = "/1/indexes/products/search"
    method = "POST"
    payload = {
      query: $input.search_term,
      hitsPerPage: 20,
      page: 0
    }
  } as search_response
  ```

  * Makes direct requests to Algolia API
  * Supports all Algolia endpoints
  * Flexible payload construction
  * Used for search, indexing, and management operations
  * Returns Algolia API response
</Accordion>


Built with [Mintlify](https://mintlify.com).