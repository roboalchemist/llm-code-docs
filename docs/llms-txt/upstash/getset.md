# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/getset.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/getset.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/getset.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/getset.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/getset.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/getset.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/getset.md

# GETSET

> Return the value of the specified key and replace it with a new value.

## Arguments

<ParamField body="key" type="string" required>
  The key to get.
</ParamField>

<ParamField body="newValue" required>
  The new value to store.
</ParamField>

## Response

<ResponseField required>
  The response is the value stored at the key or `null` if the key doesn't exist.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}

  const oldValue = await redis.getset("key", newValue);
  ```
</RequestExample>
