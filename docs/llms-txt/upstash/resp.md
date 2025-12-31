# Source: https://upstash.com/docs/redis/sdks/py/commands/json/resp.md

# JSON.RESP

> Return the value at the path in Redis serialization protocol format.

## Arguments

<ParamField body="key" type="str" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="str" default="$">
  The path of the object.
</ParamField>

## Response

<ResponseField type="TValue" required>
  Return the value at the path in Redis serialization protocol format.
</ResponseField>

<RequestExample>
  ```py Example theme={"system"}
  resp = redis.json.resp("key", "$.path")
  ```
</RequestExample>
