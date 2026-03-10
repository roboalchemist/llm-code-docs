# Source: https://developers.webflow.com/designer/reference/resize-extension.mdx

***

title: Resize the extension
slug: designer/reference/resize-extension
description: ''
hidden: false
'og:title': 'Webflow Designer API: Resize the current extension'
'og:description': Set the desired size of the Extension UI.
-----------------------------------------------------------

## `webflow.setExtensionSize(size)`

Set the desired size of the Extension UI.

Need more room in your app for certain tasks? You can easily make your Designer Extension bigger. But remember, bigger isn't always better. Make it large only when you really need additional surface area and then go back to a smaller size. This way, your users can work smoothly with your app and the Designer at the same time.

### Syntax

```typescript
webflow.setExtensionSize(
  size: 'default' | 'comfortable' | 'large' | {width: number; height: number}
): Promise<null>
```

### Parameters

**size**: *"default"* | *"comfortable"* | *"large"* | `{height: number, width: number}`

The desired size for the Extension UI.  The three available sizes are:

* **Default:** 240px by 360px
  Great for simple apps that don't require much real estate
* **Comfortable:** 320px by 460px
  For apps like form submissions that may require a bit more room
* **Large:** 800px by 600px
  For apps that require in-depth work flows, previews, or in depth control

If passing an object to create a custom size, please note the following size limits.

* **min:** 240x360
* **max:** 1200x800

### Returns

**Promise\<`null`>**

A Promise that resolves to `null` when the size is set.

### Example

```typescript
// Set the desired size for the extension UI
const newSize = "large"; // You can change this to "default," "comfortable," or provide { width, height }

// Set the Extension UI size
await webflow.setExtensionSize(newSize);

console.log(`Extension UI size set to: ${newSize}`);
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>
