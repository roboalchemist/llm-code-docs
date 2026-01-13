# Source: https://docs.datadoghq.com/containers/kubernetes/prometheus.md

# Source: https://docs.datadoghq.com/containers/docker/prometheus.md

---
title: Docker Prometheus and OpenMetrics metrics collection
description: >-
  Collect Prometheus and OpenMetrics metrics from containerized Docker
  applications using the Datadog Agent
breadcrumbs: >-
  Docs > Container Monitoring > Docker Agent for Docker, containerd, and Podman
  > Docker Prometheus and OpenMetrics metrics collection
source_url: https://docs.datadoghq.com/docker/prometheus/index.html
---

# Docker Prometheus and OpenMetrics metrics collection

Collect your exposed Prometheus and OpenMetrics metrics from your application running inside your containers by using the Datadog Agent, and the [Datadog-OpenMetrics](https://docs.datadoghq.com/integrations/openmetrics/) or [Datadog-Prometheus](https://docs.datadoghq.com/integrations/prometheus/) integrations.

## Overview{% #overview %}

Starting with version 6.5.0, the Agent includes [OpenMetrics](https://github.com/DataDog/integrations-core/tree/master/openmetrics) and [Prometheus](https://github.com/DataDog/integrations-core/tree/master/prometheus) checks capable of scraping Prometheus endpoints. Datadog recommends using the OpenMetrics check since it is more efficient and fully supports Prometheus text format. For more advanced usage of the `OpenMetricsCheck` interface, including writing a custom check, see the [Developer Tools](https://docs.datadoghq.com/developers/custom_checks/prometheus/) section. Use the Prometheus check only when the metrics endpoint does not support a text format.

This page explains the basic usage of these checks, enabling you to import all your Prometheus exposed metrics within Datadog.

The CLI commands on this page are for the Docker runtime. Replace `docker` with `nerdctl` for the containerd runtime, or `podman` for the Podman runtime.

## Setup{% #setup %}

### Installation{% #installation %}

Launch the Docker Agent next to your other containers by replacing `<DATADOG_API_KEY>` with the API key for your organization in the command below:

{% tab title="Standard" %}

```shell
docker run -d --cgroupns host \
    --pid host \
    -v /var/run/docker.sock:/var/run/docker.sock:ro \
    -v /proc/:/host/proc/:ro \
    -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
    -e DD_API_KEY="<DATADOG_API_KEY>" \
    -e DD_SITE="<YOUR_DATADOG_SITE>" \
    gcr.io/datadoghq/agent:latest
```

{% /tab %}

{% tab title="Amazon Linux version < 2" %}

```shell
docker run -d --name dd-agent -v /var/run/docker.sock:/var/run/docker.sock:ro \
    -v /proc/:/host/proc/:ro \
    -v /cgroup/:/host/sys/fs/cgroup:ro \
    -e DD_API_KEY="<DATADOG_API_KEY>" \
    -e DD_SITE="<YOUR_DATADOG_SITE>" \
    gcr.io/datadoghq/agent:latest
```

{% /tab %}

{% tab title="Windows" %}

```shell
docker run -d -e DD_API_KEY="<DATADOG_API_KEY>" \
    -e DD_SITE="<YOUR_DATADOG_SITE>" \
    gcr.io/datadoghq/agent:latest
```

{% /tab %}

**Note**: Your Datadog site is .

### Configuration{% #configuration %}

The Agent detects if it's running on Docker and automatically searches all container labels for Datadog-OpenMetrics labels. Autodiscovery expects labels to look like these examples, depending on the file type:

{% tab title="Dockerfile" %}

```
LABEL "com.datadoghq.ad.check_names"='["openmetrics"]'
LABEL "com.datadoghq.ad.init_configs"='[{}]'
LABEL "com.datadoghq.ad.instances"='[{"openmetrics_endpoint":"http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>","namespace":"<NAMESPACE>","metrics":[{"<METRIC_TO_FETCH>": "<NEW_METRIC_NAME>"}]}]'
```

#### Multiple endpoints example{% #multiple-endpoints-example %}

```
LABEL "com.datadoghq.ad.check_names"='["openmetrics","openmetrics"]'
LABEL "com.datadoghq.ad.init_configs"='[{},{}]'
LABEL "com.datadoghq.ad.instances"='[{"openmetrics_endpoint":"http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>","namespace":"<NAMESPACE>","metrics":[{"<METRIC_TO_FETCH>": "<NEW_METRIC_NAME>"}]}, {"openmetrics_endpoint":"http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>","namespace":"<NAMESPACE>","metrics":[{"<METRIC_TO_FETCH>": "<NEW_METRIC_NAME>"}]}]'
```

{% /tab %}

{% tab title="docker-compose.yaml" %}

```yaml
labels:
  com.datadoghq.ad.check_names: '["openmetrics"]'
  com.datadoghq.ad.init_configs: '[{}]'
  com.datadoghq.ad.instances: |
    [
      {
        "openmetrics_endpoint": "http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>",
        "namespace": "<NAMESPACE>",
        "metrics": [
          {"<METRIC_TO_FETCH>": "<NEW_METRIC_NAME>"}
        ]
      }
    ]
```

**Multiple endpoints example**:

```yaml
labels:
  com.datadoghq.ad.check_names: '["openmetrics", "openmetrics"]'
  com.datadoghq.ad.init_configs: '[{},{}]'
  com.datadoghq.ad.instances: |
    [
      {
        "openmetrics_endpoint": "http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>",
        "namespace": "<NAMESPACE>",
        "metrics": [
          {"<METRIC_TO_FETCH>": "<NEW_METRIC_NAME>"}
        ]
      },
      {
        "openmetrics_endpoint": "http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>",
        "namespace": "<NAMESPACE>",
        "metrics": [
          {"<METRIC_TO_FETCH>": "<NEW_METRIC_NAME>"}
        ]
      }
    ]
```

{% /tab %}

{% tab title="Docker run command" %}

```shell
# single metric
-l com.datadoghq.ad.check_names='["openmetrics"]' -l com.datadoghq.ad.init_configs='[{}]' -l com.datadoghq.ad.instances="[{\"openmetrics_endpoint\":\"http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>\",\"namespace\":\"<NAMESPACE>\",\"metrics\":[{\"<METRIC_TO_FETCH>\": \"<NEW_METRIC_NAME>\"}]}]"
```

**Examples of metrics formatting in `com.datadoghq.ad.instances`**

```shell
# multiple metrics
-l com.datadoghq.ad.instances="[{\"openmetrics_endpoint\":\"http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>\",\"namespace\":\"<NAMESPACE>\",\"metrics\":[{\"<METRIC_TO_FETCH>\": \"<NEW_METRIC_NAME>\"}, {\"<METRIC_TO_FETCH>\": \"<NEW_METRIC_NAME>\"}]}]"
```

```shell
# all metrics of a base type
-l com.datadoghq.ad.instances="[{\"openmetrics_endpoint\":\"http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>\",\"namespace\":\"<NAMESPACE>\",\"metrics\":[\"<METRIC_BASE_TO_FETCH>.*\"]}]"
```

```shell
# all metrics
-l com.datadoghq.ad.instances="[{\"openmetrics_endpoint\":\"http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT>\",\"namespace\":\"<NAMESPACE>\",\"metrics\":[\".*\"]}]"
```

**Multiple endpoints example**:

```shell
-l com.datadoghq.ad.check_names='["openmetrics", "openmetrics"]' -l com.datadoghq.ad.init_configs='[{},{}]' -l com.datadoghq.ad.instances='["{\"openmetrics_endpoint\":\"http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT> \",\"namespace\":\"<NAMESPACE>\",\"metrics\":[{\"<METRIC_TO_FETCH>\": \"<NEW_METRIC_NAME>\"}]}", "{\"openmetrics_endpoint\":\"http://%%host%%:<PROMETHEUS_PORT>/<PROMETHEUS_ENDPOINT> \",\"namespace\":\"<NAMESPACE>\",\"metrics\":[{\"<METRIC_TO_FETCH>\": \"<NEW_METRIC_NAME>\"}]}"]'
```

{% /tab %}

With the following configuration placeholder values:

| Placeholder             | Description                                                                                                                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PROMETHEUS_PORT>`     | Port to connect to in order to access the Prometheus endpoint. Can alternatively use the [Autodiscovery Template Variable](https://docs.datadoghq.com/agent/guide/template_variables/) `%%port%%`. |
| `<PROMETHEUS_ENDPOINT>` | URL path for the metrics served by the container, in Prometheus format.                                                                                                                            |
| `<NAMESPACE>`           | Set namespace to be prefixed to every metric when viewed in Datadog.                                                                                                                               |
| `<METRIC_TO_FETCH>`     | Prometheus metrics key to be fetched from the Prometheus endpoint.                                                                                                                                 |
| `<NEW_METRIC_NAME>`     | Transforms the `<METRIC_TO_FETCH>` metric key to `<NEW_METRIC_NAME>` in Datadog.                                                                                                                   |

The `metrics` configuration is a list of metrics to retrieve as custom metrics. Include each metric to fetch and the desired metric name in Datadog as key value pairs, for example, `{"<METRIC_TO_FETCH>":"<NEW_METRIC_NAME>"}`. You can alternatively provide a list of metric names strings, interpreted as regular expressions, to bring the desired metrics with their current names. **Note:** Regular expressions can potentially send a lot of custom metrics.

For a full list of available parameters for instances, including `namespace` and `metrics`, see the [sample configuration openmetrics.d/conf.yaml](https://github.com/DataDog/integrations-core/blob/master/openmetrics/datadog_checks/openmetrics/data/conf.yaml.example).

## Getting started{% #getting-started %}

### Simple metric collection{% #simple-metric-collection %}

To get started with collecting metrics exposed by Prometheus running within a container, follow these steps:

1. Launch the Datadog Agent:

   {% tab title="Standard" %}

   ```shell
   docker run -d --cgroupns host \
       --pid host \
       -v /var/run/docker.sock:/var/run/docker.sock:ro \
       -v /proc/:/host/proc/:ro \
       -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
       -e DD_API_KEY="<DATADOG_API_KEY>" \
       gcr.io/datadoghq/agent:latest
   ```

   {% /tab %}

   {% tab title="Windows" %}

   ```shell
   docker run -d -e DD_API_KEY="<DATADOG_API_KEY>" \
       gcr.io/datadoghq/agent:latest \
       -v \\.\pipe\docker_engine:\\.\pipe\docker_engine
   ```

   {% /tab %}



1. Launch a Prometheus container exposing example metrics for the Agent to collect, with the Autodiscovery Labels for the OpenMetrics Check.

The following labels will have the Agent collect the metrics `promhttp_metric_handler_requests`, `promhttp_metric_handler_requests_in_flight`, and all exposed metrics starting with `go_memory`.

   ```yaml
   labels:
     com.datadoghq.ad.check_names: '["openmetrics"]'
     com.datadoghq.ad.init_configs: '[{}]'
     com.datadoghq.ad.instances:  |
       [
         {
           "openmetrics_endpoint": "http://%%host%%:%%port%%/metrics",
           "namespace": "documentation_example_docker",
           "metrics": [
             {"promhttp_metric_handler_requests": "handler.requests"},
             {"promhttp_metric_handler_requests_in_flight": "handler.requests.in_flight"},
             "go_memory.*"
           ]
         }
       ]
   ```

To launch an example Prometheus container with these labels you can run:

   ```shell
   docker run -d -l com.datadoghq.ad.check_names='["openmetrics"]' -l com.datadoghq.ad.init_configs='[{}]' -l com.datadoghq.ad.instances='[{"openmetrics_endpoint":"http://%%host%%:%%port%%/metrics","namespace":"documentation_example_docker","metrics":[{"promhttp_metric_handler_requests":"handler.requests"},{"promhttp_metric_handler_requests_in_flight":"handler.requests.in_flight"},"go_memory.*"]}]' prom/prometheus
   ```

1. Go into your [Metric summary](https://app.datadoghq.com/metric/summary) page to see the collected metrics:

   {% image
      source="https://datadog-docs.imgix.net/images/integrations/guide/prometheus_docker/openmetrics_v2_collected_metric_docker.03df07b630996eb2a7d1193ecb6fa952.png?auto=format"
      alt="Prometheus metric collected docker" /%}

## From custom to official integration{% #from-custom-to-official-integration %}

By default, all metrics retrieved by the generic Prometheus check are considered custom metrics. If you are monitoring off-the-shelf software and think it deserves an official integration, don't hesitate to [contribute](https://docs.datadoghq.com/developers/custom_checks/prometheus/)!

Official integrations have their own dedicated directories. There's a default instance mechanism in the generic check to hardcode the default configuration and metrics metadata. For example, reference the [kube-proxy](https://github.com/DataDog/integrations-core/tree/master/kube_proxy) integration.

## Further Reading{% #further-reading %}

- [Collect your application logs](https://docs.datadoghq.com/agent/docker/log/)
- [Collect your application traces](https://docs.datadoghq.com/agent/docker/apm/)
- [Collect automatically your applications metrics and logs](https://docs.datadoghq.com/agent/docker/integrations/)
- [Limit data collection to a subset of containers only](https://docs.datadoghq.com/agent/guide/autodiscovery-management/)
- [Assign tags to all data emitted by a container](https://docs.datadoghq.com/agent/docker/tag/)
