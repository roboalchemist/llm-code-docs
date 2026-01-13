# Source: https://docs.datadoghq.com/cloud_cost_management/recommendations/custom_recommendations.md

---
title: Custom Recommendations
description: >-
  Learn how to customize and manage custom recommendations to fit your business
  needs.
breadcrumbs: >-
  Docs > Cloud Cost Management > Cloud Cost Recommendations > Custom
  Recommendations
source_url: https://docs.datadoghq.com/recommendations/custom_recommendations/index.html
---

# Custom Recommendations

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/recommendations/custom-recommendations-without-history.72ab7445f06024a9feb296f253e96a54.png?auto=format"
   alt="Configure custom recommendations from the Cloud Cost Settings page." /%}

[CCM Recommendations](https://docs.datadoghq.com/cloud_cost_management/recommendations/) are designed to be informative and actionable from the start. You can customize these recommendations to fit your specific business use cases and needs. Set your own metric thresholds and evaluation time frames to reduce unnecessary alerts and focus on the recommendations that matter most.

With custom recommendations, you can:

- Configure multiple rules for any default recommendation
- View the history and changes made to your configurations
- Modify, restore, or delete previously set rules

## Customize a recommendation{% #customize-a-recommendation %}

{% alert level="danger" %}
To customize a recommendation, you must be assigned the **Cloud Cost Management - Cloud Cost Management Write** permission.
{% /alert %}

{% alert level="info" %}
Customizations reflect within 24 hours, when recommendations are generated next.
{% /alert %}

To access custom recommendations, go to [**Cloud Cost > Settings > Configure Recommendations**](https://app.datadoghq.com/cost/settings/configure-recommendations).

On this page, you can see a list of out-of-the-box recommendations that can be customized.

Click a recommendation, then click **Create New Configuration** to get started.

### Step 1: Set custom metric thresholds{% #step-1-set-custom-metric-thresholds %}

You can set a value for each metric threshold used to generate resource recommendations.

Metric thresholds that cannot be customized appear grayed out.

### Step 2: Customize the evaluation time frame{% #step-2-customize-the-evaluation-time-frame %}

Adjust the evaluation time frame to match your business's seasonality or operational patterns. Options include: 1 week, 2 weeks, 15 days, 3 weeks, 1 month, 2 months, and 3 months.

### Step 3: Apply this rule to all resources or add a filter{% #step-3-apply-this-rule-to-all-resources-or-add-a-filter %}

You can select whether to apply the rule to **All Resources** or **Some Resources** in your environment.

If you select **Some Resources**, you can filter resources by tag (for example, `team`, `service`, or `environment`) to target specific parts of your business.

### Step 4: (optional) Label and document the customization{% #step-4-optional-label-and-document-the-customization %}

Use this step to add a reason and unique name to your configuration so you can audit and reference this recommendation later.

- **Reason:** Provide a reason for your customization to support future audits and maintain a clear record of changes.
- **Name:** Enter a descriptive name for the configuration to identify and locate this recommendation in the future.

### Step 5: Save the recommendation{% #step-5-save-the-recommendation %}

Click **Save** to save your customized recommendation. Recommendations that have already been customized **once** are labeled **Configured**.

## Updating custom recommendations{% #updating-custom-recommendations %}

You can update a custom recommendation at any time to reflect changes in your business needs.

To update a custom recommendation:

1. Navigate to [**Cloud Cost > Settings > Configure Recommendations**](https://app.datadoghq.com/cost/settings/configure-recommendations).
1. Go to the customized recommendation.
1. Modify the parameters as needed.
1. Click **Save**.
1. In the confirmation popup, click **Yes, save custom parameters** to apply your changes.

## Further reading{% #further-reading %}

- [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/)
- [Cloud Cost Recommendations](https://docs.datadoghq.com/cloud_cost_management/recommendations)
