# Source: https://www.apollographql.com/docs/apollo-operator/configuration/controllers.md

# Controllers Configuration

The `controllers` section configures the behavior of the Apollo GraphOS Operator's controllers.

## Configuration

```yaml
controllers:
  common:
    requeueDelays:
      onError: "60s"
      onMissingData: "60s"
      onPending: "5s"
  subgraph:
    expirations:
      schema: "60s"
    namespaces: []
  supergraph:
    expirations:
      schema: "60s"
    namespaces: []
    loaderImage: "localhost:5000/bundle-loader:latest"
  supergraphSchema:
    namespaces: []
```

## Common Configuration

| Field                                | Type     | Default | Description                                     |
| ------------------------------------ | -------- | ------- | ----------------------------------------------- |
| `common.requeueDelays.onError`       | `string` | `"60s"` | Requeue delay after errors                      |
| `common.requeueDelays.onMissingData` | `string` | `"60s"` | Requeue delay when data is missing              |
| `common.requeueDelays.onPending`     | `string` | `"5s"`  | Requeue delay when waiting for external systems |

## Subgraph Controller

| Field                         | Type     | Default | Description                       |
| ----------------------------- | -------- | ------- | --------------------------------- |
| `subgraph.expirations.schema` | `string` | `"60s"` | Schema cache expiration time      |
| `subgraph.namespaces`         | `array`  | `[]`    | Namespaces to watch (empty = all) |

## Supergraph Controller

| Field                           | Type     | Default                                 | Description                       |
| ------------------------------- | -------- | --------------------------------------- | --------------------------------- |
| `supergraph.expirations.schema` | `string` | `"60s"`                                 | Schema cache expiration time      |
| `supergraph.namespaces`         | `array`  | `[]`                                    | Namespaces to watch (empty = all) |
| `supergraph.loaderImage`        | `string` | `"localhost:5000/bundle-loader:latest"` | Bundle loader image               |

## SupergraphSchema Controller

| Field                         | Type    | Default | Description                       |
| ----------------------------- | ------- | ------- | --------------------------------- |
| `supergraphSchema.namespaces` | `array` | `[]`    | Namespaces to watch (empty = all) |

## Examples

### Multi-Namespace Setup

```yaml
controllers:
  subgraph:
    namespaces: ["team-a", "team-b", "team-c"]
  supergraph:
    namespaces: ["apollo"]
  supergraphSchema:
    namespaces: ["apollo"]
```
