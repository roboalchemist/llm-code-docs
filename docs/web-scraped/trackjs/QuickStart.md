# Source: https://docs.trackjs.com/QuickStart/

Title: QuickStart

URL Source: https://docs.trackjs.com/QuickStart/

Markdown Content:
Welcome to TrackJS! Let’s get you started with the most commmon configuration options to get you back to fixing bugs.

[Installation](https://docs.trackjs.com/QuickStart/#installation "Permalink Here")
----------------------------------------------------------------------------------

Once you’ve [created your account with TrackJS](https://trackjs.com/signup), you’ll need to install the agent in your website. You can do this by either referencing it from our CDN, or by taking a dependency on our [npm package](https://www.npmjs.com/package/trackjs) and bundling it into your application.

[Global](https://docs.trackjs.com/QuickStart/)[Module](https://docs.trackjs.com/QuickStart/)[Legacy](https://docs.trackjs.com/QuickStart/)

<script src="https://cdn.trackjs.com/agent/v3/latest/t.js"></script><script> window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN" });</script>

[Standard agent installation](https://docs.trackjs.com/QuickStart/#code-standard-agent-installation)

// ES6 Modular JavaScript.// npm install trackjs --saveimport { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN"});

[Standard agent installation](https://docs.trackjs.com/QuickStart/#code-standard-agent-installation)

<!-- Legacy agent deprecated 2018-10-31 --><script> window._trackJs = { token: "YOUR_TOKEN" };</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

[Standard agent installation](https://docs.trackjs.com/QuickStart/#code-standard-agent-installation)

The `token` is the only required option. You can find it on your [Dashboard](https://my.trackjs.com/install).

For more options on installing the agent, check the [Installation page](https://docs.trackjs.com/browser-agent/installation/).

[Applications](https://docs.trackjs.com/QuickStart/#applications "Permalink Here")
----------------------------------------------------------------------------------

TrackJS Applications allow you to segment your error data by codebase or environment. Each codebase you want to protect should have it’s own application key, in addition to each deployed environment. This is done by [creating application keys in the TrackJS Dashboard](https://my.trackjs.com/onboarding/applications), and assigning them to the [`application`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#application) install option.

For example, let’s say your main web application is deployed to a “production” environment for real users, and a “test” environment for internal testing. You wouldn’t want noisy test data clouding your reports about production or setting off alerts. You would create 2 applications: `my-app-prod` and `my-app-test`. After creating the application keys, update your agent config with the `application` key:

[Global](https://docs.trackjs.com/QuickStart/)[Module](https://docs.trackjs.com/QuickStart/)[Legacy](https://docs.trackjs.com/QuickStart/)

<script src="https://cdn.trackjs.com/agent/v3/latest/t.js"></script><script> window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", application: "my-app-prod" });</script>

[Installing the agent with Applications](https://docs.trackjs.com/QuickStart/#code-installing-the-agent-with-applications)

// ES6 Modular JavaScript.// npm install trackjs --saveimport { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN", application: "my-app-prod"});

[Installing the agent with Applications](https://docs.trackjs.com/QuickStart/#code-installing-the-agent-with-applications)

<!-- Legacy agent deprecated 2018-10-31 --><script> window._trackJs = { token: "YOUR_TOKEN", application: "my-app-prod" };</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

[Installing the agent with Applications](https://docs.trackjs.com/QuickStart/#code-installing-the-agent-with-applications)

You may also want to protect other codebases with TrackJS, such as another application or your public website. You’ll want to create more applications for each of them to see which are having trouble. You would create additional applications: `public-website-prod` and `public-website-test`.

Applications are a flexible way to segment your data and get more actionable reports. For more, checkout the [Applications page](https://docs.trackjs.com/data-management/applications/).

[Adding Context](https://docs.trackjs.com/QuickStart/#adding-context "Permalink Here")
--------------------------------------------------------------------------------------

TrackJS captures lots of context about the running browser, network, and application automatically. But your error reports become even better if you tell us more about your environment.

### [Setting userId, sessionId, and version](https://docs.trackjs.com/QuickStart/#setting-userid-sessionid-and-version "Permalink Here")

When installing the agent, you can specify a [`userId`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#userid) of the current user, [`sessionId`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#sessionid), and a [`version`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#version) of the running application. These will be available in the Dashboard for all errors reported.

[Global](https://docs.trackjs.com/QuickStart/)[Module](https://docs.trackjs.com/QuickStart/)[Legacy](https://docs.trackjs.com/QuickStart/)

<script src="https://cdn.trackjs.com/agent/v3/latest/t.js"></script><script> window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", userId: "user@customer.com", sessionId: "user+2018-12-07T00:00:00.000Z+1", version: "1.2.4" });</script>

[Adding userId, sessionId, and version context](https://docs.trackjs.com/QuickStart/#code-adding-userid-sessionid-and-version-context)

// ES6 Modular JavaScript.// npm install trackjs --saveimport { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN", userId: "user@customer.com", sessionId: "user+2018-12-07T00:00:00.000Z+1", version: "1.2.4"});

[Adding userId, sessionId, and version context](https://docs.trackjs.com/QuickStart/#code-adding-userid-sessionid-and-version-context)

<!-- Legacy agent deprecated 2018-10-31 --><script> window._trackJs = { token: "YOUR_TOKEN", userId: "user@customer.com", sessionId: "user+2018-12-07T00:00:00.000Z+1", version: "1.2.4" };</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

[Adding userId, sessionId, and version context](https://docs.trackjs.com/QuickStart/#code-adding-userid-sessionid-and-version-context)

If you do not provide a `userId`, we will generate one automatically based on the user’s IP Address and userAgent string.

### [Setting Metadata](https://docs.trackjs.com/QuickStart/#setting-metadata "Permalink Here")

You can get even more context by adding metadata about the current session. TrackJS metadata can be any property you find interesting about your environment, and give you the ability to filter by that property. For example, you could set the subscription level of the current user, what class of customer they belong to, or whether a feature has been enabled for them.

[Global](https://docs.trackjs.com/QuickStart/)[Module](https://docs.trackjs.com/QuickStart/)[Legacy](https://docs.trackjs.com/QuickStart/)

<script src="https://cdn.trackjs.com/agent/v3/latest/t.js"></script><script> if (window.TrackJS) { TrackJS.install({ token: "YOUR_TOKEN" }); TrackJS.addMetadata("subscription", "professional"); TrackJS.addMetadata("has_sourcemaps", "false"); }</script>

[Adding Metadata](https://docs.trackjs.com/QuickStart/#code-adding-metadata)

// ES6 Modular JavaScript.// npm install trackjs --saveimport { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN"});TrackJS.addMetadata("subscription", "professional");TrackJS.addMetadata("has_sourcemaps", "false");

[Adding Metadata](https://docs.trackjs.com/QuickStart/#code-adding-metadata)

<!-- Legacy agent deprecated 2018-10-31 --><script> window._trackJs = { token: "YOUR_TOKEN" };</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script><script> window.trackJs && trackJs.addMetadata("subscription", "professional"); window.trackJs && trackJs.addMetadata("has_sourcemaps", "false");</script>

[Adding Metadata](https://docs.trackjs.com/QuickStart/#code-adding-metadata)

Metadata can be added at any time, before or after the agent has been installed. Each error has a “metadata” section where you can see the keys reported. You can also [see all the metadata reported](https://my.trackjs.com/metadata) and filter by values in the Dashboard.

### [Logging State](https://docs.trackjs.com/QuickStart/#logging-state "Permalink Here")

You may want to include context about the state of your application with error reports. The easiest way to do this is to log state changes to the `console.log`. Every message written to the console will be included with TrackJS error reports.

Check out the [Tips & Tricks](https://docs.trackjs.com/browser-agent/tips-and-tricks/state-telemetry/) for how to do this with your application.

[Error Reporting](https://docs.trackjs.com/QuickStart/#error-reporting "Permalink Here")
----------------------------------------------------------------------------------------

The TrackJS agent automatically reports errors from several sources:

*   A globally unhandled error from `window.onerror`
*   A unhandled Promise rejection
*   An error thrown from a native callback function like `setTimeout`
*   A message written to `console.error`
*   A network request completed with a status of 400 or greater

Each of these can be configured with [install options](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/). You can also manually report an error using [`TrackJS.track()`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#track). This is useful if you have an known interesting situation in your code you want to report on, or for testing out the integration.

[Minified Sources](https://docs.trackjs.com/QuickStart/#minified-sources "Permalink Here")
------------------------------------------------------------------------------------------

When you view an error report, we will attempt to retrieve the JavaScript files referenced in the stack trace, and “prettify” them so you can understand what code is being referenced. But if you have minified your JavaScript, the Stack Traces in your error reports may not look familiar to you.

We recommend that you generate Source Maps as a part of your build process, and make them available to us. If we can find a Source Map for your files, you’ll see your original source code when we process your Stack Traces, making it much easier to understand what was running.

For more information on setting up source maps, check out [Minified Sources](https://docs.trackjs.com/data-management/minified-sources/).

[Browser Compatibility](https://docs.trackjs.com/QuickStart/#browser-compatibility "Permalink Here")
----------------------------------------------------------------------------------------------------

The TrackJS agent is tested and supported on the following browsers:

*   Android Browser (4.0 and greater)
*   Chrome (20 and greater)
*   Edge (all versions)
*   Firefox (4.0 and greater)
*   Internet Explorer (8.0 and greater)1
*   Mobile Safari (7.1 and greater)
*   Opera (2013 and newer)
*   Safari (5.0 and greater)

1 Internet Explorer 8.0 does not support the capture of network errors.

[Integrations](https://docs.trackjs.com/QuickStart/#integrations "Permalink Here")
----------------------------------------------------------------------------------

Although not required, [you can integrate TrackJS](https://docs.trackjs.com/browser-agent/integrations/) with your JavaScript frameworks, build tools, and other analytics tools to get better reporting. We specifically recommend checking out:

*   [Integrating with Angular 2+](https://docs.trackjs.com/browser-agent/integrations/angular2/) ([Angular 1](https://docs.trackjs.com/browser-agent/integrations/angular1/)) - Better error messages for Angular
*   [Integrating with React/Redux](https://docs.trackjs.com/browser-agent/integrations/react-redux/) - Application State context

[Next Steps](https://docs.trackjs.com/QuickStart/#next-steps "Permalink Here")
------------------------------------------------------------------------------

*   [Tips and Tricks](https://docs.trackjs.com/browser-agent/tips-and-tricks/)
*   [Ignoring Errors](https://docs.trackjs.com/data-management/ignore/)
*   [Handling Sensitive Data](https://docs.trackjs.com/data-management/sensitive/)
*   [Alerting and Notifications](https://docs.trackjs.com/notifications/)
*   [Troubleshoot your installation](https://docs.trackjs.com/browser-agent/troubleshooting/)
*   [Get Help](https://docs.trackjs.com/support/)
