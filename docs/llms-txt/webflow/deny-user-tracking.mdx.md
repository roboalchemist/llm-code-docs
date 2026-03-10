# Source: https://developers.webflow.com/browser/reference/deny-user-tracking.mdx

***

title: Deny user tracking
slug: reference/deny-user-tracking
description: Disable user tracking for Webflow Analyze and Optimize.
hidden: false
'og:title': Deny user tracking
'og:description': Disable user tracking for Webflow Analyze and Optimize.
-------------------------------------------------------------------------

## `wf.denyUserTracking(options)`

Disables user tracking for the current user.

### Syntax

```typescript
wf.denyUserTracking(options?: { reload?: boolean }): void
```

### Parameters

* **options?**: *object* - Controls deactivation behavior. Optional.
  * **reload?**: *boolean* - Reloads the page after disabling tracking. *Default: false*

### Returns

This method doesn't return a value to the caller.

### Example

```typescript
// Ensure Browser APIs are ready before calling
wf.ready(() => {
  // Disable user tracking and reload the page
  wf.denyUserTracking({ reload: true });
});
```
