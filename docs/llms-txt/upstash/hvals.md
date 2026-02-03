# Source: https://upstash.com/docs/redis/sdks/ts/commands/hash/hvals.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/hash/hvals.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# HVALS

> Returns all values in the hash stored at key.

## Arguments

<ParamField body="key" type="str" required>
  The key of the hash.
</ParamField>

## Response

<ResponseField type="List[str]" required>
  All values in the hash, or an empty list when key does not exist.
</ResponseField>

<RequestExample>
  ```py Example theme={"system"}
  redis.hset("myhash", values={
    "field1": "Hello",
    "field2": "World"
  })

  assert redis.hvals("myhash") == ["Hello", "World"]
  ```
</RequestExample>
