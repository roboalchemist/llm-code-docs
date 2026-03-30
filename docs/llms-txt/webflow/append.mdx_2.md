# Source: https://developers.webflow.com/designer/reference/element-children/append.mdx

***

title: Append
slug: designer/reference/element-children/append
description: Insert a new element onto the page as the last child of the target element.
hidden: false
'og:title': 'Webflow Designer API: Append'
'og:description': Insert a new element onto the page as the last child of the target element.
---------------------------------------------------------------------------------------------

## `element.append(newElement)`

Insert a new element onto the page as the last child of the target element.

## Syntax

```typescript
element.append(newElement: ElementPreset | Component): Promise<AnyElement>
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

  // Append newElement as a child to of the selected element
  const newElement = await el?.append(webflow.elementPresets.DivBlock)

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
