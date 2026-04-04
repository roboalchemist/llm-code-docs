# Source: https://docs.datadoghq.com/containers/guide/kubernetes_daemonset.md

---
title: Manually install and configure the Datadog Agent on Kubernetes with DaemonSet
description: >-
  Manual installation and configuration of the Datadog Agent on Kubernetes using
  DaemonSet deployment
breadcrumbs: >-
  Docs > Containers > Containers Guides > Manually install and configure the
  Datadog Agent on Kubernetes with DaemonSet
---

# Manually install and configure the Datadog Agent on Kubernetes with DaemonSet

{% alert level="danger" %}
Datadog discourages using DaemonSets to deploy the Datadog Agent because the manual process is prone to errors. Datadog recommends that you [use Datadog Operator or Helm](https://docs.datadoghq.com/containers/kubernetes/installation) to install the Agent on Kubernetes.
{% /alert %}

## Installation{% #installation %}

You can use DaemonSets to deploy the Datadog Agent on all your nodes (or on specific nodes by [using nodeSelectors](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector)).

To install the Datadog Agent on your Kubernetes cluster:

1. **Configure Agent permissions**: If your Kubernetes has role-based access control (RBAC) enabled, configure RBAC permissions for your Datadog Agent service account. From Kubernetes 1.6 onwards, RBAC is enabled by default. Create the appropriate ClusterRole, ServiceAccount, and ClusterRoleBinding with the following command:

   ```shell
   kubectl apply -f "https://raw.githubusercontent.com/DataDog/datadog-agent/master/Dockerfiles/manifests/rbac/clusterrole.yaml"

   kubectl apply -f "https://raw.githubusercontent.com/DataDog/datadog-agent/master/Dockerfiles/manifests/rbac/serviceaccount.yaml"

   kubectl apply -f "https://raw.githubusercontent.com/DataDog/datadog-agent/master/Dockerfiles/manifests/rbac/clusterrolebinding.yaml"
   ```

**Note**: Those RBAC configurations are set for the `default` namespace. If you are in a custom namespace, update the `namespace` parameter before applying them.

1. **Create the Datadog Agent manifest**. Create the `datadog-agent.yaml` manifest out of one of the following templates:

| Metrics | Logs                                                                                      | APM                                                                                               | Process                                                                                        | NPM                                                                                                | Security | Linux                                                                                          | Windows                                                                                                              |
| ------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| yes     | yes                                                                                       | yes                                                                                               | yes                                                                                            | yes                                                                                                | yes      | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-all-features.yaml) | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-windows-all-features.yaml) (no security) |
| yes     | yes                                                                                       | yes                                                                                               | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-logs-apm.yaml)     | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-windows-logs-apm.yaml) |
| yes     | yes                                                                                       | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-logs.yaml)            | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-windows-logs.yaml) |
| yes     | yes                                                                                       | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-apm.yaml)             | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-windows-apm.yaml)  |
| yes     | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-npm.yaml)     | no template                                                                                       |
| yes     | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-vanilla.yaml) | [Manifest template](https://docs.datadoghq.com/resources/yaml/datadog-agent-windows-vanilla.yaml) |

To enable trace collection completely, [extra steps are required on your application Pod configuration](https://docs.datadoghq.com/agent/kubernetes/apm/#setup). Refer also to the [logs](https://docs.datadoghq.com/agent/kubernetes/log/), [APM](https://docs.datadoghq.com/agent/kubernetes/apm/), [processes](https://docs.datadoghq.com/infrastructure/process/?tab=kubernetes#installation), and [Cloud Network Monitoring](https://docs.datadoghq.com/network_monitoring/cloud_network_monitoring/setup/), and [Security](https://docs.datadoghq.com/data_security/agent/) documentation pages to learn how to enable each feature individually.

**Note**: Those manifests are set for the `default` namespace. If you are in a custom namespace, update the `metadata.namespace` parameter before applying them.

1. In the `secret-api-key.yaml` manifest, replace `PUT_YOUR_BASE64_ENCODED_API_KEY_HERE` with [your Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) encoded in base64. To get the base64 version of your API key, you can run:

   ```shell
   echo -n '<Your API key>' | base64
   ```

1. If you are using the `datadog-agent-all-features.yaml` manifest template: in the `secret-cluster-agent-token.yaml` manifest, replace `PUT_A_BASE64_ENCODED_RANDOM_STRING_HERE` with a random string encoded in base64. To get the base64 version of it, you can run:

   ```shell
   echo -n 'Random string' | base64
   ```

**Note**: The random string must contain at least 32 alphanumeric characters to secure Cluster Agent to Agent communication.

1. **Set your Datadog site** to  using the `DD_SITE` environment variable in the `datadog-agent.yaml` manifest.

**Note**: If the `DD_SITE` environment variable is not explicitly set, it defaults to the `US` site `datadoghq.com`. If you are using one of the other sites, this results in an invalid API key message. Use the [documentation site selector](https://docs.datadoghq.com/getting_started/site/) to see documentation appropriate for the site you're using.

1. **Deploy the DaemonSet** with the command:

   ```shell
   kubectl apply -f datadog-agent.yaml
   ```

1. **Verification**: To verify the Datadog Agent is running in your environment as a DaemonSet, execute:

   ```shell
   kubectl get daemonset
   ```

If the Agent is deployed, output similar to the text below appears, where `DESIRED` and `CURRENT` are equal to the number of nodes running in your cluster.

   ```shell
   NAME      DESIRED   CURRENT   READY     UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
   datadog   2         2         2         2            2           <none>          10s
   ```

## Configuration{% #configuration %}

### Trace collection{% #trace-collection %}

{% tab title="TCP" %}
To enable APM trace collection over TCP, open the DaemonSet configuration file and edit the following:

- Allow incoming data from port `8126` (forwarding traffic from the host to the agent) within the `trace-agent` container:

  ```yaml
    # (...)
    containers:
      - name: trace-agent
        # (...)
        ports:
          - containerPort: 8126
            hostPort: 8126
            name: traceport
            protocol: TCP
    # (...)
  ```

- **If using Agent version 7.17 or previous**, in addition to the steps above, set the `DD_APM_NON_LOCAL_TRAFFIC` and `DD_APM_ENABLED` variables to `true` in your `env` section of the `datadog.yaml` trace Agent manifest:

  ```yaml
    # (...)
    containers:
      - name: trace-agent
        # (...)
        env:
          - name: DD_APM_ENABLED
            value: 'true'
          - name: DD_APM_NON_LOCAL_TRAFFIC
            value: "true"
          # (...)
  ```

**Warning**: The `hostPort` parameter opens a port on your host. Make sure your firewall only allows access from your applications or trusted sources. If your network plugin doesn't support `hostPorts`, add `hostNetwork: true` in your Agent pod specifications. This shares the network namespace of your host with the Datadog Agent. This also means that all ports opened on the container are opened on the host. If a port is used both on the host and in your container, they conflict (since they share the same network namespace) and the pod does not start. Some Kubernetes installations do not allow this.
{% /tab %}

{% tab title="Unix Domain Socket (UDS)" %}
To enable APM trace collection over UDS, open the DaemonSet configuration file and edit the following:

```yaml
  # (...)
  containers:
  - name: trace-agent
    # (...)
    env:
    - name: DD_APM_ENABLED
      value: "true"
    - name: DD_APM_RECEIVER_SOCKET
      value: "/var/run/datadog/apm.socket"
  # (...)
    volumeMounts:
    - name: apmsocket
      mountPath: /var/run/datadog/
  volumes:
  - hostPath:
      path: /var/run/datadog/
      type: DirectoryOrCreate
  # (...)
```

This configuration creates a directory on the host and mounts it within the Agent. The Agent then creates and listens on a socket file in that directory with the `DD_APM_RECEIVER_SOCKET` value of `/var/run/datadog/apm.socket`. The application pods can then similarly mount this volume and write to this same socket.
{% /tab %}

### Log collection{% #log-collection %}

**Note**: This option is not supported on Windows. Use the [Helm](https://docs.datadoghq.com/containers/kubernetes/log) option instead.

To enable log collection with your DaemonSet:

1. Set the `DD_LOGS_ENABLED` and `DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL` variable to true in the *env* section of the `datadog.yaml` Agent manifest:

   ```yaml
    # (...)
     env:
       # (...)
       - name: DD_LOGS_ENABLED
         value: "true"
       - name: DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL
         value: "true"
       - name: DD_CONTAINER_EXCLUDE_LOGS
         value: "name:datadog-agent"
    # (...)
   ```

**Note**: Setting `DD_CONTAINER_EXCLUDE_LOGS` prevents the Datadog Agent from collecting and sending its own logs. Remove this parameter if you want to collect the Datadog Agent logs. See the [environment variable for ignoring containers](https://docs.datadoghq.com/agent/docker/?tab=standard#ignore-containers) to learn more. When using ImageStreams inside OpenShift environments, set `DD_CONTAINER_INCLUDE_LOGS` with the container `name` to collect logs. Both of these Exclude/Include parameter value supports regular expressions.

1. Mount the `pointerdir` volume to prevent loss of container logs during restarts or network issues and `/var/lib/docker/containers` to collect logs through kubernetes log file as well, since `/var/log/pods` is symlink to this directory:

   ```yaml
     # (...)
       volumeMounts:
         # (...)
         - name: pointerdir
           mountPath: /opt/datadog-agent/run
         - name: logpodpath
          mountPath: /var/log/pods
         # Docker runtime directory, replace this path
         # with your container runtime logs directory,
         # or remove this configuration if `/var/log/pods`
         # is not a symlink to any other directory.
         - name: logcontainerpath
          mountPath: /var/lib/docker/containers
     # (...)
     volumes:
       # (...)
       - hostPath:
           path: /opt/datadog-agent/run
         name: pointerdir
       - hostPath:
           path: /var/log/pods
         name: logpodpath
       # Docker runtime directory, replace this path
       # with your container runtime logs directory,
       # or remove this configuration if `/var/log/pods`
       # is not a symlink to any other directory.
       - hostPath:
           path: /var/lib/docker/containers
         name: logcontainerpath
       # (...)
   ```

The `pointerdir` is used to store a file with a pointer to all the containers that the Agent is collecting logs from. This is to make sure none are lost when the Agent is restarted, or in the case of a network issue.

### Unprivileged{% #unprivileged %}

(Optional) To run an unprivileged installation, add the following to your [pod template](https://docs.datadoghq.com/resources/yaml/datadog-agent-all-features.yaml):

```yaml
  spec:
    securityContext:
      runAsUser: <USER_ID>
      supplementalGroups:
        - <DOCKER_GROUP_ID>
```

where `<USER_ID>` is the UID to run the agent and `<DOCKER_GROUP_ID>` is the group ID owning the docker or containerd socket.

When the agent is running with a non-root user, it cannot directly read the log files contained in `/var/lib/docker/containers`. In this case, it is necessary to mount the docker socket in the agent container so that it can fetch the container logs from the docker daemon.

### Cluster Agent event collection{% #cluster-agent-event-collection %}

If you want Kubernetes events to be collected by the Datadog Cluster Agent, use the following steps:

1. Disable leader election in your Node Agent by setting the `leader_election` variable or `DD_LEADER_ELECTION` environment variable to `false`.

1. In your Cluster Agent deployment file, set the `DD_COLLECT_KUBERNETES_EVENTS` and `DD_LEADER_ELECTION` environment variable to `true`:

   ```yaml
     - name: DD_COLLECT_KUBERNETES_EVENTS
       value: "true"
     - name: DD_LEADER_ELECTION
       value: "true"
   ```

Configuring leader election, as described in the above steps, ensures that only one Cluster Agent collects the events.

Alternatively, to collect the Kubernetes events from a Node Agent, set the environment variables `DD_COLLECT_KUBERNETES_EVENTS` and `DD_LEADER_ELECTION` to `true` in your Agent manifest.

```yaml
- name: DD_COLLECT_KUBERNETES_EVENTS
  value: "true"
- name: DD_LEADER_ELECTION
  value: "true"
```

## Environment variables{% #environment-variables %}

The following is the list of environment variables available for the Datadog Agent using a DaemonSet.

### Global options{% #global-options %}

| Env Variable           | Description                                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DD_API_KEY`           | Your Datadog API key (**required**)                                                                                                                                                                                                                                                                                                              |
| `DD_ENV`               | Sets the global `env` tag for all data emitted.                                                                                                                                                                                                                                                                                                  |
| `DD_HOSTNAME`          | Hostname to use for metrics (if autodetection fails)                                                                                                                                                                                                                                                                                             |
| `DD_TAGS`              | Host tags separated by spaces. For example: `simple-tag-0 tag-key-1:tag-value-1`                                                                                                                                                                                                                                                                 |
| `DD_SITE`              | Destination site for your metrics, traces, and logs. Your `DD_SITE` is . Defaults to `datadoghq.com`.                                                                                                                                                                                                                                            |
| `DD_DD_URL`            | Optional setting to override the URL for metric submission.                                                                                                                                                                                                                                                                                      |
| `DD_URL` (6.36+/7.36+) | Alias for `DD_DD_URL`. Ignored if `DD_DD_URL` is already set.                                                                                                                                                                                                                                                                                    |
| `DD_CHECK_RUNNERS`     | The Agent runs all checks concurrently by default (default value = `4` runners). To run the checks sequentially, set the value to `1`. If you need to run a high number of checks (or slow checks) the `collector-queue` component might fall behind and fail the healthcheck. You can increase the number of runners to run checks in parallel. |
| `DD_LEADER_ELECTION`   | If multiple instances of the Agent are running in your cluster, set this variable to `true` to avoid the duplication of event collection.                                                                                                                                                                                                        |

### Proxy settings{% #proxy-settings %}

Starting with Agent v6.4.0 (and v6.5.0 for the Trace Agent), you can override the Agent proxy settings with the following environment variables:

| Env Variable             | Description                                                            |
| ------------------------ | ---------------------------------------------------------------------- |
| `DD_PROXY_HTTP`          | An HTTP URL to use as a proxy for `http` requests.                     |
| `DD_PROXY_HTTPS`         | An HTTPS URL to use as a proxy for `https` requests.                   |
| `DD_PROXY_NO_PROXY`      | A space-separated list of URLs for which no proxy should be used.      |
| `DD_SKIP_SSL_VALIDATION` | An option to test if the Agent is having issues connecting to Datadog. |

For more information about proxy settings, see the [Agent v6 Proxy documentation](https://docs.datadoghq.com/agent/configuration/proxy/#agent-v6).

### DogStatsD (custom metrics){% #dogstatsd-custom-metrics %}

Send custom metrics with [the StatsD protocol](https://docs.datadoghq.com/developers/dogstatsd/):

| Env Variable                     | Description                                                                                                                                           |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DD_DOGSTATSD_NON_LOCAL_TRAFFIC` | Listen to DogStatsD packets from other containers (required to send custom metrics).                                                                  |
| `DD_HISTOGRAM_PERCENTILES`       | The histogram percentiles to compute (separated by spaces). The default is `0.95`.                                                                    |
| `DD_HISTOGRAM_AGGREGATES`        | The histogram aggregates to compute (separated by spaces). The default is `"max median avg count"`.                                                   |
| `DD_DOGSTATSD_SOCKET`            | Path to the Unix socket to listen to. Must be in a `rw` mounted volume.                                                                               |
| `DD_DOGSTATSD_ORIGIN_DETECTION`  | Enable container detection and tagging for Unix socket metrics.                                                                                       |
| `DD_DOGSTATSD_TAGS`              | Additional tags to append to all metrics, events, and service checks received by this DogStatsD server, for example: `"env:golden group:retrievers"`. |

Learn more about [DogStatsD over Unix Domain Sockets](https://docs.datadoghq.com/developers/dogstatsd/unix_socket/).

### Tagging{% #tagging %}

Datadog automatically collects common tags from Kubernetes. To extract even more tags, use the following options:

| Env Variable                            | Description             |
| --------------------------------------- | ----------------------- |
| `DD_KUBERNETES_POD_LABELS_AS_TAGS`      | Extract pod labels      |
| `DD_KUBERNETES_POD_ANNOTATIONS_AS_TAGS` | Extract pod annotations |

See the [Kubernetes Tag Extraction](https://docs.datadoghq.com/containers/kubernetes/tag/) documentation to learn more.

### Ignore containers{% #ignore-containers %}

Exclude containers from logs collection, metrics collection, and Autodiscovery. Datadog excludes Kubernetes and OpenShift `pause` containers by default. These allowlists and blocklists apply to Autodiscovery only; traces and DogStatsD are not affected. These environment variables support regular expressions in their values.

| Env Variable                   | Description                                                                                                                                                                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DD_CONTAINER_INCLUDE`         | Allowlist of containers to include (separated by spaces). Use `.*` to include all. For example: `"image:image_name_1 image:image_name_2"`, `image:.*`                                                                              |
| `DD_CONTAINER_EXCLUDE`         | Blocklist of containers to exclude (separated by spaces). Use `.*` to exclude all. For example: `"image:image_name_3 image:image_name_4"`, `image:.*`                                                                              |
| `DD_CONTAINER_INCLUDE_METRICS` | Allowlist of containers whose metrics you wish to include.                                                                                                                                                                         |
| `DD_CONTAINER_EXCLUDE_METRICS` | Blocklist of containers whose metrics you wish to exclude.                                                                                                                                                                         |
| `DD_CONTAINER_INCLUDE_LOGS`    | Allowlist of containers whose logs you wish to include.                                                                                                                                                                            |
| `DD_CONTAINER_EXCLUDE_LOGS`    | Blocklist of containers whose logs you wish to exclude.                                                                                                                                                                            |
| `DD_AC_INCLUDE`                | **Deprecated**. Allowlist of containers to include (separated by spaces). Use `.*` to include all. For example: `"image:image_name_1 image:image_name_2"`, `image:.*`                                                              |
| `DD_AC_EXCLUDE`                | **Deprecated**. Blocklist of containers to exclude (separated by spaces). Use `.*` to exclude all. For example: `"image:image_name_3 image:image_name_4"` (**Note**: This variable is only honored for Autodiscovery.), `image:.*` |

Additional examples are available on the [Container Discover Management](https://docs.datadoghq.com/agent/guide/autodiscovery-management/) page.

**Note**: The `kubernetes.containers.running`, `kubernetes.pods.running`, `docker.containers.running`, `.stopped`, `.running.total` and `.stopped.total` metrics are not affected by these settings. All containers are counted.

### Autodiscovery{% #autodiscovery %}

| Env Variable                | Description                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DD_LISTENERS`              | Autodiscovery listeners to run.                                                                                                                                                                                                                                                                                                                                           |
| `DD_EXTRA_LISTENERS`        | Additional Autodiscovery listeners to run. They are added in addition to the variables defined in the `listeners` section of the `datadog.yaml` configuration file.                                                                                                                                                                                                       |
| `DD_CONFIG_PROVIDERS`       | The providers the Agent should call to collect checks configurations. Available providers are:`kubelet` - Handles templates embedded in pod annotations.`docker` - Handles templates embedded in container labels.`clusterchecks` - Retrieves cluster-level check configurations from the Cluster Agent.`kube_services` - Watches Kubernetes services for cluster checks. |
| `DD_EXTRA_CONFIG_PROVIDERS` | Additional Autodiscovery configuration providers to use. They are added in addition to the variables defined in the `config_providers` section of the `datadog.yaml` configuration file.                                                                                                                                                                                  |

### Misc{% #misc %}

| Env Variable                        | Description                                                                                                                                                                                                                                                         |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DD_PROCESS_AGENT_CONTAINER_SOURCE` | Overrides container source auto-detection to force a single source. Example: `"docker"`, `"ecs_fargate"`, `"kubelet"`. This is no longer needed since Agent v7.35.0.                                                                                                |
| `DD_HEALTH_PORT`                    | Set this to `5555` to expose the Agent health check at port `5555`.                                                                                                                                                                                                 |
| `DD_CLUSTER_NAME`                   | Set a custom Kubernetes cluster identifier to avoid host alias collisions. The cluster name can be up to 40 characters with the following restrictions: Lowercase letters, numbers, and hyphens only. Must start with a letter. Must end with a number or a letter. |
