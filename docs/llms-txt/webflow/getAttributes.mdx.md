# Source: https://developers.webflow.com/browser/optimize/getAttributes.mdx

***

title: Get Attributes
slug: optimize/getAttributes
description: Get attributes for the current user or page view
hidden: false
'og:title': Get attributes
'og:description': Get attributes for the current user or page view
------------------------------------------------------------------

## `wf.getAttributes(scope, names)`

Retrieve a subset of attributes that have been previously stored using [`setAttributes()`](/browser/optimize/setAttributes). Only attributes that match the names parameter will be returned.

#

### Syntax

```typescript
wf.getAttributes(scope: 'user' | 'pageview', names: string[])
```

### Parameters

* **scope**: `'user'` | `'pageview'` - The scope of the attributes to retrieve.
* **names**: `string[]` - An array of attribute names to retrieve.

## Example implementation

```javascript
// Call the wf.ready() function the Browser API is available
wf.ready(function() {
  // Set attributes for the current user
  wf.setAttributes('user', {
    userSegment: 'enterprise'
  })
})

// Retrieve the attributes
const attributes = wf.getAttributes('user', ['userSegment'])
  console.log(attributes)
```

### Returns

An object containing the attributes that match the names parameter.

#

### Example

```json
{
  "userSegment": "enterprise"
}
```
