# Source: https://docs.datadoghq.com/actions/app_builder/embedded_apps.md

---
title: Embedded Apps
description: >-
  Embed published apps in dashboards and sync them with template variables and
  time frames for dynamic, contextual actions.
breadcrumbs: Docs > App Builder > Embedded Apps
source_url: https://docs.datadoghq.com/app_builder/embedded_apps/index.html
---

# Embedded Apps

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

When you have Datadog App Builder apps embedded in your dashboards, you can take direct actions on your resources, and all of the relevant data and context is immediately available. Link your app with the dashboard's time frame and template variables to dynamically set the scope of the app's actions, which allows you to carry out actions in your environment at any needed scope.

## Add apps to your dashboard{% #add-apps-to-your-dashboard %}

Add a previously published app to your dashboard by dragging the **App** widget type out of the dashboard's widget tray:

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/embedded_apps/app-widget-select.31104cf857e219eab6c0b36af6c54c39.png?auto=format"
   alt="The dashboard widget tray with the App widget type highlighted" /%}

The App Editor modal appears, allowing you to select an app and provide it with a title:

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/embedded_apps/app-editor.21397dc5dc140c192ff4b65a8a08a1a4.png?auto=format"
   alt="The App Editor modal with an app selected and a widget title" /%}

## Sync your app with dashboard template and time frame variables{% #sync-your-app-with-dashboard-template-and-time-frame-variables %}

You can link your app to template variables anywhere that supports template expressions in your queries or app elements. You can also link your app to the time frame that is selected on your dashboard.

When you change the value of a template variable or time frame on the dashboard, the linked app elements update automatically. For example, when you select an `instance_id` value using the template variable dropdown or directly from a graph, the `instance_id` value is added to the app's filter. This allows you to perform actions on that specific instance:

{% video
   url="https://datadog-docs.imgix.net/images/service_management/app_builder/embedded_apps/template_variables.mp4" /%}

### Template variable examples{% #template-variable-examples %}

To populate a select component with a list of all available template variables, add the following template expression to your select component's **Options** field:

```json
${global?.dashboard?.templateVariables?.map(tvar => tvar.name )}
```

To list all of the available values of a specific template variable, use the following template expression:

```json
${global?.dashboard?.templateVariables?.find(v => v.name === '<TEMPLATE_VARIABLE_NAME>')?.availableValues}
```

To list all of the available values when using a select component, use the following template expression:

```json
${global?.dashboard?.templateVariables?.find(v => v.name === '<TEMPLATE_VARIABLE_NAME>')?.availableValues.map(availableValue => {return {label: availableValue, value:availableValue}})}
```

To get the selected value of a template variable, use the following template expressions:

- For a single-select template variable:
  ```json
  ${global?.dashboard?.templateVariables?.find(v => v.name === '<TEMPLATE_VARIABLE_NAME>')?.value}
```
- For a multi-select template variable:
  ```json
  ${global?.dashboard?.templateVariables?.find(v => v.name === '<TEMPLATE_VARIABLE_NAME>')?.values}
```

### Time frame examples{% #time-frame-examples %}

To get the time frame start value, use the following template expressions:

- For the numerical timestamp:
  ```json
  ${global?.dashboard?.timeframe?.start}
```
- For a formatted date and time:
  ```json
  ${new Date(global?.dashboard?.timeframe?.start).toLocaleString()}
```

To get the time frame end value, use the following template expressions:

- For the numerical timestamp:
  ```json
  ${global?.dashboard?.timeframe?.end}
```
- For a formatted date and time:
  ```json
  ${new Date(global?.dashboard?.timeframe?.end).toLocaleString()}
```

To add a button that sets the value of a date range picker component to the dashboard's time frame, perform the following steps:

1. Add a date range picker component to your app and name it "dateRangePicker0".
1. Add a button to your app.
1. Under **Events**, fill in the following values:
   - **Event**: click
   - **Reaction**: Set Component State
   - **Component**: dateRangePicker0
   - **State Function**: setValue
   - **Value**: `${global?.dashboard?.timeframe}`
1. Save and publish your app.

## Add apps to Software Catalog{% #add-apps-to-software-catalog %}

Add a published app to the [Self-Service Actions](https://app.datadoghq.com/software/self-service) dashboard in [Software Catalog](https://app.datadoghq.com/software) to provide developers with a central place to provision infrastructure, scaffold services, remediate issues, and more.

To add to Self-Service Actions, first ensure your app is published and permissions are defined. Next, you can click **Add to Self-Service Actions**.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/software_catalog/self-service-ui.869c4591bd48c9f46fad9558bc545918.png?auto=format"
   alt="Self-Service Actions" /%}

Once added, you can view and use your app in Software Catalog.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/software_catalog/self-service-publish.85266ae3c6c5af5c2c1085a490f414a4.png?auto=format"
   alt="Publish to Self-Service Actions" /%}

## Further reading{% #further-reading %}

- [Action Catalog](https://app.datadoghq.com/actions/action-catalog/)

Do you have questions or feedback? Join the **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
