# Source: https://docs.datadoghq.com/security/notifications/variables.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-inclusive/variables.md

# Source: https://docs.datadoghq.com/actions/app_builder/variables.md

---
title: State Variables
description: >-
  Encapsulate logic within apps using state variables to store and manipulate
  data across different app components.
breadcrumbs: Docs > App Builder > State Variables
---

# State Variables

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

If you want to encapsulate logic within your app, you can use state variables.

## Create a state variable{% #create-a-state-variable %}

To add a state variable with Bits AI:

1. Click the **Build with AI** icon (**{% icon name="icon-bits-ai" /%}**).
1. Enter a custom prompt for a variable, or try the prompt `How can you help me with variables?`.

To add a state variable manually:

1. In your app, click the Data (**{ }**) icon to open the Data tab.
1. Click the plus (**+**), then select **Variable**.
1. Optionally, click the variable name and rename it.
1. Define the initial value for your state variable.

## Example app{% #example-app %}

{% video
   url="https://datadog-docs.imgix.net/images/service_management/app_builder/state-variables-example-app.mp4" /%}

To create an app that uses a button to change a callout value component's style and value, follow these instructions.

### Create the variables{% #create-the-variables %}

1. In your app, click the Data (**{ }**) icon to open the Data tab.
1. Click the plus (**+**), then select **Variable**.
1. Name the variable `callout_value` and set its **Initial Value** to `Pass`.
1. Click the plus (**+**) to create another variable.
1. Name this variable `callout_color` and set its **Initial Value** to `green`.

### Create the components{% #create-the-components %}

1. Add a callout value component to your app. Give it the following values:
   - **Value**: `${callout_value.value}`
   - **Style**: `${callout_color.value}`
1. Add a button component to your app and set its label to `Change status`.
1. Under **Events**, add an event. Give it the following values:
   - **Event**: `click`
   - **Reaction**: `custom`
   - **Callback**:
     ```
     ${ () => {
         if(callout_color.value !== "green"){
             callout_color.setValue("green")
             callout_value.setValue("Pass")
         } else {
         callout_color.setValue("red")
         callout_value.setValue("Fail")
         }
     } }
     ```
1. Click **Preview** to preview your app.When you click the **Change status** button in your app, the color and text of the callout value element alternate between a green Pass and a red Fail.

## Further reading{% #further-reading %}

- [Build Apps](https://docs.datadoghq.com/service_management/app_builder/build/)
- [JavaScript Expressions](https://docs.datadoghq.com/service_management/app_builder/expressions/)

Do you have questions or feedback? Join the **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
