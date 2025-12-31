# Source: https://upstash.com/docs/vector/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/reset.md

# Source: https://upstash.com/docs/vector/sdks/php/commands/reset.md

# Source: https://upstash.com/docs/vector/api/endpoints/reset.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/search/sdks/py/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/reset.md

# Source: https://upstash.com/docs/vector/sdks/php/commands/reset.md

# Source: https://upstash.com/docs/vector/api/endpoints/reset.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/search/sdks/py/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/reset.md

# Source: https://upstash.com/docs/vector/sdks/php/commands/reset.md

# Source: https://upstash.com/docs/vector/api/endpoints/reset.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/search/sdks/py/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/reset.md

# Source: https://upstash.com/docs/vector/sdks/php/commands/reset.md

# Source: https://upstash.com/docs/vector/api/endpoints/reset.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/search/sdks/py/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/reset.md

# Source: https://upstash.com/docs/vector/sdks/php/commands/reset.md

# Source: https://upstash.com/docs/vector/api/endpoints/reset.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/reset.md

# Source: https://upstash.com/docs/search/sdks/py/commands/reset.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/reset.md

# Reset

The `reset` method allows you to clear all vectors and metadata from a particular
namespace or all namespaces of an index.

## Arguments

There are two arguments available. You should only pass one of them:

<ResponseField name="namespace" type="string">
  Specifies a namespace to reset. Leave empty for the default namespace.
</ResponseField>

<ResponseField name="all" type="true | undefined">
  Whether to reset all namespaces. Can only be set to `true`.
</ResponseField>

## Response

`'Success'` if the index is successfully resetted.

<RequestExample>
  ```typescript Basic theme={"system"}
  const responseReset = await index.reset();
  // 'Successful'
  ```

  ```typescript All Namespaces theme={"system"}
  const responseReset = await index.reset({ all: true });
  // 'Successful'
  ```
</RequestExample>
