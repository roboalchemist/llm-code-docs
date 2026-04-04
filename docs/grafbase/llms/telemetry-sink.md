# Source: https://grafbase.com/docs/platform/self-hosting/charts/telemetry-sink.md

# Telemetry Sink

This reference documents the Kubernetes configuration options for the Telemetry Sink, which authorizes and collects telemetry data from the platform and sends it to the message broker.

## replicaCount

[Kubernetes ReplicationController Docs](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)

**Defaults**:

```yaml
replicaCount: 1
```

## serviceAccount

[Kubernetes Service Account Docs](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

**Defaults**:

```yaml
serviceAccount:
  # Controls service account creation
  create: true
  # Annotations to add to the service account
  annotations: {}
  # Service account name. Uses default if not set
  name: ''
```

## service

[Kubernetes Service Types](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)

**Defaults**:

```yaml
service:
  # Service type (e.g. ClusterIP, NodePort, LoadBalancer)
  type: ClusterIP
  # Port to expose service on
  port: 80
  # Port that the service targets on the pods
  targetPort: 4317
  # Name of the service port
  name: http
  # Port exposed on each node for NodePort type
  nodePort: 30431
```

## ingress

[Kubernetes Ingress Docs](https://kubernetes.io/docs/concepts/services-networking/ingress/)

**Defaults**:

```yaml
ingress:
  # Enables ingress
  enabled: false
  # Ingress class
  className: 'nginx'
  hosts:
    # Hostnames and paths for the ingress
    - host: telemetry-sink.local
      paths:
        - path: /*
          pathType: ImplementationSpecific
          backend:
            serviceName: telemetry-sink
            servicePort: 4317
```

## autoscaling

[Kubernetes Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

**Defaults**:

```yaml
autoscaling:
  # Enables autoscaling
  enabled: true
  # Minimum number of replicas
  minReplicas: 1
  # Maximum number of replicas
  maxReplicas: 2
  # Target CPU utilization percentage
  targetCPUUtilizationPercentage: 50
```

## configmap

Configuration values for the cluster configmap.

**Defaults**:

```yaml
configmap:
  # Controls configmap creation
  enabled: true
  name: ''
  values:
    # Address and port for the telemetry sink to listen on
    GRAFBASE_TELEMETRY_SINK_LISTEN_ADDRESS: 0.0.0.0:4317
    # Log level
    RUST_LOG: info
    # PostgreSQL acquire timeout in seconds
    PG_ACQUIRE_TIMEOUT_SECS: 5
    # PostgreSQL connect timeout in seconds
    PG_CONNECT_TIMEOUT_SECS: 5
    # PostgreSQL connection maximum lifetime in seconds
    PG_CONNECTION_MAX_LIFETIME_SECS: 3600
    # PostgreSQL idle timeout in seconds
    PG_IDLE_TIMEOUT_SECS: 300
    # PostgreSQL maximum number of connections
    PG_MAX_CONNECTIONS: 15
    # PostgreSQL minimum number of connections
    PG_MIN_CONNECTIONS: 1
    # Kafka topic name for metrics
    GRAFBASE_OTEL_KAFKA_TOPIC_METRICS: otlp_metrics
    # Kafka topic name for traces
    GRAFBASE_OTEL_KAFKA_TOPIC_TRACES: otlp_spans
    # Kafka topic name for logs
    GRAFBASE_OTEL_KAFKA_TOPIC_LOGS: otlp_logs
    # Kafka bootstrap server address
    GRAFBASE_KAFKA_BOOTSTRAP_SERVERS: grafbase-enterprise-platform-kafka:9092
    # Kafka security protocol
    GRAFBASE_KAFKA_SECURITY_PROTOCOL: PLAINTEXT
    # Kafka authentication mechanism
    GRAFBASE_KAFKA_MECHANISM: PLAIN
    # Use this environment variable to connect to AWS MSK with IAM authentication. The security protocol and mechanism will be ignored.
    # Mutually exclusive with GRAFBASE_KAFKA_USERNAME and GRAFBASE_KAFKA_PASSWORD.
    GRAFBASE_KAFKA_MSK_REGION: us-east-1
    # Environment name
    ENVIRONMENT: production

    # The following group of environment variables is an alternative to PG_CONNECTION_STRING to define how to connect to Postgres if you use AWS Aurora RDS. If defined, the telemetry sink will use the AWS SDK to periodically generate a connection string, assuming it can find appropriate AWS credentials using the standard mechanisms.
    GRAFBASE_RDS_DATABASE_NAME: grafbase
    GRAFBASE_RDS_HOST: <from your aws dashboard>
    GRAFBASE_RDS_PORT: 5432
    GRAFBASE_RDS_REGION: us-east-1
    GRAFBASE_RDS_SEARCH_PATH: public
    GRAFBASE_RDS_USERNAME: grafbase
```

## secrets

Configuration values for the cluster secret.

```yaml
secrets:
  # Controls secret creation
  enabled: true
  # Secret name. Uses default if not set
  name: ''
  values:
    # Secret key used for API access token verification. Must be the same in the API, the dashboard, and the telemetry sink.
    GRAFBASE_API_ACCESS_TOKENS_SECRET: thisisaverysecurekeythatis32byte
    # PostgreSQL connection string. This will be ignored if RDS credentials are defined.
    PG_CONNECTION_STRING: postgresql://postgres:grafbase@grafbase-enterprise-platform-postgresql:5432/grafbase
    # Kafka username for authentication. Mutually exclusive with GRAFBASE_KAFKA_MSK_REGION.
    GRAFBASE_KAFKA_USERNAME: grafbase
    # Kafka password for authentication. Mutually exclusive with GRAFBASE_KAFKA_MSK_REGION.
    GRAFBASE_KAFKA_PASSWORD: grafbase
    # ClickHouse connection string
    CLICKHOUSE_CONNECTION_STRING: clickhouse://grafbase-enterprise-platform-clickhouse:9000?database=analytics&x-multi-statement=true&username=grafbase&password=grafbase
```

## migrations

Configuration values for the database migrations.

```yaml
migrations:
  clickhouse:
    resources:
      limits:
        cpu: 1000m
        memory: 1000Mi
      requests:
        cpu: 1000m
        memory: 1000Mi
    image:
      pullPolicy: IfNotPresent
      repository: docker.io/grafbase/clickhouse-migrations
      tag: latest
```