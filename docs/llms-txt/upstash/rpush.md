# Source: https://upstash.com/docs/redis/sdks/ts/commands/list/rpush.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/list/rpush.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/list/rpush.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/list/rpush.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/list/rpush.md

# RPUSH

> Push an element at the end of the list.

## Arguments

<ParamField body="key" type="string" required>
  The key of the list.
</ParamField>

<ParamField body="elements" type="...TValue[]" required>
  One or more elements to push at the end of the list.
</ParamField>

## Response

<ResponseField type="number" required>
  The length of the list after the push operation.
</ResponseField>

<RequestExample>
  ```ts Example  theme={"system"}
  const length1 = await redis.rpush("key", "a", "b", "c"); 
  console.log(length1); // 3
  const length2 = await redis.rpush("key", "d"); 
  console.log(length2); // 4
  ```
</RequestExample>
