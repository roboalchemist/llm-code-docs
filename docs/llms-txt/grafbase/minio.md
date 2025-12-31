# Source: https://grafbase.com/docs/platform/self-hosting/charts/minio.md

# Minio

This reference documents the Kubernetes configuration options for the MinIO chart, which provides an S3 compatible object storage solution for the Grafbase platform.

All configuration options are nested under the `minio` key.

> **Note**: As of v0.9.0, the MinIO chart has been migrated from Bitnami to the official MinIO chart from https://charts.min.io/ (v5.4.0). See the [v0.9.0 release notes](https://grafbase.com/docs/platform/self-hosting/release-notes/0.9.0.md) for migration information.

> **Important**: This chart is primarily intended for proof-of-concept deployments. For production use, we recommend using AWS S3 or another cloud object storage service.

You can find the official MinIO chart documentation at [MinIO Helm Charts](https://min.io/docs/minio/kubernetes/upstream/).

## Configuration Changes from v0.8.x

The configuration structure has changed significantly:
- `auth.rootUser` → `rootUser`
- `auth.rootPassword` → `rootPassword`
- `defaultBuckets` → `buckets` (with expanded configuration)

## mode

Deployment mode for MinIO.

**Defaults**:

```yaml
mode: standalone
```

## rootUser

Root user for MinIO authentication (previously `auth.rootUser`).

**Defaults**:

```yaml
rootUser: grafbase
```

## rootPassword

Root password for MinIO authentication (previously `auth.rootPassword`).

**Defaults**:

```yaml
rootPassword: grafbase
```

## buckets

List of buckets to create during MinIO initialization.

**Defaults**:

```yaml
buckets:
  - name: grafbase
    policy: none
    purge: false
```

## resources

Resource requests for the MinIO container.

**Defaults**:

```yaml
resources:
  requests:
    memory: 256Mi
    cpu: 250m
```

## service

Service configuration for MinIO. Note that the structure differs from the Bitnami chart.

**Example for NodePort**:

```yaml
service:
  type: NodePort
  nodePorts:
    api: 30800
console:
  service:
    type: NodePort
    nodePorts:
      http: 30801
```