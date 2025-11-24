# Source: https://grafbase.com/docs/platform/self-hosting/charts/postgres.md

# Postgres

This reference documents the Kubernetes configuration options for the PostgreSQL chart, which provides a PostgreSQL database for the Grafbase Enterprise Platform.

All configuration options are nested under the `postgresql` key.

> **Note**: As of v0.9.0, this is a custom chart using the official PostgreSQL Docker image (postgres:17) instead of the deprecated Bitnami chart. See the [v0.9.0 release notes](https://grafbase.com/docs/platform/self-hosting/release-notes/0.9.0.md) for migration information.

> **Important**: This chart is primarily intended for proof-of-concept deployments. For production use, we recommend using your own PostgreSQL infrastructure.

## global

Global configuration values for the chart.

**Defaults**:

```yaml
global:
  imagePullSecrets:
    - name: custom-pull-secret
  postgresql:
    auth:
      postgresPassword: ""
```

## image

Container image configuration for PostgreSQL.

**Defaults**:

```yaml
image:
  repository: postgres
  tag: "17.5"
  pullPolicy: IfNotPresent
```

## auth

Authentication configuration for the PostgreSQL database.

**Defaults**:

```yaml
auth:
  enablePostgresUser: true
  postgresPassword: grafbase
  username: ""      # Optional: create additional user
  password: ""      # Optional: password for additional user
  database: grafbase
```

## commonAnnotations

Common annotations for the PostgreSQL resources. Can be used to configure Helm hooks for deployment ordering.

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

## primary

Primary configuration for the PostgreSQL database.

**Defaults**:

```yaml
primary:
  resources:
    limits: {}
    requests: {}
```

**Example with resource limits**:

```yaml
primary:
  resources:
    limits:
      cpu: 2000m
      memory: 2000Mi
    requests:
      cpu: 1000m
      memory: 1000Mi
```

## service

Service configuration for exposing PostgreSQL.

**Defaults**:

```yaml
service:
  type: ClusterIP
  port: 5432
  nodePort: ""  # Only used when type is NodePort
```

## persistence

Persistence configuration for PostgreSQL data.

**Defaults**:

```yaml
persistence:
  enabled: true
  size: 8Gi
```

## initdbScripts

Custom initialization scripts to run when the database is first created.

**Defaults**:

```yaml
initdbScripts: {}
```

**Example**:

```yaml
initdbScripts:
  init.sql: |
    CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```