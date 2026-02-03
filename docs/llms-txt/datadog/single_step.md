# Source: https://docs.datadoghq.com/security/application_security/setup/single_step.md

---
title: Enabling AAP threat detection and protection using single step instrumentation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Enabling App and API
  Protection > Enabling AAP threat detection and protection using single step
  instrumentation
---

# Enabling AAP threat detection and protection using single step instrumentation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="info" %}
Enabling AAP threat detection and protection using single step instrumentation is in Preview.
{% /alert %}

## Requirements{% #requirements %}

- **Minimum Agent version 7.53.0**
- **Minimum Helm version 3.62.0** (For Kubernetes deployments)
- **Languages and architectures**: Single step AAP instrumentation only supports tracing Java, Python, Node.js, and .NET Core services on `x86_64` and `arm64` architectures.
- **Operating systems**: Linux VMs (Debian, Ubuntu, Amazon Linux, CentOS/Red Hat, Fedora), Docker, Kubernetes clusters with Linux containers.

## Enabling in one step{% #enabling-in-one-step %}

If you [install or update a Datadog Agent][1] with the **Enable Threat Protection (new)** option selected, the Agent is installed and configured to enable AAP. This allows you to automatically instrument your application, without any additional installation or configuration steps. Restart services for this instrumentation to take effect.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/single_step/asm_single_step_threat_detection_2.c709aef321eb7056daf01e3506f4c90f.png?auto=format"
   alt="Account settings Ubuntu setup page highlighting the toggle for Enabling APM instrumentation and Threat Protection." /%}

The following examples show how it works on each infrastructure type.

{% tab title="Linux host or VM" %}
With one command, you can install, configure, and start the Agent, while also instrumenting your services with AAP.

For an Ubuntu host:

1. Run the one-line installation command:
   ```shell
   DD_API_KEY=<YOUR_DD_API_KEY> DD_SITE="<YOUR_DD_SITE>" DD_APM_INSTRUMENTATION_ENABLED=host DD_APM_INSTRUMENTATION_LIBRARIES="java:1,python:4,js:5,dotnet:3,php:1" DD_APPSEC_ENABLED=true bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
   ```

   1. Replace `<YOUR_DD_API_KEY>` with your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).
   1. Replace `<YOUR_DD_SITE>` with your [Datadog site](https://docs.datadoghq.com/getting_started/site/).
Important alert (level: info): You can also optionally configure the following:
   - Specifying tracing library versions.
   - Tagging observability data by environment.
1. Exit your current shell session.
1. Start a new shell session.
1. Restart the services on the host or VM.
1. [Explore the performance observability of your services in Datadog](https://docs.datadoghq.com/software_catalog/).

**Note:** To configure single-step for AAP threat protection, add the environment variable `DD_APPSEC_ENABLED=true` to your one-line installation command.

### Specifying tracing library versions{% #lib-linux %}

By default, enabling APM on your server installs support for Java, Python, Node.js, and .NET Core services. If you only have services implemented in some of these languages, set `DD_APM_INSTRUMENTATION_LIBRARIES` in your one-line installation command:

```shell
DD_APM_INSTRUMENTATION_LIBRARIES="java:1.25.0,python" DD_API_KEY=<YOUR_DD_API_KEY> DD_SITE="<YOUR_DD_SITE>" DD_APM_INSTRUMENTATION_ENABLED=host DD_APPSEC_ENABLED=true DD_ENV=staging bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
```

You can optionally provide a version number for the tracing library by placing a colon after the language name and specifying the tracing library version. If you don't specify a version, it defaults to the latest version. Language names are comma-separated.

Supported languages include:

- .NET (`dotnet`)
- Python (`python`)
- Java (`java`)
- Node.js (`js`)
- PHP (`php`)

**Note**: For the Node.js tracing library, different versions of Node.js are compatible with different versions of the Node.js tracing library. See [DataDog/dd-trace-js: JavaScript APM Tracer](https://github.com/DataDog/dd-trace-js?tab=readme-ov-file#version-release-lines-and-maintenance) for more information.

### Tagging observability data by environment{% #env-linux %}

Set `DD_ENV` in your one-line installation command for Linux to automatically tag instrumented services and other telemetry that pass through the Agent with a specific environment. For example, if the Agent is installed in your staging environment, set `DD_ENV=staging` to associate your observability data with `staging`.

For example:

```shell
DD_API_KEY=<YOUR_DD_API_KEY> DD_SITE="<YOUR_DD_SITE>" DD_APM_INSTRUMENTATION_ENABLED=host DD_APM_INSTRUMENTATION_LIBRARIES="java:1,python:4,js:5,dotnet:3,php:1" DD_APPSEC_ENABLED=true DD_ENV=staging bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
```

{% /tab %}

{% tab title="Docker" %}
For a Docker Linux container:

1. Install the library injector:
   ```shell
   DD_APM_INSTRUMENTATION_ENABLED=docker DD_APM_INSTRUMENTATION_LIBRARIES="java:1,python:4,js:5,dotnet:3,php:1" DD_NO_AGENT_INSTALL=true DD_APPSEC_ENABLED=true bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
   ```
1. Configure the Agent in Docker:
   ```shell
   docker run -d --name dd-agent \
     -e DD_API_KEY=${YOUR_DD_API_KEY} \
     -e DD_APM_ENABLED=true \
     -e DD_APPSEC_ENABLED=true \
     -e DD_APM_NON_LOCAL_TRAFFIC=true \
     -e DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true \
     -e DD_APM_RECEIVER_SOCKET=/opt/datadog/apm/inject/run/apm.socket \
     -e DD_DOGSTATSD_SOCKET=/opt/datadog/apm/inject/run/dsd.socket \
     -v /opt/datadog/apm:/opt/datadog/apm \
     -v /var/run/docker.sock:/var/run/docker.sock:ro \
     gcr.io/datadoghq/agent:7
   ```
Replace `<YOUR_DD_API_KEY>` with your [Datadog API](https://app.datadoghq.com/organization-settings/api-keys).Important alert (level: info): You can also optionally configure the following:
   - Specifying tracing library versions.
   - Tagging observability data by environment.
1. Restart the Docker containers.
1. [Explore the performance observability of your services in Datadog](https://docs.datadoghq.com/software_catalog/).

### Specifying tracing library versions{% #lib-docker %}

By default, enabling APM on your server installs support for Java, Python, Node.js, and .NET services. If you only have services implemented in some of these languages, set `DD_APM_INSTRUMENTATION_LIBRARIES` when running the installation script.

For example, to install support for only v1.25.0 of the Java tracing library and the latest Python tracing library, add the following to the installation command:

```shell
DD_APM_INSTRUMENTATION_LIBRARIES="java:1.25.0,python" DD_APM_INSTRUMENTATION_ENABLED=docker DD_NO_AGENT_INSTALL=true DD_APPSEC_ENABLED=true bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
```

You can optionally provide a version number for the tracing library by placing a colon after the language name and specifying the tracing library version. If you don't specify a version, it defaults to the latest version. Language names are comma-separated.

Supported languages include:

- .NET (`dotnet`)
- Python (`python`)
- Java (`java`)
- Node.js (`js`)
- Ruby (`ruby`)
- PHP (`php`)

**Note**: For the Node.js tracing library, different versions of Node.js are compatible with different versions of the Node.js tracing library. See [DataDog/dd-trace-js: JavaScript APM Tracer](https://github.com/DataDog/dd-trace-js?tab=readme-ov-file#version-release-lines-and-maintenance) for more information.

### Tagging observability data by environment{% #env-docker %}

Set `DD_ENV` in the library injector installation command for Docker to automatically tag instrumented services and other telemetry that pass through the Agent with a specific environment. For example, if the Agent is installed in your staging environment, set `DD_ENV=staging` to associate your observability data with `staging`.

For example:

```shell
docker run -d --name dd-agent \
  -e DD_API_KEY=${YOUR_DD_API_KEY} \
  -e DD_APM_ENABLED=true \
  -e DD_APPSEC_ENABLED=true \
  -e DD_ENV=staging \
  -e DD_APM_NON_LOCAL_TRAFFIC=true \
  -e DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true \
  -e DD_APM_RECEIVER_SOCKET=/opt/datadog/apm/inject/run/apm.socket \
  -e DD_DOGSTATSD_SOCKET=/opt/datadog/apm/inject/run/dsd.socket \
  -v /opt/datadog/apm:/opt/datadog/apm \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  gcr.io/datadoghq/agent:7
```

{% /tab %}

{% tab title="Kubernetes" %}
You can enable APM by installing the Agent with the Datadog Helm chart. This deploys the Datadog Agent across all nodes in your Linux-based Kubernetes cluster with a DaemonSet.

**Note**: Single step instrumentation doesn't instrument applications in the namespace where you install the Datadog Agent. It's recommended to install the Agent in a separate namespace in your cluster where you don't run your applications.

### Requirements{% #requirements %}

- Make sure you have [Helm](https://v3.helm.sh/docs/intro/install/) installed.

### Installation{% #installation %}

To enable single step instrumentation with Helm:

1. Add the Helm Datadog repo:

   ```bash
   helm repo add datadog https://helm.datadoghq.com
   helm repo update
   ```

1. Create a Kubernetes Secret to store your Datadog [API key](https://app.datadoghq.com/organization-settings/api-keys):

   ```bash
   kubectl create secret generic datadog-secret --from-literal api-key=$DD_API_KEY
   ```

{% /tab %}

## Removing Single Step APM and AAP instrumentation from your Agent{% #removing-single-step-apm-and-aap-instrumentation-from-your-agent %}

If you don't want to collect trace data for a particular service, host, VM, or container, complete the follow steps:

### Removing instrumentation for specific services{% #removing-instrumentation-for-specific-services %}

Run the following commands and restart the service to stop injecting the library into the service and stop producing traces from that service.

{% tab title="Linux host or VM" %}

1. Add the `DD_INSTRUMENT_SERVICE_WITH_APM` environment variable to the service startup command:
   ```shell
   DD_INSTRUMENT_SERVICE_WITH_APM=false <service_start_command>
   ```
1. Restart the service.
1. To disable AAP, remove the `DD_APPSEC_ENABLED=true` environment variable from your application configuration, and restart your service.

{% /tab %}

{% tab title="Docker" %}

1. Add the `DD_INSTRUMENT_SERVICE_WITH_APM` environment variable to the service startup command:
   ```shell
   docker run -e DD_INSTRUMENT_SERVICE_WITH_APM=false <service_start_command>
   ```
1. Restart the service.
1. To disable AAP, remove the `DD_APPSEC_ENABLED=true` environment variable from your application configuration, and restart your service.

{% /tab %}

{% tab title="Kubernetes" %}

1. Set the `admission.datadoghq.com/enabled:` label to `"false"` for the pod spec:
   ```yaml
   spec:
     template:
       metadata:
         labels:
           admission.datadoghq.com/enabled: "false"
   ```

{% /tab %}



### Removing APM for all services on the infrastructure{% #removing-apm-for-all-services-on-the-infrastructure %}

To stop producing traces, remove library injectors and restart the infrastructure:

{% tab title="Linux host or VM" %}

1. Run:
   ```shell
   dd-host-install --uninstall
   ```
1. Restart your host.

{% /tab %}

{% tab title="Docker" %}

1. Uninstall local library injection:
   ```shell
   dd-container-install --uninstall
   ```
1. Restart Docker:
   ```shell
   systemctl restart docker
   ```
Or use the equivalent for your environment.

{% /tab %}

{% tab title="Kubernetes" %}

1. Under `apm:`, remove `instrumentation:` and all following configuration in `datadog-values.yaml`.
1. Under `asm:`, remove `threats:` and all following configuration in`datadog-values.yaml`.
1. Run the following command:
   ```bash
   helm upgrade datadog-agent -f datadog-values.yaml datadog/datadog
   ```

{% /tab %}
[1]: [https://app.datadoghq.com/account/settings/agent/latest](https://app.datadoghq.com/account/settings/agent/latest) [2]: /tracing/guide/remote_config

