# Source: https://www.zuplo.com/docs/policies/comet-opik-tracing-inbound.md

# Comet Opik Tracing Policy

Comet Opik Tracing Inbound Policy

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-comet-opik-tracing-inbound-policy",
  "policyType": "comet-opik-tracing-inbound",
  "handler": {
    "export": "CometOpikTracingInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {}
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `comet-opik-tracing-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `CometOpikTracingInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `apiKey` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Comet Opik API key for authentication.
- `projectName` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Comet Opik project name for organizing traces.
- `workspace` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Comet Opik workspace name.
- `baseUrl` <code className="text-green-600">&lt;string&gt;</code> - The base URL for the Comet Opik API (optional, defaults to https://www.comet.com/opik/api).

## Using the Policy

Read more about [how policies work](/articles/policies)
