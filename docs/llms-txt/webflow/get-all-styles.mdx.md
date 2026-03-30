# Source: https://developers.webflow.com/designer/reference/get-all-styles.mdx

***

title: Get all styles
slug: designer/reference/get-all-styles
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get all styles'
'og:description': 'Retrieve all Styles, also known as Classes, present on the Webflow site.'
--------------------------------------------------------------------------------------------

## **`webflow.getAllStyles()`**

[Retrieve all Styles, also known as Classes](https://university.webflow.com/lesson/web-styling-using-classes?topics=layout-design), present on the Webflow site.

### Syntax

```typescript
webflow.getAllStyles(): Promise<Array<Style>>
```

### Returns

**Promise\<Array\<*Style*>>**

A Promise that resolves to an array of *Style* objects representing all the styles present on the current site.

### Example

```typescript
// Get all Styles
const allStyles = await webflow.getAllStyles();

// List Styles
if (allStyles.length > 0) {

  console.log("List of all styles:");

  allStyles.forEach(async (style, index) => {

    // Print style names and ids
    console.log(`${index + 1}. Style Name: ${await style.getName()}, Style ID: ${style.id}`);
  });
} else {
  console.log("No styles found in the current context.");
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
