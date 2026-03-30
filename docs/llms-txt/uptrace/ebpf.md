# Source: https://uptrace.dev/raw/ingest/ebpf.md

# Ingesting telemetry using OpenTelemetry eBPF (OBI)

> Auto-instrument any application using kernel-level eBPF with OpenTelemetry. Zero-code observability for all languages, sending traces and metrics to Uptrace.

[OpenTelemetry eBPF Instrumentation](https://opentelemetry.io/docs/zero-code/obi/) (OBI) provides automatic observability using kernel-level eBPF technology. Unlike traditional agents, OBI captures distributed traces and metrics for **any application, in any language**, with zero code changes, no restarts, and minimal performance overhead.

OBI instruments at the protocol level, automatically capturing HTTP, gRPC, SQL, Redis, and Kafka traffic without requiring application modifications. It supports Java, .NET, Go, Python, Ruby, Node.js, C, C++, and Rust.

## Requirements

OBI requires:

- **Linux kernel** 5.8 or later (4.18 for RHEL/CentOS)
- **Architecture**: x86_64 or arm64
- **Privileges**: Root access or specific Linux capabilities (`CAP_BPF`, `CAP_SYS_PTRACE`, `CAP_PERFMON`, etc.)

## Docker deployment

Run OBI with Docker, configuring it to send telemetry to Uptrace:

```bash
docker run --rm --privileged \
  --pid=host \
  -v /sys/fs/cgroup:/sys/fs/cgroup \
  -e OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317 \
  -e OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<FIXME>" \
  -e OTEL_SERVICE_NAME=my-service \
  -e OTEL_EBPF_OPEN_PORT=8080 \
  otel/ebpf-instrument:main
```

## Configuration file

Create a `config.yml` for more advanced configuration:

<code-group>

```yaml [Cloud]
# Service discovery
discovery:
  instrument:
    - open_ports: 8080,8443

# OpenTelemetry export to Uptrace Cloud
otel_traces_export:
  endpoint: https://api.uptrace.dev:4317
  headers:
    uptrace-dsn: '<FIXME>'

otel_metrics_export:
  endpoint: https://api.uptrace.dev:4317
  headers:
    uptrace-dsn: '<FIXME>'
  interval: 30s

# Enable distributed tracing context propagation
ebpf:
  context_propagation: all
```

```yaml [Self-hosted]
# Service discovery
discovery:
  instrument:
    - open_ports: 8080,8443

# OpenTelemetry export to self-hosted Uptrace
otel_traces_export:
  endpoint: http://localhost:14317

otel_metrics_export:
  endpoint: http://localhost:14317
  interval: 30s

# Enable distributed tracing context propagation
ebpf:
  context_propagation: all
```

</code-group>

Run OBI with the configuration file:

```bash
OTEL_SERVICE_NAME=my-service \
OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<FIXME>" \
obi -config config.yml
```

## Kubernetes DaemonSet

Deploy OBI as a DaemonSet to automatically instrument all pods in the cluster:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: obi
  namespace: monitoring
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: obi
rules:
  - apiGroups: ['apps']
    resources: ['replicasets']
    verbs: ['list', 'watch']
  - apiGroups: ['']
    resources: ['pods', 'services', 'nodes']
    verbs: ['list', 'watch']
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: obi
subjects:
  - kind: ServiceAccount
    name: obi
    namespace: monitoring
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: obi
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: obi
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: obi
  template:
    metadata:
      labels:
        app: obi
    spec:
      serviceAccountName: obi
      hostPID: true
      hostNetwork: true
      dnsPolicy: ClusterFirstWithHostNet
      containers:
        - name: obi
          image: otel/ebpf-instrument:main
          securityContext:
            privileged: true
            runAsUser: 0
          env:
            - name: OTEL_EBPF_OPEN_PORT
              value: '8080,8443'
            - name: OTEL_EXPORTER_OTLP_ENDPOINT
              value: 'https://api.uptrace.dev:4317'
            - name: OTEL_EXPORTER_OTLP_HEADERS
              value: 'uptrace-dsn=<FIXME>'
            - name: OTEL_EBPF_KUBE_METADATA_ENABLE
              value: 'true'
            - name: OTEL_EBPF_BPF_CONTEXT_PROPAGATION
              value: 'all'
          volumeMounts:
            - name: var-run-obi
              mountPath: /var/run/obi
            - name: cgroup
              mountPath: /sys/fs/cgroup
      volumes:
        - name: var-run-obi
          emptyDir: {}
        - name: cgroup
          hostPath:
            path: /sys/fs/cgroup
```

## Kubernetes sidecar

For instrumenting a specific service, deploy OBI as a sidecar container:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      shareProcessNamespace: true
      serviceAccountName: obi
      containers:
        - name: my-app
          image: my-app:latest
          ports:
            - containerPort: 8080
        - name: obi
          image: otel/ebpf-instrument:main
          securityContext:
            privileged: true
          env:
            - name: OTEL_EBPF_OPEN_PORT
              value: '8080'
            - name: OTEL_EXPORTER_OTLP_ENDPOINT
              value: 'https://api.uptrace.dev:4317'
            - name: OTEL_EXPORTER_OTLP_HEADERS
              value: 'uptrace-dsn=<FIXME>'
            - name: OTEL_EBPF_KUBE_METADATA_ENABLE
              value: 'true'
```

## Discovery methods

OBI supports multiple service discovery methods:

**Port-based discovery:**

```yaml
discovery:
  instrument:
    - open_ports: 8080-8090,9000
```

**Executable path:**

```yaml
discovery:
  instrument:
    - exe_path: '/usr/local/bin/my-app'
    - exe_path: '*/node'
```

**Kubernetes labels:**

```yaml
discovery:
  instrument:
    - k8s_namespace: production
      k8s_pod_labels:
        app: frontend
```

## Troubleshooting

Enable debug logging to diagnose issues:

```bash
OTEL_EBPF_LOG_LEVEL=debug obi -config config.yml
```

Print traces to stdout for testing:

```bash
docker run --rm --privileged --pid=host \
  -e OTEL_EBPF_TRACE_PRINTER=text \
  -e OTEL_EBPF_OPEN_PORT=8080 \
  otel/ebpf-instrument:main
```

## What's next?

- [OpenTelemetry Collector](/ingest/collector) - Use Collector for additional processing and routing
- [OpenTelemetry SDK](/ingest/opentelemetry) - Combine with language-specific SDKs for custom instrumentation
