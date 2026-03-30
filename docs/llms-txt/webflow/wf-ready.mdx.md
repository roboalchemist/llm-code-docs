# Source: https://developers.webflow.com/browser/reference/wf-ready.mdx

***

title: wf.ready()
slug: reference/wf-ready
description: >-
The wf.ready() method is used to ensure the Browser API is available before
calling any API methods.
hidden: false
'og:title': wf.ready()
'og:description': >-
The wf.ready() method is used to ensure the Browser API is available before
calling any API methods.
------------------------

This method ensures the Browser API is loaded on the page. It accepts a callback function that executes once the Browser API loads. Place any code you want to run after the Browser API is ready inside this callback function.

<Tip>
  To make sure your code runs, always wrap your Browser API logic in 

  `wf.ready()`

  . This ensures that the Browser API is loaded before your code runs.
</Tip>

### Syntax

```typescript
wf.ready(callback: () => void): void
```

### Parameters

* **callback**: `() => void` - A function that executes once the Browser API is ready to use. **Place any code using the Browser API methods inside of this callback function.**

### Example

```javascript
wf.ready( () => {
    // Your code here
    console.log("The Browser API is ready to use!");
    const consentStatus = wf.getUserTrackingChoice();
    console.log(consentStatus);
});
```
