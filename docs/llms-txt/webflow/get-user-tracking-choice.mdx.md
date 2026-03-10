# Source: https://developers.webflow.com/browser/reference/get-user-tracking-choice.mdx

***

title: Get user tracking choice
slug: reference/get-user-tracking-choice
description: Retrieve the user's tracking preference for Webflow Analyze and Optimize.
hidden: null
'og:title': Get user tracking choice
'og:description': Retrieve the user's tracking preference for Webflow Analyze and Optimize.
-------------------------------------------------------------------------------------------

## `wf.getUserTrackingChoice()`

Retrieves the user's current tracking preference. Returns one of three possible states: `allow`, `deny`, or `undefined`.

### Syntax

```typescript
wf.getUserTrackingChoice(): 'allow' | 'deny' |
'none'
```

### Returns

The user's current tracking choice:

* `'allow'` User has opted in to tracking.
* `'deny'` User has opted out of tracking.
* `'none'` User hasn't made a choice.

### Example

```typescript
// Ensure Browser APIs are ready before calling
wf.ready(() => {
  // Retrieve the user's tracking choice
  const choice = wf.getUserTrackingChoice();
  console.log(choice); // 'allow', 'deny', or undefined
});
```
