# Source: https://grafbase.com/docs/platform/self-hosting/charts/kafka.md

# Kafka

This reference documents the Kubernetes configuration options for the Kafka chart, which provides a message bus to store telemetry data for the Grafbase platform.

All configuration options are nested under the `kafka` key.

> **Note**: As of v0.9.0, this is a custom chart using the official Apache Kafka Docker image (apache/kafka:3.9.0) instead of the deprecated Bitnami chart. The chart is configured for KRaft mode and does not require Zookeeper. See the [v0.9.0 release notes](https://grafbase.com/docs/platform/self-hosting/release-notes/0.9.0.md) for migration information.

> **Important**: This chart is primarily intended for proof-of-concept deployments. For production use, we recommend using your own Kafka infrastructure or a managed Kafka service.

## image

Container image configuration for Kafka.

**Defaults**:

```yaml
image:
  repository: apache/kafka
  tag: "3.9.0"
  pullPolicy: IfNotPresent
```

## replicas

Number of Kafka broker replicas. This is a single-node configuration by default.

**Defaults**:

```yaml
replicas: 1
```

## service

Service configuration for exposing Kafka.

**Defaults**:

```yaml
service:
  type: ClusterIP
  port: 9092
  nodePort: ""  # Only used when type is NodePort
```

## persistence

Persistence configuration for Kafka data.

**Defaults**:

```yaml
persistence:
  enabled: true
  size: 8Gi
```

## resources

Resource requests and limits for the Kafka container.

**Defaults**:

```yaml
resources:
  limits:
    cpu: 500m
    memory: 500Mi
  requests:
    cpu: 500m
    memory: 500Mi
```

## extraConfig

Additional Kafka broker configuration. These settings are applied to the Kafka server properties.

**Defaults**:

```yaml
extraConfig:
  replica.fetch.max.bytes: "524288000"
  message.max.bytes: "524288000"
```

## Topic Management

Topics are no longer created automatically by this chart. You'll need to create the required topics (`otlp_metrics`, `otlp_spans`, `otlp_logs`) after deployment using Kafka command-line tools or your Kafka management interface.

**Example topic creation**:

```bash
kubectl exec -it <kafka-pod> -- kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create --topic otlp_metrics

kubectl exec -it <kafka-pod> -- kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create --topic otlp_spans

kubectl exec -it <kafka-pod> -- kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create --topic otlp_logs
```

## Authentication

The simplified chart does not include built-in authentication. For production deployments, configure authentication through your own Kafka infrastructure with appropriate SASL/SSL settings.