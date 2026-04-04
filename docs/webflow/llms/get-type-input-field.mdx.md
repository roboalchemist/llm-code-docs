# Source: https://developers.webflow.com/designer/reference/form-element/get-type-input-field.mdx

***

title: Get input type
slug: reference/form-element/get-type-input-field
description: Retrieves the type of the input field.
hidden: null
'og:title': Get input type
'og:description': Retrieves the type of the input field.
--------------------------------------------------------

## `formInput.getInputType()`

Retrieves the HTML type of a FormTextInput field.

Supported element:

* `FormTextInput`

#

### Syntax

```typescript
formInput.getInputType(): Promise<'text' | 'email' | 'password' | 'tel' | 'number' | 'url' | null>;
```

### Returns

**A Promise resolving to a string or null**

Returns the HTML type of the `FormTextInput` element (`'text'`, `'email'`, etc.). Returns `null` if the type isn't found.

#

### Example

```typescript
// Get the currently selected element
let formTextInput = await webflow.getSelectedElement();

// Get the input type
let type = await formTextInput.getInputType();

console.log(type); // e.g., "email"
```

### Designer ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
