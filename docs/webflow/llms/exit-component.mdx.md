# Source: https://developers.webflow.com/designer/reference/exit-component.mdx

***

title: Exit out of a component
slug: designer/reference/exit-component
description: ''
hidden: false
'og:title': 'Webflow Designer API: Exit out of a component'
'og:description': >-
Exit the focus of the Designer from a component definition. After exiting out
of a component, the focus of the Designer will return to the `body` of the
page.
-----

## `webflow.exitComponent()`

Exit the focus of the Designer from a component definition. After exiting out of a component, the focus of the Designer will return to the `body` of the page.

### Syntax

```typescript
webflow.exitComponent(): Promise<null>
```

### Returns

**Promise\<`null`>**

A Promise that resolves to `null` when the context switch is successful.

### Example

```typescript
await webflow.exitComponent()
const rootElement = await webflow.getRootElement()
const rootElementType = rootElement?.type

// Print Root Element Type. If element type is Body, the Designer has exited out of the Component context
console.log(`Element Type: ${rootElementType}`)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

***

### Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | any    | any    | any      | any      |
