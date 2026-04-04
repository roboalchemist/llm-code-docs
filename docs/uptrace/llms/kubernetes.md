# Source: https://uptrace.dev/raw/get/kubernetes.md

# Monitor K8s with OpenTelemetry Collector

> Complete Kubernetes application monitoring and cluster observability using OpenTelemetry Collector receivers. Step-by-step setup guide for Kubernetes tracing.

This guide shows you how to set up comprehensive Kubernetes monitoring using OpenTelemetry Collector for cluster observability and application performance monitoring.

Kubernetes tracing and OpenTelemetry Kubernetes example configurations provide deep insights into your containerized applications, pod performance, and cluster health through practical Kubernetes monitor setup.

## Why Monitor Kubernetes with OpenTelemetry

OpenTelemetry provides unified observability across your entire Kubernetes stack - from infrastructure metrics to application traces - through a single, vendor-neutral standard. Unlike proprietary monitoring solutions or tool sprawl (Prometheus for metrics, Jaeger for traces, ELK for logs), OpenTelemetry gives you:

**Complete Observability in One Platform:**

- Collect metrics, traces, and logs using the same instrumentation
- Correlate pod restarts with application errors and user requests
- Track requests across microservices with distributed tracing
- Export to any backend (Uptrace, Grafana, Datadog) without vendor lock-in

**Kubernetes-Native Integration:**

- Automatic enrichment with K8s metadata (pod names, namespaces, labels)
- Built-in receivers for cluster metrics (k8s_cluster) and pod metrics (kubeletstats)
- Service account-based authentication following K8s security best practices
- Deploy as DaemonSet or Deployment using standard Kubernetes patterns

**Production-Ready Scalability:**

- Minimal resource overhead (100-200MB RAM per collector)
- Efficient batching and sampling for high-volume clusters
- Support for multi-cluster deployments with centralized observability
- Auto-discovery of pods and services without manual configuration

Whether you're troubleshooting performance issues, monitoring microservices health, or ensuring SLA compliance, OpenTelemetry provides the visibility you need without locking you into a single vendor's ecosystem.

## Prerequisites

Before setting up OpenTelemetry Kubernetes monitoring, ensure you have:

- Running Kubernetes cluster (v1.24+)
- kubectl access with cluster admin permissions
- Helm 3.14+ installed

Verify your cluster is ready:

```bash
kubectl cluster-info
kubectl get nodes
```

For production deployments, you have several options to run Uptrace, including self-hosting on Kubernetes. Learn about the available [Uptrace editions](/get/hosted) to find the best fit for your needs.

## What is OpenTelemetry Collector?

[OpenTelemetry Collector](/opentelemetry/collector) is an agent that pulls telemetry data from systems you want to monitor and export the collected data to an [OpenTelemetry backend](/blog/opentelemetry-backend).

OTel Collector provides powerful data processing capabilities, allowing you to perform aggregation, filtering, sampling, and enrichment of telemetry data. You can transform and reshape the data to fit your specific monitoring and analysis requirements before sending it to the backend systems.

## Installing with Helm

The recommended way to deploy OpenTelemetry Collector in Kubernetes is using the official Helm chart. First, add the OpenTelemetry Helm repository:

```bash
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
helm repo update
```

Install the collector as a DaemonSet for node-level metrics collection:

```bash
helm install otel-collector open-telemetry/opentelemetry-collector \
  --set image.repository=otel/opentelemetry-collector-k8s \
  --set mode=daemonset
```

For cluster-level metrics, install as a Deployment:

```bash
helm install otel-collector-cluster open-telemetry/opentelemetry-collector \
  --set image.repository=otel/opentelemetry-collector-k8s \
  --set mode=deployment \
  --set presets.clusterMetrics.enabled=true \
  --set presets.kubernetesEvents.enabled=true
```

You can customize the installation by creating a `values.yaml` file with your configuration and installing with:

```bash
helm install otel-collector open-telemetry/opentelemetry-collector -f values.yaml
```

### Production Helm Values Example

Here's a comprehensive `values.yaml` for production deployments:

```yaml
mode: daemonset

image:
  repository: otel/opentelemetry-collector-k8s
  tag: "0.115.0"

presets:
  kubernetesAttributes:
    enabled: true
    extractAllPodLabels: true
    extractAllPodAnnotations: false
  kubeletMetrics:
    enabled: true

resources:
  requests:
    cpu: 100m
    memory: 256Mi
  limits:
    cpu: 500m
    memory: 512Mi

config:
  receivers:
    otlp:
      protocols:
        grpc:
          endpoint: 0.0.0.0:4317
        http:
          endpoint: 0.0.0.0:4318
    kubeletstats:
      auth_type: serviceAccount
      collection_interval: 20s
      metric_groups:
        - node
        - pod
        - container

  processors:
    batch:
      timeout: 10s
      send_batch_size: 1024
    memory_limiter:
      check_interval: 1s
      limit_mib: 400
      spike_limit_mib: 100
    resourcedetection:
      detectors: [env, system, k8snode]
      timeout: 5s

  exporters:
    otlp:
      endpoint: api.uptrace.dev:4317
      headers:
        uptrace-dsn: "<YOUR_DSN>"

  service:
    pipelines:
      traces:
        receivers: [otlp]
        processors: [memory_limiter, batch]
        exporters: [otlp]
      metrics:
        receivers: [otlp, kubeletstats]
        processors: [memory_limiter, batch, resourcedetection]
        exporters: [otlp]
      logs:
        receivers: [otlp]
        processors: [memory_limiter, batch]
        exporters: [otlp]

ports:
  otlp:
    enabled: true
    containerPort: 4317
    servicePort: 4317
    protocol: TCP
  otlp-http:
    enabled: true
    containerPort: 4318
    servicePort: 4318
    protocol: TCP

serviceAccount:
  create: true
  name: opentelemetry-collector

clusterRole:
  create: true
  rules:
    - apiGroups: [""]
      resources: ["nodes", "nodes/stats", "pods", "services", "endpoints"]
      verbs: ["get", "list", "watch"]
```

See [Uptrace Helm charts](https://github.com/uptrace/helm-charts) for additional production-ready examples.

## Authentication & RBAC

OpenTelemetry Kubernetes monitoring requires proper authentication to access the Kubernetes API. The collector uses service accounts with specific RBAC permissions to query cluster resources.

### Namespace and Service Account

First, create a dedicated namespace and service account:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: opentelemetry
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: opentelemetry-collector
  namespace: opentelemetry
```

### ClusterRole for Cluster Metrics

The k8s_cluster receiver requires broad read access to cluster resources:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: opentelemetry-collector
rules:
  - apiGroups: [""]
    resources:
      - events
      - namespaces
      - namespaces/status
      - nodes
      - nodes/spec
      - nodes/stats
      - nodes/proxy
      - pods
      - pods/status
      - replicationcontrollers
      - replicationcontrollers/status
      - resourcequotas
      - services
    verbs: ["get", "list", "watch"]
  - apiGroups: ["apps"]
    resources:
      - daemonsets
      - deployments
      - replicasets
      - statefulsets
    verbs: ["get", "list", "watch"]
  - apiGroups: ["batch"]
    resources:
      - cronjobs
      - jobs
    verbs: ["get", "list", "watch"]
  - apiGroups: ["autoscaling"]
    resources:
      - horizontalpodautoscalers
    verbs: ["get", "list", "watch"]
```

### ClusterRoleBinding

Bind the ClusterRole to your service account:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: opentelemetry-collector
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: opentelemetry-collector
subjects:
  - kind: ServiceAccount
    name: opentelemetry-collector
    namespace: opentelemetry
```

Apply these manifests:

```bash
kubectl apply -f rbac.yaml
```

## Monitor K8s Cluster Metrics

The Kubernetes Cluster [receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/k8sclusterreceiver) collects cluster-wide metrics using the Kubernetes API server. Since it monitors the entire cluster, only one instance is needed.

<table>
<thead>
  <tr>
    <th>
      Deployment Pattern
    </th>
    
    <th>
      Usable
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      DaemonSet (agent)
    </td>
    
    <td>
      Results in duplicate data
    </td>
  </tr>
  
  <tr>
    <td>
      Deployment (gateway)
    </td>
    
    <td>
      Yes (single replica recommended)
    </td>
  </tr>
  
  <tr>
    <td>
      Sidecar
    </td>
    
    <td>
      No
    </td>
  </tr>
</tbody>
</table>

Configure the receiver in `/etc/otel-contrib-collector/config.yaml` using your [Uptrace DSN](/get#dsn):

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
  k8s_cluster:
    auth_type: serviceAccount
    collection_interval: 10s
    node_conditions_to_report: [Ready, MemoryPressure]
    allocatable_types_to_report: [cpu, memory]

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: "<YOUR_DSN>"

processors:
  resourcedetection:
    detectors: [env, system, k8snode]
  cumulativetodelta:
  batch:
    timeout: 10s

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
    metrics:
      receivers: [otlp, k8s_cluster]
      processors: [cumulativetodelta, batch, resourcedetection]
      exporters: [otlp]
```

### Cluster Metrics

The k8s_cluster receiver collects comprehensive cluster-level metrics:

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      k8s.container.cpu_limit
    </td>
    
    <td>
      CPU limit set for the container
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.container.cpu_request
    </td>
    
    <td>
      CPU request set for the container
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.container.memory_limit
    </td>
    
    <td>
      Memory limit set for the container
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.container.memory_request
    </td>
    
    <td>
      Memory request set for the container
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.container.ready
    </td>
    
    <td>
      Whether the container is ready (1) or not (0)
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.container.restarts
    </td>
    
    <td>
      Number of container restarts
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.deployment.available
    </td>
    
    <td>
      Number of available replicas
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.deployment.desired
    </td>
    
    <td>
      Number of desired replicas
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.namespace.phase
    </td>
    
    <td>
      Phase of the namespace (1=Active, 0=Terminating)
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.condition
    </td>
    
    <td>
      Status of node conditions (Ready, MemoryPressure, etc.)
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.pod.phase
    </td>
    
    <td>
      Current phase of the pod
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.replicaset.available
    </td>
    
    <td>
      Number of available replicas
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.replicaset.desired
    </td>
    
    <td>
      Number of desired replicas
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.statefulset.current_pods
    </td>
    
    <td>
      Number of current pods
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.statefulset.desired_pods
    </td>
    
    <td>
      Number of desired pods
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.statefulset.ready_pods
    </td>
    
    <td>
      Number of ready pods
    </td>
  </tr>
</tbody>
</table>

See [Helm example](https://github.com/uptrace/helm-charts) and [official documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/k8sclusterreceiver) for more details.

## Kubernetes Application Monitoring

The Kubelet Stats [receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kubeletstatsreceiver) pulls node, pod, and container metrics from the kubelet API on each node.

<table>
<thead>
  <tr>
    <th>
      Deployment Pattern
    </th>
    
    <th>
      Usable
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      DaemonSet (agent)
    </td>
    
    <td>
      Preferred
    </td>
  </tr>
  
  <tr>
    <td>
      Deployment (gateway)
    </td>
    
    <td>
      Only collects metrics from its own node
    </td>
  </tr>
  
  <tr>
    <td>
      Sidecar
    </td>
    
    <td>
      No
    </td>
  </tr>
</tbody>
</table>

Configure the receiver to collect pod and container metrics:

```yaml
env:
  - name: K8S_NODE_NAME
    valueFrom:
      fieldRef:
        fieldPath: spec.nodeName
```

Configure the receiver to collect kubelet metrics:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
  kubeletstats:
    auth_type: serviceAccount
    endpoint: 'https://${env:K8S_NODE_NAME}:10250'
    insecure_skip_verify: true
    collection_interval: 20s
    metric_groups: [pod, container, node]

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: "<YOUR_DSN>"

processors:
  resourcedetection:
    detectors: [env, system, k8snode]
  cumulativetodelta:
  batch:
    timeout: 10s

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
    metrics:
      receivers: [otlp, kubeletstats]
      processors: [cumulativetodelta, batch, resourcedetection]
      exporters: [otlp]
```

### Container Metrics

The kubeletstats receiver collects detailed container-level metrics:

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      container.cpu.time
    </td>
    
    <td>
      Total CPU time consumed by the container
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.utilization
    </td>
    
    <td>
      CPU utilization percentage
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.available
    </td>
    
    <td>
      Available memory for the container
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.usage
    </td>
    
    <td>
      Current memory usage
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.rss
    </td>
    
    <td>
      Resident set size (non-swappable memory)
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.working_set
    </td>
    
    <td>
      Working set memory
    </td>
  </tr>
  
  <tr>
    <td>
      container.filesystem.available
    </td>
    
    <td>
      Available filesystem space
    </td>
  </tr>
  
  <tr>
    <td>
      container.filesystem.capacity
    </td>
    
    <td>
      Total filesystem capacity
    </td>
  </tr>
  
  <tr>
    <td>
      container.filesystem.usage
    </td>
    
    <td>
      Current filesystem usage
    </td>
  </tr>
</tbody>
</table>

### Pod Metrics

Pod-level metrics provide aggregate information:

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      k8s.pod.cpu.time
    </td>
    
    <td>
      Total CPU time consumed by all containers in the pod
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.pod.cpu.utilization
    </td>
    
    <td>
      CPU utilization percentage for the pod
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.pod.memory.available
    </td>
    
    <td>
      Available memory for the pod
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.pod.memory.usage
    </td>
    
    <td>
      Current memory usage by the pod
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.pod.memory.rss
    </td>
    
    <td>
      Resident set size for the pod
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.pod.memory.working_set
    </td>
    
    <td>
      Working set memory for the pod
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.pod.network.io
    </td>
    
    <td>
      Network bytes received and transmitted
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.pod.network.errors
    </td>
    
    <td>
      Network error counts
    </td>
  </tr>
</tbody>
</table>

### Node Metrics

Node-level metrics track system resources:

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      k8s.node.cpu.time
    </td>
    
    <td>
      Total CPU time consumed
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.cpu.utilization
    </td>
    
    <td>
      CPU utilization percentage
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.memory.available
    </td>
    
    <td>
      Available memory on the node
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.memory.usage
    </td>
    
    <td>
      Current memory usage
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.memory.rss
    </td>
    
    <td>
      Resident set size
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.memory.working_set
    </td>
    
    <td>
      Working set memory
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.filesystem.available
    </td>
    
    <td>
      Available filesystem space
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.filesystem.capacity
    </td>
    
    <td>
      Total filesystem capacity
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.filesystem.usage
    </td>
    
    <td>
      Current filesystem usage
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.network.io
    </td>
    
    <td>
      Network bytes received and transmitted
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.node.network.errors
    </td>
    
    <td>
      Network error counts
    </td>
  </tr>
</tbody>
</table>

See [kubeletstats receiver documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kubeletstatsreceiver) for the complete list of available metrics.

### CPU Metrics Deprecation Notice

**Important:** Starting with OpenTelemetry Collector v0.125.0, the kubeletstats receiver has transitioned CPU metrics from `.cpu.utilization` to `.cpu.usage`:

<table>
<thead>
  <tr>
    <th>
      Deprecated Metric
    </th>
    
    <th>
      New Metric
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      k8s.node.cpu.utilization
    </td>
    
    <td>
      k8s.node.cpu.usage
    </td>
  </tr>
  
  <tr>
    <td>
      k8s.pod.cpu.utilization
    </td>
    
    <td>
      k8s.pod.cpu.usage
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.utilization
    </td>
    
    <td>
      container.cpu.usage
    </td>
  </tr>
</tbody>
</table>

The `.cpu.utilization` name was misleading because the metrics represent raw CPU usage (in cores), not utilization (a percentage). If you're upgrading from an earlier version, update your dashboards and alerts to use the new metric names.

To temporarily restore deprecated metrics during migration, disable the feature gate:

```bash
--feature-gates=-receiver.kubeletstats.enableCPUUsageMetrics
```

### Kubernetes Attributes Processor

The Kubernetes Attributes Processor (`k8sattributes`) automatically discovers pods and adds Kubernetes metadata to your telemetry. **This is one of the most important components** for correlating application traces, metrics, and logs with Kubernetes resources.

<table>
<thead>
  <tr>
    <th>
      Deployment Pattern
    </th>
    
    <th>
      Usable
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      DaemonSet (agent)
    </td>
    
    <td>
      Yes
    </td>
  </tr>
  
  <tr>
    <td>
      Deployment (gateway)
    </td>
    
    <td>
      Yes
    </td>
  </tr>
  
  <tr>
    <td>
      Sidecar
    </td>
    
    <td>
      No
    </td>
  </tr>
</tbody>
</table>

Configure the processor to extract metadata and associate telemetry with pods:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  k8sattributes:
    auth_type: serviceAccount
    extract:
      metadata:
        - k8s.namespace.name
        - k8s.pod.name
        - k8s.pod.uid
        - k8s.pod.start_time
        - k8s.deployment.name
        - k8s.node.name
      labels:
        - tag_name: app
          key: app.kubernetes.io/name
          from: pod
      annotations:
        - tag_name: version
          key: app.kubernetes.io/version
          from: pod
    pod_association:
      - sources:
          - from: resource_attribute
            name: k8s.pod.ip
      - sources:
          - from: resource_attribute
            name: k8s.pod.uid
      - sources:
          - from: connection
```

The processor adds these attributes by default: `k8s.namespace.name`, `k8s.pod.name`, `k8s.pod.uid`, `k8s.pod.start_time`, `k8s.deployment.name`, and `k8s.node.name`.

The `pod_association` configuration determines how incoming telemetry is matched to podsâfirst by IP address, then by UID, and finally by connection IP.

## Zero-Code Instrumentation with eBPF

For applications without OpenTelemetry instrumentation, use [OpenTelemetry eBPF Instrumentation](/ingest/ebpf) (OBI) to automatically capture distributed traces and metrics at the kernel level. OBI leverages Extended Berkeley Packet Filter (eBPF) technology to instrument applications in **any language** without code changes, restarts, or performance degradation. eBPF attaches to the Linux kernel and intercepts network system calls (HTTP, gRPC, SQL), capturing request/response metadata, timing, and distributed trace context. All telemetry is enriched with Kubernetes metadata and exported to the OpenTelemetry Collector.

**Note:** Several languages offer zero-code auto-instrumentation via language-specific mechanisms: [Java](/get/opentelemetry-java/zero-code), [.NET](/get/opentelemetry-dotnet/zero-code), [Python](/get/opentelemetry-python/zero-code), [Node.js](/get/opentelemetry-js/zero-code), and [PHP](/get/opentelemetry-php/zero-code). These provide deeper framework integration and custom business metrics but require runtime-specific setup. Use eBPF for quick visibility across polyglot architectures, legacy services, or third-party applications where code changes are impractical. For production services with custom business logic, consider language-specific instrumentation for richer telemetry.

**Supported protocols:** HTTP/1.1, HTTP/2, HTTPS, gRPC, gRPC-Web, SQL (Postgres, MySQL - experimental), Redis, MongoDB, Kafka.

### DaemonSet Deployment

Deploy OBI as a DaemonSet to automatically instrument **all pods** across the cluster:

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
              value: '8080,8443,9000'
            - name: OTEL_EXPORTER_OTLP_ENDPOINT
              value: 'http://otel-collector.opentelemetry:4318'
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

**Key configuration:**

- `hostPID: true` - Required to access processes on the host node
- `privileged: true` - Necessary for loading eBPF programs into the kernel
- `OTEL_EBPF_OPEN_PORT` - Comma-separated list of ports to instrument (8080, 8443, etc.)
- `OTEL_EXPORTER_OTLP_ENDPOINT` - Points to OpenTelemetry Collector service
- `OTEL_EBPF_KUBE_METADATA_ENABLE` - Enriches spans with pod/namespace metadata

### Sidecar Pattern

For instrumenting specific services without cluster-wide deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-service
spec:
  template:
    spec:
      shareProcessNamespace: true
      serviceAccountName: obi
      containers:
        - name: payment-service
          image: payment-service:latest
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
              value: 'http://otel-collector.opentelemetry:4318'
            - name: OTEL_SERVICE_NAME
              value: 'payment-service'
            - name: OTEL_EBPF_KUBE_METADATA_ENABLE
              value: 'true'
```

Use sidecar for testing eBPF on specific services before cluster-wide rollout, services with unique port configurations, or applications requiring isolated instrumentation.

**Limitations:** eBPF captures protocol-level transactions (HTTP, gRPC, SQL) but not custom business logic. Requires Linux kernel 5.8+ and privileged container permissions. Performance overhead is typically <1%, significantly lower than SDK-based instrumentation.

## Collecting Kubernetes Logs

The Filelog receiver collects container logs from `/var/log/pods`. Deploy it as a DaemonSet to collect logs from all nodes:

<table>
<thead>
  <tr>
    <th>
      Deployment Pattern
    </th>
    
    <th>
      Usable
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      DaemonSet (agent)
    </td>
    
    <td>
      Preferred
    </td>
  </tr>
  
  <tr>
    <td>
      Deployment (gateway)
    </td>
    
    <td>
      Only collects logs from its own node
    </td>
  </tr>
  
  <tr>
    <td>
      Sidecar
    </td>
    
    <td>
      Advanced configuration
    </td>
  </tr>
</tbody>
</table>

```yaml
receivers:
  filelog:
    include:
      - /var/log/pods/*/*/*.log
    exclude:
      - /var/log/pods/*/otel-collector/*.log
    start_at: end
    include_file_path: true
    operators:
      - type: container
        id: container-parser

processors:
  k8sattributes:
    auth_type: serviceAccount
    extract:
      metadata:
        - k8s.pod.name
        - k8s.namespace.name
  batch:
    timeout: 10s

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: "<YOUR_DSN>"

service:
  pipelines:
    logs:
      receivers: [filelog]
      processors: [k8sattributes, batch]
      exporters: [otlp]
```

The Filelog receiver requires volume mounts to access log files:

```yaml
volumeMounts:
  - name: varlogpods
    mountPath: /var/log/pods
    readOnly: true
volumes:
  - name: varlogpods
    hostPath:
      path: /var/log/pods
```

## Collecting Kubernetes Events

The Kubernetes Objects receiver watches for cluster events and converts them to logs. Deploy as a single-replica Deployment to avoid duplicate events:

<table>
<thead>
  <tr>
    <th>
      Deployment Pattern
    </th>
    
    <th>
      Usable
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      DaemonSet (agent)
    </td>
    
    <td>
      Results in duplicate data
    </td>
  </tr>
  
  <tr>
    <td>
      Deployment (gateway)
    </td>
    
    <td>
      Yes (single replica only)
    </td>
  </tr>
  
  <tr>
    <td>
      Sidecar
    </td>
    
    <td>
      No
    </td>
  </tr>
</tbody>
</table>

```yaml
receivers:
  k8sobjects:
    objects:
      - name: events
        mode: watch
        namespaces: [default, production]

processors:
  batch:
    timeout: 10s

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: "<YOUR_DSN>"

service:
  pipelines:
    logs:
      receivers: [k8sobjects]
      processors: [batch]
      exporters: [otlp]
```

Events provide valuable insights into cluster activities like pod scheduling, scaling operations, and error conditions.

## Kubernetes Example

This OpenTelemetry Kubernetes example demonstrates how to deploy the collector as both DaemonSet and Deployment for complete coverage:

<code-group>

```yaml [DaemonSet]
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: otel-collector-daemonset
  namespace: opentelemetry
  labels:
    app: opentelemetry-collector
spec:
  selector:
    matchLabels:
      app: opentelemetry-collector
  template:
    metadata:
      labels:
        app: opentelemetry-collector
    spec:
      serviceAccountName: opentelemetry-collector
      containers:
        - name: otel-collector
          image: otel/opentelemetry-collector-k8s:0.115.0
          args:
            - --config=/etc/otelcol/config.yaml
          env:
            - name: K8S_NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: K8S_POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: K8S_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
          ports:
            - containerPort: 4317
              protocol: TCP
              name: otlp-grpc
            - containerPort: 4318
              protocol: TCP
              name: otlp-http
          resources:
            requests:
              cpu: 100m
              memory: 256Mi
            limits:
              cpu: 500m
              memory: 512Mi
          volumeMounts:
            - name: config
              mountPath: /etc/otelcol
      volumes:
        - name: config
          configMap:
            name: otel-collector-config
```

```yaml [Deployment]
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector-cluster
  namespace: opentelemetry
  labels:
    app: opentelemetry-cluster-collector
spec:
  replicas: 1
  selector:
    matchLabels:
      app: opentelemetry-cluster-collector
  template:
    metadata:
      labels:
        app: opentelemetry-cluster-collector
    spec:
      serviceAccountName: opentelemetry-collector
      containers:
        - name: otel-collector
          image: otel/opentelemetry-collector-k8s:0.115.0
          args:
            - --config=/etc/otelcol/config.yaml
          ports:
            - containerPort: 4317
              protocol: TCP
              name: otlp-grpc
            - containerPort: 4318
              protocol: TCP
              name: otlp-http
          resources:
            requests:
              cpu: 100m
              memory: 256Mi
            limits:
              cpu: 500m
              memory: 512Mi
          volumeMounts:
            - name: config
              mountPath: /etc/otelcol
      volumes:
        - name: config
          configMap:
            name: otel-cluster-collector-config
```

```yaml [DaemonSet ConfigMap]
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  namespace: opentelemetry
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
      kubeletstats:
        auth_type: serviceAccount
        endpoint: "https://${env:K8S_NODE_NAME}:10250"
        insecure_skip_verify: true
        collection_interval: 20s

    processors:
      batch:
        timeout: 10s
      k8sattributes:
        auth_type: serviceAccount
        extract:
          metadata:
            - k8s.pod.name
            - k8s.namespace.name
            - k8s.deployment.name

    exporters:
      otlp:
        endpoint: api.uptrace.dev:4317
        headers:
          uptrace-dsn: "<YOUR_DSN>"

    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: [k8sattributes, batch]
          exporters: [otlp]
        metrics:
          receivers: [otlp, kubeletstats]
          processors: [batch]
          exporters: [otlp]
```

```yaml [Cluster ConfigMap]
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-cluster-collector-config
  namespace: opentelemetry
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
      k8s_cluster:
        auth_type: serviceAccount
        collection_interval: 10s
        node_conditions_to_report: [Ready, MemoryPressure]
      k8sobjects:
        objects:
          - name: events
            mode: watch

    processors:
      batch:
        timeout: 10s

    exporters:
      otlp:
        endpoint: api.uptrace.dev:4317
        headers:
          uptrace-dsn: "<YOUR_DSN>"

    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: [batch]
          exporters: [otlp]
        metrics:
          receivers: [k8s_cluster]
          processors: [batch]
          exporters: [otlp]
        logs:
          receivers: [k8sobjects]
          processors: [batch]
          exporters: [otlp]
```

```yaml [Service]
apiVersion: v1
kind: Service
metadata:
  name: otel-collector
  namespace: opentelemetry
spec:
  type: ClusterIP
  selector:
    app: opentelemetry-collector
  ports:
    - name: otlp-grpc
      port: 4317
      targetPort: 4317
      protocol: TCP
    - name: otlp-http
      port: 4318
      targetPort: 4318
      protocol: TCP
```

</code-group>

This dual approach ensures comprehensive Kubernetes monitor coverage:

- **DaemonSet** - Runs on every node, collects kubelet metrics and receives application traces
- **Deployment** - Runs as a single replica, collects cluster-level metrics via k8s_cluster receiver and Kubernetes events
- **DaemonSet ConfigMap** - Configuration for node-level collection (kubeletstats, OTLP)
- **Cluster ConfigMap** - Configuration for cluster-level collection (k8s_cluster, k8sobjects)
- **Service** - Exposes the collector for applications to send telemetry

> **ð¡ Automation Tip:** For automated deployment and management of collectors in Kubernetes, consider using the [OpenTelemetry Operator](/opentelemetry/operator). It simplifies collector lifecycle management through Kubernetes-native CRDs and enables auto-instrumentation for your applications.

## Troubleshooting

Common issues and solutions when setting up OpenTelemetry Kubernetes monitoring.

### Check Collector Status

Start by verifying the collector pods are running:

```bash
# Check pod status
kubectl get pods -n opentelemetry -l app=opentelemetry-collector

# View recent logs
kubectl logs -n opentelemetry -l app=opentelemetry-collector --tail=100

# Follow logs in real-time
kubectl logs -n opentelemetry -l app=opentelemetry-collector -f

# Describe pod for events and issues
kubectl describe pod -n opentelemetry -l app=opentelemetry-collector
```

### RBAC Permission Errors

**Error:** `pods is forbidden: User "system:serviceaccount:opentelemetry:opentelemetry-collector" cannot list resource "pods"`

**Solution:** Verify RBAC permissions are correctly configured:

```bash
# Test specific permissions
kubectl auth can-i get nodes --as=system:serviceaccount:opentelemetry:opentelemetry-collector
kubectl auth can-i list pods --as=system:serviceaccount:opentelemetry:opentelemetry-collector
kubectl auth can-i get nodes/stats --as=system:serviceaccount:opentelemetry:opentelemetry-collector

# Verify ClusterRole exists
kubectl get clusterrole opentelemetry-collector -o yaml

# Verify ClusterRoleBinding exists
kubectl get clusterrolebinding opentelemetry-collector -o yaml
```

If permissions are missing, reapply the RBAC configuration from the [Authentication & RBAC](#authentication--rbac) section.

### Kubelet Connection Issues

**Error:** `Get "https://node-name:10250/stats/summary": dial tcp: connection refused`

**Solutions:**

1. **Verify kubelet is accessible:**

```bash
kubectl get nodes -o wide
kubectl exec -it <collector-pod> -n opentelemetry -- \
  wget -qO- --no-check-certificate https://${K8S_NODE_NAME}:10250/healthz
```

1. **Check if kubelet read-only port is enabled:**

Some clusters disable the read-only port (10255). Use the secure port (10250) with `insecure_skip_verify: true` or configure proper TLS.

1. **For managed Kubernetes (EKS, GKE, AKS):**

Some providers restrict kubelet access. Check provider-specific documentation for collecting node metrics.

### No Metrics Appearing

If metrics aren't appearing in your backend:

**1. Enable debug logging:**

Add to your collector configuration:

```yaml
service:
  telemetry:
    logs:
      level: debug
```

**2. Verify exporter configuration:**

```bash
# Check collector configuration
kubectl get configmap otel-collector-config -n opentelemetry -o yaml

# Verify DSN is set correctly
kubectl logs -n opentelemetry -l app=opentelemetry-collector | grep -i "export"
```

**3. Check network connectivity:**

```bash
# Test TCP connectivity to Uptrace (port 4317 is gRPC, not HTTP)
kubectl exec -it <collector-pod> -n opentelemetry -- \
  nc -vz api.uptrace.dev 4317

# Alternative: test DNS resolution
kubectl exec -it <collector-pod> -n opentelemetry -- \
  nslookup api.uptrace.dev
```

### High Memory Usage

If the collector is using excessive memory:

**1. Enable memory limiter processor:**

```yaml
processors:
  memory_limiter:
    check_interval: 1s
    limit_mib: 400
    spike_limit_mib: 100

service:
  pipelines:
    metrics:
      processors: [memory_limiter, batch]
```

**2. Increase collection interval:**

```yaml
receivers:
  kubeletstats:
    collection_interval: 60s  # Increase from 20s
  k8s_cluster:
    collection_interval: 30s  # Increase from 10s
```

**3. Filter unnecessary metrics:**

```yaml
processors:
  filter:
    metrics:
      exclude:
        match_type: regexp
        metric_names:
          - ".*_bucket"  # Exclude histogram buckets
```

### Pod CrashLoopBackOff

If collector pods are repeatedly crashing:

```bash
# Check previous logs
kubectl logs -n opentelemetry <pod-name> --previous

# Check resource limits
kubectl describe pod -n opentelemetry <pod-name> | grep -A 5 "Limits"
```

Common causes:

- **OOMKilled:** Increase memory limits
- **Configuration error:** Validate YAML syntax
- **Missing secrets:** Ensure DSN/credentials are configured

## Monitoring with Uptrace

Once metrics are collected and exported, you can visualize them using Uptrace dashboards. Uptrace is an [OpenTelemetry backend](/blog/opentelemetry-backend) that supports distributed tracing, metrics, and logs.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks. It can process billions of spans and metrics on a single server, allowing you to monitor applications at 10x lower cost.

### Creating Kubernetes Dashboards

When telemetry data reaches Uptrace, you can create custom dashboards:

1. Navigate to **Dashboards** tab
2. Click **New Dashboard**
3. Add panels to visualize Kubernetes metrics

Useful visualizations include:

- **Time series charts** for CPU and memory usage over time
- **Gauges** for current resource utilization
- **Tables** for listing pods and their current state
- **Heatmaps** for distribution analysis

### Example Queries

Here are useful queries for Kubernetes monitoring. These queries match the v0.115.0 collector images used in this guide.

**CPU usage by namespace:**

```text
# For collector v0.124.0 and earlier:
avg(k8s.pod.cpu.utilization) by k8s.namespace.name

# For collector v0.125.0 and later (see deprecation notice):
avg(k8s.pod.cpu.usage) by k8s.namespace.name
```

**Memory usage by pod:**

```text
avg(k8s.pod.memory.working_set) by k8s.pod.name, k8s.namespace.name
```

**Container restarts:**

```text
sum(k8s.container.restarts) by k8s.pod.name, k8s.namespace.name
```

**Pod phase distribution:**

```text
count(k8s.pod.phase) by k8s.pod.phase
```

### Setting Up Alerts

Configure alerts to be notified of potential issues:

1. In your dashboard panel, click **Set Up Monitors** then **Create Alerts**
2. Set conditions, for example:

  - Pod restarts > 3 in 10 minutes
  - Node memory usage > 85% for 5 minutes
  - Deployment available replicas < desired replicas
3. Configure notification channels (email, Slack, PagerDuty, etc.)

### Getting Started with Uptrace

Try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## FAQ

**How does OpenTelemetry Kubernetes monitoring compare to Prometheus?**<br />


OpenTelemetry provides unified observability (metrics, traces, logs) while Prometheus focuses on metrics only. OTel offers better application correlation and vendor flexibility.

**Can I monitor multiple Kubernetes clusters?**<br />


Yes, deploy collectors in each cluster with unique cluster identifiers and send data to a central observability backend.

**What if I need alternatives to Kubernetes?**<br />


While this guide focuses on Kubernetes monitoring, you can explore [Kubernetes alternatives](/comparisons/kubernetes-alternatives) and apply similar OpenTelemetry monitoring principles.

**What's the resource overhead of OpenTelemetry collectors?**<br />


Typically 100-200MB memory and 0.1-0.2 CPU cores per collector pod, depending on traffic volume and configuration.

**How do I enable auto-instrumentation for applications?**<br />


Use the OpenTelemetry Operator to inject instrumentation automatically via annotations on pods and deployments.

## What's next?

Kubernetes cluster monitoring is now operational with OpenTelemetry collectors tracking pods, nodes, and services. For containerized application insights, see [Docker instrumentation](/guides/opentelemetry-docker), or add infrastructure monitoring with [PostgreSQL](/guides/opentelemetry-postgresql) and [Redis](/guides/opentelemetry-redis) for complete stack visibility. Explore [top APM tools](/tools/top-apm-tools) for Kubernetes observability.
