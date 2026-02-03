# Source: https://docs.datadoghq.com/account_management/plan_and_usage/usage_details.md

---
title: Usage Details
description: >-
  Monitor your Datadog usage across all products with month-to-date summaries,
  usage trends, top custom metrics, and logs usage by index.
breadcrumbs: Docs > Account Management > Plan and Usage Settings > Usage Details
---

# Usage Details

## Overview{% #overview %}

Administrators can access the [Usage](https://app.datadoghq.com/account/usage/hourly) page by hovering over their username at the bottom left, then navigate to: `Plan & Usage`â> `Usage`.

The Usage page shows usage grouped by product category. You can navigate to a product tab to view usage specific to that product category or the "All" tab to view usage for all products. Each tab provides the following information:

- Month-to-Date Summary
- Overall Usage (current and historical)

Certain product tabs also contain additional tools:

- Custom Metrics Tab: Top Custom Metrics
- Log Management Tab: Logs Usage by Index

## Month-to-date summary{% #month-to-date-summary %}

This section summarizes your month-to-date usage. In the "All" tab, view your month-to-date usage of infrastructure hosts, containers, custom metrics, APM hosts, logs, and any other part of the platform you've used during the month.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/usage-details-v2-01.850f197eb967fc41a20d409e4cff9a8e.png?auto=format"
   alt="Usage Summary - All tab" /%}

In product specific tabs, view your month-to-date usage of the products in that product category.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/usage-details-v2-02.9e4923785bd513fa73cdcfe31d90695f.png?auto=format"
   alt="Usage Summary - Network" /%}

The month-to-date usage shown above is "All" usage, which includes non-billable usage such as product trials. Most accounts are able to view "Billable" usage, which only shows usage that contributes to your final bill. The "Billable" view breaks out your usage by commitments, allotments and on-demand usage.



{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/UsageTilesWithAllPills.c2727734fef5e1b807c4e20056fb4636.png?auto=format"
   alt="Usage Summary - Billable" /%}
For API users, endpoints are available to access ["All"](https://docs.datadoghq.com/api/latest/usage-metering/#get-usage-across-your-multi-org-account) usage and ["Billable"](https://docs.datadoghq.com/api/latest/usage-metering/#get-billable-usage-across-your-account) usage.


Month-to-date usage of each product is calculated as follows:

| Product                  | Description                                                                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Infra. Hosts             | Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current month.                                            |
| Containers               | Shows the high watermark of all distinct containers over all hours in the current month.                                                       |
| APM Hosts                | Shows the 99th percentile of all distinct APM hosts over all hours in the current month.                                                       |
| Profiled Hosts           | Shows the 99th percentile of all distinct profiled hosts over all hours in the current month.                                                  |
| Profiled Containers      | Shows the average of all distinct profiled containers over all hours in the current month.                                                     |
| Custom Metrics           | Shows the average number of distinct [custom metrics](https://docs.datadoghq.com/metrics/custom_metrics/) over all hours in the current month. |
| Ingested Custom Metrics  | Shows the average number of distinct INGESTED custom metrics over all hours in the current month.                                              |
| Ingested Logs            | Shows the sum of all log bytes ingested over all hours in the current month.                                                                   |
| Indexed Logs             | Shows the sum of all log events indexed over all hours in the current month.                                                                   |
| Scanned Logs             | Shows the sum of all log bytes scanned by Sensitive Data Scanner over all hours in the current month.                                          |
| Ingested Spans           | Shows the sum of all spans ingested over all hours in the current month.                                                                       |
| Indexed Spans            | Shows the sum of all Indexed Spans indexed over all hours in the current month.                                                                |
| Analyzed Logs (Security) | Shows the sum of all analyzed log bytes ingested over all hours in the current month.                                                          |
| Serverless Functions     | Shows the average of the number of functions that are executed 1 or more times each hour in the current month.                                 |
| Serverless Invocations   | Shows the sum of all invocations over all hours in the current month.                                                                          |
| Fargate Tasks            | Shows the sum of all Fargate tasks over all hours in the current month.                                                                        |
| Network Hosts            | Shows the 99th percentile of all distinct Network hosts over all hours in the current month.                                                   |
| Network Flows            | Shows the sum of all Network flows indexed over all hours in the current month.                                                                |
| Network Devices          | Shows the 99th percentile of all distinct Network devices over all hours in the current month.                                                 |
| Synthetic API Tests      | Shows the sum of all Synthetic API tests over all hours in the current month.                                                                  |
| Synthetic Browser Tests  | Shows the sum of all Synthetic browser tests over all hours in the current month.                                                              |
| RUM Sessions             | Shows the sum of all distinct RUM sessions over all hours in the current month.                                                                |
| Incident Management      | Shows number of unique active users to date in the selected month who interacted with incident lifecycle and timelines.                        |
| IoT Devices              | Shows the 99th percentile of all distinct IoT devices over all hours in the current month.                                                     |

## Usage trends{% #usage-trends %}

The [Usage Trends](https://app.datadoghq.com/billing/usage) section contains product usage graphs displaying summed usage for all organizations across an account. Usage reports are downloadable through the **Download as CSV** button. For each organization, these reports include an hourly breakdown of usage by product.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/UsageTrendsOverviewAndCSV.511d56eaaef4d2cc465947bc7ddb1e49.png?auto=format"
   alt="Usage Trends graphs page in the Datadog application with Download as CSV option highlighted" /%}

For products with subtypes, each category is distinguished on the graph for that product.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/UsageGraphsByProductTab.1d2ce5741984afb3433ae7af730ca07b.png?auto=format"
   alt="Usage summary with infrastructure tab selected and multiple graphs for infrastructure usage subtypes such as infra hosts, agent hosts, and containers" /%}

More detailed product subtype graphs can be found on each product's tab. For example, a breakdown by host type is available on the Infrastructure tab.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/UsageBreakdownByProductSubtype.18d6eca5e4c9b69e4ffd02c20fe748a9.png?auto=format"
   alt="Usage trends section of the Infrastructure tab with Infra Hosts graph containing Agent hosts and AWS hosts, Indexed Logs graph containing Daily Indexed Live Logs and Cumulative Indexed Live Logs" /%}

Cumulative usage over time is available for sum-based products.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/CumulativeUsageLine.4a9984658876a24c1a5446bb13c9386c.png?auto=format"
   alt="Graphs for Ingested Spans and Indexed Spans, each plotting data for the daily and cumulative sums of their respective spans" /%}

Time selection contains options to view usage graphs at daily, weekly, monthly or yearly intervals.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/TimeGranularity.38b2cde328bc46a429c29547ed8ef5b4.png?auto=format"
   alt="Time intervals on usage graphs" /%}

## Billable on-demand pills and committed lines{% #billable-on-demand-pills-and-committed-lines %}

{% alert level="danger" %}
This feature is in beta. To request access and confirm your organization meets the feature criteria, contact your account representative or [Customer Support](https://docs.datadoghq.com/help/).
{% /alert %}

Purple on-demand pills highlight the portion of billable usage that is on-demand usage. Blue committed and allotted pills highlight the portion of your usage that is covered by commitments and [allotments](https://www.datadoghq.com/pricing/allotments/) from parent products. The dashed `Committed` line shows commitments per product, without any allotments (such as Custom Metrics or Containers).

To display the committed and allotted pills on a card, ensure the **See included usage** toggle is on:

1. On the total usage card where you want to see committed and allotted usage data, click the eye (**See included usage**) icon.
1. The icon changes to an eye with a slash through it. Committed and allotted pills populate on the card.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/UsageTilesWithPillsUsageTrendsWithCommittedLine.b2cba2ac551ae631a74adf655e20c00b.png?auto=format"
   alt="Billable on-demand pills and committed usage lines on trends graphs." /%}

## Top custom metrics{% #top-custom-metrics %}

In the Custom Metrics tab, the Top Custom Metrics table provides two views for your month-to-date usage and most recent day usage, such as usage on the date of the last update.

The "Top 5000" view provides the following information about your Top 5000 custom metrics:

- Metric name
- Average custom metrics per hour
- Max custom metrics per hour
- The metric's contribution percentage to the overall custom metrics usage
- Search for a metric within your top 5000 custom metrics
- This data can be downloaded as a CSV file.

The "All" view provides the following information about all your custom metrics:

- Metric name
- Average custom metrics per hour
- Max custom metrics per hour
- Search for a metric within all your custom metrics
- This data can be downloaded as a CSV file, with a maximum of 300,000 custom metrics. You can download over 300,000 custom metrics using our [API endpoint](https://docs.datadoghq.com/api/latest/usage-metering/#get-all-custom-metrics-by-hourly-average).

For more details on your metrics, navigate to the [Metrics Summary](https://docs.datadoghq.com/metrics/summary/#overview) by hovering over the row of the metric you are interested in and clicking on the meter icon that shows up on the right side.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/usage-metrics-05.b7e289d5fc3e2662140b2e20825c0f57.png?auto=format"
   alt="Overview of Top Custom Metrics table" /%}

## Logs usage by index{% #logs-usage-by-index %}

In the Log Management tab, this table displays your hourly, daily, monthly, and annual indexed log usage by index name and retention period. It also shows the breakdown between live logs and [rehydrated logs](https://docs.datadoghq.com/logs/archives/rehydrating/?tab=awss3#overview). The following information is provided:

- Index name
- Retention period in days
- Indexed log count
- The index's contribution percentage to the overall indexed log usage for the time period selected

This data can be downloaded as a CSV file.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/usage-details-v3-03.28b13d9e2b323de18e4333633c3d119e.png?auto=format"
   alt="Logs Usage by Index" /%}

## First-time usage notifications{% #first-time-usage-notifications %}

{% alert level="danger" %}
This feature is in beta. To request access and confirm your organization meets the feature criteria, contact your account representative or [Customer Support](https://docs.datadoghq.com/help/).
{% /alert %}

The first-time usage notifications feature sends email notifications when there is first-time billable usage for a new product not included in your current contract. Emails are sent approximately 48 hours after the usage first occurs during a given month.

After enabling the feature, a new **Usage Notifications** tab is added to the parent organization's **Plan and Usage** page. On this tab, there is a list of all products covered by the functionality. Unchecking a box stops notifications for that product for all users within the account. If any first-time usage outside of your most recent active contract is detected, users do not receive a notification for any unchecked products.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/plan_and_usage/usage-notifications.f169f46a52ebd037cbb83df024ebe182.png?auto=format"
   alt="First-time usage notifications page with a product list including checked and unchecked items" /%}

Any user with *Usage Notifications Read* or *Write* permissions receives emails. For most organizations, this means any admins.

If your Datadog account is a multi-organization, parent organization users with permissions receive email notifications of usage in child organizations. These emails indicate which child organization generated the usage, and the product which usage was generated for. Child organization users with this permission receive emails for their organization only.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/plan_and_usage/usage-notifications-email.68585b1e024c766941f38cc49e8e4176.png?auto=format"
   alt="First-time usage notifications email with details on sample first-time usage" /%}

## Troubleshooting{% #troubleshooting %}

For technical questions, contact [Datadog support](https://docs.datadoghq.com/help/).

For billing questions, contact your [Customer Success](mailto:success@datadoghq.com) Manager.
