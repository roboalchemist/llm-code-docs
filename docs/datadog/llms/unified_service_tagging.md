# Source: https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging.md

---
title: Unified Service Tagging
description: >-
  Connect telemetry across traces, metrics, and logs using standardized env,
  service, and version tags for consistent monitoring.
breadcrumbs: Docs > Getting Started > Getting Started with Tags > Unified Service Tagging
---

# Unified Service Tagging

## Overview{% #overview %}

Unified service tagging ties Datadog telemetry together by using three [reserved tags](https://docs.datadoghq.com/getting_started/tagging/): `env`, `service`, and `version`.

With these three tags, you can:

- Identify deployment impact with trace and container metrics filtered by version
- Navigate seamlessly across traces, metrics, and logs with consistent tags
- View service data based on environment or version in a unified fashion

{% video
   url="https://datadog-docs.imgix.net/images/tagging/unified_service_tagging/overview.mp4" /%}

**Notes**:

- The `version` tag is expected to change with each new application deployment. Two different versions of your application's code should have distinct `version` tags.
- The official service of a log defaults to the container short-image if no Autodiscovery logs configuration is present. To override the official service of a log, add Autodiscovery [Docker labels/pod annotations](https://docs.datadoghq.com/agent/docker/integrations/?tab=docker). For example: `"com.datadoghq.ad.logs"='[{"service": "service-name"}]'`
- Host information is excluded for database and cache spans because the host associated with the span is not the database/cache host.

### Requirements{% #requirements %}

- Unified service tagging requires the setup of a [Datadog Agent](https://docs.datadoghq.com/getting_started/agent) that is 6.19.x/7.19.x or higher.

- Unified service tagging requires a tracer version that supports new configurations of the [reserved tags](https://docs.datadoghq.com/getting_started/tagging/). More information can be found per language in the [setup instructions](https://docs.datadoghq.com/tracing/setup).

| Language | Minimum Tracer Version |
| -------- | ---------------------- |
| .NET     | 1.17.0+                |
| C++      | 0.1.0+                 |
| Go       | 1.24.0+                |
| Java     | 0.50.0+                |
| Node     | 0.20.3+                |
| PHP      | 0.47.0+                |
| Python   | 0.38.0+                |
| Ruby     | 0.34.0+                |

- Unified service tagging requires knowledge of configuring tags. If you are unsure of how to configure tags, read the [Getting Started with Tagging](https://docs.datadoghq.com/getting_started/tagging/) and [Assigning Tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags?tab=noncontainerizedenvironments) documentation before proceeding to configuration.

## Configuration{% #configuration %}

To start configuring unified service tagging, choose your environment:

- Containerized
- Non-Containerized
- Serverless
- OpenTelemetry

### Containerized environment{% #containerized-environment %}

In containerized environments, `env`, `service`, and `version` are set through the service's environment variables or labels (for example, Kubernetes deployment and pod labels, Docker container labels). The Datadog Agent detects this tagging configuration and applies it to the data it collects from containers.

To setup unified service tagging in a containerized environment:

1. Enable [Autodiscovery](https://docs.datadoghq.com/getting_started/agent/autodiscovery). This allows the Datadog Agent to automatically identify services running on a specific container and gathers data from those services to map environment variables to the `env`, `service,` and `version` tags.

1. If you are using [Docker](https://docs.datadoghq.com/agent/docker/integrations/?tab=docker), make sure the Agent can access your container's [Docker socket](https://docs.datadoghq.com/agent/docker/?tab=standard#optional-collection-agents). This allows the Agent detect the environment variables and map them to the standard tags.

1. Configure your environment that corresponds to your container orchestration service based on either full configuration or partial configuration as detailed below.

#### Configuration{% #configuration-1 %}

{% tab title="Kubernetes" %}
If you deployed the Datadog Cluster Agent with [Admission Controller](https://docs.datadoghq.com/agent/cluster_agent/admission_controller/) enabled, the Admission Controller mutates the pod manifests and injects all required environment variables (based on configured mutation conditions). In that case, manual configuration of `DD_` environment variables in pod manifests is unnecessary. For more information, see the [Admission Controller documentation](https://docs.datadoghq.com/agent/cluster_agent/admission_controller/).

##### Full configuration{% #full-configuration %}

To get the full range of unified service tagging when using Kubernetes, add environment variables to both the deployment object level and the pod template spec level:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    tags.datadoghq.com/env: "<ENV>"
    tags.datadoghq.com/service: "<SERVICE>"
    tags.datadoghq.com/version: "<VERSION>"
...
template:
  metadata:
    labels:
      tags.datadoghq.com/env: "<ENV>"
      tags.datadoghq.com/service: "<SERVICE>"
      tags.datadoghq.com/version: "<VERSION>"
  containers:
  -  ...
     env:
          - name: DD_ENV
            valueFrom:
              fieldRef:
                fieldPath: metadata.labels['tags.datadoghq.com/env']
          - name: DD_SERVICE
            valueFrom:
              fieldRef:
                fieldPath: metadata.labels['tags.datadoghq.com/service']
          - name: DD_VERSION
            valueFrom:
              fieldRef:
                fieldPath: metadata.labels['tags.datadoghq.com/version']
```

You can also use the OpenTelemetry Resource Attributes environment variables to set the `env`, `service`, and `version` tags:

```yaml
  containers:
  -  ...
     env:
         - name: OTEL_RESOURCE_ATTRIBUTES
           value: "service.name=<SERVICE>,service.version=<VERSION>,deployment.environment=<ENV>"
         - name: OTEL_SERVICE_NAME
           value: "<SERVICE>"
```

{% alert level="danger" %}
The `OTEL_SERVICE_NAME` environment variable takes precedence over the `service.name` attribute in the `OTEL_RESOURCE_ATTRIBUTES` environment variable.
{% /alert %}

##### Partial configuration{% #partial-configuration %}

###### Pod-level metrics{% #pod-level-metrics %}

To configure pod-level metrics, add the following standard labels (`tags.datadoghq.com`) to the pod spec of a Deployment, StatefulSet, or Job:

```yaml
template:
  metadata:
    labels:
      tags.datadoghq.com/env: "<ENV>"
      tags.datadoghq.com/service: "<SERVICE>"
      tags.datadoghq.com/version: "<VERSION>"
```

These labels cover pod-level Kubernetes CPU, memory, network, and disk metrics, and can be used for injecting `DD_ENV`, `DD_SERVICE`, and `DD_VERSION` into your service's container through [Kubernetes's downward API](https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/#capabilities-of-the-downward-api).

If you have multiple containers per pod, you can specify standard labels by container:

```yaml
tags.datadoghq.com/<container-name>.env
tags.datadoghq.com/<container-name>.service
tags.datadoghq.com/<container-name>.version
```

###### State metrics{% #state-metrics %}

To configure [Kubernetes State Metrics](https://docs.datadoghq.com/agent/kubernetes/data_collected/#kube-state-metrics):

1. Set `join_standard_tags` to `true` in your configuration file. See this [example configuration file](https://github.com/DataDog/integrations-core/blob/master/kubernetes_state/datadog_checks/kubernetes_state/data/conf.yaml.example) for the setting location.

1. Add the same standard labels to the collection of labels for the parent resource, for example: `Deployment`.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    tags.datadoghq.com/env: "<ENV>"
    tags.datadoghq.com/service: "<SERVICE>"
    tags.datadoghq.com/version: "<VERSION>"
spec:
  template:
    metadata:
      labels:
        tags.datadoghq.com/env: "<ENV>"
        tags.datadoghq.com/service: "<SERVICE>"
        tags.datadoghq.com/version: "<VERSION>"
```

###### APM tracer and StatsD client{% #apm-tracer-and-statsd-client %}

To configure [APM tracer](https://docs.datadoghq.com/tracing/send_traces/) and [StatsD client](https://docs.datadoghq.com/integrations/statsd/) environment variables, use the [Kubernetes's downward API](https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/#capabilities-of-the-downward-api) in the format below:

```yaml
containers:
-  ...
    env:
        - name: DD_ENV
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['tags.datadoghq.com/env']
        - name: DD_SERVICE
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['tags.datadoghq.com/service']
        - name: DD_VERSION
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['tags.datadoghq.com/version']
```

##### Automatic version tagging for APM data in containerized environments{% #automatic-version-tagging-for-apm-data-in-containerized-environments %}

{% alert level="info" %}
This feature is only enabled for [Application Performance Monitoring (APM)](https://docs.datadoghq.com/tracing/) data.
{% /alert %}

You can use the `version` tag in APM to [monitor deployments](https://docs.datadoghq.com/tracing/services/deployment_tracking/) and to identify faulty code deployments through [Automatic Faulty Deployment Detection](https://docs.datadoghq.com/watchdog/faulty_deployment_detection/).

For APM data, Datadog sets the `version` tag for you in the following priority order. If you manually set `version`, Datadog does not override your `version` value.

| Priority | Version Value                                                              |
| -------- | -------------------------------------------------------------------------- |
| 1        | {your version value}                                                       |
| 2        | {image_tag}_{first_7_digits_of_git_commit_sha}                             |
| 3        | {image_tag} or {first_7_digits_of_git_commit_sha} if only one is available |

Requirements:

- Datadog Agent Version 7.52.0 or greater
- If your services run in a containerized environment and `image_tag` is sufficient for tracking new version deployments, no further configuration is needed.
- If your services are not running in a containerized environment, or if you'd also like to have the Git SHA included, [embed Git information in your build artifacts](https://docs.datadoghq.com/integrations/guide/source-code-integration/?tab=go#embed-git-information-in-your-build-artifacts).

{% /tab %}

{% tab title="Docker" %}
##### Full configuration{% #full-configuration %}

Set the `DD_ENV`, `DD_SERVICE`, and `DD_VERSION` environment variables and corresponding Docker labels for your container to get the full range of unified service tagging.

The values for `service` and `version` can be provided in the Dockerfile:

```yaml
ENV DD_SERVICE <SERVICE>
ENV DD_VERSION <VERSION>

LABEL com.datadoghq.tags.service="<SERVICE>"
LABEL com.datadoghq.tags.version="<VERSION>"
```

Since `env` is likely determined at deploy time, you can inject the environment variable and label later:

```shell
docker run -e DD_ENV=<ENV> -l com.datadoghq.tags.env=<ENV> ...
```

You may also prefer to set everything at deploy time:

```shell
docker run -e DD_ENV="<ENV>" \
           -e DD_SERVICE="<SERVICE>" \
           -e DD_VERSION="<VERSION>" \
           -l com.datadoghq.tags.env="<ENV>" \
           -l com.datadoghq.tags.service="<SERVICE>" \
           -l com.datadoghq.tags.version="<VERSION>" \
           ...
```

##### Partial configuration{% #partial-configuration %}

If your service has no need for the Datadog environment variables (for example, third party software like Redis, PostgreSQL, NGINX, and applications not traced by APM) you can use the Docker labels:

```yaml
com.datadoghq.tags.env
com.datadoghq.tags.service
com.datadoghq.tags.version
```

As explained in the full configuration, these labels can be set in a Dockerfile or as arguments for launching the container.

##### Automatic version tagging for APM data in containerized environments{% #automatic-version-tagging-for-apm-data-in-containerized-environments %}

{% alert level="info" %}
This feature is only enabled for [Application Performance Monitoring (APM)](https://docs.datadoghq.com/tracing/) data.
{% /alert %}

You can use the `version` tag in APM to [monitor deployments](https://docs.datadoghq.com/tracing/services/deployment_tracking/) and to identify faulty code deployments through [Automatic Faulty Deployment Detection](https://docs.datadoghq.com/watchdog/faulty_deployment_detection/).

For APM data, Datadog sets the `version` tag for you in the following priority order. If you manually set `version`, Datadog does not override your `version` value.

| Priority | Version Value                                                              |
| -------- | -------------------------------------------------------------------------- |
| 1        | {your version value}                                                       |
| 2        | {image_tag}_{first_7_digits_of_git_commit_sha}                             |
| 3        | {image_tag} or {first_7_digits_of_git_commit_sha} if only one is available |

Requirements:

- Datadog Agent Version 7.52.0 or greater
- If your services run in a containerized environment and `image_tag` is sufficient for tracking new version deployments, no further configuration is needed.
- If your services are not running in a containerized environment, or if you'd also like to have the Git SHA included, [embed Git information in your build artifacts](https://docs.datadoghq.com/integrations/guide/source-code-integration/?tab=go#embed-git-information-in-your-build-artifacts).

{% /tab %}

{% tab title="ECS" %}

{% alert level="danger" %}
On ECS Fargate using Fluent Bit or FireLens, unified service tagging is only available for metrics and traces, not log collection.
{% /alert %}

##### Full configuration{% #full-configuration %}

Set the `DD_ENV`, `DD_SERVICE`, and `DD_VERSION` (optional with automatic version tagging) environment variables and corresponding Docker labels in the runtime environment of each service's container to get the full range of unified service tagging. For instance, you can set all of this configuration in one place through your ECS task definition:

```
"environment": [
  {
    "name": "DD_ENV",
    "value": "<ENV>"
  },
  {
    "name": "DD_SERVICE",
    "value": "<SERVICE>"
  },
  {
    "name": "DD_VERSION",
    "value": "<VERSION>"
  }

],
"dockerLabels": {
  "com.datadoghq.tags.env": "<ENV>",
  "com.datadoghq.tags.service": "<SERVICE>",
  "com.datadoghq.tags.version": "<VERSION>"
}
```

{% alert level="danger" %}
On ECS Fargate, you must add these tags to your application container, **not** the Datadog Agent container.
{% /alert %}

##### Partial configuration{% #partial-configuration %}

If your service has no need for the Datadog environment variables (for example, third party software like Redis, PostgreSQL, NGINX, and applications not traced by APM) you can use the Docker labels in your ECS task definition:

```
"dockerLabels": {
  "com.datadoghq.tags.env": "<ENV>",
  "com.datadoghq.tags.service": "<SERVICE>",
  "com.datadoghq.tags.version": "<VERSION>"
}
```

##### Automatic version tagging for APM data in containerized environments{% #automatic-version-tagging-for-apm-data-in-containerized-environments %}

{% alert level="info" %}
This feature is only enabled for [Application Performance Monitoring (APM)](https://docs.datadoghq.com/tracing/) data.
{% /alert %}

You can use the `version` tag in APM to [monitor deployments](https://docs.datadoghq.com/tracing/services/deployment_tracking/) and to identify faulty code deployments through [Automatic Faulty Deployment Detection](https://docs.datadoghq.com/watchdog/faulty_deployment_detection/).

For APM data, Datadog sets the `version` tag for you in the following priority order. If you manually set `version`, Datadog does not override your `version` value.

| Priority | Version Value                                                              |
| -------- | -------------------------------------------------------------------------- |
| 1        | {your version value}                                                       |
| 2        | {image_tag}_{first_7_digits_of_git_commit_sha}                             |
| 3        | {image_tag} or {first_7_digits_of_git_commit_sha} if only one is available |

Requirements:

- Datadog Agent Version 7.52.0 or greater
- If your services run in a containerized environment and `image_tag` is sufficient for tracking new version deployments, no further configuration is needed.
- If your services are not running in a containerized environment, or if you'd also like to have the Git SHA included, [embed Git information in your build artifacts](https://docs.datadoghq.com/integrations/guide/source-code-integration/?tab=go#embed-git-information-in-your-build-artifacts).

{% /tab %}

### Non-containerized environment{% #non-containerized-environment %}

Depending on how you build and deploy your services' binaries or executables, you may have several options available for setting environment variables. Since you may run one or more services per host, Datadog recommends scoping these environment variables to a single process.

To form a single point of configuration for all telemetry emitted directly from your services' runtime for [traces](https://docs.datadoghq.com/getting_started/tracing/), [logs](https://docs.datadoghq.com/getting_started/logs/), [RUM resources](https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm/), [Synthetics tests](https://docs.datadoghq.com/getting_started/synthetics/), [StatsD metrics](https://docs.datadoghq.com/integrations/statsd/), or system metrics, either:

1. Export the environment variables in the command for your executable:

   ```
   DD_ENV=<env> DD_SERVICE=<service> DD_VERSION=<version> /bin/my-service
   ```

1. Or use [Chef](https://www.chef.io/), [Ansible](https://www.ansible.com/), or another orchestration tool to populate a service's systemd or initd configuration file with the `DD` environment variables. When the service process starts, it has access to those variables.

   {% tab title="Traces" %}
When configuring your traces for unified service tagging:

   1. Configure the [APM Tracer](https://docs.datadoghq.com/tracing/setup/) with `DD_ENV` to keep the definition of `env` closer to the application that is generating the traces. This method allows the `env` tag to be sourced automatically from a tag in the span metadata.

   1. Configure spans with `DD_VERSION` to add version to all spans that fall under the service that belongs to the tracer (generally `DD_SERVICE`). This means that if your service creates spans with the name of an external service, those spans do not receive `version` as a tag.

As long as version is present in spans, it is added to trace metrics generated from those spans. The version can be added manually in-code or automatically by the APM Tracer. When configured, these are used by the APM and [DogStatsD clients](https://docs.datadoghq.com/developers/dogstatsd/) to tag trace data and StatsD metrics with `env`, `service`, and `version`. If enabled, the APM tracer also injects the values of these variables into your logs.

**Note**: There can only be **one service per span**. Trace metrics generally have a single service as well. However, if you have a different service defined in your hosts' tags, that configured service tag shows up on all trace metrics emitted from that host.

      {% /tab %}

   {% tab title="Logs" %}
If you're using [connected logs and traces](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/), enable automatic logs injection if supported for your APM Tracer. Then, the APM Tracer automatically injects `env`, `service`, and `version` into your logs, therefore eliminating manual configuration for those fields elsewhere.
   {% /tab %}

   {% tab title="RUM & Session Replay" %}
If you're using [connected RUM and traces](https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm/), specify the browser application in the `service` field, define the environment in the `env` field, and list the versions in the `version` field of your initialization file.

When you [create a RUM application](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/setup/), confirm the `env` and `service` names.
   {% /tab %}

   {% tab title="Synthetics" %}
If you're using [connected Synthetic browser tests and traces](https://docs.datadoghq.com/synthetics/apm/), specify a URL to send headers to under the **APM Integration for Browser Tests** section of the [Integration Settings page](https://app.datadoghq.com/synthetics/settings/integrations).

You can use `*` for wildcards, for example: `https://*.datadoghq.com`.
   {% /tab %}

   {% tab title="Custom Metrics" %}
Tags are added in an append-only fashion for [custom StatsD metrics](https://docs.datadoghq.com/metrics/). For example, if you have two different values for `env`, the metrics are tagged with both environments. There is no order in which one tag overrides another of the same name.

If your service has access to `DD_ENV`, `DD_SERVICE`, and `DD_VERSION`, then the DogStatsD client automatically adds the corresponding tags to your custom metrics.

**Note**: The Datadog DogStatsD clients for .NET and PHP do not support this functionality.
   {% /tab %}

   {% tab title="System Metrics" %}
You can add `env` and `service` tags to your infrastructure metrics. In non-containerized contexts, tagging for service metrics is configured at the Agent level.

Because this configuration does not change for each invocation of a service's process, adding `version` is not recommended.
Single service per host:
Set the following configuration in the Agent's [main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files):

   ```yaml
   env: <ENV>
   tags:
     - service:<SERVICE>
   ```

This setup guarantees consistent tagging of `env` and `service` for all data emitted by the Agent.
Multiple services per host:
Set the following configuration in the Agent's [main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files):

   ```yaml
   env: <ENV>
   ```

To get unique `service` tags on CPU, memory, and disk I/O metrics at the process level, configure a [process check](https://docs.datadoghq.com/integrations/process) in the Agent's configuration folder (for example, in the `conf.d` folder under `process.d/conf.yaml`):

   ```yaml
   init_config:
   instances:
       - name: web-app
         search_string: ["/bin/web-app"]
         exact_match: false
         service: web-app
       - name: nginx
         search_string: ["nginx"]
         exact_match: false
         service: nginx-web-app
   ```

**Note**: If you already have a `service` tag set globally in your Agent's main configuration file, the process metrics are tagged with two services. Since this can cause confusion with interpreting the metrics, it is recommended to configure the `service` tag only in the configuration of the process check.
   {% /tab %}

### Serverless environment{% #serverless-environment %}

For more information about AWS Lambda functions, see [how to connect your Lambda telemetry using tags](https://docs.datadoghq.com/serverless/configuration/#connect-telemetry-using-tags).

### OpenTelemetry{% #opentelemetry %}

When using OpenTelemetry, map the following [resource attributes](https://opentelemetry.io/docs/languages/js/resources/) to their corresponding Datadog conventions:

| OpenTelemetry convention        | Datadog convention |
| ------------------------------- | ------------------ |
| `deployment.environment` 1      | `env`              |
| `deployment.environment.name` 2 | `env`              |
| `service.name`                  | `service`          |
| `service.version`               | `version`          |

1: `deployment.environment` is deprecated in favor of `deployment.environment.name` in [OpenTelemetry semantic conventions v1.27.0](https://github.com/open-telemetry/semantic-conventions/releases/tag/v1.27.0).2: `deployment.environment.name` is supported in Datadog Agent 7.58.0+ and Datadog Exporter v0.110.0+.

{% alert level="danger" %}
Datadog-specific environment variables like `DD_SERVICE`, `DD_ENV` or `DD_VERSION` are not supported out of the box in your OpenTelemetry configuration.
{% /alert %}

{% tab title="Environment variables" %}
To set resource attributes using environment variables, set `OTEL_RESOURCE_ATTRIBUTES` with the appropriate values:

```shell
export OTEL_RESOURCE_ATTRIBUTES="service.name=my-service,deployment.environment=production,service.version=1.2.3"
```

{% /tab %}

{% tab title="SDK" %}
To set resource attributes in your application code, create a `Resource` with the desired attributes and associate it with your `TracerProvider`.

Here's an example using Python:

```python
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider

resource = Resource(attributes={
   "service.name": "<SERVICE>",
   "deployment.environment": "<ENV>",
   "service.version": "<VERSION>"
})
tracer_provider = TracerProvider(resource=resource)
```

{% /tab %}

{% tab title="Collector" %}
To set resource attributes from the OpenTelemetry Collector, use the [transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/transformprocessor) in your Collector configuration file. The transform processor allows you to modify attributes of the collected telemetry data before sending it to the Datadog exporter:

```yaml
processors:
  transform:
    trace_statements:
      - context: resource
        statements:
          - set(attributes["service.name"], "my-service")
          - set(attributes["deployment.environment"], "production")
          - set(attributes["service.version"], "1.2.3")
...
```

{% /tab %}

## Further Reading{% #further-reading %}

- [Learn how to use tags in the Datadog app](https://docs.datadoghq.com/getting_started/tagging/using_tags)
- [Use Version tags within Datadog APM to monitor deployments](https://docs.datadoghq.com/tracing/version_tracking)
- [Learn more about Autodiscovery](https://www.datadoghq.com/blog/autodiscovery-docker-monitoring/)
