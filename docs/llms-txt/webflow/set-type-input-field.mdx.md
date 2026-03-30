# Source: https://developers.webflow.com/designer/reference/form-element/set-type-input-field.mdx

***

title: Set input type
slug: reference/form-element/set-type-input-field
description: Sets the type of the input field.
hidden: null
'og:title': Set input type
'og:description': Sets the type of the input field.
---------------------------------------------------

## `formInput.setInputType()`

Sets the HTML type of a FormTextInput field.

Supported element:

* `FormTextInput`

#

### Syntax

```typescript
formInput.setInputType(type: 'text' | 'email' | 'password' | 'tel' | 'number' | 'url'): Promise<null>;
```

### Returns

**A Promise that resolves to `null`**

#

### Example

```typescript
// Get the currently selected element
let formTextInput = await webflow.getSelectedElement();

// Set the input type
await formTextInput.setInputType("email");
```

### Designer ability

| Designer Ability | Locale | Branch | Workflow | Sitemode |
| :--------------- | :----- | :----- | :------- | :------- |
| **canEdit**      | Any    | Any    | Canvas   | Any      |
