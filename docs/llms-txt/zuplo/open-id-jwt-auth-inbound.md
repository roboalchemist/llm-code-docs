# Source: https://www.zuplo.com/docs/policies/open-id-jwt-auth-inbound.md

# JWT Auth Policy

The Open ID JWT Authentication policy allows you to authenticate incoming
requests using an OpenID-compliant bearer token. It works with common
authentication services like Auth0 but should also work with any valid OpenID
JWT token.

When configured, Zuplo checks incoming requests for a JWT token and
automatically populates the `ZuploRequest`'s `user` property with a user object.
This `user` object will have a `sub` property - taking the `sub` id from the JWT
token. It will also have a `data` property populated by other data returned in
the JWT token (including any claims).

With this policy, you'll benefit from:

- **Universal Provider Support**: Works with any OpenID-compliant identity
  provider including Auth0, Okta, Azure AD, and more
- **Enhanced Security**: Validate token signatures, expiration, and claims to
  ensure only authorized users access your API
- **Flexible Configuration**: Easily customize token sources, audience
  validation, and required claims
- **Comprehensive User Context**: Access user identity and claims directly in
  your request handlers
- **Zero-Code Authentication**: Implement industry-standard authentication with
  simple configuration
- **Multiple Authentication Modes**: Support both required and optional
  authentication patterns
- **Seamless Integration**: Works with your existing OpenID infrastructure with
  minimal setup

See [this document](https://zuplo.com/docs/articles/oauth-authentication) for
more information about OAuth authorization in Zuplo.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-open-id-jwt-auth-inbound-policy",
  "policyType": "open-id-jwt-auth-inbound",
  "handler": {
    "export": "OpenIdJwtInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "audience": "$env(AUTH_AUDIENCE)",
      "issuer": "$env(AUTH_ISSUER)",
      "jwkUrl": "https://zuplo-demo.us.auth0.com/.well-known/jwks.json"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `open-id-jwt-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `OpenIdJwtInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `authHeader` <code className="text-green-600">&lt;string&gt;</code> - The name of the header with the key. Defaults to `"Authorization"`.
- `issuer` <code className="text-green-600">&lt;string&gt;</code> - The expected issuer claim in the JWT token.
- `audience` <code className="text-green-600">&lt;string&gt;</code> - The expected audience claim in the JWT token.
- `jwkUrl` <code className="text-green-600">&lt;string&gt;</code> - the url of the JSON Web Key Set (JWKS) - this is used to validate the JWT token signature (either this or `secret` must be set).
- `secret` <code className="text-green-600">&lt;string&gt;</code> - The key used to verify the signature of the JWT token (either this or `jwkUrl` must be set).
- `allowUnauthenticatedRequests` <code className="text-green-600">&lt;boolean&gt;</code> - indicates whether the request should continue if authentication fails. Defaults is `false` which means unauthenticated users will automatically receive a 401 response. Defaults to `false`.
- `subPropertyName` <code className="text-green-600">&lt;string&gt;</code> - The name of the property in the JWT token that contains the user's unique identifier.
- `headers` <code className="text-green-600">&lt;object&gt;</code> - Additional headers to send with the JWK request.
- `oAuthResourceMetadataEnabled` <code className="text-green-600">&lt;boolean&gt;</code> - Flag that determines whether OAuth protected resource metadata is enabled. Defaults to `false`.

## Using the Policy

This policy authenticates incoming requests using OpenID-compliant JWT bearer
tokens. It validates the token's signature, expiration, and claims against your
OpenID provider's configuration.

## Configuration

When setting up this policy, you'll need to configure your OpenID provider
details. Note that sometimes the `issuer` and `audience` will vary between your
environments (e.g. dev, staging and prod). We recommend storing these values in
your environment variables and using `$env(VARIABLE_NAME)` to include them in
your policy configuration.

:::note

Note you can have multiple instances of the same policy with different `name`s
if you want to have slightly different rules (such as settings for the
`allowUnauthenticatedRequests` setting).

:::

```json
{
  "path": "/products/:123",
  "methods": ["POST"],
  "handler": {
    "module": "$import(./modules/products)",
    "export": "postProducts"
  },
  "corsPolicy": "None",
  "version": "none",
  "policies": {
    "inbound": ["your-jwt-policy-name"]
  }
}
```

## Using the user property in code

After the policy validates a JWT token, it populates the `ZuploRequest`'s `user`
property with data from the token. You can access this in your request handlers:

```typescript
export async function myHandler(request: ZuploRequest, context: ZuploContext) {
  // Access the authenticated user information
  const userId = request.user?.sub;
  const userClaims = request.user?.data;

  // Use the user information in your business logic
  context.log.info(`Request from user: ${userId}`);

  // Continue processing
  return request;
}
```

For a complete example of using the user object in a
[RequestHandler](../handlers/custom-handler), see
[Setting up JWT auth with Auth0](../policies/auth0-jwt-auth-inbound).

Read more about [how policies work](/articles/policies)
