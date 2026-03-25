# Source: https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/

Title: Passive Tracking

URL Source: https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/

Markdown Content:
This example shows how to configure TrackJS for a passive tracking environment, such as a third-party plugin or chrome module. In this case, you do not want to track _everything_ on the page, as most events are not relevant to you. You only want to track events that you _directly_ send into TrackJS.

This disables all automatic tracking and collection of Telemetry events.

[Global](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/)[Module](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/)[Legacy](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/)

window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", callback: { enabled: false }, console: { enabled: false }, network: { enabled: false }, visitor: { enabled: false }, window: { enabled: false, promise: false }};);

[Passive Agent Tracking](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/#code-passive-agent-tracking)

import { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN", callback: { enabled: false }, console: { enabled: false }, network: { enabled: false }, visitor: { enabled: false }, window: { enabled: false, promise: false }};);

[Passive Agent Tracking](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/#code-passive-agent-tracking)

<script> window._trackJs = { token: "YOUR_TOKEN", callback: { enabled: false }, console: { enabled: false }, network: { enabled: false }, visitor: { enabled: false }, window: { enabled: false, promise: false }};;</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

[Passive Agent Tracking](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/#code-passive-agent-tracking)

To record your own Telemetry events, use the TrackJS console:

[Global](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/)[Module](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/)[Legacy](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/)

window.TrackJS && TrackJS.console.log("something interesting happened"); window.TrackJS && TrackJS.console.log({ type: "event", data: myStateObject });

[Adding telemetry events](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/#code-adding-telemetry-events)

import { TrackJS } from "trackjs";TrackJS.console.log("something interesting happened");TrackJS.console.log({ type: "event", data: myStateObject });

[Adding telemetry events](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/#code-adding-telemetry-events)

window.trackJs && trackJs.console.log("something interesting happened"); window.trackJs && trackJs.console.log({ type: "event", data: myStateObject });

[Adding telemetry events](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/#code-adding-telemetry-events)

And to catch errors from your code, you’ll want to use the helper functions [`attempt`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#attempt) and [`watch`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#watch), or surround your code in try/catch blocks.

Use attempt if your code is synchronous and contained in a single function.

TrackJS.attempt(function your_main_function() { // do your work.});

[Adding explicit tracking to your code with attempt](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/#code-adding-explicit-tracking-to-your-code-with-attempt)

Use watch to wrap individual functions that you might use in a callback.

function something() { // do your work.}; document.addEventListener("click", TrackJS.watch(something));

[Adding explicit tracking to your code with watch](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/#code-adding-explicit-tracking-to-your-code-with-watch)

Or use your own `try``catch` wrapping and forward the errors to TrackJS.

try { // do your work.} catch(e) { TrackJS.track(e);}

[Adding explicit tracking to your code with try/catch](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/#code-adding-explicit-tracking-to-your-code-with-try-catch)
