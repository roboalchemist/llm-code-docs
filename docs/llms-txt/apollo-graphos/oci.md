# Source: https://www.apollographql.com/docs/apollo-operator/configuration/oci.md

# OCI Configuration

The `oci` section configures settings for Open Container Initiative (OCI) registries. The Apollo GraphOS Operator uses OCI registries to fetch GraphQL schemas that are stored as OCI artifacts, such as when a subgraph or supergraph references an `ociImage` or `oci` source.

## Configuration

| Field                  | Type    | Default | Description                              |
| ---------------------- | ------- | ------- | ---------------------------------------- |
| `http_only_registries` | `array` | `[]`    | Registries exempt from HTTPS requirement |

## Example

```yaml
oci:
  http_only_registries:
    - "localhost:5000"
    - "registry.local:5000"
```

## Use Cases

### Local Development

```yaml
oci:
  http_only_registries:
    - "localhost:5000"
```

### Internal Registries

```yaml
oci:
  http_only_registries:
    - "registry.internal.company.com"
    - "dev-registry.company.com"
```

## Security Considerations

⚠️ **Warning**: Using HTTP-only registries can expose your container images to security vulnerabilities. Only use in:

* Local development environments
* Isolated internal networks
* Testing environments with controlled access

For production, always use HTTPS-enabled registries.
