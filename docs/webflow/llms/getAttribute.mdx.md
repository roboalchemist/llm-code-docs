# Source: https://developers.webflow.com/designer/reference/dom-element/getAttribute.mdx

***

title: Get Attribute
slug: designer/reference/dom-element/getAttribute
description: Retrieve the value of the named HTML attribute of the DOMElement.
hidden: false
'og:title': 'Webflow Designer API: DOM Element - getAttribute()'
'og:description': Retrieve the value of the named HTML attribute of the DOMElement.
-----------------------------------------------------------------------------------

## `element.getAttribute(name)`

Retrieve the value of the named [HTML attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes) of the DOMElement. Use this method instead of the 'Custom Attribute' methods.

## Syntax

```typescript
element.getAttribute(name: string): Promise<null | string>
```

## Parameters

* name : `string` - The name of the attribute

## Returns

* **Promise\<*String*>**:  A promise that resolves to the value of the named HTML attribute for the DOMElement.
* **Promise\<`null`>**: If the attribute doesn't exist, this method will return `null`.

## Example

```typescript
// Get All Elements and find first DOM Element
const elements = await webflow.getAllElements()
const DOMElement = elements.find(element => element.type === "DOM")

if (DOMElement?.type === "DOM") {

  // Get DOM Element's Attribute by Name
  const attribute = await DOMElement.getAttribute("MyAttribute")
  console.log(attribute)

} else {
  console.log('No DOM Element Found')
}
```

## Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |

```
```
