# Source: https://www.zuplo.com/docs/ai-gateway/policies/akamai-ai-firewall.md

# Source: https://www.zuplo.com/docs/policies/akamai-ai-firewall.md

# Akamai AI Firewall Policy

Akamai AI Firewall Inbound Policy

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-akamai-ai-firewall-policy",
  "policyType": "akamai-ai-firewall",
  "handler": {
    "export": "AkamaiAIFirewallInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "streamingAccumulation": {
        "enabled": true,
        "eventsInterval": 5
      }
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `akamai-ai-firewall`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `AkamaiAIFirewallInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `configurationId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The configuration ID of the AI Firewall.
- `api-key` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The API key for the AI Firewall.
- `applicationId` <code className="text-green-600">&lt;string&gt;</code> - The application ID to identify this usage of the AI Firewall (optional).
- `streamingAccumulation` <code className="text-green-600">&lt;object&gt;</code> - Configuration for accumulating and validating streaming responses.
  - `enabled` <code className="text-green-600">&lt;boolean&gt;</code> - Enable accumulation and validation of streaming responses. Defaults to `true`.
  - `eventsInterval` <code className="text-green-600">&lt;number&gt;</code> - Number of SSE events to accumulate before checking with Akamai (default: 5). Defaults to `5`.
  - `checkIntervalMs` <code className="text-green-600">&lt;number&gt;</code> - Time interval in milliseconds for periodic checks (alternative to chunk count).

## Using the Policy

Read more about [how policies work](/articles/policies)
