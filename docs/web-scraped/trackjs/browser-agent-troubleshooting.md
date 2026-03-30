# Source: https://docs.trackjs.com/browser-agent/troubleshooting/

Title: Troubleshooting

URL Source: https://docs.trackjs.com/browser-agent/troubleshooting/

Markdown Content:
Here are some things to check if you are having trouble getting started. If you cannot find an answer to your question, [send us an email](mailto:hello@trackjs.com) anytime.

[Agent Must Be Installed](https://docs.trackjs.com/browser-agent/troubleshooting/#agent-must-be-installed "Permalink Here")
---------------------------------------------------------------------------------------------------------------------------

If you are attempting to call one of the [Agent Methods](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/), but seeing an error in the console that `TrackJS: Agent must be installed`, then check:

*   The call to [`TrackJS.install()`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#install) must occur before any other methods may be called. Make sure that your code where the agent is installed executes as early as possible. See [Installation](https://docs.trackjs.com/browser-agent/installation/) for more.

[Already Installed](https://docs.trackjs.com/browser-agent/troubleshooting/#already-installed "Permalink Here")
---------------------------------------------------------------------------------------------------------------

The agent can only be installed once into the document, and only the first call to `TrackJS.install()` is processed. If you are seeing `TrackJS: already installed.` in your console, then check:

*   Search your code for `TrackJS.install`, make sure it is only being called once.
*   Check that any browser plugins you may be using are not injecting TrackJS onto the page.

[Missing Token](https://docs.trackjs.com/browser-agent/troubleshooting/#missing-token "Permalink Here")
-------------------------------------------------------------------------------------------------------

When you load the page, you see an error in console that `TrackJS: missing token`, then check:

*   Your call to [`TrackJS.install()`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#install) includes the required `token` property. If you inject the token from your configuration dynamically, make sure that the injection is working.

[Monitoring Disabled in Node](https://docs.trackjs.com/browser-agent/troubleshooting/#monitoring-disabled-in-node "Permalink Here")
-----------------------------------------------------------------------------------------------------------------------------------

The agent has been installed in a NodeJS environment, perhaps as part of an isomorphic web rendering. The agent does not currently support the NodeJS environment and will not record errors. It has safely disabled itself and will not impact your application.

[No Data](https://docs.trackjs.com/browser-agent/troubleshooting/#no-data "Permalink Here")
-------------------------------------------------------------------------------------------

If you have have attempted to send an error using [`TrackJS.track()`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#track), but you do not see any data in your TrackJS Dashboard, then check the following things:

*   Confirm you have used the correct `token` for your account when calling [`TrackJS.install()`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#install).
*   Once `TrackJS.track()` has been called, do you see a network request to the [`Capture API`](https://docs.trackjs.com/data-api/capture/).
*   If you have setup [Application Segments](https://docs.trackjs.com/data-management/applications/), make sure you are sending the correct `application` key when calling `TrackJS.install()`.
*   Check your [Dashboard Filters](https://docs.trackjs.com/data-management/filters/) to make sure you are showing the **Application**, **Domains**, **Time Ranges**, and other facets that might exclude your errors from view.

**NOTE** Some adblockers with aggressive settings may block the reporting of errors. If your `Capture` requests are failing, make sure your adblocker is disabled.

[TrackJS is not Defined](https://docs.trackjs.com/browser-agent/troubleshooting/#trackjs-is-not-defined "Permalink Here")
-------------------------------------------------------------------------------------------------------------------------

If you are attempting to call one of the [Agent Methods](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/), but seeing a ReferenceError in console that `TrackJS is not defined`, then check:

*   If you are bundling the agent as a module, make sure that the agent code has been included and loaded before attempting to use it.
*   If you are referencing the agent as a script, make sure the script tag is as early in the load order as possible. Ideally it should be the first `<script>` on the page.
*   Make sure you have your adblockers disabled. Aggressive adblockers may prevent the agent from loading.

[Script Error](https://docs.trackjs.com/browser-agent/troubleshooting/#script-error "Permalink Here")
-----------------------------------------------------------------------------------------------------

If your errors in the TrackJS Dashboard are missing context and only showing the message `Script error`, then check:

*   If you are loading your JavaScript from a different origin domain than your document, the **Same-Origin Policy** of the browser will obfuscate the errors. You can decorate the script tags with the attribute `cross-origin="anonymous"` to bypass this policy
*   Check out our [Forensic Report on Script Error](https://trackjs.com/blog/script-error-javascript-forensics/) for more info.
