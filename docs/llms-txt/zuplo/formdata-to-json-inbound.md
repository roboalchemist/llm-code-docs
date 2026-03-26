# Source: https://www.zuplo.com/docs/policies/formdata-to-json-inbound.md

# Form Data to JSON Policy

Converts form data in the incoming request to JSON.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-formdata-to-json-inbound-policy",
  "policyType": "formdata-to-json-inbound",
  "handler": {
    "export": "FormDataToJsonInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "badRequestIfNotFormData": true
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `formdata-to-json-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `FormDataToJsonInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `badRequestIfNotFormData` <code className="text-green-600">&lt;boolean&gt;</code> - Should the policy return an error if the request is not of the type form data. Defaults to `true`.
- `optionalHoneypotName` <code className="text-green-600">&lt;string&gt;</code> - The name of the honeypot field. Used to provide basic spam filtering.

## Using the Policy

Read more about [how policies work](/articles/policies)
