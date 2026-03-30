# Source: https://developers.webflow.com/designer/reference/get-collection-name-from-cms-page.mdx

***

title: Get collection name from a CMS page
slug: /designer/reference/get-collection-name-from-cms-page
description: Get the name of the collection that generated the page.
hidden: false
'og:title': Get collection name from a CMS page
'og:description': Get the name of the collection that generated the page.
-------------------------------------------------------------------------

## `page.getCollectionName()`

Get the name of the collection that generated the collection-generated page.

#

### Syntax

```typescript
page.getCollectionName(): Promise<string>
```

### Returns

**Promise\<`string`>**

A promise that resolves to the name of the collection that generated the page.

#

### Example

```typescript
try{
    // Get Current Page
    const currentPage = (await webflow.getCurrentPage()) as Page

    // Get Collection ID if page belongs to a collection
    const collectionName = await currentPage.getCollectionName()
    console.log(collectionName)
    }
catch (error) {
      console.error([error.message, error.cause.tag])
    }
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Error Handling

If the method fails to find a collection, the method will return an error with the following tag and message.

| Tag               | Message              |
| :---------------- | :------------------- |
| `ResourceMissing` | `Missing ${page.id}` |

### Designer Ability

| Designer Ability        | Locale | Branch | Workflow | Sitemode |
| :---------------------- | :----- | :----- | :------- | :------- |
| **canReadPageSettings** | Any    | Any    | Any      | Any      |
