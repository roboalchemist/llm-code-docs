# Source: https://grafbase.com/docs/cli/commands/mcp.md

# Source: https://grafbase.com/docs/gateway/configuration/mcp.md

# Source: https://grafbase.com/docs/gateway/mcp.md

# Source: https://grafbase.com/docs/cli/commands/mcp.md

# Source: https://grafbase.com/docs/gateway/configuration/mcp.md

# Source: https://grafbase.com/docs/gateway/mcp.md

# Source: https://grafbase.com/docs/cli/commands/mcp.md

# Source: https://grafbase.com/docs/gateway/configuration/mcp.md

# Source: https://grafbase.com/docs/gateway/mcp.md

# Source: https://grafbase.com/docs/cli/commands/mcp.md

# Source: https://grafbase.com/docs/gateway/configuration/mcp.md

# Source: https://grafbase.com/docs/gateway/mcp.md

# Source: https://grafbase.com/docs/cli/commands/mcp.md

# Source: https://grafbase.com/docs/gateway/configuration/mcp.md

# Source: https://grafbase.com/docs/gateway/mcp.md

# Model Context Protocol

MCP is a new protocol, launched in November 2024 by [Anthropic](https://anthropic.com), designed to make structured data explorable and actionable via natural language. Grafbase offers MCP support out of the box - removing the need to stand up your own standalone MCP server, configure authentication, or fine-tune access control.

<Image
  src="/images/docs/mcp/card-mcp--dark.png"
  alt="MCP in Grafbase"
  width={604}
  height={479}
  priority="true"
/>

## Get started with Cursor

The Grafbase MCP server can be started with the [Grafbase CLI](https://grafbase.com/docs/cli/installation.md) by running:

```bash
npx grafbase mcp <url>
```

The MCP server listens to requests at `http://127.0.0.1:5000/mcp` by default. To add it to Cursor, create a `.cursor/mcp.json` file in your project with the following:

```json
{
  "mcpServers": {
    "my-graphql-api": {
      "url": "http://127.0.0.1:5000/mcp"
    }
  }
}
```

## Setting up Grafbase Gateway as a remote MCP server

The [Grafbase Gateway](https://grafbase.com/docs/gateway/installation.md) can be configured to expose a MCP endpoint with the following `grafbase.toml` configuration:

```toml
[mcp]
enabled = true # defaults to false
# Path at which to expose the MCP service
path = "/mcp"
# Whether mutations can be executed
execute_mutations = false
# Either "http-streaming" or "sse". The default is "http-streaming".
transport = "http-streaming"
```

This gives you an MCP endpoint that exposes the relevant tools to explore and query your GraphQL API. When executing GraphQL requests, all HTTP headers are forwarded from the MCP request, as if you were querying the `/graphql` endpoint on your Gateway with a regular GraphQL client. That means that authentication and authorization are enforced in exactly the same way. But if you plan to expose this MCP endpoint as a spec-compliant MCP server, you will need to configure the Gateway to implement the [Authorization section of the MCP spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization).

## Implementing MCP Authorization

The [MCP spec defines an OAuth 2.1 based authorization flow](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization). The MCP endpoint enabled with the configuration in the previous section must be secured as an OAuth 2 protected resource. You will also need an external OAuth 2 authorization server, as part of your own infrastructure or SaaS authentication solution. See for example the [WorkOS  AuthKit docs](https://workos.com/docs/user-management/mcp). The following sections walk you through the features to be addressed:

## Authentication

Authentication is handled the same way as for your GraphQL API endpoint: [with extensions](https://grafbase.com/docs/gateway/security/authentication.md).

You can either secure both the MCP endpoint and your GraphQL endpoint with the same authentication extension:

```toml
[extensions.jwt]
version = "1"
config.url = "https://example.com/sso/jwks"
```

Or separately for the MCP endpoint and the GraphQL endpoint:

```toml
[authentication.protected_resources.graphql]
extensions = []
default = "anonymous" # superfluous here, it's the default with no extension

[authentication.protected_resources.mcp]
extensions = ["jwt"]
default = "deny" # matches the default when at least one extension is defined

[extensions.jwt]
version = "1"
config.url = "https://example.com/sso/jwks"
```

For more details, see the [configuration reference section on authentication](https://grafbase.com/docs/gateway/configuration/authentication.md).

## OAuth 2.0 Protected Resource Metadata

The MCP server must expose metadata as defined in [RFC-9728](https://datatracker.ietf.org/doc/html/rfc9728). Concretely, it is a static JSON document served at a standard defined path ("/.well-known/oauth-protected-resource"), or an arbitrary path in combination with the `resource_metadata` field of the `WWW-Authenticate` header (see below).

The open source authentication extensions on the Marketplace all implement OAuth Protected Resource metadata through configuration. See the [README of the jwt extension](/extensions/jwt) for example.

If you implement authentication with your own extension, you will only need to implement the `public_metadata()` method on `AuthenticationExtension`. See [how the jwt extension does it for a working example](https://github.com/grafbase/extensions/blob/56a1d874d6d49c3a96218d58fc08540a58d8aa39/extensions/jwt/src/lib.rs#L76).

## WWW-Authenticate header

The MCP spec requires the presence of the WWW-Authenticate header in the response to unauthenticated requests. This header should contain the value "Bearer" to indicate that the resource is protected by OAuth 2.0.

Again, authentication extensions from the marketplace all let you configure what is returned in that header, and you can implement that in your own extensions with `ErrorResponse::with_header()`.

## CORS

If you want to expose your MCP server to clients inside web browsers, you will need to include the `mcp-protocol-version` header in `allow_headers`. Here is an example of what it looks like in your Gateway configuration (`grafbase.toml`):

```toml
[cors]
allow_origins = "any"
allow_methods = ["GET", "POST"]
allow_headers = [
  "authorization",
  "content-type",
  "x-grafbase-client-name",
  "x-grafbase-client-version",
  "mcp-protocol-version"
]
```

## Schema contracts

[Schema contract](https://grafbase.com/docs/gateway/security/schema-contracts.md) can be used to control which subset of your API you want to expose to your agents either statically or dynamically.