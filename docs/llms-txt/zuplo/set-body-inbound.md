# Source: https://www.zuplo.com/docs/policies/set-body-inbound.md

# Set Body Policy

The Set Body policy allows you to set or override the incoming request body.
[GET or HEAD requests do not support bodies on Zuplo](https://zuplo.com/docs/articles/zp-body-removed),
so be sure to use the
[Change Method](https://zuplo.com/docs/policies/change-method-inbound) policy to
update the method to a `POST` or whatever is appropriate. You might also need to
use the [Set Header](https://zuplo.com/docs/policies/set-headers-inbound) policy
to set a `content-type`.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-set-body-inbound-policy",
  "policyType": "set-body-inbound",
  "handler": {
    "export": "SetBodyInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "body": "Hello World!"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `set-body-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `SetBodyInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `body` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The value to set for the body.

## Using the Policy

Read more about [how policies work](/articles/policies)
