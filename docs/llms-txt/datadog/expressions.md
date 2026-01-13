# Source: https://docs.datadoghq.com/actions/app_builder/expressions.md

---
title: JavaScript Expressions
description: >-
  Use JavaScript expressions in App Builder to create custom interactions
  between components, queries, and app state.
breadcrumbs: Docs > App Builder > JavaScript Expressions
source_url: https://docs.datadoghq.com/app_builder/expressions/index.html
---

# JavaScript Expressions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

You can use JavaScript (JS) expressions anywhere in App Builder to create custom interactions between the different parts of your app. As you begin an expression, App Builder offers autocomplete suggestions based on the existing queries and components in your app. Click on an autocomplete suggestion to use it in your expression, or use the arrow keys on your keyboard and make a selection with the Enter key.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/app-builder-variable.e3625b9c19ca25849962809a5e72e4a8.png?auto=format"
   alt="If you're not sure what to enter as an expression, type ${ to open a suggestion menu with all available expressions" /%}

Some fields, like [post-query transformation](https://docs.datadoghq.com/actions/app_builder/queries/#post-query-transformation), display a code editor by default and accept plain JS. In all other fields, enclose your JS expressions in `${}`. For example, to interpolate the values of two text input components named `textInput0` and `textInput1` into the **Content** property of a text component (and add an exclamation mark), use the expression `${textInput0.value} ${textInput1.value}!`.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/interpolation-2.26ee0e8118c757fbf3cc7d3094befd84.png?auto=format"
   alt="The text component fills with the words 'Hello' and 'World', each interpolated from a text input component value" /%}

App Builder accepts standard vanilla JavaScript syntax, with the following caveats:

- The result of the expression must match the result expected by the component or query property. For example, the text component's **Is Visible** property expects a Boolean. To find out what type of data a component property expects, see View component properties.
- Your code has read-only access to the app state, but App Builder executes the code in a sandboxed environment with no access to the Document Object Model (DOM) or browser APIs.

You can also use Bits AI to work with JS expressions:

1. Click the **Build with AI** icon (**{% icon name="icon-bits-ai" /%}**).
1. Enter a custom prompt, or try the prompt `How can you help me with JavaScript expressions?`.

## View component properties{% #view-component-properties %}

Before you create an expression, it's helpful to know the available properties and defaults or current values for the component you want to interact with.

You can view the available properties and values for a component in the following ways:

- **App State**: Provides properties and values for all components and queries in your app, as well as global variables such as state variables or dashboard template variables.
- **Inspect Data**: Provides properties and values for a specific component or query in your app.
- The **Admin Console**: The **Data** tab of the **Admin Console** provides properties and values for all components and queries in your app.

{% collapsible-section %}
#### App State

To access **App State**:

1. Click **App Properties** in the left side-panel.
1. Scroll down to the **App State** section.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/app-state-2.020616923a0f3aea4033d61d012455a8.png?auto=format"
   alt="The App State section in App Properties" /%}

{% /collapsible-section %}

{% collapsible-section %}
#### Inspect Data

To access **Inspect Data**:

1. Click on the query or component you want to inspect.
1. Scroll down to the **Inspect Data** section.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/inspect-data-2.2d0e4c90115209ea6801d9a896cfca49.png?auto=format"
   alt="The App State section in App Properties" /%}

{% /collapsible-section %}

{% collapsible-section %}
#### Admin Console

To access the **Admin Console**:

1. Click on the cog (**Settings**) icon and select **Admin Console**.
1. Click **Data**.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/admin-console-2.5800b34da36bde6192ab98c7586ad26a.png?auto=format"
   alt="The App State section in App Properties" /%}

{% /collapsible-section %}

## Custom component interactions{% #custom-component-interactions %}

Most UI components provide built-in options, such as toggles and text alignment, that cover basic app usage. To add a custom interaction to a component, click the code editor symbol (**</>**) and enter a JS expression.

### Conditional visibility{% #conditional-visibility %}

You can make the visibility of a component dependent on other components.

For example, if you want a text component to be visible only when two text input components named `textInput0` and `textInput1` have values, use the expression `${textInput0.value && textInput1.value}` in the **Is Visible** property.

### Disable a component conditionally{% #disable-a-component-conditionally %}

Similar to visibility, you can disable a component unless conditions are met by other aspects of your app, such as other components or the app context.

#### Disable a component based on visibility{% #disable-a-component-based-on-visibility %}

If your app has a button that uses the content from a text component to send a message, you can disable the button unless the text component is visible:

1. Click the button component on your canvas.
1. Click the code editor symbol (**</>**) next to the **Is Disabled** property.
1. Add the expression `${!text0.isVisible}`.

The text component is invisible and the button is disabled unless both text input fields have content.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/is-disabled.a1d3095b957d57b785750056bc5039ac.png?auto=format"
   alt="The text component is invisible and the button is disabled unless both text input fields have content." /%}

#### Disable a component based on the app context{% #disable-a-component-based-on-the-app-context %}

You can also disable a component based on the app context, such as the team that the user is on.

For example, you can enable a component only for users who are in the Product Management team:

1. Click the button component on your canvas.
1. Click the code editor symbol (**</>**) next to the **Is Disabled** property.
1. Add the expression `${global.user.teams[0].name == 'Product Management'}`.

### Disable a component while loading{% #disable-a-component-while-loading %}

Another common use case is disabling a component while a query is in a loading state. In the [EC2 Management blueprint](https://app.datadoghq.com/app-builder/apps/edit?viewMode=edit&template=ec2_instance_manager), the `instanceType` select component is disabled while the `listInstances` query is loading. To accomplish this, the **Is Disabled** property uses the expression `${listInstances.isLoading}`.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/app_builder/isloading.428fd849d3d7882b407dc8e07bd78b7b.png?auto=format"
   alt="The 'instanceType' Select component is disabled while the 'listInstances' query is loading." /%}

## Custom query interactions{% #custom-query-interactions %}

Similar to components, you can use JS expressions to alter your queries based on user interaction.

### Filter query results on user input{% #filter-query-results-on-user-input %}

The [PagerDuty On-call Schedules blueprint](https://app.datadoghq.com/app-builder/apps/edit?viewMode=edit&template=pagerduty_oncall_manager) filters the result of the `listSchedules` query based on input from the user. The user selects a team and user from the `team` and `user` select components.

Inside the `listSchedules` query, the following post-query transformation filters the results based on the values of `team` and `user`:

```js
return outputs.body.schedules.map( s => {
    return {
        ...s,
        users: s.users.map(u => u.summary),
        teams: s.teams.map(u => u.summary)
    }
}).filter(s => {

        const matchesName = !name.value.length ? true : s.name.toLowerCase().includes(name.value.toLowerCase());
        const matchesTeam = team.value === 'Any Team' ? true : s.teams.includes(team.value);
        const matchesUser = user.value === 'Any User' ? true : s.users.includes(user.value);

        return matchesName && matchesUser && matchesTeam ;
    }) || []
```

Setting the query's **Run Settings** to **Auto** allows the query to run each time a user changes a value in the `team` or `user` components.

## Further reading{% #further-reading %}

- [Build Apps](https://docs.datadoghq.com/service_management/app_builder/build/)
- [Components](https://docs.datadoghq.com/service_management/app_builder/components/)
