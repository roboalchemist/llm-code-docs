# Source: https://www.zuplo.com/docs/policies/ldap-auth-inbound.md

# LDAP Auth Policy

Authenticate requests using an LDAP server.

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-ldap-auth-inbound-policy",
  "policyType": "ldap-auth-inbound",
  "handler": {
    "export": "LDAPAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "ldapConnectorName": "my-ldap-connector"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `ldap-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `LDAPAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `ldapConnectorName` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The name of your configured LDAP service connector.

## Using the Policy

Read more about [how policies work](/articles/policies)
