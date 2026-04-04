# Source: https://docs.datadoghq.com/tracing/trace_pipeline/adaptive_sampling.md

---
title: Adaptive Sampling
description: >-
  Automatically adjust sampling rates to match specific budgets while
  maintaining visibility over service endpoints.
breadcrumbs: Docs > APM > The Trace Pipeline > Adaptive Sampling
---

# Adaptive Sampling

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog **adaptive sampling** helps you capture more relevant traces while remaining close to a specific budget (ingested gigabytes).

When you choose adaptive sampling as your sampling strategy, you select a target monthly volume for trace ingestion for one or more services. This ensures that the consumption of these services matches the target volume at the end of the month, while keeping visibility over their endpoints.

Adaptive sampling uses [remote configuration](https://docs.datadoghq.com/agent/remote_config) plus the existing [sampling rules](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms#in-tracing-libraries-user-defined-rules) mechanisms to dynamically adjust sampling rates for each environment, service, and resource combination. This helps you to:

- Match your specified monthly budget.
- Ensure visibility for low-traffic services and endpoints by capturing at least one trace for each combination of service, resource, and environment every 5 minutes.

To configure services to use adaptive sampling, follow the instructions listed below.

## Requirements{% #requirements %}

- Datadog Agent [7.53.0](https://github.com/DataDog/datadog-agent/releases/tag/7.53.0) or higher.
- [Remote Configuration](https://docs.datadoghq.com/agent/remote_config) enabled for your Agent.
- `APM Remote Configuration Write` [permission](https://docs.datadoghq.com/account_management/rbac/permissions/).**Note**: If you don't have this permission, ask your Datadog admin to update your permissions from your organization settings.

### Tracing library versions{% #tracing-library-versions %}

The following table lists minimum tracing library versions required for adaptive sampling:

| Language    | Minimum version required                                                   |
| ----------- | -------------------------------------------------------------------------- |
| Java        | [v1.34.0](https://github.com/DataDog/dd-trace-java/releases/tag/v1.34.0)   |
| Go          | [v1.68.0](https://github.com/DataDog/dd-trace-go/releases/tag/v1.68.0)     |
| Python      | [v2.9.6](https://github.com/DataDog/dd-trace-py/releases/tag/v2.9.6)       |
| Ruby        | [v2.0.0](https://github.com/DataDog/dd-trace-rb/releases/tag/v2.0.0)       |
| Node.js     | [v5.16.0](https://github.com/DataDog/dd-trace-js/releases/tag/v5.16.0)     |
| .NET        | [v2.54.0](https://github.com/DataDog/dd-trace-dotnet/releases/tag/v2.54.0) |
| C++/Proxies | [v0.2.2](https://github.com/DataDog/dd-trace-cpp/releases/tag/v0.2.2)      |
| PHP         | [v1.4.0](https://github.com/DataDog/dd-trace-php/releases/tag/1.4.0)       |

## Configure the adaptive sampling target{% #configure-the-adaptive-sampling-target %}

To get started with adaptive sampling, you first need to pick a target strategy setting:

- **Set Budget by Number of APM Hosts**: Configure a budget that is proportional to your allotment and the number of services onboarded (for example, based on the number of APM hosts)
- **Set Budget by Data Volume**: Configure a fixed target in gigabytes per month

| Budget by Number of APM Hosts | Budget by Data Volume                                                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Pros**                      | Scales with the number of APM hosts and the number of services onboarded; you only have to set it once                                    | Ensures you never go over budget                                                      |
| **Cons**                      | Not a good fit if you want to stay below a specific volume, as it may vary depending on the number of hosts reporting APM data to Datadog | You have to edit the budget every time you onboard a new service to adaptive sampling |

To set the adaptive sampling monthly target:

1. Navigate to the [Ingestion Control](https://app.datadoghq.com/apm/traces/ingestion-control) page.
1. Click **Manage Adaptive Sampling Target**.
   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/adaptive_sampling/adaptive_sampling_target_cta.eedc849a9afbd7cc610a5a94649a0453.png?auto=format"
      alt="Call to action to set adaptive sampling target" /%}
1. Choose a target strategy for sampling:
   - Set budget by number of APM hosts
   - Set budget by data volume
1. Click **Apply**.

### Set budget by number of APM hosts (Recommended){% #set-budget-by-number-of-apm-hosts-recommended %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/adaptive_sampling/percentage_based_target_setting.829db6e73373ab1ca6e3e270ac9fe5df.png?auto=format"
   alt="Percentage based target setting" /%}

Set your monthly target to a percentage of your allotment. At the bottom of the page, you are provided with a more complete explanation of how that percentage is converted in a monthly target volume. It is the product of:

- The **global allotment**: `150GB * number_of_APM_hosts + 50GB * number_of_traced_serverless_invocations (if applicable) + 10GB * number_of_fargate_tasks (if applicable)`
- The **percentage of allotment** configured above
- The **contribution of onboarded services** to the allotment. For example, if the services onboarded to adaptive sampling contribute to 10% of the total ingested volume, Datadog targets 10% of the global allotment. This number increases with the number of services onboarded.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/adaptive_sampling/percentage_based_target_computation.cfb29face854e4f46aa89fb1819f9126.png?auto=format"
   alt="Percentage based target computation" /%}

That monthly target volume is recomputed every 30 minutes.

### Set budget by data volume{% #set-budget-by-data-volume %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/adaptive_sampling/volume_based_target_setting.d5c0b125856d52d6a13bc89e0df569b9.png?auto=format"
   alt="Volume based target setting" /%}

If you are configuring the first service to adaptive sampling, ensure that the ingestion volume target is `>0`. For subsequent services, you should increase the allocated budget after the new service is onboarded to account for the new volume.

{% alert level="info" %}
The configured budget is only allocated to services enrolled in adaptive sampling. It does not include ingested volume from services not enrolled in adaptive sampling, local sampling rules, or other [sampling mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms#in-the-agent) configured locally in the Agent or tracing libraries.
{% /alert %}

## Configure adaptive sampling for a service{% #configure-adaptive-sampling-for-a-service %}

### View sampling rates by resource for a service{% #view-sampling-rates-by-resource-for-a-service %}

Before you configure adaptive sampling for a service, you can view the current ingestion configuration for the service.

To see configured sampling rates:

1. Navigate to the [Ingestion Control](https://app.datadoghq.com/apm/traces/ingestion-control) page.
1. Click a service to view the **Service Ingestion Summary**.
1. View the table listing the applied sampling rates by resource of the service.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/resource_sampling_rates.2d10bd3e1783ea7a9dd770e7be33033e.png?auto=format"
   alt="Sampling rates table by resource" /%}

The table includes:

- **Ingested bytes**: Ingested bytes from spans of the service and resource.
- **Downstream bytes**: Ingested bytes from spans where the sampling decision starts from that service and resource, including downstream services.
- **Configuration**: Source of the resource sampling rate:
  - `AUTOMATIC`: [Default head-based sampling mechanism](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms#in-the-agent) from the Agent.
  - `CONFIGURED LOCAL`: [Sampling rule](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms#in-tracing-libraries-user-defined-rules) set locally in the tracing library.
  - `CONFIGURED REMOTE`: Remote sampling rule set from the Datadog UI.
  - `ADAPTIVE REMOTE`: Adaptive sampling rules set by Datadog.

Once a service is onboarded to adaptive sampling, the sampling rates are adjusted and recomputed every 10 minutes.

### Onboard a service to adaptive sampling{% #onboard-a-service-to-adaptive-sampling %}

To onboard a service to adaptive sampling:

1. Navigate to the [Ingestion Control](https://app.datadoghq.com/apm/traces/ingestion-control) page.
1. Click a service to view the **Service Ingestion Summary**.
1. Click **Manage Ingestion Rate**.
1. Choose **Datadog adaptive sampling rates** as your service's sampling strategy.
1. (Optional) Configure explicit [sampling rates](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls#configure-the-service-ingestion-rates-by-resource) for specific resources, for which you would like to capture more (for example, 100% of `GET /checkout` endpoints) or less (for example, 0.1% of `/health` requests) data.
1. Click **Apply**.

{% alert level="info" %}
If applying this configuration **Remotely** is disabled, ensure the Remote Configuration requirements are met.
{% /alert %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/adaptive_sampling/adaptive_sampling_setting_modal.53a8c1996e1bb7d9893be501c2aa28ae.png?auto=format"
   alt="Adaptive sampling setting modal" /%}

The configuration should take effect in 5-6 minutes, the time it takes for Datadog to observe the service's traffic pattern, compute, then apply the sampling rates. Resources that have been configured remotely display as `Configured Remote` in the **Configuration** column.

## Permissions{% #permissions %}

By default, only users with the `Datadog Admin` role can modify adaptive sampling configurations or onboard services to adaptive sampling.

If your organization uses custom roles, assign your user to a custom role that includes `APM Remote Configuration Write` and `APM Service Ingest Write` [permissions.](https://docs.datadoghq.com/account_management/rbac/permissions/)

### Restrict access{% #restrict-access %}

Use [granular access controls](https://docs.datadoghq.com/account_management/rbac/granular_access/) to manage who can modify a service's adaptive sampling configuration. You can restrict access based on roles, teams, or individual users.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/adaptive_sampling/add_restriction.ba49188a7965891402dd9f341cfd1bad.png?auto=format"
   alt="Restrict permission modal" /%}

To restrict access:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/adaptive_sampling/restrict_service_ingestion_permissions.b714e6676a24412af2eae395d48caea8.png?auto=format"
   alt="Open granular access control modal" /%}

**Note**: Only users with the `remote_config_write` permission can restrict access to the adaptive sampling configuration of individual services.

1. Open the **Permissions** section in the Ingestion Control side panel of the service.

1. Click **Restrict access**.

1. Select the teams, roles, or users to grant access to.

1. Click **Add**.

## Further reading{% #further-reading %}

- [Ingestion Mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms)
- [Ingestion Controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls)
