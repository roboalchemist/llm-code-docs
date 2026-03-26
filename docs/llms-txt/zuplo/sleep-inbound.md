# Source: https://www.zuplo.com/docs/policies/sleep-inbound.md

# Sleep / Delay Policy

Add a delay to the incoming request. Useful for testing.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-sleep-inbound-policy",
  "policyType": "sleep-inbound",
  "handler": {
    "export": "SleepInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "sleepInMs": 1000
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `sleep-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `SleepInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `sleepInMs` **(required)** <code className="text-green-600">&lt;number&gt;</code> - The number of milliseconds to delay the request.

## Using the Policy

Read more about [how policies work](/articles/policies)
