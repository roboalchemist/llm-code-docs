# Source: https://grafbase.com/docs/platform/self-hosting/charts/zitadel.md

# Zitadel

**Note**: the use of Zitadel is being deprecated in favor of [integrating directly with your own OpenID connect compliant IdP](https://grafbase.com/docs/platform/self-hosting/single-sign-on.md).

This reference documents the Kubernetes configuration options for the Zitadel, which provides an identity and access management solution for the Grafbase platform.

All configuration options are nested under the `zitadel` key.

You can find the Zitadel chart source code from the [GitHub repository](https://github.com/zitadel/zitadel-charts/blob/main/charts/zitadel/values.yaml).

## enabled

Enable or disable the Zitadel chart.

**Defaults**:

```yaml
enabled: true
```

## replicaCount

[Kubernetes ReplicationController Docs](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)

**Defaults**:

```yaml
replicaCount: 1
```

## resources

Resource requests and limits for the Zitadel container.

**Defaults**:

```yaml
resources:
  limits:
    cpu: 1000m
    memory: 2000Mi
  requests:
    cpu: 1000m
    memory: 1000Mi
```

## setupJob

Resource requests and limits for the Zitadel setup job.

**Defaults**:

```yaml
setupJob:
  resources:
    limits:
      cpu: 1000m
      memory: 1000Mi
    requests:
      cpu: 1000m
      memory: 500Mi
```

## zitadel

Zitadel configuration options.

**Defaults**:

```yaml
zitadel:
  masterkey: x123456789012345678901234567891y
  configmapConfig:
    ExternalSecure: false
    ExternalDomain: grafbase-enterprise-platform-zitadel
    ExternalPort: 30550
    TLS:
      Enabled: false
    Database:
      Postgres:
        Host: grafbase-enterprise-platform-postgresql
        Port: 5432
        Database: grafbase
        User:
          Username: postgres
          SSL:
            Mode: disable
        Admin:
          Username: postgres
          SSL:
            Mode: disable
    FirstInstance:
      Org:
        Machine:
          Machine:
            Username: zitadel-admin-sa
            Name: Admin
          MachineKey:
            ExpirationDate: '9999-01-01T00:00:00Z'
            # Type: 1 means JSON. This is currently the only supported machine key type.
            Type: 1

  secretConfig:
    Database:
      postgres:
        Host: grafbase-enterprise-platform-postgresql
        Port: 5432
        Database: grafbase
        User:
          Username: postgres
          Password: grafbase
          SSL:
            Mode: disable
        Admin:
          Username: postgres
          Password: grafbase
          ExistingDatabase: grafbase
          SSL:
            Mode: disable
```