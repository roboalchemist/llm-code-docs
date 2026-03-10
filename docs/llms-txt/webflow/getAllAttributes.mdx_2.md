# Source: https://developers.webflow.com/browser/optimize/getAllAttributes.mdx

***

title: Get all attributes
slug: optimize/getAllAttributes
description: Get all attributes for the current user or page view
hidden: false
'og:title': Get all attributes
'og:description': Get all attributes for the current user or page view
----------------------------------------------------------------------

## `wf.getAllAttributes()`

Retrieve all attributes that have been previously stored using [`setAttributes()`](/browser/optimize/setAttributes).

#

### Syntax

```typescript
wf.getAllAttributes(scope: 'user' | 'pageview')
```

### Parameters

* **scope**: `'user'` | `'pageview'` - The scope of the attributes to retrieve.

## Example implementation

```javascript
// Call the wf.ready() function the Browser API is available
wf.ready(function() {
  // Set attributes for the current user
  wf.setAttributes('user', {
    userSegment: 'enterprise',
    userRole: 'technicalBuyer'
  })
})

// Retrieve the attributes
const attributes = wf.getAllAttributes('user')
  console.log(attributes)
```

### Returns

An object containing all attributes set for the current scope.

#

### Example

```json
{
  "userSegment": "enterprise",
  "userRole": "technicalBuyer"
}
```
