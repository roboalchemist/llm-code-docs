# Source: https://docs.trackjs.com/data-management/pageviews/

Title: Page Views

URL Source: https://docs.trackjs.com/data-management/pageviews/

Markdown Content:
You may have noticed that we [price](https://trackjs.com/pricing) our subscriptions based on the number of page views monitored. We occasionally get questions about this metric or why we track it.

[When is a Page View Counted?](https://docs.trackjs.com/data-management/pageviews/#when-is-a-page-view-counted "Permalink Here")
--------------------------------------------------------------------------------------------------------------------------------

Whenever our JavaScript agent is initialized in the browser, it (asynchronously) sends an image request to our usage monitoring servers. This is a lightweight request which tells us which customer and application initialized the script. We consider this a single page view.

[Why Count Page Views At All?](https://docs.trackjs.com/data-management/pageviews/#why-count-page-views-at-all "Permalink Here")
--------------------------------------------------------------------------------------------------------------------------------

In the TrackJS reporting dashboard, the top graph is your errors over time, juxtaposed against your page view count over time. We believe that showing errors per page view is a good way to get a handle on your site’s script quality. If you have a large increase in JavaScript errors, but no corresponding increase in page views, it’s likely something is wrong! When you can see the two data streams together in one place, it’s much easier to determine if there are new issues, or whether you’re just seeing more traffic.

[Why Price Based on Page Views?](https://docs.trackjs.com/data-management/pageviews/#why-price-based-on-page-views "Permalink Here")
------------------------------------------------------------------------------------------------------------------------------------

Many services price their subscriptions based on the number of errors you send. If you don’t have many errors, the price looks cheap. But what happens if you have a bad release, causing thousands or millions of unexpected errors? You’ll either be paying huge surprise bills, or your data will get cut off and you’ll lose access at the most critical time. We don’t think either of those are good options!

We believe [metered pricing by number of errors is anti-developer](https://trackjs.com/blog/metered-logging-is-anti-developer/), so we chose a different metric. We found that page views are often reasonably consistent month over month, and we want to be sure we have enough infrastructure to handle your worst releases (and help you fix them)!

[Going Over Your Page View Limits](https://docs.trackjs.com/data-management/pageviews/#going-over-your-page-view-limits "Permalink Here")
-----------------------------------------------------------------------------------------------------------------------------------------

If you go over your page view limits once or twice, it’s no problem. If you go over month over month by a significant amount, you will get an email from us asking you to curtail usage, or upgrade to the next tier. We’re nice folks, and either option is fine. We will not cut off your data ingestion for overages.

[How Come Google Analytics Has A Different Page View Count Than TrackJS?](https://docs.trackjs.com/data-management/pageviews/#how-come-google-analytics-has-a-different-page-view-count-than-trackjs "Permalink Here")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We count a page view only when our script is initialized. In a single page application (SPA) it’s likely our script will initialize only once, but the user will visit many pages. Google Analytics (or other tools) are often configured to count each pushState change as a page view. We don’t do this because our main goal with page views is to provide a traffic-normalized way (errors per page view) to analyze your site’s script quality, not be the user activity analytics source of truth.
