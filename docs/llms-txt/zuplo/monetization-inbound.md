# Source: https://www.zuplo.com/docs/policies/monetization-inbound.md

# Monetization Policy

The Monetization policy allows you to track and monetize the usage of your API
resources, declaratively and programmatically.

Follow our
[Early Access: Getting Started with Monetization Guide](https://github.com/zuplo-samples/monetization-preview)
to get started.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-monetization-inbound-policy",
  "policyType": "monetization-inbound",
  "handler": {
    "export": "MonetizationInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "cacheTtlSeconds": 60,
      "meters": {
        "requests": 1
      }
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `monetization-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `MonetizationInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `authHeader` <code className="text-green-600">&lt;string&gt;</code> - The name of the header with the key. Defaults to `"Authorization"`.
- `authScheme` <code className="text-green-600">&lt;string&gt;</code> - The scheme used on the header. Defaults to `"Bearer"`.
- `cacheTtlSeconds` <code className="text-green-600">&lt;number&gt;</code> - The time to cache authentication results for a particular key. Higher values will decrease latency. Cached results will be valid until the cache expires even in the event the key is deleted, etc. Defaults to `60`.
- `meters` <code className="text-green-600">&lt;object&gt;</code> - The meters to be used by the policy against the subscription quota.
- `meterOnStatusCodes` <code className="text-green-600">&lt;undefined&gt;</code> - A list of successful status codes and ranges "200-299, 304" that should trigger a metering call. Defaults to `"200-299"`.

## Using the Policy

# Monetization Metering Policy

The Monetization policy validates subscriptions and records usage. Meter usage
is sent in a final response hook after status-code filtering.

## Configuration

- `meters` (optional): static meter increments applied on metered responses.
- `meterOnStatusCodes`: status codes/ranges that trigger metering.
- auth/cache settings: `authHeader`, `authScheme`, `cacheTtlSeconds`.

### Static meter configuration

```json
{
  "name": "monetization-inbound-policy",
  "policyType": "monetization-inbound",
  "options": {
    "meters": {
      "api": 1
    },
    "meterOnStatusCodes": "200-299"
  }
}
```

## Runtime meter updates

You can set or update meter increments at different points in a request
lifecycle (for example in an inbound policy, handler, or outbound policy). The
monetization policy reads the latest values in its final hook before sending
usage.

### Set (replace) request meter increments

```typescript
import { MonetizationInboundPolicy } from "@zuplo/runtime";

MonetizationInboundPolicy.setMeters(context, {
  input_tokens: 1000,
  output_tokens: 250,
});
```

### Add (accumulate) request meter increments

```typescript
import { MonetizationInboundPolicy } from "@zuplo/runtime";

MonetizationInboundPolicy.addMeters(context, { input_tokens: 500 });
MonetizationInboundPolicy.addMeters(context, { input_tokens: 300 });
```

### Read current request meter increments

```typescript
import { MonetizationInboundPolicy } from "@zuplo/runtime";

const meters = MonetizationInboundPolicy.getMeters(context);
```

## Meter merge behavior

- The final hook merges `options.meters` and request meter increments from
  `setMeters` / `addMeters`.
- `setMeters` replaces the current runtime meter map and overrides matching keys
  from `options.meters`.
- `addMeters` accumulates into the current runtime meter map and then merges
  additively with `options.meters`.
- If both are empty, metering is skipped.

For a meter key like `api` with `options.meters.api = 1`:

- `setMeters(context, { api: 50 })` sends `api: 50`.
- `addMeters(context, { api: 50 })` sends `api: 51`.

## Prerequisites

- `monetization-inbound` is enabled in your route/pipeline.
- Meter names match entitlements on the subscription.
- Meter quantities are finite positive numbers.

## Notes

- `setMeters` replaces current request meter increments.
- `addMeters` accumulates values across multiple calls.
- Entitlements are validated before usage is sent.

Read more about [how policies work](/articles/policies)
