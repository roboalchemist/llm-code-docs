# Source: https://developers.webflow.com/designer/reference/dom-element/getAllAttributes.mdx

***

title: Get All Attributes
slug: designer/reference/dom-element/getAllAttributes
description: Retrieve all HTML attributes for the DOMElement.
hidden: false
'og:title': 'Webflow Designer API: DOM Element - getAllAttributes()'
'og:description': Retrieve all HTML attributes for the DOMElement.
------------------------------------------------------------------

## `element.getAllAttributes()`

Retrieve all [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes) for the DOMElement. Use this method instead of the 'Custom Attribute' methods.

## Syntax

```typescript
element.getAllAttributes(): Promise<Array<NamedValue>>
```

## Returns

**Promise\<Array\<*NamedValue*>>** - `[{name: string, value:string }]`

A promise that resolves to an array of, `NamedValue` attribute objects.

## Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement();

if (selectedElement?.type === "DOM") {

  const customAttributes = await selectedElement.getAllAttributes()
  console.log(customAttributes)
}
```

## Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |

```
```
