# Source: https://developers.webflow.com/designer/reference/get-asset-by-id.mdx

***

title: Get Asset by ID
slug: designer/reference/get-asset-by-id
description: ''
hidden: false
-------------

## `webflow.getAssetById(id)`

Retrieve an asset by its unique identifier.

### Syntax

```typescript
webflow.getAssetById(id:string): Promise<Asset>
```

### Parameters

* **id**:`string` -  The unique identifier of the asset

### Returns

**Promise\<*Asset*>** | `null`

A Promise that resolves to an Asset. If an invalid ID is entered, the method will return `null`

### Example

```typescript
const asset = await webflow.getAssetById(id)
 console.log(asset)
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
