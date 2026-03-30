# Source: https://docs.datadoghq.com/tracing/trace_collection/library_config/dotnet-framework.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/compatibility/dotnet-framework.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-framework.md

---
title: Tracing .NET Framework Applications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Add the Datadog Tracing Library >
  Tracing .NET Framework Applications
---

# Tracing .NET Framework Applications

## Compatibility requirements{% #compatibility-requirements %}

### Supported .NET Framework runtimes{% #supported-net-framework-runtimes %}

The .NET Tracer supports instrumentation on .NET Framework >= 4.6.1.

For a full list of Datadog's .NET Framework library and processor architecture support (including legacy and maintenance versions), see [Compatibility Requirements](https://docs.datadoghq.com/tracing/compatibility_requirements/dotnet-framework).

## Installation and getting started{% #installation-and-getting-started %}

{% alert level="info" %}
To set up Datadog APM in Serverless environments, such as AWS Lambda or Azure Functions, see [Serverless](https://docs.datadoghq.com/serverless).
{% /alert %}

{% alert level="danger" %}
**Note:** Datadog's automatic instrumentation relies on the .NET CLR Profiling API. This API allows only one subscriber (for example, Datadog APM). To ensure maximum visibility, run only one APM solution in your application environment.
{% /alert %}

### Installation{% #installation %}

Before you begin, make sure you've already [installed and configured the Agent](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/?tab=datadoglibraries#install-and-configure-the-agent).

1. Install the tracer.
1. Enable the tracer for your service.
1. View your live data.

### Install the tracer{% #install-the-tracer %}

After you install and configure your Datadog Agent, the next step is to add the tracing library directly in the application to instrument it. Read more about [compatibility information](https://docs.datadoghq.com/tracing/compatibility_requirements/dotnet-framework).

Install the Datadog .NET Tracer machine-wide so that all services on the machine are instrumented or on a per-application basis, so developers can manage the instrumentation through the application's dependencies. To see machine-wide installation instructions, click the Windows tab. To see per-application installation instructions, click the NuGet tab.

{% tab title="Windows" %}
To install the .NET Tracer machine-wide:

1. Download the [.NET Tracer MSI installer](https://github.com/DataDog/dd-trace-dotnet/releases). Use the x64 MSI installer if you are running 64-bit Windows; this can instrument both 64-bit and 32-bit applications. Only choose the x86 installer if you are running 32-bit Windows. Starting with v3.0.0, only the x64 installer is provided, as we do not support 32-bit operating systems.

1. Run the .NET Tracer MSI installer with administrator privileges.

You can also script the MSI setup by running the following in PowerShell: `Start-Process -Wait msiexec -ArgumentList '/qn /i datadog-apm.msi'`
{% /tab %}

{% tab title="NuGet" %}

{% alert level="danger" %}
**Note:** This installation does not instrument applications running in IIS. For applications running in IIS, follow the Windows machine-wide installation process.
{% /alert %}

To install the .NET Tracer per-application:

1. Add the `Datadog.Trace.Bundle` [NuGet package](https://www.nuget.org/packages/Datadog.Trace.Bundle) to your application.

{% /tab %}

### Enable the tracer for your service{% #enable-the-tracer-for-your-service %}

To enable the .NET Tracer for your service, set the required environment variables and restart the application.

For information about the different methods for setting environment variables, see Configuring process environment variables.

{% tab title="Windows" %}
#### Internet Information Services (IIS){% #internet-information-services-iis %}

1. The .NET Tracer MSI installer adds all required environment variables. There are no environment variables you need to configure.

1. To automatically instrument applications hosted in IIS, completely stop and start IIS by running the following commands as an administrator:

   ```cmd
   net stop /y was
   net start w3svc
   # Also, start any other services that were stopped when WAS was shut down.
   ```

Important alert (level: danger): **Note:** Always use the commands above to completely stop and restart IIS to enable the tracer. Avoid using the IIS Manager GUI application or `iisreset.exe`.

#### Services outside IIS{% #services-outside-iis %}

{% alert level="danger" %}
**Note:** The .NET runtime tries to load the .NET library into *any* .NET process that is started with these environment variables set. You should limit instrumentation to only the applications that need to be instrumented. **Don't set these environment variables globally as this causes *all* .NET processes on the host to be instrumented.**
{% /alert %}

1. Set the following required environment variables for automatic instrumentation to attach to your application:

   ```
   COR_ENABLE_PROFILING=1
   ```

1. For standalone applications and Windows services, manually restart the application.

{% /tab %}

{% tab title="NuGet" %}
Follow the instructions in the package readme, also available in [`dd-trace-dotnet` repository](https://github.com/DataDog/dd-trace-dotnet/blob/master/docs/Datadog.Trace.Bundle/README.md). Docker examples are also available in the [repository](https://github.com/DataDog/dd-trace-dotnet/tree/master/tracer/samples/NugetDeployment).
{% /tab %}

### View your live data{% #view-your-live-data %}

After enabling the .NET Tracer for your service:

1. Restart your service.

1. Create application load.

1. In Datadog, navigate to [**APM** > **APM Traces**](https://app.datadoghq.com/apm/traces).

## Configuration{% #configuration %}

If needed, configure the tracing library to send application performance telemetry data, including setting up Unified Service Tagging. Read [Library Configuration](https://docs.datadoghq.com/tracing/trace_collection/library_config/dotnet-framework/) for details.

## Custom instrumentation{% #custom-instrumentation %}

Custom instrumentation depends on your automatic instrumentation and includes additional steps depending on the method:

{% tab title="Windows" %}

{% alert level="danger" %}
**Note:** Starting with v3.0.0, custom instrumentation requires you also use automatic instrumentation. You should aim to keep both automatic and custom instrumentation package versions (for example: MSI and NuGet) in sync, and ensure you don't mix major versions of packages.
{% /alert %}

To use custom instrumentation in your .NET application:

1. Instrument your application using automatic instrumentation.
1. Add the `Datadog.Trace` [NuGet package](https://www.nuget.org/packages/Datadog.Trace) to your application.
1. In your application code, access the global tracer through the `Datadog.Trace.Tracer.Instance` property to create new spans.

{% /tab %}

{% tab title="NuGet" %}
To use custom instrumentation in your .NET application:

1. In your application code, access the global tracer through the `Datadog.Trace.Tracer.Instance` property to create new spans.

{% /tab %}

For more information on adding spans and tags for custom instrumentation, see the [.NET Custom Instrumentation documentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/dotnet/).

## Configuring process environment variables{% #configuring-process-environment-variables %}

To attach automatic instrumentation to your service, set the required environment variables before starting the application. See Enable the tracer for your service section to identify which environment variables to set based on your .NET Tracer installation method and follow the examples below to correctly set the environment variables based on the environment of your instrumented service.

{% alert level="danger" %}
**Note:** The .NET runtime tries to load the .NET library into *any* .NET process that is started with these environment variables set. You should limit instrumentation to only the applications that need to be instrumented. **Don't set these environment variables globally as this causes *all* .NET processes on the host to be instrumented.**
{% /alert %}

#### Windows services{% #windows-services %}

{% tab title="Registry Editor" %}
In the Registry Editor, create a multi-string value called `Environment` in the `HKLM\System\CurrentControlSet\Services\<SERVICE NAME>` key and set the value data to:

```text
COR_ENABLE_PROFILING=1
```

{% image
   source="https://datadog-docs.imgix.net/images/tracing/setup/dotnet/RegistryEditorFramework.14a1d349e6a5d85fa5970fe210399182.png?auto=format"
   alt="Using the Registry Editor to create environment variables for a Windows service" /%}

{% /tab %}

{% tab title="PowerShell" %}

```powershell
Set-ItemProperty HKLM:SYSTEM\CurrentControlSet\Services\<SERVICE NAME> -Name Environment -Value 'COR_ENABLE_PROFILING=1'
```

{% /tab %}

#### IIS{% #iis %}

After installing the MSI, no additional configuration is needed to automatically instrument your IIS sites. To set additional environment variables that are inherited by all IIS sites, perform the following steps:

1. Open the Registry Editor, find the multi-string value called `Environment` in the `HKLM\System\CurrentControlSet\Services\WAS` key, and add the environment variables, one per line. For example, to add logs injection and runtime metrics, add the following lines to the value data:

   ```text
   DD_LOGS_INJECTION=true
   DD_RUNTIME_METRICS_ENABLED=true
   ```

1. Run the following commands to restart IIS:

   ```cmd
   net stop /y was
   net start w3svc
   # Also, start any other services that were stopped when WAS was shut down.
   ```

{% image
   source="https://datadog-docs.imgix.net/images/tracing/setup/dotnet/RegistryEditorIIS.364ce600db39a83d19e7614d1f0f8837.png?auto=format"
   alt="Using the Registry Editor to create environment variables for all IIS sites" /%}

#### Console applications{% #console-applications %}

To automatically instrument a console application, set the environment variables from a batch file before starting your application:

```bat
rem Set required environment variables
SET COR_ENABLE_PROFILING=1

rem (Optionally) Set additional Datadog environment variables, for example:
SET DD_LOGS_INJECTION=true
SET DD_RUNTIME_METRICS_ENABLED=true

rem Start application
dotnet.exe example.dll
```

## Further reading{% #further-reading %}

- [Connect .NET application logs to traces](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/dotnet/)
- [Runtime metrics](https://docs.datadoghq.com/tracing/metrics/runtime_metrics/dotnet/)
- [Microsoft Azure App Service extension](https://docs.datadoghq.com/serverless/azure_app_services/)
- [Explore your services, resources, and traces](https://docs.datadoghq.com/tracing/glossary/)
- [.NET monitoring with Datadog APM and distributed tracing](https://www.datadoghq.com/blog/net-monitoring-apm/)
- [Monitor containerized ASP.NET Core applications](https://www.datadoghq.com/blog/asp-dotnet-core-monitoring/)
- [Monitor containerized ASP.NET Core applications on AWS Fargate](https://www.datadoghq.com/blog/deploy-dotnet-core-aws-fargate/)
- [Optimize your .NET application performance with the Datadog Continuous Profiler](https://www.datadoghq.com/blog/dotnet-datadog-continuous-profiler/)
- [Examples of custom instrumentation](https://github.com/DataDog/dd-trace-dotnet/tree/master/tracer/samples)
- [Source code](https://github.com/DataDog/dd-trace-dotnet)
