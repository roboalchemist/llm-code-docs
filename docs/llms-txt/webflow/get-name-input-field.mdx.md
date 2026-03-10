# Source: https://developers.webflow.com/designer/reference/form-element/get-name-input-field.mdx

***

title: Get input name
slug: reference/form-element/get-name-input-field
description: Retrieves the name of the input field.
hidden: null
'og:title': Get input name
'og:description': Retrieves the name of the input field.
--------------------------------------------------------

## `formInput.getName()`

Retrieves the name of the input field.

This method supports the following `FormInput` elements:

* `FormCheckboxInput`
* `FormFileUploadWrapper`
* `FormRadioInput`
* `FormSelect`
* `FormTextarea`
* `FormTextInput`

#

### Syntax

```typescript
formInput.getName(): Promise<string>;
```

### Returns

**A Promise that resolves to a string**

The name of the input field.

#

### Example

```typescript
// Get the currently selected element
let formInput = await Webflow.getSelectedElement();

// Get the name of the input field
let name = await formInput.getName();

console.log(name);
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
