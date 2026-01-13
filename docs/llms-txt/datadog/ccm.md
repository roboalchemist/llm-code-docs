# Source: https://docs.datadoghq.com/datadog_cloudcraft/overlays/ccm.md

---
title: Cloud Cost Management
description: >-
  Use the Cloud Cost Management overlay in Cloudcraft to view resource-level
  costs and discover savings opportunities directly on your architecture
  diagrams.
breadcrumbs: Docs > Cloudcraft in Datadog > Overlays > Cloud Cost Management
source_url: https://docs.datadoghq.com/overlays/ccm/index.html
---

# Cloud Cost Management

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

The Cloud Cost overlay helps you visualize resource-level costs and identify savings opportunities within your AWS architecture diagrams. This overlay provides two views: **Cost** and **Recommendations**.

## Cost view{% #cost-view %}

The Cost view shows resource-level cloud costs from the past 30 days, allowing you to understand spending patterns across your architecture.

### Filter by cost{% #filter-by-cost %}

Use the slider filter at the bottom of the screen to set a cost range. The diagram updates dynamically to highlight resources within your selected range.

You can also filter by region to focus on specific parts of your infrastructure.

### Resource details{% #resource-details %}

Click a resource to open the side panel, which displays:

- Cost breakdown for the last 30 days
- Tag information associated with the resource
- **Top Cost Changes** section (when applicable) highlighting significant cost fluctuations

**Note**: The time range defaults to the last 30 days and is not configurable.

{% image
   source="https://datadog-docs.imgix.net/images/datadog_cloudcraft/overlays/cloudcraft_ccm_cost_view.a6945ccd744e41b4d55178b14925598d.png?auto=format"
   alt="Cloud Cost Management overlay in Cloudcraft showing the Cost view with resource-level costs." /%}

## Recommendations view{% #recommendations-view %}

The Recommendations view shows savings opportunities directly on resources with estimated monthly savings (for example, terminate unused RDS instances, migrate storage classes).

Use the filter at the bottom of the screen to narrow recommendations by:

- Potential monthly savings range
- Recommendation type: **Terminate**, **Migrate**, **Downsize**, or **Purchase**

### Resource details{% #resource-details-1 %}

Clicking a resource opens a detailed side panel with:

- Current and projected monthly costs
- A description of recommended changes
- Quick actions to create a Jira issue or support case
- Metrics and usage patterns explaining the recommendation

This enables faster, in-context cost optimization without switching views.

{% image
   source="https://datadog-docs.imgix.net/images/datadog_cloudcraft/overlays/cloudcraft_ccm_overlay_5.7b14774da802c75caee5e131452ffc02.png?auto=format"
   alt="Cloud Cost Management overlay in Cloudcraft showing the Recommendations view with savings opportunities highlighted." /%}

## Further reading{% #further-reading %}

- [Infrastructure overlay](https://docs.datadoghq.com/datadog_cloudcraft/overlays/infrastructure/)
- [Observability overlay](https://docs.datadoghq.com/datadog_cloudcraft/overlays/observability/)
- [Security overlay](https://docs.datadoghq.com/datadog_cloudcraft/overlays/security/)
- [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/)
