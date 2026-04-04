# Source: https://www.zuplo.com/docs/policies/request-size-limit-inbound.md

# Request Size Limit Policy

Enforces a maximum size in bytes of the incoming request.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-request-size-limit-inbound-policy",
  "policyType": "request-size-limit-inbound",
  "handler": {
    "export": "RequestSizeLimitInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "maxSizeInBytes": 10000
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `request-size-limit-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `RequestSizeLimitInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `maxSizeInBytes` **(required)** <code className="text-green-600">&lt;number&gt;</code> - The maximum size of the request in bytes.
- `trustContentLengthHeader` <code className="text-green-600">&lt;boolean&gt;</code> - If true, the policy will reject any request with a `content-length` header in excess of `maxSizeInBytes` bytes value, but will not verify the actual size of the request. This is more efficient and offers slightly better memory usage but should only be used if you trust/control the clients calling the gateway to send an accurate content-length. If false, the gateway will actually verify the request size and reject any request with a size in excess of the stated maximum.

## Using the Policy

Read more about [how policies work](/articles/policies)
