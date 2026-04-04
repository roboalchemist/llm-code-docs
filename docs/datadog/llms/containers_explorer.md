# Source: https://docs.datadoghq.com/containers/monitoring/containers_explorer.md

---
title: Containers Explorer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Containers > Container Monitoring > Containers Explorer
---

# Containers Explorer

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/live-containers-overview_2.5cc0d52cb341156569dfb6135399d524.png?auto=format"
   alt="Live containers with summaries" /%}

In Datadog, the [Containers Explorer](https://app.datadoghq.com/containers) page (formerly known as Live Containers) provides real-time visibility into all containers across your environment.

Inspired by *htop*, *ctop*, and *kubectl*, Containers Explorer gives you complete coverage of your container infrastructure. View data in a continuously updated table with resource metrics at two-second resolution, faceted search, and streaming container logs.

## Configuration{% #configuration %}

### Set up container collection{% #set-up-container-collection %}

Collecting container telemetry for Containers Explorer is **enabled by default** for most Datadog Agent installations.

{% tab title="Docker" %}
When you install the Datadog Agent in a Docker-based environment, container collection is enabled by default.

To verify that container collection is enabled, ensure that `DD_PROCESS_CONFIG_CONTAINER_COLLECTION_ENABLED` is set to `true`.

For example:

```
-v /etc/passwd:/etc/passwd:ro
-e DD_PROCESS_CONFIG_CONTAINER_COLLECTION_ENABLED=true
```

{% /tab %}

{% tab title="Datadog Operator" %}
When you install the Datadog Agent by using the Datadog Operator, container collection is enabled by default.

To verify that container collection is enabled, ensure that `features.liveContainerCollection.enabled` is set to `true` in your `datadog-agent.yaml`:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    credentials:
      apiKey: <DATADOG_API_KEY>
      appKey: <DATADOG_APP_KEY>
  features:
    liveContainerCollection:
      enabled: true
```

{% /tab %}

{% tab title="Helm" %}
When you install the Datadog Agent by using the [official Helm chart](https://github.com/DataDog/helm-charts), container collection is enabled by default.

To verify that container collection is enabled, ensure that the `processAgent.containerCollection` parameter is set to `true` in your `datadog-values.yaml` file:

```yaml
datadog:
  # (...)
  processAgent:
    containerCollection: true
```

#### Troubleshooting: No cluster name set{% #troubleshooting-no-cluster-name-set %}

If you see the error `Orchestrator explorer enabled but no cluster name set: disabling.` error, Datadog is failing to detect your Kubernetes cluster name. To fix, set `datadog.clusterName` to your cluster name in the `datadog-values.yaml` file.

```yaml
datadog:
  #(...)
  clusterName: <YOUR_CLUSTER_NAME>
  #(...)
  processAgent:
    containerCollection: true
```

{% /tab %}

{% tab title="Amazon ECS" %}
Update your task definitions with the following environment variable:

```json
{
  "name": "DD_PROCESS_CONFIG_CONTAINER_COLLECTION_ENABLED",
  "value": "true"
}
```

{% /tab %}

{% alert level="info" %}
To set up Containers Explorer for Datadog Agent v7.21.1 - v7.27.0 and Cluster Agent v1.9.0 - 1.11.0, see [Live Containers legacy configuration](https://docs.datadoghq.com/infrastructure/faq/live-containers-legacy-configuration).
{% /alert %}

### Include or exclude containers{% #include-or-exclude-containers %}

By default, Datadog automatically discovers all containers.

You can include or exclude containers from collection by using these environment variables:

- `DD_CONTAINER_EXCLUDE`: Blocklist of containers to exclude
- `DD_CONTAINER_INCLUDE`: Allowlist of containers to include

Regular expressions are supported.

#### Example: Including and excluding containers{% #example-including-and-excluding-containers %}

To exclude all Debian containers (`image:debian`) except containers with a name starting with `frontend` (`name:frontend.*`):

{% tab title="Docker" %}

```shell
docker run -d --name datadog-agent \
           (...) \
           -e DD_CONTAINER_EXCLUDE="image:debian" \
           -e DD_CONTAINER_INCLUDE="name:frontend.*"
```

{% /tab %}

{% tab title="Datadog Operator" %}

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    credentials:
      apiKey: <DATADOG_API_KEY>
  override:
    nodeAgent:
      env:
        - name: DD_CONTAINER_EXCLUDE
          value: "image:debian"
        - name: DD_CONTAINER_INCLUDE
          value: "name:frontend.*"
```

{% /tab %}

{% tab title="Helm" %}

```yaml
datadog:
  containerExclude: "image:debian"
  containerInclude: "name:frontend.*"
```

{% /tab %}

{% tab title="Amazon ECS" %}
Update your task definition:

```json
"environment": [
  {
    "name": "DD_CONTAINER_EXCLUDE",
    "value": "image:debian"
  },
  {
    "name": "DD_CONTAINER_INCLUDE",
    "value": "name:frontend.*"
  },
  ...
]
```

{% /tab %}

For more granular configuration options, see [Container Discovery Management](https://docs.datadoghq.com/containers/guide/container-discovery-management)

### Scrub sensitive information from manifests{% #scrub-sensitive-information-from-manifests %}

To help prevent leaking sensitive data, the Agent can be configured to scrub the collected Kubernetes YAML manifests. This scrubbing feature is applied to:

- Annotation values
- Label values
- Probe configurations (HTTP headers and commands)
- Environment variables
- Container exec commands

The scrubbing algorithm attempts to detect key-value pairs containing secrets based on a set of sensitive keywords, replacing corresponding values with `********`. This logic is applied to structured key-value pairs (such as environment variables) as well as values that look like JSON or YAML content, which may contain key-value pairs within the content.

Scrubbing is enabled by default using the following sensitive keywords:

- `password`
- `passwd`
- `mysql_pwd`
- `access_token`
- `auth_token`
- `api_key`
- `apikey`
- `pwd`
- `secret`
- `credentials`
- `stripetoken`

You can supply additional sensitive keywords by providing a space-delimited list in the environment variable: `DD_ORCHESTRATOR_EXPLORER_CUSTOM_SENSITIVE_WORDS`. This adds to the default words and does not overwrite them. To use this environment variable, you must configure it for following Agents:

```yaml
env:
    - name: DD_ORCHESTRATOR_EXPLORER_CUSTOM_SENSITIVE_WORDS
      value: "customword1 customword2 customword3"
```

**Note**: Any additional sensitive words must be provided as lowercase strings. The Agent converts text to lowercase before matching for sensitive words. If the sensitive word is `password`, `MY_PASSWORD=1234` is scrubbed to `MY_PASSWORD=********` because the Agent converts `MY_PASSWORD` to `my_password`, which mean the sensitive word `PASSWORD` does not match anything.

For example, because `password` is a sensitive word, the scrubber changes `<MY_PASSWORD>` in any of the following to a string of asterisks, `***********`:

```text
password <MY_PASSWORD>
password=<MY_PASSWORD>
password: <MY_PASSWORD>
password::::== <MY_PASSWORD>
config={"password":"<MY_PASSWORD>"}
```

However, the scrubber does not scrub paths that contain sensitive words. For example, it does not overwrite `/etc/vaultd/secret/haproxy-crt.pem` with `/etc/vaultd/******/haproxy-crt.pem` even though `secret` is a sensitive word.

## Searching, filtering, and pivoting{% #searching-filtering-and-pivoting %}

### String search{% #string-search %}

Containers are, by their nature, extremely high cardinality objects. Datadog's flexible string search matches substrings in the container name, ID, or image fields.

To combine multiple string searches into a complex query, you can use any of the following Boolean operators:

{% dl %}

{% dt %}
`AND`
{% /dt %}

{% dd %}
**Intersection**: both terms are in the selected events (if nothing is added, AND is taken by default)**Example**: `java AND elasticsearch`
{% /dd %}

{% dt %}
`OR`
{% /dt %}

{% dd %}
**Union**: either term is contained in the selected events**Example**: `java OR python`
{% /dd %}

{% dt %}
`NOT` / `!`
{% /dt %}

{% dd %}
**Exclusion**: the following term is NOT in the event. You may use the word `NOT` or `!` character to perform the same operation**Example**: `java NOT elasticsearch` or `java !elasticsearch`
{% /dd %}

{% /dl %}

Use parentheses to group operators together. For example, `(NOT (elasticsearch OR kafka) java) OR python`.

### Filtering and pivoting{% #filtering-and-pivoting %}

The screenshot below displays a system that has been filtered down to a Kubernetes cluster of 25 nodes. RSS and CPU utilization on containers is reported compared to the provisioned limits on the containers, when they exist. Here, it is apparent that the containers in this cluster are over-provisioned. You could use tighter limits and bin packing to achieve better utilization of resources.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/filter-by.e384428c03065dc6607de45d1d92a63a.png?auto=format"
   alt="A system that has been filtered down to a Kubernetes cluster of 25 nodes" /%}

Container environments are dynamic and can be hard to follow. The following screenshot displays a view that has been pivoted by `kube_service` and `host`âand, to reduce system noise, filtered to `kube_namespace:default`. You can see what services are running where, and how saturated key metrics are:

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/hostxservice.46324e307762b343302d289fd6db845c.png?auto=format"
   alt="Host x services" /%}

You could pivot by ECS `ecs_task_name` and `ecs_task_version` to understand changes to resource utilization between updates.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/tasksxversion2.bc4a04dee516a6805a7e7ab6426593b1.png?auto=format"
   alt="Tasks x version" /%}

## Tagging{% #tagging %}

Containers are [tagged](https://docs.datadoghq.com/tagging/assigning_tags?tab=agentv6v7#host-tags) with all existing host-level tags, as well as with metadata associated with individual containers.

All containers are tagged by `image_name`, including integrations with popular orchestrators, such as [ECS](https://docs.datadoghq.com/agent/amazon_ecs/) and [Kubernetes](https://docs.datadoghq.com/agent/kubernetes/), which provide further container-level tags. Additionally, each container is decorated with Docker, ECS, or Kubernetes icons so you can tell which are being orchestrated at a glance.

ECS containers are tagged by:

- `task_name`
- `task_version`
- `ecs_cluster`

Kubernetes containers are tagged by:

- `pod_name`
- `kube_service`
- `kube_namespace`
- `kube_replica_set`
- `kube_daemon_set`
- `kube_job`
- `kube_deployment`
- `kube_cluster_name`

If you have a configuration for [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging) in place, Datadog automatically picks up `env`, `service`, and `version` tags. Having these tags available lets you tie together APM, logs, metrics, and container data.

## Views{% #views %}

The Containers page includes Scatter Plot and [Timeseries](https://docs.datadoghq.com/dashboards/widgets/timeseries/) views, and a table to better organize your container data by fields such as container name, status, and start time.

#### Scatter plot{% #scatter-plot %}

Use the scatter plot analytic to compare two metrics with one another in order to better understand the performance of your containers.

You can switch between the "Scatter Plot" and "Timeseries" tabs in the collapsible **Summary Graphs** section in the Containers page:

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/scatterplot_selection.50870d0881eba218cb9e45fe6ea6fb09.png?auto=format"
   alt="Scatter plot selection" /%}

By default, the graph groups by the `short_image` tag key. The size of each dot represents the number of containers in that group, and clicking on a dot displays the individual containers and hosts that contribute to the group.

The options at the top of the graph allow you to control your scatter plot analytic:

- Selection of metrics to display.
- Selection of the aggregation method for both metrics.
- Selection of the scale of both X and Y axis (*Linear*/*Log*).

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/scatterplot.a2d9f17d236c84156b46e49a5112adca.png?auto=format"
   alt="Scatter plot" /%}

#### Real-time monitoring{% #real-time-monitoring %}

While actively working with the containers page, metrics are collected at a 2-second resolution. This is important for volatile metrics such as CPU. In the background, for historical context, metrics are collected at 10s resolution.

### Container logs{% #container-logs %}

View streaming logs for any container like `docker logs -f` or `kubectl logs -f` in Datadog. Click any container in the table to inspect it. Click the *Logs* tab to see real-time data from [live tail](https://docs.datadoghq.com/logs/explorer/live_tail) or indexed logs for any time in the past.

#### Live tail{% #live-tail %}

With live tail, all container logs are streamed. Pausing the stream helps you read logs that are quickly being written; unpause to continue streaming.

Streaming logs can be searched with simple string matching. See [Live Tail](https://docs.datadoghq.com/logs/explorer/live_tail) for more details.

**Note**: Streaming logs are not persisted, and entering a new search or refreshing the page clears the stream.

{% video
   url="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/livecontainerlogssidepanel.mp4" /%}

#### Indexed logs{% #indexed-logs %}

You can see indexed logs that you have chosen to index and persist by selecting a corresponding timeframe. Indexing allows you to filter your logs using tags and facets. For example, to search for logs with an Error status, type status:error into the search box. Autocompletion can help you locate the particular tag that you want. Key attributes about your logs are already stored in tags, which enables you to search, filter, and aggregate as needed.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/errorlogs.2eb3e5e93b297ab47a8cd0d0786d9113.png?auto=format"
   alt="Preview Logs Side panel" /%}

## Additional information{% #additional-information %}

- Real-time (2s) data collection is turned off after 30 minutes. To resume real-time collection, refresh the page.
- RBAC settings can restrict Kubernetes metadata collection. See the [RBAC entities for the Datadog Agent](https://github.com/DataDog/datadog-agent/blob/7.23.1/Dockerfiles/manifests/cluster-agent/rbac.yaml).
- In Kubernetes the `health` value is the containers' readiness probe, not its liveness probe.

## Further reading{% #further-reading %}

- [Monitor your Kubernetes operators to keep applications running smoothly](https://www.datadoghq.com/blog/kubernetes-operator-performance)
- [A deep dive into CPU requests and limits in Kubernetes](https://www.datadoghq.com/blog/kubernetes-cpu-requests-limits/)
- [Expedite infrastructure investigations with Kubernetes Anomalies](https://www.datadoghq.com/blog/monitor-kubernetes-anomalies/)
- [Practical tips for rightsizing your Kubernetes workloads](https://www.datadoghq.com/blog/rightsize-kubernetes-workloads/)
- [Accelerate Kubernetes issue resolution with AI-powered guided remediation](https://www.datadoghq.com/blog/kubernetes-active-remediation-ai/)
