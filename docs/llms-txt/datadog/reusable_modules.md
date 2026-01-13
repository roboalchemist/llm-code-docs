# Source: https://docs.datadoghq.com/actions/app_builder/components/reusable_modules.md

---
title: Reusable Modules
description: >-
  Save and reuse groups of components and queries across multiple App Builder
  applications as modular templates.
breadcrumbs: Docs > App Builder > Components > Reusable Modules
source_url: https://docs.datadoghq.com/app_builder/components/reusable_modules/index.html
---

# Reusable Modules

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Use the *Reusable Modules* feature to save groups of components and queries as templates for reuse across your App Builder applications. Modules automatically include all dependencies to ensure your components function correctly.

{% alert level="info" %}
Default modules are read-only. To modify a default module, duplicate it first.
{% /alert %}

## Create a reusable module{% #create-a-reusable-module %}

There are three ways to create a reusable module:

### From the components panel{% #from-the-components-panel %}

1. While editing an app, click the expand icon (
   {% icon name="icon-expand-to-left-wui" /%}
) to open the components panel.
1. Click a component to select it.
1. In the components panel, click the menu icon (
   {% icon name="icon-config-1" /%}
).
1. Click Create Module ().
1. [Configure your module](https://docs.datadoghq.com/actions/app_builder/components/reusable_modules/#configure-a-module).

### From a component's instance name tab{% #from-a-components-instance-name-tab %}

1. While editing an app, select a component on the app canvas.
1. Click the Create Module icon () in the component instance name tab.
1. [Configure your module](https://docs.datadoghq.com/actions/app_builder/components/reusable_modules/#configure-a-module).

### From selected components{% #from-selected-components %}

1. While editing an app, hold down the Shift key and click multiple components to select them.
1. In the side panel that appears on the right, click Create Module ().

## Configure a module{% #configure-a-module %}

When creating your module, the module editor allows you to preview the components and queries, add a name and description, and review dependencies before saving.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/app-builder-reusable-module-preview.eaba6bad57990191363c94ead5542002.png?auto=format"
   alt="Module editor showing preview of components and queries with name and description fields" /%}

1. Enter a name and description.
1. Review the components and queries that are automatically included. The system includes all nested query dependencies.
1. Click Save Module.

## Add a reusable module to an app{% #add-a-reusable-module-to-an-app %}

1. While editing an app, click the Add Component icon (
   {% icon name="icon-component-wui" /%}
).
1. In the Modules section, click a module or drag it onto the app canvas.

## Delete a module{% #delete-a-module %}

1. While editing an app, click the Add Component icon (
   {% icon name="icon-component-wui" /%}
).
1. In the Modules section, click the edit icon () for the module you want to delete.
1. In the module editor, click Delete Module.

## Further reading{% #further-reading %}

- [Components](https://docs.datadoghq.com/service_management/app_builder/components/)
- [Build Apps](https://docs.datadoghq.com/service_management/app_builder/build/)
- [Queries](https://docs.datadoghq.com/service_management/app_builder/queries/)

Do you have questions or feedback? Join the **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
