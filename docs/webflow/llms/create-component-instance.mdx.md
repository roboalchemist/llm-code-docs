# Source: https://developers.webflow.com/designer/reference/create-component-instance.mdx

***

title: Create a component instance
slug: designer/reference/create-component-instance
description: ''
hidden: false
'og:title': 'Webflow Designer API: Create a component instance'
'og:description': >-
Adding a component instance, also known as a *ComponentElement*, to the canvas
resembles the same process as adding any element to the canvas. Use the
element creation methods in combination with a Component Object to create a
new Component Instance.
-----------------------

Adding a component instance, also known as a *ComponentElement*, to the canvas resembles the same process as adding any element to the canvas. Use the [element creation methods](/designer/reference/insert-element-after) in combination with a Component Object to create a new Component Instance.

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

// Get Component
const allComponents = await webflow.getAllComponents()
const firstComponent = allComponents[0]

// Add Component instance onto a page
await selectedElement?.before(firstComponent)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

***

### Designer Ability

| Designer Ability        | Locale  | Branch | Workflow | SiteMode |
| :---------------------- | :------ | :----- | :------- | :------- |
| **canCreateComponents** | primary | any    | canvas   | any      |
