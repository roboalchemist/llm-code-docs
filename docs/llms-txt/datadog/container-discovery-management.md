# Source: https://docs.datadoghq.com/containers/guide/container-discovery-management.md

---
title: Container Discovery Management
description: >-
  Control which containers the Datadog Agent monitors by configuring discovery
  rules and inclusion/exclusion patterns
breadcrumbs: >-
  Docs > Container Monitoring > Containers Guides > Container Discovery
  Management
source_url: https://docs.datadoghq.com/guide/container-discovery-management/index.html
---

# Container Discovery Management

By default, the Datadog Agent automatically discovers all containers available. This document describes how to restrict the Datadog Agent's discovery perimeter and limit data collection to a subset of containers.

## Container discovery patterns{% #container-discovery-patterns %}

In a containerized environment, you should deploy the Datadog Agent once per host. Each Datadog Agent deployed automatically discovers and monitors all containers on its respective host. When the logs [`containerCollectAll` option](https://docs.datadoghq.com/containers/kubernetes/log/?tab=helm#log-collection) is enabled, the Agent collects logs from all discovered containers.

You can adjust the discovery rules for the Agent to restrict metric and log collection. Any containers restricted from metric collection are also restricted for any [Autodiscovery](https://docs.datadoghq.com/getting_started/containers/autodiscovery)-based Agent integrations.

You can set exceptions in two ways:

- Provide environment variables to the Datadog Agent container as an allowlist/blocklist of containers. Recommended if you have a list of container names, images, or namespaces to exclude for the entire cluster.
- Add annotations to your Kubernetes pods to block individual pods or containers. Recommended if you need fine-tuned exclusions.

**Note**: The `kubernetes.containers.running`, `kubernetes.pods.running`, `docker.containers.running`, `.stopped`, `.running.total`, and `.stopped.total` metrics are not affected by these settings and always count all containers.

## Simple pattern matching{% #simple-pattern-matching %}

Use the environment variables in the table below to configure container filtering. Each inclusion or exclusion is defined as a list of space-separated regex strings. You can include or exclude containers based on their:

- container name (`name`)
- container image name (`image`)
- Kubernetes namespace (`kube_namespace`)

{% alert level="danger" %}
The `name` parameter only applies to container names, not pod names, even if the container runs in a Kubernetes pod.
{% /alert %}

### Environment variables{% #environment-variables %}

In **Agent v7.20+**, use the following environment variables to exclude containers by image name, container name, or Kubernetes namespace. Logs and metrics are not collected from excluded containers.

| Environment variable           | Description                                         |
| ------------------------------ | --------------------------------------------------- |
| `DD_CONTAINER_EXCLUDE`         | Blocklist of containers to exclude.                 |
| `DD_CONTAINER_EXCLUDE_METRICS` | Blocklist of containers whose metrics are excluded. |
| `DD_CONTAINER_EXCLUDE_LOGS`    | Blocklist of containers whose logs are excluded.    |
| `DD_CONTAINER_INCLUDE`         | Allowlist of containers to include.                 |
| `DD_CONTAINER_INCLUDE_METRICS` | Allowlist of containers whose metrics are included. |
| `DD_CONTAINER_INCLUDE_LOGS`    | Allowlist of containers whose logs are included.    |

{% collapsible-section #setting-environment-variables %}
#### Setting environment variables

{% tab title="Datadog Operator" %}
In the Datadog Operator, set these environment variables under `spec.override.nodeAgent.env`.

##### Example{% #example %}

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
        value: "image:<IMAGE_NAME>"
```

{% /tab %}

{% tab title="Helm" %}
In your Helm chart, supply a space-separated string to one or more of the following:

- `datadog.containerExclude`
- `datadog.containerInclude`
- `datadog.containerExcludeLogs`
- `datadog.containerIncludeLogs`
- `datadog.containerExcludeMetrics`
- `datadog.containerIncludeMetrics`

##### Example{% #example %}

```yaml
datadog:
  containerExclude: "image:<IMAGE_NAME_1> image:<IMAGE_NAME_2>"
  containerInclude: "image:<IMAGE_NAME_3> image:<IMAGE_NAME_4>"
```

{% /tab %}

{% tab title="Containerized Agent" %}
In environments where you are not using the Datadog Operator or Helm, the following environment variables can be passed to the Agent container at startup.

##### Example Docker{% #example-docker %}

```shell
docker run -e DD_CONTAINER_EXCLUDE=image:<IMAGE_NAME> ...
```

##### Example ECS{% #example-ecs %}

```json
"environment": [
  {
    "name": "DD_CONTAINER_EXCLUDE",
    "value": "image:<IMAGE_NAME>"
  },
  ...
]
```

{% /tab %}

{% /collapsible-section %}

{% alert level="info" %}
Image name filters (`image`) are matched across full image name, including the registry and the image tag or digest (for example, `dockerhub.io/nginx:1.13.1`).
{% /alert %}

#### Examples{% #examples %}

To exclude the container with the name `dd-agent`:

```
DD_CONTAINER_EXCLUDE = "name:^dd-agent$"
```

To exclude containers using the `dockercloud/network-daemon` image, including all tags and digests:

```
DD_CONTAINER_EXCLUDE = "image:^dockercloud/network-daemon(@sha256)?:.*
```

To exclude containers using the image `dockercloud/network-daemon:1.13.0`:

```
DD_CONTAINER_EXCLUDE = "image:^dockercloud/network-daemon:1.13.0$"
```

To exclude any container whose image contains the word `agent`:

```
DD_CONTAINER_EXCLUDE = "image:agent"
```

To exclude any container using the image `foo` regardless of the registry:

```
DD_CONTAINER_EXCLUDE = "image:^.*/foo(@sha256)?:.*"
```

To exclude every container:

```
DD_CONTAINER_EXCLUDE = "name:.*"
```

Alternatively, you can also use `image:.*` or `kube_namespace:.*`. Configuring `.*` without a `name:`, `image:`, or `kube_namespace:` prefix does not work.

### Inclusion and exclusion behavior{% #inclusion-and-exclusion-behavior %}

Generally, inclusion takes precedence over exclusion. For example, to only monitor `ubuntu` or `debian` images, first exclude all other images and then specify which images to include:

```
DD_CONTAINER_EXCLUDE = "image:.*"
DD_CONTAINER_INCLUDE = "image:^docker.io/library/ubuntu(@sha256)?:.* image:^docker.io/library/debian(@sha256)?:.*"
```

The only exception to this rule is pod exclusion annotations like `ad.datadoghq.com/exclude`. When an application has an exclusion annotation set to `true`, this takes precedence, and the container is excluded from being autodiscovered for monitoring. For example, having a condition that includes every container like `DD_CONTAINER_INCLUDE = "image:.*"` does not guarantee a container is included if it has an exclusion annotation set on it. See Container Discovery Management - Pod exclude configuration for more information.

You cannot mix cross-category inclusion/exclusion rules. For instance, if you want to include a container with the image name `foo` and exclude only metrics from a container with the image name `bar`, the following is **not sufficient**:

```
DD_CONTAINER_EXCLUDE_METRICS = "image:^docker.io/library/bar(@sha256)?:.*"
DD_CONTAINER_INCLUDE = "image:^docker.io/library/foo(@sha256)?:.*"
```

Instead, use:

```
DD_CONTAINER_EXCLUDE_METRICS = "image:^docker.io/library/bar(@sha256)?:.*"
DD_CONTAINER_INCLUDE_METRICS = "image:^docker.io/library/foo(@sha256)?:.*"
DD_CONTAINER_INCLUDE_LOGS = "image:^docker.io/library/foo(@sha256)?:.*"
```

There is no interaction between the global lists and the selective (logs and metrics) lists. In other words, you cannot exclude a container globally (`DD_CONTAINER_EXCLUDE`) and then include it with `DD_CONTAINER_INCLUDE_LOGS` and `DD_CONTAINER_INCLUDE_METRICS`.

### Pause containers{% #pause-containers %}

The Datadog Agent excludes Kubernetes and OpenShift pause containers by default. This prevents their metric collection and counting as billable containers. They are still counted in the container count metrics such as `kubernetes.containers.running` and `docker.containers.running`.

To disable this behavior and include monitoring the pause containers:

{% tab title="Datadog Operator" %}
In Datadog Operator, set these environment variables under `spec.override.nodeAgent.env`.

##### Example{% #example %}

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
      - name: DD_EXCLUDE_PAUSE_CONTAINER
        value: "false"
```

{% /tab %}

{% tab title="Helm" %}
In your Helm chart, set `datadog.excludePauseContainer` to `true` or `false`.

##### Example{% #example %}

```yaml
datadog:
  containerExclude: "image:<IMAGE_NAME_1> image:<IMAGE_NAME_2>"
  containerInclude: "image:<IMAGE_NAME_3> image:<IMAGE_NAME_4>"
  excludePauseContainer: false
```

{% /tab %}

{% tab title="Containerized Agent" %}
In environments where you are not using Helm or the Operator, the following environment variables can be passed to the Agent container at startup.

Set `DD_EXCLUDE_PAUSE_CONTAINER` to `false`.
{% /tab %}

## Advanced CEL exclusion{% #advanced-cel-exclusion %}

In **Agent v7.73+**, you can use the `cel_workload_exclude` configuration option to filter containers from Autodiscovery. This feature allows you to define [Common Expression Langauge](https://github.com/google/cel-spec/blob/master/doc/langdef.md) rules to target containers to be excluded from telemetry collection.

Use the following attributes to represent the container object in your filtering rules:

| Attribute                   | Description                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| `container.name`            | The name of the container.                                              |
| `container.image.reference` | The full reference of the container image (registry, repo, tag/digest). |
| `container.pod.name`        | The name of the pod running the container.                              |
| `container.pod.namespace`   | The Kubernetes namespace of the pod.                                    |
| `container.pod.annotations` | The annotations applied to the pod (key-value map).                     |

### Configuration structure{% #configuration-structure %}

The `cel_workload_exclude` configuration option is structured as a list of rule sets evaluated as logical ORs, where a container is excluded if it matches any rule. Each rule set defines the `products` to exclude and the corresponding CEL `rules` to match against containers.

The `products` field accepts `metrics`, `logs`, and `global` (exclude container from all listed products).

{% alert level="danger" %}
If the configuration contains structural errors or CEL syntax issues, the Agent exits with an error to prevent collecting unintended telemetry that could impact billing.
{% /alert %}

In the example below, metrics and logs are excluded for any container with `nginx` in its name running in the `staging` namespace. Additionally, logs are excluded for any container running the `redis` image, OR any container within a pod that has the annotation `low_priority: "true"`. The [Agent's configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file) can be directly updated as seen by this example.

```yaml
# datadog.yaml
cel_workload_exclude:
- products: [metrics, logs]
  rules:
    containers:
      - container.name.matches("nginx") && container.pod.namespace == "staging"
- products: [logs]
  rules:
    containers:
      - container.image.reference.matches("redis")
      - container.pod.annotations["low_priority"] == "true"
```

The CEL-backed workload exclusion can also be configured by providing a JSON-formatted environment value to `DD_CEL_WORKLOAD_EXCLUDE`.

{% collapsible-section #setting-environment-variables %}
#### Setting environment variables

{% tab title="Datadog Operator" %}
In Datadog Operator, set these environment variables under `spec.override.nodeAgent.env`.

##### Example{% #example %}

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
      - name: DD_CEL_WORKLOAD_EXCLUDE
        value: >
          [{"products":["global"],"rules":{"containers":["container.name == \"redis\""]}}]
```

{% /tab %}

{% tab title="Helm" %}
In your Helm chart, use the `datadog.celWorkloadExclude` configuration option.

##### Example{% #example %}

```yaml
datadog:
  celWorkloadExclude:
  - products: [global]
    rules:
      containers:
        - container.name == "redis"
```

{% /tab %}

{% tab title="Containerized Agent" %}
In environments where you are not using Helm or the Operator, the following environment variables can be passed to the Agent container at startup.

##### Example Docker{% #example-docker %}

```shell
docker run -e DD_CEL_WORKLOAD_EXCLUDE=<JSON_CEL_RULES> ...
```

##### Example ECS{% #example-ecs %}

```json
"environment": [
  {
    "name": "DD_CEL_WORKLOAD_EXCLUDE",
    "value": "<JSON_CEL_RULES>"
  },
  ...
]
```

{% /tab %}

{% /collapsible-section %}

{% collapsible-section #validating-configuration-option %}
#### Validating configuration option

Use the `agent workloadfilter verify-cel` command to validate your configuration syntax before deployment. It accepts YAML or JSON input via stdin. The following example demonstrates validation catching an undefined field error:

```json
### cel-config.json
[
  {
    "products": ["metrics"],
    "rules":
      {
        "containers":
          [
            'container.undefined_field == "test"',
            'container.name.startsWith("-agent")',
          ],
      },
  },
]
```

```bash
agent workloadfilter verify-cel < cel-config.json

-> Validating CEL Configuration
    Loading YAML file...
â YAML loaded successfully (1 bundle(s))

-> Validating configuration structure...
â Configuration structure is valid

-> Compiling CEL rules...

  -> metrics
    Resource: container (2 rule(s))
      â Compilation failed: ERROR: <input>:1:10: undefined field 'undefined_field'
 | container.undefined_field == "test" || container.name.startsWith("-agent")
 | .........^
        Rule 1: container.undefined_field == "test"
        Rule 2: container.name.startsWith("-agent")

â Validation failed - some rules have errors
Error: CEL compilation failed
```

{% /collapsible-section %}

#### Example rules{% #example-rules %}

To exclude the container with a specific pod annotation:

```yaml
container.pod.annotations["monitoring"] == "false"
```

To exclude the container in namespaces without the substring `-dev`:

```yaml
!container.pod.namespace.matches("-dev")
```

To exclude the container with the name `nginx-server` only in the namespace `prod`:

```yaml
container.name == "nginx-server" && container.pod.namespace == "prod"
```

To exclude the container running an image with the substring `nginx`:

```yaml
container.image.reference.matches("nginx")
```

To exclude the container using grouped logic (for example, a specific container name in either of two namespaces):

```yaml
container.name == "redis" && (container.pod.namespace == "production" || container.pod.namespace == "staging")
```

To exclude containers based on their pod's owner name (for example, targeting all containers created by a Deployment or CronJob named `my-app`):

```yaml
container.pod.name.startsWith("my-app")
```

## Pod exclude configuration{% #pod-exclude-configuration %}

In **Agent v7.45+** you can set annotations on your Kubernetes pods to control Autodiscovery. Set the following annotations with the value `"true"` to add exclusion rules.

| Annotation                                          | Description                                                                      |
| --------------------------------------------------- | -------------------------------------------------------------------------------- |
| `ad.datadoghq.com/exclude`                          | Excludes the entire pod                                                          |
| `ad.datadoghq.com/logs_exclude`                     | Excludes log collection from the entire pod                                      |
| `ad.datadoghq.com/metrics_exclude`                  | Excludes metric collection from the entire pod                                   |
| `ad.datadoghq.com/<CONTAINER_NAME>.exclude`         | Excludes the container with `<CONTAINER_NAME>` in the pod                        |
| `ad.datadoghq.com/<CONTAINER_NAME>.logs_exclude`    | Excludes log collection from the container with `<CONTAINER_NAME>` in the pod    |
| `ad.datadoghq.com/<CONTAINER_NAME>.metrics_exclude` | Excludes metric collection from the container with `<CONTAINER_NAME>` in the pod |

The `ad.datadoghq.com/exclude` annotation set on the application pod takes the highest priority. This means that even if a container matches inclusion through `DD_CONTAINER_INCLUDE`, the Agent still ignores monitoring for that container. The same applies for the respective filtering configurations specific for metrics and logs.

When applying annotation-based exclusions, the Agent checks for all relevant exclusion annotations on the container. For example, when configuring logs for an NGINX container, the Agent will look for `ad.datadoghq.com/exclude`, `ad.datadoghq.com/logs_exclude`, `ad.datadoghq.com/nginx.exclude`, or `ad.datadoghq.com/nginx.logs_exclude` annotations to be `true` on the pod. The same applies for metrics.

#### Exclude the entire pod{% #exclude-the-entire-pod %}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example
spec:
  template:
    metadata:
      annotations:
        ad.datadoghq.com/exclude: "true"
    spec:
      containers:
        #(...)
```

#### Exclude log collection from a container{% #exclude-log-collection-from-a-container %}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example
spec:
  template:
    metadata:
      annotations:
        ad.datadoghq.com/helper.logs_exclude: "true"
    spec:
      containers:
        - name: app
          #(...)
        - name: helper
          #(...)
```

### Tolerate unready pods{% #tolerate-unready-pods %}

By default, `unready` pods are ignored when the Datadog Agent schedules checks. Therefore, metrics, service checks, and logs are not collected from these pods. To override this behavior, set the annotation `ad.datadoghq.com/tolerate-unready` to `"true"`. For example:

```yaml
apiVersion: v1
kind: Pod
# (...)
metadata:
  name: '<POD_NAME>'
  annotations:
    ad.datadoghq.com/tolerate-unready: "true"
  ...
```

## Security configuration{% #security-configuration %}

In **Agent v7.70+**, you can restrict security monitoring for specific containers, so you only get billed for the containers you want to have monitored. This functionality is not supported for the Datadog Operator.

{% tab title="Helm" %}

| Feature                                                                                                              | Include container                                   | Exclude container                                   |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| [Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/) | `datadog.securityAgent.compliance.containerInclude` | `datadog.securityAgent.compliance.containerExclude` |
| [Cloud Security Vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities)      | `datadog.sbom.containerImage.containerInclude`      | `datadog.sbom.containerImage.containerExclude`      |
| [Workload Protection](https://docs.datadoghq.com/security/workload_protection/)                                      | `datadog.securityAgent.runtime.containerInclude`    | `datadog.securityAgent.runtime.containerExclude`    |

{% /tab %}

{% tab title="Config file" %}
For [Cloud Security Vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities), you can use the following format in your config file to include or exclude containers:

```
---
sbom:
  container_image:
    container_include: ...
    container_exclude: ...
```

{% /tab %}

{% tab title="Containerized Agent" %}
In environments where you are not using Helm or the Operator, the following environment variables can be passed to the Agent container at startup.

| Feature                                                                                                              | Include container                              | Exclude container                              |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| [Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/) | `DD_COMPLIANCE_CONFIG_CONTAINER_INCLUDE`       | `DD_COMPLIANCE_CONFIG_CONTAINER_EXCLUDE`       |
| [Cloud Security Vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities)      | `DD_SBOM_CONTAINER_IMAGE_CONTAINER_INCLUDE`    | `DD_SBOM_CONTAINER_IMAGE_CONTAINER_EXCLUDE`    |
| [Workload Protection](https://docs.datadoghq.com/security/workload_protection/)                                      | `DD_RUNTIME_SECURITY_CONFIG_CONTAINER_INCLUDE` | `DD_RUNTIME_SECURITY_CONFIG_CONTAINER_EXCLUDE` |

{% /tab %}

## Further Reading{% #further-reading %}

- [Configure integrations with Autodiscovery on Kubernetes](https://docs.datadoghq.com/containers/kubernetes/integrations/)
- [Configure integrations with Autodiscovery on Docker](https://docs.datadoghq.com/containers/docker/integrations/)
