# Source: https://developers.webflow.com/designer/reference/create-page.mdx

***

title: Create page
slug: designer/reference/create-page
description: ''
hidden: false
'og:title': 'Webflow Designer API: Create page'
'og:description': >-
Create a new page in the Designer. This method will return an error if the App
tries to create more pages than a User's plan allows.
-----------------------------------------------------

## `webflow.createPage()`

Create a new page in the Designer. This method will return an error if the App tries to create more pages than a User's plan allows.

### Syntax

```typescript
webflow.createPage(): Promise<Page>
```

### Returns

**Promise\<*Page*>**

A Promise that resolves to the created page.

### Example

```typescript
// Create new page and set page name
const newPage = await webflow.createPage() as Page
await newPage.setName('My New Page')

// Switch to new page
await webflow.switchPage(newPage)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability  | Locale | Branch | Workflow | Sitemode |
| :---------------- | :----- | :----- | :------- | :------- |
| **canCreatePage** | Any    | Any    | Any      | Design   |
