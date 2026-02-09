# Source: https://docs.augmentcode.com/context-services/sdk/api-reference.md

# Source: https://docs.augmentcode.com/analytics/api-reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics API Reference

> Detailed API endpoint documentation.

<Note>
  **Preview Feature**

  The Analytics API is currently in preview and is available exclusively to Enterprise customers.
</Note>

<Note>
  **Important: Timezone and Data Availability**

  All dates in requests and responses are interpreted and returned in **UTC timezone**. The most recent queryable date is "yesterday" (UTC), and data for the previous day becomes available at approximately **02:00 UTC** each day.
</Note>

<Note>
  **Data Freshness**

  Analytics data is updated once daily. Data for a given day becomes available the following day at approximately 02:00 UTC.
</Note>

## GET /analytics/v0/dau-count

Returns daily active user counts over a date range.

### Query Parameters

| Parameter   | Type   | Required | Description                             |
| ----------- | ------ | -------- | --------------------------------------- |
| start\_date | string | No       | Start date in `YYYY-MM-DD` format (UTC) |
| end\_date   | string | No       | End date in `YYYY-MM-DD` format (UTC)   |

### Date Range Behavior

| Scenario                   | Behavior                                                       |
| -------------------------- | -------------------------------------------------------------- |
| Neither date provided      | Returns last 7 days ending at yesterday (UTC)                  |
| Only `start_date` provided | Returns 7 days starting from `start_date`, capped at yesterday |
| Only `end_date` provided   | Returns 7 days ending at `end_date`                            |
| Both dates provided        | Returns the specified inclusive range                          |

### Constraints

| Constraint                  | Value                                                |
| --------------------------- | ---------------------------------------------------- |
| Maximum date range          | 90 days                                              |
| Maximum historical lookback | 2 years                                              |
| Today and future dates      | Not allowed (data available at \~02:00 UTC next day) |
| Timezone                    | All dates interpreted as UTC                         |

### Example Request

```bash  theme={null}
curl -X GET "https://api.augmentcode.com/analytics/v0/dau-count?start_date=2025-10-15&end_date=2025-10-20" \
  -H "Authorization: Bearer <your-api-token>"
```

### Example Response

```json  theme={null}
{
  "daily_active_user_counts": [
    {"date": "2025-10-15", "user_count": 100},
    {"date": "2025-10-16", "user_count": 120},
    {"date": "2025-10-17", "user_count": 95},
    {"date": "2025-10-18", "user_count": 140},
    {"date": "2025-10-19", "user_count": 88},
    {"date": "2025-10-20", "user_count": 110}
  ],
  "metadata": {
    "effective_start_date": "2025-10-15",
    "effective_end_date": "2025-10-20",
    "generated_at": "2025-10-21T10:30:00Z",
    "total_days": 6
  }
}
```

### Response Fields

| Field                                      | Type    | Description                                           |
| ------------------------------------------ | ------- | ----------------------------------------------------- |
| daily\_active\_user\_counts                | array   | Array of daily user counts, one per day               |
| daily\_active\_user\_counts\[].date        | string  | Calendar date (`YYYY-MM-DD`)                          |
| daily\_active\_user\_counts\[].user\_count | integer | Number of unique active users                         |
| metadata.effective\_start\_date            | string  | Actual start date used (UTC, after defaults/clamping) |
| metadata.effective\_end\_date              | string  | Actual end date used (UTC, after defaults/clamping)   |
| metadata.generated\_at                     | string  | Response generation timestamp (ISO 8601)              |
| metadata.total\_days                       | integer | Number of days in the range                           |

***

## GET /analytics/v0/dau

Returns the list of active users for a specific date. Supports pagination.

### Query Parameters

| Parameter  | Type    | Required | Description                                |
| ---------- | ------- | -------- | ------------------------------------------ |
| date       | string  | No       | Date to query in `YYYY-MM-DD` format (UTC) |
| cursor     | string  | No       | Pagination cursor from previous response   |
| page\_size | integer | No       | Number of results per page                 |

### Date Behavior

| Scenario          | Behavior                                                         |
| ----------------- | ---------------------------------------------------------------- |
| Date not provided | Defaults to yesterday (UTC)                                      |
| Date provided     | Returns users active on that date (must be yesterday or earlier) |

### Pagination

| Parameter  | Default | Maximum |
| ---------- | ------- | ------- |
| page\_size | 100     | 250     |

To paginate through results:

1. Make initial request (optionally with `page_size`)
2. If `pagination.has_more` is `true`, use `pagination.next_cursor` as the `cursor` parameter
3. Repeat until `has_more` is `false`

### Constraints

| Constraint                  | Value                                                |
| --------------------------- | ---------------------------------------------------- |
| Maximum historical lookback | 2 years                                              |
| Today and future dates      | Not allowed (data available at \~02:00 UTC next day) |
| Timezone                    | All dates interpreted as UTC                         |

### Example Request (First Page)

```bash  theme={null}
curl -X GET "https://api.augmentcode.com/analytics/v0/dau?date=2025-10-15&page_size=50" \
  -H "Authorization: Bearer <your-api-token>"
```

### Example Response

```json  theme={null}
{
  "users": [
    {"user_email": "alice@example.com"},
    {"user_email": "bob@example.com"},
    {"service_account_name": "ci-bot"}
  ],
  "pagination": {
    "next_cursor": "eyJsYXN0X2lkIjoidXNlcjUwIn0=",
    "has_more": true
  },
  "metadata": {
    "effective_date": "2025-10-15",
    "generated_at": "2025-10-16T10:30:00Z",
    "returned_user_count": 3
  }
}
```

### Example Request (Next Page)

```bash  theme={null}
curl -X GET "https://api.augmentcode.com/analytics/v0/dau?date=2025-10-15&page_size=50&cursor=eyJsYXN0X2lkIjoidXNlcjUwIn0=" \
  -H "Authorization: Bearer <your-api-token>"
```

### Response Fields

| Field                           | Type    | Description                                              |
| ------------------------------- | ------- | -------------------------------------------------------- |
| users                           | array   | Array of active users                                    |
| users\[].user\_email            | string  | User's email address (for regular users)                 |
| users\[].service\_account\_name | string  | Service account name (for service accounts)              |
| pagination.next\_cursor         | string  | Cursor for fetching next page (empty if no more results) |
| pagination.has\_more            | boolean | `true` if more results are available                     |
| metadata.effective\_date        | string  | Actual date used (UTC, after defaults)                   |
| metadata.generated\_at          | string  | Response generation timestamp (ISO 8601)                 |
| metadata.returned\_user\_count  | integer | Number of users returned in this page                    |

<Note>Each user has either `user_email` or `service_account_name`, never both.</Note>

***

## GET /analytics/v0/daily-usage

Returns daily usage metrics for your organization over a date range. Days with no activity are omitted from the response.

### Query Parameters

| Parameter   | Type   | Required | Description                             |
| ----------- | ------ | -------- | --------------------------------------- |
| start\_date | string | No       | Start date in `YYYY-MM-DD` format (UTC) |
| end\_date   | string | No       | End date in `YYYY-MM-DD` format (UTC)   |

### Date Range Behavior

| Scenario                   | Behavior                                                       |
| -------------------------- | -------------------------------------------------------------- |
| Neither date provided      | Returns last 7 days ending at yesterday (UTC)                  |
| Only `start_date` provided | Returns 7 days starting from `start_date`, capped at yesterday |
| Only `end_date` provided   | Returns 7 days ending at `end_date`                            |
| Both dates provided        | Returns the specified inclusive range                          |

### Constraints

| Constraint                  | Value                                                |
| --------------------------- | ---------------------------------------------------- |
| Maximum date range          | 90 days                                              |
| Maximum historical lookback | 2 years                                              |
| Today and future dates      | Not allowed (data available at \~02:00 UTC next day) |
| Timezone                    | All dates interpreted as UTC                         |

### Example Request

```bash  theme={null}
curl -s -X GET "https://api.augmentcode.com/analytics/v0/daily-usage?start_date=2025-10-15&end_date=2025-10-20" \
  -H "Authorization: Bearer <your-api-token>" | jq .
```

### Example Response

```json  theme={null}
{
  "daily_usage": [
    {
      "date": "2025-10-15",
      "metrics": {
        "total_modified_lines_of_code": 1250,
        "total_messages": 340,
        "total_tool_calls": 890,
        "completions_count": 1500,
        "completions_accepted": 1120,
        "completions_lines_of_code": 980,
        "chat_messages": 85,
        "remote_agent_messages": 45,
        "remote_agent_lines_of_code": 120,
        "ide_agent_messages": 150,
        "ide_agent_lines_of_code": 95,
        "cli_agent_interactive_messages": 40,
        "cli_agent_interactive_lines_of_code": 35,
        "cli_agent_non_interactive_messages": 20,
        "cli_agent_non_interactive_lines_of_code": 20
      }
    }
  ],
  "metadata": {
    "effective_start_date": "2025-10-15",
    "effective_end_date": "2025-10-20",
    "generated_at": "2025-10-21T10:30:00Z",
    "total_days": 1
  }
}
```

### Response Fields

| Field                                                                 | Type    | Description                                                      |
| --------------------------------------------------------------------- | ------- | ---------------------------------------------------------------- |
| daily\_usage                                                          | array   | Array of daily usage data points (days with no activity omitted) |
| daily\_usage\[].date                                                  | string  | Calendar date (`YYYY-MM-DD`)                                     |
| daily\_usage\[].metrics                                               | object  | Usage metrics for this date                                      |
| daily\_usage\[].metrics.total\_modified\_lines\_of\_code              | integer | Total lines of code modified across all interactions             |
| daily\_usage\[].metrics.total\_messages                               | integer | Total messages across all interaction types                      |
| daily\_usage\[].metrics.total\_tool\_calls                            | integer | Total tool calls across all agent types                          |
| daily\_usage\[].metrics.completions\_count                            | integer | Number of completion requests                                    |
| daily\_usage\[].metrics.completions\_accepted                         | integer | Number of completions accepted by users                          |
| daily\_usage\[].metrics.completions\_lines\_of\_code                  | integer | Lines of code from completions                                   |
| daily\_usage\[].metrics.completions\_suggested\_lines\_of\_code       | integer | Lines of code suggested by completions (before acceptance)       |
| daily\_usage\[].metrics.chat\_messages                                | integer | Number of chat messages                                          |
| daily\_usage\[].metrics.remote\_agent\_messages                       | integer | Number of Remote Agent messages                                  |
| daily\_usage\[].metrics.remote\_agent\_lines\_of\_code                | integer | Lines of code from Remote Agent                                  |
| daily\_usage\[].metrics.ide\_agent\_messages                          | integer | Number of IDE Agent messages                                     |
| daily\_usage\[].metrics.ide\_agent\_lines\_of\_code                   | integer | Lines of code from IDE Agent                                     |
| daily\_usage\[].metrics.cli\_agent\_interactive\_messages             | integer | Number of CLI Agent interactive messages                         |
| daily\_usage\[].metrics.cli\_agent\_interactive\_lines\_of\_code      | integer | Lines of code from CLI Agent interactive mode                    |
| daily\_usage\[].metrics.cli\_agent\_non\_interactive\_messages        | integer | Number of CLI Agent non-interactive messages                     |
| daily\_usage\[].metrics.cli\_agent\_non\_interactive\_lines\_of\_code | integer | Lines of code from CLI Agent non-interactive mode                |
| metadata.effective\_start\_date                                       | string  | Actual start date used (UTC, after defaults/clamping)            |
| metadata.effective\_end\_date                                         | string  | Actual end date used (UTC, after defaults/clamping)              |
| metadata.generated\_at                                                | string  | Response generation timestamp (ISO 8601)                         |
| metadata.total\_days                                                  | integer | Number of days with data in the response                         |

***

## GET /analytics/v0/user-activity

Returns aggregated usage metrics per user over a date range. Users with no activity are omitted. Supports pagination.

### Query Parameters

| Parameter   | Type    | Required | Description                              |
| ----------- | ------- | -------- | ---------------------------------------- |
| start\_date | string  | No       | Start date in `YYYY-MM-DD` format (UTC)  |
| end\_date   | string  | No       | End date in `YYYY-MM-DD` format (UTC)    |
| cursor      | string  | No       | Pagination cursor from previous response |
| page\_size  | integer | No       | Number of results per page               |

### Date Range Behavior

| Scenario                   | Behavior                                                       |
| -------------------------- | -------------------------------------------------------------- |
| Neither date provided      | Returns last 7 days ending at yesterday (UTC)                  |
| Only `start_date` provided | Returns 7 days starting from `start_date`, capped at yesterday |
| Only `end_date` provided   | Returns 7 days ending at `end_date`                            |
| Both dates provided        | Returns the specified inclusive range                          |

### Pagination

| Parameter  | Default | Maximum |
| ---------- | ------- | ------- |
| page\_size | 50      | 100     |

To paginate through results:

1. Make initial request (optionally with `page_size`)
2. If `pagination.has_more` is `true`, use `pagination.next_cursor` as the `cursor` parameter
3. Repeat until `has_more` is `false`

### Constraints

| Constraint                  | Value                                                |
| --------------------------- | ---------------------------------------------------- |
| Maximum date range          | 90 days                                              |
| Maximum historical lookback | 2 years                                              |
| Today and future dates      | Not allowed (data available at \~02:00 UTC next day) |
| Timezone                    | All dates interpreted as UTC                         |

### Example Request

```bash  theme={null}
curl -s -X GET "https://api.augmentcode.com/analytics/v0/user-activity?start_date=2025-10-15&end_date=2025-10-20&page_size=3" \
  -H "Authorization: Bearer <your-api-token>" | jq .
```

### Example Response

```json  theme={null}
{
  "users": [
    {
      "user_email": "alice@example.com",
      "active_days": 5,
      "metrics": {
        "total_modified_lines_of_code": 450,
        "total_messages": 65,
        "total_tool_calls": 120,
        "completions_count": 320,
        "completions_accepted": 280,
        "completions_lines_of_code": 350,
        "chat_messages": 25,
        "remote_agent_messages": 10,
        "remote_agent_lines_of_code": 45,
        "ide_agent_messages": 30,
        "ide_agent_lines_of_code": 40,
        "cli_agent_interactive_messages": 8,
        "cli_agent_interactive_lines_of_code": 10,
        "cli_agent_non_interactive_messages": 5,
        "cli_agent_non_interactive_lines_of_code": 5
      }
    },
    {
      "user_email": "bob@example.com",
      "active_days": 3,
      "metrics": {
        "total_modified_lines_of_code": 280,
        "total_messages": 70,
        "total_tool_calls": 75,
        "completions_count": 150,
        "completions_accepted": 120,
        "completions_lines_of_code": 180,
        "chat_messages": 40,
        "remote_agent_messages": 5,
        "remote_agent_lines_of_code": 25,
        "ide_agent_messages": 20,
        "ide_agent_lines_of_code": 55,
        "cli_agent_interactive_messages": 3,
        "cli_agent_interactive_lines_of_code": 15,
        "cli_agent_non_interactive_messages": 2,
        "cli_agent_non_interactive_lines_of_code": 5
      }
    },
    {
      "service_account_name": "ci-bot",
      "active_days": 6,
      "metrics": {
        "total_modified_lines_of_code": 200,
        "total_messages": 50,
        "total_tool_calls": 85,
        "completions_count": 0,
        "completions_accepted": 0,
        "completions_lines_of_code": 0,
        "chat_messages": 0,
        "remote_agent_messages": 0,
        "remote_agent_lines_of_code": 0,
        "ide_agent_messages": 0,
        "ide_agent_lines_of_code": 0,
        "cli_agent_interactive_messages": 0,
        "cli_agent_interactive_lines_of_code": 0,
        "cli_agent_non_interactive_messages": 50,
        "cli_agent_non_interactive_lines_of_code": 200
      }
    }
  ],
  "pagination": {
    "next_cursor": "eyJsYXN0X2lkIjoidXNlcjMifQ==",
    "has_more": true
  },
  "metadata": {
    "effective_start_date": "2025-10-15",
    "effective_end_date": "2025-10-20",
    "generated_at": "2025-10-21T10:30:00Z",
    "total_days": 6,
    "returned_user_count": 3
  }
}
```

### Response Fields

| Field                                                          | Type    | Description                                                     |
| -------------------------------------------------------------- | ------- | --------------------------------------------------------------- |
| users                                                          | array   | Array of user activity records (users with no activity omitted) |
| users\[].user\_email                                           | string  | User's email address (for regular users)                        |
| users\[].service\_account\_name                                | string  | Service account name (for service accounts)                     |
| users\[].active\_days                                          | integer | Number of distinct days with activity in the date range         |
| users\[].metrics                                               | object  | Usage metrics for this user (summed over date range)            |
| users\[].metrics.total\_modified\_lines\_of\_code              | integer | Total lines of code modified across all interactions            |
| users\[].metrics.total\_messages                               | integer | Total messages across all interaction types                     |
| users\[].metrics.total\_tool\_calls                            | integer | Total tool calls across all agent types                         |
| users\[].metrics.completions\_count                            | integer | Number of completion requests                                   |
| users\[].metrics.completions\_accepted                         | integer | Number of completions accepted                                  |
| users\[].metrics.completions\_lines\_of\_code                  | integer | Lines of code from completions                                  |
| users\[].metrics.completions\_suggested\_lines\_of\_code       | integer | Lines of code suggested by completions (before acceptance)      |
| users\[].metrics.chat\_messages                                | integer | Number of chat messages                                         |
| users\[].metrics.remote\_agent\_messages                       | integer | Number of Remote Agent messages                                 |
| users\[].metrics.remote\_agent\_lines\_of\_code                | integer | Lines of code from Remote Agent                                 |
| users\[].metrics.ide\_agent\_messages                          | integer | Number of IDE Agent messages                                    |
| users\[].metrics.ide\_agent\_lines\_of\_code                   | integer | Lines of code from IDE Agent                                    |
| users\[].metrics.cli\_agent\_interactive\_messages             | integer | Number of CLI Agent interactive messages                        |
| users\[].metrics.cli\_agent\_interactive\_lines\_of\_code      | integer | Lines of code from CLI Agent interactive mode                   |
| users\[].metrics.cli\_agent\_non\_interactive\_messages        | integer | Number of CLI Agent non-interactive messages                    |
| users\[].metrics.cli\_agent\_non\_interactive\_lines\_of\_code | integer | Lines of code from CLI Agent non-interactive mode               |
| pagination.next\_cursor                                        | string  | Cursor for fetching next page (empty if no more results)        |
| pagination.has\_more                                           | boolean | `true` if more results are available                            |
| metadata.effective\_start\_date                                | string  | Actual start date used (UTC, after defaults/clamping)           |
| metadata.effective\_end\_date                                  | string  | Actual end date used (UTC, after defaults/clamping)             |
| metadata.generated\_at                                         | string  | Response generation timestamp (ISO 8601)                        |
| metadata.total\_days                                           | integer | Total number of days in the queried date range                  |
| metadata.returned\_user\_count                                 | integer | Number of users returned in this page                           |

<Note>Each user has either `user_email` or `service_account_name`, never both.</Note>

***

## GET /analytics/v0/daily-user-activity-by-editor-language

Returns user activity metrics broken down by language and editor for a specific date. Supports pagination.

### Query Parameters

| Parameter  | Type    | Required | Description                                |
| ---------- | ------- | -------- | ------------------------------------------ |
| date       | string  | No       | Date to query in `YYYY-MM-DD` format (UTC) |
| cursor     | string  | No       | Pagination cursor from previous response   |
| page\_size | integer | No       | Number of results per page                 |

### Date Behavior

| Scenario          | Behavior                                                      |
| ----------------- | ------------------------------------------------------------- |
| Date not provided | Defaults to yesterday (UTC)                                   |
| Date provided     | Returns activity for that date (must be yesterday or earlier) |

### Pagination

| Parameter  | Default | Maximum |
| ---------- | ------- | ------- |
| page\_size | 50      | 100     |

To paginate through results:

1. Make initial request (optionally with `page_size`)
2. If `pagination.has_more` is `true`, use `pagination.next_cursor` as the `cursor` parameter
3. Repeat until `has_more` is `false`

### Constraints

| Constraint                  | Value                                                |
| --------------------------- | ---------------------------------------------------- |
| Maximum historical lookback | 2 years                                              |
| Today and future dates      | Not allowed (data available at \~02:00 UTC next day) |
| Timezone                    | All dates interpreted as UTC                         |

### Example Request (First Page)

```bash  theme={null}
curl -X GET "https://api.augmentcode.com/analytics/v0/daily-user-activity-by-editor-language?date=2025-10-15&page_size=50" \
  -H "Authorization: Bearer <your-api-token>"
```

### Example Response

```json  theme={null}
{
  "records": [
    {
      "user_email": "alice@example.com",
      "language": "Python",
      "editor": "VSCode",
      "metrics": {
        "total_modified_lines_of_code": 150,
        "total_messages": 25,
        "total_tool_calls": 40,
        "completions_count": 80,
        "completions_accepted": 65,
        "completions_lines_of_code": 120,
        "chat_messages": 10,
        "remote_agent_messages": 5,
        "remote_agent_lines_of_code": 15,
        "ide_agent_messages": 8,
        "ide_agent_lines_of_code": 12,
        "cli_agent_interactive_messages": 2,
        "cli_agent_interactive_lines_of_code": 3,
        "cli_agent_non_interactive_messages": 0,
        "cli_agent_non_interactive_lines_of_code": 0
      }
    },
    {
      "user_email": "alice@example.com",
      "language": "TypeScript",
      "editor": "VSCode",
      "metrics": {
        "total_modified_lines_of_code": 80,
        "total_messages": 12,
        "total_tool_calls": 18,
        "completions_count": 45,
        "completions_accepted": 38,
        "completions_lines_of_code": 60,
        "chat_messages": 5,
        "remote_agent_messages": 2,
        "remote_agent_lines_of_code": 8,
        "ide_agent_messages": 4,
        "ide_agent_lines_of_code": 10,
        "cli_agent_interactive_messages": 1,
        "cli_agent_interactive_lines_of_code": 2,
        "cli_agent_non_interactive_messages": 0,
        "cli_agent_non_interactive_lines_of_code": 0
      }
    }
  ],
  "pagination": {
    "next_cursor": "eyJsYXN0X2lkIjoidXNlcjMifQ==",
    "has_more": true
  },
  "metadata": {
    "effective_date": "2025-10-15",
    "generated_at": "2025-10-16T10:30:00Z",
    "returned_record_count": 2
  }
}
```

### Example Request (Next Page)

```bash  theme={null}
curl -X GET "https://api.augmentcode.com/analytics/v0/daily-user-activity-by-editor-language?date=2025-10-15&page_size=50&cursor=eyJsYXN0X2lkIjoidXNlcjMifQ==" \
  -H "Authorization: Bearer <your-api-token>"
```

### Response Fields

| Field                                                            | Type    | Description                                                     |
| ---------------------------------------------------------------- | ------- | --------------------------------------------------------------- |
| records                                                          | array   | Array of user/language/editor activity records                  |
| records\[].user\_email                                           | string  | User's email address (for regular users)                        |
| records\[].service\_account\_name                                | string  | Service account name (for service accounts)                     |
| records\[].language                                              | string  | Programming language (e.g., "Python", "TypeScript", "Unknown")  |
| records\[].editor                                                | string  | Editor/IDE name (e.g., "VSCode", "JetBrains", "CLI", "Unknown") |
| records\[].metrics                                               | object  | Usage metrics for this user/language/editor combination         |
| records\[].metrics.total\_modified\_lines\_of\_code              | integer | Total lines of code modified across all interactions            |
| records\[].metrics.total\_messages                               | integer | Total messages across all interaction types                     |
| records\[].metrics.total\_tool\_calls                            | integer | Total tool calls across all agent types                         |
| records\[].metrics.completions\_count                            | integer | Number of completion requests                                   |
| records\[].metrics.completions\_accepted                         | integer | Number of completions accepted                                  |
| records\[].metrics.completions\_lines\_of\_code                  | integer | Lines of code from completions                                  |
| records\[].metrics.completions\_suggested\_lines\_of\_code       | integer | Lines of code suggested by completions (before acceptance)      |
| records\[].metrics.chat\_messages                                | integer | Number of chat messages                                         |
| records\[].metrics.remote\_agent\_messages                       | integer | Number of Remote Agent messages                                 |
| records\[].metrics.remote\_agent\_lines\_of\_code                | integer | Lines of code from Remote Agent                                 |
| records\[].metrics.ide\_agent\_messages                          | integer | Number of IDE Agent messages                                    |
| records\[].metrics.ide\_agent\_lines\_of\_code                   | integer | Lines of code from IDE Agent                                    |
| records\[].metrics.cli\_agent\_interactive\_messages             | integer | Number of CLI Agent interactive messages                        |
| records\[].metrics.cli\_agent\_interactive\_lines\_of\_code      | integer | Lines of code from CLI Agent interactive mode                   |
| records\[].metrics.cli\_agent\_non\_interactive\_messages        | integer | Number of CLI Agent non-interactive messages                    |
| records\[].metrics.cli\_agent\_non\_interactive\_lines\_of\_code | integer | Lines of code from CLI Agent non-interactive mode               |
| pagination.next\_cursor                                          | string  | Cursor for fetching next page (empty if no more results)        |
| pagination.has\_more                                             | boolean | `true` if more results are available                            |
| metadata.effective\_date                                         | string  | Actual date used (UTC, after defaults)                          |
| metadata.generated\_at                                           | string  | Response generation timestamp (ISO 8601)                        |
| metadata.returned\_record\_count                                 | integer | Number of records returned in this page                         |

<Note>Each record has either `user_email` or `service_account_name`, never both. A single user may have multiple records if they used different language/editor combinations on the queried date.</Note>

***

## Rate Limiting

The Analytics API enforces rate limits to ensure fair usage and system stability.

| Limit Type          | Value              |
| ------------------- | ------------------ |
| Requests per minute | 10 requests/minute |
| Burst allowance     | 20 requests        |

When you exceed the rate limit, the API returns HTTP status code `429 Too Many Requests`. Your requests will be blocked for the duration specified above before you can make new requests.

### Best Practices

1. **Batch your requests**: Instead of making many small requests, use larger date ranges (up to 90 days) to retrieve more data per request.

2. **Implement exponential backoff**: If you receive a `429` response, wait before retrying. Start with a short delay and increase it with each consecutive failure.

3. **Cache responses**: Analytics data is updated only once daily, so cache responses and avoid re-fetching the same data within a 24-hour period.

4. **Use pagination efficiently**: When paginating through large result sets, process each page before requesting the next one rather than fetching all pages as fast as possible.

5. **Spread requests over time**: If you need to make multiple API calls, distribute them evenly rather than sending them all at once.

***

## Error Responses

The API returns standard HTTP status codes:

| Status Code | Description                                                        |
| ----------- | ------------------------------------------------------------------ |
| 400         | Invalid request (e.g., invalid date format, range exceeds 90 days) |
| 401         | Missing or invalid authentication token                            |
| 403         | Insufficient permissions                                           |
| 429         | Too many requests (rate limit exceeded)                            |
| 500         | Internal server error                                              |

### Example Error Response

```json  theme={null}
{
  "error": {
    "code": "InvalidArgument",
    "message": "end_date cannot be later than yesterday (UTC)"
  }
}
```
