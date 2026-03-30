# Source: https://developers.webflow.com/designer/reference/style/is-combo-class.mdx

***

title: Check if a style is a combo class
slug: designer/reference/style/is-combo-class
description: Check if a style is a combo class
hidden: null
'og:title': Check if a style is a combo class
'og:description': Check if a style is a combo class
---------------------------------------------------

## `style.isComboClass()`

Check if a style is a combo class.

#

### Syntax

```typescript
style.isComboClass(): Promise<boolean>
```

### Returns

**Promise\<boolean>**

A Promise that resolves to a boolean value.

#

### Example

```typescript
// Check if a style is a combo class
const isComboClass = await style.isComboClass()
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
