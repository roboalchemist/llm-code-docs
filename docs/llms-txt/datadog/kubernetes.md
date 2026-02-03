# Source: https://docs.datadoghq.com/security/workload_protection/setup/agent/kubernetes.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/agent/kubernetes.md

# Source: https://docs.datadoghq.com/security/application_security/setup/python/kubernetes.md

# Source: https://docs.datadoghq.com/security/application_security/setup/php/kubernetes.md

# Source: https://docs.datadoghq.com/security/application_security/setup/nodejs/kubernetes.md

# Source: https://docs.datadoghq.com/security/application_security/setup/java/kubernetes.md

# Source: https://docs.datadoghq.com/security/application_security/setup/ruby/kubernetes.md

# Source: https://docs.datadoghq.com/security/application_security/setup/dotnet/kubernetes.md

# Source: https://docs.datadoghq.com/security/application_security/setup/kubernetes.md

# Source: https://docs.datadoghq.com/data_observability/jobs_monitoring/kubernetes.md

# Source: https://docs.datadoghq.com/containers/kubernetes.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/single-step-apm/kubernetes.md

---
title: Single Step APM Instrumentation on Kubernetes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Single Step APM Instrumentation >
  Single Step APM Instrumentation on Kubernetes
---

# Single Step APM Instrumentation on Kubernetes

## Overview{% #overview %}

In a Kubernetes environment, use Single Step Instrumentation (SSI) for APM to install the Datadog Agent and [instrument](https://docs.datadoghq.com/tracing/glossary/#instrumentation) your applications with the Datadog APM SDKs in one step.

## Requirements{% #requirements %}

- Kubernetes v1.20+.
- [`Helm`](https://v3.helm.sh/docs/intro/install/) for deploying the Datadog Operator.
- [`Kubectl` CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/) for installing the Datadog Agent.
- Confirmed environment compatibility per the [Single Step Instrumentation compatibility guide](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/compatibility/).

## Enable APM on your applications{% #enable-apm-on-your-applications %}

{% alert level="info" %}
Single Step Instrumentation does not instrument applications in the namespace where the Datadog Agent is installed. Install the Agent in a separate namespace where you do not run your applications.
{% /alert %}

Follow these steps to enable Single Step Instrumentation across your entire cluster. This automatically sends traces from all applications written in supported languages.

**Note:** To instrument only specific namespaces or pods, see workload targeting in Advanced options.

1. In Datadog, go to the [Install the Datadog Agent on Kubernetes](https://app.datadoghq.com/fleet/install-agent/latest?platform=kubernetes) page.

1. Follow the on-screen instructions to choose your installation method, select an API key, and set up the Operator or Helm repository.

1. In the **Configure `datadog-agent.yaml`** section, go to **Additional configuration** > **Application Observability**, and turn on **APM Instrumentation**.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_collection/k8s-apm-instrumentation-toggle.b2b0aaa1c3393f96d458e9076cd65978.jpg?auto=format"
      alt="The configuration block for installing the Datadog Agent on Kubernetes through the Datadog app" /%}

1. Deploy the Agent using the generated configuration file.

1. Restart your applications.

{% alert level="info" %}
SSI adds a small amount of startup time to instrumented applications. If this overhead is not acceptable for your use case, contact [Datadog Support](https://docs.datadoghq.com/help/).
{% /alert %}

## Configure Unified Service Tags{% #configure-unified-service-tags %}

Unified Service Tags (USTs) apply consistent tags across traces, metrics, and logs, making it easier to navigate and correlate your observability data. You can configure USTs through automatic label extraction (recommended), through explicit configuration with `ddTraceConfigs`, or in deployment manifests.

{% alert level="warning" %}
If you are using [Remote Configuration](https://docs.datadoghq.com/agent/remote_config/), automatic label extraction is not compatible. You must configure USTs explicitly using `ddTraceConfigs`.
{% /alert %}

### (Recommended) Configure USTs through automatic label extraction{% #recommended-configure-usts-through-automatic-label-extraction %}

With SSI, you can automatically extract UST values from pod labels and metadata without modifying individual deployments. To do this, configure `kubernetesResourcesLabelsAsTags` to map your existing Kubernetes labels to Datadog service tags.

**Note:** This method is not compatible with Remote Configuration. If you're using Remote Configuration, see Configure USTs explicitly with ddTraceConfigs.

#### Prerequisites{% #prerequisites %}

| Component            | Minimum version |
| -------------------- | --------------- |
| `datadog-agent`      | 7.69            |
| `datadog-operator`   | 1.16.0          |
| `datadog-helm-chart` | 3.120.0         |

#### Configuration{% #configuration %}

Replace `app.kubernetes.io/name` in the following example with any label that contains your service name (for example, `service.kubernetes.io/name` or `component`). You can configure multiple labels this way.

```yaml
datadog:
  # Automatically extract service names from Kubernetes labels
  kubernetesResourcesLabelsAsTags:
    pods:
      app.kubernetes.io/name: service     # Modern Kubernetes label
    deployments.apps:
      app.kubernetes.io/name: service
    replicasets.apps:
      app.kubernetes.io/name: service

  # Set environment globally for the entire cluster
  tags:
    - "env:production"

  apm:
    instrumentation:
      enabled: true
```

With this configuration, Datadog automatically sets the `service` tag using the value of the `app.kubernetes.io/name` label for any instrumented workload that includes this label.

### Configure USTs explicitly with ddTraceConfigs{% #configure-usts-explicitly-with-ddtraceconfigs %}

In most cases, automatic configuration is sufficient. However, if you need granular control over settings for specific workloads, use `ddTraceConfigs` to explicitly map labels to service configurations:

```yaml
datadog:
  kubernetesResourcesLabelsAsTags:
    pods:
      app.kubernetes.io/name: service
    deployments.apps:
      app.kubernetes.io/name: service

  # Set environment globally for the entire cluster
  tags:
    - "env:production"

  apm:
    instrumentation:
      enabled: true
      targets:
        - name: frontend-services
          podSelector:
            matchLabels:
              tier: frontend
          ddTraceConfigs:
            - name: DD_SERVICE       # Explicitly override service name
              valueFrom:
                fieldRef:
                  fieldPath: metadata.labels['app.kubernetes.io/name']
            # DD_ENV inherited from cluster-level tags above
            # DD_VERSION automatically extracted from image tags
```

### Configure USTs in deployment manifests{% #configure-usts-in-deployment-manifests %}

If your setup doesn't use labels suitable for UST extraction, you can set USTs directly in your deployment manifests using environment variables. This approach requires modifying each deployment individually, but offers precise control.

For complete instructions, see [setting USTs for Kubernetes services](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/?tab=kubernetes#containerized-environment).

## Enable SDK-dependent products and features{% #enable-sdk-dependent-products-and-features %}

After SSI loads the Datadog SDK into your applications and enables distributed tracing, you can configure additional products that rely on the SDK. These include capabilities such as [Continuous Profiler](https://docs.datadoghq.com/profiler/), [Application Security Monitoring](https://docs.datadoghq.com/security/application_security/), and [trace ingestion controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/).

Use one of the following setup methods:

- **Configure with workload targeting (recommended)**:

By default, Single Step Instrumentation instruments all services in all namespaces. Use workload targeting to limit instrumentation to specific namespaces, pods, or workloads, and apply custom configurations.

- **[Set environment variables](https://docs.datadoghq.com/tracing/trace_collection/library_config/)**:

Enable products by setting environment variables directly in your application configuration.

## Advanced options{% #advanced-options %}

Use the following advanced options to customize how Single Step Instrumentation behaves in your environment. These settings are optional and typically only needed in specialized setups.

### Target specific workloads{% #target-specific-workloads %}

By default, SSI instruments all services in all namespaces in your cluster. Depending on your Agent version, use one of the following configuration methods to refine which services are instrumented and how.

{% tab title="Agent v7.64+ (Recommended)" %}
Create targeting blocks with the `targets` label to specify which workloads to instrument and what configurations to apply.

Each target block has the following keys:

| Key                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`              | The name of the target block. This has no effect on monitoring state and is used only as metadata.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `namespaceSelector` | The namespace(s) to instrument. Specify using one or more of:- `matchNames`: A list of one or more namespace name(s).- `matchLabels`: A list of one or more label(s) defined in `{key,value}` pairs.- `matchExpressions`: A list of namespace selector requirements.Namespaces must meet all criteria to match. For more details, see the [Kubernetes selector documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#resources-that-support-set-based-requirements). |
| `podSelector`       | The pod(s) to instrument. Specify using one or more of:- `matchLabels`: A list of one or more label(s) defined in `{key,value}` pairs.- `matchExpressions`: A list of pod selector requirements.Pods must meet all criteria to match. For more details, see the [Kubernetes selector documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#resources-that-support-set-based-requirements).                                                                           |
| `ddTraceVersions`   | The [Datadog APM SDK](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/compatibility/#tracer-libraries) version to use for each language.                                                                                                                                                                                                                                                                                                                  |
| `ddTraceConfigs`    | APM SDK configs that allow setting Unified Service Tags, enabling Datadog products beyond tracing, and customizing other APM settings. [See full list of options](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/?tab=kubernetes).                                                                                                                                                                                                                                          |

The file you need to configure depends on how you enabled Single Step Instrumentation:

- If you enabled SSI with Datadog Operator, edit `datadog-agent.yaml`.
- If you enabled SSI with Helm, edit `datadog-values.yaml`.

**Note**: Targets are evaluated in order; the first match takes precedence.

#### Example configurations{% #example-configurations %}

Review the following examples demonstrating how to select specific services:

{% collapsible-section %}
#### Example 1: Enable all namespaces except one

This configuration:

- enables APM for all namespaces except the `jenkins` namespace.
  - **Note**: use `enabledNamespaces` to disable for all namespaces except those listed.
- instructs Datadog to instrument the Java applications with the default Java APM SDK and Python applications with `v.3.1.0` of the Python APM SDK.

```yaml
   apm:
     instrumentation:
       enabled: true
       disabledNamespaces:
         - "jenkins"
       targets:
         - name: "all-remaining-services"
           ddTraceVersions:
             java: "default"
             python: "3.1.0"
```

{% /collapsible-section %}

{% collapsible-section %}
#### Example 2: Instrument a subset of namespaces, matching on names and labels

This configuration creates two targets blocks:

- The first block (named `login-service_namespace`):
  - enables APM for services in the namespace `login-service`.
  - instructs Datadog to instrument services in this namespace with the default version of the Java APM SDK.
  - sets environment variable `DD_PROFILING_ENABLED` for this target group
- The second block (named `billing-service_apps`)
  - enables APM for services in the namespace(s) with label `app:billing-service`.
  - instructs Datadog to instrument this set of services with `v3.1.0` of the Python APM SDK.

```yaml
  apm:
    instrumentation:
      enabled: true
      targets:
        - name: "login-service_namespace"
          namespaceSelector:
            matchNames:
              - "login-service"
          ddTraceVersions:
            java: "default"
          ddTraceConfigs:
            - name: "DD_PROFILING_ENABLED"  ## profiling is enabled for all services in this namespace
              value: "auto"
        - name: "billing-service_apps"
          namespaceSelector:
            matchLabels:
              app: "billing-service"
          ddTraceVersions:
            python: "3.1.0"
```

{% /collapsible-section %}

{% collapsible-section %}
#### Example 3: Instrument different workloads with different tracers

This configuration does the following:

- enables APM for pods with the following labels:
  - `app:db-user`, which marks pods running the `db-user` application.
  - `webserver:routing`, which marks pods running the `request-router` application.
- instructs Datadog to use the default versions of the Datadog Tracer SDKs.
- sets Datadog environment variables to apply to each target group and configure the SDKs.

```yaml
   apm:
     instrumentation:
       enabled: true
       targets:
         - name: "db-user"
           podSelector:
             matchLabels:
               app: "db-user"
           ddTraceVersions:
             java: "default"
           ddTraceConfigs:   ## trace configs set for services in matching pods
             - name: "DD_DATA_STREAMS_ENABLED"
               value: "true"
         - name: "user-request-router"
           podSelector:
             matchLabels:
               webserver: "user"
           ddTraceVersions:
             php: "default"
```

{% /collapsible-section %}

{% collapsible-section %}
#### Example 4: Instrument a pod within a namespace

This configuration:

- enables APM for pods labeled `app:password-resolver` inside the `login-service` namespace.
- instructs Datadog to use the default version of the Datadog Java Tracer SDK.
- sets Datadog environment variables to apply to this target.

```yaml
   apm:
     instrumentation:
       enabled: true
       targets:
         - name: "login-service-namespace"
           namespaceSelector:
             matchNames:
               - "login-service"
           podSelector:
             matchLabels:
               app: "password-resolver"
           ddTraceVersions:
             java: "default"
           ddTraceConfigs:
             - name: "DD_PROFILING_ENABLED"
               value: "auto"
```

{% /collapsible-section %}

{% collapsible-section %}
#### Example 5: Instrument a subset of pods using `matchExpressions`

This configuration enables APM for all pods except those that have either of the labels `app=app1` or `app=app2`.

```yaml
   apm:
     instrumentation:
       enabled: true
       targets:
         - name: "default-target"
           podSelector:
               matchExpressions:
                 - key: app
                   operator: NotIn
                   values:
                   - app1
                   - app2
```

{% /collapsible-section %}

{% /tab %}

{% tab title="Agent <=v7.63 (Legacy)" %}
#### Enable or disable instrumentation for namespaces{% #enable-or-disable-instrumentation-for-namespaces %}

You can choose to enable or disable instrumentation for applications in specific namespaces. You can only set enabledNamespaces or disabledNamespaces, not both.

The file you need to configure depends on if you enabled Single Step Instrumentation with Datadog Operator or Helm:

{% collapsible-section %}
##### Datadog Operator

To enable instrumentation for specific namespaces, add `enabledNamespaces` configuration to `datadog-agent.yaml`:

```yaml
   features:
     apm:
       instrumentation:
         enabled: true
         enabledNamespaces: # Add namespaces to instrument
           - default
           - applications
```

To disable instrumentation for specific namespaces, add `disabledNamespaces` configuration to `datadog-agent.yaml`:

```yaml
   features:
     apm:
       instrumentation:
         enabled: true
         disabledNamespaces: # Add namespaces to not instrument
           - default
           - applications
```

{% /collapsible-section %}

{% collapsible-section %}
##### Helm

To enable instrumentation for specific namespaces, add `enabledNamespaces` configuration to `datadog-values.yaml`:

```yaml
   datadog:
      apm:
        instrumentation:
          enabled: true
          enabledNamespaces: # Add namespaces to instrument
             - namespace_1
             - namespace_2
```

To disable instrumentation for specific namespaces, add `disabledNamespaces` configuration to `datadog-values.yaml`:

```yaml
   datadog:
      apm:
        instrumentation:
          enabled: true
          disabledNamespaces: # Add namespaces to not instrument
            - namespace_1
            - namespace_2
```

{% /collapsible-section %}

#### Specify tracing library versions{% #specify-tracing-library-versions %}

{% alert level="info" %}
Starting with Datadog Cluster Agent v7.52.0+, you can automatically instrument a subset of your applications, based on the tracing libraries you specify.
{% /alert %}

Specify Datadog tracing libraries and their versions to automatically instrument applications written in those languages. You can configure this in two ways, which are applied in the following order of precedence:

1. Specify at the service level, or
1. Specify at the cluster level.

**Default**: If you don't specify any library versions, applications written in supported languages are automatically instrumented using the latest tracing library versions.

##### Specify at the service level{% #specify-at-the-service-level %}

To automatically instrument applications in specific pods, add the appropriate language annotation and library version for your application in your pod spec:

| Language | Pod annotation                                                        |
| -------- | --------------------------------------------------------------------- |
| Java     | `admission.datadoghq.com/java-lib.version: "<CONTAINER IMAGE TAG>"`   |
| Node.js  | `admission.datadoghq.com/js-lib.version: "<CONTAINER IMAGE TAG>"`     |
| Python   | `admission.datadoghq.com/python-lib.version: "<CONTAINER IMAGE TAG>"` |
| .NET     | `admission.datadoghq.com/dotnet-lib.version: "<CONTAINER IMAGE TAG>"` |
| Ruby     | `admission.datadoghq.com/ruby-lib.version: "<CONTAINER IMAGE TAG>"`   |
| PHP      | `admission.datadoghq.com/php-lib.version: "<CONTAINER IMAGE TAG>"`    |

Replace `<CONTAINER IMAGE TAG>` with the desired library version. Available versions are listed in the Datadog container registries and tracer source repositories for each language:

- [Java](https://github.com/DataDog/dd-trace-java/releases)
- [Node.js](https://github.com/DataDog/dd-trace-js/releases)
- [Python](https://github.com/DataDog/dd-trace-py/releases)
- [.NET](https://github.com/DataDog/dd-trace-dotnet/releases)
- [Ruby](https://github.com/DataDog/dd-trace-rb/releases)
- [PHP](https://github.com/DataDog/dd-trace-php/releases)

{% alert level="danger" %}
Exercise caution when using the `latest` tag, as major library releases may introduce breaking changes.
{% /alert %}

For example, to automatically instrument Java applications:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    # ...
spec:
  template:
    metadata:
      annotations:
        admission.datadoghq.com/java-lib.version: "<CONTAINER IMAGE TAG>"
    spec:
      containers:
        - # ...
```

##### Specify at the cluster level{% #specify-at-the-cluster-level %}

If you don't enable automatic instrumentation for specific pods using annotations, you can specify which languages to instrument across the entire cluster using the SSI configuration. When `apm.instrumentation.libVersions` is set, only applications written in the specified languages are instrumented, using the specified library versions.

The file you need to configure depends on if you enabled Single Step Instrumentation with Datadog Operator or Helm:

{% collapsible-section %}
##### Datadog Operator

For example, to instrument .NET, Python, and Node.js applications, add the following configuration to your `datadog-agent.yaml` file:

```yaml
   features:
     apm:
       instrumentation:
         enabled: true
         libVersions: # Add any libraries and versions you want to set
            dotnet: "x.x.x"
            python: "x.x.x"
            js: "x.x.x"
```

{% /collapsible-section %}

{% collapsible-section %}
##### Helm

For example, to instrument .NET, Python, and Node.js applications, add the following configuration to your `datadog-values.yaml` file:

```yaml
   datadog:
     apm:
       instrumentation:
         enabled: true
         libVersions: # Add any libraries and versions you want to set
            dotnet: "x.x.x"
            python: "x.x.x"
            js: "x.x.x"
```

{% /collapsible-section %}

{% /tab %}

### Change the default image registry{% #change-the-default-image-registry %}

Datadog publishes instrumentation libraries images on gcr.io, Docker Hub, and Amazon ECR:

| Language | gcr.io                                                                            | hub.docker.com                                                                                    | gallery.ecr.aws                                                                                 |
| -------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Java     | [gcr.io/datadoghq/dd-lib-java-init](http://gcr.io/datadoghq/dd-lib-java-init)     | [hub.docker.com/r/datadog/dd-lib-java-init](http://hub.docker.com/r/datadog/dd-lib-java-init)     | [gallery.ecr.aws/datadog/dd-lib-java-init](http://gallery.ecr.aws/datadog/dd-lib-java-init)     |
| Node.js  | [gcr.io/datadoghq/dd-lib-js-init](http://gcr.io/datadoghq/dd-lib-js-init)         | [hub.docker.com/r/datadog/dd-lib-js-init](http://hub.docker.com/r/datadog/dd-lib-js-init)         | [gallery.ecr.aws/datadog/dd-lib-js-init](http://gallery.ecr.aws/datadog/dd-lib-js-init)         |
| Python   | [gcr.io/datadoghq/dd-lib-python-init](http://gcr.io/datadoghq/dd-lib-python-init) | [hub.docker.com/r/datadog/dd-lib-python-init](http://hub.docker.com/r/datadog/dd-lib-python-init) | [gallery.ecr.aws/datadog/dd-lib-python-init](http://gallery.ecr.aws/datadog/dd-lib-python-init) |
| .NET     | [gcr.io/datadoghq/dd-lib-dotnet-init](http://gcr.io/datadoghq/dd-lib-dotnet-init) | [hub.docker.com/r/datadog/dd-lib-dotnet-init](http://hub.docker.com/r/datadog/dd-lib-dotnet-init) | [gallery.ecr.aws/datadog/dd-lib-dotnet-init](http://gallery.ecr.aws/datadog/dd-lib-dotnet-init) |
| Ruby     | [gcr.io/datadoghq/dd-lib-ruby-init](http://gcr.io/datadoghq/dd-lib-ruby-init)     | [hub.docker.com/r/datadog/dd-lib-ruby-init](http://hub.docker.com/r/datadog/dd-lib-ruby-init)     | [gallery.ecr.aws/datadog/dd-lib-ruby-init](http://gallery.ecr.aws/datadog/dd-lib-ruby-init)     |
| PHP      | [gcr.io/datadoghq/dd-lib-php-init](http://gcr.io/datadoghq/dd-lib-php-init)       | [hub.docker.com/r/datadog/dd-lib-php-init](http://hub.docker.com/r/datadog/dd-lib-php-init)       | [gallery.ecr.aws/datadog/dd-lib-php-init](http://gallery.ecr.aws/datadog/dd-lib-php-init)       |

The `DD_ADMISSION_CONTROLLER_AUTO_INSTRUMENTATION_CONTAINER_REGISTRY` environment variable in the Datadog Cluster Agent configuration specifies the registry used by the Admission Controller. The default value is `gcr.io/datadoghq`.

You can pull the tracing library from a different registry by changing it to `docker.io/datadog`, `public.ecr.aws/datadog`, or another URL if you are hosting the images in a local container registry.

For instructions on changing your container registry, see [Changing Your Container Registry](https://docs.datadoghq.com/containers/guide/changing_container_registry/).

### Use a private container registry{% #use-a-private-container-registry %}

If your organization does not allow direct pulls from public registries (such as `gcr.io`, `docker.io`, or `public.ecr.aws`), you can host the required Datadog images internally and configure the Admission Controller to use them.

To use SSI with a private container registry:

1. Follow [these instructions](https://docs.datadoghq.com/containers/guide/sync_container_images/#copy-an-image-to-another-registry-using-crane) to mirror Datadog's container images to your private registry.

You only need the images for the languages you are instrumenting. If you're not sure which ones you need, here's a baseline that covers most use cases:

   - `apm-inject`
   - `dd-lib-java-init`
   - `dd-lib-python-init`
   - `dd-lib-dotnet-init`
   - `dd-lib-php-init`
   - `dd-lib-ruby-init`
   - `dd-lib-js-init`

You can find these images on [gcr.io](https://gcr.io/datadoghq), [Docker Hub](https://hub.docker.com/u/datadog), or [Amazon ECR Public Gallery](https://gallery.ecr.aws/datadog).

1. Tag the images according to your configuration.

The versions you mirror must match the versions configured in your workloads, which might be set in one of the following ways:

   - globally in the Agent config using `ddTraceVersions`, or
   - per-pod using annotations like `admission.datadoghq.com/java-lib.version`.

If no version is explicitly configured, the default version (`0`) is used.

For example:

   ```
   apm:
     instrumentation:
       enabled: true
       targets:
         - name: "default-target"
           ddTraceVersions:
             java: "1"
             python: "3"
   ```

This configuration requires the following image tags:

   - `apm-inject:0`
   - `dd-lib-java-init:1`
   - `dd-lib-python-init:3`

1. Update the Cluster Agent configuration to use your private registry.

Set the `DD_ADMISSION_CONTROLLER_AUTO_INSTRUMENTATION_CONTAINER_REGISTRY` environment variable in your Cluster Agent config to use your private registry.

For more details on changing your container registry, see [Changing Your Container Registry](https://docs.datadoghq.com/containers/guide/changing_container_registry/).

### Using a Container Network Interface on EKS{% #using-a-container-network-interface-on-eks %}

When using a CNI like Calico, the control plane nodes are not able to initiate network connections to Datadog's Admission Controller and report an "Address is not allowed" error. To use Single Step instrumentation, modify Datadog's Cluster Agent with the `useHostNetwork: true` parameter.

```
datadog:
  ...

clusterAgent:
  useHostNetwork: true

  admissionController:
    ...
```

## Remove Single Step APM instrumentation from your Agent{% #remove-single-step-apm-instrumentation-from-your-agent %}

If you don't want to collect trace data for a particular service, host, VM, or container, complete the following steps:

### Remove instrumentation for specific services{% #remove-instrumentation-for-specific-services %}

To remove APM instrumentation and stop sending traces from a specific service, you can do one of the following:

#### Use workload selection (recommended){% #use-workload-selection-recommended %}

With workload selection (available for Agent v7.64+), you can enable and disable tracing for specific applications. See configuration details here.

#### Use the Datadog Admission Controller{% #use-the-datadog-admission-controller %}

As an alternative, or for a version of the agent that does not support workload selection, you can also disable pod mutation by adding a label to your pod.

{% alert level="danger" %}
In addition to disabling SSI, the following steps disable other mutating webhooks. Use with caution.
{% /alert %}

1. Set the `admission.datadoghq.com/enabled:` label to `"false"` for the pod spec:
   ```yaml
   spec:
     template:
       metadata:
         labels:
           admission.datadoghq.com/enabled: "false"
   ```
1. Apply the configuration:
   ```shell
   kubectl apply -f /path/to/your/deployment.yaml
   ```
1. Restart the services you want to remove instrumentation for.

### Remove APM for all services on the infrastructure{% #remove-apm-for-all-services-on-the-infrastructure %}

To stop producing traces, uninstall APM and restart the infrastructure:

The file you need to configure depends on if you enabled Single Step Instrumentation with Datadog Operator or Helm:

{% tab title="Datadog Operator" %}

1. Set `instrumentation.enabled=false` in `datadog-agent.yaml`:

   ```yaml
   features:
     apm:
       instrumentation:
         enabled: false
   ```

1. Deploy the Datadog Agent with the updated configuration file:

   ```shell
   kubectl apply -f /path/to/your/datadog-agent.yaml
   ```

{% /tab %}

{% tab title="Helm" %}

1. Set `instrumentation.enabled=false` in `datadog-values.yaml`:

   ```yaml
   datadog:
     apm:
       instrumentation:
         enabled: false
   ```

1. Run the following command:

   ```shell
   helm upgrade datadog-agent -f datadog-values.yaml datadog/datadog
   ```

{% /tab %}

## Best practices{% #best-practices %}

After you enable SSI, all supported processes in the cluster are automatically instrumented and begin producing traces within minutes.

To control where APM is activated and reduce overhead, consider the following best practices.

{% collapsible-section #id-for-anchoring %}
### Use opt-in labels for controlled APM rollout

#### Default vs. opt-in instrumentation{% #default-vs-opt-in-instrumentation %}

| Mode    | Behavior                                                                                                                                                                                                                                                                   | When to use                                                        |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Default | All supported processes in the cluster are instrumented.                                                                                                                                                                                                                   | Small clusters or prototypes.                                      |
| Opt-in  | Use [workload selection](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/kubernetes/?tab=agentv764recommended#configure-instrumentation-for-namespaces-and-pods) to restrict instrumentation to specific namespaces or pods. | Production clusters, staged rollouts, or costâsensitive use cases. |

#### Example: Enable instrumentation for specific pods{% #example-enable-instrumentation-for-specific-pods %}

1. Add a meaningful label (for example, `datadoghq.com/apm-instrumentation: "enabled"`) to both the deployment metadata and the pod template.

   ```
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: checkout-api
     labels:
       app: checkout-api
       datadoghq.com/apm-instrumentation: "enabled"   # opt-in label (cluster-wide)
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: checkout-api
     template:
       metadata:
         labels:
           app: checkout-api
           datadoghq.com/apm-instrumentation: "enabled"   # opt-in label must be on *template*, too
           # Unified Service Tags (recommended)
           tags.datadoghq.com/service: "checkout-api"
           tags.datadoghq.com/env:     "prod"
           tags.datadoghq.com/version: "2025-06-10"
       spec:
         containers:
           - name: api
             image: my-registry/checkout:latest
             ports:
               - containerPort: 8080
   ```

1. In your Datadog Agent Helm config, enable SSI and use `podSelector` to inject only into pods with the matching opt-in label.

   ```
     apm:
       instrumentation:
         enabled: true
         targets:
           - name: apm-instrumented
             podSelector:
               matchLabels:
                 datadoghq.com/apm-instrumentation: "enabled"
   ```

See [workload selection](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/kubernetes/?tab=agentv764recommended#configure-instrumentation-for-namespaces-and-pods) for additional examples.
{% /collapsible-section %}

{% collapsible-section #id-for-anchoring %}
### Control which APM SDKs are loaded

Use `ddTraceVersions` in your Agent Helm config to control both the language and the version of the APM SDK. This prevents unnecessary SDKs from being downloaded, which minimizes init-container footprint, reduces image size, and allows for more deliberate tracer upgrades (for example, to meet compliance requirements or simplify debugging).

#### Example: Specify a Java APM SDK for a namespace{% #example-specify-a-java-apm-sdk-for-a-namespace %}

Only Java applications run in the `login-service` namespace. To avoid downloading other SDKs, configure the Agent to target that namespace and inject only the Java SDK version 1.48.2.

```
targets:
  - name: login-service
    namespaceSelector:
      matchNames: ["login-service"]
    ddTraceVersions:
      java: "1.48.2"    # pin version
```

#### Default configuration{% #default-configuration %}

If a pod doesn't match any `ddTraceVersions` rule, the default target applies.

```
targets:
  - name: default-target          # tag any pod *without* an override
    ddTraceVersions:
      java:   "1"   # stay on latest v1.x
      python: "3"   # stay on latest v3.x
      js:     "5"   # NodeJS
      php:    "1"
      dotnet: "3"
```

{% /collapsible-section %}

## Troubleshooting{% #troubleshooting %}

If you encounter problems enabling APM with SSI, see the [SSI troubleshooting guide](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting).

## Further reading{% #further-reading %}

- [Enable Runtime Metrics](https://docs.datadoghq.com/tracing/metrics/runtime_metrics/)
- [Learn about init container resource usage](https://docs.datadoghq.com/tracing/guide/init_resource_calc/)
- [Instrument your applications using local SDK injection](https://docs.datadoghq.com/tracing/guide/local_sdk_injection)
