# Source: https://firebase.google.com/docs/app-hosting/monitor-routes.md.txt

<br />

Route-based Monitoring lets you aggregate your backend's logs from Cloud Logging and organize them to show you different metrics for different routes in your web app.

## Use cases for route-based monitoring

Route-based metrics provide insights into the performance and behavior of your web app routes. By monitoring and analyzing these metrics, you can optimize routes, troubleshoot issues, and enhance your app's user experience.

Benefits

- **Performance Troubleshooting:**Identify specific routes experiencing high latency (p75) or error rates, enabling targeted optimization efforts.
- **Traffic Analysis:**Understand the volume of requests for different routes, helping to prioritize resources and identify popular features.
- **Error Tracking:**Monitor 4xx and 5xx errors on individual routes, allowing for rapid detection and resolution of issues affecting specific parts of the application.

Use Cases

- **API Performance Optimization:**API providers can use route-based metrics to identify slow or error-prone endpoints and optimize their performance. This leads to faster response times, improved reliability, and a better developer experience.
- **Web App Performance Monitoring:**By monitoring route-based metrics, developers can pinpoint performance bottlenecks and optimize specific pages or features. This results in a faster and smoother user experience.
- **Ecommerce Conversion Optimization:**Ecommerce businesses can use route-based metrics to track the performance of different product pages and checkout flows. This data can be used to optimize the user experience and increase conversion rates.

## Enable route-based monitoring

To opt in and enable route-based monitoring:

1. Select your backend in the[App Hostingpage](https://console.firebase.google.com/project/_/apphosting)of the Firebase console.
2. In**Routes** , select**Register routes**to enable route-based monitoring.

Once you have opted in, you can add routes in your app that you are interested in monitoring. Make sure you are aware of the potential[cost impact](https://firebase.google.com/docs/app-hosting/monitor-routes#pricing)of using this feature.

## Register routes

For each network request sent from your app,App Hostingmaps the request to the most specific route pattern that matches the request's URL. The pattern matching only affects future requests; matches and data from previous requests won't be affected by a new custom URL pattern input.

Input routes as custom URL patterns. Start with a hostname, followed by path segments. The hostname must include a valid domain, and can optionally include the subdomain. Use the following path segment syntax to create a pattern that can match URLs.

- plain text --- matches an exact path
- \* --- matches the first subdomain segment, or any string in a single path segment
- \*\* --- matches an arbitrary path suffix

The following table describes some potential custom URL pattern matching.

|         **To match...**         | **Create a custom URL pattern like...** |                           **Example matches to this URL pattern**                           |
|---------------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------|
| An exact URL                    | `/foo/baz`                              | `example.com/foo/baz`                                                                       |
| Any single path segment (`*`)   | `/*/baz`                                | `example.com/foo/baz` `example.com/bar/baz`                                                 |
| Any single path segment (`*`)   | `/*/*/baz`                              | `example.com/foo/bar/baz` `example.com/bah/qux/baz`                                         |
| Any single path segment (`*`)   | `/foo/*`                                | `example.com/foo/baz` `example.com/foo/bar` Note:This pattern won't match`example.com/foo`. |
| An arbitrary path suffix (`**`) | `/foo/**`                               | `example.com/foo` `example.com/foo/baz` `example.com/foo/baz/more/segments`                 |
| An arbitrary path suffix (`**`) |

Note this edge behavior of route-based monitoring:

- For custom URL patterns, Firebase**does not** support syntax such as`*.[file extension]`, such as`*.png`or`*.css`.
- The domain for a URL pattern**can** also contain \* as its first segment:`*.example.com/*/fruits/**`.
- Requests are counted for all URL pattern matches.`example.com/foo/baz`will count for both`example.com/*`and`example.com/foo/*`

You can register up to 20 routes to monitor.

## Monitor metrics

The following metrics are available for each registered route:

- Number of requests
- Errors (5xx \& 4xx)
- p95 latency
- [CDN cache](https://firebase.google.com/docs/app-hosting/optimize-cache)hit rate

All metrics are displayed for the time period selected at the top of the overview tab.

### Pricing

The[log-based metrics](https://cloud.google.com/stackdriver/pricing#log-based-metrics)feature of[Cloud Logging](https://cloud.google.com/logging)is required for route-based monitoring metrics. Most projects won't see an increase in cost, but it's important to note that opting into our route based monitoring may result in increasedCloud Loggingusage.

For more information onCloud Loggingpricing and to estimate your costs, see[Cloud Loggingpricing](https://cloud.google.com/logging).