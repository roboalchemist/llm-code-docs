# Source: https://docs.trackjs.com/data-management/applications/

Title: Applications

URL Source: https://docs.trackjs.com/data-management/applications/

Markdown Content:
**TIP**: Applications are a premium feature and not available on all TrackJS plans. Check the [Pricing plans](https://trackjs.com/pricing) for details.

[Segmenting Data](https://docs.trackjs.com/data-management/applications/#segmenting-data "Permalink Here")
----------------------------------------------------------------------------------------------------------

TrackJS Applications allow you to segment your error data by codebase or environment. Each codebase you want to protect should have it’s own application key, in addition to each deployed environment. This is done by [creating application keys in the TrackJS Dashboard](https://my.trackjs.com/onboarding/applications), and assigning them to the [`application`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#application) install option.

For example, let’s say your main web application is deployed to a “production” environment for real users, and a “test” environment for internal testing. You wouldn’t want noisy test data clouding your reports about production or setting off alerts. You would create 2 applications: `my-app-prod` and `my-app-test`. After creating the application keys, update your agent config with the `application` key:

[Global](https://docs.trackjs.com/data-management/applications/)[Module](https://docs.trackjs.com/data-management/applications/)[Legacy](https://docs.trackjs.com/data-management/applications/)

<script src="https://cdn.trackjs.com/agent/v3/latest/t.js"></script><script> window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", application: "my-app-prod" });</script>

[Installing the agent with Applications](https://docs.trackjs.com/data-management/applications/#code-installing-the-agent-with-applications)

// ES6 Modular JavaScript.// npm install trackjs --saveimport { TrackJS } from "trackjs"; window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", application: "my-app-prod"});

[Installing the agent with Applications](https://docs.trackjs.com/data-management/applications/#code-installing-the-agent-with-applications)

<!-- Legacy agent deprecated 2018-10-31 --><script> window._trackJs = { token: "YOUR_TOKEN", application: "my-app-prod" };</script><script src="https://cdn.trackjs.com/releases/current/tracker.js"></script>

[Installing the agent with Applications](https://docs.trackjs.com/data-management/applications/#code-installing-the-agent-with-applications)

You may also want to protect other codebases with TrackJS, such as another application or your public website. You’ll want to create more applications for each of them to see which are having trouble. You would create additional applications: `public-website-prod` and `public-website-test`.

[Filtering Applications](https://docs.trackjs.com/data-management/applications/#filtering-applications "Permalink Here")
------------------------------------------------------------------------------------------------------------------------

You can filter the Dashboard to show data from **All Applications** or a **Single Application** using the Filtering Toolbar.

Setting this filter updates all screens in the Dashboard.

[Permanence](https://docs.trackjs.com/data-management/applications/#permanence "Permalink Here")
------------------------------------------------------------------------------------------------

Application keys are nothing more than a filtering string. Deleting an application from your Dashboard only removes your ability to filter by that application. If you recreate an application with the same key, all of the errors recorded to the key will be filterable again.
