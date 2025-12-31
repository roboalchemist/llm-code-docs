# Source: https://grafbase.com/docs/platform/self-hosting/charts/api.md

# Source: https://grafbase.com/docs/platform/api.md

# Source: https://grafbase.com/docs/platform/self-hosting/charts/api.md

# Source: https://grafbase.com/docs/platform/api.md

# Source: https://grafbase.com/docs/platform/self-hosting/charts/api.md

# Source: https://grafbase.com/docs/platform/api.md

# Source: https://grafbase.com/docs/platform/self-hosting/charts/api.md

# Source: https://grafbase.com/docs/platform/api.md

# Source: https://grafbase.com/docs/platform/self-hosting/charts/api.md

# Source: https://grafbase.com/docs/platform/api.md

# Grafbase API

The [Grafbase Dashboard](/dashboard) is powered by the Grafbase API. This same API is available for users to manage their account and projects programmatically.

Everything you have access to do inside the Grafbase Dashboard can be done using the Grafbase API.

**This API is always changing and may introduce breaking changes at any point.**

## Endpoint

You make GraphQL requests to: `https://api.grafbase.com/graphql`

## Auth

You will need a valid [Access Token](https://grafbase.com/docs/gateway/security/access-tokens.md) that you will need to pass as an `Authorization` header.

The header should the Bearer authentication format:

`Authorization: Bearer TOKEN`

## Schema

The Grafbase API endpoint has introspection enabled so you can use any GraphQL Playground (Postman, Insomnia, GraphiQL) to view the schema documentation.  

Or you can view it online right [here](/api-docs)