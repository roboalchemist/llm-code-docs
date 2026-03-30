# Source: https://developers.webflow.com/designer/reference/forms.mdx

***

title: Forms
slug: designer/reference/forms
description: Learn how to create and manage forms with the Designer API.
hidden: false
'og:title': 'Webflow Designer API: Form Element'
'og:description': Learn how to create and manage forms with the Designer API.
-----------------------------------------------------------------------------

Webflow Forms enable users to capture and collect information from visitors on a site.

## Creating a form

<div>
  <div>
    Use the `FormForm` [element preset](/designer/reference/element-presets) to create a form.

    <CodeBlocks>
      ```javascript
      // Get the currently selected element
      let el = await Webflow.getSelectedElement();

      // Create a form element
      let form = await el.after(webflow.elementPresets.FormForm);

      ```
    </CodeBlocks>

    When you create a form using the `FormForm` preset, it automatically generates a complete [form structure](#form-structure) with default form fields, as well as a success and error message.
  </div>

  <div>
    <Frame>
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/45b5e84f6c1581d2b6acb9531d5355689eda82ff445e762e1acc3cfe7bc38cab/products/designer/pages/Elements/element-methods/form-element/assets/FormForm.png" alt="Form Element Preset" />
    </Frame>
  </div>
</div>

## Form structure

A Webflow form consists of several nested elements that work together:

| Element              | Description                                                                 | Parent Element |
| -------------------- | --------------------------------------------------------------------------- | -------------- |
| `FormWrapper`        | The outermost container element that encapsulates the entire form structure |                |
| `FormForm`           | The main form element containing all form fields and inputs                 | `FormWrapper`  |
| `FormSuccessMessage` | The success message after successful form submission                        | `FormWrapper`  |
| `FormErrorMessage`   | The error message if form submission fails                                  | `FormWrapper`  |
| `FormInput`          | An individual form field.                                                   |                |
| `FormBlockLabel`     | The label for a `FormInput`                                                 | `FormInput`    |
| `FormButton`         | The submit button for the form                                              | `FormForm`     |

## Form inputs

Form inputs are the individual fields that collect user information. It's recommended to create a wrapper to contain each input and it's corresponding [label](#form-labels).

You can create form inputs using the following element presets:

* `FormTextInput`
* `FormTextarea`
* `FormSelect`
* `FormCheckboxInput`
* `FormRadioInput`

It's a best practice to wrap each input and its corresponding label (e.g. `FormBlockLabel`) in a container element, such as a `DivBlock`, to keep them organized.

**Example**

<CodeBlocks>
  ```javascript title="Inline"
  // Get the currently selected element
  let el = await Webflow.getSelectedElement();

  // Create a form element
  let formWrapper = await el.after(webflow.elementPresets.FormForm);

  // Add a text input with a label
  let formWrapperChildren = await formWrapper.getChildren(); // Get the form element
  let formInputs = formWrapperChildren[0]; // Get the form element
  let inputWrapper = await formInputs.append(webflow.elementPresets.DOMElement); // Create a wrapper for the input and label
  let label = await inputWrapper.append(webflow.elementPresets.FormBlockLabel); // Create a label
  let input = await inputWrapper.append(webflow.elementPresets.FormTextInput); // Create a text input

  ```
</CodeBlocks>

### Form labels

Each input should have a label that describes the information it collects. Create a label using the `FormBlockLabel` element preset to label each input.

## Methods

### Form element methods

<Note>
  The methods documented below apply specifically to the `FormForm` and
  `FormWrapper` elements.
</Note>

The Form Element supports the following specific methods:

<CardGroup>
  <Card title="Get form name" href="/designer/reference/form-element/get-form-name">
    Retrieves the name of the form.
  </Card>

  <Card title="Set form name" href="/designer/reference/form-element/set-form-name">
    Sets the name of the form.
  </Card>

  <Card title="Get form settings" href="/designer/reference/form-element/get-form-settings">
    Retrieves the settings of the form.
  </Card>

  <Card title="Set form settings" href="/designer/reference/form-element/set-form-settings">
    Sets the settings of the form.
  </Card>
</CardGroup>

### Form input methods

The following methods apply to form input elements:

<CardGroup>
  <Card title="Get required status" href="/designer/reference/form-element/get-required-status">
    Retrieves the required status of a form input.
  </Card>

  <Card title="Set required status" href="/designer/reference/form-element/set-required-status">
    Sets the required status of a form input.
  </Card>

  <Card title="Get input name" href="/designer/reference/form-element/get-name-input-field">
    Retrieves the name of the input field.
  </Card>

  <Card title="Set input name" href="/designer/reference/form-element/set-name-input-field">
    Sets the name of the input field.
  </Card>

  <Card title="Get input type" href="/designer/reference/form-element/get-type-input-field">
    Retrieves the type of the input field.

    <span>
      Only supported by `FormTextInput`.
    </span>
  </Card>

  <Card title="Set input type" href="/designer/reference/form-element/set-type-input-field">
    Sets the type of the input field.

    <span>
      Only supported by `FormTextInput`.
    </span>
  </Card>
</CardGroup>

{" "}

## Properties

| Property           | Description                                             | Type      | Example                                                 |
| ------------------ | ------------------------------------------------------- | --------- | ------------------------------------------------------- |
| `id`               | The unique identifier for the form.                     | `object`  | `{component: "64c813...", element: "5edf8e59-71f9..."}` |
| `type`             | The type of the element.                                | `string`  | `"FormForm" \|\| "FormWrapper`                          |
| `children`         | Indicates if the element can contain child elements.    | `boolean` | `true`                                                  |
| `customAttributes` | Indicates if the element can contain custom attributes. | `boolean` | `true`                                                  |
| `styles`           | Indicates if the element can contain styles.            | `boolean` | `true`                                                  |
| `textContent`      | Indicates if the element can contain text content.      | `boolean` | `false`                                                 |
| `appConnections`   | Indicates if the element can contain app connections.   | `boolean` | `true`                                                  |
