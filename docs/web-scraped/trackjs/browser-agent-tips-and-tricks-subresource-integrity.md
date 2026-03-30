# Source: https://docs.trackjs.com/browser-agent/tips-and-tricks/subresource-integrity/

Title: Subresource Integrity Checks (SRI)

URL Source: https://docs.trackjs.com/browser-agent/tips-and-tricks/subresource-integrity/

Markdown Content:
Subresource Integrity Checks (SRI) - TrackJS Docs
===============

☰

 - [x] 

[![Image 1: TrackJS](https://docs.trackjs.com/assets/images/logo_charcoal_red.svg)](https://trackjs.com/)

☌

1.   [QuickStart](https://docs.trackjs.com/QuickStart/)
2.   [Browser Agent](https://docs.trackjs.com/browser-agent/)
    1.   [Installation](https://docs.trackjs.com/browser-agent/installation/)
    2.   [Integrations](https://docs.trackjs.com/browser-agent/integrations/)
        1.   [Angular](https://docs.trackjs.com/browser-agent/integrations/angular2/)
        2.   [Axios](https://docs.trackjs.com/browser-agent/integrations/axios/)
        3.   [NextJS](https://docs.trackjs.com/browser-agent/integrations/nextjs16/)
        4.   [React](https://docs.trackjs.com/browser-agent/integrations/react/)
        5.   [Redux](https://docs.trackjs.com/browser-agent/integrations/redux/)
        6.   [Vue](https://docs.trackjs.com/browser-agent/integrations/vue/)
        7.   [Workers](https://docs.trackjs.com/browser-agent/integrations/workers/)
        8.   [Legacy](https://docs.trackjs.com/browser-agent/integrations/legacy/)

    3.   [Performance](https://docs.trackjs.com/browser-agent/performance/)
    4.   [Tips & Tricks](https://docs.trackjs.com/browser-agent/tips-and-tricks/)
        1.   [Android Platform Info](https://docs.trackjs.com/browser-agent/tips-and-tricks/android-platform-info/)
        2.   [Exclude Analytics](https://docs.trackjs.com/browser-agent/tips-and-tricks/exclude-analytics/)
        3.   [GDPR Consent](https://docs.trackjs.com/browser-agent/tips-and-tricks/gdpr-consent/)
        4.   [Hide Console Messages](https://docs.trackjs.com/browser-agent/tips-and-tricks/hide-console/)
        5.   [Include Network Payloads](https://docs.trackjs.com/browser-agent/tips-and-tricks/include-network-payloads/)
        6.   [Memory Monitoring](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/)
        7.   [Offline Errors](https://docs.trackjs.com/browser-agent/tips-and-tricks/offline/)
        8.   [Page Version](https://docs.trackjs.com/browser-agent/tips-and-tricks/page-version/)
        9.   [Passive Tracking](https://docs.trackjs.com/browser-agent/tips-and-tricks/passive-tracking/)
        10.   [Resource Loading](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-resource-load-error/)
        11.   [Single Error Metadata](https://docs.trackjs.com/browser-agent/tips-and-tricks/single-error-metadata/)
        12.   [State Telemetry](https://docs.trackjs.com/browser-agent/tips-and-tricks/state-telemetry/)
        13.   [Subresource Integrity](https://docs.trackjs.com/browser-agent/tips-and-tricks/subresource-integrity/)

    5.   [Troubleshooting](https://docs.trackjs.com/browser-agent/troubleshooting/)
    6.   [Browser Agent API](https://docs.trackjs.com/browser-agent/sdk-reference/)
        1.   [Agent Methods](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/)
        2.   [Agent Options](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/)

    7.   [Changelog](https://docs.trackjs.com/browser-agent/changelog/)

3.   [Node Agent](https://docs.trackjs.com/node-agent/)
    1.   [Installation](https://docs.trackjs.com/node-agent/installation/)
    2.   [Integrations](https://docs.trackjs.com/node-agent/integrations/)
        1.   [Axios](https://docs.trackjs.com/node-agent/integrations/axios/)
        2.   [Express](https://docs.trackjs.com/node-agent/integrations/express/)
        3.   [NextJS](https://docs.trackjs.com/node-agent/integrations/nextjs/)

    3.   [Node Agent API](https://docs.trackjs.com/node-agent/sdk-reference/)
        1.   [Agent Methods](https://docs.trackjs.com/node-agent/sdk-reference/agent-methods/)
        2.   [Agent Options](https://docs.trackjs.com/node-agent/sdk-reference/agent-options/)

4.   [Data Management](https://docs.trackjs.com/data-management/)
    1.   [Applications](https://docs.trackjs.com/data-management/applications/)
    2.   [Minified Sources](https://docs.trackjs.com/data-management/minified-sources/)
    3.   [Ad Blockers](https://docs.trackjs.com/data-management/ad-blockers/)
    4.   [Error Status](https://docs.trackjs.com/data-management/status/)
    5.   [Ignoring Errors](https://docs.trackjs.com/data-management/ignore/)
    6.   [Grouping Errors](https://docs.trackjs.com/data-management/grouping/)
    7.   [Deleting Errors](https://docs.trackjs.com/data-management/delete/)
    8.   [Sensitive Data](https://docs.trackjs.com/data-management/sensitive/)
    9.   [Retention and Limits](https://docs.trackjs.com/data-management/limits/)
    10.   [Page Views](https://docs.trackjs.com/data-management/pageviews/)

5.   [Notifications](https://docs.trackjs.com/notifications/)
6.   [Users & Accounts](https://docs.trackjs.com/user-accounts/)
    1.   [Single Sign-On](https://docs.trackjs.com/user-accounts/sso/)
    2.   [Permissions](https://docs.trackjs.com/user-accounts/permissions/)
    3.   [Multiple Accounts](https://docs.trackjs.com/user-accounts/multiple/)

7.   [API Reference](https://docs.trackjs.com/data-api/)
    1.   [Capture](https://docs.trackjs.com/data-api/capture/)
    2.   [Usage](https://docs.trackjs.com/data-api/usage/)
    3.   [Usage By Hour](https://docs.trackjs.com/data-api/usage-by-hour/)
    4.   [Errors](https://docs.trackjs.com/data-api/errors/)
    5.   [Errors by Day](https://docs.trackjs.com/data-api/errors-by-day/)
    6.   [Errors by Hour](https://docs.trackjs.com/data-api/errors-by-hour/)
    7.   [Errors by Message](https://docs.trackjs.com/data-api/errors-by-message/)
    8.   [Errors by URL](https://docs.trackjs.com/data-api/errors-by-url/)
    9.   [Page Views by Day](https://docs.trackjs.com/data-api/pageviews-by-day/)
    10.   [Page Views by Hour](https://docs.trackjs.com/data-api/pageviews-by-hour/)

8.   [Support](https://docs.trackjs.com/support/)

[![Image 2: TrackJS](https://docs.trackjs.com/assets/images/logo_charcoal_red.svg)](https://docs.trackjs.com/)

[TrackJS Documentation ---------------------](https://docs.trackjs.com/)

*   [Log in](https://my.trackjs.com/)
*   [Sign up](https://my.trackjs.com/signup)

*   [docs](https://docs.trackjs.com/)»
*   [browser-agent](https://docs.trackjs.com/browser-agent)»
*   [tips-and-tricks](https://docs.trackjs.com/browser-agent/tips-and-tricks)»

Subresource Integrity Checks (SRI)
==================================

[Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity), or SRI, is used to make sure that the script doesn’t change out from under you. It’s an important security check when you depend on third-party vendors for code.

The default URL to the TrackJS agent is a variable version pointing at the _latest_ version of the agent. This allows us to push out bug fixes and improvements without you needing to make code changes. But it does introduce risk that behavior may change without your knowledge, hence why you’re looking at SRI.

[How to get Subresource Integrity with TrackJS](https://docs.trackjs.com/browser-agent/tips-and-tricks/subresource-integrity/#how-to-get-subresource-integrity-with-trackjs "Permalink Here")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [1. Use the TrackJS Module](https://docs.trackjs.com/browser-agent/tips-and-tricks/subresource-integrity/#1-use-the-trackjs-module "Permalink Here")

Rather than using the SRI directives directly, you can accomplish the same goal by [using the TrackJS npm module](https://docs.trackjs.com/browser-agent/installation/#bundling-as-a-module) and bundling the agent into your code. This allows you to control exactly which version is included, probably saves you a network request too!.

### [2. Reference a version-specific agent](https://docs.trackjs.com/browser-agent/tips-and-tricks/subresource-integrity/#2-reference-a-version-specific-agent "Permalink Here")

Rather than pointing at the latest version of the agent, you can reference a specific version from the CDN:

```
https://cdn.trackjs.com/agent/3.10.4/t.js
```

You can find the paths to each version of the agent in our [CHANGELOG](https://docs.trackjs.com/browser-agent/changelog/). If you’d like to further guarantee that the code doesn’t change, you can generate an SRI hash for any of these paths using [this free SRI tool](https://www.srihash.org/);

<script src="https://cdn.trackjs.com/agent/3.10.4/t.js" integrity="sha384-njM4XFxHYqEd5zVpi3Zt1t/TGkshDeMEjIGUJtLQ38d6zwGZpTj9tPXlhspkHNhK" crossorigin="anonymous"></script>![Image 3: Copy](https://docs.trackjs.com/assets/images/copy.svg)Copy

[SRI hash for TrackJS Agent](https://docs.trackjs.com/browser-agent/tips-and-tricks/subresource-integrity/#code-sri-hash-for-trackjs-agent)

Note that SRI requires the CORS headers to be sent, and we’ve seen lots of third-party networks strip out or manipulate CORS headers. We recommend using TrackJS as a module instead.

 Found a mistake? [Let us know!](https://trackjs.com/contact/)

Thanks for the feedback!

Was this page helpful?

Yes No

something really long that isnt likely

1/4

∧∨×

All content appearing on this website is proprietary, copyrighted and owned or licensed by [TrackJS](https://trackjs.com/). Any unauthorized use of trademarks or content from this website is strictly prohibited. All rights reserved.

© 2013-2026 TrackJS LLC
