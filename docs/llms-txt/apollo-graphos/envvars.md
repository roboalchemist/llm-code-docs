# Source: https://www.apollographql.com/docs/graphos/routing/configuration/envvars.md

# Router Environment Variable Configuration Reference

This reference covers the environment variables for configuring an Apollo Router.

## Environment variables

This section lists and describes the environment variables you can set when running the `router` binary.

These environment variables apply only if your supergraph schema is managed by GraphOS.

When running Apollo Router locally with a schema fetched from Uplink, the API key must have at least the Observer role; keys with lower privileges cannot retrieve the schema.

Environment Variable
Description

##### `APOLLO_GRAPH_REF`

The graph ref for the GraphOS graph and variant that the router fetches its supergraph schema from (e.g., `docs-example-graph@staging`).

**Required** when using [managed federation](https://www.apollographql.com/docs/federation/managed-federation/overview/), except when using an [offline license](https://www.apollographql.com/docs/graphos/routing/license/#offline-license) to run the router.

##### `APOLLO_KEY`

The [graph API key](https://www.apollographql.com/docs/graphos/api-keys/#graph-api-keys) that the router should use to authenticate with GraphOS when fetching its supergraph schema.

**Required** when using [managed federation](https://www.apollographql.com/docs/federation/managed-federation/overview/), except when using an [offline license](https://www.apollographql.com/docs/graphos/routing/license/#offline-license) to run the router or when using `APOLLO_KEY_PATH`.

##### `APOLLO_KEY_PATH`

⚠️ **This is not available on Windows.**

A path to a file containing the [graph API key](https://www.apollographql.com/docs/graphos/api-keys/#graph-api-keys) that the router should use to authenticate with GraphOS when fetching its supergraph schema.

**Required** when using [managed federation](https://www.apollographql.com/docs/federation/managed-federation/overview/), except when using an [offline license](https://www.apollographql.com/docs/graphos/routing/license/#offline-license) to run the router or when using `APOLLO_KEY`.

##### `APOLLO_GRAPH_ARTIFACT_REFERENCE`

An OCI reference to a graph artifact that contains the supergraph schema. The reference must use a SHA256 digest format.

When you set this option, the router uses the schema from the specified graph artifact instead of Apollo Uplink. The router still fetches entitlements and persisted queries from Uplink.

For information on finding graph artifact references, see [Graph Artifacts](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/graph-artifacts#find-oci-artifact-references).

##### `APOLLO_GRAPH_ARTIFACT_UNSECURE_HOSTS`

A comma-separated list of registry hostnames to use HTTP instead of HTTPS when fetching graph artifacts.

When this variable is not set, Router defaults to allowing HTTP for `localhost`, `127.0.0.1`, and `dockerhost`.

When this variable is set to a non-empty value, only the specified hosts use HTTP and the defaults are replaced. For example, to allow HTTP for a custom internal registry and `localhost`:

```bash
APOLLO_GRAPH_ARTIFACT_UNSECURE_HOSTS="internal.registry.corp,localhost"
```

When this variable is set to an empty string (`""`), all HTTP overrides are disabled, requiring HTTPS for every registry, including localhost.

## Example command

To use environment variables when running router, you must set them before the `router` command:

```bash title=Using a graph ref
APOLLO_KEY="..." APOLLO_GRAPH_REF="..." ./router
```

```bash title=Using a graph artifact reference
APOLLO_KEY="..." APOLLO_GRAPH_ARTIFACT_REFERENCE="artifact.api.apollographql.com/my-graph-a50b9d546b298e5a@sha256:14409db3d8a8d74ff9e9a0b5712c0aa8d574bcacc3656e1bc0c55ecf97cd9264" ./router
```
