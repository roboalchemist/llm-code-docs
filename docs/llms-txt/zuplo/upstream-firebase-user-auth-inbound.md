# Source: https://www.zuplo.com/docs/policies/upstream-firebase-user-auth-inbound.md

# Upstream Firebase User Auth Policy

This policy adds a Firebase user token to the outgoing `Authentication` header
allowing requests to Firebase using the provided user's permissions.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-upstream-firebase-user-auth-inbound-policy",
  "policyType": "upstream-firebase-user-auth-inbound",
  "handler": {
    "export": "UpstreamFirebaseUserAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "developerClaims": {
        "premium": true
      },
      "expirationOffsetSeconds": 300,
      "serviceAccountJson": "$env(SERVICE_ACCOUNT_JSON)",
      "tokenRetries": 3,
      "userId": "1234",
      "webApiKey": "$env(WEB_API_KEY)"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `upstream-firebase-user-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `UpstreamFirebaseUserAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `serviceAccountJson` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Google Service Account key in JSON format. Note you can load this from environment variables using the $env(ENV_VAR) syntax.
- `userId` <code className="text-green-600">&lt;string&gt;</code> - The userId to use as the custom token's subject.
- `userIdPropertyPath` <code className="text-green-600">&lt;string&gt;</code> - The property on the incoming request.user object to retrieve the value of the userId.
- `developerClaims` <code className="text-green-600">&lt;object&gt;</code> - Additional claims to include in the custom token's payload.
- `webApiKey` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Firebase Web API Key (found in project settings)
- `tokenRetries` <code className="text-green-600">&lt;number&gt;</code> - The number of times to retry fetching the token in the event of a failure. Defaults to `3`.
- `expirationOffsetSeconds` <code className="text-green-600">&lt;number&gt;</code> - The number of seconds less than the token expiration to cache the token. Defaults to `300`.

## Using the Policy

Read more about [how policies work](/articles/policies)
