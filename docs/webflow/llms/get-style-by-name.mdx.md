# Source: https://developers.webflow.com/designer/reference/get-style-by-name.mdx

***

title: Get style by name or path
slug: designer/reference/get-style-by-name
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get style by name or path'
'og:description': Retrieve a Style by its name or path.
-------------------------------------------------------

## **`webflow.getStyleByName(nameOrPath)`**

Retrieve a Style by its name or path.

### Syntax

```typescript
webflow.getStyleByName(nameOrPath: string | Array<string>): Promise<Style | null>
```

### Parameters

* **`nameOrPath`**: *string | Array\<string>* - The name of the style to retrieve or the path to the style to retrieve, consisting of the name of the parent and the name of the style.

### Returns

**Promise\<*`Style`* | `null`>**

A Promise that resolves to a style object, or `null` if the named style doesn't exist.

### Examples

Getting a style by name:

```typescript
// Retrieve the style by name
const retrievedStyle = await webflow.getStyleByName(styleName);

if (retrievedStyle) {
  // Get and print properties of the retrieved style
  const styleProperties = await retrievedStyle.getProperties();
  console.log("Style properties:", styleProperties);
} else {
  console.log(`Style ${styleName} not found.`);
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

Getting a style by path:

```typescript
// Retrieve the style by parent name and style name
const retrievedStyle = await webflow.getStyleByName([styleParentName, styleName]);

if (retrievedStyle) {
  // Get and print properties of the retrieved style
  const styleProperties = await retrievedStyle.getProperties();
  console.log("Style properties:", styleProperties);
} else {
  console.log(`Style ${styleName} with parent ${styleParentName} not found.`);
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
