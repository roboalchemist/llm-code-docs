# Source: https://developers.webflow.com/designer/reference/set-div-block-tag.mdx

***

title: Set Div Block element tag
slug: designer/reference/set-div-block-tag
description: ''
hidden: false
'og:title': 'Webflow Designer API: Set Div Block element tag'
'og:description': Set the element tag of a Div Block element
------------------------------------------------------------

## `element.setTag()`

Set the element tag of a Div Block element, which helps assistive technologies and search engines understand the page structure and hierarchy.

### Syntax

```typescript
element.setTag(tag: BlockElementTag): Promise<null>
```

### Parameters

* **tag**:  BlockElementTag - A valid Block element tag, including `div`, `header`, `footer`, `nav`, `main`, `section`, `article`, `aside`, `address`, or `figure`

### Returns

*Promise\<*null*>*

A Promise that resolves to null.

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

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
