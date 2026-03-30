# Source: https://www.zuplo.com/docs/policies/upstream-zuplo-jwt-auth-inbound.md

# Upstream Zuplo JWT Policy

This policy generates a Zuplo JWT token and attaches it to outgoing requests.
It's useful when your upstream services need to authenticate requests coming
from your Zuplo API Gateway using JWT tokens.

The policy creates a self-signed JWT using Zuplo's built-in JWT service and adds
it to the specified request header (defaults to `Authorization`). The JWT
includes standard claims like subject, audience, and expiration time, plus any
additional custom claims you configure.

Key features:

- Configurable audience claim for specific service targeting
- Configurable header name and token prefix
- Support for custom claims in the JWT payload
- Adjustable token expiration time
- Automatic subject extraction from authenticated users

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-upstream-zuplo-jwt-auth-inbound-policy",
  "policyType": "upstream-zuplo-jwt-auth-inbound",
  "handler": {
    "export": "UpstreamZuploJwtAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "additionalClaims": {
        "role": "admin",
        "custom": "value"
      },
      "audience": "https://api.example.com",
      "expiresIn": 300,
      "headerName": "Authorization",
      "tokenPrefix": "Bearer"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `upstream-zuplo-jwt-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `UpstreamZuploJwtAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `audience` <code className="text-green-600">&lt;string&gt;</code> - The audience claim for the JWT.
- `headerName` <code className="text-green-600">&lt;string&gt;</code> - The header name where the JWT will be attached. Defaults to 'Authorization'. Defaults to `"Authorization"`.
- `tokenPrefix` <code className="text-green-600">&lt;string&gt;</code> - The prefix to use before the JWT token. Defaults to 'Bearer'. Set to an empty string to send the token without a prefix. Defaults to `"Bearer"`.
- `additionalClaims` <code className="text-green-600">&lt;object&gt;</code> - Additional claims to include in the JWT. These will be merged with the default claims.
- `expiresIn` <code className="text-green-600">&lt;undefined&gt;</code> - JWT expiration time. Can be a number (seconds) or a string with units (e.g., '5m' for 5 minutes, '1h' for 1 hour, '7d' for 7 days). Defaults to 300 seconds (5 minutes). Defaults to `300`.

## Using the Policy

## How It Works

When a request passes through this policy:

1. The policy generates a new JWT token using Zuplo's JWT service
2. The JWT includes standard claims (subject, audience, expiration) and any
   custom claims you configure
3. The token is added to the specified request header (default: `Authorization`)
4. The modified request is forwarded to your upstream service
5. Your upstream service can then validate the JWT to authenticate the request
   comes from your Zuplo API Gateway

## Configuration

### Basic Configuration

The simplest configuration uses all defaults:

```json
{
  "name": "upstream-jwt-policy",
  "policyType": "upstream-zuplo-jwt-inbound"
}
```

This will:

- Add the JWT to the `Authorization` header
- Use `Bearer` as the token prefix
- Set token expiration to 300 seconds (5 minutes)
- Use the authenticated user's subject or "api-gateway" as the JWT subject

### Advanced Configuration

```json
{
  "name": "upstream-jwt-policy",
  "policyType": "upstream-zuplo-jwt-auth-inbound",
  "handler": {
    "export": "UpstreamZuploJwtAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "audience": "https://api.example.com",
      "headerName": "X-API-Token",
      "tokenPrefix": "Token",
      "expiresIn": "10m",
      "additionalClaims": {
        "iss": "my-api-gateway",
        "scope": "read write",
        "custom": "value"
      }
    }
  }
}
```

## Options Reference

### `audience`

- **Type**: `string`
- **Default**: The current request URL
- **Description**: The audience claim for the JWT. Useful when your upstream
  service expects a specific audience value

### `headerName`

- **Type**: `string`
- **Default**: `"Authorization"`
- **Description**: The header name where the JWT will be attached

### `tokenPrefix`

- **Type**: `string`
- **Default**: `"Bearer"`
- **Description**: The prefix to use before the JWT token. Set to an empty
  string to send the token without a prefix

### `expiresIn`

- **Type**: `number | string`
- **Default**: `300`
- **Description**: JWT expiration time. Can be:
  - A number representing seconds (e.g., `300` for 5 minutes)
  - A string with time units (e.g., `"5m"` for 5 minutes, `"1h"` for 1 hour,
    `"7d"` for 7 days)

  Supported time units:
  - `s` - seconds
  - `m` - minutes
  - `h` - hours
  - `d` - days
  - `w` - weeks
  - `y` - years

### `additionalClaims`

- **Type**: `object`
- **Default**: `{}`
- **Description**: Additional claims to include in the JWT. These will be merged
  with the default claims

## JWT Claims

The generated JWT includes the following standard claims:

- `sub` (subject): The authenticated user's subject claim, or "api-gateway" if
  no user is authenticated
- `aud` (audience): The value from the `audience` option, or the current request
  URL if not specified
- `exp` (expiration): Token expiration timestamp based on the `expiresIn` option
- `iat` (issued at): Token issuance timestamp (automatically added by JWT
  service)

Any properties in `additionalClaims` will be merged into the JWT payload.

## Use Cases

### Audience-Specific Authentication

As a best practice, you can set the `audience` option to target specific
upstream services. This ensures that the JWT is only valid for that service,
preventing misuse if the token is intercepted.

```json
{
  "name": "audience-specific-auth",
  "policyType": "upstream-zuplo-jwt-auth-inbound",
  "handler": {
    "export": "UpstreamZuploJwtAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "audience": "https://api.example.com"
    }
  }
}
```

### Custom Claims

Custom claims can be added to the JWT to provide additional context or metadata
for your upstream service. For example, you might want to include
environment-specific variables.

```json
{
  "name": "service-auth",
  "policyType": "upstream-zuplo-jwt-auth-inbound",
  "handler": {
    "export": "UpstreamZuploJwtAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "additionalClaims": {
        "env": "$env(MY_VAR)"
      }
    }
  }
}
```

### Custom Header Authentication

Sometimes your upstream service might already expect an `Authorization` header.
In that case you can configure the policy to use a custom header.

```json
{
  "name": "custom-header-auth",
  "policyType": "upstream-zuplo-jwt-auth-inbound",
  "handler": {
    "export": "UpstreamZuploJwtAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "headerName": "X-Service-Token",
      "tokenPrefix": "", // No prefix
      "expiresIn": "30m"
    }
  }
}
```

## Prerequisites

This policy requires the JWT Service Plugin to be configured in your Zuplo
project. The JWT service handles the cryptographic signing of tokens using your
project's private key.

## Security Considerations

1. **Token Expiration**: Keep token expiration times as short as practical for
   your use case
2. **Claims Validation**: Upstream services should validate JWT claims,
   especially the audience and expiration
3. **Claim Sensitivity**: Avoid including sensitive information in JWT claims as
   they can be decoded by anyone

## Troubleshooting

### Token Not Appearing in Request

Check that:

- The policy is correctly configured in your route
- The `headerName` matches what your upstream service expects
- No other policies are overwriting the header

### Invalid Token Errors

Verify that:

- Your upstream service can validate Zuplo-signed JWTs
- The token hasn't expired (check `expiresIn` setting)
- The audience claim matches what your upstream service expects

Read more about [how policies work](/articles/policies)
