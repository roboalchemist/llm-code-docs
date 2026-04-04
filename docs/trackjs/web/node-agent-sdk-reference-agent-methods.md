# Source: https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/

Title: Agent Methods

URL Source: https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/

Markdown Content:
The following methods are available on the `TrackJS` namespace of the `trackjs-node` published module.

* * *

Function

Add one or more key-value pairs of strings to describe the current context. You can use this to track any arbitrary data that is interesting for you, such as whether it is a paying customer, their transaction id, or anything else. These metadata key-values are sent with each error and give you the capability to filter the Dashboard in your own way.

If the metadata key already exists, it will be updated with the new value. See [`removeMetadata`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#removemetadata).

Metadata can also be added during install via [`options`](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/).

Agent must be installed. See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

param 1`object` dictionary of key-value pairs OR
param 1`string` Metadata key
param 2`string` Metadata value for this page session.
returns`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.addMetadata("user_subscription", "professional");TrackJS.addMetadata({ "user_role": "owner", "server": "YOUR_SERVER_ID"});

* * *

[configure](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#configure "Permalink Here")
--------------------------------------------------------------------------------------------------------

Function

Update the [Agent Options](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/) after [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

param 1`TrackJSOptions` Options to be updated
returns`boolean``true` if successful
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-1 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.configure({ userId: "sam@customer.com", sessionId: "17734FEB342"});

* * *

[addLogTelemetry](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#addlogtelemetry "Permalink Here")
--------------------------------------------------------------------------------------------------------------------

Function

Record a Telemetry console event into the log. Messages sent to this method will not be seen in the global console. If `severity` is `"error"`, an Error will be captured by the agent.

Agent must be installed. See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

param 1`string` Severity level. “log”,”debug”,”info”,”warn”,”error”
param …n`Any` properties to be logged
returns`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-2 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.addLogTelemetry("info", "my info message", { state: "bar" });

* * *

[Handlers.expressErrorHandler](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#handlersexpresserrorhandler "Permalink Here")
---------------------------------------------------------------------------------------------------------------------------------------------

Function

Return an error handler for Express middleware. See [Express Integration](https://docs.trackjs.com/integrations/express/).

Agent must be installed. See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

param 1`Object` Options for the handler
Options.next`Boolean` Whether to pass errors on to the next handler. If you do not have another handler, this may cause duplicate errors to be captured. Default `false`.
returns`Function` Express Error Middleware function.
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-3 "Permalink Here")

import express from "express";import { TrackJS } from "trackjs-node";var app = express() // your other handlers .use(TrackJS.Handlers.expressErrorHandler({ next: false }));

* * *

[Handlers.expressRequestHandler](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#handlersexpressrequesthandler "Permalink Here")
-------------------------------------------------------------------------------------------------------------------------------------------------

Function

Return an request handler for Express middleware. See [Express Integration](https://docs.trackjs.com/integrations/express/).

Agent must be installed. See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

param 1`Object` Options for the handler
Options.correlationHeader`Boolean` Whether to send the TrackJS Correlation Id as a header on requests. This is detected by the TrackJS Browser Agent (as of v3.4.0) for linking between client and server errors. Default `true`.
returns`Function` Express Request Middleware function.
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-4 "Permalink Here")

import express from "express";import { TrackJS } from "trackjs-node";var app = express() .use(TrackJS.Handlers.expressRequestHandler({ correlationHeader: true })) // your other handlers

* * *

[install](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install "Permalink Here")
----------------------------------------------------------------------------------------------------

Function

Installs the agent into the current environment with the provided [options](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/).

If the agent has already been installed, it will throw a `TrackJSError`.

`options.token` is required, and the method will throw a `TrackJSError` if omitted.

See [`uninstall`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#uninstall).

param`TrackJSOptions` Options to install with.
returns`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-5 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.install({ token: "YOUR_TOKEN" // other config options});

* * *

[isInstalled](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#isinstalled "Permalink Here")
------------------------------------------------------------------------------------------------------------

Function

Whether the agent has been installed into the current environment. See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install) and [`uninstall`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#uninstall).

returns`boolean`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-6 "Permalink Here")

import { TrackJS } from "trackjs-node";if (!TrackJS.isInstalled()) { TrackJS.install({ token: "YOUR_TOKEN" // other config options });}

* * *

[onError](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#onerror "Permalink Here")
----------------------------------------------------------------------------------------------------

Function

Attaches a custom error handler to the agent. Use custom handlers to intercept [`Error Payloads`](https://docs.trackjs.com/data-api/capture/#request-payload) to change their values or prevent them from being captured. Error handlers will be executed in the order that they are attached. Once an error is ignored, no further error handlers will be notified.

Error handler functions take a single `payload` argument which will be a [`Capture Payload`](https://docs.trackjs.com/data-api/capture/#request-payload) object. The handler function returns a boolean where `true` signals the error should continue and `false` prevents it from being captured.

Error handlers can also be attached during install via [`options`](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/).

Agent must be installed. See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

param`Function` Error handler function to be attached to the agent.
returns`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-7 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.onError((payload) => { // re-writing the application based on message value if (payload.message.indexOf("foo") >= 0) { payload.application = "foo-app" }; return true;});TrackJS.onError((payload) => { // ignoring errors that come from an ad if (payload.url.indexOf("ads.") >= 0) { return false; } return true;});

* * *

Function

Removes one or more keys from the metadata store. The key will no longer be included with reported errors.

See [`addMetadata`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#addmetadata).

Agent must be installed. See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

param 1`object` dictionary of keys OR
param 1`string` Metadata key
returns`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-8 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.removeMetadata("user_subscription");TrackJS.removeMetadata({ "user_role": false, "server": false});

* * *

[track](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#track "Permalink Here")
------------------------------------------------------------------------------------------------

Function

Captures an error to TrackJS with the provided error. If the parameter is not an `Error`, one will be generated using the serialized parameter as the message.

Options can be provided which will override the agent options for **this error only**. This is useful if you want to include metadata unique to this request, or reroute it to a different application dashboard.

Agent must be installed. See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

param 1`Any` Error to be reported
param 2`TrackJSOptions` Optional. Agent options to be overrode for this operation.
returns`Error` Error object that was tracked. If an error object wasn’t passed, it will return the Error generated.
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-9 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.track(new Error("oops"));TrackJS.track({ custom: "object" });TrackJS.track(new Error("oops"), { application: "myapp", metadata: { "module": "olympus" }});

* * *

[uninstall](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#uninstall "Permalink Here")
--------------------------------------------------------------------------------------------------------

Function

Removes the agent from the current environment.

See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

returns`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-10 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.uninstall();

* * *

[usage](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#usage "Permalink Here")
------------------------------------------------------------------------------------------------

Function

Captures a “page-view” usage metric for the TrackJS Dashboard. Useful to understand how active the code is when correlating with error rates.

This API is likely to change as the Node client develops.

Agent must be installed. See [`install`](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#install).

returns`undefined`
Since[`1.0.0`](https://docs.trackjs.com/node-agent/changelog/)

### [Example](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/#example-11 "Permalink Here")

import { TrackJS } from "trackjs-node";TrackJS.usage();
