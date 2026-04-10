# Source: https://www.zuplo.com/docs/policies/upstream-firebase-admin-auth-inbound.md

# Upstream Firebase Admin Auth Policy

This policy adds a Firebase Admin token to the outgoing `Authentication` header
allowing requests to Firebase using Service Account admin permissions. This can
be useful for calling Firebase services such as Firestore through a Zuplo
endpoint that is secured with other means of Authentication such as API keys.
Additionally, this policy can be useful for service content to all API users
(for example serving a specific Firestore document containing configuration
data)

We recommend reading the `serviceAccountJson` from environment variables (so it
is not checked in to source control) using the `$env(ENV_VAR)` syntax.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-upstream-firebase-admin-auth-inbound-policy",
  "policyType": "upstream-firebase-admin-auth-inbound",
  "handler": {
    "export": "UpstreamFirebaseAdminAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "expirationOffsetSeconds": 300,
      "serviceAccountJson": "$env(SERVICE_ACCOUNT_JSON)",
      "tokenRetries": 3
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `upstream-firebase-admin-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `UpstreamFirebaseAdminAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `serviceAccountJson` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Google Service Account key in JSON format. Note you can load this from environment variables using the $env(ENV_VAR) syntax.
- `tokenRetries` <code className="text-green-600">&lt;number&gt;</code> - The number of times to retry fetching the token in the event of a failure. Defaults to `3`.
- `expirationOffsetSeconds` <code className="text-green-600">&lt;number&gt;</code> - The number of seconds less than the token expiration to cache the token. Defaults to `300`.

## Using the Policy

Read more about [how policies work](/articles/policies)
