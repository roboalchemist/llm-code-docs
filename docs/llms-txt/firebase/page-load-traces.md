# Source: https://firebase.google.com/docs/perf-mon/page-load-traces.md.txt

<br />

| TheFirebaseJavaScriptSDK forPerformance Monitoringis a**beta** release.  
| This product might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

Performance Monitoringuses*traces*to collect data about monitored processes in your app. A trace is a report that contains data captured between two points in time in your app.

For web apps,Performance Monitoring*automatically* collects a trace for each page of your app called a***page load trace***. Each page load trace collects the following default metrics:

- [largest contentful paint](https://firebase.google.com/docs/perf-mon/page-load-traces#largest-contentful-paint)- A metric that measures the time between when the user navigates to a page and when the*largest*visual change happens

- [interaction to next paint](https://firebase.google.com/docs/perf-mon/page-load-traces#next-paint-interaction)- A metric that measures the longest time between when the user interacts with the page to when the next paint occurs

- [cumulative layout shift](https://firebase.google.com/docs/perf-mon/page-load-traces#cumulative-layout-shift)- A metric that measures and scores unexpected layout shifts in a page

- [first paint](https://firebase.google.com/docs/perf-mon/page-load-traces#first-paint)--- A metric that measures the time between when the user navigates to a page and when*any*visual change happens

- [first contentful paint](https://firebase.google.com/docs/perf-mon/page-load-traces#first-contentful-paint)--- A metric that measures the time between when a user navigates to a page and when meaningful content displays, like an image or text

- [domInteractive](https://firebase.google.com/docs/perf-mon/page-load-traces#domInteractive)--- A metric that measures the time between when the user navigates to a page and when the page is considered interactive for the user

- [domContentLoadedEventEnd](https://firebase.google.com/docs/perf-mon/page-load-traces#domContentLoaded)--- A metric that measures the time between when the user navigates to a page and when the initial HTML document is completely loaded and parsed

- [loadEventEnd](https://firebase.google.com/docs/perf-mon/page-load-traces#loadEventEnd)--- A metric that measures the time between when the user navigates to the page and when the current document's*load event*completes

- [first input delay](https://firebase.google.com/docs/perf-mon/page-load-traces#input-delay)--- A metric that measures the time between when the user interacts with a page and when the browser is able to respond to that input

You can view data from these traces in the*Page load* subtab of the traces table, which is at the bottom of the*Performance* dashboard (learn more about[using the console](https://firebase.google.com/docs/perf-mon/page-load-traces#monitor-in-console)later on this page).
| These out-of-the-box traces get you started with monitoring your app, but to learn about the performance of specific tasks or flows in your app, try out[instrumenting your own custom traces of code](https://firebase.google.com/docs/perf-mon/custom-code-traces)in your app.

## Definition of a page load trace

This trace measures several metrics about how the pages in your app load, specifically how long it takes to reach common loading points, like an a responsive app.

Page load traces help you track your app's[core web vitals](https://web.dev/vitals/#core-web-vitals), like first contentful paint.

## Metrics collected for page load traces

These traces are out-of-the-box traces, so you cannot add additional custom metrics or custom attributes to them.

### Largest contentful paint

This metric measures the time between when the user navigates to a page and when the*largest*image, text, or video content displays.

This metric is useful to understand how quickly the main content of the web page becomes visible to the user.

- Starts when the user navigates to a page.

- Stops when the*largest* visual change happens, including images, text, or video elements. Refer to the[core web vitals](https://web.dev/articles/lcp#what-elements-are-considered)for more details.

The "*Largest contentful paint element*" is a custom attribute that identifies the element corresponding to the largest contentful paint. This is captured in addition to the largest contentful paint timing.

### Interaction to next paint

| **Note:** Interaction to next paint is not captured if the user does not interact with the page.

This metric measures the time between when a user interacts with a page to when the next paint occurs.

This metric is useful since it measures how responsive a page is to user input.

- Starts when the user interacts with the page (mouse click, tapping on a device, or keyboard input).

- Stops when next paint occurs. Refer to the[core web vitals](https://web.dev/articles/inp#what-is-inp)for more details.

The "*Longest interaction to next paint*" is a custom attribute that identifies the element that was interacted with by the user when the interaction to next paint event occurred. This is captured in addition to the interaction to next paint timing.

### Cumulative layout shift

This metric measures the largest burst of layout shifts scores for every unexpected layout shift that occurs within the entire lifecycle of the page.

This metric is useful since unexpected layout shifts can disrupt the user experience. The metric reports a score based on the[Layout Instability API](https://github.com/WICG/layout-instability). Refer to the[core web vitals](https://web.dev/articles/cls#layout-shifts-in-detail)for more details on how the score is calculated.

The "*Largest layout shift target*" is a custom attribute that identifies the element that shifted when the largest contentful shift occurred. This is captured in addition to the cumulative layout shift score.

### First paint

This metric measures the time between when the user navigates to a page and when*any*visual change happens.

This metric is useful since the first paint signals to your users that the page is*starting*to load.

- Starts when the user navigates to a page.

- Stops when*any*visual change happens, including a background color change or a header loading.

### First contentful paint

This metric measures the time between when a user navigates to a page and when meaningful content displays, like an image or text.

This metric is useful for insights into how soon your users see any of your app's actual content rather than just a new background color or header.

- Starts when the user navigates to a page.

- Stops immediately after the browser renders the first content from the DOM, including any text, image (including background images), non-white canvas, or SVG.

### domInteractive

This metric measures the time between when the user navigates to a page and when the page is considered interactive for the user.

This metric is useful for insights into how soon your users can actually interact with elements in your app, like buttons and hyperlinks, rather than just seeing them on the screen. Note that this doesn't mean that the browser will respond to the interaction (for this metric, refer to[*first input delay*trace](https://firebase.google.com/docs/perf-mon/page-load-traces#input-delay)).

- Starts when the user navigates to a page.

- Stops immediately before the user agent sets the current HTML document's readiness to "interactive".

### domContentLoadedEventEnd

This metric measures the time between when the user navigates to a page and when the initial HTML document is completely loaded and parsed.

- Starts when the user navigates to a page.

- Stops immediately after the initial HTML document is completely loaded and parsed (`DOMContentLoaded`), but this does not mean that stylesheets, images, and subframes are finished loading.

### loadEventEnd

This metric measures the time between when the user navigates to the page and when the current document's*load event*completes.

This metric is useful for insights into how long it takes to load all your content, including stylesheets and images.

- Starts when the user navigates to a page.

- Stops immediately after the current HTML document's load event completes.

### First input delay

This metric measures the time between when the user interacts with a page and when the browser is able to respond to that input.

This metric is useful since the browser responding to a user interaction gives your users their first impressions about the responsiveness of your app.

- Starts when the user*first*interacts with an element on the page, like clicking a button or hyperlink.

- Stops immediately after the browser is able to respond to the input, meaning that the browser isn't busy loading or parsing your content.

Note that to measure the first input delay metric, you need to add the polyfill library for this metric. For installation instructions, refer to the library's[documentation](https://github.com/GoogleChromeLabs/first-input-delay).
| **Note:** Performance Monitoringonly records the first input delay metric when a user clicks on the web page within the first 5 seconds after page load.

## Track, view, and filter performance data

To view real-time performance data, make sure that your app uses a Performance Monitoring SDK version that's compatible with real-time data processing.[Learn more about real-time performance data](https://firebase.google.com/docs/perf-mon/troubleshooting#faq-real-time-data).

### Track key metrics in your dashboard

To learn how your key metrics are trending, add them to your metrics board at the top of the*Performance*dashboard. You can quickly identify regressions by seeing week-over-week changes or verify that recent changes in your code are improving performance.
![an image of the metrics board in the <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-metrics-board.png)Firebase Performance Monitoringdashboard" /\>

To add a metric to your metrics board, follow these steps:

1. Go to the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)in theFirebaseconsole.
2. Click an empty metric card, then select an existing metric to add to your board.
3. Clickmore_verton a populated metric card for more options, for example to replace or remove a metric.

<br />

The metrics board shows collected metric data over time, both in graphical form and as a numerical percentage change.

Learn more about[using the dashboard](https://firebase.google.com/docs/perf-mon/console).

### View traces and their data

To view your traces, go to the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)in theFirebaseconsole, scroll down to the traces table, then click the appropriate subtab. The table displays some top metrics for each trace, and you can even sort the list by the percentage change for a specific metric.

Performance Monitoringprovides a troubleshooting page in theFirebaseconsole that highlights metric changes, making it easy to quickly address and minimize the impact of performance issues on your apps and users. You can use the troubleshooting page when you learn about potential performance issues, for example, in the following scenarios:

- You select relevant metrics on the dashboard and you notice a big delta.
- In the traces table you sort to display the largest deltas at the top, and you see a significant percentage change.
- You receive an email alert notifying you of a performance issue.

You can access the troubleshooting page in the following ways:

- On the metric dashboard, click the**View metric details**button.
- On any metric card, select**more_vert=\> View details**. The troubleshooting page displays information about the metric you selected.
- In the traces table, click a trace name or any metric value in the row associated with that trace.
- In an email alert, click**Investigate now**.

When you click a trace name in the traces table, you can then drill down into metrics of interest. Click the**Filteradd**button to filter the data by attribute, for example:
![an image of <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-filter-by-attribute_web_1.png)Firebase Performance Monitoringdata being filtered by attribute" /\>

- Filter by*Page URL*to view data for a specific page of your site
- Filter by*Effective connection type*to learn how a 3g connection impacts your app
- Filter by*Country*to make sure your database location isn't affecting a specific region

Learn more about[viewing data for your traces](https://firebase.google.com/docs/perf-mon/console?platform=web#view-traces-and-data).

## Next Steps

- Learn more about[using attributes](https://firebase.google.com/docs/perf-mon/attributes)to examine performance data.

- Learn more about how to[track performance issues](https://firebase.google.com/docs/perf-mon/issue-management)in theFirebaseconsole.

- [Set up alerts](https://firebase.google.com/docs/perf-mon/alerts)for page loads that are degrading the performance of your app. For example, you can configure an email alert for your team if the*first input delay*for a specific page exceeds a threshold that you set.