# Source: https://docs.vespa.ai/en/operations/monitoring.html.md

# Source: https://docs.vespa.ai/en/operations/kubernetes/monitoring.html.md

# Source: https://docs.vespa.ai/en/operations/self-managed/monitoring.html.md

# Monitoring

 

Vespa provides metrics integration with CloudWatch, Datadog and Prometheus / Grafana, as well as a JSON HTTP API.

There are two main approaches to transfer metrics to an external system:

- Have the external system _pull_ metrics from Vespa
- Make Vespa _push_ metrics to the external system

Use the example overview of two nodes running Vespa for where the APIs are set up and how they interact:

 ![Metrics interfaces](/assets/img/metrics-api.svg)
- [/metrics/v1/values](#metrics-v1-values) is the node metrics api, and aggregates metrics for processes running on the node.
- [/state/v1/metrics](#state-v1-metrics) is the process metrics api, and exposes all metrics from an individual service - here each node runs a container and a content node.
- [/metrics/v2/values](#metrics-v2-values) is an aggregation of [/metrics/v1/values](#metrics-v1-values), for all nodes. Served on the metrics-proxy port.
- [/prometheus/v1/values](/en/reference/api/prometheus-v1.html#prometheus-v1-values) is the same as [/metrics/v1/values](#metrics-v1-values), in prometheus format. Served on the metrics-proxy port.
- [/prometheus/v1/values](/en/reference/api/prometheus-v1.html#prometheus-v1-values) and [/metrics/v2/values](#metrics-v2-values) are also replicated on the container port, default 8080.

 **Note:** refer to the [multinode](https://github.com/vespa-engine/sample-apps/tree/master/examples/operations/multinode)and [multinode-HA](https://github.com/vespa-engine/sample-apps/tree/master/examples/operations/multinode-HA)sample applications for a practical example of using the APIs. These apps also include examples for how to find ports used by using[vespa-model-inspect](../../reference/operations/self-managed/tools.html#vespa-model-inspect).

See the [metrics guide](../metrics.html) for how to get a metric using `/metrics/v1/values` and `/prometheus/v1/values`. This guide also documents use of custom metrics and histograms.

## Metrics proxy

Each Vespa node has a _metrics-proxy_ process running for this API, default port 19092. It aggregates metrics from all processes on the node, and across nodes:

The metrics-proxy normally listens on port 19092 - use [vespa-model-inspect](../../reference/operations/self-managed/tools.html#vespa-model-inspect) to validate.

See the [metrics guide](../metrics.html) for the metrics interfaces hosted by the metrics proxy.

Metric-proxies intercommunicate to build a metric cache served on the internal _applicationmetrics/v1/_ API. This is replicated on the container on _/metrics/v2/values_ for easy access to all metrics for an application.

The metrics-proxy is started by the [config-sentinel](config-sentinel.html) and is not configurable. The metrics-proxy process looks like:

```
$ ps ax | grep admin/metrics/vespa-container

  703 ? Sl 0:10 /usr/bin/java
  -Dconfig.id=admin/metrics/vespa-container
  ...
  -cp /opt/vespa/lib/jars/jdisc_core-jar-with-dependencies.jar
  com.yahoo.jdisc.core.StandaloneMain
  file:/opt/vespa/lib/jars/container-disc-jar-with-dependencies.jar
```

## /state/v1/health

_Per-process_ health status is found at _http://host:port/state/v1/health_

 ![Health API](/assets/img/health-api.svg)

`/state/v1/health` is most commonly used for heartbeating, see the [reference](../../reference/api/state-v1.html#state-v1-health) for details. Example:

```
```
{
    "status": {
        "code": "up",
        "message": "Everything ok here"
    }
}
```
```

## /state/v1/metrics

_Per-process_ metrics are found at _http://host:port/state/v1/metrics_

Internally, Vespa aggregates metrics in the APIs above from the _per-process_ metrics and health APIs. While most users would use the aggregated APIs, the per-process metric APIs could be used for specific cases.

Metrics are reported in snapshots, where the snapshot specifies the time window the metrics are gathered from. Typically, the service will aggregate metrics as they are reported, and after each snapshot period, a snapshot is taken of the current values, and they are reset. Using this approach, min and max values are tracked, and enables values like 95% percentile for each complete snapshot period.

Refer to the [reference](../../reference/api/state-v1.html#state-v1-metrics) for details.

Vespa supports [custom metrics](../metrics.html#metrics-from-custom-components).

Example:

```
```
{
    "status" : {
        "code" : "up",
        "message" : "Everything ok here"
    },
    "metrics" : {
        "snapshot" : {
            "from" : 1334134640.089,
            "to" : 1334134700.088,
        },
        "values" : [
            {
                "name" : "queries",
                "description" : "Number of queries executed during snapshot interval",
                "values" : {
                    "count" : 28,
                    "rate" : 0.4667
                },
                "dimensions" : {
                    "chain" : "vespa"
                }
            },
            {
                "name" : "hits_per_query",
                "description" : "Number of hits returned for queries during snapshot interval",
                "values" : {
                    "count" : 28,
                    "rate" : 0.4667,
                    "average" : 128.3,
                    "min" : 0,
                    "max" : 1000,
                    "sum" : 3584,
                    "last" : 72,
                    "95percentile" : 849.1,
                    "99percentile": 672.0,
                },
                "dimensions" : {
                    "chain" : "vespa"
                }
            }
        ]
    }
}
```
```

A flat list of metrics is returned. Each metric value reported by a component should be a separate metric. For related metrics, prefix metric names with common parts and dot separate the names - e.g. `memory.free` and `memory.virtual`.

### /metrics/v1/values

This API can be used for monitoring, using products like [Prometheus](#pulling-into-prometheus) and [DataDog](#pulling-into-datadog). The response contains a selected set of metrics from each service running on the node, see the [reference](../../reference/api/metrics-v1.html) for details. Example:

```
$ curl http://localhost:19092/metrics/v1/values
```

```
```
{
    "services": [
        {
            "name": "vespa.container",
            "timestamp": 1661945852,
            "status": {
                "code": "up",
                "description": "Data collected successfully"
            },
            "metrics": [
                {
                    "values": {
                        "memory_virt": 3693178880,
                        "memory_rss": 1331331072,
                        "cpu": 2.3794255627932,
                        "cpu_util": 0.2379425562793
                    },
                    "dimensions": {
                        "metrictype": "system",
                        "instance": "container",
                        "clustername": "default",
                        "vespaVersion": "8.43.64"
                    }
                }
            ]
        }
    ]
}
```
```

### /metrics/v2/values

```
$ curl http://localhost:19092/metrics/v2/values
```

A container service on the same node as the metrics proxy might forward `/metrics/v2/values` on its own port, normally 8080.

`/metrics/v2/values` exposes a selected set of metrics for every service on all nodes for the application. For example, it can be used to [pull Vespa metrics to Cloudwatch](https://github.com/vespa-engine/metrics-emitter/tree/master/cloudwatch) using an AWS lambda function.

The [metrics API](#metrics-v2-values) exposes a [selected set of metrics](https://github.com/DataDog/integrations-extras/blob/master/vespa/metadata.csv) for the whole application, or for a single node, to allow integration with graphing and alerting services.

The response is a `nodes` list with metrics (see example output below), see the [reference](../../reference/api/metrics-v2.html) for details.

```
```
{
    "nodes": [
        {
            "hostname": "vespa-container",
            "role": "hosts/vespa-container",
            "services": [
                {
                    "name": "vespa.container",
                    "timestamp": 1634127924,
                    "status": {
                        "code": "up",
                        "description": "Data collected successfully"
                    },
                    "metrics": [
                        {
                            "values": {
                                "memory_virt": 3685253120,
                                "memory_rss": 1441259520,
                                "cpu": 29.1900152827305
                            },
                            "dimensions": {
                                "serviceId": "container"
                            }
                        },
                        {
                            "values": {
                                "jdisc.gc.ms.average": 0
                            },
                            "dimensions": {
                                "gcName": "G1OldGeneration",
                                "serviceId": "container"
                            }
                        },
```
```

### /prometheus/v1/values

Vespa provides a _node metrics API_ on each _node_ at _http://host:port/prometheus/v1/values_

Port and content is the same as _/metrics/v1/values_.

The prometheus API on each node exposes metrics in a text based [format](https://prometheus.io/docs/instrumenting/exposition_formats/) that can be scraped by [Prometheus](https://prometheus.io/docs/introduction/overview/). See below for a Prometheus / Grafana example.

## Pulling metrics from Vespa

All pull-based solutions use Vespa's [metrics API](#metrics-v2-values), which provides metrics in JSON format, either for the full system or for a single node. The polling frequency should be limited to max once every 30 seconds as more frequent polling would not give increased granularity but only lead to unnecessary load on your systems.

| Service | Description |
| --- | --- |
| CloudWatch | 

Metrics can be pulled into CloudWatch from both [Vespa Cloud](https://cloud.vespa.ai/) and self-hosted Vespa. The recommended solution is to use an AWS lambda function, as described in [Pulling Vespa metrics to Cloudwatch](https://github.com/vespa-engine/metrics-emitter/tree/master/cloudwatch).

 |
| Datadog | 

The Vespa team has created a Datadog Agent integration to allow real-time monitoring of Vespa in Datadog. The [Datadog Vespa](https://docs.datadoghq.com/integrations/vespa/) integration is not packaged with the agent, but is included in Datadog's [integrations-extras](https://github.com/DataDog/integrations-extras) repository. Clone it and follow the steps in the [README](https://github.com/DataDog/integrations-extras/blob/master/vespa/README.md).

 **Note:** The Datadog Agent integration currently works for self-hosted Vespa only.
 |
| Prometheus | 

Vespa exposes metrics in a text based [format](https://prometheus.io/docs/instrumenting/exposition_formats/) that can be scraped by [Prometheus](https://prometheus.io/docs/introduction/overview/). For [Vespa Cloud](https://cloud.vespa.ai/), append _/prometheus/v1/values_ to your endpoint URL. For self-hosted Vespa the URL is: _http://\<container-host\>:\<port\>/prometheus/v1/values_, where the _port_ is the same as for searching, e.g. 8080. Metrics for each individual host can also be retrieved at `http://host:19092/prometheus/v1/values`.

See the below for a Prometheus / Grafana example.

 |

## Pushing metrics to CloudWatch

**Note:** This method currently works for self-hosted Vespa only.

This is presumably the most convenient way to monitor Vespa in CloudWatch. Steps / requirements:

1. An IAM user or IAM role that only has the _putMetricData_ permission.
2. Store the credentials for the above user or role in a [shared credentials file](https://docs.aws.amazon.com/ses/latest/dg/create-shared-credentials-file.html) on each Vespa node. If a role is used, provide a mechanism to keep the credentials file updated when keys are rotated.
3. Configure Vespa to push metrics to CloudWatch - example configuration for the [admin](/en/reference/applications/services/admin.html) section in _services.xml_:
```
<metrics>
    <consumer id="my-cloudwatch">
        <metric-set id="default" />
        <cloudwatch region="us-east-1" namespace="my-vespa-metrics">
            <shared-credentials file="/path/to/credentials-file" />
        </cloudwatch>
    </consumer>
</metrics>
```
 This configuration sends the default set of Vespa metrics to the CloudWatch namespace `my-vespa-metrics` in the `us-east-1` region. Refer to the [metric list](https://github.com/DataDog/integrations-extras/blob/master/vespa/metadata.csv) for `default` metric set.

## Monitoring with Grafana

Follow these steps to set up monitoring with Grafana for a Vespa instance. This guide builds on the [quick start](../../basics/deploy-an-application-local.html) by adding three more Docker containers and connecting these in the Docker _monitoring_ network:

 ![Docker containers in a Docker network](/assets/img/monitoring-getting-started.svg)
1. **Run the Quick Start:**

2. **Create a network and add the _vespa_ container to it:**

3. **Launch Prometheus:**

4. **Launch Grafana:**

5. **Build the Random Data Feeder:**

6. **Run the Random Data Feeder:**

7. **Check the updated Grafana metrics:**

8. **Remove containers and network:**

## Histograms

Metric histograms is supported for [Gauge](https://javadoc.io/doc/com.yahoo.vespa/container-disc/latest/com/yahoo/metrics/simple/Gauge.html) metrics. Create the metric like in [album-recommendation-java](https://github.com/vespa-engine/sample-apps/tree/master/album-recommendation-java), adding the histogram:

```
public HitCountSearcher(MetricReceiver receiver) {
    this.hitCountMetric = receiver.declareGauge(EXAMPLE_METRIC_NAME, Optional.empty(),
        new MetricSettings.Builder().histogram(true).build());
}
```

The histograms for the last five minutes of logged data are available as CSV per dimension at [/state/v1/metrics/histograms](../../reference/api/state-v1.html#state-v1-metrics-histograms). Example output:

```
# start of metric hits_per_query, dimensions: { "chain": "metalchain" }
"Value","Percentile","TotalCount","1/(1-Percentile)"
1.00,0.000000000000,1,1.00
1.00,1.000000000000,1,Infinity
# end of metric hits_per_query, dimensions: { "chain": "metalchain" }
# start of metric example_hitcounts, dimensions: { "query_language": "en" }
"Value","Percentile","TotalCount","1/(1-Percentile)"
1.00,0.000000000000,1,1.00
1.00,1.000000000000,1,Infinity
# end of metric example_hitcounts, dimensions: { "query_language": "en" }
# start of metric query_latency, dimensions: { "chain": "metalchain" }
"Value","Percentile","TotalCount","1/(1-Percentile)"
5.69,0.000000000000,1,1.00
5.69,1.000000000000,1,Infinity
# end of metric query_latency, dimensions: { "chain": "metalchain" }
# start of metric totalhits_per_query, dimensions: { "chain": "metalchain" }
"Value","Percentile","TotalCount","1/(1-Percentile)"
1.00,0.000000000000,1,1.00
1.00,1.000000000000,1,Infinity
# end of metric totalhits_per_query, dimensions: { "chain": "metalchain" }
```

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Metrics proxy](#metrics-proxy)
- [/state/v1/health](#state-v1-health)
- [/state/v1/metrics](#state-v1-metrics)
- [/metrics/v1/values](#metrics-v1-values)
- [/metrics/v2/values](#metrics-v2-values)
- [/prometheus/v1/values](#prometheus-v1-values)
- [Pulling metrics from Vespa](#pulling-metrics-from-vespa)
- [Pushing metrics to CloudWatch](#pushing-metrics-to-cloudwatch)
- [Monitoring with Grafana](#monitoring-with-grafana)
- [Histograms](#histograms)

