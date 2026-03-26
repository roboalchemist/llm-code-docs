# Source: https://www.zuplo.com/docs/policies/readme-metrics-inbound.md

# Readme Metrics Policy

[Readme](https://readme.com) is a developer Documentation and metrics service.
This policy pushes the request/response data to their ingestion endpoint so you
can see your Zuplo API traffic in their API calls dashboard.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-readme-metrics-inbound-policy",
  "policyType": "readme-metrics-inbound",
  "handler": {
    "export": "ReadmeMetricsInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "apiKey": "$env(README_API_KEY)",
      "url": "https://metrics.readme.io/request",
      "useFullRequestPath": false,
      "userEmailPropertyPath": ""
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `readme-metrics-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `ReadmeMetricsInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `apiKey` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The API key to use when sending metrics calls to Readme.
- `userLabelPropertyPath` <code className="text-green-600">&lt;string&gt;</code> - This is the path to the property on `request.user` that contains the label you want to use. For example `.data.accountNumber` would read the `request.user.data.accountNumber` property. Defaults to `".sub"`.
- `userEmailPropertyPath` <code className="text-green-600">&lt;string&gt;</code> - This is the path to the property on `request.user` that contains the e-mail of the user. For example `.data.email` would read the `request.user.data.email` property. Defaults to `""`.
- `development` <code className="text-green-600">&lt;boolean&gt;</code> - Whether the data should be ingested as 'development' mode or not. Defaults to true for working-copy and false for all other environments.
- `useFullRequestPath` <code className="text-green-600">&lt;boolean&gt;</code> - When true, Zuplo sends the full request path (which might contain sensitive information). By default, we only send the route path which should not contain sensitive information. Defaults to `false`.
- `url` <code className="text-green-600">&lt;string&gt;</code> - The URL to send metering events. This is useful for testing purposes. Defaults to `"https://metrics.readme.io/request"`.

## Using the Policy

![Readme API Calls Dashboard](https://cdn.zuplo.com/assets/071b2ead-7769-413b-a66a-133ae6fd755d.png)

Read more about [how policies work](/articles/policies)
