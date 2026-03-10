# Source: https://developers.webflow.com/browser/reference/allow-user-tracking.mdx

***

title: Allow user tracking
slug: reference/allow-user-tracking
description: Enable user tracking for Webflow Analyze and Optimize.
hidden: false
'og:title': Allow user tracking
'og:description': Enable user tracking for Webflow Analyze and Optimize.
------------------------------------------------------------------------

## `wf.allowUserTracking(options)`

Enables user tracking for the current user.

### Syntax

```typescript
wf.allowUserTracking(options?: { reload?: boolean; activate?: boolean }): void
```

### Parameters

* **options**: *object* - Controls activation behavior. All properties are optional.
  * **reload**: *boolean* - Reloads the page after activating tracking. *Default: false*
  * **activate**: *boolean* - Activates tracking immediately. *Default: true*

### Returns

This method doesn't return a value to the caller.

### Example

```typescript
// Ensure Browser APIs are ready before calling
wf.ready(() => {
  // Enable user tracking and activate immediately
  wf.allowUserTracking({ activate: true });
});
```
