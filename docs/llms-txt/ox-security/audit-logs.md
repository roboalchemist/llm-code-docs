# Source: https://docs.ox.security/admin-settings/audit-logs.md

# Audit Logs

Audit logs display the results of recent logins, scans and other actions. From the menu pane, go to **ADMIN > Audit Logs**.

Use this page to:

* monitor logins, scans and user actions
* investigate unusual or unauthorized activity

## Prerequisites

You need read/write permissions to view audit logs.

## Audit log event types

For a list of log event types, see the article [logType](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/log-type).

## Audit log details

The page includes the following elements:

* **Filters:** Use the filter pane for single or multi-select filters. The filters display actions completed in the selected period.
* **Summary metrics:** Shows the total log count.
* **Execution list:** Displays details for each login or scan.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-096a300857934dfa4ecfa61e009ca30234945f8f%2Fox%20audit%20log%20page%20main%20screen.png?alt=media" alt=""><figcaption></figcaption></figure></div>

<table><thead><tr><th width="177" valign="top">Element</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Period filter<br>(in the header)</td><td valign="top">Filters the results to the selected period.</td></tr><tr><td valign="top">Total</td><td valign="top">Displays the total number of actions based on the applied filters.</td></tr><tr><td valign="top">Search bar</td><td valign="top">Enter text to search for a specific term.</td></tr><tr><td valign="top">Filters</td><td valign="top"><p>Select one or multiple filters:</p><ul><li><strong>Action:</strong> Examples: Login, Scan Now. Slack Alert Sent, Jira Ticket Opened.</li><li><strong>User</strong></li><li><strong>Log Type</strong>: Examples: Authentication, Scan</li></ul></td></tr><tr><td valign="top">Log details</td><td valign="top"><p>Use the tooltips to identify icons.</p><ul><li><strong>User:</strong> The name of the user.</li><li><strong>Action:</strong> Login or Scan.</li><li><strong>Additional Info:</strong> Shows additional details like the User Role or Scan ID.</li><li><strong>Log Type</strong></li><li><strong>Date:</strong> The date of the action.</li></ul></td></tr></tbody></table>

## Exporting Audit Logs

In addition to viewing audit logs in the OX platform, you can export audit logs to an external Amazon S3 bucket. Audit log export is typically used when you need to:

* **Centralized logging:** Consume audit logs using existing log processing pipelines.
* **Compliance and retention:** Store audit logs in customer-managed, long-term storage.
* **Automation:** Enable automated analysis outside the OX platform.

### How audit log export works

Audit logs are exported as JSON files to a customer-managed S3 bucket.

Each export includes all audit log events generated since the previous export.

If no user or system activity occurred during the export window, the exported file still contains a system-generated event indicating that the export ran successfully.

### Authentication and Permissions

Audit log export uses an AWS role-based connector.

During setup:

* OX generates a unique external ID
* An AWS IAM role is created with permission to write to the specified S3 bucket

The role ARN and external ID are used together to securely authenticate export operations.

### Audit log export configuration

Audit log export is configured from the **Settings → Audit Logs → Configuration** page after the relevant connector is enabled.

| Setting          | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| S3 bucket        | The Amazon S3 bucket where audit logs are exported.            |
| S3 region        | The AWS region where the bucket is located.                    |
| S3 bucket prefix | Optional folder inside the bucket where audit logs are stored. |
| Export frequency | Interval, in hours (1–24), at which audit logs are exported.   |

> **Note**\
> The first export runs at the beginning of the next full hour after the configuration is saved.\
> Subsequent exports run according to the configured frequency.

### Exported file structure

Audit logs are written to the S3 bucket using a structured folder hierarchy that is created automatically by OX.

```
<bucket-prefix>/audit-logs/<organization-name>/<timestamp>.json
```

The folder structure and file naming convention are managed by the platform and cannot be customized.
