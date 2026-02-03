# Source: https://docs.datadoghq.com/security/workload_protection/setup/agent/windows.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/agent/windows.md

# Source: https://docs.datadoghq.com/security/application_security/setup/python/windows.md

# Source: https://docs.datadoghq.com/security/application_security/setup/nodejs/windows.md

# Source: https://docs.datadoghq.com/security/application_security/setup/java/windows.md

# Source: https://docs.datadoghq.com/security/application_security/setup/dotnet/windows.md

# Source: https://docs.datadoghq.com/security/application_security/setup/windows.md

# Source: https://docs.datadoghq.com/agent/supported_platforms/windows.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/single-step-apm/windows.md

---
title: Single Step APM Instrumentation on Windows
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Single Step APM Instrumentation >
  Single Step APM Instrumentation on Windows
---

# Single Step APM Instrumentation on Windows

## Overview{% #overview %}

With Single Step Instrumentation (SSI), you can enable APM for your Java and .NET applications on Windows VMs using a single Datadog Agent installation command.

## Enable APM on Windows{% #enable-apm-on-windows %}

{% alert level="info" %}
Before proceeding, confirm that your environment is compatible by reviewing the [SSI compatibility guide.](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/compatibility/)
{% /alert %}

You can enable APM on Windows in the following ways:

- Instrument only .NET applications on IIS
- Instrument all Java and .NET applications across your entire Windows host

{% callout %}
##### Join the Preview!

Host-wide instrumentation for Windows is in Preview.

[Request Access](https://www.datadoghq.com/product-preview/single-step-instrumentation-on-windows-vms/)
{% /callout %}

{% tab title="IIS" %}
To instrument only .NET applications running on IIS:

1. In Datadog, go to [Install the Datadog Agent on Windows](https://app.datadoghq.com/fleet/install-agent/latest?platform=windows).

1. In the **Customize your observability coverage** section, toggle **Application Performance Monitoring (APM)**.

1. (Optional) Set your SDK version:

By default, Single Step Instrumentation installs the latest supported version of the Datadog .NET SDK. If you need to pin a specific version:

   1. Under **Instrumentation Configuration**, select **Customize Library Versions**.
   1. Under .NET, choose the version you want to use.

1. Copy and run the provided MSI install command on your Windows host.

1. Restart the IIS applications you want instrumented. (You do not need to restart the entire IIS server.)

After installation, the Agent automatically loads the Datadog .NET SDK into supported application processes to enable distributed tracing.
{% /tab %}

{% tab title="Host-wide (Preview)" %}

{% alert level="info" %}
Host-wide instrumentation on Windows is limited to Preview participants. The installation and configuration options described in this tab appear in the Datadog UI only after you're enrolled.
{% /alert %}

To instrument Java and .NET applications across your entire Windows host:

1. In Datadog, go to [Install the Datadog Agent on Windows](https://app.datadoghq.com/fleet/install-agent/latest?platform=windows).

1. In the **Customize your observability coverage** section, toggle **Application Performance Monitoring (APM)**.

1. (Optional) Set your SDK version:

By default, Single Step Instrumentation installs the latest supported version of the Datadog .NET and Java SDK. If you need to pin a specific version:

   1. Under **Instrumentation Configuration**, select **Customize Library Versions**.
   1. Under .NET, choose the version you want to use.

1. Copy and run the provided MSI install command on your Windows host.

1. Restart the services you want instrumented.

{% /tab %}

{% alert level="info" %}
SSI adds a small amount of startup time to instrumented applications. If this overhead is not acceptable for your use case, contact [Datadog Support](https://docs.datadoghq.com/help/).
{% /alert %}

## Configure Unified Service Tags{% #configure-unified-service-tags %}

Unified Service Tags (USTs) apply consistent tags across traces, metrics, and logs, making it easier to navigate and correlate your observability data. Learn how to [set USTs for Windows services](https://docs.datadoghq.com/integrations/windows-service/#tags).

## Enable SDK-dependent products and features{% #enable-sdk-dependent-products-and-features %}

After SSI loads the Datadog SDK into your applications and enables distributed tracing, you can configure additional products that rely on the SDK. These include capabilities such as [Continuous Profiler](https://docs.datadoghq.com/profiler/), [Application Security Monitoring](https://docs.datadoghq.com/security/application_security/), and [trace ingestion controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/).

To enable products, [set environment variables](https://docs.datadoghq.com/tracing/trace_collection/library_config/) in your application configuration.

## Remove Single Step APM instrumentation from your Agent{% #remove-single-step-apm-instrumentation-from-your-agent %}

To disable SSI for .NET on your host, run:

```shell
&"C:\Program Files\Datadog\Datadog Agent\bin\datadog-installer.exe" remove datadog-apm-library-dotnet
```

## Troubleshooting{% #troubleshooting %}

If you encounter problems enabling APM with SSI, see the [SSI troubleshooting guide](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting).

## Further reading{% #further-reading %}

- [Enable Runtime Metrics](https://docs.datadoghq.com/tracing/metrics/runtime_metrics/)
