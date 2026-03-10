# Source: https://developers.webflow.com/designer/reference/element-children/prepend.mdx

***

title: Prepend
slug: designer/reference/element-children/prepend
description: Insert a new element onto the page as the first child of the target element.
hidden: false
'og:title': 'Webflow Designer API: Prepend'
'og:description': Insert a new element onto the page as the first child of the target element.
----------------------------------------------------------------------------------------------

## `element.prepend(newElement)`

Insert a new element onto the page as the first child of the target element.

## Syntax

```typescript
element.prepend(newElement: ElementPreset | Component): Promise<AnyElement>
```

## Parameters

* **newElement**:  *Webflow\.elementPresets.\<preset>* - The new element to be inserted into the hierarchy. This element is derived from the `Webflow.elementPresets` object, which contains all Webflow elements that can be inserted onto the canvas.

## Returns

**Promise\<*AnyElement*>**

A Promise that resolves to an `AnyElement` object. `AnyElement` represents the various element types available in a Webflow project. See a full list of supported element types in our [Designer Extension type definitions.](https://www.npmjs.com/package/@webflow/designer-extension-typings?activeTab=code)

## Example

```typescript
// Get Selected Element
const el = await webflow.getSelectedElement();


// Check if element supports child elements
if (el?.children) {

  // Prepend newElement as a child to of the selected element
  const newElement = await el?.prepend(webflow.elementPresets.DivBlock)

  // Print element Details
  console.log(JSON.stringify(newElement))

}
```

## Designer Ability

| Designer Ability | Locale  | Branch | Workflow | Sitemode |
| :--------------- | :------ | :----- | :------- | :------- |
| **canDesign**    | Primary | Main   | Canvas   | Design   |

```
```
