# Source: https://docs.datadoghq.com/agent/supported_platforms/linux.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/single-step-apm/linux.md

---
title: Single Step APM Instrumentation on Linux
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Single Step APM Instrumentation >
  Single Step APM Instrumentation on Linux
source_url: https://docs.datadoghq.com/trace_collection/single-step-apm/linux/index.html
---

# Single Step APM Instrumentation on Linux

## Overview{% #overview %}

On a Linux host or VM, use Single Step Instrumentation (SSI) for APM to install the Datadog Agent and [instrument](https://docs.datadoghq.com/tracing/glossary/#instrumentation) your applications in one step, with no additional configuration required.

## Enable APM on your applications{% #enable-apm-on-your-applications %}

{% alert level="info" %}
Before proceeding, confirm that your environment is compatible by reviewing the [SSI compatibility guide.](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/compatibility/)
{% /alert %}

To enable APM on a Linux host:

1. In Datadog, go to the [Install the Datadog Agent on Linux](https://app.datadoghq.com/fleet/install-agent/latest?platform=linux) page.

1. In the **Customize your observability coverage** section, go to **Additional features** > **Application Observability**, and turn on **APM Instrumentation**.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_collection/linux-apm-instrumentation-toggle.dac7ef96134da0438df89f4ceeba3fb0.png?auto=format"
      alt="The 'Customize your observability coverage' section of in-app instructions for installing the Datadog Agent on Linux" /%}

1. Copy and run the Agent installation command on your Linux host or VM.

1. Restart your applications.

{% alert level="info" %}
SSI adds a small amount of startup time to instrumented applications. If this overhead is not acceptable for your use case, contact [Datadog Support](https://docs.datadoghq.com/help/).
{% /alert %}

## Set SDK tracer versions{% #set-sdk-tracer-versions %}

By default, Single Step Instrumentation installs the latest versions of Datadog APM SDKs.

You may want to choose specific SDK versions for compatibility with your application's language version or specific environment requirements.

To customize SDK versions:

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com



1. In Datadog, go to the [Install the Datadog Agent on Linux](https://app.datadoghq.com/fleet/install-agent/latest?platform=linux) page.

1. After you turn on **APM Instrumentation**, click **Customize library versions**.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_collection/apm-instrumentation-version-pinning.5d47edec7389b8d323467110fa5ac203.png?auto=format"
      alt="The 'Customize library versions' drop-down in the instructions for installing the Datadog Agent on Linux" /%}

1. Find your language(s) and use the dropdown to either:

   - Select an exact SDK version, or
   - Select the major version, which uses the latest minor release available when the Agent installation command is run.

1. Copy and run the updated installation command.


{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



1. In Datadog, go to the [Install the Datadog Agent on Linux](https://app.datadoghq.com/fleet/install-agent/latest?platform=linux) page.

1. After you turn on **APM Instrumentation**, set your desired library versions with the `DD_APM_INSTRUMENTATION_LIBRARIES` variable in your Agent installation command:

   ```
   DD_API_KEY=<YOUR_DD_API_KEY> 
   DD_SITE="US1-FED" 
   DD_APM_INSTRUMENTATION_ENABLED=host 
   DD_APM_INSTRUMENTATION_LIBRARIES="java:1,python:2,js:5,dotnet:3,php:1" 
   bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
   ```

1. Find your language(s) and use the dropdown to either:

   - Select an exact SDK version, or
   - Select the major version, which uses the latest minor release available when the Agent installation command is run.

1. Copy and run the updated installation command.


{% /callout %}

Available versions are listed in source repositories for each language:

- [Java](https://github.com/DataDog/dd-trace-java/releases) (`java`)
- [Node.js](https://github.com/DataDog/dd-trace-js/releases) (`js`)
- [Python](https://github.com/DataDog/dd-trace-py/releases) (`python`)
- [.NET](https://github.com/DataDog/dd-trace-dotnet/releases) (`dotnet`)
- [Ruby](https://github.com/DataDog/dd-trace-rb/releases) (`ruby`)
- [PHP](https://github.com/DataDog/dd-trace-php/releases) (`php`)

## Configure Unified Service Tags{% #configure-unified-service-tags %}

Unified Service Tags (USTs) apply consistent tags across traces, metrics, and logs, making it easier to navigate and correlate your observability data. Learn how to [set USTs for Linux services](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/?tab=kubernetes#non-containerized-environment).

## Enable SDK-dependent products and features{% #enable-sdk-dependent-products-and-features %}

After SSI loads the Datadog SDK into your applications and enables distributed tracing, you can configure additional products that rely on the SDK. These include capabilities such as [Continuous Profiler](https://docs.datadoghq.com/profiler/), [Application Security Monitoring](https://docs.datadoghq.com/security/application_security/), and [trace ingestion controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/).

Use one of the following setup methods:

- **[Configure in `application_monitoring.yaml`](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/configure_apm_features_linux/)**:

Enable products across all services on a host without modifying application command lines.

- **[Set environment variables](https://docs.datadoghq.com/tracing/trace_collection/library_config/)**:

Enable products by setting environment variables directly in your application configuration.

## Advanced options{% #advanced-options %}

### Update SDK version{% #update-sdk-version %}

The SDK version is fixed when you run the Agent installation command.

To update the SDK versions:

1. Re-run the Agent installation command. This command also updates the Agent to the latest version.
1. Restart your applications.

### Define workload selection rules{% #define-workload-selection-rules %}

{% callout %}
##### Join the Preview!

Workload selection is in Preview.

[Request Access](https://www.datadoghq.com/product-preview/single-step-instrumentation-targeting-rules-on-linux/)
{% /callout %}

Workload selection rules (available for Agent v7.73+) let you control which processes are automatically instrumented by SSI on Linux hosts.

To configure workload selection:

1. In Datadog, navigate to **APM** > **Service Setup** > [**Workload Selection**](https://app.datadoghq.com/apm/service-setup/workload-selection).

1. Click **Add or Edit Rules**.

1. Define instrumentation rules:

   1. Click **Add New Rule**, then choose **Allow Rule** or **Block Rule** to specify whether matching processes should be instrumented.
   1. Name your rule.
   1. Add one or more conditions. See Define rule conditions to learn more.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_collection/workload_selection_landing.4535a465cbe54caa5a549ff7ed207b06.png?auto=format"
      alt="The workload selection UI, showing configuration options for defining a rule" /%}

1. (Optional) Drag and drop rules to reorder them.

**Note**: Rules are evaluated in order. After a process matches a rule, subsequent rules are ignored.

1. Set the default behavior (allow or block) for processes that do not match any rule.

1. Click **Next** to preview your rules.

1. Click **Deploy Rules**.

If Remote Configuration is enabled, rules are deployed to every host and applied on those with SSI enabled within 50 seconds . Alternatively, click **Export** to export the configuration file and apply it manually to your hosts.

#### Define rule conditions{% #define-rule-conditions %}

Each rule consists of one or more conditions. A condition includes the following elements:

- **Attribute**: The process property that the rule evaluates.
- **Operator**: The comparison logic (`equals`, `not equals`, `prefix`, or `contains`).
- **Value**: The text or pattern to match, such as a process name or command-line flag.

Supported attributes include:

| Attribute                    | Description                                       | Example               |
| ---------------------------- | ------------------------------------------------- | --------------------- |
| Process Executable           | Executable name of the process.                   | `python3.11`          |
| Process Executable Full Path | Full path of the executable.                      | `/usr/bin/python3.11` |
| Process Args                 | Command-line arguments used to start the process. | `--env=production`    |
| Language                     | Programming language detected for the process.    | `python`              |

## Remove Single Step APM instrumentation from your Agent{% #remove-single-step-apm-instrumentation-from-your-agent %}

To stop producing traces for all services on your infrastructure:

1. Run:
   ```shell
   dd-host-install --uninstall
   ```
1. Restart the services on the host or VM.

## Troubleshooting{% #troubleshooting %}

If you encounter problems enabling APM with SSI, see the [SSI troubleshooting guide](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting).

## Further reading{% #further-reading %}

- [Enable Runtime Metrics](https://docs.datadoghq.com/tracing/metrics/runtime_metrics/)
