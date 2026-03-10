# Source: https://developers.webflow.com/designer/reference/set-asset-name.mdx

***

title: Set Asset Name
slug: reference/set-asset-name
description: Set the name of an asset.
hidden: false
'og:title': 'Webflow Designer API: Set Asset Name'
'og:description': Set the name of an asset.
-------------------------------------------

## `asset.setName(name)`

Set the name of an asset.

## Syntax

```typescript
asset.setName(name: string): Promise<null>
```

### Parameters

* **name**: *string* - The name of the asset.

### Returns

A Promise that resolves to `null`.

#

### Example

```typescript
const assets = await webflow.getAllAssets()
const asset = assets[0]
await asset.setName("Marvin the Paranoid Android")
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canManageAssets** | Any    | Any    | Any      | Any      |
