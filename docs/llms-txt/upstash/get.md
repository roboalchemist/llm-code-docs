# Source: https://upstash.com/docs/workflow/rest/flow-control/get.md

# Source: https://upstash.com/docs/workflow/rest/dlq/get.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/get.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/get.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/get.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON.GET

> Get a single value from a JSON document.

## Arguments

<ParamField body="key" type="str" required>
  The key of the json entry.
</ParamField>

<ParamField body="paths" type="*List[str]" required>
  One or more paths to retrieve from the JSON document. `$` is the root.
</ParamField>

## Response

<ResponseField type="List[TValue | null]" required>
  The value at the specified path or `null` if the path does not exist.
</ResponseField>

<RequestExample>
  ```py Example theme={"system"}
  value = redis.json.get("key", "$.path.to.somewhere")
  ```
</RequestExample>
