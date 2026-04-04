# Source: https://developers.webflow.com/designer/reference/string-element/getText.mdx

***

title: Get Text
slug: designer/reference/string-element/getText
description: Retrieves the text value from a String element.
hidden: false
'og:title': 'Webflow Designer API: String Element - getText()'
'og:description': Retrieves the text value from a String element.
-----------------------------------------------------------------

## `element.getText()`

Retrieves the text value from a String element.

## Syntax

```typescript
element.getText(): Promise<null | string>
```

## Returns

**Promise\<`string`>**

A Promise that always resolves to a *String* value, which is the text content of the string element.

## Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement();

if (selectedElement?.textContent && selectedElement?.children) {

  // Get Child Elements
  const children = await selectedElement.getChildren();

  // Filter string elements from children
  const strings = children.filter(child => child.type === "String");

  // Initialize an array to hold text content
  let textContent = [];

  // Loop over string elements to get text
  for (const myString of strings) {
    if (myString.type === "String") {
      const text = await myString.getText();
      textContent.push(text);
    }
  }

  // Print text
  console.log(textContent);
}
```

## Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |

```
```
