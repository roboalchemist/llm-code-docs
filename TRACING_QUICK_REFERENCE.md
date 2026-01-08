# Tracing Tools Quick Reference Guide

A fast lookup guide for common tracing scenarios and tool recommendations.

---

## Quick Selection By Use Case

### "I'm starting a new project - what should I use?"

**Recommendation: OpenTelemetry + Pick a Backend**

1. **Instrumentation**: Use OpenTelemetry SDKs/auto-instrumentation (free, vendor-neutral)
2. **Backend**: Choose one:
   - **Managed**: Uptrace ($30/mo), New Relic free tier, or Datadog
   - **Self-hosted**: Jaeger + Elasticsearch, Grafana Tempo, or Grafana Cloud
3. **Collection**: Use OpenTelemetry Collector to route data

**Time to setup**: 1-2 hours

---

### "I want everything in one platform"

**Recommendation: Datadog or New Relic**

| Platform | Pros | Cons |
|----------|------|------|
| **Datadog** | Industry standard; vast integrations; excellent UI | Expensive at scale; complex pricing |
| **New Relic** | Simple UI; usage-based pricing; free tier generous | Less integrations than Datadog; limits on infinite tracing |

**Setup time**: 2-4 hours

---

### "I want to minimize costs"

**Recommendation: Open-Source Stack**

```
Tracing: Grafana Tempo (or Jaeger)
Logging: Grafana Loki
Metrics: Prometheus
Visualization: Grafana
Collection: OpenTelemetry Collector
Profiling: Grafana Pyroscope (optional)
```

**Cost**: Infrastructure only (Kubernetes or VM)
**Setup time**: 4-8 hours
**Trade-off**: Operations overhead (you manage it)

---

### "I need to debug complex microservices issues"

**Recommendation: Honeycomb or LightStep**

These tools excel at:
- High-cardinality data analysis (thousands of unique values)
- Query history replay
- Collaborative debugging
- Unusual pattern detection

**Cost**: $200-2000+/mo depending on volume
**Setup time**: 2-3 hours

---

### "I'm using AWS/GCP/Azure"

**Cloud Provider Native:**
- **AWS**: X-Ray (free tier; transitioning to OpenTelemetry)
- **GCP**: Cloud Trace (integrates with Cloud Logging/Monitoring)
- **Azure**: Application Insights (part of Azure Monitor)

**Pros**: Native integrations, no setup
**Cons**: Vendor lock-in, limited querying, higher costs

**Better alternative**: Use cloud provider for logs/metrics, dedicated tracing backend (Tempo, Jaeger, or Honeycomb) for better observability

---

### "I need continuous profiling for performance"

**Recommendation: Grafana Pyroscope or Parca**

| Tool | Best For | Cost |
|------|----------|------|
| **Grafana Pyroscope** | Grafana-native stack; multi-language | Free (self-hosted) |
| **Parca** | Kubernetes eBPF profiling; cloud-native | Free (self-hosted) |
| **Dynatrace Profiler** | Enterprise JVM; AI-driven insights | Commercial (part of suite) |
| **Datadog Profiler** | Enterprise; integrated with APM | Commercial (add-on) |

**Setup time**: 1-2 hours

---

### "I need real-time application monitoring + tracing"

**Recommendation: New Relic or Datadog**

Both provide:
- Distributed tracing
- Real-time metrics
- Log aggregation
- Synthetic monitoring
- Custom dashboards
- Alerting

**Choose based on:**
- **New Relic**: Simpler UI, good for small/mid teams
- **Datadog**: More powerful, better for enterprises

---

## Tool Comparison Quick Tables

### By Price Point

| Budget | Recommended Tool | Cost/Month |
|--------|-----------------|-----------|
| **Free** | Uptrace free + Grafana Cloud | $0 |
| **Small** | New Relic free tier | $0-500 |
| **Small/Mid** | Uptrace managed + Grafana Cloud | $30-200 |
| **Mid** | Datadog or New Relic paid | $500-2000 |
| **Enterprise** | Dynatrace or AppDynamics | $2000+ |

### By Language Focus

| Language | Primary Library | Maturity | Auto-Instrumentation |
|----------|-----------------|----------|----------------------|
| **Java** | OpenTelemetry Java Agent | ✓ Stable | ✓ Yes |
| **Python** | OpenTelemetry Python SDK | ✓ Stable | ✓ Yes |
| **Go** | OpenTelemetry Go SDK | ✓ Stable | ✗ No |
| **Node.js** | OpenTelemetry JS SDK | ✓ Stable | ✓ Yes |
| **.NET** | OpenTelemetry .NET SDK | ✓ Stable | ✓ Yes |
| **Ruby** | OpenTelemetry Ruby SDK | ✓ Stable | ✗ Partial |

### By Deployment Model

| Model | Recommended | Cost | Complexity |
|-------|-------------|------|-----------|
| **Fully Managed SaaS** | Datadog, Honeycomb, New Relic | $$$ | Low |
| **Cloud-Hosted Open-Source** | Grafana Cloud, Uptrace | $$ | Low |
| **Self-Hosted Open-Source** | Tempo + Prometheus + Loki | $ | High |
| **Hybrid (Cloud Logs + OSS Tracing)** | Cloud provider logs + Jaeger | $$ | Medium |

---

## Implementation Quickstart

### Step 1: Choose OpenTelemetry (5 min)

```bash
# Add to your application
pip install opentelemetry-api opentelemetry-sdk  # Python
npm install @opentelemetry/api @opentelemetry/sdk-node  # Node.js
# or use auto-instrumentation agent
```

### Step 2: Select Backend (5 min)

Pick one:
- **Managed**: Uptrace, Honeycomb, New Relic, Datadog
- **Self-hosted**: Jaeger, Grafana Tempo, or Elasticsearch
- **Cloud native**: AWS X-Ray, GCP Cloud Trace, Azure Insights

### Step 3: Configure Collection (15 min)

```yaml
# OpenTelemetry Collector config
receivers:
  otlp:
    protocols:
      grpc:
      http:

processors:
  batch:
  memory_limiter:

exporters:
  jaeger:  # Replace with your backend
    endpoint: "http://jaeger:14250"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [jaeger]
```

### Step 4: Deploy & Test (30 min)

```bash
# Test trace generation
curl -X POST http://localhost:4317/v1/traces -H "Content-Type: application/json"

# View in backend UI
# Jaeger: http://localhost:16686
# Tempo: Grafana dashboard
```

**Total setup time: 1 hour**

---

## Common Integration Patterns

### Java Microservices (Spring Boot)

```bash
# 1. Add OTel Starter
dependency: org.springframework.boot:spring-boot-starter-webflux

# 2. Add OTel Agent to Dockerfile
RUN curl https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar

# 3. Run with agent
CMD java -javaagent:opentelemetry-javaagent.jar -jar app.jar
```

### Python FastAPI

```python
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

app = FastAPI()

# Auto-instrumentation with one line
FastAPIInstrumentor.instrument_app(app)
```

### Node.js Express

```javascript
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');

const sdk = new NodeSDK({
  instrumentations: [getNodeAutoInstrumentations()]
});

sdk.start();
const express = require('express');
// app code follows
```

### Kubernetes Deployment

```yaml
# Deploy OTel Collector as sidecar or DaemonSet
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: otel-collector
spec:
  template:
    spec:
      containers:
      - name: otel-collector
        image: otel/opentelemetry-collector:latest
        volumeMounts:
        - name: collector-config
          mountPath: /etc/collector
      volumes:
      - name: collector-config
        configMap:
          name: otel-config
```

---

## Troubleshooting Common Issues

### "I'm not seeing traces"

1. Check instrumentation is enabled (auto-agent or SDK)
2. Verify OpenTelemetry Collector is running
3. Check exporter configuration (correct backend endpoint)
4. Look for errors in application logs: `grep -i "telemetry\|trace"`
5. Run collector in debug mode: `--set service.telemetry.logs.level=debug`

### "Traces are sampled too aggressively"

Change sampling strategy in OTel SDK:

```python
# Python: sample all traces (100%)
from opentelemetry.sdk.trace.sampling import AlwaysOnSampler
tracer_provider = TracerProvider(sampler=AlwaysOnSampler())

# Or use tail-based sampling in Collector
processors:
  tail_sampling:
    policies:
    - name: error-traces
      rules:
        traces:
          type: status_code
          status_code:
            status_codes: [ERROR]
```

### "Costs are too high"

1. Implement head-based sampling: sample 10-20% of traces
2. Use tail-based sampling: sample only important traces
3. Filter noise: ignore health checks, metrics endpoints
4. Archive old traces: move to cheaper storage (S3, GCS)
5. Consider self-hosted: eliminate per-span costs

### "Collector is crashing / using too much memory"

1. Add memory limiter processor:

```yaml
processors:
  memory_limiter:
    check_interval: 5s
    limit_mib: 512  # Adjust for your container
```

2. Increase batch size:

```yaml
processors:
  batch:
    timeout: 10s
    send_batch_size: 512
    send_batch_max_size: 2048
```

---

## Terminology Quick Ref

| Term | Definition |
|------|-----------|
| **Span** | Single operation in a trace (e.g., HTTP request, DB query) |
| **Trace** | Full request path through system (collection of spans) |
| **Trace ID** | Unique identifier for entire request journey |
| **Span ID** | Unique identifier for single operation |
| **Attributes** | Key-value metadata on spans (e.g., user_id=123) |
| **Events** | Timestamped messages within spans |
| **Sampling** | Technique to reduce trace volume (1%, 10%, 100%, or intelligent) |
| **Head-based sampling** | Sample decision at trace start |
| **Tail-based sampling** | Sample decision after full trace collected |
| **Service map** | Visualization of services and their dependencies |
| **OTLP** | OpenTelemetry Protocol (HTTP/gRPC standard) |
| **Cardinality** | Number of unique values in attribute (high=millions) |
| **APM** | Application Performance Monitoring (broader than just tracing) |

---

## Migration Guide: From X to Y

### From Jaeger to Grafana Tempo

1. Keep existing Jaeger backend running
2. Point new apps to Tempo
3. Use TraceQL for new queries (replaces Jaeger query API)
4. Migrate old traces via backup/restore

### From OpenTracing to OpenTelemetry

1. Install OTel SDK alongside old OpenTracing lib
2. Use bridge library: `opentelemetry-instrumentation-* `
3. Gradually replace OpenTracing calls with OTel
4. Remove OpenTracing once all migrated

### From Datadog to Open-Source Stack

1. Export Datadog traces (via API)
2. Deploy Jaeger/Tempo
3. Switch SDK exporters from Datadog to Jaeger
4. Migrate dashboards to Grafana
5. Cancel Datadog (may export historical data)

---

## Recommended Reading

- [OpenTelemetry Docs](https://opentelemetry.io/docs/)
- [BetterStack Distributed Tracing Guide](https://betterstack.com/community/comparisons/distributed-tracing-tools/)
- [Grafana Tempo Best Practices](https://grafana.com/docs/tempo/)
- [Honeycomb Observability Guide](https://www.honeycomb.io/resources/guides/)

---

**Last Updated**: January 2026
