# Source: https://docs.datadoghq.com/infrastructure/process.md

---
title: Live Processes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Live Processes
---

# Live Processes

{% alert level="info" %}
Live Processes and Live Process Monitoring are included in the Enterprise plan. For all other plans, contact your account representative or [success@datadoghq.com](mailto:success@datadoghq.com) to request this feature.
{% /alert %}

## Introduction{% #introduction %}

Datadog's Live Processes gives you real-time visibility into the processes running on your infrastructure. Use Live Processes to:

- View all of your running processes in one place
- Break down the resource consumption on your hosts and containers at the process level
- Query for processes running on a specific host, in a specific zone, or running a specific workload
- Monitor the performance of the internal and third-party software you run using system metrics at two-second granularity
- Add context to your dashboards and notebooks

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/process/live_processes_main.3b38fc749ef09c75f61cebbb91ec064d.png?auto=format"
   alt="Live Processes Overview" /%}

## Installation{% #installation %}

If you are using Agent 5, follow this [specific installation process](https://docs.datadoghq.com/agent/faq/agent-5-process-collection/). If you are using Agent 6 or 7, [see the instructions below](https://docs.datadoghq.com/agent/).

{% tab title="Linux/Windows" %}
Once the Datadog Agent is installed, enable Live Processes collection by editing the [Agent main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/) by setting the following parameter to `true`:

```yaml
process_config:
  process_collection:
    enabled: true
```

Additionally, some configuration options may be set as environment variables.

**Note**: Options set as environment variables override the settings defined in the configuration file.

After configuration is complete, [restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent).
{% /tab %}

{% tab title="Docker" %}
Follow the instructions for the [Docker Agent](https://docs.datadoghq.com/agent/docker/#run-the-docker-agent), passing in the following attributes, in addition to any other custom settings as appropriate:

```text
-v /etc/passwd:/etc/passwd:ro
-e DD_PROCESS_CONFIG_PROCESS_COLLECTION_ENABLED=true
```

**Note**:

- To collect container information in the standard install, the `dd-agent` user must have permissions to access `docker.sock`.
- Running the Agent as a container still allows you to collect host processes.

{% /tab %}

{% tab title="Helm" %}
Update your [datadog-values.yaml](https://github.com/DataDog/helm-charts/blob/master/charts/datadog/values.yaml) file with the following process collection configuration:

```yaml
datadog:
    # (...)
    processAgent:
        enabled: true
        processCollection: true
```

Then, upgrade your Helm chart:

```shell
helm upgrade -f datadog-values.yaml <RELEASE_NAME> datadog/datadog
```

**Note**: Running the Agent as a container still allows you to collect host processes.
{% /tab %}

{% tab title="Datadog Operator" %}
In your `datadog-agent.yaml`, set `features.liveProcessCollection.enabled` to `true`.

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    credentials:
      apiKey: <DATADOG_API_KEY>

  features:
    liveProcessCollection:
      enabled: true
```

After making your changes, apply the new configuration by using the following command:

```shell
kubectl apply -n $DD_NAMESPACE -f datadog-agent.yaml
```

**Note**: Running the Agent as a container still allows you to collect host processes.
{% /tab %}

{% tab title="Kubernetes (Manual)" %}
In the `datadog-agent.yaml` manifest used to create the DaemonSet, add the following environmental variables, volume mount, and volume:

```yaml
 env:
    - name: DD_PROCESS_CONFIG_PROCESS_COLLECTION_ENABLED
      value: "true"
  volumeMounts:
    - name: passwd
      mountPath: /etc/passwd
      readOnly: true
  volumes:
    - hostPath:
        path: /etc/passwd
      name: passwd
```

See the standard [DaemonSet installation](https://docs.datadoghq.com/containers/guide/kubernetes_daemonset) and the [Docker Agent](https://docs.datadoghq.com/agent/docker/#run-the-docker-agent) information pages for further documentation.

**Note**: Running the Agent as a container still allows you to collect host processes.
{% /tab %}

{% tab title="AWS ECS Fargate" %}

{% alert level="info" %}
You can view your ECS Fargate processes in Datadog. To see their relationship to ECS Fargate containers, use the Datadog Agent v7.50.0 or later.
{% /alert %}

In order to collect processes, the Datadog Agent must be running as a container within the task.

To enable process monitoring in ECS Fargate, set the `DD_PROCESS_AGENT_PROCESS_COLLECTION_ENABLED` environment variable to `true` in the Datadog Agent container definition within the task definition.

For example:

```json
{
    "taskDefinitionArn": "...",
    "containerDefinitions": [
        {
            "name": "datadog-agent",
            "image": "public.ecr.aws/datadog/agent:latest",
            ...
            "environment": [
                {
                    "name": "DD_PROCESS_AGENT_PROCESS_COLLECTION_ENABLED",
                    "value": "true"
                }
                ...
             ]
         ...
         }
    ]
  ...
}
```

To start collecting process information in ECS Fargate, add the [`pidMode` parameter](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#other_task_definition_params) to the Task Definition and set it to `task` as follows:

```text
"pidMode": "task"
```

Once enabled, use the `AWS Fargate` Containers facet on the [Live Processes page](https://app.datadoghq.com/process) to filter for processes running in ECS, or enter `fargate:ecs` in the search query.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/process/fargate_ecs.fb37a1fb06a879b110dc2fe23d629b55.png?auto=format"
   alt="Processes in AWS Fargate" /%}

For more information about installing the Datadog Agent with AWS ECS Fargate, see the [ECS Fargate integration documentation](https://docs.datadoghq.com/integrations/ecs_fargate/#installation).
{% /tab %}

### I/O stats{% #io-stats %}

I/O and open files stats can be collected by the Datadog system-probe, which runs with elevated privileges. To collect these stats, enable the process module of the system-probe:

1. Copy the system-probe example configuration:

   ```shell
   sudo -u dd-agent install -m 0640 /etc/datadog-agent/system-probe.yaml.example /etc/datadog-agent/system-probe.yaml
   ```

1. Edit `/etc/datadog-agent/system-probe.yaml` to enable the process module:

   ```yaml
   system_probe_config:
     process_config:
       enabled: true
   ```

1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent):

   ```shell
   sudo systemctl restart datadog-agent
   ```

**Note**: If the `systemctl` command is not available on your system, run the following command instead: `sudo service datadog-agent restart`

### Optimized process collection footprint{% #optimized-process-collection-footprint %}

On Linux, the Datadog Agent's overall footprint is reduced by running container and process collection in the core Datadog Agent (instead of the separate Process Agent). In Datadog Agent v7.65.0+, this is enabled by default. **Note**: the Process Agent is still required for [Cloud Network Monitoring](https://docs.datadoghq.com/network_monitoring/cloud_network_monitoring/).

The Agent status for this feature is listed under the `Process Component` section, for example:

```text
=================
Process Component
=================


  Enabled Checks: [process rtprocess]
  System Probe Process Module Status: Not running
  Process Language Detection Enabled: False

  =================
  Process Endpoints
  =================
    https://process.datadoghq.com. - API Key ending with:
        - *****

  =========
  Collector
  =========
    Last collection time: 2026-01-14 10:04:49
    Docker socket: /var/run/docker.sock
    Number of processes: 48
    Number of containers: 0
    Process Queue length: 0
    RTProcess Queue length: 0
    Connections Queue length: 0
    Event Queue length: 0
    Pod Queue length: 0
    Process Bytes enqueued: 0
    RTProcess Bytes enqueued: 0
    Connections Bytes enqueued: 0
    Event Bytes enqueued: 0
    Pod Bytes enqueued: 0
    Drop Check Payloads: []
    Number of submission errors: 0
```

### Process arguments scrubbing{% #process-arguments-scrubbing %}

In order to hide sensitive data on the Live Processes page, the Agent scrubs sensitive arguments from the process command line. This feature is enabled by default and any process argument that matches one of the following words has its value hidden.

```text
"password", "passwd", "mysql_pwd", "access_token", "auth_token", "api_key", "apikey", "secret", "credentials", "stripetoken"
```

**Note**: The matching is **case insensitive**.

{% tab title="Linux/Windows" %}
Define your own list to be merged with the default one, using the `custom_sensitive_words` field in `datadog.yaml` file under the `process_config` section. Use wildcards (`*`) to define your own matching scope. However, a single wildcard (`'*'`) is not supported as a sensitive word.

```yaml
process_config:
    scrub_args: true
    custom_sensitive_words: ['personal_key', '*token', 'sql*', '*pass*d*']
```

**Note**: Words in `custom_sensitive_words` must contain only alphanumeric characters, underscores, or wildcards (`'*'`). A wildcard-only sensitive word is not supported.

The next image shows one process on the Live Processes page whose arguments have been hidden by using the configuration above.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/process/process_arg_scrubbing.23684230fb047649634620cedb0a71b5.png?auto=format"
   alt="Process arguments scrubbing" /%}

Set `scrub_args` to `false` to completely disable the process arguments scrubbing.

You can also scrub **all** arguments from processes by enabling the `strip_proc_arguments` flag in your `datadog.yaml` configuration file:

```yaml
process_config:
    strip_proc_arguments: true
```

{% /tab %}

{% tab title="Helm" %}
You can use the Helm chart to define your own list, which is merged with the default one. Add the environment variables `DD_SCRUB_ARGS` and `DD_CUSTOM_SENSITIVE_WORDS` to your `datadog-values.yaml` file, and upgrade your Datadog Helm chart:

```yaml
datadog:
    # (...)
    processAgent:
        enabled: true
        processCollection: true
    agents:
        containers:
            processAgent:
                env:
                - name: DD_SCRUB_ARGS
                  value: "true"
                - name: DD_CUSTOM_SENSITIVE_WORDS
                  value: "personal_key,*token,*token,sql*,*pass*d*"
```

Use wildcards (`*`) to define your own matching scope. However, a single wildcard (`'*'`) is not supported as a sensitive word.

Set `DD_SCRUB_ARGS` to `false` to completely disable the process arguments scrubbing.

Alternatively, you can scrub **all** arguments from processes by enabling the `DD_STRIP_PROCESS_ARGS` variable in your `datadog-values.yaml` file:

```yaml
datadog:
    # (...)
    processAgent:
        enabled: true
        processCollection: true
agents:
    containers:
        processAgent:
            env:
            - name: DD_STRIP_PROCESS_ARGS
              value: "true"
```

{% /tab %}

## Queries{% #queries %}

### Scoping processes{% #scoping-processes %}

Processes are, by nature, extremely high cardinality objects. To refine your scope to view relevant processes, you can use text and tag filters.

#### Text filters{% #text-filters %}

When you input a text string into the search bar, fuzzy string search is used to query processes containing that text string in their command lines or paths. Enter a string of two or more characters to see results. Below is Datadog's demo environment, filtered with the string `postgres /9.`.

**Note**: `/9.` has matched in the command path, and `postgres` matches the command itself.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/process/postgres.324f2f01b9ea3b003a89124ac470f034.png?auto=format"
   alt="Postgres" /%}

To combine multiple string searches into a complex query, use any of the following Boolean operators:

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

Use parentheses to group operators together. For example, `(NOT (elasticsearch OR kafka) java) OR python` .

#### Tag filters{% #tag-filters %}

You can also filter your processes using Datadog [tags](https://docs.datadoghq.com/getting_started/tagging/), such as `host`, `pod`, `user`, and `service`. Input tag filters directly into the search bar, or select them in the facet panel on the left of the page.

Datadog automatically generates a `command` tag, so that you can filter for:

- Third-party software, for example: `command:mongod`, `command:nginx`
- Container management software, for example: `command:docker`, `command:kubelet`
- Common workloads, for example: `command:ssh`, `command:CRON`

#### Containerized environment tags{% #containerized-environment-tags %}

Furthermore, processes in ECS containers are also tagged by:

- `task_name`
- `task_version`
- `ecs_cluster`

Processes in Kubernetes containers are tagged by:

- `pod_name`
- `kube_service`
- `kube_namespace`
- `kube_replica_set`
- `kube_daemon_set`
- `kube_job`
- `kube_deployment`
- `kube_cluster_name`

If you have configuration for [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging) in place, `env`, `service`, and `version` are picked up automatically. Having these tags available lets you tie together APM, logs, metrics, and process data. **Note**: This setup applies to containerized environments only.

#### Rules to create custom tags{% #rules-to-create-custom-tags %}

{% alert level="info" %}
Requires the `Process Tags Read` and `Process Tag Write` Datadog role permissions
{% /alert %}

You can create rule definitions to add manual tags to processes based on the command line.

1. On the **Manage Process Tags** tab, select the *New Process Tag Rule* button
1. Select a process to use as a reference
1. Define the parsing and match criteria for your tag
1. If validation passes, create a new rule

After a rule is created, tags are available for all process command line values that match the rule criteria. These tags are available in search and can be used in the definition of [Live Process Monitors](https://docs.datadoghq.com/monitors/types/process/) and [Custom Metrics](https://docs.datadoghq.com/metrics/custom_metrics/).

## Scatter plot{% #scatter-plot %}

Use the scatter plot analytic to compare two metrics with one another in order to better understand the performance of your containers.

To access the scatter plot analytic [in the Processes page](https://app.datadoghq.com/process) click on the *Show Summary graph* button then select the "Scatter Plot" tab:

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/process/scatterplot_selection.6a9a9e6a3e83adbe6b41e960df0fa520.png?auto=format"
   alt="Scatter plot selection" /%}

By default, the graph groups by the `command` tag key. The size of each dot represents the number of processes in that group, and clicking on a dot displays the individual processes and containers that contribute to the group.

The options at the top of the graph allow you to control your scatter plot analytic:

- Selection of metrics to display.
- Selection of the aggregation method for both metrics.
- Selection of the scale of both X and Y axis (*Linear*/*Log*).

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/process/scatterplot.46008c187d3730209b6811f2f765bfec.png?auto=format"
   alt="Container inspect" /%}

## Process monitors{% #process-monitors %}

Use the [Live Process Monitor](https://docs.datadoghq.com/monitors/types/process/) to generate alerts based on the count of any group of processes across hosts or tags. You can configure process alerts in the [Monitors page](https://app.datadoghq.com/monitors/create/live_process). To learn more, see the [Live Process Monitor documentation](https://docs.datadoghq.com/monitors/types/process/).

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/process/process_monitor.51e6844de39a273455038ce834d69699.png?auto=format"
   alt="Process Monitor" /%}

## Processes in dashboards and notebooks{% #processes-in-dashboards-and-notebooks %}

You can graph process metrics in dashboards and notebooks using the [Timeseries widget](https://docs.datadoghq.com/dashboards/widgets/timeseries/#pagetitle). To configure:

1. Select Processes as a data source
1. Filter using text strings in the search bar
1. Select a process metric to graph
1. Filter using tags in the `From` field

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/process/process_widget.292c08170c78776167347475cdfbfb4f.png?auto=format"
   alt="Processes widget" /%}

## Monitoring third-party software{% #monitoring-third-party-software %}

### Autodetected integrations{% #autodetected-integrations %}

Datadog uses process collection to autodetect the technologies running on your hosts. This identifies Datadog integrations that can help you monitor these technologies. These auto-detected integrations are displayed in the [Integrations search](https://docs.datadoghq.com/agent/faq/agent-5-process-collection/):

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/integrations/ad_integrations.b7fa69bb8d5ab1ac723573d7a2bb1cb2.png?auto=format"
   alt="Autodetected integrations" /%}

Each integration has one of two status types:

- **+ Detected**: This integration is not enabled on any host(s) running it.
- **â Partial Visibility**: This integration is enabled on some, but not all relevant hosts are running it.

Hosts that are running the integration, but where the integration is not enabled, can be found in the **Hosts** tab of the integrations tile.

### Integration views{% #integration-views %}

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/process/integration_views.ba50d26ce32062d4483fda8d810b35ba.png?auto=format"
   alt="Integration Views" /%}

After a third-party software has been detected, Live Processes helps to analyze the performance of that software.

1. To start, click on *Views* at the top right of the page to open a list of pre-set options, including Nginx, Redis, and Kafka.
1. Select a view to scope the page to only the processes running that software.
1. When inspecting a heavy process, shift to the *Integration Metrics* tab to analyze the health of the software on the underlying host. If you have already enabled the relevant Datadog integration, you can view all performance metrics collected from the integration to distinguish between a host-level and software-level issue. For instance, seeing correlated spikes in process CPU and MySQL query latency may indicate that an intensive operation, such as a full table scan, is delaying the execution of other MySQL queries relying on the same underlying resources.

You can customize integration views (for example, when aggregating a query for Nginx processes by host) and other custom queries by clicking the *+Save* button at the top of the page. This saves your query, table column selections, and visualization settings. Create saved views for quick access to the processes you care about without addition configuration, and to share process data with your teammates.

## Processes across the platform{% #processes-across-the-platform %}

### Live Containers{% #live-containers %}

Live Processes adds extra visibility to your container deployments by monitoring the processes running on each of your containers. Click on a container in the [Live Containers](https://docs.datadoghq.com/infrastructure/livecontainers/) page to view its process tree, including the commands it is running and their resource consumption. Use this data alongside other container metrics to determine the root cause of failing containers or deployments.

### APM{% #apm %}

In [APM Traces](https://docs.datadoghq.com/tracing/), you can click on a service's span to see the processes running on its underlying infrastructure. A service's span processes are correlated with the hosts or pods on which the service runs at the time of the request. Analyze process metrics such as CPU and RSS memory alongside code-level errors to distinguish between application-specific and wider infrastructure issues. Clicking on a process brings you to the Live Processes page. Related processes are not supported for serverless and browser traces.

### Cloud Network Monitoring{% #cloud-network-monitoring %}

When you inspect a dependency in the [Network Analytics](https://docs.datadoghq.com/network_monitoring/cloud_network_monitoring/network_analytics) page, you can view processes running on the underlying infrastructure of the endpoints such as services communicating with one another. Use process metadata to determine whether poor network connectivity (indicated by a high number of TCP retransmits) or high network call latency (indicated by high TCP round-trip time) could be due to heavy workloads consuming those endpoints' resources, and thus, affecting the health and efficiency of their communication.

## Real-time monitoring{% #real-time-monitoring %}

Processes are normally collected at 10s resolution. While actively working with the Live Processes page, metrics are collected at 2s resolution and displayed in real time, which is important for volatile metrics such as CPU. However, for historical context, metrics are ingested at the default 10s resolution.

## Additional information{% #additional-information %}

- Real-time (2s) data collection is turned off after 30 minutes. To resume real-time collection, refresh the page.
- In container deployments, the `/etc/passwd` file mounted into the `docker-dd-agent` is necessary to collect usernames for each process. This is a public file and the Process Agent does not use any fields except the username. If the Agent is running unprivileged, the mount does not occur. Even without access to the `/etc/passwd` file, all features except the `user` metadata field still function. **Note**: Live Processes only uses the host `passwd` file and does not perform username resolution for users created within containers.

## Further Reading{% #further-reading %}

- [Monitor your processes with Datadog](https://www.datadoghq.com/blog/live-process-monitoring/)
- [Increase the retention of process data with metrics](https://docs.datadoghq.com/infrastructure/process/generate_process_metrics/)
- [Get real-time visibility of all of the containers across your environment](https://docs.datadoghq.com/infrastructure/livecontainers)
- [Correlate software performance and resource consumption with saved views](https://www.datadoghq.com/blog/monitor-third-party-software-with-live-processes/)
- [Troubleshoot faster with process-level app and network data](https://www.datadoghq.com/blog/process-level-data/)
- [Troubleshoot anomalies in workload performance with Watchdog Insights for Live Processes](https://www.datadoghq.com/blog/watchdog-live-processes/)
