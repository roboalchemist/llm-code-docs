# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/mget.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/mget.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/mget.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/mget.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON.MGET

> Get the same path from multiple JSON documents.

## Arguments

<ParamField body="keys" type="List[str]" required>
  One or more keys of JSON documents.
</ParamField>

<ParamField body="path" type="str" required>
  The path to get from the JSON document.
</ParamField>

## Response

<ResponseField type="List[List[TValue]]" required>
  The values at the specified path or `null` if the path does not exist.
</ResponseField>

<RequestExample>
  ```py Example theme={"system"}
  values = redis.json.mget(["key1", "key2"],  "$.path.to.somewhere")
  ```
</RequestExample>
