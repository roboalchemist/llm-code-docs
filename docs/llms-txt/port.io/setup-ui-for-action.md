# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action.md

# Set up frontend

[YouTube video player](https://www.youtube.com/embed/DhDQ_lucdgM)

<br />

After selecting the blueprint you want to add an action to, we need to define the action's frontend - its structure and interface.

This is done in the first two tabs (**Basic Details**, **User Form**) of the action creation form in Port's UI:

![](/img/self-service-actions/setup-frontend/actionFormFrontend.png)

<br />

<br />

Click [here](/actions-and-automations/create-self-service-experiences/.md#action-json-structure) for a reminder of an action's JSON structure.

## Basic details[â](#basic-details "Direct link to Basic details")

Here we will define the action's `title`, `icon`, and `description`.

We will also choose the action's `operation` type:

* **Create** - the action will result in the creation of a new [entity]() in Port by triggering a provisioning process in your infrastructure. Since these actions create a new entity, they are not tied to an existing entity in your software catalog.
* **Delete** - the action will result in the deletion of an existing entity by triggering delete logic in your infrastructure.
* **Day-2** - the action will trigger logic in your infrastructure to update or modify an existing entity in your catalog.

Actions can (but do not have to) be tied to a specific `blueprint`. Selecting a blueprint will allow you to easily execute the action on entities created from that blueprint.

We can also define the execution button's label in the `Action card button text` field.

Button default value

If the `Action card button text` field is left empty, the button label will default to `Create`, `Execute` or `Delete`, according to the chosen `operation` type.

#### Conditions[â](#conditions "Direct link to Conditions")

The `condition` field allows you to define rules using Port's [search & query syntax](/search-and-query/structure-and-syntax.md#rules) to determine which entities the action will be available for.

Requirements

* Since conditions require an existing entity to evaluate, they are only available for actions with `DAY-2` or `DELETE` operations.
* For the same reason, the action must be tied to a blueprint (see above).

The following example shows a condition that will make the action available only for entities with a property named `environment` that has the value `production`:

```
{
  "type": "SEARCH",
  "rules": [
    {
      "operator": "=",
      "property": "environment",
      "value": "production"
    }
  ],
  "combinator": "and"
}
```

Note that the `combinator` field can be set to `and` or `or`, to define how multiple rules should be combined.

#### Limitations[â](#limitations "Direct link to Limitations")

Filtering by a [calculation property](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/calculation-property/.md) that is based on a [mirror property](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/mirror-property.md) is not supported. Such a condition **will not** be evaluated.

## User form[â](#user-form "Direct link to User form")

Port allows you to create a wizard-like experience for your developers by utilizing a variety of input types they will need to fill, while also including input validations.

This is done in the **User Form** tab of the action creation form:

![](/img/self-service-actions/setup-frontend/actionFormUserForm.png)

### Input types[â](#input-types "Direct link to Input types")

Actions can contain a variety of input types, including text fields, dropdowns, numbers, and much more.

See the [user inputs](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/.md) page for more details about the available input types.

### Titles[â](#titles "Direct link to Titles")

Titles can be used to create visual and logical groupings of inputs, by dividing the form into sections.

To add a title, click the `+ Title` button in the form (see the screenshot above).

* When creating a title, you can also provide a `description` to help the user understand each section's purpose. The description will be displayed below the title.
* You can add any number of titles to a form.
* After adding titles and/or inputs, you can reorder them by dragging and dropping.

When a user executes the action, he/she will see the titles and their inputs in the order they were defined:

![](/img/self-service-actions/setup-frontend/actionFormTitleExample.png)

### Steps[â](#steps "Direct link to Steps")

In cases where an action contains a large number of inputs, you may want to break the form into multiple steps. Users executing the action will see and fill each step at a time, which can help guide them through the process and make the action easier to understand.

In the UI, after creating at least one input, a `+ Step` button will appear (see the screenshot above).

Each step can contain multiple inputs, and you can define as many steps as you need.

When a user executes the action, he/she will see the steps and their inputs in the order they were defined:

![](/img/self-service-actions/setup-frontend/actionFormStepsExecution.png)

*After clicking `Next`, the form will move to step 2, requiring the user to fill the inputs defined in that step*

### Advanced configurations[â](#advanced-configurations "Direct link to Advanced configurations")

You can define more advanced forms with dynamic fields that change according to your data or other inputs in the form.<br /><!-- -->See [advanced input configurations](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/advanced-form-configurations.md) for more information and examples.

## Next step[â](#next-step "Direct link to Next step")

Once the frontend is set up, we will move on to the action's [backend configuration](/actions-and-automations/setup-backend/.md).
