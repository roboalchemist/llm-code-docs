# Source: https://developers.webflow.com/designer/reference/dom-element/getTag.mdx

***

title: Get Tag
slug: designer/reference/dom-element/getTag
description: Retrieve the HTML tag of the element.
hidden: false
'og:title': 'Webflow Designer API: DOM Element - getTag()'
'og:description': Retrieve the HTML tag of the element.
-------------------------------------------------------

## `element.getTag()`

Retrieve the [HTML tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) of the element.

## Syntax

```typescript
element.getTag(): Promise<null | string>
```

## Returns

* **Promise\<*String*>** : If the element has a tag, a promise that resolves to the tag value.
* **Promise\<`null`>**: If the element does not have a tag, a promise that resolves to `null`

## Example

```typescript
// Get All Elements and find first DOM Element
const elements = await webflow.getAllElements()
const DOMElement = elements.find(element => element.type === "DOM")

if (DOMElement?.type === "DOM") {

  // Get DOM Element's Tag
  const tag = await DOMElement.getTag()
  console.log(tag)

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
