# Source: https://developers.webflow.com/designer/reference/get-div-block-tag.mdx

***

title: Get Div Block element tag
slug: designer/reference/get-div-block-tag
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get Div Block element tag'
'og:description': Get the element tag of a Div Block element
------------------------------------------------------------

## `element.getTag()`

Retrieve the element tag of a Div Block element.

### Syntax

```typescript
element.getTag(): Promise<null | BlockElementTag>
```

### Returns

*Promise\<`null` | `BlockElementTag`>*

A Promise that resolves to one of the following:

* `BlockElementTag`: The Block element tag, including `div`, `header`, `footer`, `nav`, `main`, `section`, `article`, `aside`, `address`, or `figure`
* `null`: If the element is not found or the Block element tag is not set

### Example

```typescript
// Get a Div Block element
const el = await webflow.getSelectedElement();

// Set its element tag to main
if (el.type === 'Block') {
  // Get the current element tag
  const elementTag = await el.getTag();
  if (elementTag !== 'main') {
    // Set the element tag
    await el.setTag('main');
  }
}
```

### Designer Ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | An       |
