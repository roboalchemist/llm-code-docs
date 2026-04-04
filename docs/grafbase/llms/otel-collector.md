# Source: https://grafbase.com/docs/platform/self-hosting/charts/otel-collector.md

# OpenTelemetry Collector Reference

This reference documents the Kubernetes configuration options for the OpenTelemetry Collector, which aggregates telemetry data from Kafka to ClickHouse.

## replicaCount

[Kubernetes ReplicationController Docs](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)

**Defaults**:

```yaml
replicaCount: 1
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

## extraEnvs

Configuration values for the opentelemetry collector.

**Defaults**:

```yaml
extraEnvs:
  - name: KAFKA_BROKER
    value: grafbase-enterprise-platform-kafka:9092
  - name: KAFKA_USER
    value: grafbase
  - name: KAFKA_PASSWORD
    value: grafbase
  # Use this variable if you want to connect to AWS MSK with IAM authentication. In that case, omit KAFKA_USER and KAFKA_PASSWORD and set the KAFKA_SASL_MECHANISM to AWS_MSK_IAM_OAUTHBEARER.
  - name: KAFKA_MSK_REGION
    value: us-east-1
  - name: KAFKA_SASL_MECHANISM
    value: PLAIN
  - name: KAFKA_TLS_INSECURE
    value: "false"
  - name: CLICKHOUSE_ENDPOINT
    value: clickhouse://grafbase-enterprise-platform-clickhouse:9000
  - name: CLICKHOUSE_DB
    value: analytics
  - name: CLICKHOUSE_USER
    value: grafbase
  - name: CLICKHOUSE_PASSWORD
    value: grafbase
```