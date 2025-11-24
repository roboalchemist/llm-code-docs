# Source: https://grafbase.com/docs/platform/self-hosting/charts/clickhouse.md

# ClickHouse

This reference documents the Kubernetes configuration options for the ClickHouse chart, which provides an analytics database for the Grafbase Enterprise Platform.

All configuration options are nested under the `clickhouse` key.

> **Note**: As of v0.9.0, this is a custom chart using the official ClickHouse Docker image (clickhouse/clickhouse-server:24.11) instead of the deprecated Bitnami chart. See the [v0.9.0 release notes](https://grafbase.com/docs/platform/self-hosting/release-notes/0.9.0.md) for migration information.

> **Important**: This chart is primarily intended for proof-of-concept deployments. For production use, we recommend using your own ClickHouse infrastructure.

## image

Container image configuration for ClickHouse.

**Defaults**:

```yaml
image:
  repository: clickhouse/clickhouse-server
  tag: "24.11"
  pullPolicy: IfNotPresent
```

## replicas

Number of replicas for the ClickHouse deployment.

[Kubernetes ReplicationController Docs](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)

**Defaults**:

```yaml
replicas: 1
```

## auth

Authentication configuration for the ClickHouse database. The database is automatically created on startup.

**Defaults**:

```yaml
auth:
  username: grafbase
  password: grafbase
  database: analytics
```

## commonAnnotations

Common annotations for the ClickHouse resources. Can be used to configure Helm hooks for deployment ordering.

[Kubernetes Common Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)

**Defaults**:

```yaml
commonAnnotations: {}
```

**Example with hooks**:

```yaml
commonAnnotations:
  'helm.sh/hook': pre-install
  'helm.sh/hook-weight': '-15'
```

## service

Service configuration for exposing ClickHouse.

**Defaults**:

```yaml
service:
  type: ClusterIP
  httpPort: 8123      # HTTP interface port
  nativePort: 9000    # Native protocol port
  httpNodePort: ""    # Only used when type is NodePort
  nativeNodePort: ""  # Only used when type is NodePort
```

## persistence

Persistence configuration for ClickHouse data.

**Defaults**:

```yaml
persistence:
  enabled: true
  size: 8Gi
```

## resources

Resource requests and limits for the ClickHouse container.

**Defaults**:

```yaml
resources:
  requests:
    cpu: 1
    memory: 1024Mi
  limits:
    cpu: 1
    memory: 2048Mi
```