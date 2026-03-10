# Source: https://firebase.google.com/docs/hosting/web-request-logs-and-metrics.md.txt

You can link your Firebase project to Cloud Logging to view, search, and
filter your web request logs for each of your Hosting sites. These logs are
from the CDN that's automatically provided by Firebase, so every request to your
site and the associated request data are logged.

Here are some things you do with Cloud Logging logs. Visit each section of
this page to learn details.

- [**Better understand your site**](https://firebase.google.com/docs/hosting/web-request-logs-and-metrics#better-understand-your-site) --- Learn from
  where and when you have visits to your site, your site's response statuses,
  the latency of end user requests, and more.

- [**Filter your logs with queries**](https://firebase.google.com/docs/hosting/web-request-logs-and-metrics#filter-logs-with-queries) --- Leverage
  automatically collected data to filter and plot data associated with each
  request or your site.

- [**Use log-based metrics**](https://firebase.google.com/docs/hosting/web-request-logs-and-metrics#use-log-based-metrics) --- Create Cloud
  Monitoring charts and alerting policies from predefined system metrics or
  user-defined metrics.

- [**Export logs to other Google Cloud tools**](https://firebase.google.com/docs/hosting/web-request-logs-and-metrics#export-to-other-cloud-tools) ---
  Use logs data in other tools
  (like BigQuery and Looker Studio) for more powerful
  analysis and correlation.

If you have multiple Hosting sites in your project, you can select which of
your Hosting sites will export logs. You can then filter and view your logs
data by Hosting site and even by domain. By selecting specific Hosting
sites to export logs, you can also control the amount of data processed for your
project.

<br />

Learn about Cloud Logging quotas and pricing

<br />

Cloud Logging offers a no-cost level of usage per month (per project).
The usage can be from any Google or Firebase product using Cloud Logging. You
can upgrade your project to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) to unlock additional
paid usage and features. Learn more about
[pricing for Cloud Logging](https://cloud.google.com/stackdriver/pricing).

You can monitor and manage Cloud Logging and billing:

- Estimate your Cloud Logging bills using the
  [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).

- Throttle logs by creating
  [exclusion filters for log sinks](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).

- Set up
  [alerts](https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor#monitor)
  to help control costs.

Logs are automatically deleted after 30 days, with the option to set
[custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention).

Note that the log entry for a particular request or event may be delayed or, in
rare cases, dropped. While logs can be used to understand requests or events,
they may not reflect the true usage that appears in your project usage and
billing.

<br />

<br />

## Link to Cloud Logging and monitor your data usage

### Link to Cloud Logging and export web request logs

1. Click **Link** in the
   [**Cloud Logging** integration card](https://console.firebase.google.com/project/_/settings/integrations/cloudlogging)
   in the Firebase console.

   To link or unlink Cloud Logging, you need the permissions bundled into
   any of the following roles:
   [project Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic) or
   [Firebase Develop Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-category#develop_roles).
2. Follow the on-screen instructions to select which of your Hosting sites
   should export logs to Cloud Logging.

   If you already have one or more active Hosting sites, the linking
   workflow displays an estimated data usage level for logs from each of your
   Hosting sites. This value is estimated from the past 30 days.

After linking to Cloud Logging, logs for any *new* requests to your
Hosting sites will usually show up within 30 minutes of the request being
made.

You can also
[unlink Firebase Hosting](https://firebase.google.com/docs/projects/cloud-logging-export#unlink)
from Cloud Logging, which stops exports of web request logs to
Cloud Logging.

### Monitor your data usage for logs

After linking to Cloud Logging, you can view the data usage level for logs
from your Hosting sites:

- In the
  [*Cloud Logging* integration card](https://console.firebase.google.com/project/_/settings/integrations/cloudlogging)
  in the Firebase console

- In the
  [Logs Viewer interface](https://cloud.google.com/logging/docs/view/logs-viewer-interface#getting_started)
  in the Google Cloud console (the `log_bytes` metric)

<br />

Learn about Cloud Logging quotas and pricing

<br />

Cloud Logging offers a no-cost level of usage per month (per project).
The usage can be from any Google or Firebase product using Cloud Logging. You
can upgrade your project to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) to unlock additional
paid usage and features. Learn more about
[pricing for Cloud Logging](https://cloud.google.com/stackdriver/pricing).

You can monitor and manage Cloud Logging and billing:

- Estimate your Cloud Logging bills using the
  [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).

- Throttle logs by creating
  [exclusion filters for log sinks](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).

- Set up
  [alerts](https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor#monitor)
  to help control costs.

Logs are automatically deleted after 30 days, with the option to set
[custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention).

Note that the log entry for a particular request or event may be delayed or, in
rare cases, dropped. While logs can be used to understand requests or events,
they may not reflect the true usage that appears in your project usage and
billing.

<br />

<br />

## Better understand your site

The
[Logs Viewer interface](https://cloud.google.com/logging/docs/view/logs-viewer-interface#getting_started)
in the Google Cloud console offers tools to view your specific logs and data
using queries and built-in filters and data panels. Learn more about filtering
your logs with queries in the next section below.

- ***Where is your site's traffic coming from at a granular level?***   

  You can view information about each request, including source IP, referer,
  city, and status.

- ***When are users visiting your site?***   

  You can use the
  [Histogram panel](https://cloud.google.com/logging/docs/view/logs-viewer-interface#histogram_panel)
  to see the distribution by specific time ranges. This can give you insight
  into the normal peaks and dips of your app's usage, as well as reveal any
  unexpected spikes in traffic.

- ***What's the status distribution for end-user requests?***   

  You can view the status for each request and even diagnose requests that
  receive errors. You can filter your logs by `Critical`, `Error` or `Warning`.

- ***How long does your site take to respond to a request?***   

  You can view your site's latency for each request using the `latency`
  value captured in each log.

- ***Is your site taking advantage of content caching?***   

  Each log contains a `cacheHit` field to tell you if your site's resource was
  served quickly from Hosting's CDN cache, or if it had to make the full
  trip to the Hosting backend. This can help you improve your website's
  performance by making the most of Firebase's global CDN. For example, you
  can use the data to fine-tune the caching habits of your
  [static assets](https://firebase.google.com/docs/hosting/full-config#headers) and
  [dynamic content](https://firebase.google.com/docs/hosting/manage-cache).

- ***What is the distribution of traffic to your various domains?***   

  If you have multiple domains or Hosting sites, you can filter your logs
  by domain or by site. This allows you to see how your traffic is
  distributed. When you filter by domain, you can track which domain is
  visited most frequently.

## Filter your logs with queries

To learn about how to filter your logs with queries, visit
[Sample queries using Logs Viewer](https://cloud.google.com/logging/docs/view/query-library-preview)
and
[Building log queries](https://cloud.google.com/logging/docs/view/building-queries).
The table below describes the fields available for those queries.

For Hosting, here are some initial filters for a query:

- **Resource** (`resource.type`) --- `firebase_domain` (Firebase Hosting Site Domain)
- **Log name** (`logName`) --- `webrequests` (Firebase Hosting)

Each log entry has a predefined structure and queryable fields (see
[LogEntry](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)).
For Hosting, some fields are standard to an HTTP request, but there are
other field values which come from the processing that Hosting runs on each
request.

| **Field** | **Description** |
|---|---|
| Firebase Hosting stores the following fields in the [`httpRequest`](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#httprequest) object of the log entry. These fields are defined in the HTTP specification. ||
| `cacheHit` | Whether or not the Hosting CDN had the resource of the response in cache |
| `latency` | The request duration, in seconds with `s` postfix (for example, `1.256s`) |
| `protocol` | The protocol used for the request (for example, `HTTP/1.1`, `HTTP/2`, `websocket`) |
| `referer` | The address of the previous web page from which a link to the currently requested page was followed (if present) |
| `remoteIp` | The originating client IP for the request |
| `requestMethod` | The request method (`GET`, `POST`, `PUT`, etc.) |
| `requestSize` | The size of the request in bytes |
| `requestUrl` | The full URL of the request (for example, `https://foo.web.app/bar` or `https://custom.domain.com?query=param`) |
| `responseSize` | The HTTP response size in bytes |
| `serverIp` | *not populated* |
| `status` | The HTTP response status (for example, `200` or `404`) |
| `userAgent` | The user-Agent header of the request |
| Firebase Hosting stores additional fields in the [`jsonPayload`](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.json_payload) object of the log entry. ||
| `acceptEncoding` | *(from the HTTP request)* Which content encoding, usually a compression algorithm, the client supports (for example, `gzip` or `compress`) |
| `billable` | Whether or not your project was billed for the request |
| `customDomain` | Whether or not the request was made against a custom domain |
| `hostname` | The hostname that the request was made against |
| `remoteIpCountry` | The originating country of the request |
| `remoteIpCity` | The originating city of the request |

## Use log-based metrics

You can view and build
[log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics),
then use these metrics in Cloud Monitoring to create charts and alerting
policies.

- Leverage
  [predefined system metrics](https://cloud.google.com/logging/docs/logs-based-metrics#logs-based_metrics_interface)
  that are automatically recorded, such as the number of logging events that
  occurred within a specific time period.

- Create
  [user-defined metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#user-defined_metrics)
  for your project. You can count the number of log entries that match a given
  query or keep track of particular values with the matching log entries. You
  can filter using regular expressions.

- Use
  [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)
  to record the number of log entries containing particular messages or extract
  latency information reported in log entries. You can then use these metrics in
  charts and alerting policies.

Firebase Hosting also generates the following Hosting-specific logging
metrics. These metrics are not specific to a log entry but rather to the
specific Hosting site as a whole.

- `log_bytes`: Total bytes of data usage for each site

- `response_count`: Total count of responses written for the site

  This metric includes the field of HTTP status, so you can plot HTTP responses
  by status (as an example).

## Export logs to other Google Cloud tools

You can also export your site's logs to other Google Cloud tools, like
Cloud Monitoring or BigQuery, for example:

- Using
  [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs),
  you can create log-based metrics that you can use in charts and alerting
  policies.

- Using [BigQuery](https://cloud.google.com/bigquery), you can do any of
  the following:

  - Use Looker Studio to generate dashboards of your Hosting data.
  - Run queries to get more insight into your requests (average response size, cache hits vs misses, etc.).
  - Learn which URLs your users actually request.
  - Combine your Hosting data with other Firebase data that you exported to BigQuery and query it in new ways.