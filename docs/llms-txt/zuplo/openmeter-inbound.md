# Source: https://www.zuplo.com/docs/policies/openmeter-inbound.md

# OpenMeter Policy

Send usage metrics to [OpenMeter](https://openmeter.io/) for metering and
billing. This policy allows you to track API usage by sending events to
OpenMeter's API in CloudEvents format.

With this policy, you'll benefit from:

- **Usage-Based Billing**: Implement precise metering for pay-as-you-go pricing
  models
- **Real-Time Analytics**: Track API usage patterns and customer behavior as
  they happen
- **Customizable Event Tracking**: Capture specific metrics that matter to your
  business
- **Customer Segmentation**: Identify usage patterns across different customer
  segments
- **Flexible Integration**: Works seamlessly with OpenMeter's CloudEvents-based
  API
- **Batch Processing**: Efficiently sends events in batches to minimize
  performance impact

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-openmeter-inbound-policy",
  "policyType": "openmeter-inbound",
  "handler": {
    "export": "OpenMeterInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "apiKey": "$env(OPENMETER_API_KEY)",
      "meter": {
        "type": "api-request",
        "data": {
          "count": 1
        }
      },
      "requiredEntitlements": ["api-request"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `openmeter-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `OpenMeterInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `apiUrl` <code className="text-green-600">&lt;string&gt;</code> - The URL of the OpenMeter API endpoint. Defaults to `"https://openmeter.cloud"`.
- `apiKey` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The API key to use when sending metering calls to OpenMeter.
- `meter` <code className="text-green-600">&lt;undefined&gt;</code> - A single meter configuration or an array of meter configurations for OpenMeter.
- `meterOnStatusCodes` <code className="text-green-600">&lt;undefined&gt;</code> - A list of successful status codes and ranges "200-299, 304" that should trigger a metering event. Defaults to `"200-299"`.
- `eventSource` <code className="text-green-600">&lt;string&gt;</code> - The event's source (e.g. the service name). Defaults to `"api-gateway"`.
- `requiredEntitlements` <code className="text-green-600">&lt;string[]&gt;</code> - A list of entitlements (feature keys) required in order for the call to be allowed.
- `subjectPath` <code className="text-green-600">&lt;string&gt;</code> - The path to the property on `request.user` that contains the subject used for meters and entitlements. For example `.data.accountId` would read the `request.user.data.accountId` property. Defaults to `".sub"`.

## Using the Policy

## How it works

The policy sends usage events to OpenMeter's API in
[CloudEvents](https://cloudevents.io/) format whenever a request matches the
configured status codes. The events include customer identification, event type,
and custom data that can be used for metering and billing.

Additionally, the policy can check entitlements before allowing access to your
API. When entitlement checking is enabled, the policy will:

1. Check if the subject has access to the required features
2. Block the request if the subject doesn't have access to any required feature
3. Log detailed information about failed entitlements

## Programmatic Meters

You can dynamically set meters for each request using the
`OpenMeterInboundPolicy.setMeters` method:

```typescript
import { OpenMeterInboundPolicy } from "@zuplo/runtime";

export default async function (request, context) {
  // Set a single meter
  OpenMeterInboundPolicy.setMeters(context, {
    type: "api-call",
    data: {
      endpoint: request.url,
      method: request.method,
      tokens: 150,
    },
  });

  // Or set multiple meters
  OpenMeterInboundPolicy.setMeters(context, [
    {
      type: "api-call",
      data: {
        endpoint: request.url,
        method: request.method,
      },
    },
    {
      type: "llm-usage",
      data: {
        model: "gpt-4",
        prompt_tokens: 100,
        completion_tokens: 50,
      },
    },
  ]);

  return request;
}
```

## Examples

### Basic Metering

```json
{
  "type": "openmeter-inbound",
  "handler": "$import(@zuplo/runtime).OpenMeterInboundPolicy",
  "options": {
    "apiKey": "your-api-key",
    "meter": {
      "type": "api-call",
      "data": {
        "service": "payment-api",
        "tier": "premium"
      }
    }
  }
}
```

### Multiple Meters

```json
{
  "type": "openmeter-inbound",
  "handler": "$import(@zuplo/runtime).OpenMeterInboundPolicy",
  "options": {
    "apiKey": "your-api-key",
    "meter": [
      {
        "type": "api-call",
        "data": {
          "service": "payment-api"
        }
      },
      {
        "type": "data-transfer",
        "data": {
          "bytes": 1024
        }
      }
    ]
  }
}
```

### Metering with Entitlement Checking

```json
{
  "type": "openmeter-inbound",
  "handler": "$import(@zuplo/runtime).OpenMeterInboundPolicy",
  "options": {
    "apiKey": "your-api-key",
    "meter": {
      "type": "api-call",
      "data": {
        "service": "payment-api"
      }
    },
    "requiredEntitlements": ["payment-api-access", "premium-tier"]
  }
}
```

### Custom Status Codes

```json
{
  "type": "openmeter-inbound",
  "handler": "$import(@zuplo/runtime).OpenMeterInboundPolicy",
  "options": {
    "apiKey": "your-api-key",
    "meterOnStatusCodes": "200-299,304",
    "meter": {
      "type": "api-call"
    }
  }
}
```

## CloudEvents Format

The policy sends events to OpenMeter in CloudEvents format. Each event includes:

- `specversion`: Always "1.0"
- `id`: Unique identifier (combines request ID and meter type)
- `time`: ISO 8601 timestamp
- `source`: The configured event source
- `subject`: The user/customer identifier
- `type`: The meter type
- `data`: Custom data from the meter configuration

You can override CloudEvents fields when setting meters dynamically:

```typescript
OpenMeterInboundPolicy.setMeters(context, {
  type: "llm-usage",
  id: "custom-event-id-123",
  subject: "user-456",
  data: {
    model: "gpt-4",
    tokens: 1500,
  },
});
```

Read more about [how policies work](/articles/policies)
