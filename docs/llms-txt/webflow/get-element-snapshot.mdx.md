# Source: https://developers.webflow.com/designer/reference/get-element-snapshot.mdx

***

title: Get element snapshot
slug: designer/reference/get-element-snapshot
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get element snapshot'
'og:description': Capture a snapshot of an element in the Designer.
-------------------------------------------------------------------

## `webflow.getElementSnapshot()`

Captures a snapshot of the specified element.

### Syntax

```typescript
webflow.getElementSnapshot(element: AnyElement): Promise<null | string>
```

### Parameters

| Parameter | Type         | Description                           |
| --------- | ------------ | ------------------------------------- |
| `element` | *AnyElement* | The element to capture a snapshot of. |

### Returns

A Promise that resolves to a [base64](https://developer.mozilla.org/en-US/docs/Glossary/Base64) string representing the snapshot of the element, or `null` if the snapshot could not be captured. The string is a PNG image and includes the `data:image/png;base64,` prefix, making it ready to use directly as an image source.

### Examples

#### Get a snapshot

```typescript
const selectedElement = await webflow.getSelectedElement();

if (selectedElement) {
  const snapshot = await webflow.getElementSnapshot(selectedElement);
  console.log("Snapshot:", snapshot); // base64 string
} else {
  console.log("No element selected");
}
```

#### Render snapshot as an image

```typescript
const selectedElement = await webflow.getSelectedElement();
const img = document.getElementById("snapshot-image") as HTMLImageElement;

if (selectedElement) {
  const snapshot = await webflow.getElementSnapshot(selectedElement);

  if (snapshot) {
    // Get an existing image element and set the base64 string as source
    img.src = snapshot;
  }
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
