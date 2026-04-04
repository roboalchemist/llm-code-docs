# Source: https://upstash.com/docs/vector/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/reset.md

# Source: https://upstash.com/docs/vector/sdks/php/commands/reset.md

# Source: https://upstash.com/docs/vector/api/endpoints/reset.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/search/sdks/py/commands/reset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reset

## Reset Command for Python SDK

The `reset` method allows you to clear all documents from a particular index.

### Response

<ResponseField name="Response" type="string" required>
  `'Success'` if the database is successfully reset.
</ResponseField>

<RequestExample>
  ```python  theme={"system"}
  from upstash_search import Search

  client = Search(
      url="<UPSTASH_SEARCH_REST_URL>",
      token="<UPSTASH_SEARCH_REST_TOKEN>",
  )

  index = client.index("movies")
  index.reset()
  ```
</RequestExample>
