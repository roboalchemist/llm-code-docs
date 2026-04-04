# Source: https://docs.trackjs.com/node-agent/sdk-reference/agent-options/

Title: Agent Options

URL Source: https://docs.trackjs.com/node-agent/sdk-reference/agent-options/

Markdown Content:
The Agent Options allows you to customize the agent to best meet the needs of your application. The following config options can be provided to the [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install), [`configure`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#configure), or passed as an override to [`track`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#track).

**Required** options must be provided when installing the agent.

* * *

[application](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#application "Permalink Here")
------------------------------------------------------------------------------------------------------------

String

A application allows you to segment your reported error data by codebase or deployment environment. This key is generated when you [create an Application segment in your Dashboard](https://my.trackjs.com/Account/Applications). [Learn more about application segmentation](https://docs.trackjs.com/data-management/applications/).

Default`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}", application: "{APPLICATION}"});

* * *

[correlationId](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#correlationid "Permalink Here")
----------------------------------------------------------------------------------------------------------------

String

A correlationId is an arbitrary string identifier that will combine errors into a series. It allows you to see all the errors that happened on an activity together.

Default Generated UUIDv4
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-1 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}", correlationId: "user@/widgets/123"});

* * *

Boolean

Whether the agent should include default NodeJS properties, such as `hostname`, `username`, and `cwd`, as metadata.

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-2 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}", defaultMetadata: false});

* * *

[dependencies](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#dependencies "Permalink Here")
--------------------------------------------------------------------------------------------------------------

Boolean

Whether the agent should attempt discovery of the Node modules installed into the environment when loaded. This is done by shelling out to `npm list` asynchronously.

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-3 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}", dependencies: false});

* * *

{ [key: string]: string }

Hash of metadata key-value pairs to be added to the agent. See [`addMetadata()`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#addMetadata).

Default`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-4 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}", metadata: { "shard": "alpha1" }});

* * *

[network.enabled](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#networkenabled "Permalink Here")
-------------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether to record Telemetry events from network requests.

Default`true`
Changeable`false`
Since[`1.3.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-5 "Permalink Here")

[Global](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/)[Module](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/)[Legacy](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", network: { enabled: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", network: { enabled: false }});

<script> window._trackJs = { token: "{TOKEN}", network: { enabled: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[network.error](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#networkerror "Permalink Here")
---------------------------------------------------------------------------------------------------------------

Boolean

Optional

Whether an error should be reported if a network request is returned with a response code of `400` or greater.

Default`true`
Changeable`false`
Since[`1.3.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-6 "Permalink Here")

[Global](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/)[Module](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/)[Legacy](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/)

window.TrackJS && TrackJS.install({ token: "{TOKEN}", network: { error: false }});

import { TrackJS } from "trackjs";TrackJS.install({ token: "{TOKEN}", network: { error: false }});

<script> window._trackJs = { token: "{TOKEN}", network: { error: false }};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

[onError](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#onerror "Permalink Here")
----------------------------------------------------------------------------------------------------

Function

Error handler function to be added to the agent. Invoked when the agent has detected an error but before it has been reported. The callback function is presented with the [payload](https://docs.trackjs.com/data-api/capture/#request-payload), which can be manipulated by the callback.

The callback returns a `boolean` with `true` indicating that the error should be reported and `false` that the error should be ignored.

This is useful for:

*   adding custom context
*   removing sensitive data
*   complex error grouping
*   complex ignore logic.

See [`onError()`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#onerror).

Default`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-7 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}", onError: (payload) => { // ignore errors from local environments. if (payload.url.indexOf("localhost") >= 0) { return false; } return true; }});

* * *

[sessionId](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#sessionid "Permalink Here")
--------------------------------------------------------------------------------------------------------

String

Customer-generated identification string for the current session. Use this to correlate error reports with external logs and reporting data.

Default`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-8 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}", sessionId: "4973c64584a84df1a925fdc4138c8d81"});

* * *

[token](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#token "Permalink Here")
------------------------------------------------------------------------------------------------

String

Required

Customer account token, generated by TrackJS. This identifies error traffic for your account. Get this from [the install page](https://my.trackjs.com/install).

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-9 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}"});

* * *

[userId](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#userid "Permalink Here")
--------------------------------------------------------------------------------------------------

String

Customer-generated identification string for the current user. Use this to identify and correlate errors happening to a single user. If you do not wish to send [Sensitive Data](https://docs.trackjs.com/data-management/sensitive/) to TrackJS, do not send an externally identifiable string.

If you do not provide a `userId`, one will be generated based on other available data.

Default`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-10 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}", userId: "sam@customer.org"});

* * *

[version](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#version "Permalink Here")
----------------------------------------------------------------------------------------------------

String

Customer-generated identification string for running application version. Use this to identify and correlate errors happening to a release of your application. This could be a semver string, or a git commit hash.

Default`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/#example-11 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "{TOKEN}", version: "3.2.1"});

* * *
