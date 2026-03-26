# Source: https://www.zuplo.com/docs/policies/mtls-auth-inbound.md

# mTLS Auth Policy

This policy will authenticate users based on mTLS certificates that are
configured for your project. This policy is available only to enterprise
customers (contact sales@zuplo.com to request info). When a requests is
authenticated with an mTLS certificate, the certificate data will be set as the
user object of the request. The `user.sub` property will be the value of the
certificates DN.

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-mtls-auth-inbound-policy",
  "policyType": "mtls-auth-inbound",
  "handler": {
    "export": "MTLSAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "allowExpiredCertificates": false,
      "allowRevokedCertificates": false,
      "allowUnauthenticatedRequests": false
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `mtls-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `MTLSAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `allowUnauthenticatedRequests` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the request should continue if authentication fails. Default is `false` which means unauthenticated users will automatically receive a 401 response. Defaults to `false`.
- `allowExpiredCertificates` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the request should continue if the certificate is expired. Defaults to `false`.
- `allowRevokedCertificates` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the request should continue if the certificate is revoked. Defaults to `false`.

## Using the Policy

Read more about [how policies work](/articles/policies)
