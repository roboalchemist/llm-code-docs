# Source: https://upstash.com/docs/vector/sdks/ts/commands/info.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/info.md

# Source: https://upstash.com/docs/vector/sdks/php/commands/info.md

# Source: https://upstash.com/docs/vector/api/endpoints/info.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/info.md

# Source: https://upstash.com/docs/search/sdks/py/commands/info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Info

## Info Command for Python SDK

Used to retrieve the stats of an index.

### Response

<ResponseField name="document_count" type="int" required>
  The total number of documents in the database, that are ready to use.
</ResponseField>

<ResponseField name="pending_document_count" type="int" required>
  The number of documents in the database, that are still processing and not ready to use.
</ResponseField>

<ResponseField name="disk_size" type="int" required>
  Size of the database in bytes.
</ResponseField>

<ResponseField name="indexes" required>
  Doctionary of index names and their information (`document_count` and `pending_document_count`)
</ResponseField>

<RequestExample>
  ```python  theme={"system"}
  from upstash_search import Search

  client = Search(
      url="<UPSTASH_SEARCH_REST_URL>",
      token="<UPSTASH_SEARCH_REST_TOKEN>",
  )

  info = client.info()
  print(info)
  ```
</RequestExample>
