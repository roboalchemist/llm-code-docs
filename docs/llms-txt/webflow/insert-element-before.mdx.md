# Source: https://developers.webflow.com/designer/reference/insert-element-before.mdx

***

title: Insert element before target element
slug: designer/reference/insert-element-before
description: ''
hidden: false
'og:title': 'Webflow Designer API: Insert a new element before target element.'
'og:description': Insert a new element onto the page before the target element.
-------------------------------------------------------------------------------

## `element.before(newElement)`

Insert a new element onto the page before the target element.

### Syntax

```typescript
element.before(newElement: ElementPreset | Component): Promise<AnyElement>
```

### Parameters

* **newElement**:  *webflow\.elementPresets.\<preset>* - The new element to be inserted into the hierarchy. This element is derived from the `webflow.elementPresets` object, which contains all Webflow elements that can be inserted onto the canvas.

### Returns

**Promise\<*AnyElement*>**

A Promise that resolves to an `AnyElement` object.

`AnyElement` represents the various element types available in a Webflow project. See a full list of supported element types in our [Designer Extension type definitions.](https://www.npmjs.com/package/@webflow/designer-extension-typings?activeTab=code)

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

if (selectedElement) {

  // Insert DIV before selected Element
  const newDiv = await selectedElement.before(webflow.elementPresets.DivBlock)

  // Print element details
  console.log(`${JSON.stringify(newDiv)}`)

}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### App Mode

| Designer Ability | Locale  | Branch | Workflow | Sitemode |
| :--------------- | :------ | :----- | :------- | :------- |
| **canDesign**    | Primary | Main   | Canvas   | Design   |
