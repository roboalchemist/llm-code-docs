# Source: https://developers.webflow.com/browser/optimize/deleteAllAttributes.mdx

***

title: Delete all attributes
slug: optimize/deleteAllAttributes
description: Delete all custom attributes for the current user or page view
hidden: false
'og:title': Delete all attributes
'og:description': Delete all custom attributes for the current user or page view
--------------------------------------------------------------------------------

## `wf.deleteAllAttributes(scope)`

Delete all custom attributes for the current user or page view. This method removes previously set attributes from storage.

### Syntax

```typescript
wf.deleteAllAttributes(scope: 'user' | 'pageview')
```

### Parameters

* **scope**: `'user'` | `'pageview'` - The scope of the attributes. You can choose to set attributes for the current user or the current page view.

### Example implementation

```javascript
// Call the wf.ready() function the Browser API is available
wf.ready(function() {
  // Set attributes for the current user
  wf.deleteAllAttributes('user')
})
```

### Returns

This method doesn't return a value. It only deletes the specified attributes from storage. To see updated attributes, use [`wf.getAttributes()`](/browser/optimize/getAttributes).
