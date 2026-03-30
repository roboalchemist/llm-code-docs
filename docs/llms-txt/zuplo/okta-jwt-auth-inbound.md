# Source: https://www.zuplo.com/docs/policies/okta-jwt-auth-inbound.md

# Okta JWT Auth Policy

Authenticate requests with JWT tokens issued by Okta. This is a customized
version of the
[OpenId JWT Policy](https://zuplo.com/docs/policies/open-id-jwt-auth-inbound)
specifically for Okta.

See [this document](https://zuplo.com/docs/articles/oauth-authentication) for
more information about OAuth authorization in Zuplo.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-okta-jwt-auth-inbound-policy",
  "policyType": "okta-jwt-auth-inbound",
  "handler": {
    "export": "OktaJwtInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "allowUnauthenticatedRequests": false,
      "audience": "api://my-api",
      "issuerUrl": "https://dev-12345.okta.com/oauth2/abc",
      "oAuthResourceMetadataEnabled": false
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `okta-jwt-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `OktaJwtInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `allowUnauthenticatedRequests` <code className="text-green-600">&lt;boolean&gt;</code> - Allow unauthenticated requests to proceed. This is use useful if you want to use multiple authentication policies or if you want to allow both authenticated and non-authenticated traffic. Defaults to `false`.
- `issuerUrl` **(required)** <code className="text-green-600">&lt;string&gt;</code> - Your Okta authorization server's issuer URL. For example, `https://dev-12345.okta.com/oauth2/abc`.
- `audience` <code className="text-green-600">&lt;string&gt;</code> - The Okta audience of your API, for example `api://my-api`.
- `oAuthResourceMetadataEnabled` <code className="text-green-600">&lt;boolean&gt;</code> - Flag that determines whether OAuth protected resource metadata is enabled. Defaults to `false`.

## Using the Policy

Read more about [how policies work](/articles/policies)
