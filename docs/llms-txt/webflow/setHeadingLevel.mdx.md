# Source: https://developers.webflow.com/designer/reference/heading-element/setHeadingLevel.mdx

***

title: Set Heading Level
slug: designer/reference/heading-element/setHeadingLevel
description: Set the heading level of a heading element.
hidden: false
'og:title': 'Webflow Designer API: Heading Element - setHeadingLevel()'
'og:description': Set the heading level of a heading element.
-------------------------------------------------------------

## `element.setHeadingLevel(level)`

Set the heading level of a heading element.

## Syntax

```typescript
element.setHeadingLevel(level: 1 | 2 | 3 | 4 | 5 | 6): Promise<null>
```

## Parameters

* `level`: *Number* - 1 | 2 | 3 | 4 | 5 | 6

## Returns

**Promise\<`null`>**

A Promise that resolves to `null`

## Example

```typescript
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.type === 'Heading'){

  const headingLevel = await selectedElement.setHeadingLevel(1)
  console.log(headingLevel)

} else {
  console.log("Selected Element is not a Heading Element")
}
```

## Designer Ability

| Designer Ability | Locale | Branch | Workflow | Sitemode |
| :--------------- | :----- | :----- | :------- | :------- |
| **canEdit**      | Any    | Any    | Canvas   | Any      |

```
```
