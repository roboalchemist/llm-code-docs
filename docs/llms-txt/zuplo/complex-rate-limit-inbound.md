# Source: https://www.zuplo.com/docs/policies/complex-rate-limit-inbound.md

# Complex Rate Limiting Policy

Limit the number of requests based on complex counters derived from request or
response details. This is an advanced version of the
[Rate Limit Policy](https://zuplo.com/docs/policies/rate-limit-inbound) with
support for multiple limits and dynamic increments.

With this policy, you'll benefit from:

- **Advanced Rate Control**: Create multiple rate limits with different
  thresholds and time windows for sophisticated traffic management
- **Dynamic Limiting**: Adjust rate limit increments based on request or
  response data to implement usage-based pricing models
- **Resource Protection**: Shield your downstream services from traffic spikes
  and abuse while ensuring optimal performance
- **Flexible Implementation**: Define custom limit keys based on any request
  attribute for precise control over your API traffic
- **Granular Usage Plans**: Implement tiered consumption rates for different
  user segments to maximize monetization opportunities
- **Comprehensive Monitoring**: Track limit usage with detailed metrics to
  identify patterns and optimize your API strategy
- **Intelligent Traffic Shaping**: Prioritize critical requests while throttling
  less important traffic during peak loads
- **Seamless Scalability**: Handle growing API traffic with configurable limits
  that adapt to your business needs

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-complex-rate-limit-inbound-policy",
  "policyType": "complex-rate-limit-inbound",
  "handler": {
    "export": "ComplexRateLimitInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "limits": {
        "apples": 2,
        "bananas": 3
      },
      "rateLimitBy": "ip",
      "timeWindowMinutes": 0.6
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `complex-rate-limit-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `ComplexRateLimitInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `rateLimitBy` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The identifying element of the request that enforces distinct rate limits. For example, you can limit by `user`, `ip`, `function` or `all` - function allows you to specify a simple function to create a string identifier to create a rate-limit group. Allowed values are `user`, `ip`, `function`, `all`. Defaults to `"user"`.
- `limits` **(required)** <code className="text-green-600">&lt;object&gt;</code> - A dictionary (string: number) of limits to be enforced across custom counters for this policy.
- `timeWindowMinutes` **(required)** <code className="text-green-600">&lt;integer&gt;</code> - The time window in which the requests are rate-limited. The count restarts after each window expires. Defaults to `60`.
- `identifier` <code className="text-green-600">&lt;object&gt;</code> - The function that returns dynamic configuration data. Used only with `rateLimitBy=function`.
  - `export` **(required)** <code className="text-green-600">&lt;string&gt;</code> - used only with rateLimitBy=function. Specifies the export to load your custom bucket function, e.g. `default`, `rateLimitIdentifier`. Defaults to `""`.
  - `module` **(required)** <code className="text-green-600">&lt;string&gt;</code> - Specifies the module to load your custom bucket function, in the format `$import(./modules/my-module)`. Defaults to `""`.
- `headerMode` <code className="text-green-600">&lt;string&gt;</code> - Adds the retry-after header. Allowed values are `none`, `retry-after`. Defaults to `"retry-after"`.
- `throwOnFailure` <code className="text-green-600">&lt;boolean&gt;</code> - If true, the policy will throw an error in the event there is a problem connecting to the rate limit service. Defaults to `false`.
- `mode` <code className="text-green-600">&lt;string&gt;</code> - The mode of the policy. If set to `async`, the policy will check if the request is over the rate limit without blocking. This can result in some requests allowed over the rate limit. Allowed values are `strict`, `async`. Defaults to `"strict"`.

## Using the Policy

This policy allows setting multiple limits that can optionally be overridden
programmatically.

### Set Increments Programmatically

Override the increments for limits in the current request.

If your policy has a limit set as follows:

```
"limits": {
  "compute": 10
}
```

You can use this function to override the increment of the `compute` units
consumed on a request by calling
`ComplexRateLimitInboundPolicy.setIncrements(context, {     compute: 5,   });`
on a custom policy. This can be useful if you want to dynamically change the
increment of a limit based on data in the response (such as a header).

Read more about [how policies work](/articles/policies)
