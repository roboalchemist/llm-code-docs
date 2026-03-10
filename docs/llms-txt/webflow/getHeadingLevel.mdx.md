# Source: https://developers.webflow.com/designer/reference/heading-element/getHeadingLevel.mdx

***

title: Get Heading Level
slug: designer/reference/heading-element/getHeadingLevel
description: Retrieves the heading level of a heading element.
hidden: false
'og:title': 'Webflow Designer API: Heading Element - getHeadingLevel()'
'og:description': Retrieves the heading level of a heading element.
-------------------------------------------------------------------

## `element.getHeadingLevel()`

Retrieves the heading level of a heading element.

## Syntax

```typescript
element.getHeadingLevel(): Promise<null | 1 | 2 | 3 | 4 | 5 | 6>
```

## Returns

**Promise\<`level`>**: *Number* - 1 | 2 | 3 | 4 | 5 | 6

A Promise that resolves to the value of the heading level.

## Example

```typescript
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.type === 'Heading'){

  const headingLevel = await selectedElement.getHeadingLevel()
  console.log(headingLevel)

} else {
  console.log("Selected Element is not a Heading Element")
}
```

## Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |

```
```
