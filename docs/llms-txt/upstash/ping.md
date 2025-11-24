# Source: https://upstash.com/docs/redis/sdks/ts/commands/auth/ping.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/auth/ping.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/auth/ping.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/auth/ping.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/auth/ping.md

# PING

> Send a ping to the server and get a response if the server is alive.

## Arguments

No arguments

## Response

<ResponseField type="string" required>
  `PONG`
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  const response = await redis.ping();
  console.log(response); // "PONG"
  ```
</RequestExample>
