# Source: https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls.md

---
title: Ingestion Controls
description: Learn how to control Ingestion rates with APM.
breadcrumbs: Docs > APM > The Trace Pipeline > Ingestion Controls
source_url: https://docs.datadoghq.com/trace_pipeline/ingestion_controls/index.html
---

# Ingestion Controls

{% image
   source="https://datadog-docs.imgix.net/images/tracing/apm_lifecycle/ingestion_sampling_rules.049c4637df137191e7beb433e16173e6.png?auto=format"
   alt="Ingestion Sampling Rules" /%}

Ingestion controls affect what traces are sent by your applications to Datadog. [APM Metrics](https://docs.datadoghq.com/tracing/metrics/metrics_namespace/) are always calculated based on all traces, and are not impacted by ingestion controls.

The Ingestion Control page provides visibility into the ingestion configuration of your applications and services. From the [ingestion control page](https://app.datadoghq.com/apm/traces/ingestion-control):

- Gain visibility on your service-level ingestion configuration.
- Adjust trace sampling rates for high throughput services or endpoints to better manage ingestion budget.
- Adjust trace sampling rates for low throughput, rare traffic services or endpoints to increase visibility.
- Understand which [ingestion mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/) are responsible for sampling most of your traces.
- Investigate and act on potential ingestion configuration issues, such as limited CPU or RAM resources for the Agent.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/ingestion_control_page.d3ffd45f6df13587a0d142b37f2469aa.png?auto=format"
   alt="Ingestion Control Page Overview" /%}

## Understanding your ingestion configuration{% #understanding-your-ingestion-configuration %}

Use the data in the ingestion control header to monitor your trace ingestion. The header displays the total amount of data ingested over the past hour, your estimated monthly usage, and the percentage of your allocated monthly ingestion limit, calculated based on your active APM infrastructure (such as hosts, Fargate tasks, and serverless functions).

If the monthly usage is under `100%`, the projected ingested data fits within your monthly allotment. A monthly usage value over `100%` means that the monthly ingested data is projected to be over your monthly allotment.

### Ingestion levels by service{% #ingestion-levels-by-service %}

The service table contains information about the ingested volumes and ingestion configuration, broken down by service:

{% dl %}

{% dt %}
Type
{% /dt %}

{% dd %}
The service type: web service, database, cache, browser, etcâ¦
{% /dd %}

{% dt %}
Name
{% /dt %}

{% dd %}
The name of each service sending traces to Datadog. The table contains root and non-root services for which data was ingested in the past one hour.
{% /dd %}

{% dt %}
Ingested Traces/s
{% /dt %}

{% dd %}
Average number of traces per second ingested starting from the service over the past one hour.
{% /dd %}

{% dt %}
Ingested Bytes/s
{% /dt %}

{% dd %}
Average number of bytes per second ingested for the service over the past one hour.
{% /dd %}

{% dt %}
Downstream Bytes/s
{% /dt %}

{% dd %}
Average number of bytes per second ingested for which the service *makes the sampling decision*. This includes the bytes of all downstream services' spans in the call stack that follow the decision made at the head of the trace. This column's data is based on the `sampling_service` dimension, set on the `datadog.estimated_usage.apm.ingested_bytes` metrics. For more information, read [APM usage metrics](https://docs.datadoghq.com/tracing/trace_pipeline/metrics#what-is-the-sampling-service).
{% /dd %}

{% dt %}
Traffic Breakdown
{% /dt %}

{% dd %}
A detailed breakdown of traffic sampled and unsampled for traces starting from the service. See Traffic breakdown for more information.
{% /dd %}

{% dt %}
Ingestion Configuration
{% /dt %}

{% dd %}
Shows `Automatic` if the [default head-based sampling mechanism](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-the-agent) from the Agent applies. If the ingestion was configured with [trace sampling rules](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-tracing-libraries-user-defined-rules), the service is marked as `Configured`; a `Local` label is set when the sampling rule is applied from configuration in the tracing library, a `Remote` label is set when the sampling rule is applied remotely, from the UI. For more information about configuring ingestion for a service, read about changing the default ingestion rate.
{% /dd %}

{% dt %}
Infrastructure
{% /dt %}

{% dd %}
Hosts, containers, and functions on which the service is running.
{% /dd %}

{% dt %}
Service status
{% /dt %}

{% dd %}
Shows `Limited Resource` when some spans are dropped due to the Datadog Agent reaching CPU or RAM limits set [in its configuration](https://docs.datadoghq.com/tracing/troubleshooting/agent_rate_limits/#maximum-cpu-percentage), `Legacy Setup` when some spans are ingested through the legacy [App Analytics mechanism](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#single-spans-app-analytics), or `OK` otherwise.
{% /dd %}

{% /dl %}

Filter the page by environment, configuration, and status to view services for which you need to take an action. To reduce the global ingestion volume, sort the table by the `Downstream Bytes/s` column to view services responsible for the largest share of your ingestion.

**Note**: The table is powered by the [usage metrics](https://docs.datadoghq.com/tracing/trace_pipeline/metrics) `datadog.estimated_usage.apm.ingested_spans` and `datadog.estimated_usage.apm.ingested_bytes`. These metrics are tagged by `service`, `env` and `ingestion_reason`.

#### Traffic breakdown{% #traffic-breakdown %}

The Traffic Breakdown column breaks down the destination of all traces starting from the service. It gives you an estimate of the share of traffic that is ingested and dropped, and for which reasons.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/service_traffic_breakdown.0a85f8443f211f3de60155774a0420e7.png?auto=format"
   alt="Traffic breakdown of trace ingestion" /%}

The breakdown is composed of the following parts:

- **Complete traces ingested** (blue): The percentage of traces that have been ingested by Datadog.

- **Complete traces not retained** (gray): The percentage of traces that have not been ingested by Datadog. Some traces might be dropped because:

  1. By default, the [Agent automatically sets a sampling rate](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-the-agent) on services, depending on service traffic.
  1. The service is configured to ingest a certain percentage of traces using [sampling rules](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-tracing-libraries-user-defined-rules).

- **Complete traces dropped by the tracer rate limiter** (orange): When you choose to manually set the service ingestion rate as a percentage with trace sampling rules, a rate limiter is automatically enabled, set to 100 traces per second by default. See the [rate limiter](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-tracing-libraries-user-defined-rules) documentation to change this rate.

- **Traces dropped due to the Agent CPU or RAM limit** (red): This mechanism may drop spans and create incomplete traces. To fix this, increase the CPU and memory allocation for the infrastructure that the Agent runs on.

## Configuring ingestion for a service{% #configuring-ingestion-for-a-service %}

Click on any service to view the Service Ingestion Summary, which provides actionable insights and configuration options for managing that service's trace ingestion.

### Ingestion configuration for a service{% #ingestion-configuration-for-a-service %}

#### Sampling rates by resource{% #sampling-rates-by-resource %}

The table lists the applied sampling rates by resource of the service.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/resource_sampling_rates.2d10bd3e1783ea7a9dd770e7be33033e.png?auto=format"
   alt="Sampling rates table by resource" /%}

- The `Ingested bytes` column surfaces the ingested bytes from spans of the service and resource, while the `Downstream bytes` column surfaces the ingested bytes from spans where the sampling decision is made starting from that service and resource, including bytes from downstream services in the call chain.
- The `Configuration` column surfaces where the resource sampling rate is being applied from:
  - `Automatic` if the [default head-based sampling mechanism](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-the-agent) from the Agent applies.
  - `Local Configured` if a [sampling rule](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-tracing-libraries-user-defined-rules) was set locally in the tracing library.
  - `Remote Configured` if a remote sampling rule was set from the Datadog UI. To learn how to configure sampling rules from the Ingestion Control page, read the section on remotely configuring sampling rules.

**Note**: If the service is not making sampling decisions, the service's resources will be collapsed under the `Resources not making sampling decisions` row.

#### Ingestion Reasons and sampling decision makers{% #ingestion-reasons-and-sampling-decision-makers %}

Explore the **Ingestion reasons breakdown** to see which mechanisms are responsible for your service ingestion. Each ingestion reason relates to one specific [ingestion mechanism](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/). After changing your service ingestion configuration, you can observe the increase or decrease of ingested bytes and spans in this timeseries graph based on the past hour of ingested data.

If most of your service ingestion volume is due to decisions taken by upstream services, investigate the detail of the **Sampling decision makers** top list. For example, if your service is non-root, (meaning that it **never decides** to sample traces), observe all upstream services responsible for your non-root service ingestion. Configure upstream root services to reduce your overall ingestion volume.

For further investigations, use the [APM Trace - Estimated Usage Dashboard](https://app.datadoghq.com/dash/integration/30337/app-analytics-usage), which provides global ingestion information as well as breakdown graphs by `service`, `env` and `ingestion reason`.

#### Agent and tracing library versions{% #agent-and-tracing-library-versions %}

See the **Datadog Agent and tracing library versions** your service is using. Compare the versions in use to the latest released versions to make sure you are running recent and up-to-date Agents and libraries.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/agent_tracer_version.f3ed8c0f22c3810f426ad09a05081372.png?auto=format"
   alt="Agent and tracing library versions" /%}

### Managing services' sampling rates{% #managing-services-sampling-rates %}

To control sampling rates for a service, you might want to use:

- **Adaptive sampling**: Automatically adjust sampling rates to match a configured monthly ingested volume budget.
- **Resource-based sampling**: Manually set explicit sampling rates by resource.

Configurations for these strategies can be applied **Remotely** through the Datadog UI. This method allows changes to take effect immediately without redeploying your service. For **Resource-based Sampling**, you also have the option to apply configurations **locally** by updating your service's configuration files and redeploying.

Using **Remote Configuration** for service ingestion rates has specific requirements.

{% collapsible-section open=null #remote-configuration-requirements %}
#### Remote Configuration requirements

- Datadog Agent [7.41.1](https://github.com/DataDog/datadog-agent/releases/tag/7.41.1) or higher.
- [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config) enabled for your Agent.
- `APM Remote Configuration Write` [permissions](https://docs.datadoghq.com/account_management/rbac/permissions/). If you don't have these permissions, ask your Datadog admin to update your permissions from your organization settings.

Find below the minimum tracing library version required for the feature:

| Language | Minimum version required |
| -------- | ------------------------ |
| Java     | v1.34.0                  |
| Go       | v1.64.0                  |
| Python   | v.2.9.0                  |
| Ruby     | v2.0.0                   |
| Node.js  | v5.16.0                  |
| PHP      | v1.4.0                   |
| .NET     | v2.53.2                  |
| C++      | v0.2.2                   |

{% /collapsible-section %}

#### Adaptive sampling{% #adaptive-sampling %}

Use Adaptive sampling to let Datadog manage services' sampling rates on your behalf. Specify a target monthly ingestion volume for one or multiple services while keeping visibility over all services and endpoints.

To configure adaptive sampling:

1. Navigate to the [Ingestion Control](https://app.datadoghq.com/apm/traces/ingestion-control) page.
1. Click a service to view the **Service Ingestion Summary**.
1. Click **Manage Ingestion Rate**.
1. Choose **Datadog adaptive sampling rates** as your service's sampling strategy.
1. Click **Apply**.

{% alert level="info" %}
If applying this configuration **Remotely** is disabled, ensure the Remote Configuration requirements are met.
{% /alert %}

For more information, see [Adaptive Sampling](https://docs.datadoghq.com/tracing/trace_pipeline/adaptive_sampling/).

#### Resource-based sampling{% #resource-based-sampling %}

To configure custom sampling rates for the service by resource name:

1. Navigate to the [Ingestion Control](https://app.datadoghq.com/apm/traces/ingestion-control) page.
1. Click a service to view the **Service Ingestion Summary**.
1. Click **Manage Ingestion rate**.
1. Click **Custom sampling rates only**.
1. Click **Add new rule** to set sampling rates for some resources.**Note**: Sampling rules use glob pattern matching, so you can use wildcards (`*`) to match against multiple resources at the same time.
   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/sampling_configuration_custom.4d668dc6ddc1063711c82cb0a4d59ea3.png?auto=format"
      alt="Configuration Modal" /%}
1. Apply the configuration **Remotely** or **Locally**:
   {% tab title="Remotely" %}
This option applies the configuration using Remote Configuration, so you **do not need** to redeploy the service for the change to take effect. You can observe the configuration changes from the [Live Search Explorer](https://docs.datadoghq.com/tracing/trace_explorer/?tab=listview#live-search-for-15-minutes).

Click **Apply** to save the configuration.

Resources that have been configured remotely display as `Configured Remote` in the **Configuration** column.


Important alert (level: info): If applying this configuration **Remotely** is disabled, ensure the Remote Configuration requirements are met.

   {% /tab %}

   {% tab title="Locally" %}
This option generates configuration for you to apply manually.

   1. Apply the generated configuration to your service.**Note**: The service name value is case sensitive. It should match the case of your service name.
   1. Redeploy the service.
   1. Confirm that the new percentage has been applied by looking at the **Traffic Breakdown** column. Resources that have been configured locally display as `Configured Local` in the **Configuration** column.

      {% /tab %}

## Managing Datadog Agent ingestion configuration{% #managing-datadog-agent-ingestion-configuration %}

Click **Configure Datadog Agent Ingestion** to manage default head-based sampling rates, error sampling and rare sampling.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/agent_level_configurations_modal.5f3e84cc363ea1d02b56cdc7736d07d0.png?auto=format"
   alt="Agent Level Configuration Modal" /%}

- **[Head-based Sampling](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-the-agent)**: When no sampling rules are set for a service, the Datadog Agent automatically computes sampling rates to be applied for your services, targeting **10 traces per second per Agent**. Change this target number of traces in Datadog, or set `DD_APM_MAX_TPS` locally at the Agent level.
- **[Error Spans Sampling](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#error-traces)**: For traces not caught by head-based sampling, the Datadog Agent catches local error traces **up to 10 traces per second per Agent**. Change this target number of traces in Datadog, or set `DD_APM_ERROR_TPS` locally at the Agent level.
- **[Rare Spans Sampling](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#rare-traces)**: For traces not caught by head-based sampling, the Datadog Agent catches local rare traces **up to 5 traces per second per Agent**. This setting is disabled by default. Enable the collection of rare traces in Datadog, or set `DD_APM_ENABLE_RARE_SAMPLER` locally at the Agent level.

With remote configuration, you don't have to restart the Agent to update these parameters. Click `Apply` to save the configuration changes, and the new configuration takes effect immediately. Remote configuration for Agent sampling parameters is available if you are using Agent version [7.42.0](https://github.com/DataDog/datadog-agent/releases/tag/7.42.0) or higher.

**Note**: The `Other Ingestion Reasons` (gray) section of the pie chart represents other ingestion reasons which *are not configurable* at the Datadog Agent level.

**Note**: Remotely configured parameters take precedence over local configurations such as environment variables and `datadog.yaml` configuration.

## Sampling rules' precedence{% #sampling-rules-precedence %}

If sampling rules are set in multiple locations, the following precedence rules apply in order, where rules that appear first on the list can override lower precedence rules:

1. Remotely configured sampling rules, set through resource-based sampling
1. [Adaptive sampling rules](https://docs.datadoghq.com/tracing/trace_pipeline/adaptive_sampling/)
1. [Locally configured sampling rules](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-tracing-libraries-user-defined-rules) (`DD_TRACE_SAMPLING_RULES`)
1. [Remotely configured global sampling rate](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-tracing-libraries-user-defined-rules)
1. [Locally configured global sampling rate](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#in-tracing-libraries-user-defined-rules) (`DD_TRACE_SAMPLE_RATE`)
1. Rates from the trace agent controlled indirectly with Agent settings remotely or locally (`DD_APM_MAX_TPS`)

To phrase it another way, Datadog uses the following precedence rules:

- Tracer settings > Agent settings
- Sampling rules > Global sampling rate
- Remote > Local

## Further Reading{% #further-reading %}

- [Ingestion Mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/)
- [Usage Metrics](https://docs.datadoghq.com/tracing/trace_pipeline/metrics/)
