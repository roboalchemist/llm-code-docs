# Source: https://grafbase.com/docs/gateway/security/authorization.md

Authorization extensions are available in the [Marketplace](/extensions):

- [Authenticated](/extensions/authenticated): Restrict access to unauthenticated clients.
- [Requires Scopes](/extensions/requires-scopes): Grant access only to clients with appropriate OAuth scopes.

You can learn how authorization extensions work and build your own with this follow along tutorial: [Customize your GraphQL Federation authentication and authorization with Grafbase Extensions](/blog/custom-authentication-and-authorization-in-graphql-federation).

A complete example can be found on [GitHub](https://github.com/grafbase/grafbase/tree/main/examples/authorization) and the [Grafbase SDK](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/) is the extension reference.