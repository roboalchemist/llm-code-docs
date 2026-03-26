# Source: https://www.zuplo.com/docs/policies/mock-api-inbound.md

# Mock API Response Policy

Returns example responses from the OpenAPI document associated with this route.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-mock-api-inbound-policy",
  "policyType": "mock-api-inbound",
  "handler": {
    "export": "MockApiInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "contentType": "application/json",
      "exampleName": "example1",
      "random": false
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `mock-api-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `MockApiInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `random` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the response should be selected randomly, from the available examples (that match any filter criteria). If `false` the first matching example is used. Defaults to `false`.
- `responsePrefixFilter` <code className="text-green-600">&lt;string&gt;</code> - Specifies a prefix to match the responses to select from. Typically this is a status code like "200" or "2XX". If you want the policy to select randomly from all 2XX codes, set this property to "2" and random to `true`.
- `contentType` <code className="text-green-600">&lt;string&gt;</code> - Specify the content-type of the response to select from. If not specified, the first matching response is used (or random).
- `exampleName` <code className="text-green-600">&lt;string&gt;</code> - Specify the name of the example to select. If not specified, the first matching response is used (or random).

## Using the Policy

Read more about [how policies work](/articles/policies)
