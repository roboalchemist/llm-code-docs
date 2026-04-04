# Source: https://www.zuplo.com/docs/policies/replace-string-outbound.md

# Replace String in Response Body Policy

Replace a string in the incoming request body

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-replace-string-outbound-policy",
  "policyType": "replace-string-outbound",
  "handler": {
    "export": "ReplaceStringOutboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "match": "/(\\d+)/g",
      "mode": "regexp",
      "replaceWith": "1234"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `replace-string-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `ReplaceStringOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `mode` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The type of string replacement to perform. Allowed values are `regexp`, `string`.
- `match` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The pattern to match.
- `replaceWith` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The value to each match is replaced with.

## Using the Policy

Read more about [how policies work](/articles/policies)
