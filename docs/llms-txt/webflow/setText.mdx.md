# Source: https://developers.webflow.com/designer/reference/string-element/setText.mdx

***

title: Set Text
slug: designer/reference/string-element/setText
description: 'Sets the text value on a String element, overwriting any prior text value.'
hidden: false
'og:title': 'Webflow Designer API: String Element - setText()'
'og:description': 'Sets the text value on a String element, overwriting any prior text value.'
----------------------------------------------------------------------------------------------

## `element.setText(text)`

Sets the text value on a String element, overwriting any prior text value.

## Syntax

```typescript
element.setText(text: string): Promise<null>
```

## Parameters

* text: `string` - The new text for your `StringElement`

## Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

## Example

```typescript
// Get all elements and find the first StringElement
const allElements = await webflow.getAllElements();
const foundElement = allElements.find(el => el.type === "String");

if (foundElement) {
    // Check that element has the method in order to use it
    if ('setText' in foundElement) {
        const elementText = foundElement.setText("Hello Element 🚀"); // Set Text
    }
} else {
    console.log('Element not found on page');
}
```

## Designer Ability

| Designer Ability | Locale | Branch | Workflow | Sitemode |
| :--------------- | :----- | :----- | :------- | :------- |
| **canEdit**      | Any    | Any    | Canvas   | Any      |

```
```
