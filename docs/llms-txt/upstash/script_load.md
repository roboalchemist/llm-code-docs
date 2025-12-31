# Source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/scripts/script_load.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_load.md

# SCRIPT LOAD

> Load the specified Lua script into the script cache.

## Arguments

<ParamField body="script" type="string" required>
  The script to load.
</ParamField>

## Response

<ResponseField type="string" required>
  The sha1 of the script.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const script = `
    local value = redis.call('GET', KEYS[1])
    return value
  `;
  const sha1 = await redis.scriptLoad(script);

  ```
</RequestExample>
