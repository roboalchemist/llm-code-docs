# Source: https://docs.datadoghq.com/tracing/trace_collection/configure_apm_features_linux.md

---
title: Enable SDK-dependent products on Linux
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Enable SDK-dependent products on
  Linux
---

# Enable SDK-dependent products on Linux

{% callout %}
The following functionality is in Preview.
{% /callout %}

## Overview{% #overview %}

On Linux hosts that use Single Step Instrumentation (SSI), you can enable or disable Datadog SDK-dependent products at the host level with the `application_monitoring.yaml` file. All instrumented services on the host inherit these settings.

## Configuration steps{% #configuration-steps %}

1. Ensure the `application_monitoring.yaml` file exists at the following path:

   ```
   /etc/datadog-agent/application_monitoring.yaml
   ```

1. To enable or disable products, define them under the `apm_configuration_default` block and set them to `true` or `false`.

**Note:** If a product is enabled through [environment variables set on the SDK](https://docs.datadoghq.com/tracing/trace_collection/library_config/), those values override the settings in `application_monitoring.yaml`.

As an example, the following enables profiling and Data Streams Monitoring, and disables tracing:

   ```
   apm_configuration_default:
     DD_PROFILING_ENABLED: true
     DD_DATA_STREAMS_ENABLED: true
     DD_APM_TRACING_ENABLED: false
   ```

## Supported products and configuration keys{% #supported-products-and-configuration-keys %}

The following table lists the products and their respective configuration keys:

| Product                                                                                                | Configuration key         |
| ------------------------------------------------------------------------------------------------------ | ------------------------- |
| [APM Tracing](https://www.datadoghq.com/product/apm/)                                                  | `DD_APM_TRACING_ENABLED`  |
| [Continuous Profiler](https://www.datadoghq.com/product/code-profiling/)                               | `DD_PROFILING_ENABLED`    |
| [Data Streams Monitoring](https://www.datadoghq.com/product/data-streams-monitoring/)                  | `DD_DATA_STREAMS_ENABLED` |
| [App and API Protection (AAP)](https://www.datadoghq.com/dg/security/application-security-management/) | `DD_APPSEC_ENABLED`       |
| [Code Security (IAST)](https://www.datadoghq.com/dg/security/code-security/)                           | `DD_IAST_ENABLED`         |
| [Data Observability: Jobs Monitoring](https://www.datadoghq.com/product/data-jobs-monitoring/)         | `DD_DATA_JOBS_ENABLED`    |
| [Software Composition Analysis](https://www.datadoghq.com/product/software-composition-analysis/)      | `DD_APPSEC_SCA_ENABLED`   |

## SDK version requirements{% #sdk-version-requirements %}

The following minimum SDK versions support configuration via `application_monitoring.yaml`:

| Language | Minimum SDK version |
| -------- | ------------------- |
| Java     | v1.47.0             |
| Python   | v3.2.0              |
| Node.js  | v5.41.0             |
| .NET     | Not yet supported   |
| PHP      | v1.8.0              |
| Ruby     | v2.18.0             |
| Go       | v2.1.0              |

## Further reading{% #further-reading %}

- [Learn more about Single Step Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm)
