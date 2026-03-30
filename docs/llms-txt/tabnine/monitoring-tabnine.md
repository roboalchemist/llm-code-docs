# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/monitoring-tabnine.md

# Monitoring & Logs

## Overview <a href="#overview" id="overview"></a>

This document will go over how Tabnine services deployed on-premise can be monitored and go over a few examples of monitoring our services locally. You can also enable Tabnine telemetry, which uses the principles shown in this document and reports the data to Tabnine’s servers.

As Tabnine’s self-hosted solution runs in a Kubernetes cluster, we rely on standard tools for our logs and metrics - logs are written to the stdout, and metrics are exposed using http endpoints in Prometheus format.

Note that as both writing logs to stdout and exposing metrics endpoints for scraping are industry standards when working in the Kubernetes ecosystem, there is an extensive collection of tools and platforms that support those formats. This document will go over the configuration options for scrapping metrics and will also provide examples for setting up a simple [Prometheus](https://prometheus.io/) server for scraping the metrics and [FluentBit](https://fluentbit.io/) for the collection of the logs into a centralized endpoint.

## Logs <a href="#logs" id="logs"></a>

All Tabnine services output their logs to the stdout. They are picked by and managed by Kubernetes, which allows integration with standard tools for log management and retention.

In Kubernetes, the standard way to deal with logs is to run a collection service, such as [FluentD](https://www.fluentd.org/) or [FluentBit](https://fluentbit.io/), which collects the logs from the pods and forwards them to a centralized location. Cloud providers usually have an official way of integrating the logs with their native logging platforms. However, they all use FluentD or FluentBit under the hood.

When Tabnine’s telemetry is enabled, we install and use FluentD to forward logs from the cluster to Tabnine’s servers.

Log messages are in the following format:

```json
{
  "timestamp": "2023-01-15T03:46:06.861Z",
  "level": "error/warning/info/debug",
  "message": "msg content"
}
```

**How to send logs to an external log management system**

* Cloud providers
  * [GKE - Google’s Kubernetes Engine logs to **StackDriver** by default based on fluentbit, and it enabled by default](https://cloud.google.com/stackdriver/docs/solutions/gke/managing-logs)
  * [EKS - Amazon’s Elastic Kubernetes Service supports logging to **CloudWatch** both fluentbit and fluentd](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-logs.html)
  * [AKS - Azure allows you to view live data with **Container insights** from Azure Kubernetes Service (AKS) clusters](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-livedata-overview)[<br>](https://docs.newrelic.com/docs/logs/get-started/get-started-log-management/)
* 3rd party log management tools
  * [NewRelic](https://docs.newrelic.com/docs/logs/get-started/get-started-log-management/)
  * [Coralogix](https://coralogix.com/docs/fluentbit-helm-chart-for-kubernetes/)
  * [Logz.io](https://docs.logz.io/shipping/log-sources/kubernetes.html)
  * [Datadog](https://docs.datadoghq.com/containers/kubernetes/installation/)

### Tabnine Audit Logs API

Audit logs are available through the Tabnine Audit Logs API

## Metrics <a href="#metrics" id="metrics"></a>

Tabnine services export Prometheus metrics and rely on having Prometheus Operator installed on the cluster. If you are unfamiliar with how to install a Prometheus Operator please follow [Prometheus Operator install](https://docs.tabnine.com/enterprise/admin-guide/prometheus-operator-install) article.

#### Enable monitoring of metrics <a href="#enable-monitoring-of-metrics" id="enable-monitoring-of-metrics"></a>

In order to enable Tabnine metrics monitoring, edit the following sections in `values.yaml`.

```yaml
global:
  monitoring:
    enabled: true
    # labels -- by default. If your Promtheus server requires specific labels to be present for the monitors to be picked up, add them here
    labels: {}
    # annotations -- by default. Some platforms require specific annotations to be present, this setting will apply the annotation to all monitor objects
    annotations: {}
  tabnine:
    telemetry:
      # enabled -- Send telemetry data to Tabnine backend
      enabled: false
```

Now that `values.yaml` is updated, it is time to install the chart on the cluster.

```shell
helm upgrade --install -n tabnine --create-namespace tabnine oci://registry.tabnine.com/self-hosted/tabnine-cloud --values values.yaml
```

### Prometheus example <a href="#prometheus-example" id="prometheus-example"></a>

#### Values file examples <a href="#values-file-examples" id="values-file-examples"></a>

The following example adds a `release=prom-example` label to all `PodMonitor`s and `ServiceMonitor` created by Tabnine as part of the installation.

```yaml
global:
  monitoring:
    enabled: true
    labels:
      release: prom-example
  image:
    imagePullSecrets:
      - name: regcred
  tabnine:
  [...]
```

#### Prometheus configuration file <a href="#prometheus-configuration-file" id="prometheus-configuration-file"></a>

The following configuration:

1. Scrapes only PodMonitors and ServiceMonitors with a `release=prom-example` label,
2. keeps the data for 14 days
3. requires 50GB of storage
4. requires 6G of RAM to operate

for full list of available configurations, please check the [Prometheus (CRD) documentation](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api.md#monitoring.coreos.com/v1.PrometheusSpec)

```
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: prom-example
  namespace: monitoring
spec:
  evaluationInterval: 30s
  paused: false
  podMonitorNamespaceSelector: {}
  podMonitorSelector:
    matchLabels:
      release: prom-example
  portName: http-web
  probeNamespaceSelector: {}
  probeSelector:
    matchLabels:
      release: prom-example
  replicas: 1
  resources:
    limits:
      cpu: 1
      memory: 6G
    requests:
      cpu: 1
      memory: 6G
  retention: 14d
  routePrefix: /
  ruleNamespaceSelector: {}
  ruleSelector:
    matchLabels:
      release: prom-example
  scrapeInterval: 30s
  securityContext:
    fsGroup: 2000
    runAsGroup: 2000
    runAsNonRoot: true
    runAsUser: 1000
  serviceMonitorNamespaceSelector: {}
  serviceMonitorSelector:
    matchLabels:
      release: prom-example
  shards: 1
  storage:
    volumeClaimTemplate:
      spec:
        resources:
          requests:
            storage: 50Gi
  version: v2.42.0
```

### Prometheus Operator Install <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0c9e271dca6232ae6a4d7479ee437207a78827ba%2Fprometheus%20orange%20logo.png?alt=media" alt="" data-size="line">

[Prometheus operator](https://github.com/prometheus-operator/prometheus-operator) allows setting up and configuring Prometheus servers running in your cluster. As part of the helm installation we also set up by default `ServiceMonitor` and `PodMonitor` objects which define how to scrape our services.

If your cluster doesn’t have Prometheus operator installed already, you can install one from our repository or the [official helm](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack), depending on your setup. Note that, unlike the official helm, Tabnine’s version doesn’t install Prometheus server by default (`.prometheus.enabled` is set to false). If you opt-in to install the prometheus server as part of the `kube-prometheus-stack` - either from the official helm or by setting `.prometheus.enabled=true` in our chat’s values, you will need to fine-tune the server configuration in the helm chart and not in the `Prometheus` server object shown later on, as it will be created by the helm chart.

```shell
helm upgrade --install --create-namespace -n monitoring monitoring oci://registry.tabnine.com/self-hosted/kube-prometheus-stack

```

**Check if there is an installed operator in your cluster**

If you are unsure if the operator is in your cluster, you can run the following commands

```shell
# Make sure you have the relevant CRDs installed
$ kubectl get crd | grep monitoring.coreos.com
alertmanagerconfigs.monitoring.coreos.com        2022-12-08T13:15:57Z
alertmanagers.monitoring.coreos.com              2022-12-08T13:15:57Z
podmonitors.monitoring.coreos.com                2022-12-08T13:15:58Z
probes.monitoring.coreos.com                     2022-12-08T13:15:58Z
prometheuses.monitoring.coreos.com               2022-12-08T13:15:59Z
prometheusrules.monitoring.coreos.com            2022-12-08T13:15:59Z
servicemonitors.monitoring.coreos.com            2022-12-08T13:16:00Z
thanosrulers.monitoring.coreos.com               2022-12-08T13:16:00Z

# Make sure there is a prometheus operator running. Note that depening on the helm installation the name might be slightly different.
$ kubectl get pods -A | grep operator
monitoring                     kube-prometheus-stack-operator-XX

```

**Check if you already have Prometheus server in your cluster**

```shell
$ kubectl get prometheus -A
NAMESPACE    NAME
monitoring   kube-prometheus-stack-prometheus
```

Note that if you have enabled telemetry as part of Tabnine installation, you will see a Prometheus server created by Tabnine. That server is used for [remote-writing](https://prometheus.io/docs/concepts/remote_write_spec/) metrics to Tabnine and doesn’t persist data locally. If that is the only server you see in the list, or there are none, you can create a server based on the example below.

If you have a Prometheus server, It might be configured the collect data only from `Pod/ServiceMontor`s with specific labels and/or namespaces. Run the following command (based on the example output above, this might be different in your environment) and check the output of the following fields

* `Pod Monitor Namespace Selector`
* `Pod Monitor Selector`
* `Service Monitor Namespace Selector`
* `Service Monitor Selector`

In its default setup `kube-prometheus-stack` requires some labels to be present on the monitor objects for them to be propagated to the Prometheus server. If that is the case, write down the required labels - we will use them below
