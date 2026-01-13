# Source: https://docs.datadoghq.com/actions/app_builder/embedded_apps/input_parameters.md

---
title: Input Parameters
description: >-
  Input parameters allow you to embed the same app in multiple dashboards or
  notebooks using different configurations for each instance.
breadcrumbs: Docs > App Builder > Embedded Apps > Input Parameters
source_url: >-
  https://docs.datadoghq.com/app_builder/embedded_apps/input_parameters/index.html
---

# Input Parameters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Input parameters allow you to embed the same app in multiple dashboards or notebooks using different configurations for each instance.

## Example app{% #example-app %}

A common use case for input parameters is to reuse and customize an app for different environments, like dev, staging, and production. In the screenshot below, one app is embedded twice in a dashboard. The app on the left shows monitors in the demo environment, while the app on the right shows the same information for monitors in the staging environment. You can play around with this app by cloning the blueprint [How to: Input Parameters](https://app.datadoghq.com/app-builder/apps/edit?template=how_to_input_parameters&viewMode=templatePreview).

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/embedded_apps/example-input-parameters-dashboard.57fadd48c27cf8707334225f829abaa3.png?auto=format"
   alt="Two embedded apps with different input parameters selected" /%}

## Create an input parameter{% #create-an-input-parameter %}

1. In [App Builder](https://app.datadoghq.com/app-builder/apps/list), select an app and click **Edit**.
1. Click the **App Properties** icon ().
1. Click the plus icon (
   {% icon name="icon-plus-2" /%}
) to add an input parameter.
1. Click the new input parameter to configure its elements:
   - Parameter Name
   - Display Name (Optional)
   - Data Type
   - Allowed Values
   - Default Value
   - Description (Optional)
1. Click **Save**.

### Example input parameter{% #example-input-parameter %}

This example input parameter shows the same app in various staging environments:

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/embedded_apps/example-input-parameters-configuration.7060861ac332728ca8314dbf15ad8b22.png?auto=format"
   alt="An example of configured input parameters inside an app" /%}

## Use input parameters{% #use-input-parameters %}

{% alert level="info" %}
Apps with input parameters work best in dashboards and notebooks. While you can add an app to Self-Service Actions, you can't select the input parameters you've configured.
{% /alert %}

To embed an app with input parameters:

1. In [App Builder](https://app.datadoghq.com/app-builder/apps/list), select an app with a configured input parameter.
1. Click **Add to a dashboard**.
1. Select a dashboard, then click **Save and Open**.
1. In your dashboard, hover over the app and click the **Edit** icon ().
1. In the **Input Parameters** section, select an input parameter:
   {% image
      source="https://datadog-docs.imgix.net/images/service_management/app_builder/embedded_apps/example-input-params-configuring-in-dashboard.d8ef352117b44effa0fa33d3fed17491.png?auto=format"
      alt="An example of an app in editing mode with Input Parameters circled" /%}
1. Click **Save**.

## Reuse an app{% #reuse-an-app %}

After embedding an app in a dashboard or notebook, you can create a copy to reuse it with different contexts:

1. Select the embedded app.
1. Click the **Options** icon (
   {% icon name="icon-kebab-wui" /%}
), then click **Clone**.
   - Alternatively, you can select the app and use copy and paste keyboard shortcuts.
1. Follow the steps [above](https://docs.datadoghq.com/actions/app_builder/embedded_apps/input_parameters/#use-input-parameters) to select a different input parameter.
