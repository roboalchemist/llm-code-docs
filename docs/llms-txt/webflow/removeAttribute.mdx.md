# Source: https://developers.webflow.com/designer/reference/dom-element/removeAttribute.mdx

***

title: Remove Attribute
slug: designer/reference/dom-element/removeAttribute
description: Remove the specified HTML attribute from the DOMElement.
hidden: false
'og:title': 'Webflow Designer API: DOM Element - removeAttribute()'
'og:description': Remove the specified HTML attribute from the DOMElement.
--------------------------------------------------------------------------

## `element.removeAttribute(name)`

Remove the specified [HTML attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes) from the DOMElement. Use this method instead of the 'Custom Attribute' methods.

## Syntax

```typescript
element.removeAttribute(name: string): Promise<null>
```

## Parameters

* name : `string` - The name of the attribute to remove

## Returns

**Promise\<`null`>**

A promise that resolves to `null`

## Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement();

if (selectedElement?.type === "DOM") {
  // Get current attributes
  const beforeAttributes = await selectedElement.getAllAttributes();
  console.log('Before removal:', beforeAttributes);

  // Remove an attribute
  await selectedElement.removeAttribute('width');

  // Get attributes after removal to verify
  const afterAttributes = await selectedElement.getAllAttributes();
  console.log('After removal:', afterAttributes);
}
```

## Designer Ability

| Designer Ability | Locale  | Branch | Workflow | Sitemode |
| :--------------- | :------ | :----- | :------- | :------- |
| **canDesign**    | Primary | Main   | Canvas   | Design   |

```
```
