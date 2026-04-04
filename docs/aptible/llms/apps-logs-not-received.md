# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/apps-logs-not-received.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# App Logs Not Being Received

## Cause

There can be several causes why a [Log Drain](/core-concepts/observability/logs/log-drains/overview) would stop receiving logs from your app:

* Your logging provider stopped accepting logs (e.g., because you are over quota)

* Your app stopped emitting logs

* The Log Drain crashed

## Resolution

You can start by restarting your Log Drain via the Dashboard. To do so, Navigate to the "Logging" Tab, then click on "Restart" next to the affected Log Drain.

If logs do not appear within a few minutes, the issue is likely somewhere else; contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) for assistance.
