# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/json/strappend.md

# Source: https://upstash.com/docs/redis/sdks/ts/commands/json/strappend.md

# JSON.STRAPPEND

> Append the json-string values to the string at path.

## Arguments

<ParamField body="key" type="string" required>
  The key of the json entry.
</ParamField>

<ParamField body="path" type="string" default="$">
  The path of the value.
</ParamField>

<ParamField body="value" type="string" required>
  The value to append to the existing string.
</ParamField>

## Response

<ResponseField type="integer[]" required>
  The length of the array after the appending.
</ResponseField>

<RequestExample>
  ```ts Example theme={"system"}
  await redis.json.strappend("key", "$.path.to.str", "abc");
  ```
</RequestExample>
