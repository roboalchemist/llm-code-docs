# Source: https://www.zuplo.com/docs/policies/galileo-tracing-inbound.md

# Galileo Tracing Policy

Galileo Tracing Inbound Policy

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-galileo-tracing-inbound-policy",
  "policyType": "galileo-tracing-inbound",
  "handler": {
    "export": "GalileoTracingInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {}
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `galileo-tracing-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `GalileoTracingInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `apiKey` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Galileo API key for authentication.
- `projectId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Galileo project ID (UUID) for organizing traces.
- `logStreamId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Galileo log stream ID (UUID) for organizing traces.
- `baseUrl` <code className="text-green-600">&lt;string&gt;</code> - The base URL for the Galileo API (optional, defaults to https://api.galileo.ai).

## Using the Policy

Read more about [how policies work](/articles/policies)
