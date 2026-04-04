# Source: https://developers.webflow.com/designer/reference/form-element/set-form-name.mdx

***

title: Set Form Name
slug: designer/reference/form-element/set-form-name
description: Sets the name of the form.
hidden: false
'og:title': 'Webflow Designer API: Form Element - setName()'
'og:description': Sets the name of the form.
--------------------------------------------

## `FormForm.setName(name)`

Sets the name of the form.

## Syntax

```typescript
form.setName(name: string): Promise<null>
```

## Parameters

* `name`: *String* - The name of the form.

## Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

## Example

```typescript
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.type === 'FormForm' || selectedElement?.type === 'FormWrapper'){

  await selectedElement.setName("My Form")

} else {
  console.log("Selected Element is not a Form Element")
}
```

## Designer Ability

| Designer Ability | Locale | Branch | Workflow | Sitemode |
| :--------------- | :----- | :----- | :------- | :------- |
| **canEdit**      | Any    | Any    | canvas   | Any      |

```
```
