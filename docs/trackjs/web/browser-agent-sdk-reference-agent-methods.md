# Source: https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/

Title: Agent Methods

URL Source: https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/

Markdown Content:
The following methods are available on the `TrackJS` namespace (since [`3.0.0`](https://docs.trackjs.com/browser-agent/changelog/)) or the `trackJs` namespace for earlier versions.

**WARNING** If you are referencing the agent as a separate script, you should perform a [safety check](https://docs.trackjs.com/browser-agent/installation/#safety-checking) for the existence of the `TrackJS` namespace before calling any function. This will prevent your code from failing if the agent is blocked by a third-party.

* * *

Function

Add a key-value pair of data that will describe errors captured in this page view. You can use this to track any arbitrary data that is interesting for you, such as whether it is a paying customer, their transaction id, or anything else. These metadata key-values are sent with each error and give you the capability to filter the Dashboard in your own way.

If the metadata key already exists, it will be updated with the new value. See [`removeMetadata`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#removemetadata).

param 1`string` Metadata key
param 2`string` Metadata value for this page session.
returns`undefined`
Since[`2.2.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

if (window.TrackJS) { TrackJS.addMetadata("user_subscription", "professional"); TrackJS.addMetadata("user_role", "owner"); TrackJS.addMetadata("server", "YOUR_SERVER_ID");}

import { TrackJS } from "trackjs";TrackJS.addMetadata("user_subscription", "professional");TrackJS.addMetadata("user_role", "owner");TrackJS.addMetadata("server", "YOUR_SERVER_ID");

if (window.trackJs) { trackJs.addMetadata("user_subscription", "professional"); trackJs.addMetadata("user_role", "owner"); trackJs.addMetadata("server", "YOUR_SERVER_ID");}

* * *

[attempt](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#attempt "Permalink Here")
-------------------------------------------------------------------------------------------------------

Function

Invoke a function with a `try-catch` wrapper and report any errors to TrackJS. Context to invoke the function and parameters can be passed as additional parameters.

param 1`function` Function to invoke
param 2`Object` (Optional) Context to invoke the function on. IE, `this`.
param …n`Any` (Optional) Parameters to pass to the function when invoked.
returns`*` Output from the invoked function.
Since[`1.2.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-1 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

TrackJS.attempt(function multiply(a, b) { return a*b;}, {}, 4, 8); // 32

import { TrackJS } from "trackjs";TrackJS.attempt(function multiply(a, b) { return a*b;}, {}, 4, 8); // 32

trackJs.attempt(function multiply(a, b) { return a*b;}, {}, 4, 8); // 32

* * *

[configure](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#configure "Permalink Here")
-----------------------------------------------------------------------------------------------------------

Function

Update the [Agent Config](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/) after install. Not all options can be updated, see the `Changeable` flag in the Config SDK.

param 1`Object` Options to be updated
returns`boolean``true` if successful
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-2 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && TrackJS.configure({ userId: "sam@customer.com", sessionId: "17734FEB342"});

import { TrackJS } from "trackjs";TrackJS.configure({ userId: "sam@customer.com", sessionId: "17734FEB342"});

window.trackJs && trackJs.configure({ userId: "sam@customer.com", sessionId: "17734FEB342"});

* * *

[console.log](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#consolelog "Permalink Here")
--------------------------------------------------------------------------------------------------------------

Function

Record a Telemetry event into the log with _default_ severity. The `TrackJS.console.log` function is a private clone of the global `console.log` for context that is relevant for debugging, but should not be displayed in the browser console.

param …n`Any` properties to be logged
returns`undefined`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-3 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && TrackJS.console.log("it's happening!", { foo: "bar" });

import { TrackJS } from "trackjs";TrackJS.console.log("it's happening!", { foo: "bar" });

window.trackJs && trackJs.console.log("it's happening!", { foo: "bar" });

* * *

[console.debug](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#consoledebug "Permalink Here")
------------------------------------------------------------------------------------------------------------------

Function

Record a Telemetry event into the log with _debug_ severity. The `TrackJS.console.debug` function is a private clone of the global `console.debug` for context that is relevant for debugging, but should not be displayed in the browser console.

param …n`Any` properties to be logged
returns`undefined`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-4 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && TrackJS.console.debug("it's happening!", { foo: "bar" });

import { TrackJS } from "trackjs";TrackJS.console.debug("it's happening!", { foo: "bar" });

window.trackJs && trackJs.console.debug("it's happening!", { foo: "bar" });

* * *

[console.info](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#consoleinfo "Permalink Here")
----------------------------------------------------------------------------------------------------------------

Function

Record a Telemetry event into the log with _info_ severity. The `TrackJS.console.info` function is a private clone of the global `console.info` for context that is relevant for debugging, but should not be displayed in the browser console.

param …n`Any` properties to be logged
returns`undefined`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-5 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && TrackJS.console.info("it's happening!", { foo: "bar" });

import { TrackJS } from "trackjs";TrackJS.console.info("it's happening!", { foo: "bar" });

window.trackJs && trackJs.console.info("it's happening!", { foo: "bar" });

* * *

[console.warn](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#consolewarn "Permalink Here")
----------------------------------------------------------------------------------------------------------------

Function

Record a Telemetry event into the log with _warning_ severity. The `TrackJS.console.warn` function is a private clone of the global `console.warn` for context that is relevant for debugging, but should not be displayed in the browser console.

param …n`Any` properties to be logged
returns`undefined`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-6 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && TrackJS.console.warn("it's happening!", { foo: "bar" });

import { TrackJS } from "trackjs";TrackJS.console.warn("it's happening!", { foo: "bar" });

window.trackJs && trackJs.console.warn("it's happening!", { foo: "bar" });

* * *

[console.error](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#consoleerror "Permalink Here")
------------------------------------------------------------------------------------------------------------------

Function

Record a Telemetry event into the log with _error_ severity. The `TrackJS.console.error` function is a private clone of the global `console.error` for context that is relevant for debugging, but should not be displayed in the browser console.

If the [`console.error`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#consoleerror) option is on, which is the default, this will also send an error report.

param …n`Any` properties to be logged
returns`undefined`
Since[`1.0.1`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-7 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && TrackJS.console.error("it's happening!", { foo: "bar" });

import { TrackJS } from "trackjs";TrackJS.console.error("it's happening!", { foo: "bar" });

window.trackJs && trackJs.console.error("it's happening!", { foo: "bar" });

* * *

[install](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#install "Permalink Here")
-------------------------------------------------------------------------------------------------------

Function

Installs the agent into the current document and start reporting errors with the provided [Config](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/) options.

Before [`3.0.0`](https://docs.trackjs.com/browser-agent/changelog/), initializing the agent was automatic as soon as the script was loaded. Config was passed by creating a `window._trackJs` object with the properties.

param`Config` Options to install with.
returns`boolean``true` if successful.
Since[`3.0.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-8 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN" // other config options});

import { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN" // other config options});

<script> window._trackJs = { token: "YOUR_TOKEN" // other config options};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

[isInstalled](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#isinstalled "Permalink Here")
---------------------------------------------------------------------------------------------------------------

Function

Whether the agent has been installed into the current environment. See [`install`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#install).

returns`boolean`
Since[`3.4.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-9 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && !TrackJS.isInstalled() && TrackJS.install({ token: "YOUR_TOKEN" // other config options});

import { TrackJS } from "trackjs";if (!TrackJS.isInstalled()) { TrackJS.install({ token: "YOUR_TOKEN" // other config options });}

<script> window._trackJs = { token: "YOUR_TOKEN" // other config options};</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

* * *

Function

Removes a key, and any associated value, from the metadata store for this page session. The key will no longer be included with reported errors.

See [`addMetadata`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#addmetadata).

param 1`string` Metadata key
returns`undefined`
Since[`2.2.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-10 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

if (window.TrackJS) { TrackJS.removeMetadata("user_subscription");}

import { TrackJS } from "trackjs";TrackJS.removeMetadata("user_subscription");

if (window.trackJs) { trackJs.removeMetadata("user_subscription");}

* * *

[track](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#track "Permalink Here")
---------------------------------------------------------------------------------------------------

Function

Reports an error to TrackJS immediately with the provided error. If the parameter is not an `Error`, one will be generated using the serialized parameter as the message.

The reported error will include all Telemetry logged by the agent.

param 1`Any` Error to be reported
returns`undefined`
Since[`1.2.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-11 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && TrackJS.track("State.property should be positive");

import { TrackJS } from "trackjs";TrackJS.track("State.property should be positive");

window.trackJs && trackJs.track("State.property should be positive");

* * *

[version](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#version "Permalink Here")
-------------------------------------------------------------------------------------------------------

String

The version of the agent.

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-12 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

window.TrackJS && TrackJS.version; // 3.0.0

import { TrackJS } from "trackjs";TrackJS.version; // 3.0.0

window.trackJs && trackJs.version; // 3.0.0

* * *

[watch](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#watch "Permalink Here")
---------------------------------------------------------------------------------------------------

Function

Creates a wrapper around a function that automatically reports any errors that occur. Context for the function can be passed as additional argument.

param 1`function` Function to be wrapped.
param 2`Object` (Optional) Context to invoke the function on. IE, `this`.
returns`*` Return value of the function.
Since[`1.2.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-13 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

var protectedFn = TrackJS.watch(function(a, b) { throw new Error("oops");}, this); protectedFn(1, 2); // Error is reported and rethrown as "TrackJS Caught: oops"

import { TrackJS } from "trackjs";var protectedFn = TrackJS.watch(function(a, b) { throw new Error("oops");}, this); protectedFn(1, 2); // Error is reported and rethrown as "TrackJS Caught: oops"

var protectedFn = trackJs.watch(function(a, b) { throw new Error("oops");}, this); protectedFn(1, 2); // Error is reported and rethrown as "TrackJS Caught: oops"

* * *

[watchAll](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#watchall "Permalink Here")
---------------------------------------------------------------------------------------------------------

Function

Replaces all the functions on an object with [watch](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#watch) wrappers of all the functions. This is useful for watching all the methods on a Class.

param 1`function` Function to be wrapped.
param 2`Object` (Optional) Context to invoke the function on. IE, `this`.
returns`*` Return value of the function.
Since[`1.2.0`](https://docs.trackjs.com/browser-agent/changelog/)

### [Example](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#example-14 "Permalink Here")

[Global](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Module](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)[Legacy](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)

var protectedModel = TrackJS.watchAll(myModel); protectedModel.foo(1, 2); // Errors will be reported and rethrown

import { TrackJS } from "trackjs";var protectedModel = TrackJS.watchAll(myModel); protectedModel.foo(1, 2); // Errors will be reported and rethrown

var protectedModel = trackJs.watchAll(myModel); protectedModel.foo(1, 2); // Errors will be reported and rethrown

* * *
