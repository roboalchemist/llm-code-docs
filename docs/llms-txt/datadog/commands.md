# Source: https://docs.datadoghq.com/containers/cluster_agent/commands.md

---
title: Cluster Agent Commands and Options
description: >-
  Reference guide for Datadog Cluster Agent command-line interface and
  environment variables
breadcrumbs: >-
  Docs > Container Monitoring > Cluster Agent for Kubernetes > Cluster Agent
  Commands and Options
source_url: https://docs.datadoghq.com/cluster_agent/commands/index.html
---

# Cluster Agent Commands and Options

## Cluster Agent commands{% #cluster-agent-commands %}

The available commands for the Datadog Cluster Agents are:

{% dl %}

{% dt %}
`datadog-cluster-agent status`
{% /dt %}

{% dd %}
Gives an overview of the components of the Agent and their health.
{% /dd %}

{% dt %}
`datadog-cluster-agent metamap <NODE_NAME>`
{% /dt %}

{% dd %}
Queries the local cache of the mapping between the pods living on `NODE_NAME`, and the cluster level metadata they are associated with, such as endpoints. Not specifying the `NODE_NAME` runs the mapper on all the nodes of the cluster.
{% /dd %}

{% dt %}
`datadog-cluster-agent flare <CASE_ID>`
{% /dt %}

{% dd %}
Similarly to the node-based Agent, the Cluster Agent can aggregate the logs and the configurations used and forward an archive to the support team, or be deflated and used locally. **Note**: this command runs from within the Cluster Agent pod.
{% /dd %}

{% /dl %}

## Cluster Agent environment variables{% #cluster-agent-environment-variables %}

{% tab title="Datadog Operator" %}
Set Cluster Agent environment variables under `override.clusterAgent.env`:

In the `datadog-agent.yaml` file:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  override:
    clusterAgent:
      env:
        - name: <ENV_VAR_NAME>
          value: <ENV_VAR_VALUE>
```

{% /tab %}

{% tab title="Helm" %}
Set Cluster Agent environment variables under `clusterAgent.env`:

In the `datadog-values.yaml` file:

```yaml
clusterAgent:
  env:
    - name: <ENV_VAR_NAME>
      value: <ENV_VAR_VALUE>
```

{% /tab %}

The following environment variables are supported:

{% dl %}

{% dt %}
`DD_API_KEY`
{% /dt %}

{% dd %}
Your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).
{% /dd %}

{% dt %}
`DD_CLUSTER_CHECKS_ENABLED`
{% /dt %}

{% dd %}
Enable Cluster Check Autodiscovery. Defaults to `false`.
{% /dd %}

{% dt %}
`DD_CLUSTER_AGENT_AUTH_TOKEN`
{% /dt %}

{% dd %}
32-character token that needs to be shared between the node Agent and the Datadog Cluster Agent.
{% /dd %}

{% dt %}
`DD_CLUSTER_AGENT_KUBERNETES_SERVICE_NAME`
{% /dt %}

{% dd %}
Name of the Kubernetes service through which Cluster Agents are exposed. Defaults to `datadog-cluster-agent`.
{% /dd %}

{% dt %}
`DD_CLUSTER_NAME`
{% /dt %}

{% dd %}
Cluster name. Added as an instance tag to all cluster check configurations.
{% /dd %}

{% dt %}
`DD_CLUSTER_CHECKS_ENABLED`
{% /dt %}

{% dd %}
When true, enables dispatching logic on the leader Cluster Agent. Default: `false`.
{% /dd %}

{% dt %}
`DD_CLUSTER_CHECKS_NODE_EXPIRATION_TIMEOUT`
{% /dt %}

{% dd %}
Time (in seconds) after which node-based Agents are considered down and removed from the pool. Defaults to `30` seconds.
{% /dd %}

{% dt %}
`DD_CLUSTER_CHECKS_WARMUP_DURATION`
{% /dt %}

{% dd %}
Delay (in seconds) between acquiring leadership and starting the Cluster Checks logic, allowing for all node-based Agents to register first. Default is `30` seconds.
{% /dd %}

{% dt %}
`DD_CLUSTER_CHECKS_CLUSTER_TAG_NAME`
{% /dt %}

{% dd %}
Name of the instance tag set with the `DD_CLUSTER_NAME` option. Defaults to `cluster_name`.
{% /dd %}

{% dt %}
`DD_CLUSTER_CHECKS_EXTRA_TAGS`
{% /dt %}

{% dd %}
Adds extra tags to cluster check metrics.
{% /dd %}

{% dt %}
`DD_CLUSTER_CHECKS_ADVANCED_DISPATCHING_ENABLED`
{% /dt %}

{% dd %}
When true, the leader Cluster Agent collects stats from the cluster-level check runners to optimize check dispatching logic. Default: `false`.
{% /dd %}

{% dt %}
`DD_CLUSTER_CHECKS_CLC_RUNNERS_PORT`
{% /dt %}

{% dd %}
The port used by the Cluster Agent client to reach cluster-level check runners and collect their stats. Default: `5005`.
{% /dd %}

{% dt %}
`DD_HOSTNAME`
{% /dt %}

{% dd %}
Hostname to use for the Datadog Cluster Agent.
{% /dd %}

{% dt %}
`DD_ENV`
{% /dt %}

{% dd %}
Sets the `env` tag for data emitted by the Cluster Agent. Recommended only if the Cluster Agent monitors services within a single environment.
{% /dd %}

{% dt %}
`DD_USE_METADATA_MAPPER`
{% /dt %}

{% dd %}
Enables cluster level metadata mapping. Defaults to `true`.
{% /dd %}

{% dt %}
`DD_COLLECT_KUBERNETES_EVENTS`
{% /dt %}

{% dd %}
Configures the Agent to collect Kubernetes events. Defaults to `false`.
{% /dd %}

{% dt %}
`DD_LEADER_ELECTION`
{% /dt %}

{% dd %}
Activates leader election. Set `DD_COLLECT_KUBERNETES_EVENTS` to `true` to activate this feature. Defaults to `false`.
{% /dd %}

{% dt %}
`DD_LEADER_LEASE_DURATION`
{% /dt %}

{% dd %}
Used only if leader election is activated. Value in seconds, 60 by default.
{% /dd %}

{% dt %}
`DD_KUBE_RESOURCES_NAMESPACE`
{% /dt %}

{% dd %}
Configures the namespace where the Cluster Agent creates the configmaps required for the leader election, event collection (optional), and horizontal pod autoscaling.
{% /dd %}

{% dt %}
`DD_KUBERNETES_INFORMERS_RESYNC_PERIOD`
{% /dt %}

{% dd %}
Frequency (in seconds) for querying the API server to resync the local cache. The default is 5 minutes, or `300` seconds.
{% /dd %}

{% dt %}
`DD_KUBERNETES_INFORMERS_RESTCLIENT_TIMEOUT`
{% /dt %}

{% dd %}
Timeout (in seconds) of the client communicating with the API server. Defaults to `60` seconds.
{% /dd %}

{% dt %}
`DD_METRICS_PORT`
{% /dt %}

{% dd %}
Port to expose Datadog Cluster Agent metrics. Defaults to port `5000`.
{% /dd %}

{% dt %}
`DD_EXTERNAL_METRICS_PROVIDER_BATCH_WINDOW`
{% /dt %}

{% dd %}
Time waited (in seconds) to process a batch of metrics from multiple autoscalers. Defaults to `10` seconds.
{% /dd %}

{% dt %}
`DD_EXTERNAL_METRICS_PROVIDER_MAX_AGE`
{% /dt %}

{% dd %}
Maximum age (in seconds) of a datapoint before considering it invalid to be served. Default to `120` seconds.
{% /dd %}

{% dt %}
`DD_EXTERNAL_METRICS_AGGREGATOR`
{% /dt %}

{% dd %}
Aggregator for Datadog metrics. Applies to all autoscalers processed. Choose from `sum`/`avg`/`max`/`min`.
{% /dd %}

{% dt %}
`DD_EXTERNAL_METRICS_PROVIDER_BUCKET_SIZE`
{% /dt %}

{% dd %}
Size of the window (in seconds) used to query metrics from Datadog. Defaults to `300` seconds.
{% /dd %}

{% dt %}
`DD_EXTERNAL_METRICS_LOCAL_COPY_REFRESH_RATE`
{% /dt %}

{% dd %}
Rate to resync local cache of processed metrics with the global store. Useful when there are several replicas of the Cluster Agent.
{% /dd %}

{% dt %}
`DD_EXTRA_CONFIG_PROVIDERS`
{% /dt %}

{% dd %}
Additional Autodiscovery configuration providers to use.
{% /dd %}

{% dt %}
`DD_EXTRA_LISTENERS`
{% /dt %}

{% dd %}
Additional Autodiscovery listeners to run.
{% /dd %}

{% dt %}
`DD_PROXY_HTTPS`
{% /dt %}

{% dd %}
Sets a proxy server for HTTPS requests.
{% /dd %}

{% dt %}
`DD_PROXY_HTTP`
{% /dt %}

{% dd %}
Sets a proxy server for HTTP requests.
{% /dd %}

{% dt %}
`DD_PROXY_NO_PROXY`
{% /dt %}

{% dd %}
Sets a list of hosts that should bypass the proxy. The list is space-separated.
{% /dd %}

{% dt %}
`DD_ADMISSION_CONTROLLER_AUTO_INSTRUMENTATION_INIT_RESOURCES_CPU`
{% /dt %}

{% dd %}
Configures the CPU request and limit for the init containers.
{% /dd %}

{% dt %}
`DD_ADMISSION_CONTROLLER_AUTO_INSTRUMENTATION_INIT_RESOURCES_MEMORY`
{% /dt %}

{% dd %}
Configures the memory request and limit for the init containers.
{% /dd %}

{% /dl %}

## Further Reading{% #further-reading %}

- [Introducing the Datadog Cluster Agent](https://www.datadoghq.com/blog/datadog-cluster-agent/)
- [Autoscale your Kubernetes workloads with any Datadog metric](https://www.datadoghq.com/blog/autoscale-kubernetes-datadog/)
- [Running Cluster Checks with Autodiscovery](https://docs.datadoghq.com/agent/cluster_agent/clusterchecks/)
- [Kubernetes DaemonSet Setup](https://docs.datadoghq.com/agent/kubernetes/daemonset_setup/)
- [Troubleshooting the Datadog Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent/troubleshooting/)
