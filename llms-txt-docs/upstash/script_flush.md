# Source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_flush.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/scripts/script_flush.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_flush.md

# SCRIPT FLUSH

> Removes all scripts from the script cache.

## Arguments

<ParamField body="options" type="Object">
  <ParamField body="async" type="boolean">
    Performs the flush asynchronously.
  </ParamField>

  <ParamField body="sync" type="boolean">
    Performs the flush synchronously.
  </ParamField>
</ParamField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.scriptFlush();
  ```

  ```ts With options theme={"system"}
  await redis.scriptFlush({
    async: true,
  });
  ```
</RequestExample>
