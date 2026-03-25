# Source: https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/

Title: Agent Options

URL Source: https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/

Markdown Content:
The Agent Options allows you to customize the agent to best meet the needs of your application. The following config options can be provided to the [install](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#install) method, or as the [preconfig](https://docs.trackjs.com/browser-agent/installation/#auto-install) object.

**Changeable** options can be used by the [configure()](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#configure) method after installation.

* * *

[application](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#application "Permalink Here")
--------------------------------------------------------------------------------------------------------------

String

Optional

A application allows you to segment your reported error data by codebase or deployment environment. This key is generated when you [create an Application segment in your Dashboard](https://my.trackjs.com/Account/Applications). [Learn more about application segmentation](https://docs.trackjs.com/data-management/applications/).

Default`undefined`
Changeable`false`
Since[`2.1.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", application: "{APPLICATION}"});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", application: "{APPLICATION}"});

<script> window._trackJs = { token: "{TOKEN}", application: "{APPLICATION}"};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[callback.enabled](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#callbackenabled "Permalink Here")
-----------------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether the agent should wrap browser callback functions for error detection, such as `addEventListener` and `setTimeout`.

Default`true`
Changeable`false`
Since[`2.0.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-1 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", callback: { enabled: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", callback: { enabled: false }});

<script> window._trackJs = { token: "{TOKEN}", callback: { enabled: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[callback.bindStack](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#callbackbindstack "Permalink Here")
---------------------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether to generate stack traces during asynchronous actions, similar to Chrome’s “async stack traces”. This will produce additional stack traces when asynchronous functions are called, such as `addEventListener` or `setTimeout`, and show you the history of the call stacks.

**WARNING** There is a performance impact to enabling this and may generate higher memory usage than normal for the agent. Test your application with this setting before deploying your app to production.

Default`false`
Changeable`false`
Since[`2.0.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-2 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", callback: { bindStack: true }} );

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", callback: { bindStack: true }} );

<script> window._trackJs = { token: "{TOKEN}", callback: { bindStack: true }} ;</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[console.enabled](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#consoleenabled "Permalink Here")
---------------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether to record Telemetry events from the console.

Default`true`
Changeable`false`
Since[`1.1.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-3 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", console: { enabled: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", console: { enabled: false }});

<script> window._trackJs = { token: "{TOKEN}", console: { enabled: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[console.display](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#consoledisplay "Permalink Here")
---------------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether to pass recorded console messages through to the actual browser console. This allows you to hide console messages in production environments.

Default`true`
Changeable`false`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-4 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", console: { display: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", console: { display: false }});

<script> window._trackJs = { token: "{TOKEN}", console: { display: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[console.error](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#consoleerror "Permalink Here")
-----------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether an error should be reported if `console.error` is invoked.

Default`true`
Changeable`false`
Since[`1.1.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-5 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", console: { error: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", console: { error: false }});

<script> window._trackJs = { token: "{TOKEN}", console: { error: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[console.warn](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#consolewarn "Permalink Here")
---------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether an error should be reported if `console.warn` is invoked.

Default`false`
Changeable`false`
Since[`2.5.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-6 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", console: { warn: true }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", console: { warn: true }});

<script> window._trackJs = { token: "{TOKEN}", console: { warn: true }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[console.watch](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#consolewatch "Permalink Here")
-----------------------------------------------------------------------------------------------------------------

String[]

Optional

A list of function names that will be recorded for Telemetry events. This allows you to remove a console function, such as `debug`, from your error reports.

Default`["log", "debug", "info", "warn", "error"]`
Changeable`false`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-7 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", console: { watch: ["log", /*"debug",*/ "info", "warn", "error"] }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", console: { watch: ["log", /*"debug",*/ "info", "warn", "error"] }});

<script> window._trackJs = { token: "{TOKEN}", console: { watch: ["log", /*"debug",*/ "info", "warn", "error"] }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[dedupe](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#dedupe "Permalink Here")
----------------------------------------------------------------------------------------------------

Boolean

Optional

Whether the agent should attempt to suppress duplicate errors from being reported. This greatly reduces noise in the dashboard and is recommended.

Default`true`
Changeable`true`
Since[`2.8.5`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-8 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", dedupe: false});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", dedupe: false});

<script> window._trackJs = { token: "{TOKEN}", dedupe: false};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[dependencies](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#dependencies "Permalink Here")
----------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether the agent should attempt discovery of the JavaScript libraries on the page when an error is detected. This is done by crawling over `window.*.version`, which can trip errors if your app has built custom global property getters.

Default`true`
Changeable`true`
Since[`2.13.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-9 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", dependencies: false});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", dependencies: false});

<script> window._trackJs = { token: "{TOKEN}", dependencies: false};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[enabled](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#enabled "Permalink Here")
------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether the agent should be able to be installed on the current

**WARNING** This option has been deprecated as of `3.0.0`. It is no longer necessary now that agent installation is called explicitly with [install()](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#install).

Default`true`
Changeable`false`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-10 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", enabled: (location.host.indexOf("localhost") !== 0)});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", enabled: (location.host.indexOf("localhost") !== 0)});

<script> window._trackJs = { token: "{TOKEN}", enabled: (location.host.indexOf("localhost") !== 0)};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[forwardingDomain](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#forwardingdomain "Permalink Here")
------------------------------------------------------------------------------------------------------------------------

String

Optional

Tells the agent to send all error payloads through a first-party domain. This is often done to prevent ad-blockers from rejecting error payloads.

**NOTE** Before you use this option, you must [Configure Domain Forwarding](https://docs.trackjs.com/data-management/ad-blockers/#domain-forwarding) for your account.

Default`undefined`
Changeable`false`
Since[`3.9.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-11 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", forwardingDomain: "errors.mydomain.com"});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", forwardingDomain: "errors.mydomain.com"});

<script> window._trackJs = { token: "{TOKEN}", forwardingDomain: "errors.mydomain.com"};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[network.enabled](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#networkenabled "Permalink Here")
---------------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether to record Telemetry events from `XMLHttpRequest` and `fetch` requests.

Default`true`
Changeable`false`
Since[`1.1.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-12 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", network: { enabled: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", network: { enabled: false }});

<script> window._trackJs = { token: "{TOKEN}", network: { enabled: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[network.error](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#networkerror "Permalink Here")
-----------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether an error should be reported if a network request is returned with a response code of `400` or greater.

Default`true`
Changeable`false`
Since[`1.1.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-13 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", network: { error: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", network: { error: false }});

<script> window._trackJs = { token: "{TOKEN}", network: { error: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[onError](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#onerror "Permalink Here")
------------------------------------------------------------------------------------------------------

Function

Optional

A callback function invoked when the agent has detected an error but before it has been reported. The callback function is presented with the [payload](https://docs.trackjs.com/data-api/capture/#request-payload), which can be manipulated by the callback, and the original error that triggered the event. If the original event was not an instance of `Error`, an `Error` object will be created with a serialized message and stack trace.

The callback returns a `boolean` with `true` indicating that the error should be reported and `false` that the error should be ignored.

This is useful for:

*   adding custom context
*   removing sensitive data
*   complex error grouping
*   complex ignore logic.

Default`undefined`
Changeable`true`
Since[`2.0.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-14 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", onError: function(payload, error) { payload.metadata.push({ key: "interesting property", value: "interesting value" }); return (SHOULD_WE_SEND) ? true : false; }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", onError: function(payload, error) { payload.metadata.push({ key: "interesting property", value: "interesting value" }); return (SHOULD_WE_SEND) ? true : false; }});

<script> window._trackJs = { token: "{TOKEN}", onError: function(payload, error) { payload.metadata.push({ key: "interesting property", value: "interesting value" }); return (SHOULD_WE_SEND) ? true : false; }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[serialize](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#serialize "Permalink Here")
----------------------------------------------------------------------------------------------------------

Function

Optional

A custom serializer function for non-string objects. This will be invoked when an error or Telemetry item needs to be recorded into the log. The callback will be invoked with a unknown object, which must be transformed and returned as a string.

If you have custom objects that the default serializer is not sufficiently representing, you can use this callback to implement your own serializer.

**WARNING** This option has been deprecated as of `3.0.0`. The default serializer was dramatically improved in [`2.8.4`](https://docs.trackjs.com/browser-agent/changelog/), making custom serializers likely unnecessary.

Default`undefined`
Changeable`true`
Since[`2.0.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-15 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", serialize: function(thing) { try { return JSON.stringify(thing); } catch (e) { return "unknown entity"; } }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", serialize: function(thing) { try { return JSON.stringify(thing); } catch (e) { return "unknown entity"; } }});

<script> window._trackJs = { token: "{TOKEN}", serialize: function(thing) { try { return JSON.stringify(thing); } catch (e) { return "unknown entity"; } }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[sessionId](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#sessionid "Permalink Here")
----------------------------------------------------------------------------------------------------------

String

Optional

Customer-generated identification string for the current browser session. Use this to correlate error reports with external logs and reporting data.

Default`undefined`
Changeable`true`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-16 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", sessionId: "4973c64584a84df1a925fdc4138c8d81"});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", sessionId: "4973c64584a84df1a925fdc4138c8d81"});

<script> window._trackJs = { token: "{TOKEN}", sessionId: "4973c64584a84df1a925fdc4138c8d81"};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[token](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#token "Permalink Here")
--------------------------------------------------------------------------------------------------

String

Required

Customer account token, generated by TrackJS. This identifies error traffic for your account. Get this from [the install page](https://my.trackjs.com/install).

Default`true`
Changeable`false`
Since[`2.0.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-17 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}"});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}"});

<script> window._trackJs = { token: "{TOKEN}"};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[userId](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#userid "Permalink Here")
----------------------------------------------------------------------------------------------------

String

Optional

Customer-generated identification string for the current browser user. Use this to identify and correlate errors happening to a single user. If you do not wish to send [Sensitive Data](https://docs.trackjs.com/data-management/sensitive/) to TrackJS, do not send an externally identifiable string.

If you do not provide a `userId`, one will be generated when an error is reported based on the Browser definition and originating IP Address.

Default`undefined`
Changeable`true`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-18 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", userId: "sam@customer.org"});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", userId: "sam@customer.org"});

<script> window._trackJs = { token: "{TOKEN}", userId: "sam@customer.org"};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[visitor.enabled](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#visitorenabled "Permalink Here")
---------------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether to record Telemetry events from Visitor actions such as click and form input.

Default`true`
Changeable`false`
Since[`1.1.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-19 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", visitor: { enabled: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", visitor: { enabled: false }});

<script> window._trackJs = { token: "{TOKEN}", visitor: { enabled: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[version](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#version "Permalink Here")
------------------------------------------------------------------------------------------------------

String

Optional

Customer-generated identification string for running application version. Use this to identify and correlate errors happening to a release of your application. This could be a semver string, or a git commit hash.

Default`undefined`
Changeable`true`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-20 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", version: "3.2.1"});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", version: "3.2.1"});

<script> window._trackJs = { token: "{TOKEN}", version: "3.2.1"};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[window.enabled](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#windowenabled "Permalink Here")
-------------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether to report errors captured globally from `window.onerror`.

Default`true`
Changeable`false`
Since[`1.1.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-21 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", window: { enabled: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", window: { enabled: false }});

<script> window._trackJs = { token: "{TOKEN}", window: { enabled: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[window.promise](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#windowpromise "Permalink Here")
-------------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether to report unhandled Promise rejections.

Default`true`
Changeable`false`
Since[`2.10.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#example-22 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", window: { promise: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", window: { promise: false }});

<script> window._trackJs = { token: "{TOKEN}", window: { promise: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *
