# Source: https://www.apollographql.com/docs/graphos/connectors/getting-started/version-requirements.md

# Version Requirements

Your graph's build and runtime components must meet specific version requirements to compose and run a graph with Apollo Connectors.
This page outlines the compatibility requirements and provides upgrade recommendations.

## Version requirements

To use Apollo Connectors, your schemas must import the [Connector specification](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives#connector-specification) and [Connectors directives](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives#connect) like so:

```graphql
extend schema
  @link(
    url: "https://specs.apollo.dev/connect/v0.2"
    import: ["@connect", "@source"]
  )
```

Each Connector specification version (`v0.2` above, for example) requires:

* A minimum GraphOS Router version
* A minimum GraphOS build pipeline version
  * The build pipeline collects subgraph schemas and composes them into a unified supergraph. For that reason, it's sometimes referred to as the "composition pipeline."
  * You set the build pipeline version in GraphOS Studio from a graph's **Settings** page in the **Build pipeline** section.
* A minimum Apollo Federation specification version

  * You import the Federation specification and any necessary directives in your schema like so:

  ```graphql
  extend schema
    @link(
      url: "https://specs.apollo.dev/federation/v2.11"
      import: ["@key"]
    )
  ```

Refer to the compatibility table below for details.

### Connector compatibility matrix

| Connect Spec Version | Minimum Router Version | Minimum Build Pipeline Version | Minimum Federation Spec Version |
| -------------------- | ---------------------- | ------------------------------ | ------------------------------- |
| 0.1                  | 2.0                    | 2.10                           | 2.10                            |
| 0.2                  | 2.3                    | 2.11                           | 2.11                            |

## Upgrade recommendations

Apollo recommends upgrading your Connector Specification version only when functionality from a newer version is needed.
Upgrading may require a corresponding update to your router, build pipeline, and Federation spec versions.

Subgraphs aren't required to match their supergraph's build pipeline version.
They can use the same or an earlier version—unless they're using Connector directives, which require Federation v2.10 or later. That means:

* You don't need to update every subgraph whenever you update your build pipeline version.
* Only subgraph schemas using the [Connector directives](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives) must use Federation v.2.10.0 or later.
* Subgraphs that don't use Connectors can stay on an older Federation version.

Learn more about the [recommended update order](https://www.apollographql.com/docs/graphos/platform/graph-management/updates#recommended-update-order) for your supergraph.
