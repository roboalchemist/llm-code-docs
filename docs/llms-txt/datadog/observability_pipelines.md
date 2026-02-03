# Source: https://docs.datadoghq.com/cloudprem/ingest/observability_pipelines.md

# Source: https://docs.datadoghq.com/observability_pipelines.md

---
title: Observability Pipelines
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Observability Pipelines
---

# Observability Pipelines

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/observability_pipelines/op_marketecture_06042025.66612c8ba52ee5dd0f0e425d72e09cfb.png?auto=format"
   alt="A graphic showing data being aggregated from a variety of sources, processed and enriched by the observability pipelines worker in your own environment, and then being routed to the security, analytics, and storage destinations of your choice" /%}

Datadog Observability Pipelines allows you to collect and process logs and metrics (Preview (PREVIEW indicates an early access version of a major product or feature that you can opt into before its official release.)) within your own infrastructure, and then route the data to different destinations. It gives you control over your observability data before it leaves your environment.

With out-of-the-box templates, you can build pipelines that redact sensitive data, enrich data, filter out noisy events, and route data to destinations like Datadog, SIEM tools, or cloud storage.

## Key components{% #key-components %}

### Observability Pipelines Worker{% #observability-pipelines-worker %}

The Observability Pipelines Worker runs within your infrastructure to aggregate, process, and route data.

{% alert level="info" %}
Datadog recommends you update Observability Pipelines Worker (OPW) with every minor and patch release, or, at a minimum, monthly.Upgrading to a major OPW version and keeping it updated is the only supported way to get the latest OPW functionality, fixes, and security updates. See [Upgrade the Worker](https://docs.datadoghq.com/observability_pipelines/configuration/install_the_worker/#upgrade-the-worker) to update to the latest Worker version.
{% /alert %}

### Observability Pipelines UI{% #observability-pipelines-ui %}

The Observability Pipelines UI provides a centralized control plane where you can:

- Build and edit pipelines with guided templates.
- Deploy and manage Workers.
- Enable monitors to track pipeline health.

## Get started{% #get-started %}

1. Navigate to [Observability Pipelines](https://app.datadoghq.com/observability-pipelines).
1. Select a template based on your use case.
1. Set up your pipeline:
   1. Choose a log [source](https://docs.datadoghq.com/observability_pipelines/sources/).
   1. Configure [processors](https://docs.datadoghq.com/observability_pipelines/processors/).
   1. Add one or more [destinations](https://docs.datadoghq.com/observability_pipelines/destinations/).
1. [Install the Worker](https://docs.datadoghq.com/observability_pipelines/configuration/install_the_worker/) in your environment
1. Enable monitors for real-time observability into your pipeline health.

See [Set Up Pipelines](https://docs.datadoghq.com/observability_pipelines/configuration/set_up_pipelines/) for detailed instructions.

## Common use cases and templates{% #common-use-cases-and-templates %}

Observability Pipelines includes prebuilt templates for common data routing and transformation workflows. You can fully customize or combine them to meet your needs.

{% image
   source="https://datadog-docs.imgix.net/images/observability_pipelines/eight_templates.be7c19b5e359ab96361497fe1b87862e.png?auto=format"
   alt="The Observability Pipelines UI showing the eight templates" /%}

### Templates{% #templates %}

{% tab title="Logs" %}

| Template                   | Description                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Archive Logs               | Store raw logs in Amazon S3, Google Cloud Storage, or Azure Storage for long-term retention and rehydration. |
| Dual Ship Logs             | Send the same log stream to multiple destinations (for example, Datadog and a SIEM).                         |
| Generate Log-based Metrics | Convert high-volume logs into count or distribution metrics to reduce storage needs.                         |
| Log Enrichment             | Add metadata from reference tables or static mappings for more effective querying.                           |
| Log Volume Control         | Reduce indexed log volume by filtering low-value logs before they're stored.                                 |
| Sensitive Data Redaction   | Detect and remove personally identifiable information (PII) and secrets using built-in or custom rules.      |
| Split Logs                 | Route logs by type (for example, security vs. application) to different tools.                               |

{% /tab %}

{% tab title="Metrics" %}

{% alert level="info" %}
Metric Tag Governance is in Preview. Fill out the [form](https://www.datadoghq.com/product-preview/metrics-ingestion-and-cardinality-control-in-observability-pipelines/) to request access.
{% /alert %}

| Template              | Description                                                                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Metric Tag Governance | Manage the quality and volume of your metrics by keeping only the metrics you need, standardizing metrics tagging, and removing unwanted tags to prevent high cardinality. |

{% /tab %}

See [Explore templates](https://docs.datadoghq.com/observability_pipelines/configuration/explore_templates/) for more information.

## Further Reading{% #further-reading %}

- [Simplify log collection and aggregation for MSSPs with Datadog Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines-mssp)
- [Manage metric volume and tags in your environment with Observability Pipelines](https://www.datadoghq.com/blog/manage-metrics-cost-control-with-observability-pipelines)
- [Set up pipelines](https://docs.datadoghq.com/observability_pipelines/configuration/explore_templates/)
- [Explore use cases and templates](https://docs.datadoghq.com/observability_pipelines/configuration/set_up_pipelines/)
- [Install the Observability Pipelines Worker](https://docs.datadoghq.com/observability_pipelines/configuration/install_the_worker/)
- [Dual shipping with Observability Pipelines](https://docs.datadoghq.com/agent/configuration/dual-shipping/#yaml-configuration)
- [Strategies for Reducing Log Volume](https://docs.datadoghq.com/observability_pipelines/guide/strategies_for_reducing_log_volume/)
- [Redact sensitive data from your logs on-prem by using Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines-sensitive-data-redaction/)
- [Dual ship logs with Datadog Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines-dual-ship-logs/)
- [Control your log volumes with Datadog Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines-log-volume-control/)
- [Archive your logs with Observability Pipelines for a simple and affordable migration to Datadog](https://www.datadoghq.com/blog/observability-pipelines-archiving/)
- [Aggregate, process, and route logs easily with Datadog Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines/)
- [Stream logs in the OCSF format to your preferred security vendors or data lakes with Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines-stream-logs-in-ocsf-format/)
- [Simplify your SIEM migration to Microsoft Sentinel with Datadog Observability Pipelines](https://www.datadoghq.com/blog/observability-pipelines-route-logs-microsoft-sentinel/)
- [How state, local, and education organizations can manage logs flexibly and efficiently using Datadog Observability Pipelines](https://www.datadoghq.com/blog/sled-observability-pipelines/)
- [How to optimize high-volume log data without compromising visibility](https://www.datadoghq.com/blog/optimize-high-volume-logs/)
- [Search your historical logs more efficiently with Datadog Archive Search](https://www.datadoghq.com/blog/archive-search/)
- [Store and search logs at petabyte scale in your own infrastructure with Datadog CloudPrem](https://www.datadoghq.com/blog/introducing-datadog-cloudprem/)
- [Control logging costs on any SIEM or data lake using Packs with Observability Pipelines](https://www.datadoghq.com/blog/manage-high-volume-logs-with-observability-pipeline-packs/)
- [Use OpenTelemetry with Observability Pipelines for vendor-neutral log collection and cost control](https://www.datadoghq.com/blog/observability-pipelines-otel-cost-control/)
