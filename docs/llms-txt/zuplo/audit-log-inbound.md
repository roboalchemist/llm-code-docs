# Source: https://www.zuplo.com/docs/policies/audit-log-inbound.md

# Audit Logs Policy

Audit logging is an important part of API security that plays a critical role in
detecting and correcting issues such as unauthorized access or permission
elevations within your system. Audit logging is also a requirement for many
compliance certifications as well as part of the buying criteria for larger
enterprises.

Adding Audit Logging to your APIs that are secured with Zuplo is as easy as
adding a policy. Typically you want to add audit logs to any API that modifies
data, however depending on the API you may want it on read operations as well
(i.e. retrieve a secret key, etc.)

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-audit-log-inbound-policy",
  "policyType": "audit-log-inbound",
  "handler": {
    "export": "AuditLogsInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "logGeolocation": true,
      "logIpAddress": true,
      "logQueryParameters": true,
      "logRouteParameters": true,
      "logUser": true
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `audit-log-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `AuditLogsInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `logIpAddress` <code className="text-green-600">&lt;undefined&gt;</code> - if the IP address should be logged. Defaults to `true`.
- `logUser` <code className="text-green-600">&lt;undefined&gt;</code> - if the user's `sub` should be logged. Defaults to `true`.
- `logGeolocation` <code className="text-green-600">&lt;undefined&gt;</code> - if the geolocation information should be logged (i.e. state, country, longitude, latitude, etc.). Defaults to `true`.
- `logQueryParameters` <code className="text-green-600">&lt;undefined&gt;</code> - log the values of query parameters. Defaults to `true`.
- `logRouteParameters` <code className="text-green-600">&lt;undefined&gt;</code> - The parameters in the route to log. Defaults to `true`.
- `tenant` <code className="text-green-600">&lt;undefined&gt;</code> - if the route parameters should be logged (i.e. the value of `customerId` in the route `/customers/:customerId`).
- `metadata` <code className="text-green-600">&lt;undefined&gt;</code> - A function to add additional data to the audit logs.

## Using the Policy

## Adding Custom Metadata

You can add any additional data to the audit logs with a custom function.

:::note

Custom metadata functions cannot be asynchronous. Due to the frequency of their
calls, asynchronous functions will add significant latency to your API.

:::

```ts
//module - ./modules/audit-logs.ts

import { ZuploRequest } from "@zuplo/runtime";

export function auditLogMetadata(request: ZuploRequest): any {
  const metadata = {
    accountId: request.user.data.account,
    customTraceId: request.headers.get("custom-trace-id"),
  };
  return metadata;
}
```

## Log Data

The structure of an audit log is shown below.

```json
{
  "route": "/customers/:customerId",
  "method": "GET",
  "query": {
    "a": 1,
    "b": 2
  },
  "params": {
    "customerId": "12345"
  },
  "headers": {
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
  },
  "user": {
    "sub": "user|12356"
  },
  "geolocation": {
    "country": "US",
    "city": "Seattle",
    "continent": "NA",
    "latitude": "1.123",
    "longitude": "4.567",
    "postalCode": "29700",
    "metroCode": "100",
    "region": "Washington",
    "timezone": "America/LosAngeles"
  },
  "metadata": {
    // Custom data
  }
}
```

## Audit Logs in the Portal

Audit logs are not currently surfaced in the Zuplo portal, but the feature is
planned soon.

## Audit Log API

Audit logs can be retrieved using the Zuplo Management API. Logs can be
retrieved by time span and can be filtered by `tenant`.

```http
GET /deployments/:deploymentId/auditlogs?tenant=TENANT
content-type: application/json
authorization: Bearer YOUR_TOKEN
```

Read more about [how policies work](/articles/policies)
