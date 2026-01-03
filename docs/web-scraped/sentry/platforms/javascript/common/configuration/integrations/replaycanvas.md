---
---
title: ReplayCanvas
description: "Capture session replays from HTML canvas elements."
---

This integration only works inside a browser environment.

_Import name: `Sentry.replayCanvasIntegration`_

The Replay Canvas integration can be used to capture [Session Replays](/product/session-replay/) from HTML canvas elements. It requires the Replay integration to be enabled.

There is currently no PII scrubbing in canvas recordings!

Read more about [setting up Session Replay with the Canvas integration](./../../../session-replay#canvas-recording).

```JavaScript
Sentry.init({
  integrations: [Sentry.replayCanvasIntegration()],
});
```
