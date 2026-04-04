# Source: https://developers.webflow.com/designer/reference/custom-attributes/getAllCustomAttributes.mdx

***

title: Get All Custom Attributes
slug: designer/reference/custom-attributes/getAllCustomAttributes
description: ''
hidden: null
'og:title': 'Webflow Designer API: Get All Custom Attributes'
'og:description': ''
--------------------

## **`element.getAllCustomAttributes()`**

Get all [custom HTML attributes](https://university.webflow.com/lesson/custom-attributes?topics=elements) from an element.

### Syntax

```typescript
element.getAllCustomAttributes():Promise<Array<NamedValue>>
```

### Returns

**Promise\<Array\<*NamedValue*>>** - `[{name: string, value: string}]`

A Promise that resolves to an array of *NamedValue*  custom attribute objects.

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.customAttributes) {

  // Get All Custom Attributes
  const customAttributes = await selectedElement.getAllCustomAttributes()
  console.log(customAttributes)

}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
