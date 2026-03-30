# Source: https://developers.webflow.com/designer/reference/user-changes-cms-page.mdx

***

title: User changes CMS Page
slug: designer/reference/user-changes-cms-page
description: ''
hidden: false
-------------

## `webflow.subscribe("currentcmsitem", callback)`

Use this method to listen for specific events in your app. When a user selects a [collection page](https://university.webflow.com/lesson/structure-and-style-collection-pages?topics=cms-dynamic-content) or chooses a new CMS item on a collection page, this event will trigger. This can be especially useful for determining the path of auto-generated pages from a CMS or Ecommerce collection.

### Syntax

```typescript
webflow.subscribe(
  event: 'currentcmsitem',
  callback: (element: null | AnyElement) => void
): Unsubscribe;
```

### Parameters

**`event`** :   `"currentpage"`

The name of the event to subscribe to.

***

**callback**: `(() => void)`

The callback function to execute when the event occurs.

***

### Returns

#### ***`Unsubscribe`***

This is a special function returned after subscribing. Call this function when you want to stop listening to the event and discontinue receiving notifications.

### Example

```typescript
// Callback for subscription
    const cmsCallback = async () => {
      const page = await webflow.getCurrentPage()
      console.log(await page.getPublishPath())
    }

// Subscribe to changes for CMS Pages
 const unsubscribeCmsPages = webflow.subscribe('currentcmsitem', cmsCallback)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>
