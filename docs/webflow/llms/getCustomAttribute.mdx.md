# Source: https://developers.webflow.com/designer/reference/custom-attributes/getCustomAttribute.mdx

***

title: Get Custom Attribute
slug: designer/reference/custom-attributes/getCustomAttribute
description: ''
hidden: null
'og:title': 'Webflow Designer API: Get Custom Attribute'
'og:description': ''
--------------------

## `element.getCustomAttribute(name)`

Get [custom HTML attributes](https://university.webflow.com/lesson/custom-attributes?topics=elements) for an element by name.

### Syntax

```typescript
element.getCustomAttribute(name: string):Promise<null | string>
```

### Parameters

* **`name`** :   *String* - The name of the custom attribute.

### Returns

**Promise\<*String*>**

A Promise that resolves to the value of the named custom attribute.

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.customAttributes) {

  // Get Custom Attribute by Name
  const customAttribute = await selectedElement.getCustomAttribute('tooltip')
  console.log(customAttribute)

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
