# Source: https://docs.trackjs.com/data-management/grouping/

Title: Grouping Errors

URL Source: https://docs.trackjs.com/data-management/grouping/

Markdown Content:
There can be a lot of variability in your error data that can cause noise. For example, error messages containing ids or URLs containing cache-busters. To improve the quality of your TrackJS reports, we recommend adding some Grouping Logic in either the Group Builder or the Agent Grouping below.

[Group Builder](https://docs.trackjs.com/data-management/grouping/#group-builder "Permalink Here")
--------------------------------------------------------------------------------------------------

The Group Builder allows you to [create rules in the TrackJS Dashboard](https://my.trackjs.com/Account/ErrorGrouping) to automatically group together Error `Message` and `URL` patterns.

Dynamic parts are indicated using “Replacements”, which are lazy wildcard regex matches. There are two types of replacements, named and hidden. They both have the same matching behavior, but affect the resulting group differently.

The builder provides some testing capability, allowing you to enter test patterns and showing data from your account that would match the pattern.

### [Named Replacements](https://docs.trackjs.com/data-management/grouping/#named-replacements "Permalink Here")

Use `${name}` to create “named replacements” in groups. For example, say you have the following Error URLs:

*   `https://example.com/1234/details`
*   `https://example.com/abcd/details`

You create a grouping `https://example.com/${id}/details` that will match both of these URLS and combine them in to a single UI entry with the URL, “https://example.com/${id}/details”.

### [Hidden Replacements](https://docs.trackjs.com/data-management/grouping/#hidden-replacements "Permalink Here")

Use an empty `${}` to create “hidden replacements” in groups. For example, say you have the following Error Message:

*   `TypeError: undefined is not a function`
*   `undefined is not a function`

Some browsers prefix the error type, and some do not. Creating a group like `${}undefined is not a function` will result in a single message in the UI with the message, “undefined is not a function”. We drop the empty `${}` replacement sections from the visible message.

[Agent Grouping](https://docs.trackjs.com/data-management/grouping/#agent-grouping "Permalink Here")
----------------------------------------------------------------------------------------------------

If your grouping rules are too complex for the Group Builder above, we can add them using the agent [`onError callback`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#onerror). The callback will be invoked with the [capture payload](https://docs.trackjs.com/data-api/capture/#request-payload) every time an error has been detected. You can manipulate the payload to add your own grouping logic.

For example, let’s consider that you want to remove a cache-buster querystring parameter `x` from all your error URLs. We can’t predict where the `x` parameter will occur, it might be the first parameter, it might be the last.

[Global](https://docs.trackjs.com/data-management/grouping/)[Module](https://docs.trackjs.com/data-management/grouping/)[Legacy](https://docs.trackjs.com/data-management/grouping/)

window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", onError: function(payload) { if (payload.url.indexOf("x") >= 0) { // Regular expression strips out the x=ANYTHING querystring parameter. payload.url = payload.url.replace(/x=[^\&]+[\&]?/gi, ""); } // Return truthy to proceed with error report. return true; }});

[remove cache-buster querystring example](https://docs.trackjs.com/data-management/grouping/#code-remove-cache-buster-querystring-example)

import { TrackJS } from "trackjs";TrackJS.install({ token: "YOUR_TOKEN", onError: function(payload) { if (payload.url.indexOf("x") >= 0) { // Regular expression strips out the x=ANYTHING querystring parameter. payload.url = payload.url.replace(/x=[^\&]+[\&]?/gi, ""); } // Return truthy to proceed with error report. return true; }});

[remove cache-buster querystring example](https://docs.trackjs.com/data-management/grouping/#code-remove-cache-buster-querystring-example)

window._trackJs = { token: "YOUR_TOKEN", onError: function(payload) { if (payload.url.indexOf("x") >= 0) { // Regular expression strips out the x=ANYTHING querystring parameter. payload.url = payload.url.replace(/x=[^\&]+[\&]?/gi, ""); } // Return truthy to proceed with error report. return true; }};

[remove cache-buster querystring example](https://docs.trackjs.com/data-management/grouping/#code-remove-cache-buster-querystring-example)
