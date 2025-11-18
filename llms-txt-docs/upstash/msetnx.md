# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/msetnx.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/msetnx.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/msetnx.md

# MSETNX

> Set multiple keys in one go unless they exist already.

For billing purposes, this counts as a single command.

## Arguments

<ParamField type="Record<string, TValue>" required>
  An object where the keys are the keys to set, and the values are the values to set.
</ParamField>

## Response

<ResponseField required>
  `True` if all keys were set, `False` if at least one key was not set.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  redis.msetnx({
    "key1": "value1",
    "key2": "value2"
  })
  ```
</RequestExample>
