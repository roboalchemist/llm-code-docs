# Source: https://docs.curator.interworks.com/site_administration/logging/logging_overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Logging Overview

> Understanding Curator logging systems including usage logs, event logs, access logs, and alert logs.

Curator provides several logging systems to help administrators monitor, troubleshoot, and audit their Curator
instance. Logs are available through both the Curator backend interface and directly on the server file system.

## Types of Logs

Curator maintains several different log types, each serving a specific purpose:

| Log Type                                                                          | Purpose                                     | Access             |
| --------------------------------------------------------------------------------- | ------------------------------------------- | ------------------ |
| [Usage Log](/site_administration/logging/database_logs#usage-log)                 | Audit trail of who made what changes        | Curator Backend    |
| [Event Log](/site_administration/logging/database_logs#event-log)                 | Records system events, errors, and warnings | Curator Backend    |
| [Access Log](/site_administration/logging/database_logs#access-log)               | Logs backend administrator access           | Curator Backend    |
| [Alert Log](/site_administration/logging/database_logs#alert-log)                 | Aggregates recurring system alerts          | Curator Backend    |
| [System Log](/site_administration/logging/file_based_logs#system-log)             | Detailed application logs for debugging     | Server File System |
| [PHP Error Log](/site_administration/logging/file_based_logs#php-error-log)       | PHP runtime errors and warnings             | Server File System |
| [Apache Error Log](/site_administration/logging/file_based_logs#apache-error-log) | Web server errors and access information    | Server File System |

## Backend Logs vs Server Logs

**[Backend Logs](/site_administration/logging/database_logs)** are stored in the Curator database and accessible
through the Curator backend interface. These logs are designed for day-to-day monitoring and auditing by
administrators who may not have direct server access.

**[Server Logs](/site_administration/logging/file_based_logs)** are stored as files on the server and require
direct server or file system access. These logs are typically used for deeper troubleshooting, especially when
database connectivity issues prevent backend access or when investigating web server configuration problems.

## API Access

Curator provides API endpoints for programmatic access to log data. All API endpoints require a valid API key.
For general information about using the Curator API, see the
[Curator API Overview](/curator_api/getting_started/curator_api_overview).

### List Event Log

Returns event log entries with pagination support.

```
GET /api/v1/portal/listEventLog?apikey=YOUR_API_KEY
```

**Parameters:**

* `limit` (optional) - Maximum number of results to return (default: 1000)
* `offset` (optional) - Number of results to skip for pagination (default: 0)

### List Usage Log

Returns usage log entries with filtering options.

```
GET /api/v1/portal/listUsageLog?apikey=YOUR_API_KEY
```

**Parameters:**

* `limit` (optional) - Maximum number of results to return (default: 1000)
* `offset` (optional) - Number of results to skip for pagination (default: 0)
* `username` (optional) - Filter results by username
* `is_frontend` (optional) - Filter by frontend (`true`), backend (`false`), or both (omit parameter)

### List Alert Log

Returns alert log entries with filtering options.

```
GET /api/v1/portal/listAlertLogs?apikey=YOUR_API_KEY
```

**Parameters:**

* `limit` (optional) - Maximum number of results to return (default: 1000)
* `offset` (optional) - Number of results to skip for pagination (default: 0)
* `status` (optional) - Filter by status: `active`, `resolved`, `suppressed`
* `level` (optional) - Filter by level: `error`, `warning`, `info`

### Download System Log

Downloads the current system log file.

```
GET /api/v1/portal/downloadLog?apikey=YOUR_API_KEY
```

This endpoint returns the `storage/logs/system.log` file as a downloadable attachment.

## Best Practices

1. **Set appropriate retention periods** - Balance the need for historical data against database storage
   requirements. For most installations, 1-3 months of event log retention is sufficient.

2. **Monitor the Alert Log** - Regularly review the Status page to catch recurring issues early.

3. **Archive logs before purging** - If compliance requirements mandate long-term log retention, use the API
   endpoints to export log data before automatic purging occurs.

4. **Review Access Logs periodically** - Regular review of administrator access helps identify unauthorized
   access attempts.

5. **Check multiple log sources** - When troubleshooting issues, check both backend logs and server logs for
   a complete picture. The System Log may contain entries not present in the Event Log.
