# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/getdel.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/string/getdel.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/string/getdel.md

# GETDEL

> Return the value of the specified key and delete the key.

## Arguments

<ParamField body="key" type="string" required>
  The key to get.
</ParamField>

## Response

<ResponseField required>
  The response is the value stored at the key or `null` if the key doesn't exist.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  type MyType = {
      a: number;
      b: string;
  }
  await redis.getdel<MyType>("key");
  // returns {a: 1, b: "2"}
  ```
</RequestExample>
