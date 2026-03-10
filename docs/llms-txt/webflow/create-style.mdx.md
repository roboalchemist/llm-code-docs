# Source: https://developers.webflow.com/designer/reference/create-style.mdx

***

title: Create style
slug: designer/reference/create-style
description: ''
hidden: false
'og:title': 'Webflow Designer API: Create style'
'og:description': Create a new Style with a provided name.
----------------------------------------------------------

## **`webflow.createStyle(name, options?)`**

Create a new style with a provided name. Provide a parent style to create a [combo class](https://help.webflow.com/hc/en-us/articles/33961311094419-Classes#how-to-create-a-combo-class).

### Syntax

```typescript
webflow.createStyle(
  name: string,
  options?: {
    parent?: Style
  }
): Promise<Style>
```

### Parameters

* **`name`**: *String* - The name of the style.
* **`options`**: *Object* - An object containing the following properties:
  * **`parent`**: *Style* - A style object that will be the parent of the combo class style.

### Returns

**Promise\<*Style*>**

A Promise that resolves to a Style object.

### Example

```typescript
// Create new style
const newStyle = await webflow.createStyle(styleName);

// Set properties for the style
newStyle.setProperties({
  "background-color": "blue",
  "font-size": "16px",
  "font-weight": "bold",
});

// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.styles) {

  // Apply style to selected element
  await selectedElement.setStyles([newStyle])

} else {
  console.log("No element selected")
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

| Designer ability         | Locale  | Branch | Workflow | Sitemode |
| :----------------------- | :------ | :----- | :------- | :------- |
| **canCreateStyleBlocks** | Primary | Any    | Canvas   | Design   |
