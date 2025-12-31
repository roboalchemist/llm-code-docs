# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/rename.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/rename.md

# RENAME

> Rename a key

## Arguments

<ParamField body="source" type="string" required>
  The original key.
</ParamField>

<ParamField body="destination" type="string" required>
  A new name for the key.
</ParamField>

## Response

<ResponseField type="string" required>
  `OK`
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
   await redis.rename("old", "new");
  ```
</RequestExample>
