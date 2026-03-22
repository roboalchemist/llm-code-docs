# Source: https://www.apollographql.com/docs/apollo-mcp-server/guides/dev-to-prod-workflows.md

# Development to Production Workflows

This guide outlines how to work with your Apollo MCP Server in development, staging, and production environments. For each environment, your workflow differs in how you define and manage your tools, deploy your server, and configure additional settings.

* **Local development:** Define operations as local files, run your MCP server locally with `rover dev`, and test.
* **Dev and staging environments:** Publish schema to graph variants, manage tools using operation collections, deploy and test.
* **Production environments:** Choose your operation source (files or persisted queries), configure authentication, deploy, test, and monitor.

## Local development

1. Define tools using [local operation files](https://www.apollographql.com/docs/apollo-mcp-server/define-tools#from-operation-files).

   ```yaml title=Example MCP config file
   operations:
     source: local
   paths:
     - ./operations/local.graphql
   ```

2. Run your MCP server locally using `rover dev`, alongside your GraphQL API.

   ```bash
   rover dev --supergraph-config supergraph.yaml --mcp .apollo/mcp.local.yaml
   ```

   You can also run the MCP server using [Docker](https://www.apollographql.com/docs/apollo-mcp-server/deploy#with-docker) or the [binary](https://www.apollographql.com/docs/apollo-mcp-server/run#standalone-mcp-server-binary).

3. Test your tools using [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) or [connect the server to an AI agent](https://www.apollographql.com/docs/apollo-mcp-server/quickstart#step-3-connect-to-an-mcp-client).

## Dev and staging environments

1. [Create separate graph variants](https://www.apollographql.com/docs/graphos/platform/graph-management/variants) for dev and staging.

2. [Publish your schema](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publishing) to each variant.

3. Define tools using [operation collections](https://www.apollographql.com/docs/apollo-mcp-server/define-tools#from-operation-collections).

   Create and organize operations per graph variant. Then, configure your MCP server to use the collection.

   ```yaml title=Example MCP config file using operation collections
   operations:
     source: collection
     id: default
   ```

4. [Deploy an MCP server](https://www.apollographql.com/docs/apollo-mcp-server/deploy) pointing to each variant.

5. [Connect your AI agent](https://www.apollographql.com/docs/apollo-mcp-server/quickstart#step-3-connect-to-an-mcp-client) to each environment and validate behavior.

## Production environments

1. Define your tools using either [local operation files](https://www.apollographql.com/docs/apollo-mcp-server/define-tools#from-operation-files) or [persisted queries](https://www.apollographql.com/docs/apollo-mcp-server/define-tools#from-graphos-managed-persisted-queries).

   **Using local operation files**

   * Store operations in your git repository
   * Operations are version-controlled and reviewed in PRs before deployment
   * Use CI/CD to validate and deploy
   * See [Define Tools > From operation files](https://www.apollographql.com/docs/apollo-mcp-server/define-tools#from-operation-files)

   ```yaml title=Example MCP config file
   operations:
     source: local
   paths:
     - ./operations/local.graphql
   ```

   **Using persisted queries**

   * Publish operations to a [persisted query list](https://www.apollographql.com/docs/graphos/platform/security/persisted-queries)
   * Configure [safelisting with persisted queries](https://www.apollographql.com/docs/graphos/routing/security/persisted-queries), so that the router enforces that only registered operations can execute
   * Use CI/CD to publish operations to the persisted query list
   * See [Define Tools > From GraphOS-managed persisted queries](https://www.apollographql.com/docs/apollo-mcp-server/define-tools#from-graphos-managed-persisted-queries)

   ```yaml title=Example MCP config file
   operations:
     source: uplink
   ```

   You will also need to set your graph credentials `APOLLO_GRAPH_REF` and `APOLLO_KEY` as environment variables.

2. [Configure authentication](https://www.apollographql.com/docs/apollo-mcp-server/auth) in your MCP server.

3. [Disable introspection tools](https://www.apollographql.com/docs/apollo-mcp-server/config-file#introspection).

4. [Deploy the MCP Server](https://www.apollographql.com/docs/apollo-mcp-server/deploy) using container-based deployment to your infrastructure.

5. Monitor your MCP server using:

   * GraphOS Studio: View operation metrics and usage patterns in [Insights](https://www.apollographql.com/docs/graphos/platform/insights)
   * OpenTelemetry: Instrument for traces, metrics, and logs by [configuring telemetry](https://www.apollographql.com/docs/apollo-mcp-server/telemetry)
