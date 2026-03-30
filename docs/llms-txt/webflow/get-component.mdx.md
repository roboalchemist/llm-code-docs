# Source: https://developers.webflow.com/designer/reference/get-component.mdx

***

title: Get component
slug: designer/reference/get-component
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get component'
'og:description': Get the Component Definition that is associated to a Component Instance
-----------------------------------------------------------------------------------------

## **`ComponentElement.getComponent()`**

Get the Component Definition associated to a Component Instance

### Syntax

```typescript
element.getComponent(): Promise<Component>
```

### Returns

**Promise\<*Component*>**

A promise that resolves to a Component Object associated with a Component Instance.

```typescript
//Get User Selected Element from the Designer
const parent = await webflow.getSelectedElement();

// Check if this selected element is a Component Instance
if(parent && !parent.configurable && parent.type === 'ComponentInstance'){
      console.log(await parent.getComponent().getName());
    }
```

### Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | any    | any    | any      | any      |
