# Source: https://developers.webflow.com/designer/reference/custom-attributes/removeCustomAttribute.mdx

***

title: Remove Custom Attribute
slug: designer/reference/custom-attributes/removeCustomAttribute
description: ''
hidden: null
'og:title': 'Webflow Designer API: Remove Custom Attribute'
'og:description': ''
--------------------

## `element.removeCustomAttribute(name)`

Remove a [custom HTML attribute](https://university.webflow.com/lesson/custom-attributes?topics=elements) from an element.

### Syntax

```typescript
element.removeCustomAttribute(name: string): Promise<null>
```

### Parameters

* **`name`** :   *String* - The name of the custom attribute.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.customAttributes) {

  // Remove Custom Attribute
  await selectedElement.removeCustomAttribute("tooltip")

}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability | Locale  | Branch | Workflow | Sitemode |
| :--------------- | :------ | :----- | :------- | :------- |
| **canDesign**    | Primary | Main   | Canvas   | Design   |
