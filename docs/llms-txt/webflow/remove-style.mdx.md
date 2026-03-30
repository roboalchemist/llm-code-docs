# Source: https://developers.webflow.com/designer/reference/remove-style.mdx

***

title: Remove style
slug: designer/reference/remove-style
description: ''
hidden: false
-------------

## **`webflow.removeStyle(Style)`**

Remove an unused style from a site. In order to remove the style, it must not be used by any elements throughout the site.

### Syntax

```typescript
webflow.removeStyle(style: Style): Promise<void>
```

### Parameters

* **`Style`**: *StyleObject* - The style to remove.

### Returns

**Promise\<void>**

A Promise that resolves to `undefined`.

### Example

```typescript
// Retrieve the style by name
const retrievedStyle = await webflow.getStyleByName(styleName)

if (retrievedStyle) {

  // Remove Style
  await webflow.removeStyle(retrievedStyle)
  console.log(`Style: ${styleName} was removed`)

} else {
  console.log(`Style ${styleName} not found.`)
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability         | Locale | Branch | Workflow | Sitemode |
| :----------------------- | :----- | :----- | :------- | :------- |
| **canModifyStyleBlocks** | Any    | Any    | Canvas   | Design   |
