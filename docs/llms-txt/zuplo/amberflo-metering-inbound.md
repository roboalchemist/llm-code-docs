# Source: https://www.zuplo.com/docs/policies/amberflo-metering-inbound.md

# Amberflo Metering / Billing Policy

Seamlessly integrate usage-based metering and billing into your API with
Amberflo integration. This policy automatically tracks API usage and sends
metering data to [Amberflo](https://www.amberflo.io) for accurate billing and
consumption analytics.

With this policy, you'll benefit from:

- **Usage-Based Billing**: Easily implement consumption-based pricing models for
  your API
- **Granular Metering**: Track usage at the customer and endpoint level with
  customizable dimensions
- **Flexible Configuration**: Define meter names, values, and customer
  identification at the policy or code level
- **Batch Processing**: Efficiently send usage data with automatic batching for
  optimal performance
- **Real-Time Analytics**: Monitor API consumption patterns through Amberflo's
  dashboard

Add the policy to each route you want to meter, with the ability to customize
meter names, values, and dimensions per endpoint or dynamically in your code.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-amberflo-metering-inbound-policy",
  "policyType": "amberflo-metering-inbound",
  "handler": {
    "export": "AmberfloMeteringInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "apiKey": "$env(AMBERFLO_API_KEY)",
      "customerIdPropertyPath": ".sub",
      "meterApiName": "$env(AMBERFLO_METER_API_NAME)",
      "meterValue": "$env(AMBERFLO_METER_VALUE)",
      "statusCodes": "200-299",
      "url": " https://app.amberflo.io/ingest"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `amberflo-metering-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `AmberfloMeteringInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `apiKey` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The API key to use when sending metering calls to Amberflo.
- `meterApiName` <code className="text-green-600">&lt;string&gt;</code> - The name of the meter to use when sending metering calls to Amberflo (overridable in code).
- `meterValue` <code className="text-green-600">&lt;number&gt;</code> - The value to use when sending metering calls to Amberflo (overridable in code).
- `customerIdPropertyPath` <code className="text-green-600">&lt;string&gt;</code> - The path to the property on `request.user` contains the customer ID. For example `.data.accountNumber` would read the `request.user.data.accountNumber` property. Defaults to `".sub"`.
- `customerId` <code className="text-green-600">&lt;string&gt;</code> - The default customerId for all metering calls - overridable in code and by `customerIdPropertyPath`.
- `dimensions` <code className="text-green-600">&lt;object&gt;</code> - A dictionary of dimensions to be sent to Amberflo (extensible in code).
- `statusCodes` <code className="text-green-600">&lt;undefined&gt;</code> - A list of successful status codes and ranges "200-299, 304" that should trigger a metering call to Amberflo. Defaults to `"200-299"`.
- `url` <code className="text-green-600">&lt;string&gt;</code> - The URL to send metering events. This is useful for testing purposes. Defaults to `" https://app.amberflo.io/ingest"`.

## Using the Policy

This policy integrates with [Amberflo](https://www.amberflo.io) to enable
usage-based metering and billing for your API. It automatically tracks API usage
and sends metering data to Amberflo when requests match your configured success
criteria.

### How It Works

The policy performs the following operations:

1. Monitors API requests and captures successful responses based on configured
   status codes
2. Collects metering data including customer ID, meter name, and value
3. Batches metering events for efficient processing
4. Sends the data to Amberflo's ingest endpoint
5. Provides error handling and logging

### Policy Configuration

Configure the policy with your Amberflo API key and metering parameters:

```json
{
  "name": "amberflo-metering",
  "export": "AmberfloMeteringInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    "apiKey": "$env(AMBERFLO_API_KEY)",
    "meterApiName": "api-requests",
    "meterValue": 1,
    "customerIdPropertyPath": ".sub",
    "statusCodes": "200-299",
    "dimensions": {
      "environment": "production"
    }
  }
}
```

### Customer Identification

You can identify customers in three ways:

1. **Dynamic Property Path**: Extract customer ID from the request user object
   (recommended)
2. **Static Default**: Set a global customer ID at the policy level (not
   recommended)
3. **Programmatic Setting**: Set customer ID in code for complete flexibility

#### Using customerIdPropertyPath

The `customerIdPropertyPath` extracts the customer ID from the `request.user`
object. For example, with a JWT token or API Key metadata containing:

```json
{
  "sub": "bobby-tables",
  "data": {
    "email": "bob@example.com",
    "name": "Bobby Tables",
    "accountNumber": 1233423,
    "roles": ["admin"]
  }
}
```

You can access properties using dot notation (note the required leading dot):

- For the `sub` property: `".sub"`
- For nested properties: `".data.accountNumber"`

### Programmatic Configuration

You can dynamically set metering properties in your code using the
`AmberfloMeteringPolicy` helper class:

```ts
import {
  AmberfloMeteringPolicy,
  ZuploContext,
  ZuploRequest,
} from "@zuplo/runtime";

export default async function (
  request: ZuploRequest,
  context: ZuploContext,
  options: MyPolicyOptionsType,
  policyName: string,
) {
  AmberfloMeteringPolicy.setRequestProperties(context, {
    customerId: request.user.sub,
    meterApiName: request.params.color,
    meterValue: request.params.quantity || 1,
    dimensions: {
      region: request.headers.get("x-region") || "default",
    },
  });

  return request;
}
```

### Configuration Options

| Option                   | Type         | Required | Description                                                                                |
| ------------------------ | ------------ | -------- | ------------------------------------------------------------------------------------------ |
| `apiKey`                 | string       | Yes      | Your Amberflo API key for authentication                                                   |
| `meterApiName`           | string       | Yes\*    | The name of the meter to use when sending metering calls                                   |
| `meterValue`             | number       | Yes\*    | The value to increment the meter by (typically 1 for counting API calls)                   |
| `customerIdPropertyPath` | string       | No       | Path to extract customer ID from `request.user` object                                     |
| `customerId`             | string       | No       | Default customer ID if not using `customerIdPropertyPath`                                  |
| `dimensions`             | object       | No       | Additional dimensions to include with metering data                                        |
| `statusCodes`            | string/array | Yes      | Status codes that trigger metering (e.g., "200-299" or [200, 201])                         |
| `url`                    | string       | No       | Custom URL for the Amberflo ingest endpoint (defaults to "https://app.amberflo.io/ingest") |

\*Can be set programmatically if not provided in policy configuration

### Usage Examples

#### Basic API Request Metering

Apply the policy to routes you want to meter:

```json
{
  "paths": {
    "/api/products": {
      "get": {
        "x-zuplo-route": {
          "policies": {
            "inbound": ["jwt-auth", "amberflo-product-api-metering"]
          },
          "handler": {
            "export": "forwardToOrigin",
            "module": "$import(@zuplo/runtime)"
          }
        }
      }
    }
  }
}
```

#### Different Meters for Different Endpoints

Create separate policy instances for different meters:

```json
[
  {
    "name": "amberflo-read-metering",
    "export": "AmberfloMeteringInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "apiKey": "$env(AMBERFLO_API_KEY)",
      "meterApiName": "api-reads",
      "meterValue": 1,
      "customerIdPropertyPath": ".sub",
      "statusCodes": "200-299"
    }
  },
  {
    "name": "amberflo-write-metering",
    "export": "AmberfloMeteringInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "apiKey": "$env(AMBERFLO_API_KEY)",
      "meterApiName": "api-writes",
      "meterValue": 1,
      "customerIdPropertyPath": ".sub",
      "statusCodes": "200-299"
    }
  }
]
```

### Best Practices

- Store your Amberflo API key as an environment variable using
  `$env(AMBERFLO_API_KEY)`
- Use `customerIdPropertyPath` instead of hardcoding customer IDs
- Consider creating different meters for different types of API operations
- Add relevant dimensions to your metering data for better analytics
- Monitor your Amberflo dashboard to track API usage patterns

Read more about [how policies work](/articles/policies)
