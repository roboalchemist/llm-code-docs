# Source: https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/

Title: Increase user engagement

URL Source: https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/

Markdown Content:
Increase user engagement | New Relic Documentation
===============

Opens in a new window Opens an external website Opens an external website in a new window

We use cookies and other tracking technologies - provided by other companies with whom we share your data - to make our website work, improve your experience, and support our marketing efforts, as explained in our [](https://newrelic.com/termsandconditions/privacy)[Privacy Notice](https://newrelic.com/termsandconditions/privacy). By using our website, you agree to our [](https://newrelic.com/termsandconditions/website-terms)[Website Terms of Use](https://newrelic.com/termsandconditions/website-terms). [Privacy Notice](https://newrelic.com/termsandconditions/privacy)

[](https://newrelic.com/)

[Docs](https://docs.newrelic.com/)[Community](https://support.newrelic.com/)[Learn](https://learn.newrelic.com/)

*   [Docs](https://docs.newrelic.com/)
*   [Community](https://support.newrelic.com/)
*   [Learn](https://learn.newrelic.com/)

*   / 
*   [English](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/)[Español](https://docs.newrelic.com/es/docs/website-performance-monitoring/increase-user-engagement/)[Français](https://docs.newrelic.com/fr/docs/website-performance-monitoring/increase-user-engagement/)[日本語](https://docs.newrelic.com/jp/docs/website-performance-monitoring/increase-user-engagement/)[한국어](https://docs.newrelic.com/kr/docs/website-performance-monitoring/increase-user-engagement/)[Português](https://docs.newrelic.com/pt/docs/website-performance-monitoring/increase-user-engagement/)   
*   [Log in](https://one.newrelic.com/)[Start now](https://newrelic.com/signup)

[](https://docs.newrelic.com/)

[](https://docs.newrelic.com/)

START HERE

[Get started with New Relic](https://docs.newrelic.com/docs/new-relic-solutions/get-started/intro-new-relic/)

Tutorials and walkthroughs

Guides and best practices

MONITOR YOUR DATA

New Relic Control

AI monitoring

Application performance monitoring

Browser monitoring

eBPF observability

Infrastructure monitoring

Kubernetes monitoring

Log management

Mobile monitoring

Model performance monitoring

Queues and Streams

Network monitoring

OpenTelemetry

SAP Solutions

Serverless monitoring

Streaming Video & Ads

Synthetic monitoring

Website performance monitoring

[Increase user engagement](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/)

DATA INSIGHTS

New Relic AI

Alerts

Change tracking

Charts, dashboards, and querying

Cloud Cost Intelligence

CodeStream

Distributed tracing

Errors inbox

New Relic Lens

NRQL

Service Architecture Intelligence

Service level management

Workflow Automation

SECURITY

Interactive application security testing (IAST)

Security RX (Remediation Explorer)

PRODUCT UPDATES

Release notes

What's new?

[End-of-life announcements](https://docs.newrelic.com/eol/)

ADMIN AND DATA

Account & user management

Data and APIs

[Data dictionary](https://docs.newrelic.com/attribute-dictionary/)

Security and privacy

Licenses

Increase user engagement
========================

Maintaining a website combines the efforts of multiple teams. When outages happen, developer and engineering teams can resolve issues directly, but a digital marketer may not have the same access to site administration. As a digital marketer, your team's success is just as dependent on site performance, but you might not have the tools to identify or address any issue yourselves.

Our website performance monitoring (WPM) tool gives insight into your site's availability and performance. With out-of-the-box alerts and routine checks from our monitors, you'll never be uncertain about how your site performs.

[![Image 3: Docs site](https://docs.newrelic.com/images/tutorial_screenshot-crop2_full-wpm.webp)](https://docs.newrelic.com/images/tutorial_screenshot-crop2_full-wpm.webp)

Once data has been collected, you'll be able to view different charts that track user details about your page's assets. Taken together, they can help you understand how your users experience your site.

Objectives [](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#objectives)
-----------------------------------------------------------------------------------------------------------------

This doc helps you set up our codeless website monitoring tool, then walks you through understanding your data. In this tutorial, you will:

*   Set up monitoring without an installation
*   Learn about your collected data

Set up website performance monitoring [](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#setup)
---------------------------------------------------------------------------------------------------------------------------------------

1

### Get data without an installation[](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#get-data-without-an-installation)

Website performance monitoring requires no installation or setup. It currently only supports desktop browsers. To access your data, go to **[one.newrelic.com > Website performance monitoring](https://one.newrelic.com/website-grader)**.

2

### Choose your URL[](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#choose-your-url)

Once you've chosen pages to monitor, New Relic deploys a set of monitors from different servers around the globe that checks your page for website availability, broken links, performance, and SSL certificate expiration. To get started, we recommend choosing your homepage.

New Relic will take a few minutes to deploy the monitors, then you'll start receiving data about your website. Keep in mind that your monitors only check the performance of pages you've manually added.

3

### Add Google PageSpeed API key[](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#add-google-pagespeed-api-key)

We draw core web vitals from Google's API so that scores in New Relic match what you have in Google. To continue capturing these scores after initial setup, you'll need to create a [Google PageSpeed API key](https://developers.google.com/speed/docs/insights/v5/get-started).

[![Image 4: Capture your core web vitals after inputting your Google PageSpeed API key](https://docs.newrelic.com/images/tutorial_screenshot-full_pageSpeed-wpm.gif)](https://docs.newrelic.com/images/tutorial_screenshot-full_pageSpeed-wpm.gif)

Put your data in context[](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#put-your-data-in-context)
--------------------------------------------------------------------------------------------------------------------------------------------

Once your monitors report data to New Relic, you'll see metrics that can help you improve user experience and SEO ranking. Below are examples of the kind of data you'll see on your summary page.

##### Check page availability[](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#ping)

[![Image 5: View page availability](https://docs.newrelic.com/images/tutorial_screenshot-crop_ping-wpm.webp)](https://docs.newrelic.com/images/tutorial_screenshot-crop_ping-wpm.webp)
The first section shows you ping data. This kind of data is an availability check, confirming basic site functionalities:

*   **Site availability**. This reports whether your page has loaded at all. If it hasn't, there might be an issue with your servers or domain.

*   **Page load time**. This collects the median speed for how long it takes your page to load all of its assets. This data gets further broken down by content type and size.

*   **SSL Validity**. This tells you whether your SSL certificate is valid, expiring, or expired. It'll include the date you need to renew your SSL certificate as well.

*   **Broken links**. After testing all the links on your page, it'll report back which links are broken.

Our monitors capture site behavior via monitors that interact with your site. This lets you see updated data on a day-to-day basis so you never have to guess when assets or pages fail to load.

##### Track user experience[](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#track-user-experience)

[![Image 6: View your data about how user's experience your site](https://docs.newrelic.com/images/tutorial_screenshot-crop_cwv-wpm.webp)](https://docs.newrelic.com/images/tutorial_screenshot-crop_cwv-wpm.webp)
Google PageSpeed reports your core web vitals alongside other metrics collected by New Relic. This data gives you insight into how users experience your site.

*   **First contentful paint**. This captures the time it takes for the first asset to load on a page. In the above screenshot, it took the site 3.22s for something to load on the page.

*   **Largest contentful paint**. Unlike first contentful paint, this captures the time taken for the largest content on the page to fully load. For example, if information about an important campaign appears in a page's largest asset, then this number tells us how long a user waits before seeing it. In the above screenshot, it took 2.79s.

*   **Interaction to next paint**. When a user interacts with an element on your site, it takes time to process the user's interaction This number captures that time as a delay between the request (user interaction) and response (how the page changes based on the user request).

*   **Cumulative layout shift**. This measures visual stability of different assets on your site. For example, after a user goes to your site's main page, images may shift while loading. This movement is unanticipated.

[![Image 7: Adjust timeslice data](https://docs.newrelic.com/images/tutorial_screenshot-crop_cwv-time-wpm.gif)](https://docs.newrelic.com/images/tutorial_screenshot-crop_cwv-time-wpm.gif)
We collect data over time so you can get a richer picture of your site's performance. You can zoom in and out of windows of time and see how your data changes around a particular incident, like in the gif above. When you're finished, click the time stamp button at the top to adjust back to your preferred time period.

##### Compare content size, load times, and sources[](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#content)

[![Image 8: Analyze content size](https://docs.newrelic.com/images/tutorial_screenshot-crop_content-wpm.webp)](https://docs.newrelic.com/images/tutorial_screenshot-crop_content-wpm.webp)
Your webpage is made up of different types of content, like HTML, images, JavaScript, and videos. Our content charts show you how different content types perform relative to one another. For example:

*   **Content size** shows you the size in kilobytes of each type. Referring to the above chart, you can see that your JavaScript content type is proportionally smaller than your images on a given page. If your site's performance is down, you can request that your dev team optimizes your site on the code-level.

*   **Content sources** breaks down where your content is hosted by size. For example, in the above chart, the bulk of your content is sourced from New Relic, represented by the yellow. If your content is optimized but still broken on your page, then changing where you're sourcing your content could resolve that error.

*   **Content load time** shows how long it takes a given content type to load relative to the entire page's load time.

*   **Network** breaks down how content is delivered to the page and how much time it takes to deliver that content.

If your page is loading slowly, then you can use the **Content** section to diagnose potential sources of the problem. For example, comparing **Content size** to **Content load time** can give insight into whether CSS is taking up too many resources and loading last, which would cause a delay in largest contentful paint. If content size is optimal but page load is still slow, perhaps it's a network or source issue.

##### Fix broken links[](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#geo)

[![Image 9: Docs site](https://docs.newrelic.com/images/tutorial_screenshot-crop_broken-links-wpm.webp)](https://docs.newrelic.com/images/tutorial_screenshot-crop_broken-links-wpm.webp)
If user engagement is down but your site is available and content is optimized, then something else might be at play. A possible journey to troubleshoot might look like:

1.   Go to **[one.newrelic.com > Website performance monitoring](https://one.newrelic.com/website-grader)**.

2.   Check the availability of your page. It reads as available.

3.   Your core web vitals are reporting as **Good** across the board.

4.   You notice timeslice data shows a steep drop-off in traffic the day before, around the time your team made updates to your landing page.

5.   You notice a broken link has been reported. It's a link inside a banner that's used across your site.

At this point, you can coordinate with the relevant teams to fix the broken link and deploy an update for the rest of the site.

What's next? [](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#next)
-------------------------------------------------------------------------------------------------------------

Website performance monitoring is designed to simplify getting detailed insight about your site. We recommend you start with these next steps:

*   Add more pages to WPM. We recommend adding pages critical to your customer funnel such as thank you pages, product pages, or login pages.
*   [Create a codeless step monitor](https://one.newrelic.com/synthetics/monitor-create) that mimics a user journey through your site, such as adding an item, logging in, or filling out a form. If you're uncertain, check out our tutorial on [how to create a step monitor](https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/getting-started/get-started-synthetic-monitoring/#step).
*   If you want to learn more about how New Relic can improve your website, we have a tutorial about [improving your website's performance](https://docs.newrelic.com/docs/journey-performance/improve-website-performance/). While written for developer audiences, it breaks down potential sources for poor performance and how to improve them.

#### On this page

*   [Objectives](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#objectives)
*   [Set up website performance monitoring](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#setup)
*   [Put your data in context](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#put-your-data-in-context)
*   [What's next?](https://docs.newrelic.com/docs/website-performance-monitoring/increase-user-engagement/#next)

Was this doc helpful?

😁

Yes

🙁

No

[Edit this doc](https://github.com/newrelic/docs-website/blob/develop/src/content/docs/website-performance-monitoring/increase-user-engagement.mdx)

Copyright © 2026 New Relic Inc.

[Careers](https://newrelic.com/about/careers)[Terms of Service](https://newrelic.com/termsandconditions/terms)[DMCA Policy](https://newrelic.com/termsandconditions/dmca)[Patent Notice](https://newrelic.com/termsandconditions/patent-notice)[Privacy Notice](https://newrelic.com/termsandconditions/services-notices)Your Privacy Choices[Cookie Policy](https://newrelic.com/termsandconditions/cookie-policy)[UK Slavery Act](https://newrelic.com/termsandconditions/uk-slavery-act)

This site is protected by reCAPTCHA and the Google[Privacy Policy](https://policies.google.com/privacy) and[Terms of Service](https://policies.google.com/terms) apply.
