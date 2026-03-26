# Source: https://www.zuplo.com/docs/policies/basic-auth-inbound.md

# Basic Auth Policy

The Basic Authentication policy allows you to authenticate incoming requests
using the Basic authentication standard. You can configure multiple accounts
with different passwords and a different bucket of user 'data'.

The API will expect a Basic Auth header (you can generate samples
[using this tool](https://www.debugbear.com/basic-auth-header-generator)).
Requests with invalid credentials (or no header) will not be authenticated.
Authenticated requests will populate the `user` property of the `ZuploRequest`
parameter on your RequestHandler.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-basic-auth-inbound-policy",
  "policyType": "basic-auth-inbound",
  "handler": {
    "export": "BasicAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "accounts": [
        {
          "data": {
            "name": "John Doe",
            "email": "john.doe@gmail.com"
          },
          "password": "$env(ACCOUNT_JOHN_PASSWORD)",
          "username": "$env(ACCOUNT_JOHN_USERNAME)"
        }
      ],
      "allowUnauthenticatedRequests": false
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `basic-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `BasicAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `accounts` **(required)** <code className="text-green-600">&lt;object[]&gt;</code> - An array of account objects (username, password and data properties).
  - `username` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The username for the account (this will be the `sub` property on `request.user`.
  - `password` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The password for the account - note we recommend storing this in environment variables.
  - `data` <code className="text-green-600">&lt;object&gt;</code> - The data payload you want associated with this account (this will be the `data` property on `request.user`).
- `allowUnauthenticatedRequests` <code className="text-green-600">&lt;boolean&gt;</code> - If 'true' allows the request to continue even if authenticated. When 'false' (the default) any unauthenticated request is automatically rejected with a 401. Defaults to `false`.

## Using the Policy

Read more about [how policies work](/articles/policies)
