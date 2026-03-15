# Source: https://docs.trackjs.com/browser-agent/installation/

Title: Installation

URL Source: https://docs.trackjs.com/browser-agent/installation/

Markdown Content:
You install the Browser Agent by including the script on your website. The agent script listens for errors and other events to be reported back to your TrackJS Dashboard. The agent is lightweight and dependency free.

Here is the default installation method for loading from our CDN, bundling as a module, or using the legacy client (earlier than 3.0.0). Loading from the CDN is the easiest way to get started, especially if you don’t already use a module bundler (like Webpack).

[Global](https://docs.trackjs.com/browser-agent/installation/)[Module](https://docs.trackjs.com/browser-agent/installation/)[Legacy](https://docs.trackjs.com/browser-agent/installation/)

<script src="https://cdn.trackjs.com/agent/v3/latest/t.js"></script><script> window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN" });</script>

[Standard agent installation](https://docs.trackjs.com/browser-agent/installation/#code-standard-agent-installation)

// ES6 Modular JavaScript.// npm install trackjs --saveimport { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN"});

[Standard agent installation](https://docs.trackjs.com/browser-agent/installation/#code-standard-agent-installation)

<!-- Legacy agent deprecated 2018-10-31 --><script> window._trackJs = { token: "YOUR_TOKEN" };</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

[Standard agent installation](https://docs.trackjs.com/browser-agent/installation/#code-standard-agent-installation)

[Install Options](https://docs.trackjs.com/browser-agent/installation/#install-options "Permalink Here")
--------------------------------------------------------------------------------------------------------

In addition to `token`, there are [lots of options you can pass](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/) when installing the agent to better integrate with your application. Options can be used to:

*   add custom context to your errors
*   disable agent behaviors
*   customize reporting behavior

If you need the agent to do something specialized, checkout the [onError](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#onerror) option that allows you to manipulate errors before they are reported.

[Crossorigin](https://docs.trackjs.com/browser-agent/installation/#crossorigin "Permalink Here")
------------------------------------------------------------------------------------------------

If you are installing the TrackJS agent from our CDN, the script will be loaded from a different `origin` than your page. This can sometimes cause errors to be obfuscated as `"Script Error"`[due to the browser’s Same-Origin Policy](https://trackjs.com/blog/script-error-javascript-forensics/).

For this reason, [we recommend including the agent as a module and bundling it with your other scripts](https://docs.trackjs.com/browser-agent/installation/#bundling-as-a-module), hosted from your own domains. If this is not feasible for you, you can also decorate the script with the `crossorigin` attribute to attempt to bypass the Same-Origin policy.

<script src="https://cdn.trackjs.com/agent/v3/latest/t.js" crossorigin></script><script> window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN" });</script>

[Using the crossorigin attribute](https://docs.trackjs.com/browser-agent/installation/#code-using-the-crossorigin-attribute)

Be aware that not all browsers support the crossorigin attribute, and networks can block the delivery of CORS headers required for it to function. [Check out Crossorigin Scripts and Corporate Proxies](https://trackjs.com/blog/crossorigin-scripts-and-corporate-proxies/) for more.

[Safety Checking](https://docs.trackjs.com/browser-agent/installation/#safety-checking "Permalink Here")
--------------------------------------------------------------------------------------------------------

It is not uncommon for scripts to fail to load in production. Slow devices, flaky connections, network middleware, and browser extensions can call interfere with a script loading.

Anytime you are referencing a script that loads separately, you should perform a Safety Check that it has loaded. Otherwise, you might encounter an error like `ReferenceError: TrackJS is not defined`, and stop execution of your code prematurely.

When you load the agent from our cdn, or as a standalone script, safety check to make sure the agent has loaded before calling a method. This looks like `window.TrackJS && TrackJS.someMethod()`. This is performing a logical operation to check if `window.TrackJS` exists before attempting to call the method.

If you are [bundling the agent as a module](https://docs.trackjs.com/browser-agent/installation/#bundling-as-a-module) with your code, this safety check is probably unnecessary.

[Auto Install](https://docs.trackjs.com/browser-agent/installation/#auto-install "Permalink Here")
--------------------------------------------------------------------------------------------------

You can configure the agent to automatically install itself as soon as it is loaded by creating a [config object](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/) on `window._trackJs`. This is useful if you do not know when the agent may be loaded.

This was the default mechanism of installation before agent version 3.0.0.

[Versions](https://docs.trackjs.com/browser-agent/installation/#versions "Permalink Here")
------------------------------------------------------------------------------------------

The latest version of the agent is published to our CDN at [`https://cdn.trackjs.com/agent/v3/latest/t.js`](https://cdn.trackjs.com/agent/v3/latest/t.js). You can also find it on [GitHub](https://github.com/TrackJs/trackjs-package) and [npm](https://www.npmjs.com/package/trackjs). All the version information is available in the [changelog](https://docs.trackjs.com/browser-agent/changelog/).

The Agent is periodically updated with new capabilities and fixes for browser variations. We recommend referencing a **specific version** of the agent so that you control when changes are introduced in your application.

To be notified when a new version of the agent is released, you can [subscribe to the GitHub package for releases](https://github.com/TrackJs/trackjs-package), or [join the agent release mailing list](http://eepurl.com/c1LPwj).

[Placement](https://docs.trackjs.com/browser-agent/installation/#placement "Permalink Here")
--------------------------------------------------------------------------------------------

When the agent is installed, it wraps the browser’s native functions to capture context and report errors. Errors and events that occur before the agent is installed will not be recorded. Therefore, we recommend that you reference and install the agent **as early as possible** in the page.

If you are referencing the agent as a script tag, which is the default, the agent should be the **first script in the document**. If you are bundling the agent, make sure that [`TrackJS.install()`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#install) is called as soon as possible during initialization.

Initialization errors are very common for web applications. Delaying the installation of the TrackJS agent can create dangerous blindspots to these kinds of errors.

[Bundling as a Module](https://docs.trackjs.com/browser-agent/installation/#bundling-as-a-module "Permalink Here")
------------------------------------------------------------------------------------------------------------------

The agent is published to [npm](https://www.npmjs.com/package/trackjs) and supports ES6, CommonJS, and AMD modules. Below are some common use cases, which expect you’ve already included the agent from npm (`npm install trackjs --save`).

import { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN" });

[Bundling the Agent as a ES6 Module](https://docs.trackjs.com/browser-agent/installation/#code-bundling-the-agent-as-a-es6-module)

var TrackJS = require("trackjs").TrackJS;TrackJS.install({ token: "YOUR_TOKEN" });

[Bundling the Agent as a CommonJS Module](https://docs.trackjs.com/browser-agent/installation/#code-bundling-the-agent-as-a-commonjs-module)

require.config({ paths: { "TrackJS": "/node_modules/trackjs/t.js" }});require(["TrackJS"], function(TrackJS) { TrackJS.install({ token: "YOUR_TOKEN" }); });

[Bundling the Agent as a AMD Module](https://docs.trackjs.com/browser-agent/installation/#code-bundling-the-agent-as-a-amd-module)

[Async](https://docs.trackjs.com/browser-agent/installation/#async "Permalink Here")
------------------------------------------------------------------------------------

Although we [strongly recommend against it](https://docs.trackjs.com/browser-agent/installation/#placement), you may want to load the agent asynchronously to reduce page load time. You can effectively do this by using the [async attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), which will load and execute the script when the browser is ready. For example,

<script> window._trackJs = { token: "TOKEN" };</script><script async src="https://cdn.trackjs.com/agent/v3/latest/t.js></script>

[Loading the agent asynchronously](https://docs.trackjs.com/browser-agent/installation/#code-loading-the-agent-asynchronously)

This code utilizes the [Automatic Install](https://docs.trackjs.com/browser-agent/installation/#auto-install) method of installation, which will install the agent as soon as it is loaded if it detects a `window._trackJs` config object.

[Content-Security](https://docs.trackjs.com/browser-agent/installation/#content-security "Permalink Here")
----------------------------------------------------------------------------------------------------------

If you are using a [Content-Security Policy](https://docs.trackjs.com/browser-agent/installation/) to secure the scripts on your page, here are the directives you’ll need to ensure TrackJS functions properly.

script-src https://cdn.trackjs.com; connect-src https://capture.trackjs.com; img-src https://usage.trackjs.com; img-src https://fault.trackjs.com

[CSP Directives for the Agent](https://docs.trackjs.com/browser-agent/installation/#code-csp-directives-for-the-agent)

[Developing Locally](https://docs.trackjs.com/browser-agent/installation/#developing-locally "Permalink Here")
--------------------------------------------------------------------------------------------------------------

The agent can interfere with your development on local environments. You may see that console messages all appear from `t.js`, or that your debugger is stepping through our minified code.

If you are developing using either **Chrome**, [Blackboxing](https://developer.chrome.com/devtools/docs/blackboxing) the agent script will remove these console annoyances and bypass our agent in your debugger.

You may prefer to disable the agent entirely on local environments to cut down on noise in your Dashboard. Assuming your local environment is hosted at `localhost`, here is how you can do that:

[Global](https://docs.trackjs.com/browser-agent/installation/)[Module](https://docs.trackjs.com/browser-agent/installation/)[Legacy](https://docs.trackjs.com/browser-agent/installation/)

<script src="https://cdn.trackjs.com/agent/v3/latest/t.js"></script><script> if (location.host.indexOf("localhost") !== 0) { window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN" }); }</script>

[Excluding localhost from Install](https://docs.trackjs.com/browser-agent/installation/#code-excluding-localhost-from-install)

// ES6 Modular JavaScript.// npm install trackjs --saveimport { TrackJS } from "trackjs";if (location.host.indexOf("localhost") !== 0) { TrackJS.install({ token: "YOUR_TOKEN" });}

[Excluding localhost from Install](https://docs.trackjs.com/browser-agent/installation/#code-excluding-localhost-from-install)

<!-- Legacy agent deprecated 2018-10-31 --><script> window._trackJs = { token: "YOUR_TOKEN", enabled: location.host.indexOf("localhost") !== 0 };</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

[Excluding localhost from Install](https://docs.trackjs.com/browser-agent/installation/#code-excluding-localhost-from-install)
