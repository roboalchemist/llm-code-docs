# Source: https://docs.datadoghq.com/cloud_cost_management/cost_changes/anomalies.md

---
title: Anomalies Page
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloud Cost Management > Cost Changes > Anomalies Page
source_url: https://docs.datadoghq.com/cost_changes/anomalies/index.html
---

# Anomalies Page

## Overview{% #overview %}

Datadog Cloud Cost Management (CCM) continuously monitors your environment to detect and prioritize unexpected cost changes, enabling you to share, investigate, and resolve anomalies. Cost anomalies are available for AWS, Azure, and Google Cloud and do not require any additional setup after CCM is set up.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/anomalies/anomalies-overview.230db47877c2df3e2dbd2fb2a6a7cc86.png?auto=format"
   alt="List of cost anomalies showing service names, usage types, and cost impacts" /%}

A typical workflow could be the following:

1. **View** anomalies on the Anomalies tab
1. **Investigate** using Watchdog Explains to understand what's driving the cost changes
1. **Share with engineering teams** who can take action by reviewing details, investigating further, or setting up monitoring
1. **Resolve** anomalies that are expected or not significant

## How anomalies are defined{% #how-anomalies-are-defined %}

Anomalies are significant, unexpected changes that stand out from typical patterns. Datadog automatically identifies anomalies using machine learning techniques that adapt to your specific usage patterns.

To distinguish between true anomalies and expected fluctuations, Datadog's algorithm:

- Recognizes recurring cost spikes and dips, such as a cost increase every Monday, or a spike on the fourth day of every month
- Focuses on engineering usage (excludes taxes, credits, refunds, and Reserved Instance fees)
- Filters out low-impact anomalies to reduce noise

## View cost anomalies{% #view-cost-anomalies %}

On the [Anomalies tab of the Cloud Cost page in Datadog](https://app.datadoghq.com/cost/analyze/anomalies), you can view and filter anomalies:

- **Active**: Anomalies from the last full day of cost data (typically 2-3 days prior).
- **Past**: Anomalies that lasted more than 7 days or are no longer detected as anomalous. Past anomalies can be useful to report on, but are often less urgent and actionable.
- **Resolved**: Anomalies that you've marked as resolved with context.

Each anomaly card shows:

- Service name (`rds`, for example)
- Usage type
- Cloud accounts affected
- Expected vs. actual costs
- Cost trend graph (past 1 month)

Anomalies are sorted by cost impact, with the most significant changes at the top.

## Investigate anomalies{% #investigate-anomalies %}

### Understand what drives anomalies{% #understand-what-drives-anomalies %}

CCM automatically uses [Watchdog Explains](https://docs.datadoghq.com/dashboards/graph_insights/watchdog_explains), an investigation assistant, to help you identify what is driving cost anomalies. Watchdog Explains analyzes and identifies the specific:

- accounts
- teams
- services
- Kubernetes or ECS clusters
- regions

where the anomaly happened, reducing manual investigation steps. When hovering over the anomaly graph, you can see two graphs: one with and one without the tags identified by Watchdog Explains. This shows how removing specific tags flattens the spike, confirming the impact on the cost.

### Take action on anomalies{% #take-action-on-anomalies %}

Follow these steps to investigate and resolve anomalies:

1. **Hover** over an anomaly to see anomaly drivers or click **See more** to open the side panel.

   {% image
      source="https://datadog-docs.imgix.net/images/cloud_cost/anomalies/anomalies-watchdog.dc0b0ad8bf363d61d686babc70d5257d.png?auto=format"
      alt="Click See More to see side panel showing anomaly details, investigation options, and action buttons" /%}

1. **Review the details** for services affected, teams involved, environments impacted, resource IDs, or how usage and unit price may be driving the cost anomaly.

1. **Investigate further**: View the anomaly in Cost Explorer or a Datadog Notebook to further investigate anomalies by using additional dimensions. You can then send the anomaly, Explorer link, or Notebook to the service owners or teams identified by Watchdog Explains. This enables teams to resolve anomalies with context for why the anomaly occurred and whether it's expected.

   {% image
      source="https://datadog-docs.imgix.net/images/cloud_cost/anomalies/anomalies-take-action.66d505880e948fb39de5274ab70cdc50.png?auto=format"
      alt="Click Take Action to view the anomaly in Cost Explorer or add it to a Notebook" /%}

1. **Set up monitoring**: Create a cost anomaly monitor for similar patterns or configure alerts for future anomalies.

   {% image
      source="https://datadog-docs.imgix.net/images/cloud_cost/anomalies/anomalies-create-monitor.6e71fc1c6231144ff7aeee3cd8702754.png?auto=format"
      alt="Create a cost anomaly monitor" /%}

## Resolve anomalies{% #resolve-anomalies %}

As you investigate anomalies, you may find some that are not significant, were actually expected costs, or are otherwise not considered anomalies.

To resolve an anomaly:

1. Click **Resolve Anomaly** to open the resolution popup.
1. Select one of the following resolutions to help improve the algorithm:
   - The anomaly amount was too small
   - This is an unexpected increase
   - This is an expected increase
1. **Add context** about why it is or is not an anomaly.
1. Click **Resolve** to move it to the Resolved tab.

This is an example of how to mark a cost anomaly as significant and explain why it's an anomaly:

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/anomalies/cost_anomalies_side-panel_is-unexpected-1.cc10adc5f817985122393cee41d1ceea.png?auto=format"
   alt="Form for marking an anomaly as unexpected with explanation field" /%}

## Troubleshooting{% #troubleshooting %}

If you're not seeing expected anomalies:

- Verify that CCM is [properly set up](https://docs.datadoghq.com/cloud_cost_management/setup/)
- Check that you have the necessary permissions for AWS, Azure, or Google Cloud
- Review the time range of your anomaly view

For more help, contact [Datadog Support](https://docs.datadoghq.com/help/).

## Further reading{% #further-reading %}

- [Learn about Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/)
- [Create Cost Monitors](https://docs.datadoghq.com/cloud_cost_management/cost_changes/monitors)
