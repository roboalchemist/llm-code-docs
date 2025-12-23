# Source: https://github.com/weaviate/docs/blob/main/docs/weaviate/client-libraries/_components/client.auth.bearer.token.mdx

Any other OIDC authentication method can be used to obtain tokens directly from your identity provider, for example by using this step-by-step guide of the [hybrid flow](/weaviate/configuration/authz-authn).

If no `refresh token` is provided, there is no possibility to obtain a new `access token` and the client becomes unauthenticated after expiration.
