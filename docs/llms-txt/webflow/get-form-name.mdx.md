# Source: https://developers.webflow.com/designer/reference/form-element/get-form-name.mdx

***

title: Get Form Name
slug: designer/reference/form-element/get-form-name
description: Retrieves the name of the form.
hidden: false
'og:title': 'Webflow Designer API: Get Form Name'
'og:description': Retrieves the name of the form.
-------------------------------------------------

## `FormForm.getName()`

Retrieves the name of the form.

## Syntax

```typescript
form.getName(): Promise<string>
```

## Returns

**Promise\<`name`>**: *String* - The name of the form.

## Example

```typescript
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.type === 'FormForm' || selectedElement?.type === 'FormWrapper'){

  const name = await selectedElement.getName()
  console.log(name)

} else {
  console.log("Selected Element is not a Form Element")
}
```

## Designer Ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |

```
```
