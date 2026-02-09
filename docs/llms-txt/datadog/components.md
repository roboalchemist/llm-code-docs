# Source: https://docs.datadoghq.com/actions/app_builder/components.md

---
title: Components
description: >-
  Comprehensive reference for App Builder UI components including buttons,
  forms, tables, charts, and interactive elements.
breadcrumbs: Docs > App Builder > Components
---

# Components

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

This page provides a list of UI components that you can use when creating apps in App Builder.

Many component properties allow you to select from provided values. If you want to use an expression for a property's value, click **</>** next to the property to use the code editor. For more information on using JavaScript in App Builder, see [JavaScript Expressions](https://docs.datadoghq.com/service_management/app_builder/expressions). For more information about saving your components as a template, see [Reusable Modules](https://docs.datadoghq.com/actions/app_builder/components/reusable_modules/).

{% collapsible-section %}
### Button

Button components have the following properties.

### General{% #general %}

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays on the button.**Value**: string or expression
{% /dd %}

{% /dl %}

### Appearance{% #appearance %}

{% dl %}

{% dt %}
Intent
{% /dt %}

{% dd %}
Controls the color of the button, with colors representing the purpose of the button.**Provided values**: default, danger, success, warning
{% /dd %}

{% dt %}
Is Primary
{% /dt %}

{% dd %}
Designed to call user attention to the most important action(s) for a given page or workflow.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Borderless
{% /dt %}

{% dd %}
Removes the border from any button. On hover, it gets a background fill.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Loading
{% /dt %}

{% dd %}
Shows a loading indicator.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: click
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, open url, download file, set state variable value
{% /dd %}

{% dt %}
State Function
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data %}

Displays property and value pairs in JSON format.

### Example{% #example %}

To view this component in context, see the [Metrics Explorer & Monitors Builder](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=datadog_metrics_and_monitors&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### Callout value

Callout value components have the following properties.

### General{% #general-1 %}

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays at the top of the component.**Value**: string or expression
{% /dd %}

{% dt %}
Value
{% /dt %}

{% dd %}
The value that the callout highlights.**Value**: string or expression
{% /dd %}

{% dt %}
Unit
{% /dt %}

{% dd %}
The unit associated with the value.**Value**: string or expression
{% /dd %}

{% /dl %}

### Style{% #style %}

{% dl %}

{% dt %}
Style
{% /dt %}

{% dd %}
The visual style of the component.**Provided values**: default, success, warning, danger, blue, purple, pink, orange, yellow, red, green, gray, vivid blue, vivid purple, vivid pink, vivid orange, vivid yellow, vivid red, vivid green
{% /dd %}

{% dt %}
Size
{% /dt %}

{% dd %}
Responsively sizes the metric so that it is proportional to the sizing of the value.**Provided values**: sm, md, lg, xl
{% /dd %}

{% /dl %}

### Appearance{% #appearance-1 %}

{% dl %}

{% dt %}
Is Loading
{% /dt %}

{% dd %}
Shows a loading indicator.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Inspect data{% #inspect-data-1 %}

Displays property and value pairs in JSON format.

### Example{% #example-1 %}

To view this component in context, see the [EC2 Instance Manager](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=ec2_instance_manager&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### Checkbox

Checkbox components have the following properties.

### General{% #general-2 %}

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays at the top of the component.**Value**: string or expression
{% /dd %}

{% dt %}
Options
{% /dt %}

{% dd %}
The list of checkboxes that a user can select from. The format is an array of objects where each object consists of a `label` and `value` key-value pair. The minimum number of options is 1.**Value**: expression**Example**:
{% /dd %}

{% dd %}

```json
${[
  {
      "label": "Staging",
      "value": "staging"
  },
  {
      "label": "Production",
      "value": "production"
  }
]}
```

{% /dd %}

{% /dl %}

### Appearance{% #appearance-2 %}

{% dl %}

{% dt %}
Is Multiline
{% /dt %}

{% dd %}
Determines whether the checkbox text should wrap onto a new line or be truncated by an ellipsis.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-1 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: change
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Function
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-2 %}

Displays property and value pairs in JSON format.

### Example{% #example-2 %}

To view this component in context, see the [Metrics Explorer & Monitors Builder](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=datadog_metrics_and_monitors&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### Container

Container components have the following properties.

### Appearance{% #appearance-3 %}

{% dl %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Inspect data{% #inspect-data-3 %}

Displays property and value pairs in JSON format.

### Example{% #example-3 %}

To view this component in context, see the [Metrics Explorer & Monitors Builder](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=datadog_metrics_and_monitors&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### Custom chart

Custom chart components have the following properties.

### General{% #general-3 %}

{% dl %}

{% dt %}
Vega Specification
{% /dt %}

{% dd %}
A string representing a valid Vega-Lite or Vega JSON specification.
{% /dd %}

{% /dl %}

### Appearance{% #appearance-4 %}

{% dl %}

{% dt %}
Is Loading
{% /dt %}

{% dd %}
Shows a loading indicator.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Inspect data{% #inspect-data-4 %}

Displays property and value pairs in JSON format.

### Example{% #example-4 %}

For an example showing how to use this component, see [Custom charts](https://docs.datadoghq.com/service_management/app_builder/components/custom_charts/).
{% /collapsible-section %}

{% collapsible-section %}
### Date range picker

Date range picker components have the following properties.

### General{% #general-4 %}

{% dl %}

{% dt %}
Default timeframe
{% /dt %}

{% dd %}
The default timeframe that the date picker displays.**Provided values**: past 5 minutes, past 30 minutes, past 1 hour, past 4 hours, past 1 day
{% /dd %}

{% /dl %}

### Appearance{% #appearance-5 %}

{% dl %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-2 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: change
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file
{% /dd %}

{% dt %}
State Function
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-5 %}

Displays property and value pairs in JSON format.

### Example{% #example-5 %}

To view this component in context, see the [Metrics Explorer & Monitors Builder](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=datadog_metrics_and_monitors&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### File input

File input components have the following properties.

### General{% #general-5 %}

{% dl %}

{% dt %}
Accepted File Types
{% /dt %}

{% dd %}
Determines which file types the file input component accepts.**Values**: .csv, .json
{% /dd %}

{% /dl %}

### Appearance{% #appearance-6 %}

{% dl %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-3 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: change
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Function
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-6 %}

Displays property and value pairs in JSON format.
{% /collapsible-section %}

{% collapsible-section %}
### Integration logo

Integration logo components have the following properties.

### General{% #general-6 %}

{% dl %}

{% dt %}
Integration Id
{% /dt %}

{% dd %}
Specifies which integration logo icon to display.**Value**: string or expression**Examples**: datadog, amazon-s3, postgres, okta
{% /dd %}

{% /dl %}

### Appearance{% #appearance-7 %}

{% dl %}

{% dt %}
Horizontal Alignment
{% /dt %}

{% dd %}
Controls the horizontal positioning of the logo within the component.**Provided values**: align left, align center, align right
{% /dd %}

{% dt %}
Vertical Alignment
{% /dt %}

{% dd %}
Controls the vertical positioning of the logo within the component.**Provided values**: align top, align center, align bottom
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Loading
{% /dt %}

{% dd %}
Shows a loading indicator.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Inspect data{% #inspect-data-7 %}

Displays property and value pairs in JSON format.
{% /collapsible-section %}

{% collapsible-section %}
### Form

Form components have the following properties.

### General{% #general-7 %}

{% dl %}

{% dt %}
Title
{% /dt %}

{% dd %}
The title of the form.**Value**: string or expression
{% /dd %}

{% dt %}
Default value
{% /dt %}

{% dd %}
The default value that the app populates in the form. To populate a specific field, you can use JSON notation, such as `{"org":"frontend"}` to populate the `org` field with the value `frontend`.**Value**: string or expression
{% /dd %}

{% /dl %}

### Fields{% #fields %}

Each item represents a field in the form. Fields each have one of the following types: `textInput`, `select`, `textArea`, or `text`.

Fields have some or all of the following properties depending on their field type:

{% dl %}

{% dt %}
Field name
{% /dt %}

{% dd %}
The unique identifier for a field. You can use this identifier to reference the field in an expression.**Value**: string or expression
{% /dd %}

{% dt %}
Label
{% /dt %}

{% dd %}
The label that displays above the field.**Value**: string or expression
{% /dd %}

{% dt %}
Content
{% /dt %}

{% dd %}
The content that displays in a `text` field.**Value**: string or expression
{% /dd %}

{% dt %}
Options
{% /dt %}

{% dd %}
The options available in a `select` field. Options must be an array of objects, with a `const` key for the option value and an optional `title` key for the option label.**Value**: Each object's `label` and `value` can be a string or expression.You can populate each object using the GUI (default), or toggle **Raw** to use raw JSON input to provide the entire array of objects.
{% /dd %}

{% dt %}
Placeholder text
{% /dt %}

{% dd %}
The text that displays in a `textInput` or `textArea` field when no value is entered.**Value**: string or expression
{% /dd %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the field is visible in the form.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Required
{% /dt %}

{% dd %}
Determines whether the field is required in order to submit the form.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Appearance{% #appearance-8 %}

{% dl %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-4 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: submit, change, validate
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Function
{% /dt %}

{% dd %}
setValue**Example**: `form0.setValue({name: 'node-group-1'})` sets the value of the `form0` component to `{name: 'node-group-1'}`.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-8 %}

Displays property and value pairs in JSON format.
{% /collapsible-section %}

{% collapsible-section %}
### JSON input

JSON input components have the following properties.

### General{% #general-8 %}

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays at the top of the component.
{% /dd %}

{% dt %}
Default value
{% /dt %}

{% dd %}
The default JSON value that the component displays.
{% /dd %}

{% /dl %}

### Appearance{% #appearance-9 %}

{% dl %}

{% dt %}
Is Read Only
{% /dt %}

{% dd %}
Determines whether the component is read only.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-5 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: change
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Function
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-9 %}

Displays property and value pairs in JSON format.
{% /collapsible-section %}

{% collapsible-section %}
### Modal

Modal components have the following properties.

### General{% #general-9 %}

{% dl %}

{% dt %}
Title
{% /dt %}

{% dd %}
The title of the modal.**Value**: string or expression
{% /dd %}

{% /dl %}

### Appearance{% #appearance-10 %}

{% dl %}

{% dt %}
Size
{% /dt %}

{% dd %}
The scale of the modal.**Provided values**: sm, md, lg
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-6 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Values**: toggleOpen, close, open
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Functions
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% dd %}
setIsOpen**Example**: `modal0.setIsOpen(true)` sets the state of `modal0` to open.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-10 %}

Displays property and value pairs in JSON format.

### Example{% #example-6 %}

To view this component in context, see the [Metrics Explorer & Monitors Builder](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=datadog_metrics_and_monitors&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### Number input

Number input components have the following properties.

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays at the top of the component.**Value**: string or expression
{% /dd %}

{% dt %}
Default value
{% /dt %}

{% dd %}
The default value that the app populates in the input box.**Value**: number or expression that evaluates to a number
{% /dd %}

{% dt %}
Placeholder text
{% /dt %}

{% dd %}
The text that displays when no value is entered.**Value**: string or expression
{% /dd %}

{% /dl %}

### Validation{% #validation %}

{% dl %}

{% dt %}
Min
{% /dt %}

{% dd %}
The minimum value the number input accepts.**Value**: number or expression that evaluates to a number
{% /dd %}

{% dt %}
Max
{% /dt %}

{% dd %}
The maximum value the number input accepts.**Value**: number or expression that evaluates to a number
{% /dd %}

{% /dl %}

### Appearance{% #appearance-11 %}

{% dl %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-7 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: change
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Functions
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% dd %}
setValue**Example**: `numberInput0.setValue(3)` sets the value of the `numberInput0` component to `3`.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-11 %}

Displays property and value pairs in JSON format.

### Example{% #example-7 %}

To view this component in context, see the [ECS Task Manager](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=ecs_task_manager&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### Radio

Radio components have the following properties.

### General{% #general-10 %}

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays at the top of the component.**Value**: string or expression
{% /dd %}

{% dt %}
Options
{% /dt %}

{% dd %}
The list of radio button options that a user can select from. The format is an array of objects where each object consists of a `label` and `value` key-value pair.**Value**: expression**Example**:
{% /dd %}

{% dd %}

```json
${[
  {
      "label": "Staging",
      "value": "staging"
  },
  {
      "label": "Production",
      "value": "production"
  }
]}
```

{% /dd %}

{% dt %}
Default value
{% /dt %}

{% dd %}
The value that is selected when the radio loads.**Value**: string or expression
{% /dd %}

{% /dl %}

### Appearance{% #appearance-12 %}

{% dl %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-8 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: change
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Functions
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% dd %}
setValue**Example**: `radioButtons0.setValue("production")` sets the value of the `radioButtons0` component to `"production"`.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-12 %}

Displays property and value pairs in JSON format.
{% /collapsible-section %}

{% collapsible-section %}
### React renderer

React renderer components have the following properties.

### General{% #general-11 %}

{% dl %}

{% dt %}
React Component Definition
{% /dt %}

{% dd %}
The code that is executed to create a React component.
{% /dd %}

{% dt %}
Component Input Props
{% /dt %}

{% dd %}
The props that are passed to the React component and can be accessed in the props object of the component.
{% /dd %}

{% dt %}
Initial Component State
{% /dt %}

{% dd %}
Sets the initial state values for your component. This state is used when the component first renders or if no state has been set yet. The component can access this data through `props.state`.
{% /dd %}

{% /dl %}

### Appearance{% #appearance-13 %}

{% dl %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-9 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Values**: set component state, callback function
{% /dd %}

{% dt %}
Function Name
{% /dt %}

{% dd %}
**Value**: `props.customFunctionName`
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: close modal, custom, download file, open modal, open side panel, close side panel, set component state, set state variable value, toast notification, trigger action
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-13 %}

Displays property and value pairs in JSON format.

### Relationships{% #relationships %}

Displays data dependencies between React renderer and components in the app.

### Example{% #example-8 %}

For an example showing how to use this component, see [React renderer](https://docs.datadoghq.com/actions/app_builder/components/react_renderer/).
{% /collapsible-section %}

{% collapsible-section %}
### Search

Search components have the following properties.

### General{% #general-12 %}

{% dl %}

{% dt %}
Default value
{% /dt %}

{% dd %}
The default value that the app populates in the search box.**Value**: string or expression
{% /dd %}

{% dt %}
Placeholder text
{% /dt %}

{% dd %}
The text that displays when no value is entered.**Value**: string or expression
{% /dd %}

{% /dl %}

### Appearance{% #appearance-14 %}

{% dl %}

{% dt %}
Size
{% /dt %}

{% dd %}
The scale of the search component.**Provided values**: sm, md, lg
{% /dd %}

{% dt %}
Is Loading
{% /dt %}

{% dd %}
Shows a loading indicator.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-10 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Values**: change, submit
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Functions
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% dd %}
setValue**Example**: `search0.setValue("search query")` sets the value of the `search0` component to `"search query"`.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-14 %}

Displays property and value pairs in JSON format.

### Example{% #example-9 %}

To view this component in context, see the [EC2 Instance Manager](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=ec2_instance_manager&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### Select

Select components have the following properties.

### General{% #general-13 %}

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays at the top of the component.**Value**: string or expression
{% /dd %}

{% dt %}
Placeholder text
{% /dt %}

{% dd %}
The text that displays when no value is entered.**Value**: string or expression
{% /dd %}

{% dt %}
Options
{% /dt %}

{% dd %}
The list of select options that a user can select from. The format is an array of objects where each object consists of a `label` and `value` key-value pair.**Value**: expression**Example**:
{% /dd %}

{% dd %}

```json
${[
  {
      "label": "Staging",
      "value": "staging"
  },
  {
      "label": "Production",
      "value": "production"
  }
]}
```

{% /dd %}

{% dt %}
Default value
{% /dt %}

{% dd %}
The value that is selected when the select loads.**Value**: string or expression
{% /dd %}

{% dt %}
Is Multiselect
{% /dt %}

{% dd %}
Determines whether the user can select more than one option at a time.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Appearance{% #appearance-15 %}

{% dl %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-11 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: change
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Functions
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% dd %}
setValue**Example**: `select0.setValue("staging")` sets the value of the `select0` component to `"staging"`.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-15 %}

Displays property and value pairs in JSON format.

### Example{% #example-10 %}

To view this component in context, see the [Metrics Explorer & Monitors Builder](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=datadog_metrics_and_monitors&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### Tab

Tab components have the following properties.

### Tabs{% #tabs %}

A list of tab views. Use the **+ (plus)** to add additional views.

### Style{% #style-1 %}

{% dl %}

{% dt %}
Style
{% /dt %}

{% dd %}
The coloring style used for the tab component.**Provided values**: Default, purple, pink, orange, red, green
{% /dd %}

{% dt %}
Alignment
{% /dt %}

{% dd %}
The way the tabs are aligned within the tab component.**Provided values**: Horizontal (â), vertical (â)
{% /dd %}

{% dt %}
Impact
{% /dt %}

{% dd %}
Controls whether the selected tab's background is fully colored or only a small band at the bottom is colored.**Provided values**: High, low
{% /dd %}

{% /dl %}

### Appearance{% #appearance-16 %}

{% dl %}

{% dt %}
Hide Tabs
{% /dt %}

{% dd %}
Controls whether the tab markers are displayed.**Provided values**: on, off
{% /dd %}

{% dt %}
Hide Body
{% /dt %}

{% dd %}
Controls whether the body of the tabs are displayed.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-12 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Value**: change
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Functions
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% dd %}
setTabIndex**Example**: `tab0.setTabIndex(0)` sets the value of the `tab0` component to the first tab.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-16 %}

Displays property and value pairs in JSON format.
{% /collapsible-section %}

{% collapsible-section %}
### Table

Table components have the following properties.

### General{% #general-14 %}

{% dl %}

{% dt %}
Title
{% /dt %}

{% dd %}
A title for the table. Select **Markdown** for custom formatting.**Value**: string
{% /dd %}

{% dt %}
Data source
{% /dt %}

{% dd %}
The array of objects to display in a table.**Values**: query, demo data, components
{% /dd %}

{% /dl %}

### Columns{% #columns %}

Each column of data from the data source is represented here and has the following properties:

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays at the top of the column.**Value**: string or expression
{% /dd %}

{% dt %}
Data path
{% /dt %}

{% dd %}
JSON path to access values nested within objects and arrays of a given column.**Value**: string or expression
{% /dd %}

{% dt %}
Formatting
{% /dt %}

{% dd %}
The type of format that the column takes on.**Provided values**: string, link, status pill, date / time, markdown, tags, percent bar, number, score bar, avatar
{% /dd %}

{% dt %}
Sortable
{% /dt %}

{% dd %}
Determines whether the user can sort by the column.
{% /dd %}

{% dt %}
Copyable
{% /dt %}

{% dd %}
Determines whether the user can click to copy the contents of the column.**Provided values**: on, off
{% /dd %}

{% dt %}
Filterable
{% /dt %}

{% dd %}
Determines whether a filter option is available for the column.**Provided values**: on, off
{% /dd %}

{% /dl %}

Some columns have additional properties based on their **Formatting** property.

### Pagination{% #pagination %}

{% dl %}

{% dt %}
Has summary
{% /dt %}

{% dd %}
Determines whether to display a pagination summary directly above the table.**Provided values**: on, off
{% /dd %}

{% dt %}
Page size
{% /dt %}

{% dd %}
Number of rows per page to display.**Value**: number or expression that evaluates to a number
{% /dd %}

{% dt %}
Total count
{% /dt %}

{% dd %}
Total number of rows to display in the table.**Value**: number or expression that evaluates to a number
{% /dd %}

{% dt %}
Type
{% /dt %}

{% dd %}
Determines the type of pagination.**Provided values**: client side, server side
{% /dd %}

{% /dl %}

### Sorting{% #sorting %}

{% dl %}

{% dt %}
Select the column and direction for default table sorting.
{% /dt %}

{% dt %}
Column
{% /dt %}

{% dd %}
The column to sort by.**Value**: column name
{% /dd %}

{% dt %}
Direction
{% /dt %}

{% dd %}
The direction to sort.**Provided values**: ascending, descending
{% /dd %}

{% /dl %}

### Row actions{% #row-actions %}

Adding a row action adds an **Actions** column to the table, which contains user-defined action buttons. Rows can have multiple actions. Actions have the following properties:

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays on the action button.**Value**: string or expression
{% /dd %}

{% dt %}
Primary
{% /dt %}

{% dd %}
Designed to call user attention to the most important action(s) for a given page or workflow.**Provided values**: on, off
{% /dd %}

{% dt %}
Borderless
{% /dt %}

{% dd %}
Removes the border from any button. On hover, it gets a background fill.**Provided values**: on, off
{% /dd %}

{% dt %}
Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Level
{% /dt %}

{% dd %}
Controls the color of the button according to its intent.**Provided values**: default, danger, success, warning
{% /dd %}

{% dt %}
Reactions
{% /dt %}

{% dd %}
The reactions the button triggers. A button can have multiple reactions.**Provided values**: download file, open modal, close modal, open side panel, close side panel, open URL, set component state, set state variable value, toast notification, trigger action, customSome reaction types have additional properties.
{% /dd %}

{% dt %}
State Function
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% /dl %}

### Appearance{% #appearance-17 %}

{% dl %}

{% dt %}
Scrollable
{% /dt %}

{% dd %}
Determines what ways the table is scrollable in.**Provided values**: both, vertical
{% /dd %}

{% dt %}
Is Loading
{% /dt %}

{% dd %}
Shows a loading indicator.**Provided values**: on, off
{% /dd %}

{% dt %}
Has text wrapping
{% /dt %}

{% dd %}
Determines whether cell text wraps.**Provided values**: on, off
{% /dd %}

{% dt %}
Has subrows
{% /dt %}

{% dd %}
Enables subrows for each row. Include the `subRows` property in the data source.**Provided values**: on, off
{% /dd %}

{% dt %}
Is searchable
{% /dt %}

{% dd %}
Determines whether to add a search bar to the table.**Provided values**: on, off
{% /dd %}

{% dt %}
Show sort options
{% /dt %}

{% dd %}
Adds a **Sort** button to the table that gives users sorting options.**Provided values**: on, off
{% /dd %}

{% dt %}
Show column options
{% /dt %}

{% dd %}
Adds a **Columns** button to the table for displaying, hiding, or reorganizing table columns.**Provided values**: on, off
{% /dd %}

{% dt %}
Has date range filter
{% /dt %}

{% dd %}
Adds a date range filter to the table.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-13 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Values**: pageChange, tableRowClick
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: download file, open modal, close modal, open side panel, close side panel, set component state, set state variable value, toast notification, trigger action, custom
{% /dd %}

{% dt %}
State Functions
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% dd %}
setSelectedRow**Examples**:
- `table0.setSelectedRow(0)` sets the `selectedRow` property of `table0` to the first row.
- `table0.setSelectedRow(null)` clears the `selectedRow` property.

{% /dd %}

{% dd %}
setPageIndex**Example**: `table0.setPageIndex(0)` sets the `pageIndex` property of `table0` to the first page.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-17 %}

Displays property and value pairs in JSON format.

### Example{% #example-11 %}

To view this component in context, see the [Metrics Explorer & Monitors Builder](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=datadog_metrics_and_monitors&viewMode=preview) app blueprint.

For examples showing how to use advanced features of tables, see [Tables](https://docs.datadoghq.com/service_management/app_builder/components/tables/).
{% /collapsible-section %}

{% collapsible-section %}
### Text

Text components have the following properties.

### General{% #general-15 %}

{% dl %}

{% dt %}
Content
{% /dt %}

{% dd %}
The content that the component displays.**Value**: string or expression
{% /dd %}

{% dt %}
Content type
{% /dt %}

{% dd %}
Determines how to render the text. When **Markdown** is selected, the text component supports [basic Markdown syntax](https://www.markdownguide.org/basic-syntax/), including images that you host elsewhere.**Provided values**: plain text, Markdown
{% /dd %}

{% /dl %}

### Appearance{% #appearance-18 %}

{% dl %}

{% dt %}
Text alignment
{% /dt %}

{% dd %}
Determines the horizontal alignment of the text within the component.**Provided values**: align left, align center, align right
{% /dd %}

{% dt %}
Vertical alignment
{% /dt %}

{% dd %}
Determines the vertical alignment of the text within the component.**Provided values**: align top, align center, align bottom
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Inspect data{% #inspect-data-18 %}

Displays property and value pairs in JSON format.

### Relationships{% #relationships-1 %}

Displays data dependencies between table data and components in the app.

### Example{% #example-12 %}

To view this component in context, see the [Metrics Explorer & Monitors Builder](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=datadog_metrics_and_monitors&viewMode=preview) app blueprint.
{% /collapsible-section %}

{% collapsible-section %}
### Text area

Text area components have the following properties.

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays at the top of the component.**Value**: string or expression
{% /dd %}

{% dt %}
Default value
{% /dt %}

{% dd %}
The value that is selected when the text area loads.**Value**: string or expression
{% /dd %}

{% dt %}
Placeholder text
{% /dt %}

{% dd %}
The text that displays when no value is entered.**Value**: string or expression
{% /dd %}

{% /dl %}

### Appearance{% #appearance-19 %}

{% dl %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-14 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Values**: change, submit
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Functions
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% dd %}
setValue**Example**: `textArea0.setValue("text")` sets the value of the `textArea0` component to `"text"`.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-19 %}

Displays property and value pairs in JSON format.
{% /collapsible-section %}

{% collapsible-section %}
### Text input

Text input components have the following properties.

{% dl %}

{% dt %}
Label
{% /dt %}

{% dd %}
The text that displays at the top of the component.**Value**: string or expression
{% /dd %}

{% dt %}
Default value
{% /dt %}

{% dd %}
The value that is selected when the text input loads.**Value**: string or expression
{% /dd %}

{% dt %}
Placeholder text
{% /dt %}

{% dd %}
The text that displays when no value is entered.**Value**: string or expression
{% /dd %}

{% /dl %}

### Appearance{% #appearance-20 %}

{% dl %}

{% dt %}
Is Disabled
{% /dt %}

{% dd %}
Applies disabled styling and removes interactions.**Provided values**: on, off
{% /dd %}

{% dt %}
Is Visible
{% /dt %}

{% dd %}
Determines whether the component is visible to the end-user. In edit mode, all components remain visible.**Provided values**: on, off
{% /dd %}

{% /dl %}

### Events{% #events-15 %}

{% dl %}

{% dt %}
Event
{% /dt %}

{% dd %}
**Values**: change, submit
{% /dd %}

{% dt %}
Reaction
{% /dt %}

{% dd %}
**Values**: custom, set component state, trigger query, open modal, close modal, download file, set state variable value
{% /dd %}

{% dt %}
State Functions
{% /dt %}

{% dd %}
fetch**Example**: See [events](https://docs.datadoghq.com/service_management/app_builder/events/#state-functions).
{% /dd %}

{% dd %}
setValue**Example**: `textInput0.setValue("text")` sets the value of the `textInput0` component to `"text"`.
{% /dd %}

{% /dl %}

For more information on events, see [Events](https://docs.datadoghq.com/service_management/app_builder/events).

### Inspect data{% #inspect-data-20 %}

Displays property and value pairs in JSON format.

### Example{% #example-13 %}

To view this component in context, see the [Metrics Explorer & Monitors Builder](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=datadog_metrics_and_monitors&viewMode=preview) app blueprint.
{% /collapsible-section %}

## Further reading{% #further-reading %}

- [Tables](https://docs.datadoghq.com/service_management/app_builder/tables/)
- [Build Apps](https://docs.datadoghq.com/service_management/app_builder/build/)
- [JavaScript Expressions](https://docs.datadoghq.com/service_management/app_builder/expressions/)
- [Build Self-Serve Apps with App Builder for Third-Party Integrations](https://learn.datadoghq.com/courses/app-builder-integration)

Do you have questions or feedback? Join the **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
