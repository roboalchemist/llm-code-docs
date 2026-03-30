# Source: https://developers.webflow.com/designer/reference/custom-attributes/setCustomAttribute.mdx

***

title: Set Custom Attribute
slug: designer/reference/custom-attributes/setCustomAttribute
description: ''
hidden: null
'og:title': 'Webflow Designer API: Set Custom Attribute'
'og:description': ''
--------------------

## **`element.setCustomAttribute(name, value)`**

Set a [custom HTML attribute](https://university.webflow.com/lesson/custom-attributes?topics=elements) for an element.

### Syntax

```typescript
element.setCustomAttribute(name: string, value: string): Promise<null>
```

### Parameters

* **`name`** :   *String* - The name of the custom attribute.
* **`value`** :   *String* - The value of the custom attribute

The value of the named custom attribute.

### Returns

**Promise\<`null`>**

A promise that resolves to `null`

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.customAttributes) {

  // Set Custom Attribute
  await selectedElement.setCustomAttribute("tooltip", "my tooltip value")

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
