# Source: https://upstash.com/docs/redis/sdks/ts/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/auth/echo.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/auth/echo.md

# ECHO

Returns a message back to you. Useful for debugging the connection.

## Arguments

<ParamField body="message" type="string" required>
  A message to send to the server.
</ParamField>

## Response

<ResponseField type="string" required>
  The same message you sent.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const response = await redis.echo("hello world");
  console.log(response); // "hello world"
  ```
</RequestExample>
