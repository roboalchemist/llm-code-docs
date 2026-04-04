# Source: https://www.zuplo.com/docs/policies/rate-limit-inbound.md

# Rate Limiting Policy

Rate-limiting allows you to set a maximum rate of requests for your API gateway.
This is useful to enforce rate limits agreed with your clients and protect your
downstream services from being overwhelmed.

The Zuplo Rate-Limit policy allows you to limit requests based on different
attributes of the incoming request. For example, you might set a rate limit of
10 requests per minute per user, or 20 requests per minute for a given IP
address.

With this policy, you'll benefit from:

- **API Protection**: Shield your backend services from traffic spikes and
  potential DoS attacks
- **Flexible Limiting Options**: Limit by IP address, user ID, API key, or
  custom attributes
- **Granular Control**: Set different limits for different routes, users, or
  customer tiers
- **Custom Rate Limit Logic**: Implement dynamic rate limiting with custom
  functions
- **Fair Usage Enforcement**: Ensure equitable API access across all consumers
- **Quota Management**: Easily implement usage-based pricing tiers for your API
- **Automatic Response Handling**: Returns standard 429 status codes with
  appropriate headers

The Zuplo rate-limiter also allows you to set a custom bucket name to implement
rate limits using a function, giving you complete control over how requests are
grouped and limited.

When a client reaches a rate limit, they will receive a `429 Too Many Requests`
response code with appropriate headers indicating when they can retry.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-rate-limit-inbound-policy",
  "policyType": "rate-limit-inbound",
  "handler": {
    "export": "RateLimitInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "rateLimitBy": "ip",
      "requestsAllowed": 2,
      "timeWindowMinutes": 1
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `rate-limit-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `RateLimitInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `rateLimitBy` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The identifying element of the request that enforces distinct rate limits. For example, you can limit by `user`, `ip`, `function` or `all` - function allows you to specify a simple function to create a string identifier to create a rate-limit group. Allowed values are `user`, `ip`, `function`, `all`. Defaults to `"user"`.
- `requestsAllowed` **(required)** <code className="text-green-600">&lt;integer&gt;</code> - The max number of requests allowed in the given time window. Defaults to `1000`.
- `timeWindowMinutes` **(required)** <code className="text-green-600">&lt;integer&gt;</code> - The time window in which the requests are rate-limited. The count restarts after each window expires. Defaults to `60`.
- `identifier` <code className="text-green-600">&lt;object&gt;</code> - The function that returns dynamic configuration data. Used only with `rateLimitBy=function`.
  - `export` **(required)** <code className="text-green-600">&lt;string&gt;</code> - used only with rateLimitBy=function. Specifies the export to load your custom bucket function, e.g. `default`, `rateLimitIdentifier`. Defaults to `"$import(./modules/my-module)"`.
  - `module` **(required)** <code className="text-green-600">&lt;string&gt;</code> - Specifies the module to load your custom bucket function, in the format `$import(./modules/my-module)`. Defaults to `""`.
- `headerMode` <code className="text-green-600">&lt;string&gt;</code> - Adds the retry-after header. Allowed values are `none`, `retry-after`. Defaults to `"retry-after"`.
- `throwOnFailure` <code className="text-green-600">&lt;boolean&gt;</code> - If true, the policy will throw an error in the event there is a problem connecting to the rate limit service. Defaults to `false`.
- `mode` <code className="text-green-600">&lt;string&gt;</code> - The mode of the policy. If set to `async`, the policy will check if the request is over the rate limit without blocking. This can result in some requests allowed over the rate limit. Allowed values are `strict`, `async`. Defaults to `"strict"`.

## Using the Policy

The Rate Limit Inbound policy allows you to control the number of requests that
can be made to your API within a specified time window. This helps protect your
API from abuse, ensures fair usage among clients, and prevents downstream
services from being overwhelmed.

## Configuration Options

The policy offers several ways to identify and group requests for rate limiting:

- **IP Address**: Limit requests based on the client's IP address
- **User ID**: Limit requests based on the authenticated user's identity
- **Custom Function**: Create custom rate limiting logic based on any request
  property
- **API Key**: Limit requests based on the API key used for authentication

:::tip

Note you can have multiple instances of rate-limiting policies to use in
combination. You should apply the longest duration timeWindow first, followed by
shorter duration time windows.

:::

## Using a custom function

You can create a rate-limit bucket based on any property of a request using a
custom function that returns a `CustomRateLimitDetails` object (which provides
the identifier used by the limiting system).

The `CustomRateLimitDetails` object can be used to override the
`timeWindowMinutes` & `requestsAllowed` options.

This example creates a unique rate-limiting function based on the `customerId`
parameter in routes (note it's important that a policy like this is applied to a
route that has a `/:customerId` parameter).

```ts
//module - ./modules/rate-limiter.ts

import {
  CustomRateLimitDetails,
  ZuploRequest,
  ZuploContext,
} from "@zuplo/runtime";

export function rateLimitKey(
  request: ZuploRequest,
  context: ZuploContext,
  policyName: string,
): CustomRateLimitDetails | undefined {
  context.log.info(
    `processing customerId '${request.params.customerId}' for rate-limit policy '${policyName}'`,
  );
  if (request.params.customerId === "43567890") {
    // Override timeWindowMinutes & requestsAllowed
    return {
      key: request.params.customerId,
      requestsAllowed: 100,
      timeWindowMinutes: 1,
    };
  }
}
```

```json
// config - ./config/policies.json
"export": "RateLimitInboundPolicy",
"module": "$import(@zuplo/runtime)",
"options": {
  "rateLimitBy": "function",
  "requestsAllowed": 2,
  "timeWindowMinutes": 1,
  "identifier": {
    "module": "$import(./modules/rate-limiter)",
    "export": "rateLimitKey"
  }
}
```

Read more about [how policies work](/articles/policies)
