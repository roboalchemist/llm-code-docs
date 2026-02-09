# Source: https://docs.datadoghq.com/security/workload_protection/setup/agent/docker.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/agent/docker.md

# Source: https://docs.datadoghq.com/security/application_security/setup/python/docker.md

# Source: https://docs.datadoghq.com/security/application_security/setup/php/docker.md

# Source: https://docs.datadoghq.com/security/application_security/setup/nodejs/docker.md

# Source: https://docs.datadoghq.com/security/application_security/setup/java/docker.md

# Source: https://docs.datadoghq.com/security/application_security/setup/ruby/docker.md

# Source: https://docs.datadoghq.com/security/application_security/setup/dotnet/docker.md

# Source: https://docs.datadoghq.com/security/application_security/setup/docker.md

# Source: https://docs.datadoghq.com/containers/docker.md

# Source: https://docs.datadoghq.com/cloudprem/install/docker.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/single-step-apm/docker.md

---
title: Single Step APM Instrumentation on Docker
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Single Step APM Instrumentation >
  Single Step APM Instrumentation on Docker
---

# Single Step APM Instrumentation on Docker

## Overview{% #overview %}

In a Docker Linux container, use Single Step Instrumentation (SSI) for APM to install the Datadog Agent and [instrument](https://docs.datadoghq.com/tracing/glossary/#instrumentation) your applications in one step, with no additional configuration required.

## Enable APM on your applications{% #enable-apm-on-your-applications %}

{% alert level="info" %}
Before proceeding, confirm that your environment is compatible by reviewing the [SSI compatibility guide.](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/compatibility/)
{% /alert %}

To enable APM in a Docker Linux container:

1. In Datadog, go to the [Install the Datadog Agent on Docker](https://app.datadoghq.com/fleet/install-agent/latest?platform=docker) page.

1. In the **Customize my agent install command** section, go to **Additional configuration** > **Application Observability**, and turn on **APM Instrumentation**.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_collection/docker-apm-instrumentation-toggle.938c8ca3f7550fba24ac50a6c4f8062d.png?auto=format"
      alt="The 'Customize your agent install command' section of in-app instructions for installing the Datadog Agent on Docker" /%}

1. Copy and run the Agent installation command in your Docker container. If the Agent is already running, redeploy the Agent container using the new command.

1. Restart your applications.

{% alert level="info" %}
SSI adds a small amount of startup time to instrumented applications. If this overhead is not acceptable for your use case, contact [Datadog Support](https://docs.datadoghq.com/help/).
{% /alert %}

## Set SDK tracer versions{% #set-sdk-tracer-versions %}

By default, Single Step Instrumentation installs the latest major versions of Datadog APM SDKs. Minor version updates are applied automatically when they become available.

You may want to customize SDK versions based on your application's language version or specific environment requirements. You can control the major and minor versions used by customizing library versions during setup.

To customize tracer versions:

1. In Datadog, go to the [Install the Datadog Agent on Docker](https://app.datadoghq.com/fleet/install-agent/latest?platform=docker) page.

1. After you turn on **APM Instrumentation**, click **Customize library versions**.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_collection/apm-instrumentation-version-pinning.5d47edec7389b8d323467110fa5ac203.png?auto=format"
      alt="The 'Customize library versions' drop-down in the instructions for installing the Datadog Agent on Docker" /%}

1. Find your language(s) and use the dropdown to either:

   - Pin an exact tracer version, or
   - Select the major version you want to use.

1. Copy and run the updated installation command.

Available versions are listed in source repositories for each language:

- [Java](https://github.com/DataDog/dd-trace-java/releases) (`java`)
- [Node.js](https://github.com/DataDog/dd-trace-js/releases) (`js`)
- [Python](https://github.com/DataDog/dd-trace-py/releases) (`python`)
- [.NET](https://github.com/DataDog/dd-trace-dotnet/releases) (`dotnet`)
- [Ruby](https://github.com/DataDog/dd-trace-rb/releases) (`ruby`)
- [PHP](https://github.com/DataDog/dd-trace-php/releases) (`php`)

## Configure Unified Service Tags{% #configure-unified-service-tags %}

Unified Service Tags (USTs) apply consistent tags across traces, metrics, and logs, making it easier to navigate and correlate your observability data. Learn how to [set USTs for Docker services](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/?tab=docker#containerized-environment).

## Enable SDK-dependent products and features{% #enable-sdk-dependent-products-and-features %}

After SSI loads the Datadog SDK into your applications and enables distributed tracing, you can configure additional products that rely on the SDK. These include capabilities such as [Continuous Profiler](https://docs.datadoghq.com/profiler/), [App and API Protection](https://docs.datadoghq.com/security/application_security/), and [trace ingestion controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/).

To enable products, [set environment variables](https://docs.datadoghq.com/tracing/trace_collection/library_config/) in your application configuration.

## Remove Single Step APM instrumentation from your Agent{% #remove-single-step-apm-instrumentation-from-your-agent %}

If you don't want to collect trace data for a particular service, host, VM, or container, complete the following steps:

### Remove instrumentation for specific services{% #remove-instrumentation-for-specific-services %}

To remove APM instrumentation and stop sending traces from a specific service:

1. Add the `DD_INSTRUMENT_SERVICE_WITH_APM` environment variable to the service startup command:
   ```shell
   docker run -e DD_INSTRUMENT_SERVICE_WITH_APM=false <service_start_command>
   ```
1. Restart the service.

### Remove APM for all services on the infrastructure{% #remove-apm-for-all-services-on-the-infrastructure %}

To stop producing traces, uninstall APM and restart the infrastructure:

1. Run:
   ```shell
   dd-container-install --uninstall
   ```
1. Restart Docker:
   ```shell
   systemctl restart docker
   ```
Or use the equivalent for your environment.

## Troubleshooting{% #troubleshooting %}

If you encounter problems enabling APM with SSI, see the [SSI troubleshooting guide](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting).

## Further reading{% #further-reading %}

- [Enable Runtime Metrics](https://docs.datadoghq.com/tracing/metrics/runtime_metrics/)
