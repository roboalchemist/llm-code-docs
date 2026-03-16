# Source: https://www.apollographql.com/docs/apollo-operator/resources/supergraph/networking.md

# Supergraph networking

The `spec.networking` section of your **Supergraph** resource allows you to customize the networking configuration of the underlying **Pod**s, **Service**, and Apollo Router instances.

## Properties

### `containerPort`

The port that the router containers will listen on. Changing this automatically modifies the Apollo Router configuration on your behalf.

**Default value**: 4000.

```yaml
spec:
  networking:
    containerPort: 4000
```

### `healthCheckPort`

The port that will be used for health checks against router containers. Changing this automatically modifies the Apollo Router, livenessProbe, and readinessProbe on your behalf.

**Default value**: 8088.

```yaml
spec:
  networking:
    healthCheckPort: 8088
```

### `metricsPort`

The port to use for exporting Prometheus metrics. If this is not specified, Router instances will not expose metrics via a Prometheus endpoint.

```yaml
spec:
  networking:
    metricsPort: 9090
```

### `servicePort`

The port that the supergraph service will listen on.

**Default value**: 80

```yaml
spec:
  networking:
    servicePort: 80
```

### `serviceType`

Determines how the underlying Service is exposed. This maps to the `.spec.type` field on the underlying **Service**.

**Default value**: ClusterIp.

```yaml
spec:
  networking:
    serviceType: ClusterIp
```
