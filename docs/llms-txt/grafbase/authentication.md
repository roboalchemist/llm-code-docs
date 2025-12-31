# Source: https://grafbase.com/docs/gateway/configuration/authentication.md

# Source: https://grafbase.com/docs/gateway/security/authentication.md

# Source: https://grafbase.com/docs/gateway/configuration/authentication.md

# Source: https://grafbase.com/docs/gateway/security/authentication.md

# Source: https://grafbase.com/docs/gateway/configuration/authentication.md

# Source: https://grafbase.com/docs/gateway/security/authentication.md

# Source: https://grafbase.com/docs/gateway/configuration/authentication.md

# Source: https://grafbase.com/docs/gateway/security/authentication.md

# Source: https://grafbase.com/docs/gateway/configuration/authentication.md

# Source: https://grafbase.com/docs/gateway/security/authentication.md

# Authentication

Authentication extensions are available in the [Marketplace](/extensions):

- [JWT](/extensions/jwt): Validates a JWT token

You can learn how authentication extensions work and build your own with this follow along tutorial: [Customize your GraphQL Federation authentication and authorization with Grafbase Extensions](/blog/custom-authentication-and-authorization-in-graphql-federation).

A complete example can be found on [GitHub](https://github.com/grafbase/grafbase/tree/main/examples/authorization) and the [Grafbase SDK](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/) is the extension reference.

## OAuth

The Grafbase Gateway can act as an [OAuth 2.1 protected resource](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-12.html#name-roles) server. A protected resource server has two responsibilities: enforcing access control (authentication and authorization), and exposing [metadata (RFC 9728)](https://datatracker.ietf.org/doc/html/rfc9728).

The open source extensions in the [Extensions Marketplace](/extensions), like the [JWT extension](/extensions/jwt), have out of the box support for this spec. Check out the relevant READMEs for configuration options.

If you want an extension only in order to expose protected resource metadata — for example if authentication is enforced at the subgraph level —, you can use the [OAuth 2.0 Protected Resource Metadata](/extensions/oauth-protected-resource) extension.