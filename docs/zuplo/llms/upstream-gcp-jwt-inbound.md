# Source: https://www.zuplo.com/docs/policies/upstream-gcp-jwt-inbound.md

# Upstream GCP Self-Signed JWT Policy

This policy adds a JWT token to the headers, ready for us in an outgoing request
when calling a GCP service (e.g. Cloud Endpoints / ESPv2). We recommend reading
the `serviceAccountJson` from environment variables (so it is not checked in to
source control) using the `$env(ENV_VAR)` syntax.

CAUTION: This policy only works with
[certain Google APIs](https://developers.google.com/identity/protocols/oauth2/service-account#jwt-auth).
In most cases, the
[Upstream GCP Service Auth](https://zuplo.com/docs/policies/upstream-gcp-service-auth-inbound)
should be used.

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-upstream-gcp-jwt-inbound-policy",
  "policyType": "upstream-gcp-jwt-inbound",
  "handler": {
    "export": "UpstreamGcpJwtInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "audience": "your_gcp_service.endpoint.com",
      "serviceAccountJson": "$env(SERVICE_ACCOUNT_JSON)"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `upstream-gcp-jwt-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `UpstreamGcpJwtInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `audience` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The audience for the minted JWT. See the document [AuthRequirement](https://cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.AuthRequirement) for details.
- `serviceAccountJson` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Google Service Account key in JSON format. Note you can load this from environment variables using the $env(ENV_VAR) syntax.

## Using the Policy

Read more about [how policies work](/articles/policies)
