# Source: https://render.com/docs/logging.md

# Logs in the Render Dashboard


> *Want to stream logs to your observability provider?*
>
> See [Streaming Render Service Logs](log-streams).

View, search, and filter your service's runtime logs from its *Logs* page in the [Render Dashboard](https://dashboard.render.com):

[image: Log explorer in the Render Dashboard]

With a [*Professional* workspace](professional-features) or higher, the log explorer also shows [HTTP request logs](#http-request-logs) for web services.

Use any combination of text search and [supported filters](#log-filters) to narrow results:

[image: Log explorer in the Render Dashboard]

Separately, you can view logs for any recent [deploy or one-off job](#logs-for-an-individual-deploy-or-job).

Render does not emit logs for [static sites](static-sites).

## Inspecting a log line

Log lines in the explorer display the following information:

[image: Log line format]

> [HTTP request logs](#http-request-logs) display the request's HTTP method and status code instead of an instance ID.

------

###### Component

*Level*

###### Description

An icon representing the log level, such as `info`, `warning`, or `error`. Hidden for `info`-level lines until you hover. Hover to view the log level as text. Supports the following values:

- `debug`
- `info`
- `notice`
- `warning`
- `error`
- `critical`
- `alert`
- `emergency`

---

###### Component

*Timestamp*

###### Description

The time of day the log was generated, in your local time zone. Mouse over this value to view the _full_ timestamp in local, UTC, and Unix formats.

---

###### Component

*Instance*

###### Description

The identifier for the service instance that generated the log, surrounded by square brackets. Helpful for filtering logs for a [scaled service](scaling), or for pinpointing an instance swap during a deploy. Click this value to add it as a search filter. [HTTP request logs](#http-request-logs) are aggregated at the service level (not the individual instance level), so they do not display this value.

---

###### Component

*Message*

###### Description

The logged message. [HTTP request logs](#http-request-logs) instead display the details for the corresponding HTTP request, such as:

- HTTP method
- Status code
- Requested URL

------

## Log filters

When searching with the log explorer, you can filter results by the following (in addition to searching for an arbitrary string):

------

###### Filter

Time range / Live tail

###### Description

Limit results to a predefined range (such as *Last 24 hours*), specify a custom range, or select *Live tail* to view a live feed of recent logs. The default displayed range is *Last hour*. Specify a different range using the dropdown in the upper right of the log explorer. The maximum available range depends on your workspace's [log retention period](#retention-period).

---

###### Filter

`level`

###### Description

The log level. Specify in the search box. Supports the following values:

- `debug`
- `info`
- `notice`
- `warning`
- `error`
- `critical`
- `alert`
- `emergency`

---

###### Filter

`instance`

###### Description

The ID of the service instance that generated the log. Helpful for filtering logs for a [scaled service](scaling), or for pinpointing an instance swap during a deploy. Specify in the search box. You can also click the instance ID for any log line to add it as a filter.

---

###### Filter

`method`

###### Description

*[HTTP request logs](#http-request-logs) only.* The HTTP method of a particular request (such as `GET` or `POST`). Specify in the search box.

---

###### Filter

`status_code`

###### Description

*[HTTP request logs](#http-request-logs) only.* The response code for a particular request (such as `200`, `404`, or `500`). Specify in the search box.

---

###### Filter

`host`

###### Description

*[HTTP request logs](#http-request-logs) only.* The destination domain of a particular request (such as `my-web-service.onrender.com`). Helpful if your service has multiple [custom domains](custom-domains) used by different clients. Specify in the search box.

---

###### Filter

`path`

###### Description

*[HTTP request logs](#http-request-logs) only.* The path of a particular request (such as `/api/orders` or `/blog/post/123`). Helpful for filtering logs for a specific resource or endpoint. Specify in the search box.

------

## Wildcards and regular expressions

The log explorer supports searching with wildcards and regular expressions.

To match any number of characters, use the wildcard token (`*`). To match against a regular expression, enclose your search in forward slashes (`/`). You can then use any metacharacters supported by the [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

You can use wildcards and regular expressions in search strings and in filters. See the table below for some useful examples.

| Search | Description |
| --- | --- |
| `foo*bar` | Returns logs that contain `foo` followed by `bar` using wildcard search. |
| `/foo.*bar/` | Returns logs that contain `foo` followed by `bar` using a regular expression. |
| `/(foo\|bar)/` | Returns logs that contain `foo` or `bar`. |
| `status_code:/4../` | Returns request logs with a `4xx` status code. |
| `method:/(GET\|POST)/` | Returns request logs with a `GET` or `POST` method. |
| `path:api/resource/*/subresource` | Returns request logs with a path that starts with `api/resource/` and ends with `/subresource`. |
| `/responseTimeMS=\d{3}\d+/` | Returns request logs with a response time greater than one second. |

## Keyboard shortcuts

The log explorer supports these keyboard shortcuts:

| Action | Shortcut |
| --- | --- |
| Focus search bar | `/` |
| Enable fullscreen | `M` |
| Exit fullscreen | `M` or `Esc` |
| Scroll (slow) | `Arrow Up` / `Arrow Down` |
| Scroll (fast) | `Page Up` / `Page Down` |
| Jump to top | `Home` |
| Jump to bottom | `End` |
| Copy all currently displayed logs | `CMD+Shift+C` (macOS) `CTRL+Shift+C` (Windows/Linux) |
| Clear logs (live tail view only) | `Shift+L` |

## HTTP request logs

If you have a [*Professional* workspace](professional-features) or higher, Render generates a log entry for each HTTP request to your team's web services from the public internet:

[image: HTTP request logs in the Render Dashboard]

This helps you debug unexpected behavior for a request, in particular by tracing its execution via the [`requestID` field](#tracing-with-requestid-and-rndr-id).

HTTP request logs appear alongside application logs in the explorer, and they support additional [filters](#log-filters) (such as `method` and `status_code`).

> Render does _not_ generate request logs for HTTP requests sent from other services over your private network—only for requests sent to web services over the public internet.

### Tracing with `requestID` and `Rndr-Id`

In each [HTTP request log entry](#http-request-logs), the value of the `requestID` field uniquely identifies the associated request:

```log
11:24:03 [GET] example.com/api/orders clientIP="198.51.100.3" requestID="8ebfa3c3-8929-4885" ...
```

Render includes this same value in the `Rndr-Id` HTTP header—both in the request to your web service _and_ in the response to the requesting client:

```http
Rndr-Id: 58ebfa3c3-8929-4885
```

In your web service's code, you can extract this value from the header and include it in every log you generate for a given request. If you do, you can search for this ID in the log explorer to view the corresponding request's chronological log history.

On the client's side, here's what a `Rndr-Id` looks like in Chrome's Network panel:

[image: Viewing the Rndr-Id header in Chrome]

By tracing each phase of the request lifecycle with one consistent ID, you can more quickly diagnose and debug issues in collaboration with the users who encounter them.

## Logs for an individual deploy or job

View the logs for an individual deploy of your service from the service's *Events* page. Click the word *Deploy* in a timeline entry to open the log explorer:

[image: Selecting a deploy to view logs]

⬇️

[image: Viewing logs for a single deploy]

Similarly, you can view logs for the execution of a [one-off job](one-off-jobs) from the associated service's *Jobs* page.

## Explorer theme

The log explorer supports both light and dark display themes. It defaults to matching the theme that you [set for the Render Dashboard](render-dashboard#set-your-display-theme).

You can independently set the explorer's theme from the *Appearance* section of your [User Settings page](https://dashboard.render.com/u/settings#appearance):

[image: Log explorer theme settings in the Render Dashboard]

## Log limits

### Retention period

Render's log retention period depends on your workspace's plan (see the [pricing page](/pricing)):

| Workspace Plan | Retention Period |
| --- | --- |
| Hobby | 7 days |
| Professional | 14 days |
| Organization / Enterprise | 30 days |

Logs older than your current retention period are no longer available, even if you upgrade your plan to extend the period.

If you need to retain logs for a longer period, you can [stream your logs to a syslog-compatible provider](log-streams).

### Rate limit

Render processes a maximum of 6,000 application-generated log lines per minute for each running instance of a service.

If an instance generates logs in excess of this limit, Render drops the excess log lines. Dropped log lines don't appear in the log explorer or in [log streams](log-streams).

---

##### Appendix: Glossary definitions

###### private network

Your Render services in the same *region* can reach each other without traversing the public internet, enabling faster and safer communication.

Related article: https://render.com/docs/private-network.md