# Source: https://docs.datadoghq.com/tracing/guide/resource_based_sampling.md

---
title: Resource-based sampling
description: >-
  Learn how to configure resource-based sampling to control trace ingestion
  based on specific resources and endpoints for cost optimization.
breadcrumbs: Docs > APM > Tracing Guides > Resource-based sampling
source_url: https://docs.datadoghq.com/guide/resource_based_sampling/index.html
---

# Resource-based sampling

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Remote configuration allows you to dynamically set ingestion [sampling rates by service and resource name](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms#in-tracing-libraries-user-defined-rules), from the Datadog UI, without having to redeploy your service.

## Requirements{% #requirements %}

- Datadog Agent [7.41.1](https://github.com/DataDog/datadog-agent/releases/tag/7.41.1) or higher.
- [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config/) enabled for your Agent.
- `APM Remote Configuration Write` [permissions](https://docs.datadoghq.com/account_management/rbac/permissions/). If you don't have these permissions, ask your Datadog admin to update your permissions from your organization settings.

### Tracing library version{% #tracing-library-version %}

Find below the minimum tracing library version required for the feature:

| Language | Minimum version required                                                    |
| -------- | --------------------------------------------------------------------------- |
| Java     | [v1.34.0](https://github.com/DataDog/dd-trace-java/releases/tag/v1.34.0)    |
| Go       | [v1.64.0](https://github.com/DataDog/dd-trace-go/releases/tag/v1.63.1)      |
| Python   | [v.2.9.0](https://github.com/DataDog/dd-trace-py/releases/tag/v2.9.0)       |
| Ruby     | [v2.4.0](https://github.com/DataDog/dd-trace-rb/releases/tag/v2.4.0)        |
| Node.js  | [v5.16.0](https://github.com/DataDog/dd-trace-js/releases/tag/v5.16.0)      |
| PHP      | [v1.4.0](https://github.com/DataDog/dd-trace-php/releases/tag/1.4.0)        |
| .NET     | [v.2.53.2](https://github.com/DataDog/dd-trace-dotnet/releases/tag/v2.53.2) |
| C++      | [v0.2.2](https://github.com/DataDog/dd-trace-cpp/releases/tag/v0.2.2)       |

## See sampling rates by resource in the Ingestion Control page{% #see-sampling-rates-by-resource-in-the-ingestion-control-page %}

To see configured sampling rates by resource, navigate to the Ingestion controls [Service Ingestion summary](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls#service-ingestion-summary). The table lists the applied sampling rate by resource of the service.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/resource_sampling_rates.2d10bd3e1783ea7a9dd770e7be33033e.png?auto=format"
   alt="Sampling rates table by resource" /%}

- The `Ingested bytes` column surfaces the ingested bytes from spans of the service and resource, while the `Downstream bytes` column surfaces the ingested bytes from spans where the sampling decision is made starting from that service and resource, including bytes from downstream services in the call chain.
- The `Configuration` column surfaces where the resource sampling rate is being applied from:
  - `Automatic` if the [default head-based sampling mechanism](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms#in-the-agent) from the Agent applies.
  - `Local Configured` if a [sampling rule](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms#in-tracing-libraries-user-defined-rules) was set locally in the tracing library.
  - `Remote Configured` if a remote sampling rule was set from the Datadog UI. To learn how to configure sampling rules from the Ingestion Control page, read the section on remotely configuring sampling rules.

## Remotely configure sampling rules for the service{% #remotely-configure-sampling-rules-for-the-service %}

To configure sampling rates for the service by resource name:

1. Click **Manage Ingestion rate**. If the remote configuration option is disabled, make sure that the listed requirements are all met.
   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/sampling_configuration_modal.d4e4971e0db6099fb12ec8cc5879cf5f.png?auto=format"
      alt="Configuration Modal" /%}
1. Click **Add new rule** to set sampling rates for some resources. Sampling rules use glob pattern matching, so you can use wildcards (`*`) to match against multiple resources at the same time.
1. Click **Apply** to save the configuration.

The configuration should take effect in less than a minute. You can observe the configuration changes from the [Live Search Explorer](https://docs.datadoghq.com/tracing/trace_explorer/#live-search-for-15-minutes).

From the **Service Ingestion Summary**, resources for which the sampling rate are remotely applied should show as `Remote Configured` in the **Configuration** column.

## Further reading{% #further-reading %}

- [Ingestion Mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms)
- [Ingestion Control Page](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls)
