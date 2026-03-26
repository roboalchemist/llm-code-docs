# Source: https://www.zuplo.com/docs/policies/semantic-cache-inbound.md

# Semantic Cache Policy

The Semantic Cache Inbound policy caches responses based on semantic similarity
of cache keys rather than exact matches. This allows for more flexible caching
where similar requests can return cached responses even if the cache key is not
exactly the same.

:::caution{title="Beta"}

This policy is in beta. You can use it today, but it may change in non-backward compatible ways before the final release.

:::

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-semantic-cache-inbound-policy",
  "policyType": "semantic-cache-inbound",
  "handler": {
    "export": "SemanticCacheInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "cacheBy": "propertyPath",
      "cacheByPropertyPath": ".userId",
      "expirationSecondsTtl": 3600,
      "namespace": "user-cache",
      "semanticTolerance": 0.8
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `semantic-cache-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `SemanticCacheInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `semanticTolerance` <code className="text-green-600">&lt;number&gt;</code> - The semantic similarity threshold for semantic cache matches. Values closer to 0 require closer similarity, while larger values allow more flexible matching. Default is 0.2. Defaults to `0.2`.
- `expirationSecondsTtl` <code className="text-green-600">&lt;number&gt;</code> - The timeout of the cache in seconds. Defaults to 1 hour. Defaults to `3600`.
- `namespace` <code className="text-green-600">&lt;string&gt;</code> - Optional namespace to isolate cache entries. Useful for multi-tenant scenarios or different cache contexts. Defaults to `"default"`.
- `cacheBy` **(required)** <code className="text-green-600">&lt;string&gt;</code> - Determines how the cache key is generated. Use 'function' for custom logic or 'propertyPath' to extract from JSON body. Allowed values are `function`, `propertyPath`.
- `cacheByFunction` <code className="text-green-600">&lt;object&gt;</code> - The function that returns dynamic cache key data. Used only with `cacheBy=function`.
  - `export` **(required)** <code className="text-green-600">&lt;string&gt;</code> - Specifies the export to load your custom cache key function, e.g. `default`, `cacheKeyIdentifier`.
  - `module` **(required)** <code className="text-green-600">&lt;string&gt;</code> - Specifies the module to load your custom cache key function, in the format `$import(./modules/my-module)`.
- `cacheByPropertyPath` <code className="text-green-600">&lt;string&gt;</code> - The path to the property in the request body (JSON) to use as cache key. For example '.userId' would read the 'userId' property from the request body. Only works with cacheBy=propertyPath.
- `statusCodes` <code className="text-green-600">&lt;number[]&gt;</code> - Response status codes to be cached. Defaults to `[200,206,301,302,303,410]`.
- `returnCacheStatusHeader` <code className="text-green-600">&lt;boolean&gt;</code> - If true, the policy will return a custom header with the cache status. The default header name is `zp-semantic-cache`. Defaults to `false`.
- `cacheStatusHeaderName` <code className="text-green-600">&lt;string&gt;</code> - The name of the header to return the cache status. Only used if `returnCacheStatusHeader` is true. Defaults to `"zp-semantic-cache"`.

## Using the Policy

## How it works

1. **Cache Key Generation**: The policy generates a cache key either through a
   custom function or by extracting a value from the request body using a
   property path.

2. **Semantic Matching**: When a request comes in, the policy checks the
   semantic cache service to find semantically similar cache keys based on the
   configured similarity tolerance.

3. **Response Caching**: Successful responses are cached in the semantic cache
   service with the generated cache key.

4. **LLM-powered Similarity**: The cache matching uses Large Language Model
   (LLM) embeddings to determine semantic similarity between cache keys.

## Configuration

The policy supports two modes for cache key generation:

- **Function Mode**: Use a custom function to generate cache keys
- **Property Path Mode**: Extract cache keys from JSON request body using a
  property path

### Key Parameters

- **semanticTolerance** (optional): A number between 0 and 1 that controls how
  similar cache keys need to be for a match. Default is 0.8. Higher values
  (closer to 1) require more similarity, while lower values allow more flexible
  matching. Can be overridden by custom functions when using
  `cacheBy: "function"`.
- **expirationSecondsTtl** (optional): Cache expiration time in seconds. Default
  is 3600 (1 hour). Can be overridden by custom functions when using
  `cacheBy: "function"`.
- **namespace** (optional): An optional string to isolate cache entries within a
  specific namespace. This is useful for multi-tenant scenarios or when you want
  to separate different cache contexts. When specified, only cache entries
  within the same namespace will be matched and retrieved.

### Custom Functions

When using `cacheBy: "function"`, your custom function should return an object
with the following structure:

```typescript
{
  cacheKey: string;           // Required: The cache key for semantic matching
  semanticTolerance?: number;       // Optional: Override the policy's similarity tolerance
  expirationSecondsTtl?: number;      // Optional: Override the policy's cache expiration time
}
```

This allows for dynamic configuration where different requests can have
different caching behaviors based on your custom logic.

## Use Cases

- Caching API responses where requests may be semantically similar but not
  identical
- Natural language query caching where similar questions should return the same
  response
- User-specific caching where slight variations in user identifiers map to the
  same cache entry

Read more about [how policies work](/articles/policies)
