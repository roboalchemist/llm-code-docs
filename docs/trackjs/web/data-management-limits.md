# Source: https://docs.trackjs.com/data-management/limits/

Title: Retention and Limits

URL Source: https://docs.trackjs.com/data-management/limits/

Markdown Content:
Data Retention
--------------

All TrackJS plans have a [Retention Period](https://trackjs.com/pricing/) that specifies how long we will retain errors from your pages. Typically, errors that are relevant and important continue to happen frequently, so a short retention period serves most customers well.

If there is a particular error that is interesting and you’d like to retain it beyond your plan’s retention period, you can Star or Share the error. Starred and Shared errors are exempt from the retention policies, and we will hold onto them for as long as you maintain your account.

Capture Throttle
----------------

All TrackJS plans have a [High-Volume Error Throttle](https://trackjs.com/pricing/) that specifies how many errors can be saved every minute, and anything over that limit is discarded. This limit is applied per minute: each minute you get a new quota of errors that can be saved.

You can see if your account is hitting the throttle from the [Usage Report](https://my.trackjs.com/usage) in the Dashboard. Errors that are “Dropped” were in excess of your throttle limit.

This limit ensures you can send us as many errors as you want over the entire month, and we’ll keep saving a consistent number of errors. There’s nothing you need to worry about as far as overages with the capture throttle. It simply keeps your noise levels low and the system performant.

**TIP**[Ignored errors](https://docs.trackjs.com/data-management/ignore/) do not count against the Capture Throttle limit. If your account is dropping errors, consider Ignoring errors that are not relevant to you. You can also increase your limit by [subscribing to a higher plan](https://trackjs.com/pricing/).

Agent Throttle
--------------

In addition to the [Capture Throttle](https://docs.trackjs.com/data-management/limits/#capture-throttle), the Browser Agent throttles errors reported from noisy clients by [deduplicating](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#dedupe) subsequent identical errors and limiting the number of errors that can be sent in 1 second to 10. This limit continually resets itself and reduces a lot of noise from your reports.

Error Report Limit
------------------

The [Capture API](https://docs.trackjs.com/data-api/capture/) is limited payloads less than 100kb. If a larger payload is sent, it will return a `413 Payload Too Large` response. This limit is in place to ensure timely processing of error records and to protect the system from attack from very large data streams. In most practical use cases, an error report should not approach this size.

Automatic Truncation
--------------------

As of [version 2.11.0](https://docs.trackjs.com/browser-agent/changelog/), the Browser Agent will attempt to truncate large errors that may be rejected due to the [Error Report Limit](https://docs.trackjs.com/data-management/limits/#error-report-limit) by truncating Network Telemetry URLs, Visitor Telemetry Elements, and Console Telemetry Messages.

Truncated values will be appended with “`...{COUNT}`” where `COUNT` is the number of characters that have been removed.
