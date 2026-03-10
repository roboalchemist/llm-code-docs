# Source: https://developers.webflow.com/designer/reference/component-element/getComponent.mdx

***

title: Get Component
slug: designer/reference/component-element/getComponent
description: Retrieves the associated component of the element.
hidden: false
'og:title': 'Webflow Designer API: Component Element - getComponent()'
'og:description': Retrieves the associated component definition of the component instance.
------------------------------------------------------------------------------------------

## `element.getComponent()`

Retrieves the associated [component definition](/designer/reference/components-overview#component-definition) of the component instance.

## Syntax

```typescript
element.getComponent(): Promise<Component>
```

## Returns

**Promise\<*Component*>**

A Promise that resolves to a [Component Object](/designer/reference/components-overview)

## Example

```typescript
// Select Component Element on Page
const elements = await webflow.getAllElements()
const componentInstance = elements.find(el => el.type === 'ComponentInstance')

if (componentInstance?.type === "ComponentInstance") {

  // Get Component object from instance
  const component = await componentInstance?.getComponent()
  const componentName = await component.getName()
  console.log(componentName)
} else {
  console.log("No component element found")
}
```

## Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |

```
```
