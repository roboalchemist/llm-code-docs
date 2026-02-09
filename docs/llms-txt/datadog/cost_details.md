# Source: https://docs.datadoghq.com/account_management/plan_and_usage/cost_details.md

---
title: Cost Details
description: >-
  Track Datadog costs with cost summaries and chargebacks, including projected
  monthly costs, historical data, and multi-organization cost allocation.
breadcrumbs: Docs > Account Management > Plan and Usage Settings > Cost Details
---

# Cost Details

## Overview{% #overview %}

Cost Summary and Cost Chargebacks help you understand your estimated month-to-date, projected end-of-month, and historical Datadog costs. Cost data is available for the past 15 months.

You can break down your costs by sub-organization and by product to:

- Allocate costs according to their source
- Gain insight into how costs are tracking

For visibility into daily Datadog spending in Cloud Cost Explorer, dashboards, and [cost monitors](https://docs.datadoghq.com/cloud_cost_management/cost_changes/monitors/?tab=costmetricbased), see [Datadog Costs](https://docs.datadoghq.com/cloud_cost_management/datadog_costs/) under Cloud Cost Management.

### Permissions{% #permissions %}

Roles with Billing Read (`billing_read`) and Usage Read (`usage_read`) [permissions](https://docs.datadoghq.com/account_management/rbac/) can view the Cost Summary and Cost Chargebacks data. Users with the Datadog Admin role have these permissions by default.

## Cost summary{% #cost-summary %}

Use the cost summary to:

- View estimated month-to-date and projected end-of-month costs
- View historical costs
- Filter and group costs by product or sub-organization
- View month-over-month % and $ cost changes
- View cost trends within the month
- View cumulative day-over-day costs

### Projected Costs (parent organization){% #projected-costs-parent-organization %}

Projected end-of-month costs are calculated by applying the prior and current month's projected usage data against your contracted rates. Projected end-of-month costs are updated daily and may change over time, depending on your usage throughout the month. Because the costs are a prediction, the amount may differ from your finalized monthly cost.

### Cost Summary (parent organization){% #cost-summary-parent-organization %}

The cost summary functionality changes according to your Datadog usage as a single organization or a multi-organization. As a multi-organization, you can view estimated, projected, and historical costs for the parent organization and each sub-organization.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/plan_and_usage/multiorg-current-month-historical-costs.3d69c6cb2d509b34da380c434e891eca.png?auto=format"
   alt="Screenshot of the current month's Cost Summary for a parent organization, showing the overall month-to-date cost, projected cost, a graph with cumulative cost breakdowns, and a summary table including month-over-month cost changes." /%}

View historical costs by toggling back to previous months, or use the date dropdown to view costs over 1, 3, 6 or 12 months.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/plan_and_usage/parent-org-multi-month-cost-changes.9581a213047012b6ac7f91c97a49f4b0.png?auto=format"
   alt="Screenshot of a parent organization's historical costs over a three month period, showing the overall cost for the month, a graph with cumulative cost breakdowns, and a summary table including month-over-month cost changes." /%}

1. While logged in to the parent organization, navigate to [Plan & Usage](https://app.datadoghq.com/billing/usage).
1. Click the **Usage** tab.
1. For a multi-organization, ensure the **Overall** tab is selected.

#### View and filter{% #view-and-filter %}

Use the search facets at the left to filter the cost by **Products**, **Sub-Orgs** or **Cost Breakdown**. Use the Daily Cost tab to see how the cumulative day-over-day costs have changed within the current month.

#### Download{% #download %}

To download the data as a comma separated value file, click **Download as CSV**. Data is available for the current month and pre-defined prior months. Use the `Cost Type` field to distinguish between the records:

- **Projected**: Data is available for the current month.
- **Estimated MTD**: Data is available from the first of the month to the current date. If historical cost data is not yet available for the prior month, estimated cost data also displays for the prior month.
- **Historical**: Data is available after month close, which is approximately 16 days after the end of the month.

To query estimated cost data through the API, see [Get estimated cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-estimated-cost-across-your-account). To query projected cost data through the API, see [Get projected cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-projected-cost-across-your-account).

### Cost Summary (sub-organization){% #cost-summary-sub-organization %}

{% alert level="danger" %}
This feature is in limited availability. To request access and confirm your organization meets the feature criteria, contact your account representative or [Customer Support](https://docs.datadoghq.com/help/).
{% /alert %}

As a sub-organization, you can view the costs for your organization only. This restriction allows for more distributed ownership and removes the need to grant broader Admin permissions to the parent organization.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/plan_and_usage/suborg-cost-trends.93afc5678e4cd6017ba6c73eb0708723.png?auto=format"
   alt="Screenshot of the current month's Cost Summary for a sub-organization, showing the overall month-to-date cost, projected cost, a graph with cumulative cost breakdowns, and a summary table including month-over-month cost changes." /%}

View historical costs by toggling back to previous months, or use the date dropdown to view costs over 1,3, 6 or 12 months.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/plan_and_usage/suborg-multi-month-cost-changes.15abad4530ba4ef9657e891c1eb6f7e7.png?auto=format"
   alt="Screenshot of a sub organization's historical costs over a six month period, showing the overall cost for the month, a graph with cumulative cost breakdowns, and a summary table including month-over-month cost changes." /%}

1. While logged in to the sub-organization, navigate to [Plan & Usage](https://app.datadoghq.com/billing/usage).
1. Click the **Usage** tab.
1. Ensure the **Overall** tab is selected.

#### View and filter{% #view-and-filter-1 %}

Use the search facets at the left to filter the cost by **Products** or **Cost Breakdown**. Use the **Daily Cost** tab to see how the cumulative day-over-day costs have changed within the current month.

#### Download{% #download-1 %}

To download the data as a comma separated value file, click **Download as CSV**.

## Cost chargebacks{% #cost-chargebacks %}

Use the cost chargebacks to:

- View estimated month-to-date and historical costs for multi-organizations
- Attribute costs to each sub-organization

Cost chargebacks are derived by:

- Calculating the sub-organization usage ratio. This is done by dividing usage per sub-organization by the total parent organization usage.
- Applying the sub-organization usage ratio against the parent organization costs, providing the cost chargebacks per sub-organization.

### Historical cost chargebacks{% #historical-cost-chargebacks %}

From a parent organization, view finalized historical costs aggregated by product and sub-organization.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/plan_and_usage/historical-cost-chargebacks.170dbf6d4463e2089590870132f7a15b.png?auto=format"
   alt="Screenshot of a table titled 'Usage and Cost Summary', showing total usage in dollars for four sub-organizations and the total cost." /%}

1. While logged in to the parent organization, navigate to [Plan & Usage](https://app.datadoghq.com/billing/usage).
1. Select the **Usage** tab.
1. Click **Individual Organizations**.
1. Ensure the **Billable** and **Cost** toggles are selected.
1. Use the date selector to view a prior month for which billing has completed.

**Note**: Data is available after month close, which is approximately 16 days after the end of the month.

### Estimated cost chargebacks{% #estimated-cost-chargebacks %}

From a parent organization, view estimated costs aggregated by product and sub-organization.

Estimated cost data is available for the current month. If historical cost data is not yet available for the prior month, estimated cost data also displays for the prior month.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/plan_and_usage/estimated-cost-chargebacks.9daf2584d7fa0223179b20bf8e630117.png?auto=format"
   alt="Screenshot of a table titled 'Usage and Cost Summary', showing total usage in dollars for four sub-organizations and the total cost." /%}

1. While logged in to the parent organization, navigate to [Plan & Usage](https://app.datadoghq.com/billing/usage).
1. Select the **Usage** tab.
1. Click **Individual Organizations**.
1. Ensure the **Billable** and **Cost** toggles are selected.
1. Ensure the date selector shows the current or prior month.

### Download{% #download-2 %}

- To download historical or estimated cost chargeback data as a comma separated value file, click **Download as CSV**.
- See [Get historical cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-historical-cost-across-your-account) to query historical cost chargeback data through the API.
- See [Get estimated cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-estimated-cost-across-your-account) to query estimated cost chargeback data through the API.

## How billing aggregations affect cost changes{% #how-billing-aggregations-affect-cost-changes %}

Your estimated month-to-date Datadog bill varies throughout the month. The type of aggregation used to bill each product determines how the costs are impacted. For the best visualization, see the [cost summary](https://docs.datadoghq.com/account_management/plan_and_usage/cost_details/#cost-summary) feature chart. Each **Products** filter includes the relevant billing aggregation method next to the product name.

### Percentile and average usage billing{% #percentile-and-average-usage-billing %}

Products billed by the maximum count (high-water mark) of the lower 99 percent of usage for the month include infrastructure hosts and APM hosts. Products billed by the average over the month include custom metrics and Fargate tasks. For these two types of products, expect their costs to remain relatively stable throughout the month. However, they are still subject to cost changes if there is a significant spike or drop in usage.

### Sum of usage billing{% #sum-of-usage-billing %}

Products billed by the sum of usage throughout the month include indexed logs and ingested logs. For these types of products, expect their costs to increase or decrease based on changes to usage volume.

## Further reading{% #further-reading %}

- [Billing](https://docs.datadoghq.com/account_management/billing/)
- [Usage details](https://docs.datadoghq.com/account_management/billing/usage_details/)
- [Managing multiple-organization accounts](https://docs.datadoghq.com/account_management/multi_organization/)
