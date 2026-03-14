# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/autoscaling.md

# Autoscaling

> Configure autoscaling for GitGuardian self-hosted installations using Kubernetes HPA or KEDA.

# Autoscaling

:::info
This page only concerns installation on an existing cluster using **[KOTS](/self-hosting/installation/installation-existing-cluster-kots)** or **[Helm](/self-hosting/installation/installation-existing-cluster-helm)**.
:::

## Requirements for autoscaling

You can use either **Kubernetes HPA (Horizontal Pod Autoscaler)** or **KEDA (Kubernetes Event-Driven Autoscaler)** for autoscaling. Both rely on the same metrics but have different requirements.

  - **HPA**: Kubernetes built-in, reads metrics from Metrics Server or external metrics pushed by Prometheus Adapter. A bit less responsive than KEDA. Cannot scale to zero replica.
  - **KEDA**: Reads events from a variety of sources (here Prometheus). Faster scaling. Can scale to zero replica. _Not available on KOTS-based installations._

### Required components

Depending on your chosen autoscaling method, you will need different components installed in your cluster:

| Component                                                                   | HPA | KEDA |
|:----------------------------------------------------------------------------|:---:|:----:|
| [Prometheus server](https://prometheus.io/)                                 | Required | Required |
| [Prometheus adapter](https://github.com/kubernetes-sigs/prometheus-adapter) | Required | Not required |
| [KEDA controller](https://keda.sh/)                                         | Not required | Required |

HPA requires Prometheus adapter to expose these metrics to the Kubernetes metrics API, while KEDA can directly query Prometheus.

### Installing Prometheus server

If you don't already have Prometheus in your cluster, we recommend installing the standalone Prometheus server using the official Helm chart.

Add the Prometheus Community Helm repository:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

You can then proceed to install Prometheus:

```bash
helm install prometheus prometheus-community/prometheus \
  --namespace monitoring \
  --create-namespace \
  --set alertmanager.enabled=false \
  --set prometheus-pushgateway.enabled=false
```

The Prometheus server will be available at `http://prometheus-server.monitoring.svc.cluster.local:80` (only reachable from within the cluster).

### Installing Prometheus adapter

If you choose to use HPA for autoscaling, install [Prometheus Adapter](https://github.com/kubernetes-sigs/prometheus-adapter) to expose Prometheus metrics to the Kubernetes metrics API.

```bash
helm install prometheus-adapter prometheus-community/prometheus-adapter \
  --namespace monitoring \
  --set prometheus.url=http://prometheus-server.monitoring.svc.cluster.local \
  --set prometheus.port=80
```

See the [Prometheus Adapter configuration](#prometheus-adapter-configuration) section below for the rules to add.

### Installing KEDA controller

Install the [KEDA controller](https://github.com/kedacore/keda) to enable autoscaling. You can install it using the [KEDA Helm chart](https://github.com/kedacore/charts) with the following commands:

```bash
helm repo add kedacore https://kedacore.github.io/charts
helm install keda kedacore/keda \
  --namespace keda \
  --create-namespace
```

You must configure the Helm values of your GitGuardian chart to allow KEDA to connect to your Prometheus server:

```yaml
autoscaling:
  keda:
    prometheus:
      metadata:
        # Use the Prometheus server address from your installation
        # Example with the prometheus-community/prometheus chart installed above:
        serverAddress: http://prometheus-server.monitoring.svc.cluster.local:80
        # Optional. Custom headers to include in query
        customHeaders: X-Client-Id=cid,X-Tenant-Id=tid,X-Organization-Id=oid
        # Optional. Specify authentication mode (basic, bearer, tls)
        authModes: bearer
      # Optional. Specify TriggerAuthentication resource to use when authModes is specified.
      authenticationRef:
        name: keda-prom-creds
```

A `ScaledObject` and an `hpa` will be created in the GitGuardian namespace.

## Autoscaling workers

Autoscaling allows for dynamic scaling of worker pods based on Celery task queue length as an external metric for scaling decisions, improving efficiency and performance while optimizing resource costs.

To enable autoscaling based on Celery queue lengths, you need first to enable application metrics following this [guide](../application-management/metrics.md#enable-or-disable-application-metrics).

If you use KEDA, configuring the Prometheus adapter is not necessary.

### Prometheus adapter configuration

Configure Prometheus adapter to expose Celery queue lengths as external metrics. This is done by setting up a custom rule in the Prometheus Adapter configuration.

The following rule should be added to your Prometheus Adapter Helm values to expose Celery queue lengths:

```yaml
rules:
  external:
    - seriesQuery: '{__name__="gim_celery_queue_length",queue_name!=""}'
      metricsQuery: sum(<<.Series>>{<<.LabelMatchers>>}) by (queue_name)
      resources:
        namespaced: true
        overrides:
          namespace:
            resource: namespace
```

If you use Machine Learning, you will also need this rule:

```yaml
rules:
  external:
    - seriesQuery: '{__name__="bentoml_service_request_in_progress",exported_endpoint!=""}'
      resources:
        namespaced: false
      metricsQuery: sum(<<.Series>>{<<.LabelMatchers>>}) by (<<.GroupBy>>)
```

### Autoscaling Behavior

The following behavior will be applied:

- **Scaling Up**: If the length of a Celery queue exceeds 10 tasks per current worker replica, the number of replicas will be increased, provided the current number of replicas is below the specified maximum limit.
- **Scaling Down**: If the number of tasks per current worker replica remains below 10 for a continuous period of 5 minutes, the number of replicas will be decreased, provided the current number of replicas is above the specified minimum limit.

![HPA behavior](/img/self-hosting/management/infrastructure-management/replicated_hpa_behavior.png)

:::info
Using KEDA, when the Celery queue is empty, the worker will transition to an idle state, resulting in the number of replicas being scaled down to zero.
:::

## KOTS-based installation

KOTS-based installation only allows HPA autoscaling.

Navigate under **Config > Scaling** in the [KOTS Admin Console](./admin-console), you will have access to the worker scaling options.

For each worker, you can enable autoscaling by ticking the option `Enable Horizontal Pod Autoscaling`, then you will be able to specify the minimum and the maximum replicas.
![Worker Autoscaling configuration](/img/self-hosting/management/infrastructure-management/replicated_worker_autoscaling.png)

## Helm-based installation

Customize Helm applications using your `local-values.yaml` file, submitted with the `helm` command.

### Autoscaling Workers

You can enable worker autoscaling by setting the following Helm values (here, we enable HPA for the "worker" worker):

```yaml
celeryWorkers:
  worker:
    autoscaling:
      hpa:
        enabled: true
      keda:
        enabled: false
      minReplicas: 1
      maxReplicas: 10
```

### Autoscaling the Machine Learning Secret Engine

For effective autoscaling of the **Machine Learning Secret Engine**, you must enable autoscaling for **both**:

- **The ML Worker processing the Celery queue** (`ml-api-priority`): this worker is responsible for queuing and dispatching ML-related tasks. Without autoscaling, it could become a bottleneck, leading to delays in processing requests.

- **The Secret Engine handling the computation** (`secretEngine`): enabling autoscaling for the Secret Engine ensures that it can scale in response to the demand for ML computations.

To enable autoscaling, configure the following Helm values:

```yaml
# ML Secret Engine
secretEngine:
  autoscaling:
      hpa:
        enabled: true
      keda:
        enabled: false
      minReplicas: 1
      maxReplicas: 2

celeryWorkers:
  # ML Worker
  ml-api-priority:
    autoscaling:
      hpa:
        enabled: true
      keda:
        enabled: false
      minReplicas: 1
      maxReplicas: 2
```

See [the values reference documentation](./helm-values) for further details.

:::caution
`autoscaling.hpa.enabled` and `autoscaling.keda.enabled` Helm parameters are mutually exclusive, you must choose between **hpa** (using Prometheus adapter) and **KEDA** controller.
:::
