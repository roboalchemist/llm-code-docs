# Source: https://docs.datadoghq.com/cloud_cost_management.md

---
title: Cloud Cost Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloud Cost Management
---

# Cloud Cost Management

{% callout %}
##### Join an enablement webinar session

Explore your cloud provider costs and correlate them with real-time telemetry data. Gain actionable insights and alerts on where your cloud costs are coming from, how they are changing, and where to find potential optimizations.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=Cloud+Cost+Management)
{% /callout %}

## Overview{% #overview %}

Cloud Cost Management provides insights for engineering and finance teams to understand how infrastructure changes impact costs, allocate spend across your organization, and identify inefficiencies.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/summary.f1e80e9fb92cc3428f6023b6f7a71825.png?auto=format"
   alt="Gain insights into all of your cloud provider's cost and usage on the Cloud Costs Summary page in Datadog" /%}

Datadog ingests your cloud cost data and transforms it into metrics you can use in a search query on the [**Explorer** page](https://app.datadoghq.com/cost/explorer). If costs rise, you can correlate the increase with usage metrics to determine the root cause.

## Setup{% #setup %}

- [AWS: Configure Cloud Cost Management for your AWS bill.](https://docs.datadoghq.com/cloud_cost_management/setup/aws)
- [Azure: Configure Cloud Cost Management for your Azure bill.](https://docs.datadoghq.com/cloud_cost_management/setup/azure)
- [Google Cloud: Configure Cloud Cost Management for your Google Cloud bill.](https://docs.datadoghq.com/cloud_cost_management/setup/google_cloud)
- [Oracle: Configure Cloud Cost Management for your Oracle bill.](https://docs.datadoghq.com/cloud_cost_management/setup/oracle)
- [SaaS Cost Integrations: Send cost data from a supported SaaS cost provider to Datadog.](https://docs.datadoghq.com/cloud_cost_management/setup/saas_costs)
- [Custom Costs: Upload any cost data source to Datadog.](https://docs.datadoghq.com/cloud_cost_management/setup/custom)
- [Datadog Costs: Visualize daily Datadog spending and utilization metrics.](https://docs.datadoghq.com/cloud_cost_management/datadog_costs)

## Use cloud cost data{% #use-cloud-cost-data %}

Visualize infrastructure spend alongside related utilization metrics with a retention period of 15 months to spot potential inefficiencies and savings opportunities.

When creating a dashboard, select **Cloud Cost** as the data source for your search query.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/cloud_cost_data_source-1.de6b5d382de539e89c12bd5f831ef09c.png?auto=format"
   alt="Cloud Cost available as a data source in dashboard widget creation" /%}

Optionally, you can programmatically export a timeseries graph of your cloud cost data by using the [Metrics API](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-data-across-multiple-products).

## Use daily Datadog cost data{% #use-daily-datadog-cost-data %}

Visualize daily Datadog spending alongside related utilization metrics with a retention period of 15 months to spot potential inefficiencies and savings opportunities. Learn more about [Datadog Costs](https://docs.datadoghq.com/cloud_cost_management/datadog_costs).

When creating a dashboard, select **Cloud Cost** as the data source, then choose **Datadog** from the available cost types.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/datadog_costs/dashboard-updated.4803d2a3fc6bed063dae69dee4679170.png?auto=format"
   alt="Datadog costs as an option for the Cloud Cost data source in a dashboard" /%}

Optionally, you can programmatically export a timeseries graph of your Datadog cost data by using the [Metrics API](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-data-across-multiple-products).

## Tagging and cost allocation{% #tagging-and-cost-allocation %}

Learn how tags are sourced, enriched, and managed in Cloud Cost Management by reading the [Tags documentation](https://docs.datadoghq.com/cloud_cost_management/tags/).

You can create tag rules to correct missing or incorrect tags, and add inferred tags that align with your organization's business logic.

## Create a cost monitor{% #create-a-cost-monitor %}

Proactively manage and optimize your cloud spending by creating a [Cloud Cost Monitor](https://docs.datadoghq.com/monitors/types/cloud_cost/). You can choose **Cost Changes** or **Cost Threshold** to monitor your cloud expenses.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/monitor.b44149e163ba2f0e629d90c5f4753cd1.png?auto=format"
   alt="Create a Cloud Cost monitor that alerts on cost changes" /%}

## Allocate costs{% #allocate-costs %}

Use [Container Cost Allocation metrics](https://docs.datadoghq.com/cloud_cost_management/container_cost_allocation) to discover costs associated with clusters and workloads across Kubernetes, Amazon ECS, Azure, and Google Cloud. You can gain visibility into pod-level costs, identify idle resource costs, and analyze costs by resource type.

## Permissions{% #permissions %}

Two permissions are available:

1. Cloud Cost Management Read (`cloud_cost_management_read`)
1. Cloud Cost Management Write (`cloud_cost_management_write`)

The table below describes the impact of these permissions in both Cloud Cost Management and related pages.

| Page/Functionality                            | Cloud Cost Management Read Permission       | Cloud Cost Management Write Permission            |
| --------------------------------------------- | ------------------------------------------- | ------------------------------------------------- |
| CCM Summary Page                              | Permission Required                         | N/A                                               |
| CCM Containers Page                           | Permission Required                         | N/A                                               |
| CCM Recommendations Page                      | Permission Required                         | N/A                                               |
| CCM Explorer Page                             | Permission Required                         | N/A                                               |
| CCM Plan Page                                 | Permission Required                         | Permission Required to modify or create Budgets   |
| CCM Settings Page - Custom Costs              | Permission Required                         | Permission Required to upload custom costs        |
| CCM Settings Page - Tag Pipelines             | Permission Required                         | Permission Required to create tag pipelines       |
| CCM Settings Page - SaaS Integrations         | Permission Required                         | Permission Required to enable integration for CCM |
| CCM Settings Page - Accounts                  | Permission Required                         | Permission Required to modify or create accounts  |
| CCM Settings Page - Configure Recommendations | Permission Required                         | Permission Required to customize recommendations  |
| Dashboards/Notebooks (external)               | Permission Required to create and view data | N/A                                               |
| Monitors (external)                           | Permission Required to create CCM monitors  | N/A                                               |
| Service Catalog (external)                    | Permission Required to view cost data       | N/A                                               |
| Resource Catalog (external)                   | Permission Required to view cost data       | N/A                                               |
| API Queries for Cost Data                     | Permission Required                         | N/A                                               |

### Data access control preview{% #data-access-control-preview %}

More granular tag-level restrictions are available as part of the [Data Access Control Preview](https://docs.datadoghq.com/account_management/rbac/data_access/). To request preview access, fill out [this form](https://www.datadoghq.com/product-preview/data-access-control/).

## Review data history{% #review-data-history %}

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/ccm-data-history.254be773f82db02f1931dabf6293c06d.png?auto=format"
   alt="View your Cloud Cost data history in Cloud Cost settings." /%}

Monitor the freshness and processing status of your cloud cost data on the **Cloud Cost > Settings > Data History** page.

- **Last Bill Received**: When your cloud or SaaS provider generated the billing data visible in CCM.
- **Last Processed**: When Datadog last processed billing data from your cloud provider, including:
  - Tag pipeline rules (retroactively processes up to 3 months of historical data by default)
  - Cost allocation rules (retroactively processes up to 1 month of historical data by default)

Use this page to troubleshoot data delays or confirm that recent tag pipelines and cost allocation changes have taken effect.

## Further reading{% #further-reading %}

- [Gain visibility and control of your cloud spend with Datadog Cloud Cost Management](https://www.datadoghq.com/blog/control-your-cloud-spend-with-datadog-cloud-cost-management/)
- [Driving AI ROI: How Datadog connects cost, performance, and infrastructure so you can scale responsibly](https://www.datadoghq.com/blog/manage-ai-cost-and-performance-with-datadog/)
- [Understand your Kubernetes and ECS spend with Datadog Cloud Cost Management](https://www.datadoghq.com/blog/cloud-cost-management-container-support/)
- [Empower engineers to take ownership of Google Cloud costs with Datadog](https://www.datadoghq.com/blog/google-cloud-cost-management/)
- [Quickly and comprehensively analyze the cloud and SaaS costs behind your services](https://www.datadoghq.com/blog/total-cost-of-service-ownership-ccm/)
- [Create a Cloud Cost monitor](https://docs.datadoghq.com/monitors/types/cloud_cost/)
- [Learn about Tags in Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/tags/)
- [Key learnings from the State of Cloud Costs study](https://www.datadoghq.com/blog/cloud-costs-study-learnings/)
- [Monitor unit economics with Datadog Cloud Cost Management](https://www.datadoghq.com/blog/unit-economics-ccm/)
- [How we've created a successful FinOps practice at Datadog](https://www.datadoghq.com/blog/finops-at-datadog/)
- [How we saved $1.5 million per year with Cloud Cost Management](https://www.datadoghq.com/blog/cloud-cost-management-saved-millions/)
- [Manage and optimize your OCI costs with Datadog Cloud Cost Management](https://www.datadoghq.com/blog/cloud-cost-management-oci/)
- [How Cambia Health Solutions saved $30,000 monthly with Cloud Cost Management and the Datadog Resource Catalog](https://www.datadoghq.com/blog/cambia-health-cost-optimization)
