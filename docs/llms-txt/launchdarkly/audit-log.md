# Source: https://launchdarkly.com/docs/api/audit-log.md

LaunchDarkly maintains a record of all the changes made to any resource in the system. You can access this history using the audit log API, including filtering by timestamps, or using a custom policy to select which entries to receive.

Several of the endpoints in the audit log API require an audit log entry ID. The audit log entry ID is returned as part of the [List audit log entries](https://launchdarkly.com/docs/api/audit-log/get-audit-log-entries) response. It is the `_id` field of each element in the `items` array.

In the LaunchDarkly UI, this information appears on the **Change history** page. To learn more, read [Change history](https://launchdarkly.com/docs/home/observability/change-history).
