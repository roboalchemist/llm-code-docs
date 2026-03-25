# Source: https://docs.trackjs.com/data-management/ignore/

Title: Ignoring Errors

URL Source: https://docs.trackjs.com/data-management/ignore/

Markdown Content:
Lots of client-side errors may be beyond your control, such as a buggy advertising provider, open source package, or user’s browser extension. To handle this noise, TrackJS give you unlimited capacity to create Ignore Rules in the Dashboard or with the agent.

Errors Ignored by a rule are removed before your account is subject to [throttling limits](https://docs.trackjs.com/data-management/limits/), so it’s a good idea to ignore unactionable errors right away.

[Ignore Rule Builder](https://docs.trackjs.com/data-management/ignore/#ignore-rule-builder "Permalink Here")
------------------------------------------------------------------------------------------------------------

The Ignore Rule Builder allows you to [create ignore rules in the TrackJS Dashboard](https://my.trackjs.com/account/ignore) based on exact or token matching on a number of error properties including `message`, `url`, `browser`, and `stack trace`.

It is common to create an Ignore Rule for a noisy third-party script. For example, let’s say we have a lot of errors coming from the _Mixpanel agent_. It’s unlikely that you’ll be able to “fix” these errors from a third party, and so-long-as they are not breaking the behavior of your site, it is safe to ignore them.

The best way to Ignore a third-party error is by Ignoring errors where the `Stack Trace`_contains_ the third-party script name or url. In the case of _Mixpanel_, loaded from `cdn.mxpnl.com`, we would create an Ignore Rule like:

[Agent Ignore](https://docs.trackjs.com/data-management/ignore/#agent-ignore "Permalink Here")
----------------------------------------------------------------------------------------------

If your ignore rules are too complex for the builder above, we can add them using the agent [`onError callback`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#onerror). The callback will be invoked with the [capture payload](https://docs.trackjs.com/data-api/capture/#request-payload) every time an error has been detected. You can manipulate the payload to add your own ignore logic. If you return a `falsy` value from the callback, the error will be ignored.

For example, let’s consider that you have an “admin” section of your application that requires a special session to use. You may want to ignore errors from that “admin” pages if that session doesn’t exist.

[Global](https://docs.trackjs.com/data-management/ignore/)[Module](https://docs.trackjs.com/data-management/ignore/)[Legacy](https://docs.trackjs.com/data-management/ignore/)

window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", onError: function(payload) { // Check if the URL contains "/admin/" AND if there is no session if (/\/admin\/gi.test(payload.url) && !YourApp.isSession()) { return false; } return true; }});

[Ignore sessionless admin errors example](https://docs.trackjs.com/data-management/ignore/#code-ignore-sessionless-admin-errors-example)

import { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN", onError: function(payload) { // Check if the URL contains "/admin/" AND if there is no session if (/\/admin\/gi.test(payload.url) && !YourApp.isSession()) { return false; } return true; }});

[Ignore sessionless admin errors example](https://docs.trackjs.com/data-management/ignore/#code-ignore-sessionless-admin-errors-example)

<script> window._trackJs = { token: "YOUR_TOKEN", onError: function(payload) { // Check if the URL contains "/admin/" AND if there is no session if (/\/admin\/gi.test(payload.url) && !YourApp.isSession()) { return false; } return true; }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

[Ignore sessionless admin errors example](https://docs.trackjs.com/data-management/ignore/#code-ignore-sessionless-admin-errors-example)
