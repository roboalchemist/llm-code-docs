# Source: https://developers.webflow.com/designer/reference/form-element/set-required-status.mdx

***

title: Set Required Status
slug: designer/reference/form-element/set-required-status
description: Sets the required status of a form input.
hidden: false
'og:title': 'Webflow Designer API: Form Input - setRequired()'
'og:description': Sets the required status of a form input.
-----------------------------------------------------------

## `formInput.setRequired(value)`

Sets the required status of a form input.

This method is applicable to the following form input types:

* `FormCheckboxInput`
* `FormFileUploadWrapper`
* `FormRadioInput`
* `FormSelect`
* `FormTextarea`
* `FormTextInput`

## Syntax

```typescript
formInput.setRequired(value: boolean): Promise<null>
```

## Parameters

* `value`: *Boolean* - The required status of the form input.

## Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

## Example

```typescript
const selectedElement = await webflow.getSelectedElement()

const formInputTypes = [
  'FormCheckboxInput',
  'FormFileUploadWrapper',
  'FormRadioInput',
  'FormSelect',
  'FormTextarea',
  'FormTextInput'
];

if (selectedElement?.type && formInputTypes.includes(selectedElement.type)) {
  await selectedElement.setRequired(true)

} else {
  console.log("Selected Element is not a Form Input Element")
}
```

## Designer Ability

| Designer Ability | Locale | Branch | Workflow | Sitemode |
| :--------------- | :----- | :----- | :------- | :------- |
| **canEdit**      | Any    | Any    | canvas   | Any      |

```
```
