# Source: https://developers.webflow.com/designer/reference/clear-all-style-properties.mdx

***

title: Remove all style properties
slug: designer/reference/clear-all-style-properties
description: ''
hidden: false
'og:title': 'Webflow Designer API: Remove all style properties'
'og:description': Remove all style properties from a Style.
-----------------------------------------------------------

## **`style.removeAllProperties()`**

Remove all style properties from a Style.

### Syntax

```typescript
style.removeAllProperties(): Promise<void>
```

### Returns

**Promise\<`null`>**

A promise that resolves to `null`

### Example

```typescript
// Retrieve the style by name
const retrievedStyle = await webflow.getStyleByName(styleName);

// Clear Style Properties
await retrievedStyle?.removeAllProperties()
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
