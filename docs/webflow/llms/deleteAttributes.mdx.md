# Source: https://developers.webflow.com/browser/optimize/deleteAttributes.mdx

***

title: Delete attributes
slug: optimize/deleteAttributes
description: Delete custom attributes for the current user or page view
hidden: false
'og:title': Delete attributes
'og:description': Delete custom attributes for the current user or page view
----------------------------------------------------------------------------

## `wf.deleteAttributes(scope, names)`

Delete specified custom attributes for the current user or page view. This method removes previously set attributes from storage. If you attempt to delete an attribute that doesn't exist, the operation will be ignored and no error will be thrown.

### Syntax

```typescript
wf.deleteAttributes(scope: 'user' | 'pageview', names: string[])
```

### Parameters

* **scope**: `'user'` | `'pageview'` - The scope of the attributes. You can choose to set attributes for the current user or the current page view.
* **names**: `string[]` - An array of attribute names to delete.

### Example implementation

```javascript
// Call the wf.ready() function the Browser API is available
wf.ready(function() {
  // Set attributes for the current user
  wf.deleteAttributes('user', ['userSegment'])
})
```

### Returns

This method doesn't return a value. It only deletes the specified attributes from storage. To see updated attributes, use [`wf.getAttributes()`](/browser/optimize/getAttributes).
