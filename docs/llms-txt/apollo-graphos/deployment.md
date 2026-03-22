# Source: https://www.apollographql.com/docs/graphos/connectors/deployment.md

# Connectors Deployment Overview

This overview walks through end-to-end deployment workflow for Apollo Connectors.
First, it's helpful to understand Connectors' architectural approach and what this means for deployment.

## Connectors architectural approach

Unlike traditional GraphQL implementations, Connectors don't require you to deploy GraphQL servers. Instead, you manage:

* **GraphQL schema files**: Define your API and publish to GraphOS (stored in your source control)
* **GraphOS Router configuration**: YAML files that configure your graph's runtime (also in source control)
* **Router runtime**: The executable binary that you deploy to your infrastructure

### The GraphOS Router

The GraphOS Router serves as the runtime environment that powers your Connectors implementation. It's a high-performance service that:

* Receives GraphQL operations from your clients
* Creates and executes a query plan to retrieve data from your backend services
* Assembles responses from multiple sources into a single response for the client
* Handles authentication, caching, and other cross-cutting concerns

Since Connectors eliminate the need for passthrough GraphQL servers, deployment focuses solely on hosting and running the router.

## Deployment workflow

The deployment workflow for a graph with Apollo Connectors involves:

1. **Local development** - Define your GraphQL schema using Connectors
2. **Router configuration** - Configure the GraphOS Router for your security, performance, and observability needs; you can also include variables in your configuration that you use in your schema when configuring requests.
3. **Schema publication and management** - Publish schema updates to GraphOS
4. **Router deployment** - Deploy the GraphOS Router to your infrastructure

### Local development

During local development, you:

* Create GraphQL schema files with Connectors directives
* Test queries locally using the router's dev mode
* Iterate on your schema design

The Rover CLI provides [the `dev` command](https://www.apollographql.com/docs/rover/commands/dev) to validate your schema and run a local development server.

### Router configuration

The GraphOS Router uses a declarative YAML configuration model that provides control over:

```yaml title=router.yaml
supergraph:
  listen: 0.0.0.0:4000
headers:
  all:
    request:
      - insert:
          name: "x-api-key"
          value: "${env.API_KEY}"
```

Key configuration areas include:

* **Security**, including authentication, TLS settings, and request limits
* **Performance**, including traffic management and shaping, caching strategies, and batching and deduplication
* **Observability**, including logging configuration, telemetry, and distributed tracing

All [router configurations](https://www.apollographql.com/docs/graphos/routing/configuration/yaml) are supported for graphs using Connectors, except for those [documented in the limitations](https://www.apollographql.com/docs/graphos/connectors/reference/limitations#interactions-with-graphos-router-features).

### Schema publication

Publishing your schema to GraphOS involves:

* Using Rover to [`publish` schema changes](https://www.apollographql.com/docs/rover/commands/subgraphs#publishing-a-subgraph-schema-to-graphos)
* Integrating schema checks into [CI/CD pipelines](https://www.apollographql.com/docs/rover/ci-cd)

See the [Schema Publishing overview](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publishing) for more information.

### Router deployment

The GraphOS Router is a lightweight, Rust-based service that can be deployed alongside your existing infrastructure:

* **[Docker](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/docker)** - Run the router as a containerized application
* **[Kubernetes](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/kubernetes)** - Deploy using Kubernetes manifests or Helm charts
* **Cloud services**:
  * **[AWS](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/aws)** - Deploy on ECS or other AWS services
  * **[Azure](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/azure)** - Run as an Azure Container App
  * **[GCP](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/gcp)** - Deploy with Google Cloud Run

## Deployment best practices

Best practices for this workflow include:

* **Version control** - Store your schema and router configuration in source control
* **Environment management** - Use separate graph variants for each environment and configure environment-specific values

### Environment management

Each variant has its own schemas, along with its own change history and metrics.

You can use environment variables to manage different values per environment:

```yaml title=router.yaml
supergraph:
  listen: 0.0.0.0:${env.PORT:-4000}

headers:
  all:
    request:
      - insert:
          name: "x-api-key"
          value: "${env.API_KEY}"  # Different per environment

connectors:
  sources:
    products:
      url: "${env.PRODUCTS_API_URL}"  # Different URL per environment
```

## Next steps

* Learn more about how you can use [router configurations](https://www.apollographql.com/docs/graphos/connectors/deployment/configuration) to override [request URLs](https://www.apollographql.com/docs/graphos/connectors/deployment/overriding-base-urls) and [headers](https://www.apollographql.com/docs/graphos/connectors/deployment/overriding-headers)
* Refer to [environment best practices](https://www.apollographql.com/docs/graphos/platform/production-readiness/environment-best-practices) for more detailed guidance on environments
* Explore [router deployment options](https://www.apollographql.com/docs/graphos/routing/self-hosted) for your infrastructure
* Set up [monitoring and observability](https://www.apollographql.com/docs/graphos/connectors/observability) for your deployed Connectors
