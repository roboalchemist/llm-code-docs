# Source: https://developers.webflow.com/designer/reference/get-asset-name.mdx

***

title: Get Asset Name
slug: designer/reference/get-asset-name
description: ''
hidden: false
-------------

## `asset.getName()`

Retrieve name of specified asset.

### Syntax

```typescript
asset.getName(): Promise<string>
```

### Returns

**Promise\<*string*>**

A Promise that resolves to the name of the Asset

### Example

```typescript
// Get Selected Element
const el = await webflow.getSelectedElement()

// Check if element is selected and its type
if (!el || el.type !== 'Image') {
  console.error('Please select an Image element on the canvas')
  await webflow.notify({
    type: 'Error',
    message: 'Please select an Image element on the canvas',
  })
} else {
  const asset = await el.getAsset() // Get Asset
  const assetName = await asset?.getName() // Get Asset Name
  console.log(`Asset Name: ${assetName}`)
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
| **canAccessAssets** | any    | any    | any      | any      |
