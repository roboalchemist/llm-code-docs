# Source: https://www.zuplo.com/docs/policies/require-origin-inbound.md

# Require Origin Policy

The Require Origin policy is used to enforce that the client is sending an
`origin` header that matches your allow-list specified in the policy options.

This is useful if you want to stop any browser traffic from different domains.

However, it is important to note that it does not guarantee that traffic is only
coming from a browser. Somebody could simulate a browser request from a backend
server and set any origin they like.

If the incoming origin is missing, or not allowed - a 400 Forbidden Problem
Response will be sent to the client. You can customize the `detail` property in
the policy options.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-require-origin-inbound-policy",
  "policyType": "require-origin-inbound",
  "handler": {
    "export": "RequireOriginInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "failureDetail": "Your origin is not authorized to make this request.",
      "origins": "https://example.com, https://example.org"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `require-origin-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `RequireOriginInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `origins` **(required)** <code className="text-green-600">&lt;string&gt;</code> - A comma separated string containing valid origins.
- `failureDetail` <code className="text-green-600">&lt;string&gt;</code> - The `detail` of the HTTP Problem response, if the origin is missing or disallowed. Defaults to `"Forbidden"`.

## Using the Policy

Read more about [how policies work](/articles/policies)
