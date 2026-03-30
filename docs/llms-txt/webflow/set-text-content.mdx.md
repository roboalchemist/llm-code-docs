# Source: https://developers.webflow.com/designer/reference/set-text-content.mdx

***

title: Set Text Content
slug: designer/reference/set-text-content
description: Set text content for an element.
hidden: false
'og:title': 'Webflow Designer API: Set Text Content'
'og:description': Set text content for an element.
--------------------------------------------------

## `element.setTextContent(content)`

Set text content for an element that supports text content.

## Syntax

```typescript
element.setTextContent(content: string): Promise<null>>
```

## Parameters

* **`content`**: `string` - Text to add to the element

## Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

## Example

```typescript
// Get Selected Element
const selectedElement = await Webflow.getSelectedElement()

if (selectedElement?.textContent) {

  // Set and print text content
  const text = await selectedElement.setTextContent("Lorem Ipsum")
  console.log(selectedElement.textContent)

}
```

## Designer Ability

| Designer Ability | Locale | Branch | Workflow | Sitemode |
| :--------------- | :----- | :----- | :------- | :------- |
| **canEdit**      | Any    | Any    | Canvas   | Any      |

```
```
