# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/strlen.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/strlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/strlen.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/strlen.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON.STRLEN

> Report the length of the JSON String at path in key

## Arguments

<ParamField body="key" type="str" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="str" required>
  The path of the string. `$` is the root.
</ParamField>

## Response

<ResponseField type="List[int]" required>
  The length of the string at the path.
</ResponseField>

<RequestExample>
  ```py Example theme={"system"}
  redis.json.strlen("key", "$.path.to.str")
  ```
</RequestExample>
