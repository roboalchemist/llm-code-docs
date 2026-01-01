---
---
title: BrowserSession
description: "Track healthy Sessions in the Browser."
---

This integration only works inside a browser environment.

_Import name: `Sentry.browserSessionIntegration`_

Sentry's [Release Health](/product/releases/health/) feature allows you to track user adoption and your application's crash-free rate.
When the BrowserSession integration is enabled, it automatically creates a session each time a user loads your page or application. These sessions are used to track your release health. If an error is captured during an active session, the session will be flagged as faulty.
Read more about Sessions.

```JavaScript
Sentry.init({
  integrations: [Sentry.browserSessionIntegration()],
});
```
