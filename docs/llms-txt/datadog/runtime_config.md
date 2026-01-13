# Source: https://docs.datadoghq.com/tracing/trace_collection/runtime_config.md

---
title: Configuration at Runtime
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > APM > Application Instrumentation > Configuration at Runtime
source_url: https://docs.datadoghq.com/trace_collection/runtime_config/index.html
---

# Configuration at Runtime

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Configuration at runtime lets you modify APM library configuration from the Datadog UI, without needing to restart your application or service. You don't need to wait for a new deployment or code change to update your configuration. Instead, update it right away with configuration at runtime.

{% video
   url="https://datadog-docs.imgix.net/images//tracing/runtime_config/runtime-config-nav.mp4" /%}

## Setup{% #setup %}

Before you can use configuration at runtime, you must set up Remote Configuration. For more information, see [Setting up Remote Configuration for Tracing](https://docs.datadoghq.com/tracing/guide/remote_config/).

## Using configuration at runtime{% #using-configuration-at-runtime %}

To make changes to a service's configuration at runtime:

1. Go to the [Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/) in APM.
1. Hover over the service for which you want to update configuration.
1. Click **Full Page** next to the service name.
1. Click **Service Info**.
1. From the **Setup Guidance** tab, click **Edit**.
1. Change the configuration options as needed. See supported configuration options for more details.
1. Click **Apply Configuration**.

In **Active Library Configuration**, you can see which options are configured for this service and the selected environment:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/runtime_config/active-library-config.9dd77749a345f3da9ccf730f86c26c97.png?auto=format"
   alt="From the Setup Guidance tab, you can see your active library configuration." /%}

In this example, you can see that Log Injection is enabled for the Staging environment across two instances. An instance refers to an instance of the Remote Configuration client. There should be one instance per process of your application.

You can tell when the configuration changes have been successfully applied by referencing the **X Applied** text. In this example, the configuration applied successfully to all two instances.

## Supported configuration options{% #supported-configuration-options %}

The following options are supported with configuration at runtime. The required tracer version is listed for each language:

| Option                                                                                                                          | Java      | Node.js                 | Python   | .NET      | Ruby      | Go        | C++      |
| ------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------- | -------- | --------- | --------- | --------- | -------- |
| Custom sampling rate: Set a global sampling rate for the library using `DD_TRACE_SAMPLE_RATE`.                                  | `1.17.0+` | `4.11+` `3.32+` `2.45+` | `2.4.0+` | `2.33.0+` | `1.13.0+` | `1.59.0+` | `0.2.0+` |
| Log injection: Automatically inject trace correlation identifiers to correlate logs and traces by enabling `DD_LOGS_INJECTION`. | `1.17.0+` | `4.11+` `3.32+` `2.45+` | `2.6.0+` | `2.33.0+` | `1.13.0+` |
| HTTP header tags: Add HTTP header values as tags on traces using `DD_TRACE_HEADER_TAGS`.                                        | `1.17.0+` | `4.11+` `3.32+` `2.45+` | `2.6.0+` | `2.33.0+` | `1.13.0+` | `1.59.0+` |
| Custom span tags: Add specified tags to each span using `DD_TAGS`.                                                              | `1.31.0+` | `4.23.0+` `3.44.0+`     | `2.5.0+` | `2.44.0+` | `1.59.0+` | `0.2.0+`  |
| Resource-based sampling: Set sampling rates by service and resource name, from the Datadog UI using `DD_TRACE_SAMPLING_RULES`.  | `1.34.0+` | `5.16.0+`               | `2.9.0+` | `2.53.2+` | `2.0.0+`  | `1.64.0+` | `0.2.2+` |
| Adaptive Sampling: let Datadog control sampling rates on your behalf to match a configured monthly ingested volume budget.      | `1.34.0+` | `5.16.0+`               | `2.9.6+` | `2.54.0+` | `2.0.0+`  | `1.68.0+` | `0.2.2+` |

## Further reading{% #further-reading %}

- [Remote Configuration](https://docs.datadoghq.com/remote_configuration)
