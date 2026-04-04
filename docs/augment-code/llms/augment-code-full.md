# Augment Code Documentation

Source: https://docs.augmentcode.com/llms-full.txt

---

# Analytics API
Source: https://docs.augmentcode.com/analytics/analytics-api

Access usage metrics and analytics for your organization.

<Note>
  **Preview Feature**

  The Analytics API is currently in preview and is available exclusively to Enterprise customers.
</Note>

The Analytics API provides access to usage metrics for your organization, including how Augment Code is being used across your team. It allows you to build your own AI integration dashboards with tools like Jellyfish. Track daily active users, usage patterns, and detailed activity metrics to understand and optimize your team's use of Augment Code.

## Base URL

| Environment | URL                           |
| ----------- | ----------------------------- |
| Production  | `https://api.augmentcode.com` |

## Getting started

To use the Analytics API, you need to create a service account and generate an API token.

<Steps>
  <Step title="Create a Service Account">
    1. Navigate to your organization's **Service Accounts** page in the Augment web app: [app.augmentcode.com/settings/service-accounts](https://app.augmentcode.com/settings/service-accounts)
    2. Click **Add Service Account**
    3. Enter a **Service Name** (1-100 characters, alphanumeric, hyphens, and underscores only)
    4. Optionally add a **Description** for the service account
    5. Click **Create**

    <Note>Service account names must be unique within your organization.</Note>
  </Step>

  <Step title="Generate an API Token">
    1. In the **Service Accounts** list, find your newly created service account
    2. Click **Create Token**
    3. Enter a **Token Description** (e.g., "Analytics API integration")
    4. Click **Create**
    5. **Copy and securely store the token** — it will only be shown once

    <Warning>Treat API tokens like passwords. Do not share them or commit them to version control.</Warning>
  </Step>

  <Step title="Use the Token">
    Include the token in the `Authorization` header of your API requests:

    ```bash theme={null}
    curl -X GET "https://api.augmentcode.com/analytics/v0/dau-count" \
      -H "Authorization: Bearer <your-api-token>"
    ```

    For more details on service accounts, see the [Service Accounts documentation](/cli/automation/service-accounts).
  </Step>
</Steps>

## Available Endpoints

The Analytics API provides several endpoints to access different types of usage data:

<CardGroup>
  <Card title="Daily Active Users Count" icon="chart-line" href="/analytics/api-reference#get-analyticsv0dau-count">
    Get daily active user counts over a date range
  </Card>

  <Card title="Daily Active Users List" icon="users" href="/analytics/api-reference#get-analyticsv0dau">
    Get the list of active users for a specific date with pagination
  </Card>

  <Card title="Daily Usage Metrics" icon="chart-bar" href="/analytics/api-reference#get-analyticsv0daily-usage">
    Get aggregated usage metrics by day over a date range
  </Card>

  <Card title="User Activity" icon="user-chart" href="/analytics/api-reference#get-analyticsv0user-activity">
    Get per-user usage metrics over a date range with pagination
  </Card>

  <Card title="Activity by Editor & Language" icon="code" href="/analytics/api-reference#get-analyticsv0daily-user-activity-by-editor-language">
    Get user activity broken down by programming language and editor
  </Card>
</CardGroup>

## Important Considerations

<Note>
  **Timezone and Data Availability**

  All dates in requests and responses are interpreted and returned in **UTC timezone**. The most recent queryable date is "yesterday" (UTC), and data for the previous day becomes available at approximately **02:00 UTC** each day. Make sure to account for this when querying data or processing results.
</Note>

<Note>
  **Data Freshness**

  Analytics data is updated once daily. Data for a given day becomes available the following day at approximately 02:00 UTC.
</Note>

### Common Constraints

Most endpoints share these constraints:

| Constraint                  | Value                                                |
| --------------------------- | ---------------------------------------------------- |
| Maximum date range          | 90 days                                              |
| Maximum historical lookback | 2 years                                              |
| Today and future dates      | Not allowed (data available at \~02:00 UTC next day) |
| Timezone                    | All dates interpreted as UTC                         |

## Next Steps

<CardGroup>
  <Card title="API Reference" icon="book" href="/analytics/api-reference">
    View detailed API endpoint documentation
  </Card>

  <Card title="Service Accounts" icon="key" href="/cli/automation/service-accounts">
    Learn more about service accounts and authentication
  </Card>
</CardGroup>


# Analytics API Reference
Source: https://docs.augmentcode.com/analytics/api-reference

Detailed API endpoint documentation.

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

```bash theme={null}
curl -X GET "https://api.augmentcode.com/analytics/v0/dau-count?start_date=2025-10-15&end_date=2025-10-20" \
  -H "Authorization: Bearer <your-api-token>"
```

### Example Response

```json theme={null}
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

```bash theme={null}
curl -X GET "https://api.augmentcode.com/analytics/v0/dau?date=2025-10-15&page_size=50" \
  -H "Authorization: Bearer <your-api-token>"
```

### Example Response

```json theme={null}
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

```bash theme={null}
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

```bash theme={null}
curl -s -X GET "https://api.augmentcode.com/analytics/v0/daily-usage?start_date=2025-10-15&end_date=2025-10-20" \
  -H "Authorization: Bearer <your-api-token>" | jq .
```

### Example Response

```json theme={null}
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

```bash theme={null}
curl -s -X GET "https://api.augmentcode.com/analytics/v0/user-activity?start_date=2025-10-15&end_date=2025-10-20&page_size=3" \
  -H "Authorization: Bearer <your-api-token>" | jq .
```

### Example Response

```json theme={null}
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

```bash theme={null}
curl -X GET "https://api.augmentcode.com/analytics/v0/daily-user-activity-by-editor-language?date=2025-10-15&page_size=50" \
  -H "Authorization: Bearer <your-api-token>"
```

### Example Response

```json theme={null}
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

```bash theme={null}
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

```json theme={null}
{
  "error": {
    "code": "InvalidArgument",
    "message": "end_date cannot be later than yesterday (UTC)"
  }
}
```


# Overview of Analytics
Source: https://docs.augmentcode.com/analytics/overview

Monitor team usage patterns and analyze Augment Code adoption across your organization.

<Note>
  **Enterprise-Only Feature**

  Exclusive to Enterprise customers, access the Team Usage under Analytics at [app.augmentcode.com/dashboard](https://app.augmentcode.com/dashboard).
</Note>

## Feature Metrics at a Glance

<CardGroup>
  <Card title="Monthly Active Users" icon="users">
    Number of unique users in the current calendar month
  </Card>

  <Card title="Lines of Code All Sources" icon="code">
    Total lines of code generated from all sources during the selected period
  </Card>

  <Card title="User Messages & Tool Calls" icon="messages">
    Total number of user messages and tool calls during the selected period
  </Card>
</CardGroup>

## Understand adoption inside of your organization

Review detailed per-user metrics to understand power-user usage patterns or inactivity inside your organization.

### Available Columns

| Column                                 | Description                                                                |
| -------------------------------------- | -------------------------------------------------------------------------- |
| **User**                               | Email or service account name (with visual indicator for service accounts) |
| **First Seen**                         | Date user first appeared in the system                                     |
| **Last Seen**                          | Date of user's most recent activity                                        |
| **Active Days**                        | Number of days user was active in the selected period                      |
| **Completions**                        | Total code completions generated                                           |
| **Accepted Completions**               | Number of completions accepted by user                                     |
| **Accept Rate**                        | Percentage of completions accepted                                         |
| **Chat Messages**                      | Total chat messages sent                                                   |
| **Agent Messages**                     | Messages from agent interactions                                           |
| **Remote Agent Messages**              | Messages from remote agent sessions                                        |
| **Interactive CLI Agent Messages**     | Interactive CLI agent interactions                                         |
| **Non-Interactive CLI Agent Messages** | Non-interactive CLI agent interactions                                     |
| **Tool Uses**                          | Total number of tool invocations                                           |
| **Total Modified Lines of Code**       | All lines of code modified                                                 |
| **Completion Lines of Code**           | Lines from completions                                                     |
| **Instruction Lines of Code**          | Lines from instructions                                                    |
| **Agent Lines of Code**                | Lines from agent edits                                                     |
| **Remote Agent Lines of Code**         | Lines from remote agent                                                    |
| **CLI Agent Lines of Code**            | Lines from CLI agent                                                       |

## Data Export

Export your usage data for custom analysis, reporting, or integration with other tools:

* **CSV Download** - Export all user statistics to a CSV file
* **Filename Format** - `user-feature-stats-YYYY-MM-DD-to-YYYY-MM-DD.csv`
* **Complete Data** - Includes all columns from the user statistics table

## Mobile Experience

The dashboard is fully optimized for mobile devices with:

* Card-based layout for easy viewing on smaller screens
* Mobile sort selector dropdown for choosing sort column and direction
* Responsive pagination controls adapted for touch interfaces
* All key metrics and data accessible on any device

## Getting Help

If you have questions about the Enterprise Dashboard or need assistance interpreting your usage data:

<CardGroup>
  <Card title="Contact Sales" icon="briefcase">
    Reach out to your sales representative for strategic guidance
  </Card>

  <Card title="Contact Support" icon="life-ring" href="https://support.augmentcode.com">
    Get technical support at support.augmentcode.com
  </Card>
</CardGroup>

## Related Resources

<CardGroup>
  <Card title="Analytics API" icon="code" href="/analytics/analytics-api">
    Programmatic access to usage metrics via REST API
  </Card>

  <Card title="API Reference" icon="book" href="/analytics/api-reference">
    Detailed API endpoint documentation
  </Card>
</CardGroup>


# ACP Mode
Source: https://docs.augmentcode.com/cli/acp/agent

Auggie is a fully compatible Agent Client Protocol (ACP) agent enabling you to bring the power of Augment to any compatible client.

## About ACP Mode

[Agent Client Protocol](https://agentclientprotocol.com/overview/introduction) (ACP) is an open protocol that provides a standardized way to connect AI agents to different text editors, IDEs, and other tools. ACP mode uses JSON-RPC over standard input and output to communicate between the agent and the client. You can see a [overview of the protocol](https://agentclientprotocol.com/protocol/overview) to learn more.

## Using ACP Mode

To use Auggie in ACP mode, you need to pass the `--acp` flag when starting Auggie. You can pass additional [command-line arguments](/cli/reference) to set the model, authentication, and other options.

```sh theme={null}
auggie --acp
```

To use Auggie in a ACP-compatible client, you need to configure the client to launch Auggie with the `--acp` flag and follow the client-specific instructions. See the [ACP Clients](/cli/acp/clients) page for more details.

## Compatibility

ACP is an emerging protocol and is in active development. Not all features available in interactive mode are supported in ACP mode. We are looking forward to working with the community to add support for more features in the future.


# ACP Clients
Source: https://docs.augmentcode.com/cli/acp/clients

Configure Auggie to run in any Agent Client Protocol (ACP) compatible client like Zed, Neovim, or Emacs.

## About ACP Clients

[Agent Client Protocol](https://agentclientprotocol.com/overview/introduction) (ACP) is an open protocol that provides a standardized way to connect AI agents to different text editors, IDEs, and other tools. Auggie is a fully ACP compatible agent enabling you to bring the power of Augment to editors like Zed, Neovim, or Emacs. See a [full list of supported clients](https://agentclientprotocol.com/overview/clients) in the ACP docs.

## Prerequisites

* Auggie CLI [installed and configured](/cli/setup-auggie/install-auggie-cli)
* Login to Augment with `auggie login`
* A compatible ACP client

## Client configuration

If you have an ACP client that you would like to have listed here, please [open an issue](https://github.com/augmentcode/auggie/issues/new) and we'll be happy to add it.

### Zed

<Note>
  We recommend installing and configuring Auggie in [Zed](https://zed.dev/) using the [Auggie extension](https://zed.dev/extensions/auggie).
</Note>

If you want to configure Auggie manually through Zed's settings, you can use the following configuration. You can pass additional [command-line arguments](/cli/reference) to Auggie by adding them to the `args` array or use alternative [authentication methods](/cli/setup-auggie/authentication) by passing environment variables in the `env` object.

```
{
  "agent_servers": {
    "Auggie CLI": {
      "command": "auggie",
      "args": ["--acp"],
      "env": {}
    }
  }
}
```

### JetBrains

<Note>
  We recommend installing and configuring Augment in [JetBrains IDEs](/jetbrains/setup-augment/install-jetbrains-ides) using the [Augment extension](https://plugins.jetbrains.com/plugin/24072-augment-ai-coding-assistant-for-professionals).
</Note>

To use Auggie with JetBrains IDEs, you can configure it in your IDE settings. You can pass additional [command-line arguments](/cli/reference) to Auggie by adding them to the `args` array or use alternative [authentication methods](/cli/setup-auggie/authentication) by passing environment variables in the `env` object.

```json theme={null}
{
  "agent_servers": {
    "Auggie CLI": {
      "command": "auggie",
      "args": [
        "--acp"
      ],
      "env": {}
    }
  }
}
```

### Neovim

To use Auggie with Neovim, you can use one of the following plugins:

#### [**Avante.nvim**](https://github.com/yetone/avante.nvim)

Add the following to your lazy.nvim configuration:

```lua theme={null}
  {
    "yetone/avante.nvim",
    event = "VeryLazy",
    build = "make",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
    },
    opts = {
      provider = "auggie-acp",
      acp_providers = {
        ["auggie-acp"] = {
          command = "auggie",
          args = { "--acp" },
        },
      },
      behaviour = {
        auto_suggestions = false,
        auto_set_highlight_group = true,
        auto_set_keymaps = true,
        auto_apply_diff_after_generation = false,
        support_paste_from_clipboard = false,
      },
    },
  },

```

#### [**Agentic.nvim**](https://github.com/carlos-algms/agentic.nvim)

Add the following to your lazy.nvim configuration:

```lua theme={null}
{
  "carlos-algms/agentic.nvim",
  opts = {
    provider = "auggie-acp",
    acp_providers = {
      ["auggie-acp"] = {
        command = "auggie",
        args = { "--acp" },
      },
    },
  },
}
```

#### [**CodeCompanion.nvim**](https://github.com/olimorris/codecompanion.nvim)

Add the following to your lazy.nvim configuration:

```lua theme={null}
{
  "olimorris/codecompanion.nvim",
  opts = {
    strategies = {
      chat = {
        adapter = "auggie_cli",
      },
      inline = {
        adapter = "auggie_cli",
      },
    },
  },
}
```

### Emacs

To use Auggie with emacs, you can use one of the following plugins:

* [agent-shell.el](https://github.com/xenodium/agent-shell)


# Using Auggie with Automation
Source: https://docs.augmentcode.com/cli/automation/overview

Auggie was designed to not just be a powerful agent to write code, but to automate all the tasks that are needed to build software at scale.

## About automation

Auggie was purpose built to integrate into your software development stack. From using Auggie in your local development workflows to automatically running Auggie in your CI/CD pipelines, Auggie can help you build better software faster.

### Example use cases

* **Code reviews**: Review code changes and provide feedback.
* **Issue triage**: Triage incoming issues and route them to the appropriate team or individual.
* **Automate on-call**: Respond to incoming alerts and create an assessment plan.
* **Exception management**: Analyze incoming exceptions and create tickets.

## Integrating with your workflows

In order to use Auggie in your systems, like a CI/CD pipeline, you'll need to install Auggie CLI, provide a session token, and write an instruction that will be used alongside any data from your system you want to include.

### Installation

Auggie can be [installed](/cli/setup-auggie/install-auggie-cli) directly from npm anywhere you can run Node 22 or later including VMs, serverless functions, and containers. You will also need to install any dependencies for defined MCP servers in those environments.

```sh theme={null}
npm install -g @augmentcode/auggie
```

### Authentication

Session tokens are associated with the user that created it, and Auggie will run with integration configurations from that user. See [Authentication](/cli/setup-auggie/authentication) for full details. You can override the user's GitHub configuration by passing `--github-api-token <token>`.

```sh theme={null}
# First, login to Augment with the CLI
auggie login

# Next, output your token
auggie tokens print

# Then, pass your token to auggie
AUGMENT_SESSION_AUTH='<token>' auggie --print "Summarize the build failure"
```

### Scripts and pipes

Auggie runs as a subprocess, so it can be used in any shell script. It can be used just like any command-line tool that follows the Unix philosophy. You can pipe data into Auggie and then pipe the response to another command. Data passed into Auggie through stdin will be used as context in addition to the instruction.

```sh theme={null}
# Pipe data through stdin
cat build.log | auggie --print "Summarize the failure and open a Linear ticket"

# Provide input from a file
auggie --compact --instruction /path/to/instruction.md < build.log
```

## GitHub Actions

GitHub Actions makes it easy to connect Auggie to other parts of your software development pipeline, from linting, testing, build, and deploy. We've built a [simple wrapper for Auggie](https://github.com/augmentcode/augment-agent) that enables you to  integrate with GitHub Action workflows and build custom tooling around Auggie.

Follow the instructions to [configure Augment Agent](https://github.com/augmentcode/augment-agent/blob/main/README.md) in GitHub Actions and explore the [example-workflows](https://github.com/augmentcode/augment-agent/tree/main/example-workflows) directory to get started.

### Ready to use workflows

Get started using Auggie in GitHub Actions immediately by following the instructions for setup and deploy in one of the following workflows, or use the `/github-workflow` wizard in Auggie to have the workflows generated for you.

* [PR Description](https://github.com/augmentcode/describe-pr): This action automatically analyzes your PR changes and generates comprehensive, informative descriptions.
* [PR Review](https://github.com/augmentcode/review-pr): This action automatically analyzes your PR changes and generates comprehensive, informative reviews

Need even more help building GitHub Actions? May we suggest asking Auggie.

```sh theme={null}
auggie "Help me build a GitHub Action to..."
```


# Service Accounts
Source: https://docs.augmentcode.com/cli/automation/service-accounts



## About

Service Accounts provide non-human identities for automation use cases to make API requests to the Augment backend through Auggie CLI. They decouple automation tasks from using individual user accounts and enable per-automation task token lifecycle management.

## Managing Service Accounts

Service Accounts can be managed by navigating to [app.augmentcode.com/settings/service-accounts](https://app.augmentcode.com/settings/service-accounts) and logging in. Service accounts are only available to [Enterprise plan](https://augmentcode.com/pricing) customers. Service accounts can only be managed by the Administrator of the Enterprise Plan.

### Creating a Service Account

To create a new service account, click the "New Service Account" button. You will be prompted to enter a name and an optional description for the service account. The account name must be unique within your organization.

### Creating API tokens

Once you've created a service account, you can create API tokens for it by clicking the "Add API token" button next to the service account name in the list of service accounts. You will be prompted to enter a name for the API token which must be unique amongst the tokens for this service account. Once you've created a token, you will be given a one time opportunity to retrieve the token value by either:

* Copying the token value directly or using the "Copy token" button **OR**
* Downloading a `session.json` file that is ready to use with Auggie CLI.

API tokens for service accounts don't have an expiration date and need to be manually revoked if they are no longer needed.

### Deleting Service Accounts and API tokens

API tokens can be revoked by selecting "Revoke" from the triple dot menu next to the token name in the service account list. Note that revoking a token is a permanent action and cannot be undone. Any existing Auggie CLI automation sessions using the token will be disrupted.

Service accounts can be deleted by clicking "Manage" next to the service account name in the service account list, and then clicking "Delete Account" from the dialog that appears. Note that deleting a service account will also delete all the associated API tokens.

## Using API tokens with Auggie CLI

In order to use a service account API token with Auggie CLI, you need to edit the `session.json` file stored under `~/.augment`. If you've downloaded a `session.json` file after creating the API token, you can simply replace the existing `session.json` file with the new one. If you've only copied the token value, you need to edit the `session.json` file with the following content and replace the `accessToken` value with the new token value.

```
{
  "accessToken": "<TOKEN VALUE>",
  "tenantURL": "<TENANT URL>",
  "scopes": [
    "read",
    "write"
  ]
}
```

The correct `tenantURL` value for your organization is displayed on top of the service account list in the management UI.

## Best Practices

* Use a separate service account per automation task. This will allow you to manage token lifecycle and monitor credit usage per automation task.
* Use the ability to create multiple tokens under a service account to rotate tokens when needed. Create a new API token, update the automation tasks to use the new token, and revoke the old token once all automation tasks have been updated.


# Automatic Updates
Source: https://docs.augmentcode.com/cli/autoupgrade

Learn how to manage and troubleshoot Auggie CLI's automatic update feature.

## How Automatic Updates Work

Auggie CLI automatically updates itself when running in interactive mode to ensure you always have the latest features and bug fixes.

### Interactive Mode (TUI)

* Automatically checks npm for newer versions when you start Auggie
* Performs upgrades without prompting to minimize interruption
* Shows a brief notification when an update is applied
* Best-effort approach - continues running even if update fails

### Non-interactive Mode (Print/Text Mode)

* Auto-update is completely disabled
* Respects version pinning in automation scripts

## Disabling Automatic Updates

Set the `AUGMENT_DISABLE_AUTO_UPDATE` environment variable to `1` to disable automatic updates.

### Environment Variable (Recommended for Scripts)

```bash theme={null}
# Disable for current session
export AUGMENT_DISABLE_AUTO_UPDATE=1

# Disable for single command
AUGMENT_DISABLE_AUTO_UPDATE=1 auggie --print "Your instruction here"
```

## Manual Updates

You can manually update Auggie CLI by running the following command.

```bash theme={null}
auggie upgrade
```


# Custom Slash Commands
Source: https://docs.augmentcode.com/cli/custom-commands

Create and manage custom slash commands for frequently-used prompts and workflows.

## About Custom Slash Commands

Custom slash commands let you create reusable prompts stored as Markdown files that Auggie can run. You can organize commands by scope (workspace or user) and use directory structures for namespacing.

### Syntax

```
/<command-name> [arguments]
```

### Parameters

| Parameter        | Description                              |
| :--------------- | :--------------------------------------- |
| `<command-name>` | Name derived from the Markdown filename  |
| `[arguments]`    | Optional arguments passed to the command |

## Command Types and Locations

Custom commands are stored in markdown files and can be placed in multiple locations with a specific order of precedence:

### Command Locations (in order of precedence)

1. **User Commands**: `~/.augment/commands/<name>.md` (user)
2. **Workspace Commands**: `./.augment/commands/<name>.md` (workspace)
3. **Claude Code Commands**: `./.claude/commands/<name>.md` (.claude)

### User Commands

Commands available across all your projects. These are user-wide and persist across different workspaces.

**Location**: `~/.augment/commands/`

```sh theme={null}
# Create a global command
mkdir -p ~/.augment/commands
echo "Review this code for security vulnerabilities:" > ~/.augment/commands/security-review.md
```

### Workspace Commands

Commands stored in your repository and shared with your team. These are workspace-specific and can be committed to version control.

**Location**: `./.augment/commands/`

```sh theme={null}
# Create a workspace command
mkdir -p .augment/commands
echo "Analyze this code for performance issues and suggest optimizations:" > .augment/commands/optimize.md
```

### Claude Code Compatibility

Auggie automatically detects and supports commands from `./.claude/commands/` for compatibility with existing Claude Code setups. This allows teams already using Claude Code to continue using their existing command libraries without modification.

**Location**: `./.claude/commands/` and `~/.claude/commands/`

**Migration**: While `./.claude/commands/` is supported for compatibility, we recommend migrating to `./.augment/commands/` for new projects to maintain consistency with Auggie's naming conventions.

## Features

### Namespacing

Organize commands in subdirectories. Commands from nested directories can be accessed using the `namespace:command` syntax, where the namespace corresponds to the subdirectory name.

For example, a file at `.augment/commands/frontend/component.md` creates the command `/frontend:component`.

Conflicts between user and workspace level commands are not supported and will be defined in order of precedence above.

### Arguments

Pass dynamic values to commands.

```markdown theme={null}
# Command definition
echo 'Fix issue following our coding standards' > .augment/commands/fix-issue.md

# Usage
> /fix-issue 123
```

### Frontmatter

Command files support frontmatter for metadata:

| Frontmatter     | Purpose                                                                    | Default                             |
| :-------------- | :------------------------------------------------------------------------- | :---------------------------------- |
| `description`   | Brief description of the command                                           | Uses the first line from the prompt |
| `argument-hint` | Expected arguments format that will be displayed after typing in a command | None                                |
| `model`         | Specify the model to run this command with (overrides the CLI default)     | Uses the CLI default model          |

**File**: `~/.augment/commands/deploy-staging.md`

```markdown theme={null}
---
description: Deploy the application to staging with health checks
argument-hint: [branch-name]
model: gpt-4o
---

Deploy the application to the staging environment:

1. Run all tests to ensure code quality
2. Build the application for production
3. Deploy to staging server
4. Run health checks to verify deployment
5. Send notification to team channel
```

## Command Line Execution

We also provide the ability to execute custom commands from the command line using the `auggie command <your_command>` or list them with `auggie command list`. For complete command-line reference, see [CLI Reference for Custom Commands](/cli/reference#custom-commands).

```sh theme={null}
# Execute a custom command
auggie command deploy-staging

# List all available commands (including custom ones)
auggie command list
```

Custom commands appear in the help output with their descriptions:

```
Available custom commands:
  auggie command deploy-staging    # Deploy the application to staging
  auggie command security-review   # Review code for security vulnerabilities
```

## Example Commands

For ready-to-use examples of custom slash commands, including code review templates, bug fix guides, and feature implementation plans, see:

**[Custom Commands Examples](/cli/custom-commands-examples)**

## Best Practices

1. **Use kebab-case naming** for command names (e.g., `deploy-staging`, `run-tests`)
2. **Keep names descriptive** but concise, avoiding spaces and special characters
3. **Use meaningful prefixes** for related commands (e.g., `deploy-staging`, `deploy-production`)
4. **Include clear descriptions** in frontmatter for better discoverability
5. **Break complex workflows** into numbered steps for clarity
6. **Use user commands** (`~/.augment/commands/`) for personal workflows across all projects
7. **Use workspace commands** (`./.augment/commands/`) for team-shared, project-specific tasks
8. **Organize with subdirectories** for related command groups using namespacing
9. **Document command purpose** and expected outcomes clearly
10. **Version your commands** when making significant changes

## See Also

* [Custom Commands Examples](/cli/custom-commands-examples) - Ready-to-use command templates and examples
* [Interactive Mode Slash Commands](/cli/interactive#slash-commands) - Learn about Auggie's interactive terminal features
* [CLI Reference for Custom Commands](/cli/reference#custom-commands) - Complete reference for command-line flags


# Custom Slash Commands Examples
Source: https://docs.augmentcode.com/cli/custom-commands-examples

Ready-to-use examples of custom slash commands for common development workflows.

## Example Commands

Here are some practical examples of custom slash commands you can use in your projects:

<AccordionGroup>
  <Accordion title="Code Review Command">
    ```markdown theme={null}
    ---
    description: Perform a comprehensive code review
    argument-hint: [file-path]
    ---

    Please perform a comprehensive code review of the specified file or current changes, focusing on:

    1. **Code Quality**: Check for readability, maintainability, and adherence to best practices
    2. **Security**: Look for potential security vulnerabilities
    3. **Performance**: Identify potential performance issues
    4. **Testing**: Suggest areas that need test coverage
    5. **Documentation**: Check if code is properly documented

    $ARGUMENTS
    ```
  </Accordion>

  <Accordion title="Bug Fix Template">
    ```markdown theme={null}
    ---
    description: Generate a structured bug fix approach
    argument-hint: [bug-description]
    ---

    Help me fix this bug: $ARGUMENTS

    Please provide:
    1. Root cause analysis
    2. Step-by-step fix approach
    3. Testing strategy
    4. Prevention measures for similar issues
    ```
  </Accordion>

  <Accordion title="Feature Implementation Guide">
    ```markdown theme={null}
    ---
    description: Create implementation plan for new features
    argument-hint: [feature-description]
    ---

    Create a detailed implementation plan for: $ARGUMENTS

    Include:
    - Technical requirements
    - Architecture considerations
    - Implementation steps
    - Testing approach
    - Documentation needs
    ```
  </Accordion>

  <Accordion title="Security Review Command">
    ```markdown theme={null}
    ---
    description: Perform security analysis on code
    argument-hint: [file-path]
    ---

    Perform a security review of: $ARGUMENTS

    Focus on:
    1. **Input validation** and sanitization
    2. **Authentication** and authorization checks
    3. **Data exposure** and privacy concerns
    4. **Injection vulnerabilities** (SQL, XSS, etc.)
    5. **Cryptographic** implementations
    6. **Dependencies** with known vulnerabilities

    Provide specific recommendations for any issues found.
    ```
  </Accordion>

  <Accordion title="Performance Optimization">
    ```markdown theme={null}
    ---
    description: Analyze and optimize code performance
    argument-hint: [file-path]
    ---

    Analyze the performance of: $ARGUMENTS

    Please examine:
    1. **Algorithm complexity** and efficiency
    2. **Memory usage** patterns
    3. **Database queries** and optimization opportunities
    4. **Caching** strategies
    5. **Network requests** and bundling
    6. **Rendering performance** (for frontend code)

    Suggest specific optimizations with expected impact.
    ```
  </Accordion>

  <Accordion title="Documentation Generator">
    ```markdown theme={null}
    ---
    description: Generate comprehensive documentation
    argument-hint: [file-path]
    ---

    Generate documentation for: $ARGUMENTS

    Include:
    1. **Overview** and purpose
    2. **API reference** with parameters and return values
    3. **Usage examples** with code snippets
    4. **Configuration options** if applicable
    5. **Error handling** and troubleshooting
    6. **Dependencies** and requirements

    Format as clear, structured markdown.
    ```
  </Accordion>

  <Accordion title="Test Generation Command">
    ```markdown theme={null}
    ---
    description: Generate comprehensive test cases
    argument-hint: [file-path]
    ---

    Generate test cases for: $ARGUMENTS

    Create tests covering:
    1. **Happy path** scenarios
    2. **Edge cases** and boundary conditions
    3. **Error handling** and exceptions
    4. **Integration points** with other components
    5. **Performance** considerations
    6. **Security** edge cases

    Use appropriate testing framework conventions and include setup/teardown as needed.
    ```
  </Accordion>
</AccordionGroup>

## How to Add Commands to Your Project

To use these custom slash commands in your project, you need to save them in the `.augment/commands/` directory:

### Step 1: Create the Commands Directory

First, create the `.augment/commands/` directory in your project root if it doesn't exist:

```bash theme={null}
mkdir -p .augment/commands
```

### Step 2: Save Command Files

Save each command as a separate `.md` file in the `.augment/commands/` directory. For example:

```bash theme={null}
# Save the code review command
cat > .augment/commands/code-review.md << 'EOF'
---
description: Perform a comprehensive code review
argument-hint: [file-path]
---

Please perform a comprehensive code review of the specified file or current changes, focusing on:

1. **Code Quality**: Check for readability, maintainability, and adherence to best practices
2. **Security**: Look for potential security vulnerabilities
3. **Performance**: Identify potential performance issues
4. **Testing**: Suggest areas that need test coverage
5. **Documentation**: Check if code is properly documented

$ARGUMENTS
EOF
```

### Step 3: Use Your Commands

Once saved, your custom commands become available as slash commands in Augment:

```
/code-review src/components/Button.tsx
/bug-fix "Login form validation not working"
/security-review auth/middleware.js
```

### Directory Structure

Your project structure should look like this:

```
your-project/
├── .augment/
│   └── commands/
│       ├── code-review.md
│       ├── bug-fix.md
│       ├── security-review.md
│       └── performance-optimization.md
├── src/
└── package.json
```

## Usage Tips

* **Save these templates** in your `.augment/commands/` directory
* **Customize the prompts** to match your team's coding standards and practices
* **Add project-specific context** to make the commands more effective
* **Combine commands** by referencing outputs from one command in another
* **Use meaningful filenames** like `code-review.md`, `bug-fix.md`, etc.
* **Version control your commands** by committing the `.augment/commands/` directory to your repository

## Creating Your Own Examples

When creating custom commands, consider these patterns:

1. **Start with a clear description** in the frontmatter
2. **Use argument hints** to guide users on expected inputs
3. **Structure your prompts** with numbered lists or bullet points
4. **Include specific instructions** for the type of analysis or output you want
5. **Reference the `$ARGUMENTS` variable** where user input should be inserted

## See Also

* [Custom Slash Commands](/cli/custom-commands) - Learn how to create and manage custom commands
* [CLI Reference for Custom Commands](/cli/reference#custom-commands) - Complete command-line reference for custom commands


# Hooks
Source: https://docs.augmentcode.com/cli/hooks

Intercept and control tool execution with custom scripts

## Overview

Hooks allow you to intercept tool execution at specific lifecycle events and run custom scripts. This enables powerful workflows like:

* **Security auditing** - Block dangerous commands or log sensitive file access
* **Policy enforcement** - Enforce coding standards or restrict production access
* **Logging** - Track tool usage for compliance and analytics
* **Integration** - Connect with external systems and workflows

Hooks execute automatically when specific events occur during agent operation, giving you fine-grained control over tool execution and session lifecycle.

## Configuration

Hooks are configured in `settings.json` files:

### Settings File Locations

| Location                               | Platform    | Supported By          | Description                                        |
| :------------------------------------- | :---------- | :-------------------- | :------------------------------------------------- |
| `/etc/augment/settings.json`           | Linux/macOS | CLI, VSCode, IntelliJ | System-wide settings for enterprise/admin policies |
| `C:\ProgramData\Augment\settings.json` | Windows     | CLI, VSCode, IntelliJ | System-wide settings for enterprise/admin policies |
| `~/.augment/settings.json`             | All         | CLI, VSCode, IntelliJ | User-level settings                                |

<Note>
  System-level settings (`/etc/augment/settings.json`) take precedence and cannot be overridden by
  user settings.
</Note>

<Warning>
  `PreToolUse`, `PostToolUse`, and `Stop` hooks run **synchronously** - the agent waits for them to
  complete before proceeding. Use appropriate timeouts to prevent long delays. Note that only
  `PreToolUse` can block tool execution; `Stop` can block the agent from finishing (via `decision:
      "block"`), but `PostToolUse` cannot block anything.
</Warning>

### Structure

Hooks are organized by event type with optional matchers:

```json theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "launch-process",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/validate-command.sh",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

**Configuration fields:**

| Field      | Description                                                                                                                                                                                                                     |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `matcher`  | Pattern to match tool names (case-sensitive). Supports regex patterns. Optional for `PreToolUse` and `PostToolUse` (defaults to `".*"` to match all tools). Not used for session events (`SessionStart`, `SessionEnd`, `Stop`). |
| `hooks`    | Array of hook handlers to execute when the pattern matches.                                                                                                                                                                     |
| `type`     | Hook execution type - currently only `"command"` is supported.                                                                                                                                                                  |
| `command`  | Path to the shell script to execute (must be a `.sh` file).                                                                                                                                                                     |
| `timeout`  | *(Optional)* Timeout in milliseconds (default: 60000ms).                                                                                                                                                                        |
| `metadata` | *(Optional)* Configuration for additional context fields - see [Hook Metadata](#hook-metadata-configuration).                                                                                                                   |

**Matcher pattern examples:**

| Pattern                           | Description                               |
| :-------------------------------- | :---------------------------------------- |
| `"launch-process"`                | Match a specific tool                     |
| `"str-replace-editor\|save-file"` | Match multiple tools using regex OR       |
| `".*"`                            | Match all tools                           |
| `"mcp:*"`                         | Match all MCP tools (special case)        |
| `"mcp:.*_my-server$"`             | Match any tool from a specific MCP server |

For session events (`SessionStart`, `SessionEnd`, `Stop`) that don't require matchers:

```json theme={null}
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/setup-script.sh"
          }
        ]
      }
    ]
  }
}
```

### Script Requirements

Hook scripts must:

1. **Use `.sh` file extension** - Only shell scripts are supported
2. **Be executable** - Run `chmod +x your-hook.sh`
3. **Have a valid shebang** - First line must specify the interpreter

<Tip>
  You can use any interpreter (Python, Node.js, Ruby, etc.) by specifying it in the shebang line.
  The file extension must still be `.sh`.
</Tip>

```bash theme={null}
#!/usr/bin/env python3
# Python script with .sh extension - uses Python interpreter via shebang
import sys, json
event_data = json.load(sys.stdin)
# ... your Python code
```

## Hook Events

### PreToolUse

Runs **before** a tool executes. Can block tool execution.

**Common tool names:**

| Tool                 | Description        |
| :------------------- | :----------------- |
| `launch-process`     | Shell commands     |
| `view`               | File reading       |
| `str-replace-editor` | File editing       |
| `save-file`          | File writing       |
| `remove-files`       | File deletion      |
| `web-fetch`          | Fetch web content  |
| `web-search`         | Web search         |
| `codebase-retrieval` | Codebase search    |
| `github-api`         | GitHub integration |
| `linear`             | Linear integration |

Use [PreToolUse output control](#pretooluse-output) to block tools or modify inputs.

### PostToolUse

Runs immediately **after** a tool completes. Can provide feedback to the agent but cannot block execution.

Recognizes the same tool names as PreToolUse. Includes `tool_output` and `tool_error` in the event data.

### Stop

Runs when the agent finishes responding. Can block the agent from stopping (useful for requiring tests before completion).

<Note>Does not run if stopped by user interrupt.</Note>

### SessionStart

Runs when Auggie starts a new session. Useful for:

* Loading development context (git status, open issues)
* Installing dependencies
* Setting up environment variables

### SessionEnd

Runs when an Auggie session ends. Useful for:

* Cleanup tasks
* Logging session statistics
* Saving session state

## Hook Input

Hooks receive event data via **stdin** as a JSON object. The structure varies by event type, but all events share common base fields.

### Common Fields (All Events)

These fields are present in **every** hook event:

| Field             | Type      | Description                                                                                    |
| :---------------- | :-------- | :--------------------------------------------------------------------------------------------- |
| `hook_event_name` | string    | The type of event: `"PreToolUse"`, `"PostToolUse"`, `"Stop"`, `"SessionStart"`, `"SessionEnd"` |
| `conversation_id` | string    | Unique identifier for the current conversation                                                 |
| `workspace_roots` | string\[] | List of workspace root directories (usually contains one path)                                 |

### Event-Specific Fields

#### PreToolUse / PostToolUse Events

Tool events include information about the tool being executed:

| Field          | Type       | Availability     | Description                                                                                                                     |
| :------------- | :--------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `tool_name`    | string     | Always           | Name of the tool (e.g., `"launch-process"`, `"str-replace-editor"`). Use to filter which tools your hook applies to.            |
| `tool_input`   | object     | Always           | Input parameters passed to the tool. **Critical for security hooks** - extract and validate specific parameters.                |
| `tool_output`  | string?    | PostToolUse only | Output returned by the tool (if successful). Use for auditing or providing context to the agent.                                |
| `tool_error`   | string?    | PostToolUse only | Error message if tool execution failed. Use to detect failures and inject troubleshooting tips.                                 |
| `file_changes` | object\[]? | PostToolUse only | File changes for `save-file`, `str-replace-editor`, `remove-files`. Includes `path`, `changeType`, `content`, and `oldContent`. |

**Example: Extracting tool-specific parameters**

<CodeGroup>
  ```bash Bash - Extract Bash command theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name')

  if [[ "$TOOL_NAME" == "launch-process" ]]; then
    # Extract the command being executed
    COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command')
    echo "Command: $COMMAND" >&2

    # Check for dangerous patterns
    if echo "$COMMAND" | grep -qE "rm -rf|sudo|curl.*sh"; then
      echo "Blocked dangerous command" >&2
      exit 2
    fi
  fi

  exit 0
  ```

  ```python Python - Extract file path theme={null}
  #!/usr/bin/env python3
  import sys, json

  event_data = json.load(sys.stdin)
  if event_data.get('tool_name') == 'str-replace-editor':
      path = event_data.get('tool_input', {}).get('path', '')
      if any(p in path for p in ['.env', 'secrets', 'credentials']):
          print(f"[AUDIT] Sensitive file: {path}", file=sys.stderr)

  sys.exit(0)
  ```
</CodeGroup>

**Example: Using `tool_output` for context (PostToolUse)**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name')
  TOOL_OUTPUT=$(echo "$EVENT_DATA" | jq -r '.tool_output // ""')

  if [[ "$TOOL_NAME" == "launch-process" ]] && echo "$TOOL_OUTPUT" | grep -q "test.*passed"; then
    # Tests passed - inject success context
    cat << EOF
  {
    "hookSpecificOutput": {
      "hookEventName": "PostToolUse",
      "additionalContext": "All tests passed successfully!"
    }
  }
  EOF
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json

  event_data = json.load(sys.stdin)
  tool_name = event_data.get('tool_name', '')
  tool_output = event_data.get('tool_output', '')

  if tool_name == 'launch-process' and 'test' in tool_output and 'passed' in tool_output:
      # Tests passed - inject success context
      output = {
          "hookSpecificOutput": {
              "hookEventName": "PostToolUse",
              "additionalContext": "All tests passed successfully!"
          }
      }
      print(json.dumps(output))

  sys.exit(0)
  ```
</CodeGroup>

**Example: Using `tool_error` for troubleshooting (PostToolUse)**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  TOOL_ERROR=$(echo "$EVENT_DATA" | jq -r '.tool_error // ""')

  if [[ -n "$TOOL_ERROR" ]] && echo "$TOOL_ERROR" | grep -q "permission denied"; then
    # Inject troubleshooting tip
    cat << EOF
  {
    "hookSpecificOutput": {
      "hookEventName": "PostToolUse",
      "additionalContext": "Permission denied error detected. Try running with appropriate permissions or check file ownership."
    }
  }
  EOF
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json

  event_data = json.load(sys.stdin)
  tool_error = event_data.get('tool_error', '')

  if tool_error and 'permission denied' in tool_error.lower():
      output = {
          "hookSpecificOutput": {
              "hookEventName": "PostToolUse",
              "additionalContext": "Permission denied error detected. Try with appropriate permissions."
          }
      }
      print(json.dumps(output))

  sys.exit(0)
  ```
</CodeGroup>

**Example: Using `file_changes` for audit logging (PostToolUse)**

The `file_changes` field is populated for file-modifying tools and includes the old content for edits:

```json theme={null}
{
  "hook_event_name": "PostToolUse",
  "conversation_id": "conv-xyz789",
  "tool_name": "str-replace-editor",
  "tool_input": {
    "path": "src/auth.ts",
    "old_str_1": "...",
    "new_str_1": "..."
  },
  "file_changes": [
    {
      "path": "src/auth.ts",
      "changeType": "edit",
      "content": "// New code content here...",
      "oldContent": "// Old code that was replaced..."
    }
  ]
}
```

```bash theme={null}
#!/usr/bin/env bash
EVENT_DATA=$(cat)
echo "$EVENT_DATA" | jq -c '.file_changes[]?' | while read -r change; do
  echo "[AUDIT] $(echo $change | jq -r '.changeType'): $(echo $change | jq -r '.path')" >&2
done
exit 0
```

#### SessionStart / SessionEnd Events

Session events have no additional fields beyond the common base fields.

**Example SessionStart event:**

```json theme={null}
{
  "hook_event_name": "SessionStart",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"]
}
```

#### Stop Event

Stop events include information about why the agent stopped:

|        Field       |  Type  |                         Description                         |
| :----------------: | :----: | :---------------------------------------------------------: |
| `agent_stop_cause` | string | Why the agent stopped (e.g., `"end_turn"`, `"interrupted"`) |

**Example Stop event:**

```json theme={null}
{
  "hook_event_name": "Stop",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"],
  "agent_stop_cause": "end_turn"
}
```

### Metadata-Based Fields

When hooks declare metadata options in their configuration, additional fields are included in the event data:

#### `context` field (when `includeUserContext: true`)

Available for: **All event types**

```json theme={null}
{
  "context": {
    "userEmail": "user@example.com",
    "modelName": "Claude Opus 4.5",
    "toolVersion": "0.6.0",
    "timestamp": "2025-01-15T10:30:00-08:00"
  }
}
```

**How to use:**

* **`userEmail`**: Identify which user triggered the hook. Use for user-specific policies or analytics.
* **`modelName`**: AI model display name (e.g., "Claude Opus 4.5", "Sonnet-3.7"). Use for model-specific behavior.
* **`toolVersion`**: CLI or VSCode extension version (e.g., "0.6.0"). Use for debugging or version-specific behavior.
* **`timestamp`**: ISO 8601 timestamp. Use for auditing and analytics.

**Example: User-specific permissions**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  USER_EMAIL=$(echo "$EVENT_DATA" | jq -r '.context.userEmail // ""')
  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name')
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command // ""')

  # Only allow deployments for specific users
  if [[ "$TOOL_NAME" == "launch-process" ]] && echo "$COMMAND" | grep -q "deploy"; then
    if [[ "$USER_EMAIL" != "admin@example.com" ]]; then
      echo "Only admins can deploy" >&2
      exit 2
    fi
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json

  event_data = json.load(sys.stdin)
  user_email = event_data.get('context', {}).get('userEmail', '')

  # Only allow deployments for specific users
  tool_name = event_data.get('tool_name', '')
  command = event_data.get('tool_input', {}).get('command', '')

  if tool_name == 'launch-process' and 'deploy' in command:
      if user_email != 'admin@example.com':
          print("Only admins can deploy", file=sys.stderr)
          sys.exit(2)

  sys.exit(0)
  ```
</CodeGroup>

#### `mcp_metadata` field (when `includeMCPMetadata: true`)

Available for: **PreToolUse and PostToolUse only**

```json theme={null}
{
  "mcp_metadata": {
    "timestamp": "2025-01-15T10:30:00-08:00",
    "mcpDecision": "yes",
    "mcpTotalToolsCount": 215,
    "mcpExecutedToolName": "search_my-server",
    "mcpExecutedToolServerName": "my-server",
    "mcpExecutedToolServerToolsCount": 6
  }
}
```

**How to use:**

* **`timestamp`**: ISO 8601 timestamp. Use for auditing and analytics.
* **`mcpDecision`**: Whether this is an MCP tool (`"yes"`) or native tool (`"no"`).
* **`mcpTotalToolsCount`**: Total MCP tools available across all servers.
* **`mcpExecutedToolName`**: Full MCP tool name (e.g., `"search_my-server"`).
* **`mcpExecutedToolServerName`**: MCP server name (e.g., `"my-server"`).
* **`mcpExecutedToolServerToolsCount`**: Tools available from the executed server.

**Example: MCP-specific rate limiting**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  MCP_DECISION=$(echo "$EVENT_DATA" | jq -r '.mcp_metadata.mcpDecision // "no"')
  MCP_TOTAL=$(echo "$EVENT_DATA" | jq -r '.mcp_metadata.mcpTotalToolsCount // 0')

  # Block if too many MCP tools are enabled (security concern)
  if [[ "$MCP_DECISION" == "yes" ]] && [[ "$MCP_TOTAL" -gt 100 ]]; then
    echo "Too many MCP tools enabled ($MCP_TOTAL). Contact admin." >&2
    exit 2
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  # /etc/augment/hooks/mcp-limit.sh (Python via shebang)
  import sys
  import json

  event_data = json.load(sys.stdin)
  mcp_metadata = event_data.get('mcp_metadata', {})

  mcp_decision = mcp_metadata.get('mcpDecision', 'no')
  mcp_total = mcp_metadata.get('mcpTotalToolsCount', 0)

  # Block if too many MCP tools are enabled (security concern)
  if mcp_decision == 'yes' and mcp_total > 100:
      print(f"Too many MCP tools enabled ({mcp_total}). Contact admin.", file=sys.stderr)
      sys.exit(2)

  sys.exit(0)
  ```
</CodeGroup>

#### `conversation` field (when `includeConversationData: true`)

Available for: **Stop event only**

```json theme={null}
{
  "conversation": {
    "timestamp": "2025-01-15T10:30:00-08:00",
    "userPrompt": "Add error handling to the login function",
    "agentTextResponse": "I'll add comprehensive error handling...",
    "agentCodeResponse": [
      {
        "path": "src/auth/login.ts",
        "changeType": "edit",
        "content": "export function login() { try { ... } catch (e) { ... } }"
      }
    ]
  }
}
```

**How to use:**

* **`timestamp`**: ISO 8601 timestamp. Use for auditing.
* **`userPrompt`**: The user's original request.
* **`agentTextResponse`**: Agent's explanation of what it did.
* **`agentCodeResponse`**: Array of file changes. Each entry has:
  * `path`: File path modified
  * `changeType`: `"edit"`, `"create"`, or `"delete"`
  * `content`: New content (for edit/create only)

**Example: Require tests before finishing**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  # Extract code changes
  CODE_RESPONSE=$(echo "$EVENT_DATA" | jq -r '.conversation.agentCodeResponse // []')

  # Check if any test files were modified
  TEST_FILES=$(echo "$CODE_RESPONSE" | jq -r '.[] | select(.path | test("test|spec")) | .path')

  if [[ -z "$TEST_FILES" ]]; then
    # No test files modified - block stop
    cat << EOF
  {
    "hookSpecificOutput": {
      "hookEventName": "Stop",
      "decision": "block",
      "reason": "Please add or update tests before finishing"
    }
  }
  EOF
    exit 0
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  conversation = event_data.get('conversation', {})
  code_response = conversation.get('agentCodeResponse', [])

  # Check if any test files were modified
  test_files = [
      change['path'] for change in code_response
      if re.search(r'test|spec', change.get('path', ''))
  ]

  if not test_files:
      # No test files modified - block stop
      output = {
          "hookSpecificOutput": {
              "hookEventName": "Stop",
              "decision": "block",
              "reason": "Please add or update tests before finishing"
          }
      }
      print(json.dumps(output))
      sys.exit(0)

  sys.exit(0)
  ```
</CodeGroup>

### Reading Hook Input

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash

  # Read entire JSON from stdin
  EVENT_DATA=$(cat)

  # Extract fields using jq
  HOOK_EVENT=$(echo "$EVENT_DATA" | jq -r '.hook_event_name')
  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name // ""')
  CONV_ID=$(echo "$EVENT_DATA" | jq -r '.conversation_id')

  echo "Event: $HOOK_EVENT, Tool: $TOOL_NAME, Conversation: $CONV_ID"
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json

  event_data = json.load(sys.stdin)

  hook_event = event_data['hook_event_name']
  tool_name = event_data.get('tool_name', '')
  conv_id = event_data['conversation_id']

  print(f"Event: {hook_event}, Tool: {tool_name}, Conversation: {conv_id}")
  ```
</CodeGroup>

## Hook Output and Communication

Hooks communicate results through exit codes and output streams. The behavior depends on the exit code and the hook event type.

### Exit Codes

* **Exit code 0**: Success - Hook completed successfully
* **Exit code 2**: Blocking error - Prevents tool execution (PreToolUse only)
* **Other exit codes**: Non-blocking error - Logged but execution continues

### Output Streams

* **stdout**: Standard output from the hook
* **stderr**: Error output from the hook

### Communication Matrix

The following table shows how hook output is handled based on exit code and event type:

| Exit Code | Event Type   | Output Stream | Shown To |                         Behavior                        |
| :-------: | ------------ | :-----------: | -------- | :-----------------------------------------------------: |
|     2     | PreToolUse   |     stderr    | Agent    |   Blocks tool execution, agent sees why it was blocked  |
|     2     | SessionStart |     stderr    | User     | Hook failed at startup, user needs to fix configuration |
|     0     | PreToolUse   |     stderr    | User     |              Warning message shown to user              |
|     0     | PreToolUse   |     stdout    | User     |              Success message shown to user              |
|     0     | PostToolUse  |     stderr    | User     |              Warning message shown to user              |
|     0     | PostToolUse  |     stdout    | User     |              Success message shown to user              |
|     0     | SessionStart |     stdout    | Agent    |             Inject context at session start             |
|     0     | SessionEnd   |     stdout    | User     |                 Show completion message                 |
|   Other   | Any          |     stderr    | User     |            Error logged, execution continues            |

<Info>
  **Key Principle**: Exit code 2 with PreToolUse blocks the tool and shows stderr to the agent (so
  it knows why). Exit code 0 shows output to the user. SessionStart stdout is special - it injects
  context for the agent.
</Info>

### PreToolUse Output

**Blocking a tool (exit code 2):**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command // ""')

  if echo "$COMMAND" | grep -qE "rm -rf|sudo"; then
    echo "Blocked dangerous command: $COMMAND" >&2
    exit 2  # Blocks tool, stderr shown to agent
  fi

  exit 0  # Allow tool to proceed
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  command = event_data.get('tool_input', {}).get('command', '')

  if re.search(r'rm -rf|sudo', command):
      print(f"Blocked dangerous command: {command}", file=sys.stderr)
      sys.exit(2)  # Blocks tool, stderr shown to agent

  sys.exit(0)  # Allow tool to proceed
  ```
</CodeGroup>

**Warning message (exit code 0):**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)
  FILE_PATH=$(echo "$EVENT_DATA" | jq -r '.tool_input.path // ""')

  if echo "$FILE_PATH" | grep -qE "\.env|secrets"; then
    echo "Warning: Accessing sensitive file: $FILE_PATH" >&2
  fi

  exit 0  # Allow tool but show warning
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  file_path = event_data.get('tool_input', {}).get('path', '')

  if re.search(r'\.env|secrets', file_path):
      print(f"Warning: Accessing sensitive file: {file_path}", file=sys.stderr)

  sys.exit(0)  # Allow tool but show warning
  ```
</CodeGroup>

### SessionStart Output

SessionStart hooks can inject context for the agent by writing to stdout:

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash

  # Load current issues from issue tracker
  ISSUES=$(curl -s https://api.example.com/issues)

  # Output to stdout - this will be injected as context for the agent
  echo "Current open issues:"
  echo "$ISSUES"

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import requests

  # Load current issues from issue tracker
  response = requests.get('https://api.example.com/issues')
  issues = response.text

  # Output to stdout - this will be injected as context for the agent
  print("Current open issues:")
  print(issues)

  sys.exit(0)
  ```
</CodeGroup>

## Hook Output Reference

Hooks can return structured output to control execution and communicate with the agent or user. Output is provided via **stdout** (as JSON) and **stderr** (for error messages).

### Exit Codes

| Exit Code | Meaning            |                                           Behavior                                          |
| :-------: | ------------------ | :-----------------------------------------------------------------------------------------: |
|    `0`    | Success            |    Hook completed successfully. Tool execution continues (unless JSON output blocks it).    |
|    `2`    | Blocking Error     | **PreToolUse only**: Blocks tool execution. Stderr message is shown to both user and agent. |
|   Other   | Non-blocking Error |           Hook failed, but tool execution continues. Stderr shown in verbose mode.          |

### JSON Output Format

Hooks can return JSON on stdout (exit code 0 only) to provide structured control:

```json theme={null}
{
  "continue": true,
  "stopReason": "Optional reason if continue=false",
  "suppressOutput": false,
  "systemMessage": "Message shown to user",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Security policy violation"
  }
}
```

### Common JSON Fields (All Events)

These fields can be returned by any hook:

|       Field      | Type    |                     Description                     | Destination |
| :--------------: | ------- | :-------------------------------------------------: | :---------: |
|    `continue`    | boolean | If `false`, stops execution (overrides exit code 0) |      -      |
|   `stopReason`   | string  |          Reason shown when `continue=false`         |     User    |
| `suppressOutput` | boolean |      If `true`, hides stdout from verbose mode      |      -      |
|  `systemMessage` | string  |           Warning or informational message          |     User    |

### Event-Specific JSON Output

#### PreToolUse Output

PreToolUse hooks can control tool execution and modify tool input:

|            Field           | Type     |           Description          |   Destination  |
| :------------------------: | -------- | :----------------------------: | :------------: |
|    `permissionDecision`    | `"deny"` |      Block tool execution      |        -       |
| `permissionDecisionReason` | string   |  Reason for blocking the tool  | Agent and User |
|       `updatedInput`       | object   | Modified tool input parameters |        -       |

<Note>
  Currently only `permissionDecision: "deny"` is supported. The `"allow"` and `"ask"` values will be
  implemented in a future release.
</Note>

**Example: Block dangerous command**

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Command contains 'rm -rf' which is not allowed"
  }
}
```

**Example: Modify tool input**

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "git status --short"
    }
  }
}
```

#### PostToolUse Output

PostToolUse hooks can provide additional context to the agent:

|        Field        | Type      |                     Description                    | Destination |
| :-----------------: | --------- | :------------------------------------------------: | :---------: |
|      `decision`     | `"block"` |              Blocks agent with reason              |      -      |
|       `reason`      | string    | Reason for blocking (required if decision="block") |    Agent    |
| `additionalContext` | string    |    Additional context for the agent to consider    |    Agent    |

**Example: Provide context to agent**

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command modified 3 files in the authentication module"
  }
}
```

#### Stop Output

Stop hooks can prevent the agent from finishing:

|    Field   | Type      |                       Description                       | Destination |
| :--------: | --------- | :-----------------------------------------------------: | :---------: |
| `decision` | `"block"` |                      Prevents stop                      |      -      |
|  `reason`  | string    | Reason for blocking stop (required if decision="block") |    Agent    |

**Example: Prevent stop**

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "decision": "block",
    "reason": "Please run tests before finishing"
  }
}
```

#### SessionStart Output

SessionStart hooks can inject context for the agent:

|        Field        | Type   |             Description            | Destination |
| :-----------------: | ------ | :--------------------------------: | :---------: |
| `additionalContext` | string | Context to inject at session start |    Agent    |

**Example: Inject context**

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Current sprint: Sprint 23. Focus: Authentication refactor"
  }
}
```

### Output Routing

Different output goes to different destinations:

**To Agent (injected into conversation):**

* Exit code 2 stderr (PreToolUse, PostToolUse, Stop events)
* `permissionDecisionReason` (when decision="deny")
* `reason` (when decision="block")
* `additionalContext`
* SessionStart stdout or `additionalContext`

**To User (displayed in UI):**

* Exit code 2 stderr (SessionStart, SessionEnd events)
* `systemMessage`
* `permissionDecisionReason` (when decision="allow" or "ask")
* Plain stdout (in verbose mode, for non-SessionStart events)

### Complete Output Examples

<CodeGroup>
  ```bash Bash - Block with Exit Code 2 theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command // ""')

  if echo "$COMMAND" | grep -qE "rm -rf"; then
    echo "Blocked dangerous command: $COMMAND" >&2
    exit 2  # Blocks tool, stderr shown to agent and user
  fi

  exit 0
  ```

  ```python Python - Block with Exit Code 2 theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  command = event_data.get('tool_input', {}).get('command', '')

  if re.search(r'rm -rf', command):
      print(f"Blocked dangerous command: {command}", file=sys.stderr)
      sys.exit(2)  # Blocks tool, stderr shown to agent and user

  sys.exit(0)
  ```
</CodeGroup>

<CodeGroup>
  ```bash Bash - Block with JSON theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command // ""')

  if echo "$COMMAND" | grep -qE "rm -rf"; then
    cat << EOF
  {
    "hookSpecificOutput": {
      "hookEventName": "PreToolUse",
      "permissionDecision": "deny",
      "permissionDecisionReason": "Command contains 'rm -rf' which violates security policy"
    }
  }
  EOF
    exit 0
  fi

  exit 0
  ```

  ```python Python - Block with JSON theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)
  command = event_data.get('tool_input', {}).get('command', '')

  if re.search(r'rm -rf', command):
      output = {
          "hookSpecificOutput": {
              "hookEventName": "PreToolUse",
              "permissionDecision": "deny",
              "permissionDecisionReason": "Command contains 'rm -rf' which violates security policy"
          }
      }
      print(json.dumps(output))
      sys.exit(0)

  sys.exit(0)
  ```
</CodeGroup>

## Hook Metadata (Configuration)

Hook metadata options are **configuration-level flags** that control what data is included in the hook input. They provide a privacy-first, opt-in model for accessing conversation data, MCP metadata, and user context.

### Available Metadata Options

Metadata options are specified in the hook configuration (not in hook output):

```json theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/analytics.sh"
          }
        ],
        "metadata": {
          "includeConversationData": true,
          "includeMCPMetadata": true,
          "includeUserContext": false
        }
      }
    ]
  }
}
```

**Metadata flags:**

* **`includeUserContext`**: Include user and environment context in hook input
  * Adds `context` field to hook event data
  * Available for: **All event types** (PreToolUse, PostToolUse, Stop, SessionStart, SessionEnd)
  * Fields included:
    * `userEmail` - User's email address (e.g., "[user@example.com](mailto:user@example.com)")
    * `modelName` - Model name being used (e.g., "Claude Opus 4.5")
    * `timestamp` - ISO 8601 timestamp (e.g., "2025-01-15T10:30:00-08:00")
  * Default: `false` (user context excluded)

* **`includeMCPMetadata`**: Include MCP-specific metadata in hook input
  * Adds `mcp_metadata` field to hook event data
  * Available for: **PreToolUse and PostToolUse only**
  * Fields included:
    * `mcpDecision` - Whether MCP tools were used ("yes" | "no")
    * `mcpTotalToolsCount` - Total number of MCP tools available across all servers
    * `mcpExecutedToolName` - Name of the executed MCP tool (if any)
    * `mcpExecutedToolServerName` - Server name of the executed MCP tool (if any)
    * `mcpExecutedToolServerToolsCount` - Number of tools from the executed server (if any)
  * Default: `false` (MCP metadata excluded)

* **`includeConversationData`**: Include conversation fields in hook input
  * Adds `conversation` field to hook event data
  * Available for: **Stop event only**
  * Fields included:
    * `userPrompt` - The user's prompt/message that triggered the agent response
    * `agentTextResponse` - Agent's text response (markdown format)
    * `agentCodeResponse` - Array of file changes made by the agent, each containing:
      * `path` - File path relative to workspace root
      * `changeType` - Type of change ("edit" | "create" | "delete")
      * `content` - File content after the change (undefined for deletions)
  * Default: `false` (conversation data excluded for privacy)

**Metadata availability by event type:**

|      Metadata Option      | PreToolUse | PostToolUse | Stop | SessionStart | SessionEnd |
| :-----------------------: | :--------: | :---------: | :--: | :----------: | :--------: |
|    `includeUserContext`   |      ✓     |      ✓      |   ✓  |       ✓      |      ✓     |
|    `includeMCPMetadata`   |      ✓     |      ✓      |   -  |       -      |      -     |
| `includeConversationData` |      -     |      -      |   ✓  |       -      |      -     |

### When to Use Metadata Options

**Use `includeUserContext` when:**

* Implementing user-specific rate limiting
* Building per-user analytics
* Tracking model usage by user
* Implementing user-based access controls
* Logging user activity for compliance

**Use `includeMCPMetadata` when:**

* Monitoring MCP tool usage patterns
* Debugging MCP integration issues
* Building MCP usage analytics
* Rate limiting MCP tool calls
* Tracking which MCP servers are being used

**Use `includeConversationData` when:**

* Building analytics dashboards that track user interactions
* Implementing compliance logging for audit trails
* Analyzing agent response quality
* Tracking code changes made by the agent
* Capturing complete conversation context for debugging

### Hook Input with Metadata

When metadata options are enabled, the hook receives additional fields in the event data. Here's an example showing all three options enabled:

**Configuration:**

```json theme={null}
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/analytics.sh"
          }
        ],
        "metadata": {
          "includeUserContext": true,
          "includeConversationData": true
        }
      }
    ]
  }
}
```

**Hook Input (Stop event with all metadata options):**

```json theme={null}
{
  "hook_event_name": "Stop",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"],
  "agent_stop_cause": "end_turn",

  "context": {
    "userEmail": "user@example.com",
    "modelName": "Claude Opus 4.5",
    "toolVersion": "0.6.0",
    "timestamp": "2025-01-15T10:30:00-08:00"
  },

  "conversation": {
    "timestamp": "2025-01-15T10:30:00-08:00",
    "userPrompt": "Add error handling to the login function",
    "agentTextResponse": "I'll add comprehensive error handling...",
    "agentCodeResponse": [{ "path": "src/auth/login.ts", "changeType": "edit" }]
  }
}
```

**Hook Input (PostToolUse event with metadata - MCP tool):**

```json theme={null}
{
  "hook_event_name": "PostToolUse",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"],
  "tool_name": "search_example-server",
  "tool_input": { "query": "latest documentation" },
  "tool_output": "Found 5 results...",
  "is_mcp_tool": true,
  "context": {
    "userEmail": "user@example.com",
    "modelName": "Claude Opus 4.5",
    "toolVersion": "0.6.0",
    "timestamp": "2025-01-15T10:30:00-08:00"
  },
  "mcp_metadata": {
    "timestamp": "2025-01-15T10:30:00-08:00",
    "mcpDecision": "yes",
    "mcpTotalToolsCount": 15,
    "mcpExecutedToolName": "search",
    "mcpExecutedToolServerName": "example-server",
    "mcpExecutedToolServerToolsCount": 5
  }
}
```

**Hook Input (PostToolUse event with file\_changes - file edit):**

```json theme={null}
{
  "hook_event_name": "PostToolUse",
  "conversation_id": "conv-xyz789",
  "workspace_roots": ["/Users/username/project"],
  "tool_name": "str-replace-editor",
  "tool_input": {
    "path": "src/auth.ts",
    "old_str_1": "...",
    "new_str_1": "..."
  },
  "tool_output": "File edited successfully",
  "is_mcp_tool": false,
  "file_changes": [
    {
      "path": "src/auth.ts",
      "changeType": "edit",
      "content": "// New content...",
      "oldContent": "// Old content that was replaced..."
    }
  ],
  "context": {
    "userEmail": "user@example.com",
    "modelName": "Claude Opus 4.5",
    "toolVersion": "0.6.0",
    "timestamp": "2025-01-15T10:30:00-08:00"
  }
}
```

### Privacy Considerations

Metadata options follow a **privacy-first, opt-in model**:

1. **Default deny**: All sensitive data is excluded by default
2. **Explicit opt-in**: Hooks must explicitly request metadata options
3. **Minimal access**: Request only the options you need
4. **Audit trail**: Metadata usage should be logged for compliance

<Warning>
  When using metadata options that include user data (`includeConversationData`,
  `includeUserContext`), ensure your hook scripts: - Handle sensitive data securely - Comply with
  privacy regulations (GDPR, CCPA, etc.) - Implement appropriate data retention policies - Use
  encryption for data at rest and in transit
</Warning>

### Example: Analytics Hook with Metadata

**Configuration:**

```json theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/analytics.sh"
          }
        ],
        "metadata": {
          "includeUserContext": true,
          "includeMCPMetadata": true
        }
      }
    ]
  }
}
```

**Hook script (with metadata options):**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  # /etc/augment/hooks/analytics.sh

  EVENT_DATA=$(cat)

  # Extract user context (available because includeUserContext=true)
  USER_EMAIL=$(echo "$EVENT_DATA" | jq -r '.context.userEmail // ""')
  MODEL_NAME=$(echo "$EVENT_DATA" | jq -r '.context.modelName // ""')

  # Extract MCP metadata (available because includeMCPMetadata=true)
  MCP_DECISION=$(echo "$EVENT_DATA" | jq -r '.mcp_metadata.mcpDecision // "no"')
  MCP_SERVER=$(echo "$EVENT_DATA" | jq -r '.mcp_metadata.mcpExecutedToolServerName // ""')

  # Log analytics
  echo "User: $USER_EMAIL, Model: $MODEL_NAME, MCP: $MCP_DECISION, Server: $MCP_SERVER"
  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  # /etc/augment/hooks/analytics.sh (Python via shebang)

  import sys
  import json

  event_data = json.load(sys.stdin)

  # Extract user context
  context = event_data.get('context', {})
  user_email = context.get('userEmail', '')
  model_name = context.get('modelName', '')

  # Extract MCP metadata
  mcp = event_data.get('mcp_metadata', {})
  mcp_decision = mcp.get('mcpDecision', 'no')
  mcp_server = mcp.get('mcpExecutedToolServerName', '')

  print(f"User: {user_email}, Model: {model_name}, MCP: {mcp_decision}")
  sys.exit(0)
  ```
</CodeGroup>

## Working with MCP Tools

Hooks work seamlessly with [Model Context Protocol (MCP)](/setup-augment/mcp) tools. MCP tools have special naming and metadata that you can use in hooks.

### MCP Tool Naming

MCP tools follow the naming pattern `{toolName}_{serverName}`. For example:

* `search_my-server` - "search" tool from "my-server"
* `query_database-server` - "query" tool from "database-server"
* `read_filesystem-mcp` - "read" tool from "filesystem-mcp"

<Note>
  Both tool names and server names can contain underscores. The server name is always the suffix
  after the **last** underscore that matches the known server name. For reliable matching, use the
  `mcp_server_name` field in your hook script rather than parsing the tool name.
</Note>

### MCP Tool Matchers

Use the `mcp:` prefix to match MCP tools. The pattern after `mcp:` is a regex matched against the full tool name (`toolName_serverName`):

* `"mcp:*"` - Match ALL MCP tools (special case)
* `"mcp:.*_my-server$"` - Match any tool from `my-server` (use `$` anchor)
* `"mcp:^search_my-server$"` - Match exact tool `search` from `my-server`
* `"mcp:^search_.*"` - Match `search` tool from any server

<Info>
  The `mcp:` prefix ensures only MCP tools are matched. The pattern is a standard regex applied to
  the full tool name. Use the `$` anchor when matching server names to avoid partial matches.
</Info>

### MCP Hook Examples

**Log MCP tool usage:**

```bash theme={null}
#!/usr/bin/env bash
EVENT_DATA=$(cat)
SERVER=$(echo "$EVENT_DATA" | jq -r '.mcp_server_name // ""')
echo "[MCP] Server: $SERVER, Tool: $(echo "$EVENT_DATA" | jq -r '.tool_name')" >&2
exit 0
```

**Configuration:**

```json theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp:*",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/log-mcp-tools.sh",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

**Block specific MCP server:**

```bash theme={null}
#!/usr/bin/env bash
EVENT_DATA=$(cat)
MCP_SERVER=$(echo "$EVENT_DATA" | jq -r '.mcp_server_name // ""')

if [ "$MCP_SERVER" = "blocked-server" ]; then
  echo "This MCP server is blocked by security policy" >&2
  exit 2
fi

exit 0
```

**Configuration:**

```json theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp:.*_blocked-server$",
        "hooks": [
          {
            "type": "command",
            "command": "/etc/augment/hooks/block-mcp-server.sh",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

## Examples

For ready-to-use hook examples, see [Hooks Examples](/cli/hooks-examples).

## Debugging Hooks

### Environment Variables

Hooks have access to these environment variables during execution:

|          Variable         | Description                                                  |          Example          |
| :-----------------------: | ------------------------------------------------------------ | :-----------------------: |
|   `AUGMENT_PROJECT_DIR`   | First workspace root directory (or `process.cwd()` if empty) | `/Users/username/project` |
| `AUGMENT_CONVERSATION_ID` | Current conversation ID                                      |       `conv-xyz789`       |
|    `AUGMENT_HOOK_EVENT`   | Event type                                                   |        `PreToolUse`       |
|    `AUGMENT_TOOL_NAME`    | Tool name (PreToolUse/PostToolUse only)                      |      `launch-process`     |

```bash theme={null}
#!/usr/bin/env bash
echo "Project: $AUGMENT_PROJECT_DIR, Event: $AUGMENT_HOOK_EVENT" >&2
exit 0
```

### Testing Hooks Locally

**1. Create a test event file:**

```bash theme={null}
cat > test-event.json << 'EOF'
{
  "hook_event_name": "PreToolUse",
  "conversation_id": "test-conv",
  "workspace_roots": ["/Users/username/project"],
  "tool_name": "launch-process",
  "tool_input": { "command": "git status" }
}
EOF
```

**2. Test your hook script:**

```bash theme={null}
# Test your hook script (works for both bash and Python via shebang)
cat test-event.json | /etc/augment/hooks/my-hook.sh
echo "Exit code: $?"
```

**3. Validate JSON output:**

```bash theme={null}
# Test and validate JSON output
OUTPUT=$(cat test-event.json | /etc/augment/hooks/my-hook.sh)
echo "$OUTPUT" | jq .  # Validates JSON syntax
```

### Viewing Hook Execution Logs

Hooks log to the Augment logger. To see hook execution details:

**CLI:**

```bash theme={null}
# Run with verbose logging
auggie --verbose "your prompt here"

# Or set log level
export AUGMENT_LOG_LEVEL=debug
auggie "your prompt here"
```

**Check logs for:**

* `[HookExecutor]` - Hook execution details
* `[HookManager]` - Hook matching and routing
* `[hook-output-router]` - Output routing decisions

### Common Debugging Techniques

**Log to stderr (won't affect hook output):**

```bash theme={null}
#!/usr/bin/env bash
EVENT_DATA=$(cat)
echo "[DEBUG] $(echo "$EVENT_DATA" | jq -r '.hook_event_name')" >&2
exit 0
```

**Save event data for inspection:**

```bash theme={null}
#!/usr/bin/env bash
cat > /tmp/hook-debug.json
exit 0
```

#### 3. Validate hook matcher patterns

To test if your matcher pattern works:

```bash theme={null}
# Test regex pattern in bash
TOOL_NAME="search_my-server"
PATTERN=".*_my-server$"

if [[ "$TOOL_NAME" =~ $PATTERN ]]; then
  echo "Pattern matches!"
else
  echo "Pattern does not match"
fi
```

```python theme={null}
# Test regex pattern in Python
import re

tool_name = "search_my-server"
pattern = r".*_my-server$"

if re.match(pattern, tool_name):
    print("Pattern matches!")
else:
    print("Pattern does not match")
```

### Performance Tips

1. **Keep hooks fast** - Hooks run synchronously and block tool execution
2. **Cache expensive operations** - Store results in files or environment variables
3. **Use early returns** - Exit as soon as you know the result
4. **Avoid network calls** - Network requests add latency
5. **Minimize JSON parsing** - Parse only the fields you need

**Example: Fast hook with early return**

<CodeGroup>
  ```bash Bash theme={null}
  #!/usr/bin/env bash
  EVENT_DATA=$(cat)

  # Early return if not a launch-process tool
  TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name')
  if [[ "$TOOL_NAME" != "launch-process" ]]; then
    exit 0  # Not interested, return immediately
  fi

  # Only parse command if we got here
  COMMAND=$(echo "$EVENT_DATA" | jq -r '.tool_input.command')

  # Check command
  if echo "$COMMAND" | grep -qE "rm -rf"; then
    echo "Blocked dangerous command" >&2
    exit 2
  fi

  exit 0
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  import sys
  import json
  import re

  event_data = json.load(sys.stdin)

  # Early return if not a launch-process tool
  tool_name = event_data.get('tool_name', '')
  if tool_name != 'launch-process':
      sys.exit(0)  # Not interested, return immediately

  # Only parse command if we got here
  command = event_data.get('tool_input', {}).get('command', '')

  # Check command
  if re.search(r'rm -rf', command):
      print("Blocked dangerous command", file=sys.stderr)
      sys.exit(2)

  sys.exit(0)
  ```
</CodeGroup>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Hook not being triggered">
    **Check:**

    1. **Matcher pattern** - Verify your regex pattern matches the tool name
    2. **Event type** - Ensure you're listening to the correct event (PreToolUse vs PostToolUse)
    3. **Settings file location** - Verify hooks are in the correct settings file (project vs user vs system)
    4. **Hook path** - Ensure the hook script path is correct and the file exists
    5. **File permissions** - Make sure the hook script is executable (`chmod +x hook.sh`)

    **Debug:**

    ```bash theme={null}
    # Check if hook file exists and is executable
    ls -la /etc/augment/hooks/my-hook.sh

    # Test matcher pattern
    echo "launch-process" | grep -E "launch-process|str-replace-editor"  # Should match
    echo "view" | grep -E "launch-process|str-replace-editor"  # Should not match
    ```
  </Accordion>

  <Accordion title="Hook execution timeout">
    Hooks have a **60-second timeout** by default. If your hook takes longer:

    1. **Optimize the hook** - Make it faster
    2. **Run async operations** - Don't wait for slow operations
    3. **Use background jobs** - Start long-running tasks in the background

    ```bash theme={null}
    #!/usr/bin/env bash
    EVENT_DATA=$(cat)

    # Start long-running task in background (don't wait)
    (
      # Long-running operation here
      sleep 300
    ) &

    # Return immediately
    exit 0
    ```
  </Accordion>

  <Accordion title="JSON parsing errors">
    **Common issues:**

    * **Invalid JSON syntax** - Use `jq` to validate
    * **Missing quotes** - Ensure all strings are quoted
    * **Trailing commas** - JSON doesn't allow trailing commas
    * **Special characters** - Escape special characters in strings

    **Validate JSON:**

    ```bash theme={null}
    # Test JSON output
    cat << 'EOF' | jq .
    {
      "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny"
      }
    }
    EOF
    ```
  </Accordion>

  <Accordion title="Hook blocks but shouldn't">
    **Check:**

    * **Exit code** - Make sure you're returning `exit 0` for success
    * **JSON output** - Verify `permissionDecision` is not set to `"deny"`
    * **stderr output** - Ensure you're not writing errors to stderr with exit code 2

    **Debug:**

    ```bash theme={null}
    #!/usr/bin/env bash
    EVENT_DATA=$(cat)

    # Explicitly allow
    echo "Allowing tool execution" >&2  # Debug message
    exit 0  # Success - don't block
    ```
  </Accordion>

  <Accordion title="Hook errors in logs">
    Check the Auggie logs for hook execution errors:

    ```bash theme={null}
    # View recent logs
    tail -f ~/.augment/logs/auggie.log | grep -i hook
    ```
  </Accordion>

  <Accordion title="Testing hooks locally">
    Test your hook script manually:

    ```bash theme={null}
    # Create test event data
    echo '{
      "hook_event_name": "PreToolUse",
      "tool_name": "launch-process",
      "tool_input": {"command": "ls -la"}
    }' | /etc/augment/hooks/your-hook.sh

    # Check exit code
    echo $?
    ```
  </Accordion>
</AccordionGroup>

## Security Considerations

<Warning>
  **USE AT YOUR OWN RISK**: Hooks execute arbitrary shell commands on your system automatically. By using hooks, you acknowledge that:

  * You are solely responsible for the commands you configure
  * Hooks can modify, delete, or access any files your user account can access
  * Malicious or poorly written hooks can cause data loss or system damage
  * You should thoroughly test hooks in a safe environment before production use

  Always review and understand any hook commands before adding them to your configuration.
</Warning>

### Security Best Practices

1. **Validate and sanitize inputs** - Never trust input data blindly
2. **Always quote shell variables** - Use `"$VAR"` not `$VAR`
3. **Block path traversal** - Check for `..` in file paths
4. **Use absolute paths** - Specify full paths for scripts
5. **Skip sensitive files** - Avoid `.env`, `.git/`, keys, etc.
6. **Set appropriate timeouts** - Prevent hooks from hanging indefinitely
7. **Test thoroughly** - Test hooks with various inputs before deploying

## Best Practices

1. **Keep hooks fast**: Hooks should complete quickly (\< 1 second) to avoid slowing down the agent
2. **Use timeouts**: Always set reasonable timeouts to prevent hanging
3. **Handle errors gracefully**: Use exit code 0 for non-critical errors to avoid blocking the agent
4. **Log appropriately**: Use stderr for user-facing messages, log files for detailed audit trails
5. **Test thoroughly**: Test hooks with various tool inputs before deploying
6. **Version control**: Keep hook scripts in version control with your project
7. **Document behavior**: Add comments explaining what each hook does and why

## Limitations

* Hooks currently only support command execution (webhooks planned for future)
* PostToolUse hooks cannot modify tool output (read-only)
* Hooks cannot access the agent's conversation history directly
* Maximum timeout is enforced to prevent indefinite blocking
* Hook execution is sequential, not parallel

## Hook Execution Details

* **Timeout**: 60-second execution limit by default, configurable per command
* **Execution order**: Hooks execute in the order they are defined
* **Environment**: Runs in current directory with Auggie's environment
* **Input**: JSON via stdin
* **Output**:
  * PreToolUse/PostToolUse/Stop: Progress shown in logs
  * SessionStart: stdout added as context for agent
  * SessionEnd: Logged to debug only

## Related Documentation

* [Hooks Examples](/cli/hooks-examples) - Ready-to-use hook examples
* [MCP (Model Context Protocol)](/setup-augment/mcp) - External tool integration
* [Permissions](/cli/permissions) - Tool permission system
* [Rules & Guidelines](/cli/rules) - Custom rules and guidelines
* [Custom Commands](/cli/custom-commands) - Create custom CLI commands


# Integrations and MCP
Source: https://docs.augmentcode.com/cli/integrations

Expand Augment's capabilities with external tools and data sources through native integrations and Model Context Protocol (MCP) servers.

<Note>Auggie runs commands and tools automatically. Only use integrations and MCP servers from trusted sources, and be aware of the risks of combining multiple tools with external data sources or production systems.</Note>

## About Integrations and MCP

Auggie can utilize external integrations through native integrations like GitHub, Linear, and Notion and Model Context Protocol (MCP) to access external systems for information and integrate tools to take actions. MCP is an open protocol that provides a standardized way to connect AI models to different data sources and tools.

## Native Integrations

You'll need to configure the integration in Augment for VS Code or JetBrains IDEs. Once configured, the integration will be available for use with Auggie automatically. See a full list and examples for [native agent integrations](/setup-augment/agent-integrations).

### 1. Setup in Augment extension

* **Visual Studio Code**: Click the settings icon in the top right of Augment's chat window or press <Keyboard /> and select <Command />
* **JetBrains IDEs**: Click the Augment icon in the bottom right of your JetBrains IDE and select <Command />

### 2. Connect the integration

Click "Connect" for the integration you want to set up

<img alt="Set up integrations in the settings page" />

You'll be redirected to authorize the integration with the appropriate service. After authorization, the integration will be available for use with Augment Agent.

## MCP Integrations

In addition to native integrations, Auggie can also access external systems through Model Context Protocol (MCP) servers. MCP servers enable Auggie to interact with external tools and services through a standardized protocol, such as accessing databases, running browser automation, sending messages to Slack, or integrating with APIs.

### Configure MCP via settings.json

You can persist MCP servers in the Augment settings file `~/.augment/settings.json`, which will initialize on startup and can be checked with `/mcp-status`.

```json theme={null}
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    },
    "weather": {
      "type": "sse",
      "url": "https://weather-mcp.example.com/v1",
      "headers": {
        "X-API-Key": "your_weather_api_key",
        "Content-Type": "application/json"
      }
    },
    "renderMCP": {
      "type": "http",
      "url": "https://mcp.render.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_KEY>"
      }
    },
    "local-tool": {
      "command": "/usr/local/bin/custom-mcp",
      "args": ["--serve", "--port", "3000"],
      "env": { "DEBUG": "true" }
    }
  }
}
```

#### HTTP Transport with Headers

MCP servers using HTTP transport can include a `headers` object for authentication or custom headers:

```json theme={null}
{
  "mcpServers": {
    "renderMCP": {
      "type": "http",
      "url": "https://mcp.render.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "X-Custom-Header": "custom-value"
      }
    }
  }
}
```

The `headers` field accepts any valid HTTP headers as key-value pairs.

**Common uses**

* **Authentication** - `Authorization` headers with bearer tokens or API keys
* **Custom parameters** - Server-specific information that doesn't fit into standard request parameters
* **Session management** - `Mcp-Session-Id` header for managing sessions in Streamable HTTP transport

**Considerations**

* **Transport type** - Headers are relevant for HTTP and SSE transports only. Stdio transport uses standard input/output and does not use HTTP headers
* **Server requirements** - Required headers depend on the MCP server implementation
* **Security** - Avoid including sensitive information like API keys directly in configuration files. Consider secure credential management methods

### Manage MCP servers with the Auggie CLI

You can add and inspect MCP servers is via Auggie subcommands, which will persist the configuration to your `~/.augment/settings.json` file:

#### Usage

**Add MCP server:**

```bash theme={null}
auggie mcp add <name> [options]
```

Writes the server entry to your settings.json with interactive prompts for overwriting existing configurations.

Options:

* `--command <path>` - Executable path (for stdio transport)
* `--args <args>` - Arguments string for command
* `-e, --env <KEY=VAL>` - Environment variable (repeatable)
* `-t, --transport <transport>` - stdio|sse|http (default: "stdio")
* `-u, --url <url>` - URL (required for --transport sse or http)
* `-h, --header <KEY:VAL>` - HTTP header (repeatable, for http transport)
* `-r, --replace` - Overwrite existing entry without prompt
* `--json` - Output JSON

**Add MCP server from JSON:**

```bash theme={null}
auggie mcp add-json <name> <json>
```

Import an MCP server configuration directly from a JSON string. This is useful when you have a complete server configuration in JSON format and want to add it quickly without specifying individual options.

The JSON string should match the structure used in `settings.json` for MCP server configurations. This command uses the same mechanism as `--mcp-config` but provides a convenient way to add servers directly from the command line.

**List MCP servers:**

```bash theme={null}
auggie mcp list [options]
```

Lists configured MCP servers (from settings and any active overrides).

Options:

* `--json` - Output JSON format

**Remove MCP server:**

```bash theme={null}
auggie mcp remove <name> [options]
```

Cleanly removes the named server configuration from settings.json.

Examples:

```bash theme={null}
# Add a stdio-based MCP server (executable with args and environment)
auggie mcp add context7 \
  --command npx \
  --args "-y @upstash/context7-mcp@latest" \
  --env CONTEXT7_API_KEY=your_key

# Compressed syntax 
auggie mcp add context7 -- npx -y @upstash/context7-mcp

# Add an SSE-based MCP server (Server-Sent Events with URL)
auggie mcp add weather-api \
  --transport sse \
  --url https://weather-mcp.example.com/sse

# Compressed syntax
auggie mcp add weather-api --transport sse https://weather-mcp.example.com/sse

# Add an HTTP-based MCP server with authentication headers
auggie mcp add renderMCP \
  --transport http \
  --url https://mcp.render.com/mcp \
  --header "Authorization:Bearer YOUR_API_TOKEN"

# Add HTTP server with multiple headers
auggie mcp add api-service \
  --transport http \
  --url https://api.example.com/mcp \
  --header "Authorization:Bearer YOUR_TOKEN" \
  --header "X-Custom-Header:custom-value"

# List all configured servers (tabular display with status)
auggie mcp list

# List servers in JSON format for programmatic access
auggie mcp list --json

# Remove a server configuration
auggie mcp remove context7

# Replace existing server without interactive prompt
auggie mcp add context7 --command npx --args "..." --replace

# Add MCP server from JSON configuration (stdio transport)
auggie mcp add-json weather-api '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'

# Add MCP server from JSON configuration (SSE transport)
auggie mcp add-json remote-api '{"type":"sse","url":"https://api.example.com/sse"}'

# Add MCP server from JSON configuration (HTTP transport with headers)
auggie mcp add-json renderMCP '{"type":"http","url":"https://mcp.render.com/mcp","headers":{"Authorization":"Bearer ABC_XYZ_123"}}'
```

### MCP overrides

You can define servers by passing ad‑hoc overrides with `--mcp-config`. The structure is the same as `settings.json`:

```json theme={null}
// After npm install gitlab-mr-mcp
{
  "mcpServers": {
    "gitlab-mr-mcp": {
      "command": "node",
      "args": ["/path/to/gitlab-mr-mcp/index.js"],
      "env": {
        "MR_MCP_GITLAB_TOKEN": "your_gitlab_token",
        "MR_MCP_GITLAB_HOST": "your_gitlab_host"
      }
    }
  }
}
```


# Interactive mode
Source: https://docs.augmentcode.com/cli/interactive

Use a rich interactive terminal experience to explore your codebase, build new features, debug issues, and integrate your tools.

<Note>Auggie is currently in beta and does not support all features available in the Augment plugins for Visual Studio Code or JetBrains IDEs.</Note>

## About interactive mode

Auggie is an agentic terminal-based code assistant that has deep codebase knowledge powered by Augment's context engine. Auggie can help you understand a new codebase, fix bugs quickly, and build new features faster. Auggie has access to your connected integrations and MCP servers and can pull in additional context or run tools to get your tasks done.

## Using interactive mode

Run `auggie` without any mode flags to get the full-screen terminal user interface with rich interactive features, real-time streaming of responses, and visual progress indicators. This mode shows all tool calls, results, and allows ongoing conversation through an intuitive interface.

```sh theme={null}
# Start Auggie in interactive mode
auggie

# Provide an initial instruction
auggie "Look at my open issues and prioritize the highest impact ones for me"
```

### Multi-line input

Entering a new line in the input box depends on your terminal configuration and platform. You can use `Ctrl + J` to enter a new line in any terminal. See below for instructions to configure your terminal to use `Option + Enter` to enter a new line.

| Terminal application       | New line shortcut |
| :------------------------- | :---------------- |
| All terminals              | `Ctrl + J`        |
| MacOS Terminal (see below) | `Option + Enter`  |
| iTerm2 (see below)         | `Option + Enter`  |
| VS Code Terminal           | `Option + Enter`  |
| Ghostty                    | `Shift + Enter`   |

**MacOS Terminal**

1. Go to <Command />
2. Check <Command />

**iTerm2**

1. Go to <Command />
2. Check <Command />

## Reference

### Shortcuts

| Command             | Description                                                 |
| :------------------ | :---------------------------------------------------------- |
| `Ctrl + P`          | Enhance your prompt with codebase context                   |
| `Escape`            | Interrupt the active agent                                  |
| `Ctrl + C`          | Interrupt the active agent                                  |
| `Escape` + `Escape` | Clear the input box                                         |
| `Ctrl + C`          | Press twice to exit                                         |
| `Ctrl + D`          | Press twice to exit                                         |
| `Up Arrow`          | Cycle through previous messages                             |
| `Down Arrow`        | Cycle through previous messages                             |
| `Ctrl + O`          | Open current input in external editor, inserts text on exit |

### Slash Commands

| Command            | Description                                                 |
| :----------------- | :---------------------------------------------------------- |
| `/account`         | Show account information                                    |
| `/clear`           | Clear the input box                                         |
| `/editor`          | Open current input in external editor, inserts text on exit |
| `/exit`            | Exit Auggie                                                 |
| `/feedback`        | Provide feedback to the Augment team                        |
| `/github-workflow` | Generate a GitHub Action workflow                           |
| `/help`            | Show help                                                   |
| `/logout`          | Logout of Augment                                           |
| `/mcp-status`      | View the status of all configured MCP servers               |
| `/model`           | Select the model for this session                           |
| `/new`             | Start a new conversation with no message history            |
| `/permissions`     | View and manage tool permissions                            |
| `/request-id`      | Show the request ID for the current conversation            |
| `/rules`           | View loaded rules and their attachment status               |
| `/skills`          | View loaded skills and their token counts                   |
| `/task`            | Open task manager to add, edit, and manage tasks            |
| `/verbose`         | Toggle verbose output for tools                             |
| `/vim`             | Toggle Vim mode for advanced text editing                   |

For more information about slash commands, including how to create custom commands, see [Custom Slash Commands](/cli/custom-commands).


# Prompt Enhancer
Source: https://docs.augmentcode.com/cli/interactive/prompt-enhancer

Use Ctrl+P to enhance your prompts with relevant context, structure, and conventions from your codebase.

## About the Prompt Enhancer

The Auggie CLI prompt enhancer is a powerful feature that helps you craft better prompts by automatically adding relevant context, structure, and conventions from your codebase. Instead of writing detailed prompts from scratch, you can start with a simple idea and let the prompt enhancer transform it into a comprehensive, well-structured prompt.

## Activating the Prompt Enhancer

To use the prompt enhancer in Auggie's interactive mode:

1. **Start typing your prompt** in the input box
2. **Press <Keyboard />** to activate the prompt enhancer
3. **Wait for enhancement** - Auggie will process your prompt and replace it with an enhanced version
4. **Review and edit** the enhanced prompt if needed
5. **Submit your enhanced prompt** by pressing Enter

<Note>The prompt enhancer is only available when you have text entered at the command prompt. The <Keyboard /> shortcut will only work in interactive mode.</Note>

## How It Works

When you press <Keyboard />, the prompt enhancer:

1. **Captures your current input** and saves it to history
2. **Switches to Enhancement mode** - you'll see the mode indicator change and input will be temporarily disabled
3. **Sends your prompt** to the enhancement service using your current workspace context
4. **Processes the response** and extracts the enhanced prompt
5. **Replaces your input** with the enhanced version and returns to Normal mode

During enhancement, you'll see:

* The mode indicator shows "Enhancing your prompt, press Esc to cancel"
* Input is disabled to prevent conflicts
* A visual indication that processing is in progress

## Enhancement Process

The prompt enhancer uses your workspace context to improve your prompts by:

* **Adding relevant file references** from your current project
* **Including coding conventions** and patterns from your codebase
* **Structuring the prompt** for better clarity and specificity
* **Adding context** about your project's architecture and dependencies
* **Suggesting specific examples** based on existing code patterns

## Canceling Enhancement

You can cancel the prompt enhancement process at any time:

* **Press <Keyboard />** to cancel enhancement and restore your original input
* **Press <Keyboard />** to cancel enhancement and restore your original input

When canceled, you'll see a brief notification and your original prompt will be restored.

## Error Handling

If the prompt enhancement fails:

* Your original input will be restored
* An error notification will appear briefly (\~3 seconds)
* You can try enhancing again or proceed with your original prompt

Common reasons for enhancement failure:

* Network connectivity issues
* Service temporarily unavailable
* Input too short or unclear for enhancement

## Examples

### Before Enhancement

```
fix the login bug
```

### After Enhancement (Example)

```
Fix the authentication bug in the login flow. Please:

1. Review the current login implementation in `src/auth/login.ts`
2. Check for issues with token validation and session management
3. Examine error handling in the authentication middleware
4. Look at recent changes to the user authentication flow
5. Test the fix with both valid and invalid credentials
6. Ensure the fix follows our existing error handling patterns

Context: This appears to be related to the recent changes in the authentication system. Please maintain consistency with our existing auth patterns and ensure proper error messages are returned to the user.
```

## Integration with Other Features

The prompt enhancer works seamlessly with other Auggie CLI features:

* **History Navigation**: Enhanced prompts are added to your command history
* **Multi-line Input**: Works with both single-line and multi-line prompts
* **Conversation Context**: Uses your current conversation history for better enhancement
* **Workspace Awareness**: Leverages your current workspace and file context

## Tips for Best Results

1. **Start with clear intent** - Even simple prompts like "add tests" or "refactor this" work well
2. **Be specific about scope** - Mention specific files or components when relevant
3. **Use domain language** - Technical terms related to your project help the enhancer understand context
4. **Review enhanced prompts** - The enhancer provides a starting point; feel free to edit further
5. **Iterate if needed** - You can enhance the same prompt multiple times for different approaches

## Troubleshooting

**Ctrl+P doesn't work:**

* Ensure you have text in the input box
* Make sure you're in Normal mode (not in a menu or other mode)
* Check that you're using the correct key combination for your terminal

**Enhancement takes too long:**

* Press Esc to cancel and try again
* Check your network connection
* Try with a shorter or simpler prompt

**Enhanced prompt isn't helpful:**

* Edit the enhanced prompt manually
* Try starting with a more specific initial prompt
* Consider the context - the enhancer works best with workspace-relevant requests

## Related Features

* [Task Management](/cli/interactive/task-management) - Break down enhanced prompts into manageable tasks
* [Keyboard Shortcuts](/cli/interactive#shortcuts) - Learn other useful CLI shortcuts
* [Slash Commands](/cli/interactive#slash-commands) - Discover other interactive commands


# Using Task Manager
Source: https://docs.augmentcode.com/cli/interactive/task-management

Use /task to break down complex problems into manageable steps.

## About the Task Manager

The Auggie CLI task manager allows you to break down complex problems into discrete, manageable actions and track your progress through each step. It's particularly useful for automation workflows and keeping the agent focused on multi-step tasks.

The task manager maintains state per session and stores tasks under `~/.augment` for persistence across CLI sessions.

## Activating the Task Manager

Start Auggie in interactive mode and use the `/task` slash command:

```bash theme={null}
# Start Auggie in interactive mode
auggie

# Then type the slash command
/task
```

This opens the task manager interface, which takes over the main panel and provides a focused environment for task management.

### Alternative Access

You can also ask the agent to create a task list for you:

```bash theme={null}
auggie "Start a task list to implement user authentication"
```

The agent will automatically create and populate a task list when it encounters complex, multi-step problems.

## Task Manager Interface

The task manager provides a scrollable interface with comprehensive theming and visual feedback. When active, it replaces the main chat interface to provide a focused task management experience.

### Navigation and Interaction

Use your keyboard to interact with the Task Manager:

| Key        | Action                                                                                     |
| :--------- | :----------------------------------------------------------------------------------------- |
| `↑` / `↓`  | Navigate between tasks. The active task is highlighted with • next to the \[ ] Task Title. |
| `J` / `K`  | Alternative vim-style navigation (up/down)                                                 |
| `A`        | Add a new task                                                                             |
| `E`        | Edit the active task's title and description                                               |
| `D`        | Delete the active task                                                                     |
| `Spacebar` | Toggle task status                                                                         |
| `Esc`      | Dismiss the Task Manager                                                                   |

## Task Status Indicators

Tasks have three distinct states with corresponding visual status indicators:

* **\[ ] Not Started** - Empty checkbox, task has not been started
* **\[✓] Done** - Checkmark, task has been completed
* **\[-] Cancelled** - Dash, task has been cancelled or is no longer needed

## Working with Tasks

### Creating Tasks

**Manual Creation:**

1. Press `A` to add a new task
2. Enter the task title when prompted
3. Optionally add a description for more detailed context

**Agent-Generated Tasks:**
The agent automatically creates tasks inside the Task Manager when it encounters complex problems. You can also explicitly request task creation:

```bash theme={null}
"Create a task list to refactor the authentication system"
```

### Editing Tasks

1. Navigate to the desired task using arrow keys or J/K
2. Press `E` to edit
3. Modify the title first, then the description
4. The task manager provides inline editing with clear visual feedback

### Task Execution

**Manual Execution:**

* Use the task list as a checklist, manually updating status as you complete work
* Toggle status with `Spacebar` to track progress

**Agent Execution:**
You can ask the agent to work on specific tasks from the task manager:

```bash theme={null}
"Work on the first incomplete task in my task list"
"Complete the database migration task"
```

The agent will access your task list and update task status as it works.

## Advanced Features

### Task Hierarchy and Subtasks

The task manager supports nested task structures:

* Main tasks can have subtasks for complex workflows
* Subtasks are automatically indented and organized hierarchically
* Navigate through nested structures using standard navigation keys

### Persistence and Sessions

* Tasks are automatically saved per session under `~/.augment`
* Task lists persist across CLI restarts within the same session
* Each conversation session maintains its own task list

### Integration with Agent Workflow

The task manager is designed to work seamlessly with agent automation:

* **Keeps agents focused**: Provides clear structure for multi-step workflows
* **Progress tracking**: Agent can update task status as it completes work
* **Context preservation**: Tasks maintain context across long conversations
* **Automation-friendly**: Particularly useful for non-interactive automation workflows

## Use Cases and Examples

### Development Workflow

```bash theme={null}
auggie "Create a task list to implement user registration feature"
# Agent creates tasks like:
# [ ] Design user registration API endpoints
# [ ] Create user model and database schema
# [ ] Implement registration validation
# [ ] Add password hashing and security
# [ ] Write unit tests for registration
# [ ] Update API documentation
```

### Code Refactoring

```bash theme={null}
auggie "Break down refactoring the payment system into tasks"
# Agent creates structured tasks for complex refactoring
```

### Bug Investigation

```bash theme={null}
auggie "Create tasks to investigate and fix the login timeout issue"
# Agent creates systematic debugging tasks
```

## Tips for Effective Task Management

1. **Be Specific**: Create clear, actionable task descriptions
2. **Break Down Complex Work**: Use subtasks for multi-step processes
3. **Regular Updates**: Keep task status current for accurate progress tracking
4. **Agent Collaboration**: Let the agent help create and organize task structures
5. **Session Organization**: Use task lists to maintain focus across long sessions

## Troubleshooting

**Task Manager Won't Open:**

* Ensure you're in interactive mode (`auggie` without `-p` flag)
* Try typing `/task` exactly as shown
* Check that you're not in the middle of another operation

**Tasks Not Persisting:**

* Tasks are saved per session - starting a new session creates a new task list
* Check that `~/.augment` directory has proper write permissions

**Navigation Issues:**

* Use either arrow keys (↑/↓) or vim keys (J/K) for navigation
* Ensure the task manager has focus (not in edit mode)

## Related Features

* [Prompt Enhancer](/cli/interactive/prompt-enhancer) - Enhance task descriptions with context
* [Keyboard Shortcuts](/cli/interactive#shortcuts) - Learn other useful CLI shortcuts
* [Slash Commands](/cli/interactive#slash-commands) - Discover other interactive commands


# Introducing Auggie CLI
Source: https://docs.augmentcode.com/cli/overview

Auggie in the terminal gives you powerful agentic capabilities to analyze code, make changes, and execute tools in an interactive terminal and in your automated workflows.

## Introduction

<CardGroup>
  <Card title="GitHub Repository" icon="github" href="https://github.com/augmentcode/auggie">
    Report issues, leave feature requests and view custom workflows for Auggie CLI
  </Card>

  <Card title="NPM Package" icon="npm" href="https://www.npmjs.com/package/@augmentcode/auggie">
    Install Auggie CLI from npm
  </Card>
</CardGroup>

Auggie CLI takes the power of Augment's agent and context engine and puts it in your terminal, allowing you to use Augment anywhere your code goes. You can use Auggie in a standalone interactive terminal session alongside your favorite editor or in any part of your software development stack.

* Build features and debug issues with a standalone interactive agent.
* Get instant feedback, insight, and suggestions for your PRs and builds.
* Triage customer issues and alerts from your observability stack.

## Getting started

To use Auggie CLI in interactive mode or in your automations, you'll need:

* Node 22 or later installed
* A compatible shell like zsh, bash, fish

<Steps>
  <Step title="Install Auggie with npm">
    ```sh theme={null}
    npm install -g @augmentcode/auggie
    ```

    You can install Auggie CLI directly from npm anywhere you can run Node 22 or later. Auggie is currently in beta and may not run on all environments and terminal configurations.
  </Step>

  <Step title="Go to your project directory">
    ```sh theme={null}
    cd /path/to/your/project
    ```

    Your project will be indexed automatically when you run Auggie in your project directory. Augment's powerful context engine provides the best results when it has access to your project's codebase and any related repositories.
  </Step>

  <Step title="Login or sign up to Augment">
    ```sh theme={null}
    auggie login
    ```

    After installing, you'll have to log in to your Augment account. Run auggie login and follow the prompts.
  </Step>

  <Step title="Start using Auggie">
    ```sh theme={null}
    auggie "optional initial prompt"
    ```

    Just run `auggie` to start the interactive terminal. You can also pass a prompt as an argument and use `--print` to print the response to stdout instead of the interactive terminal–perfect for automation workflows.
  </Step>
</Steps>

## Using Auggie in interactive mode

Run `auggie` without any mode flags to get the full-screen terminal user interface with rich interactive features, real-time streaming of responses, and visual progress indicators. This mode shows all tool calls, results, and allows ongoing conversation through an intuitive interface.

Best for manual development work, exploration, and interactive problem-solving sessions where you want the full visual experience and plan to have back-and-forth conversations with the agent.

## Using Auggie in your automations

**Print Mode**: Add the `--print` flag (e.g., `auggie --print "your instruction"`) to execute the instruction once without the UI. This mode exits immediately without prompting for additional input. Perfect for automation, CI/CD pipelines, and background tasks where you want the agent to act without follow-up from a person.

**Quiet Mode**: `--quiet` flag (e.g., `auggie --print --quiet "your instruction"`) to tell the agent to only reply back with a final output. Ideal when you need to use the agent to provide structured data back without all the steps it took to get there. Provides a simple, clean response.


# Tool Permissions
Source: https://docs.augmentcode.com/cli/permissions

Control what tools Auggie CLI can execute with granular permission settings for security and compliance. Tool permissions configured will only work inside the CLI and not in the Augment code extension.

## About Tool Permissions

Auggie CLIs tool permission system provides fine-grained control over what actions the agent can perform in your environment. This security layer ensures that Auggie only executes approved operations, protecting your codebase and system from unintended changes.

Tool permissions are especially important when:

* Running Auggie in production environments
* Working with sensitive codebases
* Enforcing organizational security policies
* Using Auggie in automated workflows

## How Permissions Work

When Auggie attempts to use a tool, the permission system:

1. **Checks for matching rules** in your configuration
2. **Applies the first matching rule** based on tool name and optional patterns
3. **Rules are evaluated top-down** - first match wins
4. **Prompts for approval** when set to ask-user mode (interactive only)

### Permission Flow

```
Tool Request → Check Rules → Apply Permission → Execute/Deny → Log Decision
```

### Notes on Unmatched Tools

* Rules are evaluated in order from top to bottom
* The first matching rule determines the permission
* If no rules match, the CLI follows its implicit runtime behavior
* Configure explicit rules for all tools you want to control

## Configuration Files

Tool permissions are configured through the `settings.json` located in `~/.augment/settings.json` as personal settings that apply to all your projects.

## Basic Configuration

### Creating Rules

Rules define permissions for specific tools. Each rule can specify:

* **Tool name** - The specific tool to control
* **Permission type** - `allow`, `deny`, or `ask-user`
* **Optional patterns** - For shell commands, use regex matching

### Basic Rule Structure

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "launch-process", "permission": { "type": "deny" } },
    { "toolName": "view", "permission": { "type": "allow" } }
  ]
}
```

### Allow List Configuration

Create an explicit allow list by only allowing specific tools:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "view", "permission": { "type": "allow" } },
    { "toolName": "codebase-retrieval", "permission": { "type": "allow" } },
    { "toolName": "grep-search", "permission": { "type": "allow" } },
    { "toolName": "github-api", "permission": { "type": "allow" } }
  ]
}
```

<Note>This configuration explicitly allows only the listed tools. Tools not in this list will follow the CLI's implicit behavior.</Note>

### Block List Configuration

Create a block list by explicitly denying specific dangerous tools:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "remove-files", "permission": { "type": "deny" } },
    { "toolName": "kill-process", "permission": { "type": "deny" } },
    { "toolName": "launch-process", "shellInputRegex": "^(rm|sudo|shutdown|reboot)", "permission": { "type": "deny" } }
  ]
}
```

<Note>This configuration blocks specific dangerous operations. Tools not explicitly denied will follow the CLI's implicit behavior.</Note>

### Mix and Match Configuration

Combine allow, deny, and ask-user rules for fine-grained control:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "view", "permission": { "type": "allow" } },
    { "toolName": "codebase-retrieval", "permission": { "type": "allow" } },
    { "toolName": "grep-search", "permission": { "type": "allow" } },

    { "toolName": "str-replace-editor", "permission": { "type": "ask-user" } },
    { "toolName": "save-file", "permission": { "type": "ask-user" } },

    { "toolName": "launch-process", "shellInputRegex": "^(npm test|npm run lint|git status|git diff)", "permission": { "type": "allow" } },
    { "toolName": "launch-process", "shellInputRegex": "^(rm -rf|sudo|chmod 777)", "permission": { "type": "deny" } },
    { "toolName": "launch-process", "permission": { "type": "ask-user" } },

    { "toolName": "remove-files", "permission": { "type": "deny" } }
  ]
}
```

This configuration provides fine-grained control with different permission levels based on tool risk and usage patterns.

## Available Tools

### Process Management

| Tool             | Description                        |
| :--------------- | :--------------------------------- |
| `launch-process` | Execute shell commands and scripts |
| `read-process`   | Read output from running processes |
| `write-process`  | Send input to running processes    |
| `list-processes` | List all active processes          |
| `kill-process`   | Terminate running processes        |

### File Operations

| Tool                 | Description                         |
| :------------------- | :---------------------------------- |
| `view`               | Read file contents                  |
| `str-replace-editor` | Edit files with find/replace        |
| `save-file`          | Create or overwrite files           |
| `remove-files`       | Delete files from the filesystem    |
| `codebase-retrieval` | Search codebase with context engine |
| `grep-search`        | Search files with regex patterns    |

### External Services

| Tool         | Description                  |
| :----------- | :--------------------------- |
| `github-api` | GitHub API operations        |
| `linear`     | Linear issue tracking        |
| `notion`     | Notion workspace access      |
| `supabase`   | Supabase database operations |
| `web-search` | Web search queries           |
| `web-fetch`  | Fetch web page content       |

### MCP Server Tools

MCP tools follow the pattern `{tool-name}_{server-name}`:

* Example: `query_database-mcp`
* Truncated to 64 characters if longer
* Treated like any other tool for permissions

## Advanced Rules

### Shell Command Filtering

Control which shell commands can be executed using regex patterns:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "launch-process", "shellInputRegex": "^(ls|pwd|echo|cat|grep)\\s", "permission": { "type": "allow" } },
    { "toolName": "launch-process", "permission": { "type": "deny" } }
  ]
}
```

This configuration:

1. Allows only safe commands (ls, pwd, echo, cat, grep)
2. Denies all other shell commands
3. Rules are evaluated in order - first match wins

### Event-Based Permissions

Control when permission checks occur:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "github-api", "eventType": "tool-response", "permission": { "type": "allow" } }
  ]
}
```

**Event types:**

* **`tool-call`** (default) - Check before tool execution
* **`tool-response`** - Check after execution but before returning results to agent

## Interactive Approval

When using `ask-user` mode in interactive sessions, Auggie displays approval prompts:

```
🔒 Tool Approval Required
─────────────────────────
Tool: launch-process
Command: npm install express

[A]llow once  [D]eny  [Always allow]  [Never allow]
```

### Keyboard Shortcuts

| Key   | Action                      |
| :---- | :-------------------------- |
| `A`   | Allow this specific request |
| `D`   | Deny this specific request  |
| `Y`   | Always allow this tool      |
| `N`   | Never allow this tool       |
| `Esc` | Cancel and deny request     |

<Note>In non-interactive mode (--print), ask-user permissions default to deny for security.</Note>

## Common Configurations

### Read-Only Mode

Allow only read operations, perfect for code review and analysis:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "view", "permission": { "type": "allow" } },
    { "toolName": "codebase-retrieval", "permission": { "type": "allow" } },
    { "toolName": "grep-search", "permission": { "type": "allow" } },
    { "toolName": "web-search", "permission": { "type": "allow" } },
    { "toolName": "web-fetch", "permission": { "type": "allow" } },
    { "toolName": "str-replace-editor", "permission": { "type": "deny" } },
    { "toolName": "save-file", "permission": { "type": "deny" } },
    { "toolName": "remove-files", "permission": { "type": "deny" } },
    { "toolName": "launch-process", "permission": { "type": "deny" } }
  ]
}
```

### Development Mode

Add safety guards for potentially dangerous operations:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "remove-files", "permission": { "type": "ask-user" } },
    {
      "toolName": "launch-process",
      "shellInputRegex": "^(rm|sudo|chmod)\\s",
      "permission": { "type": "ask-user" }
    }
  ]
}
```

### CI/CD Pipeline

Restrictive settings for automated workflows:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "view", "permission": { "type": "allow" } },
    { "toolName": "str-replace-editor", "permission": { "type": "allow" } },
    { "toolName": "save-file", "permission": { "type": "allow" } },
    {
      "toolName": "launch-process",
      "shellInputRegex": "^(npm test|npm run lint|jest)\\s",
      "permission": { "type": "allow" }
    },
    { "toolName": "remove-files", "permission": { "type": "deny" } },
    { "toolName": "launch-process", "permission": { "type": "deny" } }
  ]
}
```

## Custom Policies

### Webhook Validation

Use external services to validate tool requests:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "github-api", "permission": { "type": "webhook-policy", "webhookUrl": "https://api.company.com/validate-tool" } }
  ]
}
```

The webhook receives a POST request with the following JSON payload:

```json theme={null}
{
  "tool-name": "github-api",
  "event-type": "tool-call",
  "details": { /* tool-specific data, see below */ },
  "timestamp": "2025-01-01T02:41:40.580Z"
}
```

**Payload fields:**

* **`tool-name`**: The name of the tool being invoked
* **`event-type`**: Either `"tool-call"` (before execution) or `"tool-response"` (after execution)
* **`details`**: Tool-specific data (for `tool-call`) or response data (for `tool-response`)
* **`timestamp`**: ISO 8601 timestamp of the request

**Details for `tool-call` event type** (varies by tool):

| Tool                 | Details Fields    |
| :------------------- | :---------------- |
| `launch-process`     | `cwd`, `command`  |
| `view`               | `path`            |
| `str-replace-editor` | `path`, `command` |
| `save-file`          | `path`            |
| `remove-files`       | `file_paths`      |
| `web-fetch`          | `url`             |

**Details for `tool-response` event type:**

```json theme={null}
{
  "text": "Tool output text",
  "isError": false
}
```

**Expected response:**

```json theme={null}
{
  "allow": true,
  "output": "Optional message to include in agent response"
}
```

### Script Validation

Use local scripts for complex validation logic:

```json theme={null}
{
  "toolPermissions": [
    { "toolName": "launch-process", "permission": { "type": "script-policy", "script": "/path/to/validate-command.sh" } }
  ]
}
```

The script receives the same JSON payload as webhooks via **stdin**:

```json theme={null}
{
  "tool-name": "launch-process",
  "event-type": "tool-call",
  "details": {
    "cwd": "/path/to/workspace",
    "command": "npm install express"
  },
  "timestamp": "2025-01-01T02:41:40.580Z"
}
```

**Script behavior:**

* **Exit code 0**: Allow the tool execution
* **Non-zero exit code**: Deny the tool execution
* **stdout/stderr**: Optional message included in the agent response

**Example script:**

```bash theme={null}
#!/bin/bash
# Read JSON payload from stdin
payload=$(cat)

# Extract command using jq
command=$(echo "$payload" | jq -r '.details.command // empty')

# Deny dangerous commands
if [[ "$command" == *"rm -rf"* ]] || [[ "$command" == *"sudo"* ]]; then
  echo "Dangerous command blocked: $command"
  exit 1
fi

# Allow all other commands
exit 0
```

## Best Practices

1. **Be Explicit**: Define clear rules for all tools you want to control
2. **Test Configurations**: Verify permissions work as expected before automation
3. **Log Decisions**: Monitor which tools are being allowed/denied for audit trails
4. **Regular Reviews**: Periodically review and update permission rules
5. **Order Matters**: Remember that rules are evaluated top-down, first match wins

## Troubleshooting

**Ask-User Mode in Automation:**

* Ask-user permissions automatically deny in non-interactive mode
* Use explicit allow/deny rules for automation scenarios
* Consider webhook or script policies for dynamic decisions

**MCP Tools Not Recognized:**

* Ensure MCP server name follows `{tool}_{server}` pattern
* Check for 64-character truncation on long names
* Verify MCP server is properly configured and running

## Security Considerations

* **Never commit sensitive webhook URLs** to version control
* **Use `.augment/settings.local.json`** for personal security overrides
* **Regularly audit** tool usage in production environments
* **Implement defense in depth** with multiple permission layers
* **Test permission changes** in isolated environments first

## Related Features

* [Authentication](/cli/setup-auggie/authentication) - Secure access to Auggie
* [Custom Rules](/cli/rules) - Project-specific guidelines
* [MCP Integrations](/cli/integrations) - External tool configuration
* [Automation](/cli/automation) - Using permissions in CI/CD


# CLI Flags and Options
Source: https://docs.augmentcode.com/cli/reference

A comprehensive reference for all command-line flags available in the Auggie CLI.

## CLI flags

| Command                          | Description                                                                                                                                                          |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auggie`                         | Start Auggie in interactive mode                                                                                                                                     |
| `auggie --print` (`-p`)          | Output simple text for one instruction and exit                                                                                                                      |
| `auggie --quiet`                 | Output only the final response for one instruction and exit                                                                                                          |
| `auggie --compact`               | Output tool calls, results, and final response as one line each and exit                                                                                             |
| `auggie -p --output-format json` | Output the response in structured JSON format. Must be used with `--print` (`-p`) mode. Useful for parsing Auggie's output programmatically in automation workflows. |

### Input

| Command                                            | Description                                        |
| :------------------------------------------------- | :------------------------------------------------- |
| `auggie "Fix the typescript errors"`               | Provide an initial instruction in interactive mode |
| `auggie --print "Summarize the staged changes"`    | Provide an instruction and exit                    |
| `cat file \| auggie --print "Summarize this data"` | Pipe content through stdin                         |
| `auggie --print "Summarize this data" < file.txt`  | Provide input from a file                          |
| `auggie --instruction "Fix the errors"`            | Provide an initial instruction in interactive mode |
| `auggie --instruction-file /path/to/file.txt`      | Provide an instruction by file in interactive mode |

### Custom Commands

| Command                         | Description                                                                  |
| :------------------------------ | :--------------------------------------------------------------------------- |
| `auggie command <command-name>` | Execute a custom command from `.augment/commands/` or `~/.augment/commands/` |

Custom commands are reusable instructions stored as markdown files. They can be placed in:

* `~/.augment/commands/<name>.md` - Global commands (user-wide)
* `./.augment/commands/<name>.md` - Project commands (workspace-specific)
* `~/.claude/commands/<name>.md` - Claude Code user commands
* `./.claude/commands/<name>.md` - Claude Code workspace commands

Commands are resolved in order of precedence, with Auggie-specific locations taking priority over Claude Code locations.

**Examples:**

```sh theme={null}
# Execute a custom deployment command
auggie command deploy-staging

# Execute a code review command
auggie command security-review

# List available commands (shown in help output)
auggie command help
```

See [Custom Commands](/cli/custom-commands) for detailed information on creating and managing custom commands.

### Sessions

| Command                          | Description                                       |
| :------------------------------- | :------------------------------------------------ |
| `auggie --continue` `(-c)`       | Resumes the previous conversation                 |
| `auggie --dont-save-session`     | Do not save the conversation to the local history |
| `auggie --delete-saved-sessions` | Delete all saved sessions from disk               |

### Configuration

| Command                                    | Description                                                               |
| :----------------------------------------- | :------------------------------------------------------------------------ |
| `auggie --workspace-root /path/to/project` | Specify the root of the workspace                                         |
| `auggie --rules /path/to/rules.md`         | Additional rules to append to workspace guidelines                        |
| `auggie --model "name"`                    | Select the model to use (accepts long or short names from the model list) |

<Note>Skills are loaded automatically from `.augment/skills/` and `.claude/skills/` directories in both your workspace and home directory. See [Skills](/cli/skills) for more information.</Note>

### Models

List out available models and their short names to be passed into the `--model` flag

| Command              | Description           |
| :------------------- | :-------------------- |
| `auggie models list` | List available models |

### Tools

Manage which tools are available to the agent. You can temporarily disable tools for a session or persistently manage them via settings.

| Command                            | Description                                                                              |
| :--------------------------------- | :--------------------------------------------------------------------------------------- |
| `auggie --remove-tool <tool-name>` | Remove a specific tool by name for the current session. Can be specified multiple times. |
| `auggie tools list`                | List all available tools and their current status                                        |
| `auggie tools remove <tool-name>`  | Persistently remove a tool by adding it to the `removedTools` list in settings.json      |
| `auggie tools add <tool-name>`     | Re-enable a previously removed tool by removing it from the `removedTools` list          |

**Examples:**

```sh theme={null}
# Disable the web-fetch tool for this session
auggie --remove-tool web-fetch

# Disable multiple tools for this session
auggie --remove-tool web-fetch --remove-tool web-search

# Persistently disable a tool
auggie tools remove launch-process

# Re-enable a previously disabled tool
auggie tools add launch-process

# See all tools and their status
auggie tools list
```

<Note>Command-line `--remove-tool` flags take precedence over settings. For fine-grained control over tool behavior (allow, deny, ask-user), see [Permissions](/cli/permissions).</Note>

### MCP and integrations

| Command                             | Description                                       |
| :---------------------------------- | :------------------------------------------------ |
| `auggie mcp add [options] <name>`   | Create or update a named MCP server configuration |
| `auggie mcp add-json <name> <json>` | Add an MCP server from JSON configuration         |
| `auggie mcp list`                   | Display all configured MCP servers                |
| `auggie mcp remove <name>`          | Remove a named MCP server configuration           |

| Command                                 | Description                        |
| :-------------------------------------- | :--------------------------------- |
| `auggie --mcp-config {key: value}`      | MCP configuration as a JSON string |
| `auggie --mcp-config /path/to/mcp.json` | MCP configuration from a JSON file |

<Note>You can define MCP servers persistently in the settings files: `~/.augment/settings.json`. Any `--mcp-config` flags are applied last and override settings.</Note>

For detailed usage examples, options, settings.json format, and precedence rules, see [Integrations and MCP](/cli/integrations#manage-mcp-servers-with-the-auggie-cli).

### MCP Server Mode

Run Auggie as an MCP server to expose the codebase-retrieval tool to external AI tools like Claude Code, Cursor, and others.

| Flag                   | Description                                                                                       |
| :--------------------- | :------------------------------------------------------------------------------------------------ |
| `--mcp`                | Run Auggie as an MCP tool server. Uses the current working directory as the workspace by default. |
| `--mcp-auto-workspace` | Enable automatic workspace discovery based on client requests (added in v0.14.0)                  |
| `-w /path/to/project`  | Specify a workspace to index                                                                      |

#### Automatic Workspace Discovery

The `--mcp-auto-workspace` flag enables dynamic workspace discovery in MCP mode. When enabled:

* The `codebase-retrieval` tool accepts a `directory_path` parameter to specify which workspace to search
* Workspaces are indexed on-demand when first accessed
* Multiple workspaces can be searched within a single MCP server session

This is useful when the MCP client (e.g., Claude Code) needs to work with multiple projects or when the workspace isn't known at startup time.

You can combine `--mcp-auto-workspace` with `-w` to pre-index a primary workspace at startup while still allowing dynamic discovery of additional workspaces. This is useful for large workspaces that take time to index, or to reduce latency on the first query to your main project.

**Examples:**

```bash theme={null}
# MCP server with auto-discovery (recommended)
auggie --mcp --mcp-auto-workspace

# Pre-index a workspace, allow dynamic discovery of others
auggie --mcp --mcp-auto-workspace -w /path/to/primary/project

# Use only a single workspace path
auggie --mcp -w /path/to/project

# Use current working directory as the workspace
auggie --mcp
```

<Note>When using `--mcp-auto-workspace`, the first query to a new workspace may take longer as the workspace is indexed. Subsequent queries to the same workspace will be fast.</Note>

### Authentication

| Command               | Description                                  |
| :-------------------- | :------------------------------------------- |
| `auggie login`        | Login to Augment and store the token locally |
| `auggie logout`       | Remove the locally stored token              |
| `auggie tokens print` | Print the locally stored token               |

### Additional commands

| Command            | Description  |
| :----------------- | :----------- |
| `auggie --help`    | Show help    |
| `auggie --version` | Show version |

## Environment Variables

| Variable                      | Description                   |
| ----------------------------- | ----------------------------- |
| `AUGMENT_SESSION_AUTH`        | Authentication JSON.          |
| `AUGMENT_API_URL`             | Backend API endpoint          |
| `AUGMENT_API_TOKEN`           | Authentication token          |
| `GITHUB_API_TOKEN`            | GitHub API token              |
| `AUGMENT_DISABLE_AUTO_UPDATE` | Disable automatic CLI updates |

### Shell Environment

When Auggie executes shell commands using the `launch-process` tool, it sets the following environment variable:

| Variable        | Description                                                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `AUGMENT_AGENT` | Set to `1` when a command is executed by Auggie. Scripts can check for this variable to detect if they are being run by the agent. |

**Example usage in a script:**

```sh theme={null}
if [ -n "$AUGMENT_AGENT" ]; then
  echo "Running inside Auggie"
  # Adjust behavior for agent execution
fi
```

## See Also

* [Custom Rules and Guidelines](/cli/rules) - Configure custom rules for project-specific guidance
* [Skills](/cli/skills) - Extend capabilities with specialized domain knowledge
* [Custom Commands](/cli/custom-commands) - Create reusable command templates
* [Permissions](/cli/permissions) - Configure tool permissions and security
* [Integrations](/cli/integrations) - Connect external tools and services


# Rules & Guidelines
Source: https://docs.augmentcode.com/cli/rules

Configure custom rules and guidelines to provide context-aware assistance in Auggie CLI.

## Overview

Auggie automatically loads custom rules and guidelines from several file locations to provide context-aware assistance. These files help Auggie understand your project's conventions, coding standards, and preferences.

<Note>The Auggie CLI uses the same rules system as the VSCode and JetBrains IDE extensions. For more information on IDE specific features like user guidelines, see [Rules & Guidelines for Agent and Chat](/setup-augment/guidelines).</Note>

<Note>Looking for specialized domain knowledge? Check out [Skills](/cli/skills) - a standardized way to provide framework-specific guidance, tool usage patterns, and workflow procedures following the agentskills.io specification.</Note>

## Supported Rules Files

Auggie looks for rules files in the following order of precedence:

1. **Custom rules file** (via `--rules` flag): `/path/to/custom-rules.md`
2. **CLAUDE.md**: Compatible with Claude Code and other AI tools
3. **AGENTS.md**: Compatible with Cursor and other AI development tools
4. **Workspace guidelines**: `<workspace_root>/.augment/guidelines.md` (legacy format)
5. **Workspace rules folder**: `<workspace_root>/.augment/rules/` - Recursively searches .md files in the workspace
6. **User rules folder**: `~/.augment/rules/` - Recursively searches .md files for user-wide rules

### User Rules vs Workspace Rules

Rules can be defined at two levels:

| Scope     | Location                           | Availability                        |
| :-------- | :--------------------------------- | :---------------------------------- |
| User      | `~/.augment/rules/`                | Available in all workspaces         |
| Workspace | `<workspace_root>/.augment/rules/` | Available in current workspace only |

**User rules** are stored in your home directory and apply to all projects. Use these for personal preferences, coding style guidelines, or conventions you want to follow across all your work. User rules are always treated as `always_apply` type and are automatically included in every prompt regardless of any frontmatter configuration.

**Workspace rules** are stored in the project repository and apply only to that specific project. Use these for project-specific guidelines that should be shared with your team via version control.

## Rules File Format

Rules files should be written in Markdown format with natural language instructions. Here's the recommended structure:

```markdown theme={null}
# Project Guidelines

## Code Style
- Use TypeScript for all new JavaScript files
- Follow the existing naming conventions in the codebase
- Add JSDoc comments for all public functions and classes

## Architecture
- Follow the MVC pattern established in the codebase
- Place business logic in service classes
- Keep controllers thin and focused on request/response handling

## Testing
- Write unit tests for all new functions
- Maintain test coverage above 80%
- Use Jest for testing framework

## Dependencies
- Prefer built-in Node.js modules when possible
- Use npm for package management
- Pin exact versions in package.json for production dependencies
```

## Frontmatter Configuration for Rules

Rules files in the `<workspace_root>/.augment/rules/` (workspace) directory support frontmatter to configure their behavior. Use YAML frontmatter at the beginning of your rule file to specify how the rule should be applied:

<Note>User rules in `~/.augment/rules/` are always treated as `always_apply` and do not support other frontmatter types. Frontmatter configuration only affects workspace rules.</Note>

| Frontmatter Field | Purpose                                                                       | Options                           | Default        |
| :---------------- | :---------------------------------------------------------------------------- | :-------------------------------- | :------------- |
| `type`            | Controls when the rule is applied                                             | `always_apply`, `agent_requested` | `always_apply` |
| `description`     | Brief description of the rule's purpose (required for `agent_requested` type) | Any text                          | None           |

**Rule Types:**

* **`always_apply`**: Rule contents are automatically included in every user prompt
* **`agent_requested`**: Rule is automatically detected and attached based on the description field when relevant

<Note>Manual rules are not yet supported in the CLI. In the CLI, workspace rules in `<workspace_root>/.augment/rules/` are currently treated as `always_apply` rules and automatically included. User rules in `~/.augment/rules/` are always `always_apply`. The `manual` type only works in the IDE extensions where you can use @ mentions to selectively attach rules.</Note>

Use `agent_requested` (also called `auto` in IDE extensions) over `always_apply` if you want to optimize context usage. For these rules, the agent will determine the rule is relevant to your current task, ensuring specialized guidelines are available when needed.

**Example with frontmatter:**

```markdown theme={null}
---
type: always_apply
---

# TypeScript Guidelines

- Use strict mode in all TypeScript files
- Define explicit return types for all functions
- Avoid using `any` type unless absolutely necessary
```

**Agent-requested example:**

```markdown theme={null}
---
type: agent_requested
description: React component development patterns and best practices
---

# React Component Guidelines

- Use functional components with hooks
- Implement proper TypeScript interfaces for props
- Follow the established folder structure in src/components/
```

## Hierarchical Rules

In addition to workspace-level rules, the agent supports **hierarchical rules** through `AGENTS.md` and `CLAUDE.md` files placed in subdirectories. When working on files in a subdirectory, Augment automatically discovers and applies rule files from that directory and all parent directories.

### How Hierarchical Rules Work

1. When you work on a file, Augment looks for `AGENTS.md` and `CLAUDE.md` in the file's directory
2. It then walks up the directory tree, checking each parent directory for these files
3. All discovered rules are included in the context for that work session
4. The search stops at the workspace root (since workspace root rules are already loaded separately)

### Example Directory Structure

```
my-project/
  AGENTS.md                  <- Always included (workspace root)
  src/
    AGENTS.md                <- Included when working in src/ or subdirectories
    frontend/
      AGENTS.md              <- Included when working in src/frontend/
      App.tsx
    backend/
      AGENTS.md              <- Included when working in src/backend/
      server.ts
  tests/
    AGENTS.md                <- Only included when working in tests/
```

When working on `src/frontend/App.tsx`:

* `src/frontend/AGENTS.md` is loaded (current directory)
* `src/AGENTS.md` is loaded (parent directory)
* `AGENTS.md` at workspace root is loaded via standard rules
* `src/backend/AGENTS.md` and `tests/AGENTS.md` are **not** loaded (different branches)

### Use Cases for Hierarchical Rules

* **Framework-specific guidelines**: Place React-specific rules in your frontend directory and Node.js rules in your backend directory
* **Module-specific conventions**: Define API design patterns in your `api/` directory
* **Test-specific rules**: Add testing conventions that only apply when writing tests
* **Team boundaries**: Different teams can maintain their own coding standards in their directories

### Important Notes

* Only `AGENTS.md` and `CLAUDE.md` files are discovered hierarchically
* Files in `.augment/rules/` are only loaded from the workspace root, not from subdirectories
* Rules are cached per conversation session to avoid duplicate inclusion
* Hierarchical rules are combined with workspace and user rules

## Best Practices for Rules Files

1. **Be Specific**: Provide clear, actionable guidelines rather than vague suggestions
2. **Use Examples**: Include code examples when describing patterns or conventions
3. **Keep Updated**: Regularly review and update rules as your project evolves
4. **Be Concise**: Focus on the most important guidelines to avoid overwhelming the AI
5. **Test Guidelines**: Verify that Auggie follows your rules by testing with sample requests

## Command-Line Flag

You can specify a custom rules file when starting Auggie:

```bash theme={null}
auggie --rules /path/to/custom-rules.md
```

This will append the specified rules to any workspace guidelines that are automatically loaded.

## See Also

* [Skills](/cli/skills) - Extend capabilities with specialized domain knowledge
* [Rules & Guidelines for Agent and Chat](/setup-augment/guidelines) - Configure rules in VSCode and JetBrains IDEs
* [CLI Reference](/cli/reference) - Complete command-line reference
* [Workspace Context](/cli/setup-auggie/workspace-context) - Understanding workspace configuration
* [Custom Commands](/cli/custom-commands) - Create reusable command templates


# Auggie SDK
Source: https://docs.augmentcode.com/cli/sdk

Build custom integrations and agents using the Auggie SDK.

<CardGroup>
  <Card title="TypeScript SDK" icon="js" href="/cli/sdk-typescript">
    Build Node.js and TypeScript applications with the Auggie SDK
  </Card>

  <Card title="Python SDK" icon="python" href="/cli/sdk-python">
    Build Python applications with the Auggie SDK
  </Card>
</CardGroup>

## Installation

<CodeGroup>
  ```sh TypeScript theme={null}
  npm install @augmentcode/auggie-sdk
  ```

  ```sh Python theme={null}
  pip install auggie-sdk
  ```
</CodeGroup>

## Authentication

The Auggie SDK supports multiple authentication methods:

1. **Passing API Key Directly (Recommended)** - Provide `apiKey` parameter when initializing
2. **Using Environment Variables** - Set `AUGMENT_API_TOKEN` and `AUGMENT_API_URL` environment variables
3. **Using `settings.json`** - Store credentials in `settings.json` file

### Finding Your API keys

<Note>
  **Coming Soon:** Service accounts and team-level tokens will be available for production deployments and CI/CD environments.
</Note>

Running `auggie token print` will print your API keys:

```json theme={null}
{
  "accessToken": "ABC-XYZ-123", // Use as apiKey
  "tenantURL": "https://...",   // Use as apiUrl
  ...
}
```

## Quick Start

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { Auggie } from "@augmentcode/auggie-sdk";

  const client = await Auggie.create({ model: "sonnet4.5" });
  const response = await client.prompt("What files are in the current directory?");
  console.log(response);
  await client.close();
  ```

  ```python Python theme={null}
  from auggie_sdk import Auggie

  agent = Auggie(model="sonnet4.5")
  result = agent.run("What is 2 + 2?", return_type=int)
  print(result)  # 4
  ```
</CodeGroup>

## Key Features

Both SDKs provide:

* **High-level API** - Simple interface for common tasks
* **Multiple Output Modes** - String responses, typed returns, streaming, and more
* **Codebase Awareness** - Automatic indexing and context from your workspace
* **Custom Tools** - Extend Auggie with your own tools and integrations

## TypeScript-Specific Features

The TypeScript SDK also includes:

* **AI SDK Provider** - Use Augment as a language model provider with [Vercel's AI SDK](https://sdk.vercel.ai/docs)
  * Compatible with `generateText`, `streamText`, and other AI SDK functions
  * Full support for tool calling (function calling)
  * Works with API credentials only (no local Auggie installation needed)
  * See the [TypeScript SDK documentation](/cli/sdk-typescript#ai-sdk-provider-vercel-ai-sdk) for details


# Python SDK
Source: https://docs.augmentcode.com/cli/sdk-python

Build custom integrations and agents using the Auggie Python SDK.

## About

The Auggie Python SDK provides a programmatic interface to Auggie for building custom integrations and agents in Python applications.

## Installation

```sh theme={null}
pip install auggie-sdk
```

## Usage

### Basic Initialization

```python theme={null}
from auggie_sdk import Auggie

# Simple initialization
agent = Auggie(model="sonnet4.5")

# Run a task
result = agent.run("What is 2 + 2?", return_type=int)
print(result)  # 4
```

### Full Configuration

```python theme={null}
from auggie_sdk import Auggie
from auggie_sdk.acp import AgentEventListener

# Optional: Create a custom event listener
class MyListener(AgentEventListener):
    def on_agent_message_chunk(self, text: str):
        print(text, end="", flush=True)

agent = Auggie(
    # Working directory for the agent (default: current directory)
    workspace_root="/path/to/workspace",

    # Model to use: "haiku4.5" | "sonnet4.5" | "sonnet4" | "gpt5"
    model="sonnet4.5",

    # Event listener for real-time updates (optional)
    listener=MyListener(),

    # Allow codebase indexing (default: True)
    allow_indexing=True,

    # Default timeout in seconds (default: 300)
    timeout=600,

    # API key for authentication (optional, sets AUGMENT_API_TOKEN)
    api_key="your-api-key",

    # API URL (optional, sets AUGMENT_API_URL)
    api_url="https://api.augmentcode.com",

    # Rule file paths (optional)
    rules=["/path/to/rules.md"],

    # Additional CLI arguments (optional)
    cli_args=["--quiet", "--max-turns", "10"]
)

# Use the agent
result = agent.run("Your question here", return_type=str)
print(result)
```

### Custom CLI Arguments

The `cli_args` parameter allows you to pass additional command-line arguments to the Auggie CLI when spawning the agent process. This is useful for passing custom or experimental CLI flags that aren't exposed as dedicated parameters.

```python theme={null}
from auggie_sdk import Auggie

# Example 1: Limit agent turns and reduce output
agent = Auggie(
    cli_args=["--quiet", "--max-turns", "10"]
)

# Example 2: Configure retry behavior and shell
agent = Auggie(
    cli_args=["--retry-timeout", "60", "--shell", "bash"]
)

# Example 3: Add custom rules and startup script
agent = Auggie(
    cli_args=[
        "--rules", "/path/to/custom-rules.md",
        "--startup-script", "export MY_VAR=value"
    ]
)

# Example 4: Configure tool permissions
agent = Auggie(
    cli_args=[
        "--permission", "web-search:allow",
        "--permission", "launch-process:ask-user"
    ]
)
```

**Common CLI arguments:**

* `--quiet` - Only show final assistant message
* `--max-turns <n>` - Limit the number of agentic turns
* `--retry-timeout <sec>` - Timeout for rate-limit retries (seconds)
* `--shell <name>` - Select shell: bash | zsh | fish | powershell
* `--rules <path>` - Additional rules file (repeatable)
* `--permission <rule>` - Set tool permissions with 'tool-name:policy' format
* `--startup-script <script>` - Inline startup script to run before each command

The `cli_args` are appended after all other CLI arguments, giving you flexibility to pass any additional flags or options supported by the underlying Auggie CLI. See the [CLI reference](/cli/reference) for available command-line options.

## Output Modes

The Python SDK supports multiple output modes to fit different use cases:

### Typed Returns

Specify the exact type you expect, and the SDK ensures the agent returns data in that format:

```python theme={null}
from auggie_sdk import Auggie

agent = Auggie()

# Get an integer
result = agent.run("What is 15 + 27?", return_type=int)
print(result)  # 42

# Get a dictionary
weather = agent.run(
    "Get weather info for Tokyo",
    return_type=dict
)

# Get a list
files = agent.run(
    "List all Python files",
    return_type=list
)
```

### Automatic Type Inference

When no `return_type` is specified, the agent automatically infers the best type:

```python theme={null}
result, inferred_type = agent.run("What is 15 + 27?")
print(f"Result: {result} (type: {inferred_type.__name__})")
# Result: 42 (type: int)
```

### Structured Data with Dataclasses

Return complex structured data using Python dataclasses:

```python theme={null}
from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    id: int
    description: str
    is_done: bool

# Get a single object
task = agent.run(
    "Create a sample task for 'Buy groceries'",
    return_type=Task
)

# Get a list of objects
tasks = agent.run(
    "Create 3 sample tasks for a weekend to-do list",
    return_type=List[Task]
)
```

### Streaming Mode

Listen to real-time updates using an event listener:

```python theme={null}
from auggie_sdk import Auggie
from auggie_sdk.acp import AgentEventListener

class MyListener(AgentEventListener):
    def on_agent_message_chunk(self, text: str):
        """Called when agent sends response chunks (streaming)."""
        print(text, end="", flush=True)

    def on_tool_call(self, tool_call_id, title, kind=None, status=None):
        """Called when agent makes a tool call."""
        print(f"\n🔧 Using tool: {title}")

agent = Auggie(listener=MyListener())
result = agent.run("Your question here")
```

**Supported return types:** `int`, `float`, `str`, `bool`, `list`, `dict`, `List[T]`, `Dict[K, V]`, `dataclasses`, `Enum`

## Custom Functions

The Python SDK supports **custom function calling**, allowing you to provide Python functions that the agent can intelligently call during execution. This enables the agent to interact with external systems, perform calculations, fetch data, and more.

### Creating Custom Functions

Define Python functions with type hints and docstrings. The agent will automatically understand how to use them:

```python theme={null}
from auggie_sdk import Auggie
import datetime


def get_current_weather(location: str, unit: str = "celsius") -> dict:
    """
    Gets the weather for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA
        unit: Temperature unit ('celsius' or 'fahrenheit')
    """
    # In a real app, you'd call a weather API here
    return {"temp": 72, "unit": unit, "forecast": "sunny"}


def get_time() -> str:
    """Returns the current time."""
    return datetime.datetime.now().strftime("%H:%M")


agent = Auggie()

# The agent will call the appropriate function(s) to answer the question
response = agent.run(
    "What's the weather like in NYC right now, and what time is it there?",
    functions=[get_current_weather, get_time],
)
print(response)
```

### Function Requirements

For functions to work properly with the agent:

1. **Type Hints Required**: All parameters must have type annotations
2. **Docstrings Required**: Function must have a docstring with:
   * Function description (first paragraph)
   * Parameter descriptions in the `Args:` section
3. **JSON-Serializable**: Arguments and return values must be JSON-serializable
4. **Keyword Arguments**: Functions must accept keyword arguments

### Example with Multiple Functions

```python theme={null}
from auggie_sdk import Auggie


def add_numbers(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number
    """
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together.

    Args:
        a: First number
        b: Second number
    """
    return a * b


agent = Auggie()

result = agent.run(
    "What is (15 + 27) multiplied by 3?",
    return_type=int,
    functions=[add_numbers, multiply_numbers],
)
print(result)  # 126
```

### How It Works

1. Function schemas are automatically generated from type hints and docstrings
2. The agent receives the instruction and available functions
3. The agent intelligently decides when to call functions
4. The SDK executes the functions and sends results back to the agent
5. The agent continues processing and can call more functions if needed
6. Final response is returned according to `return_type`

<Note>
  **Function Calling Limits**: Function calling is limited to 5 rounds to prevent infinite loops.
</Note>

## See Also

* [Python SDK on PyPI](https://pypi.org/project/auggie-sdk)
* [TypeScript SDK](/cli/sdk-typescript)
* [ACP Clients](/cli/acp/clients)


# TypeScript SDK
Source: https://docs.augmentcode.com/cli/sdk-typescript

Build custom integrations and agents using the Auggie TypeScript SDK.

## About

The Auggie TypeScript SDK provides a programmatic interface to Auggie for building custom integrations and agents in Node.js and TypeScript applications.

The SDK offers two main interfaces:

1. **Agent Interaction (ACP)** - Launch and communicate with a local Auggie agent process
2. **AI SDK Provider** - Use Augment as a language model provider with Vercel's AI SDK (API-only, no local installation required)

## Installation

```sh theme={null}
npm install @augmentcode/auggie-sdk
```

## Agent Interaction (ACP)

**⚠️ Requires Local Auggie Installation**

The Agent Interaction interface allows you to launch Auggie in ACP mode and communicate bidirectionally. This requires a local Auggie installation.

## Usage

### Basic Initialization

```typescript theme={null}
import { Auggie } from "@augmentcode/auggie-sdk";

// Simple initialization
const client = await Auggie.create({
  model: "sonnet4.5"
});

// Send a prompt
const response = await client.prompt("What files are in the current directory?");
console.log(response);

// Close the connection
await client.close();
```

### Full Configuration

```typescript theme={null}
import { Auggie } from "@augmentcode/auggie-sdk";

const client = await Auggie.create({
  // Path to Auggie executable (default: "auggie")
  auggiePath: "/path/to/auggie",

  // Working directory for the Auggie process (default: process.cwd())
  workspaceRoot: "/path/to/workspace",

  // Eg: "haiku4.5" | "gpt-5" | "sonnet4.5" | "sonnet4"
  model: "sonnet4.5",

  // Allow codebase indexing (default: true)
  allowIndexing: true,

  // API key for authentication (optional, sets AUGMENT_API_TOKEN)
  apiKey: "your-api-key",

  // API URL (optional, sets AUGMENT_API_URL)
  apiUrl: "https://api.augmentcode.com",

  // Custom tools to provide to Auggie (optional)
  tools: {
    // Your custom tools here
  },

  // Rule file paths (optional)
  rules: ["/path/to/rules.md"],

  // Additional CLI arguments to pass to the Auggie process (optional)
  cliArgs: ["--quiet", "--max-turns=10"]
});

// Use the client
const response = await client.prompt("Your question here");
console.log(response);

await client.close();
```

### Advanced CLI Arguments

The `cliArgs` option allows you to pass additional command-line arguments directly to the Auggie CLI process. These arguments are appended after all SDK-generated flags, allowing you to use advanced configurations or experimental flags not exposed through standard SDK options.

```typescript theme={null}
import { Auggie } from "@augmentcode/auggie-sdk";

// Pass custom CLI flags
const client = await Auggie.create({
  model: "sonnet4.5",
  cliArgs: ["--quiet", "--max-turns=10"]
});

// Arguments can use either format:
// 1. Separate flag and value: ["--retry-timeout", "60"]
// 2. Combined with equals: ["--retry-timeout=60"]
const client2 = await Auggie.create({
  model: "sonnet4.5",
  cliArgs: ["--shell=bash", "--allow-indexing"]
});
```

**Note:** Since `cliArgs` are appended after SDK-generated flags, they can override default values when the CLI uses a last-value-wins strategy. Refer to `auggie --help` for available CLI flags.

## Output Modes

The TypeScript SDK supports multiple output modes to fit different use cases:

### String Response (Default)

By default, the SDK returns the complete agent response as a string:

```typescript theme={null}
const client = await Auggie.create({ model: "sonnet4.5" });
const response = await client.prompt("What files are in the current directory?");
console.log(response); // Full response as string
```

### Answer-Only Mode

Get only the final answer after all tool calls complete, excluding intermediate reasoning:

```typescript theme={null}
const finalAnswer = await client.prompt(
  "List all TypeScript files in this project",
  { isAnswerOnly: true }
);
// Returns only the final response after tool execution
```

### Streaming Mode

Listen to real-time updates as the agent processes your request:

```typescript theme={null}
client.onSessionUpdate((event) => {
  switch (event.update.sessionUpdate) {
    case "agent_message_chunk":
      if (event.update.content.type === "text") {
        process.stdout.write(event.update.content.text);
      }
      break;
    case "tool_call":
      console.log(`\nTool: ${event.update.title}`);
      break;
    case "tool_call_update":
      console.log("Output:", event.update.rawOutput);
      break;
  }
});

const response = await client.prompt("Your question here");
```

## Custom Tools

The TypeScript SDK supports **ai-sdk compatible tools**, allowing you to extend Auggie with custom functionality. You can provide tools that the agent can call during execution.

### Creating a Custom Tool

Here's an example of a custom weather tool:

```typescript theme={null}
import { Auggie } from "@augmentcode/auggie-sdk";
import { tool } from "ai";
import { z } from "zod";

// Define a custom tool
const weather_tool = tool({
  name: "get_weather",
  description: "Get the weather in a location",
  inputSchema: z.object({
    location: z.string().describe("The location to get the weather for"),
  }),
  execute: ({ location }) => {
    console.log(`\n Weather tool called for location: ${location}`);
    return `The weather in ${location} is sunny.`;
  },
});

// Initialize Auggie with the custom tool
const client = await Auggie.create({
  model: "sonnet4.5",
  tools: {
    get_weather: weather_tool,
  },
});

// The agent can now use the weather tool
const response = await client.prompt("What's the weather like in San Francisco?");
console.log(response);

await client.close();
```

### Key Points

* **ai-sdk Compatible**: Tools follow the [Vercel AI SDK](https://sdk.vercel.ai/docs) tool format
* **Zod Schemas**: Use Zod for input validation and type safety
* **Automatic Discovery**: The agent automatically discovers and uses available tools when relevant
* **Multiple Tools**: Pass multiple tools in the `tools` object

### Tool Structure

Each tool requires:

* `name` - Unique identifier for the tool
* `description` - Clear description of what the tool does (helps the agent decide when to use it)
* `inputSchema` - Zod schema defining the tool's input parameters
* `execute` - Function that implements the tool's logic

## AI SDK Provider (Vercel AI SDK)

**✅ No Local Auggie Required - API Only**

The AI SDK Provider allows you to use Augment as a language model provider with [Vercel's AI SDK](https://sdk.vercel.ai/docs). This interface only requires API credentials and works without a local Auggie installation.

### Features

* Compatible with `generateText`, `streamText`, and other AI SDK functions
* Full support for tool calling (function calling) with automatic execution
* Multi-turn conversations with context retention
* Streaming responses for real-time output
* Works with API credentials only (no local Auggie installation needed)

### Quick Start

```typescript theme={null}
import { AugmentLanguageModel, resolveAugmentCredentials } from "@augmentcode/auggie-sdk";
import { generateText } from "ai";

// Resolve credentials from environment or ~/.augment/session.json
const credentials = await resolveAugmentCredentials();

// Create the Augment language model
const model = new AugmentLanguageModel("claude-sonnet-4-5", credentials);

// Use with AI SDK functions
const { text } = await generateText({
  model,
  prompt: "Explain TypeScript in one sentence.",
});

console.log(text);
```

### Streaming Responses

```typescript theme={null}
import { streamText } from "ai";

const { textStream } = await streamText({
  model,
  prompt: "Write a haiku about coding.",
});

for await (const chunk of textStream) {
  process.stdout.write(chunk);
}
```

### Tool Calling

```typescript theme={null}
import { generateText, tool, stepCountIs } from "ai";
import { z } from "zod";

const weatherTool = tool({
  description: "Get the weather in a location",
  inputSchema: z.object({
    location: z.string().describe("The location to get the weather for"),
  }),
  execute: async ({ location }) => {
    return `The weather in ${location} is sunny.`;
  },
});

const { text } = await generateText({
  model,
  tools: { weather: weatherTool },
  stopWhen: stepCountIs(5),
  prompt: "What's the weather like in San Francisco?",
});
```

### Multi-turn Conversations

```typescript theme={null}
const messages = [
  { role: "user" as const, content: "What's 2+2?" },
];

const response1 = await generateText({ model, messages });
messages.push({ role: "assistant" as const, content: response1.text });
messages.push({ role: "user" as const, content: "Multiply that by 3" });

const response2 = await generateText({ model, messages });
console.log(response2.text); // "12"
```

### Authentication

The AI SDK Provider uses the same authentication methods as the rest of the SDK:

1. **Environment Variables** - Set `AUGMENT_API_TOKEN` and `AUGMENT_API_URL`
2. **Session File** - Use credentials from `~/.augment/session.json` (created by `auggie login`)
3. **Direct Credentials** - Pass credentials directly to `AugmentLanguageModel`

```typescript theme={null}
// Option 1: Auto-resolve from environment or session file
const credentials = await resolveAugmentCredentials();
const model = new AugmentLanguageModel("claude-sonnet-4-5", credentials);

// Option 2: Pass credentials directly
const model = new AugmentLanguageModel("claude-sonnet-4-5", {
  apiKey: "your-api-key",
  apiUrl: "https://api.augmentcode.com",
});
```


# Login and authentication
Source: https://docs.augmentcode.com/cli/setup-auggie/authentication

You will need an active account and valid session token to use Auggie CLI which you can get by following the instructions below.

## About authentication

Before you can use Auggie, you will need to login to create a session token that can be used by Auggie in both interactive and automation modes.

<Note>Augment authentication tokens are secrets and should be protected with the same level of security you'd use for any sensitive credential. Tokens are tied to the user who logged in, not to your team or enterprise account, so each user has a unique augment token.</Note>

## Logging in

You can login by running the following command and following the prompts.

```sh theme={null}
auggie login
```

## Logging out

You can logout by running the following command. This will remove the local token from your machine and you will need to login again to use Auggie.

```sh theme={null}
auggie logout
```

## Getting your token

For automation, you will need to provide your token each time you run Auggie. After you have logged in above, you can get your token by running the following command.

```sh theme={null}
auggie tokens print
```

## Using your token

After you have your token, you can pass it to Auggie through a number of methods depending on your use case and environment.

### Environment variables

You can set the `AUGMENT_SESSION_AUTH` environment variable to your token before running Auggie. Pass it before you run the command, add it to your environment, or add it to your shell's rc file to persist it.

```sh theme={null}
AUGMENT_SESSION_AUTH='<token>'
```

### Token file

You can store the token as plaintext in a file and then use the `--augment-token-file` flag to pass it to Auggie. We do not recommend checking your token into version control.

```sh theme={null}
auggie --augment-token-file /path/to/token
```

## Revoking your tokens

You can expire all the tokens for the current logged in user by running the following command. Using `--logout` will only remove the local token from your machine.

```sh theme={null}
auggie tokens revoke 
```


# Install Auggie CLI
Source: https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli

Install Auggie to get agentic coding capabilities in your terminal, on your server, or anywhere your code runs.

```sh theme={null}
npm install -g @augmentcode/auggie
```

# About installing Auggie

Installing Auggie CLI is easy and will take you less than a minute. You can install Auggie CLI directly from npm anywhere you can run Node 22 or later. Many systems do not ship with the latest version of Node.js, so you may need to upgrade Node to use Auggie.

Auggie is currently in beta and may not run on all environments and terminal configurations.

## Automatic Updates

Auggie CLI automatically updates itself when running in interactive mode to ensure you always have the latest features and bug fixes. This feature is enabled by default and works seamlessly in the background. You can [disable automatic updates](/cli/reference#environment-variables).

## System requirements

* [**Node.js 22+**](https://nodejs.org/en/download/)
* **Platforms**: MacOS, Windows WSL, Linux
* **Shells**: zsh, bash, fish

### Interactive mode

Using Auggie in interactive mode requires a terminal that supports ANSI escape codes. We recommend using Ghostty, iTerm2, MacOS Terminal, Windows Terminal, Alacritty, Kitty, and other modern terminals.

If you are connecting to your shell over SSH or through tmux you may need to adjust your terminal settings or configuration to enable proper color support, font rendering, and interactivity.


# Workspace context
Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-context

Auggie will automatically index the current working directory or directory you specify to give Augment a full view of your system.

## About Workspace Context

Augment is powered by its deep understanding of your code. Your codebase will be automatically indexed when you run `auggie` from a git directory or you can specify a directory to index. If you run Auggie from a non-git directory, a temporary workspace will be created for you.

## Specifying a directory to index

To specify a directory other than the current working directory pass the target directory to the `--workspace-root` flag.

```sh theme={null}
auggie --workspace-root /path/to/your/project
```

To learn more about what files are indexed and how to ignore files, see [Workspace indexing](/cli/setup-auggie/workspace-indexing).


# Index your workspace
Source: https://docs.augmentcode.com/cli/setup-auggie/workspace-indexing

When your workspace is indexed, Augment can provide tailored code suggestions and answers based on your unique codebase, best practices, coding patterns, and preferences. You can always control what files are indexed.

## Security and privacy

Augment stores your code securely and privately to enable our powerful context engine. We ensure code privacy through a proof-of-possession API and maintain strict internal data minimization principles. [Read more about our security](https://www.augmentcode.com/security).

## What gets indexed

Augment will index all the files in your workspace, except for the files that match patterns in your `.gitignore` file and the `.augmentignore` file. [Read more about Workspace Context](/cli/setup-auggie/workspace-context).

## Ignoring files with .augmentignore

The `.augmentignore` file is a list of file patterns that Augment will ignore when indexing your workspace. Create an `.augmentignore` file in the root of your workspace. You can use any glob pattern that is supported by the [gitignore](https://git-scm.com/docs/gitignore) file.

## Including files that are .gitignored

If you have a file or directory in your `.gitignore` that you want to be indexed, you can add it to your `.augmentignore` file using the `!` prefix.

For example, you may want your `node_modules` indexed to provide Augment with context about the dependencies in their project, but it is typically included in their `.gitignore`. Add `!node_modules` to your `.augmentignore` file.

<CodeGroup>
  ```bash .augmentignore theme={null}
  # Include .gitignore excluded files with ! prefix
  !node_modules

  # Exclude other files with .gitignore syntax
  data/test.json
  ```

  ```bash .gitignore theme={null}
  # Exclude dependencies
  node_modules

  # Exclude secrets
  .env

  # Exclude build artifacts
  out
  build
  ```
</CodeGroup>


# Agent Skills
Source: https://docs.augmentcode.com/cli/skills

Extend Auggie's capabilities with specialized domain knowledge using the agentskills.io specification.

## Overview

Skills provide a standardized way to give Auggie specialized domain knowledge and capabilities. Following the [agentskills.io](https://agentskills.io) specification, skills are modular packages of guidance, resources, and context that help the agent understand specific domains or workflows.

## What are Skills?

Skills are self-contained packages that provide:

* **Specialized knowledge**: Domain-specific guidance and best practices
* **Contextual resources**: Links to documentation, APIs, or tools
* **Workflow patterns**: Step-by-step procedures for common tasks
* **Tool usage guidance**: How to use specific tools or frameworks

Unlike rules (which provide general guidelines), skills are designed to be:

* **Discoverable**: The agent can see what skills are available through their metadata
* **Modular**: Each skill is independent and can be added or removed easily
* **Standardized**: Following the agentskills.io spec ensures compatibility across AI tools

## Skill File Structure

Skills are defined in `SKILL.md` files located in the `.augment/skills/` or `.claude/skills/` directories (in either your workspace or home directory). Each skill must be in its own subdirectory:

```
.augment/skills/
  ├── python-testing/
  │   └── SKILL.md
  ├── api-design/
  │   └── SKILL.md
  └── database-migrations/
      └── SKILL.md
```

### SKILL.md Format

Each `SKILL.md` file must include YAML frontmatter with required metadata:

**Example SKILL.md file:**

```markdown theme={null}
---
name: python-testing
description: Best practices for writing and running Python tests with pytest
---

# Python Testing Skill

This skill provides guidance on writing effective Python tests.
```

The file content after the frontmatter can include:

* Markdown headings and text
* Code examples (using code blocks)
* Lists and other markdown formatting

### Required Frontmatter Fields

| Field         | Description                            | Requirements                                                                        |
| :------------ | :------------------------------------- | :---------------------------------------------------------------------------------- |
| `name`        | Skill identifier                       | 1-64 characters, lowercase alphanumeric and hyphens only, must match directory name |
| `description` | What the skill does and when to use it | 1-1024 characters, helps the agent understand when to apply the skill               |

### Skill Name Requirements

Per the agentskills.io specification, skill names must:

* Be 1-64 characters long
* Use only lowercase letters, numbers, and hyphens
* Not start or end with a hyphen
* Not contain consecutive hyphens
* Match the directory name containing the SKILL.md file

**Valid names**: `python-testing`, `api-design`, `database-migrations`\
**Invalid names**: `Python-Testing`, `api_design`, `-database`, `my--skill`

## Skill Locations

Skills are discovered from multiple locations, similar to rules:

| Location                       | Source    | Description                                                |
| :----------------------------- | :-------- | :--------------------------------------------------------- |
| `~/.augment/skills/`           | User      | Available in all workspaces, stored in your home directory |
| `<workspace>/.augment/skills/` | Workspace | Project-specific skills, can be version controlled         |
| `~/.claude/skills/`            | User      | Compatible with Claude Code, stored in home directory      |
| `<workspace>/.claude/skills/`  | Workspace | Compatible with Claude Code, in workspace                  |

Skills from all locations are loaded and made available to the agent. The **Source** column in the `/skills` popover shows whether each skill came from your home directory (User) or the current workspace (Workspace).

## Viewing Skills

Use the `/skills` slash command to view all loaded skills and their details:

```
/skills
```

This opens a popover showing:

* **Name**: The skill identifier
* **Source**: Where the skill was loaded from (Workspace or User)
* **Description**: What the skill does
* **Tokens**: Estimated token count based on the SKILL.md file size

### Skills Popover Navigation

| Key                    | Action                                 |
| :--------------------- | :------------------------------------- |
| `↑` / `↓` or `j` / `k` | Navigate between skills                |
| `Enter`                | Open the selected skill in your editor |
| `Esc`                  | Close the popover                      |

The token count helps you understand the context window cost of each skill. Skills with larger instructions will consume more tokens when activated.

## Creating Your First Skill

<Steps>
  <Step title="Create the skills directory">
    ```bash theme={null}
    mkdir -p .augment/skills/my-skill
    ```
  </Step>

  <Step title="Create the SKILL.md file">
    Create a file at `.augment/skills/my-skill/SKILL.md` with the following content:

    ```markdown theme={null}
    ---
    name: my-skill
    description: Custom skill for my project's specific workflow
    ---

    # My Custom Skill

    Add your skill content here with guidance, examples, and resources.
    ```
  </Step>

  <Step title="Verify the skill is loaded">
    Start Auggie and use the `/skills` command to confirm your skill appears in the list.
  </Step>
</Steps>

## Skills vs Rules

While both skills and rules provide guidance to the agent, they serve different purposes:

| Feature       | Skills                              | Rules                              |
| :------------ | :---------------------------------- | :--------------------------------- |
| **Purpose**   | Specialized domain knowledge        | General coding guidelines          |
| **Format**    | agentskills.io specification        | Markdown with optional frontmatter |
| **Discovery** | Metadata-based (name + description) | Content-based or always-applied    |
| **Scope**     | Specific domains/workflows          | Project-wide conventions           |
| **Standard**  | Cross-platform (agentskills.io)     | Augment-specific                   |

Use **skills** for:

* Framework-specific knowledge (e.g., React patterns, Django best practices)
* Tool usage guides (e.g., Docker workflows, CI/CD procedures)
* Domain expertise (e.g., security practices, performance optimization)

Use **rules** for:

* Code style preferences
* Project architecture guidelines
* Team conventions

## Best Practices

1. **Be Specific**: Focus each skill on a single domain or workflow
2. **Include Examples**: Provide concrete code examples and commands
3. **Keep Updated**: Review and update skills as tools and practices evolve
4. **Use Clear Descriptions**: Help the agent understand when to use each skill
5. **Version Control**: Commit workspace skills to share with your team

## See Also

* [agentskills.io Specification](https://agentskills.io/specification) - Official skill format specification
* [Example Skills](https://github.com/anthropics/skills) - Collection of example skills from Anthropic
* [Rules & Guidelines](/cli/rules) - Configure general project guidelines
* [CLI Reference](/cli/reference) - Complete command-line reference


# Subagents
Source: https://docs.augmentcode.com/cli/subagents

Configure custom agents for specific tasks to automate your workflow and share them with your team.

<Availability />

## About subagents

Subagents are custom agents that you can configure for specialized tasks, like code review or project bootstrapping. Each subagent has its own tools and capabilities that you can delegate specific tasks to. You can have local subagents or share them with your team by adding their configuration to your repository.

* Subagents have their own context window independent from the main agent
* Subagents have a custom prompt that is used to instruct the agent
* Subagents run in parallel with other subagents
* Subagents will show a summary of their current progress in the main thread

## Create a subagent

You can create a new subagent through the wizard by running `/agents` command in interactive mode. Or you can create the configuration file manually.

### Create a subagent with the wizard

1. Run the `/agents` command in interactive mode
2. Select "Create new agent"
3. Select where you want the agent configuration to be stored
4. Complete the following fields to configure the agent:
   * Name
   * Description
   * Color
   * Model
   * Prompt
5. Review the configuration and press enter to save the agent

### Create a subagent manually

You can create a subagent manually by creating a configuration file. The configuration file should be a markdown file stored in either `~/.augment/agents/` (user only) or `./.augment/agents/` (shared). See the [Subagent configuration reference](#subagent-configuration-reference) for more details.

**Example subagent configuration:**

```markdown theme={null}
---
name: code-review
description: Code review agent
model: sonnet4.5
color: purple
---

You are an agentic code-review AI assistant with access to the developer's codebase through Augment's deep codebase context engine and integrations. You are conducting a comprehensive code review for the staged changes in the current working directory.

## Review Areas to focus on:

- **Potential Bugs**: Identify bugs, logic errors, edge cases, crash-causing problems.
- **Security Concerns**: Look for potential vulnerabilities, input validation, authentication issues ONLY if the code is security-sensitive
- **Documentation**: Report comments or documentation that is incorrect or inconsistent with the code.
- **API contract violations**
- **Database and schema errors**
- **High Value Typos**: typos that affect correctness, UX-strings, etc.
```

## Running your subagent

Once you've configured the subagent, you can trigger it by sending a message that references the agent name. Augment will also automatically detect when a task is appropriate for a subagent and offer to use it.

```
> Use the code-review agent to review my staged changes
```

## Subagent configuration reference

### File locations

Subagents are configured in markdown files with YAML frontmatter. Subagents can be configured at the user level or the workspace level. User-level subagents are available in all workspaces, while workspace-level subagents are only available in the current workspace.

| Scope     | Location             | Availability                        |
| :-------- | :------------------- | :---------------------------------- |
| User      | `~/.augment/agents/` | Available in all workspaces         |
| Workspace | `./.augment/agents/` | Available in current workspace only |

### Frontmatter configuration

| Field         | Required | Purpose                                                                      |
| :------------ | :------- | :--------------------------------------------------------------------------- |
| **`name`**    | **Yes**  | **Name of the agent**                                                        |
| `description` | No       | Description of the agent                                                     |
| `color`       | No       | Color of the agent in the CLI, should be a valid ANSI color name.            |
| `model`       | No       | Model to use for the agent. If not specified, the CLI default model is used. |

### Supported models

Subagents can use any model available in Auggie. To see a list of available models, run the following command:

```bash theme={null}
auggie models list
```

This will display all supported models along with their identifiers that you can use in your subagent configuration.

<Note>
  Model availability may vary depending on your Augment subscription and organization settings.
</Note>

### Agent prompt

The agent prompt is the main body of the markdown file. The prompt is used to instruct the agent on its role and capabilities. The prompt can include any information that you want to be available to the agent, including specific tools or instructions. The prompt is rendered as markdown and supports code blocks, lists, and other formatting.

## Best practices for subagents

* **Subagents are most effective when they have a specific and focused task.** It is better to create multiple subagents for different tasks rather than trying to create a single agent for multi-step, long-running, or complex tasks.
* **Subagents should have a detailed prompt**. The prompt should clearly define the agent's role, capabilities, and expected behavior. Include specific instructions, task lists, examples, and expected output. Take advantage of markdown formatting to make the prompt as clear as possible.
* **Share your subagents with your team**. Subagents are a great way to share custom workflows with your team. Store your subagents in your projects `./.augment/agents/` directory to make them available to everyone.

## Example subagents

### Code review agent

```markdown theme={null}
---
name: code-review
description: Code review agent
model: sonnet4.5
color: purple
---

You are an agentic code-review AI assistant with access to the developer's codebase through Augment's deep codebase context engine and integrations. You are conducting a comprehensive code review for the staged changes in the current working directory.

Review Areas to focus on:

- **Potential Bugs**: Identify bugs, logic errors, edge cases, crash-causing problems.
- **Security Concerns**: Look for potential vulnerabilities, input validation, authentication issues ONLY if the code is security-sensitive
- **Documentation**: Report comments or documentation that is incorrect or inconsistent with the code.
- **API contract violations**
- **Database and schema errors**
- **High Value Typos**: typos that affect correctness, UX-strings, etc.

Review Areas to avoid:

- **Style nags**: e.g. prefer `const` over `let`, prefer template strings, etc.
- **Opinionated suggestions**: e.g. prefer `map` over `forEach`, etc.
- **Low value typos**: e.g. spelling errors in comments, etc.
```

### Test generation agent

```markdown theme={null}
---
name: test-generation
description: Generates and runs tests for new or modified code
model: sonnet4.5
color: green
---

You are an agentic test generation AI assistant. You are responsible for writing thorough and high quality automated tests for this software project. You have access to the codebase through Augment's deep codebase context engine and integrations, and are able to run commands through the terminal.

Your goals:

1. Analyze recent code changes or diffs to identify new or modified functions, classes, or modules.
2. Determine which parts of the changes are missing test coverage.
3. Generate clear, idiomatic unit or integration tests using the project's existing testing framework and conventions.
4. Write test files or append tests to existing files in appropriate locations.
5. Run the test suite and summarize results, including:
   - Number of tests added or updated
   - Any failures or skipped tests
   - Edge cases or scenarios still untested
6. If a test fails immediately, analyze the likely cause and propose fixes or clarifications.

Guidelines:

- Favor readability, determinism, and minimal mocking.
- Reuse existing helper utilities and fixtures if present.
- Match the naming conventions and import patterns found in the repository.
- Always include at least one negative test (an example where the function should fail).

```

### API designer agent

```markdown theme={null}
---
name: api-designer
description: Use for designing REST/GraphQL APIs, OpenAPI specs, and API documentation
model: sonnet4.5
color: blue
---

You are an API design specialist focused on creating well-structured, intuitive, and maintainable APIs. You are responsible for designing and documenting APIs for this software project. You have access to the codebase through Augment's deep codebase context engine and integrations, and are able to run commands through the terminal.

## Design Principles

- Use consistent naming conventions (plural nouns for resources)
- Implement proper HTTP methods and status codes
- Design for idempotency where appropriate
- Include pagination for list endpoints
- Provide filtering, sorting, and field selection
- Follow HATEOAS principles for discoverability
- Implement rate limiting considerations

## API Patterns

**REST Best Practices:**

- `/api/v1/resources` - Collection endpoint
- `/api/v1/resources/{id}` - Single resource
- `/api/v1/resources/{id}/relationships` - Nested resources
- Use query params for filtering: `?status=active&sort=-created_at`

**Error Responses:**

- Return consistent error format with code, message, details
- Use appropriate HTTP status codes (400, 401, 404, 422, 500)

## Documentation Style

- Generate or update OpenAPI 3.0+ spec
- Include examples for all endpoints

```


# Analytics Dashboard
Source: https://docs.augmentcode.com/codereview/analytics-dashboard

Track code review metrics and measure the impact of Augment Code Review on your team.

## Code Review Analytics

Use the Code Review Analytics dashboard to track the review load automated by Augment, along with the comments made by Code Review that developers ultimately addressed.

1. **Navigate to Code Review** - In your browser, visit [Code Review Analytics](https://app.augmentcode.com/code-review/analytics).
2. **Filter by Date** - Refine your Analytics using the tabs for Last 7 Days, Last 30 Days, or Last 60 Days.

### Metric Definitions

* **Total PRs Reviewed**: The number of PRs that have been reviewed by Augment Code Review.
* **Total Reviews Performed**: The number of reviews that have been run by Augment Code Review. One PR can have multiple reviews if people manually trigger more reviews.
* **Total Comments**: The total number of inline comments left by Augment Code Review.
* **Percentage of Comments Addressed**: A comment is addressed if the developer resolved the concerns raised by the Augment Code Review comment. The percentage is calculated by dividing the number of addressed comments by the total number of comments left by Augment Code Review.
* **Percentage of Thumbs Up Reactions**: A thumbs up reaction is counted if a user reacts with the Thumbs Up emoji on GitHub on an inline comment left by Augment Code Review. The percentage is calculated by dividing the number of thumbs up reactions by the total number of thumbs up and thumbs down emoji reactions.
* **Estimated Dev Hours Saved**: Number of PRs multiplied by 10 minutes

### Reading the Charts

* **Addressed Comments**: A chart detailing total number of comments per day broken down by unaddressed (gray) vs addressed (green). You can interpret the green bar to mean Augment Code Review caught issues that developers fixed and may not have without the comment.
* **Reviewed PRs**: A chart detailing the total number of reviewed PRs per day (blue).


# Auto-Generated PR Descriptions
Source: https://docs.augmentcode.com/codereview/auto-generated-pr-descriptions

Generates comprehensive PR descriptions using Augment Code's Context Engine.

After Augment Code Review has reviewed your pull request, it will leave a comment summarizing the work to that point. This description saves reviewers time by handling the 'what' and 'how' of the changes, allowing them to focus on explaining the 'why' and the broader context. The result: faster reviews, better collaboration, and more time on building.

## How It Works

1. **Create Your PR**: Open a pull request in GitHub with your code changes
2. **Automatic Analysis**: Augment's Context Engine analyzes your code diff and understands the changes in the context of your entire codebase
3. **Description Generation**: A comprehensive PR description is automatically generated, covering what changed, how it works, and potential impacts
4. **Review and Edit**: Review the generated description and add any additional context about why the changes were made
5. **Faster Reviews**: Reviewers can quickly understand your changes and provide meaningful feedback

## Best Practices

**Review Before Accepting**: Always review the auto-generated description to ensure accuracy and completeness. The AI understands your code, but you understand the business context.

**Add the 'Why'**: Supplement the generated description with the reasoning behind your changes. This helps reviewers understand not just what changed, but why it matters.

**Keep PRs Focused**: Smaller, focused PRs result in more accurate and useful descriptions. Avoid mixing unrelated changes in a single PR.

**Update for Significant Changes**: If you make substantial changes to your PR after the description is generated, consider regenerating or manually updating the description.

**Use as a Starting Point**: Treat the auto-generated description as a foundation. Enhance it with project-specific context, design decisions, and any nuances the AI might miss.

**Give Reviewers Context**: Give reviewers comprehensive context upfront, leading to faster and more thorough reviews. At the same time, help new team members understand changes more quickly with detailed, consistent PR descriptions.


# Code Review Enterprise Features
Source: https://docs.augmentcode.com/codereview/enterprise-features

Advanced features and capabilities available to Enterprise plan customers for Augment Code Review.

## Overview

Augment Code Review Enterprise provides advanced features designed for organizations that need greater control, deeper integrations, and comprehensive analytics. This page outlines the key differences between self-serve and Enterprise plans.

## Feature Comparison

| Feature                | Self-Serve                 | Enterprise                                                         |
| ---------------------- | -------------------------- | ------------------------------------------------------------------ |
| **Advanced Analytics** | Total reviews performed    | Full dashboard with reviews, comments addressed, and team insights |
| **User Allowlist**     | All repo users get reviews | Control exactly which users receive PR reviews                     |
| **MCP Integration**    | Not available              | Connect to Jira, Linear, Notion, feature flags, and more           |
| **Multi-Org Support**  | Single GitHub organization | Multiple GitHub organizations per tenant                           |
| **Seats**              | Up to 20 seats             | Unlimited seats                                                    |
| **Connected Repos**    | Limited                    | Unlimited repositories                                             |

## Available Enterprise Features

### Advanced Analytics

Enterprise customers have access to a comprehensive analytics dashboard that goes beyond basic metrics:

* **Reviews Performed**: Track the total number of reviews completed by Augment Code Review
* **Comments Addressed**: See how many review comments were acted upon by developers
* **Engagement Metrics**: Understand how your team interacts with Code Review feedback

Self-serve users see only the total number of reviews performed.

<Note>
  Access the analytics dashboard at [Code Review Analytics](https://app.augmentcode.com/code-review/analytics).
</Note>

### User Allowlist

Enterprise administrators can specify exactly which GitHub users can trigger Augment Code Review. This provides fine-grained control over feature access within your organization.

When Allowlist Mode is active:

* Only users in the allowlist can trigger Augment Code Review
* Automatic and manual reviews are disabled for all other users
* Useful for phased rollouts or restricting access to specific teams

<Note>
  Manage your allowlist at [User Access Settings](https://app.augmentcode.com/settings/code-review/user-access).
</Note>

### MCP Integration

Connect Augment Code Review to your existing tools through Model Context Protocol (MCP). This enables the code review agent to gather additional context from your organization's systems:

* **Ticketing Systems**: Jira, Linear, and other issue trackers
* **Documentation**: Notion, Confluence, and internal wikis
* **Feature Flags**: LaunchDarkly, Split, and other feature management tools
* **Other Systems**: Any MCP-compatible tool relevant to your development workflow

This additional context allows Code Review to provide more informed and relevant feedback based on your team's specific requirements and documentation.

<Note>
  Configure MCP servers at [MCP Settings](https://app.augmentcode.com/settings/code-review/mcp).
</Note>

### Multi-Organization Support

Enterprise customers can install the Augment Code Review GitHub bot across multiple GitHub organizations or accounts. This is essential for:

* Organizations with separate GitHub orgs for different products or teams
* Companies that have acquired other organizations with existing GitHub structures
* Enterprises with strict organizational boundaries between business units

All organizations connect to a single Augment Enterprise tenant for unified management and billing.

### Unlimited Seats

Enterprise plans provide access to Augment Code Review for your entire organization without seat limitations. Self-serve plans are limited to 20 seats.

### Unlimited Connected Repositories

Enterprise customers can enable Code Review on an unlimited number of repositories. Self-serve plans have a cap on the number of repositories that can be connected.

## Getting Started with Enterprise

To upgrade to Enterprise or learn more about Enterprise features, visit [augmentcode.com/pricing](https://augmentcode.com/pricing) or contact our sales team.

If you're already an Enterprise customer, visit your [Code Review Settings](https://app.augmentcode.com/settings/code-review) to configure these features.


# Fix in Augment
Source: https://docs.augmentcode.com/codereview/fix-with-augment

Automatically address issues found during code review directly using the agent in your IDE or paste the details into your preferred environment to address it yourself.

When Augment Code Review identifies issues in your pull request, you can use the "Fix in Augment" button inside the comment to automatically address the issue.

<img alt="Fix in Augment button" />

Options include:

* **Open in Agent Session**: For VS Code only, allows you to copy the prompt and start a new thread inside the Augment Code extension
* **Copy to Clipboard**: Allows you to paste the prompt into your preferred environment, e.g. Auggie CLI, Augment Code for JetBrains, etc.

<img alt="Fix in Augment options" />

***

## Best Practices

**Review the Fix**: Always review the changes proposed by Agent before accepting them. While Agent has full context, you should verify the fix aligns with your intent.

**Test the Changes**: Run your tests after applying the fix to ensure the issue is resolved and no new issues are introduced.

**Update the PR**: After pushing your fix, you can reply to the Code Review comment to indicate you've addressed the issue.

**Request Follow-up Review**: If you make significant changes, consider requesting another review by commenting `auggie review` on your PR.


# Adding Context with MCP
Source: https://docs.augmentcode.com/codereview/mcp-context

Connect Augment Code Review to external context sources through Model Context Protocol.

## Configuring Model Context Protocol (MCP) Servers

Administrators can connect Augment Code Review to external context sources through Model Context Protocol (MCP). MCP servers provide additional context to the code review agent, such as access to documentation, APIs, databases, or other external systems that can help improve review quality.

To configure MCP servers, visit [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp).

### Types of MCP Servers

Augment Code Review supports both remote and local MCP servers:

* **Remote MCP servers** run remotely and are hosted by providers. Once you add a remote MCP server, you may need to complete an OAuth flow to authenticate before it can be used by the code review agent.
* **Local MCP servers** run in their own environment within the code review agent's workspace. You can specify environment variables for local servers when adding them. Environment variables are write-only and can only be overwritten or removed (not viewed) after the server has been added.

### Adding MCP Servers

There are three ways to add MCP servers to Code Review:

#### 1. Add Local MCP Server (+ MCP)

To add a local MCP server:

1. Navigate to [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp)
2. Click **+ MCP** to add a local server
3. Enter the following information:
   * **Name**: A descriptive name for your MCP server
   * **Command**: The executable command to run the server
   * **Arguments**: Command-line arguments (optional)
4. Add environment variables if needed:
   * Click **+ Environment Variable**
   * Enter the variable name and value
   * Repeat for additional variables
5. Click **Add Server** to save
6. Add a review guideline telling Augment Code Review when to use the MCP server (see [Review Guidelines](/codereview/review-guidelines) for more information)

<Note>
  Environment variables for local MCP servers are stored securely and cannot be viewed after saving. You can only overwrite or remove them.
</Note>

#### 2. Add Remote MCP Server (+ Remote MCP)

To add a remote MCP server:

1. Navigate to [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp)
2. Click **+ Remote MCP** to add a remote server
3. Enter the following information:
   * **Name**: A descriptive name for your MCP server
   * **URL**: The full URL of the remote MCP server (e.g., `https://mcp.example.com`)
4. Click **Add Server**
5. If the server requires OAuth authentication, you'll be redirected to complete the authentication flow
6. After successful authentication, you'll be redirected back to the settings page
7. Add a review guideline telling Augment Code Review when to use the MCP server (see [Review Guidelines](/codereview/review-guidelines) for more information)

Remote MCP servers that require authentication will show a status indicator:

* **Connected** (green): Server is authenticated and ready to use
* **Authenticate** (yellow): Server needs authentication or re-authentication

#### 3. Import from JSON

To import MCP server configurations from a JSON file:

1. Navigate to [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp)
2. Click **Import from JSON**
3. Paste your JSON configuration in the format:
   ```json theme={null}
   {
     "mcpServers": {
       "server-name": {
         "command": "npx",
         "args": ["-y", "@example/mcp-server"],
         "env": {
           "API_KEY": "your-api-key"
         }
       }
     }
   }
   ```
4. Click **Import** to add the servers
5. Add a review guideline telling Augment Code Review when to use the MCP server (see [Review Guidelines](/codereview/review-guidelines) for more information)

<Note>
  The JSON format matches the structure used in Augment's settings.json file, making it easy to share configurations across your team.
</Note>

### Managing MCP Servers

Once added, MCP servers appear in the "Configured MCP Servers" list. For each server, you can:

* **View status**: See if the server is connected or needs authentication
* **Re-authenticate**: Click the **Authenticate** button for remote servers that need re-authentication
* **Remove**: Click the trash icon to remove a server from Code Review

All configured MCP servers are available to the code review agent when analyzing pull requests.

### Example: Review Guideline for MCP Servers

After adding an MCP server, you should create a review guideline that tells Augment Code Review when and how to use it. Add guidelines to your `code_review_guidelines.yaml` file at `<repo-root>/.augment/code_review_guidelines.yaml`.

Here's an example guideline for using the Linear MCP server:

```yaml theme={null}
areas:
  linear_ticket_verification:
    description: "Verify PRs implement their linked Linear tickets correctly"
    globs:
      - "**"
    rules:
      - id: "verify_linear_ticket_implementation"
        description: "If a Linear ticket is linked in the PR description, use the Linear MCP server to retrieve the ticket description and verify that the PR correctly implements the requirements specified in the ticket."
        severity: "high"
```

This guideline instructs the code review agent to:

1. Check if a Linear ticket is referenced in the PR description
2. Use the Linear MCP server to fetch the ticket details
3. Verify that the code changes align with the ticket requirements

For more information on writing review guidelines, see [Review Guidelines](/codereview/review-guidelines).


# Using Augment Code Review
Source: https://docs.augmentcode.com/codereview/overview

A native GitHub experience to catch critical issues, comment on pull requests, and collaborate on fixes.

## Quickstart

<Tabs>
  <Tab title="New Users">
    <Steps>
      <Step title="Create an Augment Account">
        Visit [augmentcode.com](https://www.augmentcode.com) and click **Sign Up**. Complete registration with your email address, verify your email, and accept the terms of service during onboarding.
      </Step>

      <Step title="Connect GitHub to Configure your Repos for Code Review">
        Log in to [app.augmentcode.com](https://app.augmentcode.com), navigate to **Settings** → **Code Review** → **Configuration**, and click **Connect GitHub**. You'll be redirected to GitHub to authorize the app. Select the repositories you want to grant access to (all repositories or specific repos) and click **Install & Authorize**.
      </Step>

      <Step title="Set Code Review to Automatic or Manual">
        Return to [app.augmentcode.com](https://app.augmentcode.com), Under **Configuration**, Find the repository you want to enable. Under **Set Review Trigger**, choose **Automatic Review** for instant feedback on every PR when marked "ready for review", or **Manual Review** to trigger reviews by commenting `auggie review` on PRs.
      </Step>

      <Step title="Submit Your First Review">
        Create a pull request on GitHub in any enabled repository. For automatic reviews, mark the PR as "ready for review" and Augment will analyze it within minutes. For manual reviews, add a comment with `auggie review` to trigger the analysis.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Enterprise Plan" icon="building">
    <Steps>
      <Step title="Contact Your Enterprise Administrator">
        Before using Code Review, your Enterprise Plan administrator must enable the feature for your organization. Request access to specific repositories or organization-wide access, and confirm any custom enterprise policies or guidelines. Provide your GitHub organization name and list of repositories you want to enable.
      </Step>

      <Step title="Install the Augment GitHub App">
        If not already installed, navigate to [app.augmentcode.com/settings/code-review](https://app.augmentcode.com/settings/code-review) and click **Connect GitHub**. Select your organization (requires organization admin permissions), choose repository access level, and click **Install & Authorize**. See [Setup Guide for Enterprise](/codereview/setup-guide-enterprise) for detailed instructions.
      </Step>

      <Step title="Configure Repository Access">
        **For Admins:** In Code Review settings, enable or disable code review for specific repositories and configure per-repository settings (automatic review on PR ready, custom guidelines path). **For Non-Admins:** Contact your administrator to request access to additional repositories.
      </Step>

      <Step title="Start Using Code Review">
        Create a pull request in an enabled repository. For automatic reviews, mark the PR as "ready for review". For manual reviews, comment `auggie review`. Code Review will analyze and post review comments. Address feedback and use the **Fix with Augment** button to resolve issues in your IDE.
      </Step>
    </Steps>

    <Card title="Setup Guide for Enterprise Plan" icon="gear" href="/codereview/setup-guide-enterprise">
      Enterprise Plan administrators can configure Augment Code Review and grant repository access on GitHub.
    </Card>
  </Tab>

  <Tab title="All Other Plans" icon="star">
    Follow these steps if you are on an Indie, Standard, or Max plan.

    <Steps>
      <Step title="Connect GitHub to Configure your Repos for Code Review">
        Visit [app.augmentcode.com/settings/code-review](https://app.augmentcode.com/settings/code-review) and log in. Click **Connect GitHub to Get Started** to install the Augment GitHub App. You'll be redirected to GitHub to authorize the app and select repositories. Choose **All repositories** for organization-wide access or **Only select repositories** for specific repos, then click **Install & Authorize**.
      </Step>

      <Step title="Set Code Review to Automatic or Manual">
        As an Administrator, control when Code Review triggers. Navigate to **[Settings](https://app.augmentcode.com/settings/code-review)** → **Code Review** → **Configuration**. Under **Repositories**, use **Set Review Trigger**, to select  **Automatic Review** for instant feedback on every PR when marked "ready for review", or **Manual Review** to trigger reviews by commenting `auggie review` on PRs.
      </Step>

      <Step title="Start Reviewing Pull Requests">
        Create or open a pull request in GitHub. For automatic reviews, mark the PR as "ready for review". For manual reviews, comment `auggie review`, `augment review`, or `augmentcode review`. Code Review will add 👀 to show it's reviewing and post comments on any issues found.
      </Step>
    </Steps>

    <Card title="Setup Guide for All Other Plans" icon="star" href="/codereview/setup-guide-otherplans">
      Learn more about setting up Augment Code Review for Indie, Standard, and Max plans.
    </Card>
  </Tab>
</Tabs>

***

## Context powered code reviews focus on high-impact issues

Augment Code Review prioritizes high signal-to-noise ratio by focusing on high-impact issues:

* **Bugs**: Logic errors, edge cases, and potential runtime issues
* **Security concerns**: Vulnerabilities, unsafe operations, and data exposure risks
* **Correctness**: Null handling and error management
* **Cross-system problems**: Breaking changes, API compatibility, and integration issues

The agent avoids low-value style nags and focuses on objective issues by gathering context from multiple sources:

* **PR Contents**: The agent analyzes the complete code diff to understand what changed and why.

* **Entire Repository**: Through Augment's Context Engine, the agent has access to your full codebase, enabling it to identify cross-system impacts and maintain consistency with existing patterns.

* **PR Title and Description**: More detailed PR descriptions help the agent provide better, more targeted reviews. Include information about:
  * What the PR accomplishes
  * Why the changes were made
  * Any special considerations or context

***

## Best Practices

**Write detailed PR descriptions**: The more context you provide in your PR title and description, the better the agent can understand your intent and provide relevant feedback.

**Use custom guidelines**: Define repository-specific review guidelines to help the agent focus on your team's priorities and domain-specific concerns.

**Provide feedback**: Give feedback on comments using the thumbs up emoji to indicate whether the comment is useful or thumbs down if the comment was not helpful.

**Ask for a follow-up review**: If you make significant changes to the PR and want another review, then ask for a follow-up review by commenting on your PR with the same comments as a manual request: `auggie review`, `augment review`, or `augmentcode review`. The agent will add 👀 to the comment so you know it is reviewing the PR.


# Providing Feedback
Source: https://docs.augmentcode.com/codereview/providing-feedback

Learn how to provide feedback on Augment Code Review comments directly in GitHub.

## Providing feedback

You can provide in product feedback directly in GitHub by reacting with a thumbs up or thumbs down emoji to the inline comment left by Augment Code Review.

<img alt="Code Review Feedback using GitHub Reactions" />


# Review Guidelines
Source: https://docs.augmentcode.com/codereview/review-guidelines

Configure custom guidelines to help Augment Code Review focus on specific areas and domain knowledge. Learn which files are automatically skipped and how to customize file exclusions.

## Tell Augment Code Review to check specific areas with guidelines

Some domain knowledge cannot be inferred from code alone. Tell Augment Code Review exactly what to check by adding custom guidelines. Guidelines are most relevant for repositories that contain multiple distinct domains and should be captured as custom review guidelines. Tell Augment Code Review to check specific areas like security vulnerabilities or inside particular directories when relevant. Augment Code Review allows you to outline these special guidelines per repository. Describe any areas of focus using a yaml file entitled code\_review\_guidelines.yaml inside the .augment folder at the repository root:

`<repo-root>/.augment/code_review_guidelines.yaml`

Scope guidelines to the appropriate sub-directories and focus on objective issues that can cause bugs, expose vulnerabilities, etc. and less on stylistic or subjective things. Augment Code Review uses a unique yaml file instead of relying on markdown guideline files like Agents.md, etc. because it allows the agent to cite a guideline if it was used for a particular comment, and compute per-guideline analytics.

### Example Augment Code Review Guidelines

For a complete working example, see the [Code Review Best Practices](https://github.com/augmentcode/code-review-best-practices) repository.

```yaml theme={null}
# Guidelines exclusive to augmentcode/auggie

areas:
  databases:
    description: "Data and Database related rules"
    globs:
      - "**"
    rules:
      - id: "no_pii_in_bigquery"
        description: "Never store PII data in BigQuery tables."
        severity: "high"
      - id: "no_guid_keys"
        description: "GUID foreign keys can slow lookups"
        severity: "medium"

  memory_safety:
    description: "Ensure Memory Safety"
    globs:
      - "kernel/**"
    rules:
      - id: "avoid_unsafe_rust"
        description: "Avoid unsafe Rust operations."
        severity: "high"
```

<Note>
  Common **globs** or pattern matching syntax:

  * `**` - Matches any number of directories (recursive wildcard)
    * Example: `**/test.py` matches `test.py`, `src/test.py`, `src/utils/test.py`, etc.
  * `*` - Matches any sequence of characters within a single directory level
    * Example: `*.py` matches `file.py`, `main.py` but not `src/main.py`
  * `?` - Matches exactly one character
    * Example: `test?.py` matches `test1.py`, `testA.py` but not `test10.py`
</Note>

* **Rules:** Areas can contain more than one rule. Each rule contains:
  * **ID**: Double quoted unique identifier
  * **Description**: Double quoted message summarizing intent of the rule
  * **Severity**: Expects double quoted "high", "medium" or "low". Sets the priority of review by Augment Code Review

### Referencing Existing Rules Files

You can add a custom rule that references an existing rules file (like `Agents.md`) to incorporate those guidelines into your code review process. This allows you to reuse existing documentation and standards without duplicating content.

However, it is recommended to use the YAML format to track guidelines, as this enables Augment Code Review to cite specific guidelines in comments and compute per-guideline analytics.

## Files Automatically Skipped During Review

Augment Code Review automatically skips certain file types that are not typically code files. This helps focus the review on meaningful code changes and avoids wasting time on binary files, generated content, and other non-reviewable assets.

<Accordion title="File Extensions Automatically Ignored">
  The following file extensions are automatically skipped during code review:

  **Archive files:**

  * `.bz2`, `.gz`, `.xz`, `.zip`, `.7z`, `.rar`, `.zst`, `.tar`, `.jar`, `.war`, `.nar`

  **Image files:**

  * `.ico`, `.svg`, `.jpeg`, `.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webm`

  **Font files:**

  * `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot`

  **Document files:**

  * `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`

  **Data files:**

  * `.csv`, `.tsv`, `.dat`, `.db`, `.parquet`

  **System files:**

  * `.DS_Store`, `.tags`

  **Cscope files:**

  * `.cscope.files`, `.cscope.out`, `.cscope.in.out`, `.cscope.po.out`

  **Log and output files:**

  * `.log`, `.map`, `.out`, `.sum`, `.work`, `.md5sum`

  **3D and graphics files:**

  * `.tga`, `.dds`, `.psd`, `.fbx`, `.obj`, `.blend`, `.dae`, `.gltf`

  **Shader files:**

  * `.hlsl`, `.glsl`

  **Game engine files:**

  * `.unity`, `.umap`, `.prefab`, `.mat`, `.shader`, `.shadergraph`, `.sav`, `.scene`, `.asset`

  **Python compiled files:**

  * `.pyc`, `.pyd`, `.pyo`, `.pkl`, `.pickle`

  **Protocol buffer files:**

  * `.pb.go`, `.pb.gw.go`

  **Terraform files:**

  * `.tfstate`, `.tfstate.backup`

  **Minified files:**

  * `.min.js`, `.min.js.map`, `.min.css`

  **Lock and dependency files:**

  * `.lock`, `.lockb`, `.lockfile`

  **Debug and trace files:**

  * `.trace`, `.dump`

  **Backup files:**

  * `.bak`, `.backup`

  **Database files:**

  * `.sql.gz`
</Accordion>

<Accordion title="File Patterns Automatically Ignored">
  In addition to specific extensions, the following file patterns are also skipped:

  * `*lock.json`, `*lock.yaml`, `*lock.yml` - Lock files with specific patterns
  * `go.sum` - Go module checksum files
  * `*.bundle.js`, `*.chunk.js` - JavaScript bundle files
  * `**/generated/**`, `**/*.generated.*` - Generated files
  * `*_snapshot.json` - Snapshot files
</Accordion>

## Customizing Files to Skip

You can add additional files or paths to skip during code review by specifying them in your custom guidelines file. This is useful for repository-specific generated files, large data files, or other content that shouldn't be reviewed.

### Adding Custom File Paths to Ignore

Use the `file_paths_to_ignore` section in your `code_review_guidelines.yaml` file. This field supports doublestar glob patterns for flexible matching.

```yaml theme={null}
# File paths to ignore during code review (supports doublestar glob patterns)
file_paths_to_ignore:
  - "services/code_review/**/category_taxonomy.json"
  - "**/generated/**"
  - "**/*.generated.ts"
  - "dist/**"
  - "build/**"
```

<Accordion title="Complete Example with Custom Ignores">
  ```yaml theme={null}
  # Guidelines for myproject

  # Custom files to skip during review
  file_paths_to_ignore:
    - "services/code_review/**/category_taxonomy.json"
    - "**/*.generated.graphql"
    - "public/assets/**"

  areas:
    databases:
      description: "Data and Database related rules"
      globs:
        - "**"
      rules:
        - id: "no_pii_in_bigquery"
          description: "Never store PII data in BigQuery tables."
          severity: "high"
  ```
</Accordion>


# Review Preferences
Source: https://docs.augmentcode.com/codereview/review-preferences

Configure your code review preferences to customize how Augment Code Review analyzes your pull requests.

<Tabs>
  <Tab title="Review Style">
    ## Choose Your Review Style

    Augment Code Review offers two review styles to match your team's preferences. Both maintain the same low false positive rate while offering different levels of coverage.

    ### Available Review Styles

    Set your review style on the [Configuration page](https://app.augmentcode.com/settings/code-review).

    * **Thorough**: Provides comprehensive coverage, catching 50% more bugs than Precise. Ideal for teams that want maximum code quality assurance.

    * **Precise**: Focuses on the most critical issues with fewer overall comments. Best for teams that prefer a more targeted review approach.

    <Note>
      **Thorough** is the default review style for all users, but you can switch to **Precise** at any time.
    </Note>
  </Tab>
</Tabs>


# Setup Guide for Enterprise
Source: https://docs.augmentcode.com/codereview/setup-guide-enterprise

Configure Augment Code Review for Enterprise accounts with multi-organization support.

## Using Augment Code Review natively inside of GitHub

Augment Code Review helps professional software teams complete code-reviews faster inside GitHub while also catching more critical bugs before they hit production. Backed by Augment's industry-leading Context Engine, the agent understands your codebase at a deep level, providing reviews that are more meaningful and account for codebase-wide effects. Augment prioritizes high signal-to-noise ratio by focusing on high-impact issues like bugs, security concerns, correctness, and cross-system problems while avoiding low-value style nags.

<Note>
  Augment Code Review relies on the Augment GitHub App which is only compatible with GitHub Enterprise Cloud and github.com. GitHub Enterprise Server is not currently supported.
</Note>

## About the installation process

Visit [app.augmentcode.com/settings/code-review](https://app.augmentcode.com/settings/code-review) and log in. Settings are accessible to all members of the Enterprise plan, but only configurable for Administrators of the Enterprise plan. If you aren't sure if you are an Administrator, please contact your solutions team.

### Configure Repo Access inside of the Augment GitHub App

Before you can configure repositories, click on "Connect GitHub" to install the Augment GitHub App. This will redirect you to GitHub to provide permissions for all the repos you grant Augment Code Review to engage.

<img alt="Code Review Settings Configure button" />

If your firewall configuration, allowlist or network policy requires a static IP for this integration, please refer to our [static IP address](https://docs.augmentcode.com/setup-augment/static-ip-support#allow-augment-traffic-from-static-ips) documentation.

<AccordionGroup>
  <Accordion title="Who can install the Augment GitHub App?">
    To install the Augment GitHub App, you will need to be an Administrator of your GitHub organization. To find who the Administrators are, visit your GitHub organization settings page and click on "People." Administrators are listed under "Owners."

    <img alt="GitHub Admins" />
  </Accordion>
</AccordionGroup>

Once you finish installing the GitHub app, you should see a green checkmark with the text "All set!". Then, back in the Augment Code Review Settings, should now show a green "Installed" badge. If you do not see either of these, you may need to uninstall the app through GitHub and reinstall it. See [Troubleshooting](/codereview/troubleshooting#stuck-on-install-button) for more help.

<img alt="GitHub App Installed" />

### Permissions requested by the Augment GitHub App:

* Contents, read-only: Clone repositories

* Pull Requests, read and write: Read pull requests and post comments to pull requests

* Issues, read-only: Read top-level PRs / Issues

* Organization Members, read-only: Read members of an organization, to distinguish internal and external users and their access levels to Augment features

Organization owners and repository admins can install the app directly; others will need owner approval. See [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) for details. If your organization uses [Augment for Slack,](https://docs.augmentcode.com/setup-augment/install-slack-app) the same selections will apply to both Augment for Slack and Augment Code Review.

<img alt="Installing the GitHub app on a single repository" />

You can modify repository access anytime in the Augment GitHub App settings.

### Configuring Triggers Per Repository

As the Administrator, you control when Augment Code Review triggers via [Settings](https://app.augmentcode.com/settings/code-review). Look for "Set Review Trigger" to the right of the repository name.

* **Automatic**: Augment Code Review will automatically review and post a comment as soon as the PR is opened for review in GitHub. Use it when your teams want immediate feedback on all pull requests.

* **Manual Command**: Augment Code Review is only triggered when someone comments on the PR with any of the following:  `auggie review`, `augment review`, or `augmentcode review` on GitHub. Use it when you want full control over when a review happens.

* **Disabled**: Augment Code Review will not run on the repository.

<img alt="Trigger Types" />

If the repo is set to "Automatic" or "Manual Command", to run additional rounds of reviews on a subsequent commit of any PR, you can use the same manual trigger keywords (`auggie review`, `augment review`, or `augmentcode review`).

On public repositories, reviews are only triggered for PRs whose authors are members of the GitHub organization, outside collaborators to the organization or repository, or contributors to that repository.

## Next Steps

Now that you've completed the basic setup, explore these additional features to get the most out of Augment Code Review:

<CardGroup>
  <Card title="Adding Another Organization" icon="building" href="/codereview/adding-another-organization">
    Configure Code Review across multiple GitHub organizations
  </Card>

  <Card title="Review Guidelines" icon="list-check" href="/codereview/review-guidelines">
    Set custom guidelines to focus reviews on specific areas
  </Card>

  <Card title="MCP Context" icon="plug" href="/codereview/mcp-context">
    Connect external context sources via Model Context Protocol
  </Card>

  <Card title="User Access" icon="users" href="/codereview/user-access">
    Manage which users can trigger Code Review
  </Card>

  <Card title="Analytics Dashboard" icon="chart-line" href="/codereview/analytics-dashboard">
    Track metrics and measure Code Review impact
  </Card>

  <Card title="Providing Feedback" icon="thumbs-up" href="/codereview/providing-feedback">
    Learn how to provide feedback on reviews
  </Card>
</CardGroup>

## Need Help?

If you encounter any issues during setup, check out our [Troubleshooting](/codereview/troubleshooting) guide.


# Setup Guide for All Other Plans
Source: https://docs.augmentcode.com/codereview/setup-guide-otherplans

Get started with Augment Code Review for Indie, Standard and Max plans.

## Using Augment Code Review

Augment Code Review is available as an add-on feature for individuals and teams. It provides automated code review directly in GitHub, helping you catch bugs and improve code quality before merging. Backed by Augment’s industry-leading Context Engine, the agent understands your codebase at a deep level, providing reviews that are more meaningful and account for codebase-wide effects. Augment prioritizes high signal-to-noise ratio by focusing on high-impact issues like bugs, security concerns, correctness, and cross-system problems while avoiding low-value style nags.

## About the installation process

Visit [app.augmentcode.com/settings/code-review](https://app.augmentcode.com/settings/code-review) and log in. Settings are accessible to all [Team members](https://docs.augmentcode.com/teams/teams-admin-guide), but only configurable by Administrators of the plan.

### Configure Repo Access inside of the Augment GitHub App

Administrators can configure repositories by clicking "Connect GitHub" to launch the Augment GitHub App. This will redirect you to GitHub to provide permissions for all the repos you grant Augment Code Review to engage.

<img alt="Code Review Settings Configure button" />

If your firewall configuration, allowlist or network policy requires a static IP for this integration, please refer to our [static IP address](https://docs.augmentcode.com/setup-augment/static-ip-support#allow-augment-traffic-from-static-ips) documentation.

<AccordionGroup>
  <Accordion title="Who can install the Augment GitHub App?">
    To install the Augment GitHub App, you will need to be an Administrator of your GitHub organization. To find who the Administrators are, visit your GitHub organization settings page and click on "People." Administrators are listed under "Owners."

    <img alt="GitHub Admins" />
  </Accordion>
</AccordionGroup>

Once you finish installing the GitHub app, you should see a green checkmark with the text "All set!". Then, back in the Augment Code Review Settings, should now show a green "Installed" badge. If you do not see either of these, you may need to uninstall the app through GitHub and reinstall it. See [Troubleshooting](/codereview/troubleshooting#stuck-on-install-button) for more help.

<img alt="GitHub App Installed" />

### Permissions requested by the Augment GitHub App:

* Contents, read-only: Clone repositories

* Pull Requests, read and write: Read pull requests and post comments to pull requests

* Issues, read-only: Read top-level PRs / Issues

* Organization Members, read-only: Read members of an organization, to distinguish internal and external users and their access levels to Augment features

Organization owners and repository admins can install the app directly; others will need owner approval. See [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) for details.

<img alt="Installing the GitHub app on a single repository" />

You can modify repository access anytime in the Augment GitHub App settings.

### Configuring Triggers Per Repository

As the Administrator, you control when Augment Code Review triggers via [Settings](https://app.augmentcode.com/settings/code-review). Look for "Set Review Trigger" to the right of the repository name.

* **Automatic**: Augment Code Review will automatically review and post a comment as soon as the PR is opened for review in GitHub. Use it when your teams want immediate feedback on all pull requests.

* **Manual Command**: Augment Code Review is only triggered when someone comments on the PR with any of the following:  `auggie review`, `augment review`, or `augmentcode review` on GitHub. Use it when you want full control over when a review happens.

* **Disabled**: Augment Code Review will not run on the repository.

<img alt="Trigger Types" />

If the repo is set to "Automatic" or "Manual Command", to run additional rounds of reviews on a subsequent commit of any PR, you can use the same manual trigger keywords (`auggie review`, `augment review`, or `augmentcode review`).

On public repositories, reviews are only triggered for PRs whose authors are members of the GitHub organization, outside collaborators to the organization or repository, or contributors to that repository.

<Note>
  If you are an Enterprise customer, please refer to the [Enterprise setup guide](/codereview/setup-guide-enterprise) for additional information.
</Note>

## Questions?

If you have questions about Augment Code Review or want to learn more about Enterprise features:

* Visit our [Support Center](https://support.augmentcode.com/)
* Join our [Subreddit](https://www.reddit.com/r/AugmentCodeAI/)
* Contact Us [Augment Support](https://portal.usepylon.com/augment-code/forms/augment-support)

## Related Resources

* [Code Review Overview](/codereview/overview) - Learn about Code Review features
* [Fix with Augment](/codereview/fix-with-augment) - Automatically fix issues in your IDE
* [Setup Guide for Enterprise](/codereview/setup-guide-enterprise) - Full setup instructions for Enterprise


# Troubleshooting
Source: https://docs.augmentcode.com/codereview/troubleshooting

Common issues and solutions for Augment Code Review setup and configuration.

## Known issues and Remediations

### Stuck on Install button

If you still see the "Install" button on the Augment Code Review Settings page, then the Augment GitHub App installation failed. You will need to uninstall the Augment GitHub App from your organization and then reinstall it. Make sure the person installing the GitHub app has an Augment account and they see the "All set!" text after installing the app.

<Steps>
  <Step title="Navigate to the Augment GitHub App settings page on GitHub">
    Follow the steps on [GitHub Docs](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify) to modify the Augment GitHub App installation.
  </Step>

  <Step title="Uninstall the Augment GitHub App from your organization">
    In the Danger zone section, click on "Uninstall"
  </Step>

  <Step title="Reinstall the Augment GitHub App">
    Follow the steps in [Configure Repo Access](/codereview/setup-guide-enterprise#configure-repo-access-inside-of-the-augment-github-app) again to install the app
  </Step>
</Steps>

### Unable to see the repositories from Organization just added

If you are unable to see the repositories from an organization you just added, then the Augment GitHub App installation failed for that organization. You will need to uninstall the Augment GitHub App from your organization and then reinstall it. Make sure the GitHub administrator installing the GitHub app has an Augment account and they see the "All set!" text after installing the app.

<Steps>
  <Step title="Navigate to the Augment GitHub App settings page on GitHub">
    Follow the steps on [GitHub Docs](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify) to modify the Augment GitHub App installation.
  </Step>

  <Step title="Uninstall the Augment GitHub App from your organization">
    In the Danger zone section, click on "Uninstall"
  </Step>

  <Step title="Reinstall the Augment GitHub App">
    Follow the steps in [Configure Repo Access](/codereview/setup-guide-enterprise#configure-repo-access-inside-of-the-augment-github-app) again to install the app
  </Step>
</Steps>


# User Access
Source: https://docs.augmentcode.com/codereview/user-access

Manage which GitHub users can trigger Augment Code Review with allowlist mode.

## User Access

Enterprise Plan administrators are able to specify a list of GitHub users who can trigger Augment Code Review by turning on **Allowlist Mode**.

When Allowlist Mode is active, only users in the allowlist will be able to trigger Augment Code Review. Automatic and manual reviews will be disabled for all other users. This is useful for organizations that want to limit access to the feature to a select group of users.

Administrators can manage permissions at [User Access for Code Review](https://app.augmentcode.com/settings/code-review/user-access).


# Custom Client
Source: https://docs.augmentcode.com/context-services/context-connectors/advanced/custom-client

Build custom search clients for your applications

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

Build custom search clients to load indexes and provide search functionality for web apps, CLIs, or serverless functions.

## Basic Search Client

<Tabs>
  <Tab title="TypeScript">
    ```typescript theme={null}
    import { SearchClient, FilesystemStore } from "@augmentcode/context-connectors";

    // Create a search client
    const client = new SearchClient({
      store: new FilesystemStore({ basePath: "./indexes" }),
      indexName: "my-docs",
    });

    // Initialize (loads index from store)
    await client.initialize();

    // Search
    const { results } = await client.search("authentication");
    console.log(results);

    // Ask a question about the search results
    const answer = await client.searchAndAsk(
      "authentication",
      "How does auth work?"
    );
    console.log(answer);
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={null}
    from auggie_sdk.context import DirectContext
    import os

    class SearchClient:
        def __init__(self, index_name: str, store_path: str = None):
            self.index_name = index_name
            self.store_path = store_path
            self.context = None

        def initialize(self):
            # Load search-optimized state (smaller, no file list)
            search_file = os.path.join(self.store_path, self.index_name, 'search.json')
            self.context = DirectContext.import_from_file(search_file)

        def search(self, query: str):
            return self.context.search(query)

        def ask(self, search_query: str, prompt: str = None):
            return self.context.search_and_ask(search_query, prompt)

    # Usage
    client = SearchClient('my-docs', store_path='./indexes')
    client.initialize()
    results = client.search('authentication')
    answer = client.ask('authentication', 'How does auth work?')
    ```
  </Tab>
</Tabs>

<Note>
  Search clients load `search.json` which is optimized for search operations.
  The full `state.json` file is only needed by indexers for incremental updates.
</Note>

## Web Application

<Tabs>
  <Tab title="TypeScript (Express)">
    ```typescript theme={null}
    import express from "express";
    import { SearchClient, FilesystemStore } from "@augmentcode/context-connectors";

    const app = express();
    app.use(express.json());

    // Initialize client at startup
    const client = new SearchClient({
      store: new FilesystemStore(),
      indexName: "my-docs",
    });
    await client.initialize();

    app.post("/api/search", async (req, res) => {
      const { query } = req.body;
      const { results } = await client.search(query);
      res.json({ results });
    });

    app.post("/api/ask", async (req, res) => {
      const { query, question } = req.body;
      const answer = await client.searchAndAsk(query, question);
      res.json({ answer });
    });

    app.listen(3000);
    ```
  </Tab>

  <Tab title="Python (Flask)">
    ```python theme={null}
    from flask import Flask, request, jsonify

    app = Flask(__name__)
    client = SearchClient('my-docs')
    client.initialize()

    @app.post('/api/search')
    def search():
        query = request.json['query']
        results = client.search(query)
        return jsonify({'results': results})

    @app.post('/api/ask')
    def ask():
        query = request.json['query']
        prompt = request.json.get('prompt')
        answer = client.ask(query, prompt)
        return jsonify({'answer': answer})
    ```
  </Tab>
</Tabs>

## CLI Client

<Tabs>
  <Tab title="TypeScript">
    ```typescript theme={null}
    import { program } from "commander";
    import { SearchClient, FilesystemStore } from "@augmentcode/context-connectors";

    program
      .command("search <query>")
      .option("-i, --index <name>", "Index name", "my-project")
      .action(async (query, options) => {
        const client = new SearchClient({
          store: new FilesystemStore(),
          indexName: options.index,
        });
        await client.initialize();
        const { results } = await client.search(query);
        console.log(results);
      });

    program
      .command("ask <query>")
      .option("-i, --index <name>", "Index name", "my-project")
      .option("-q, --question <question>", "Question to ask")
      .action(async (query, options) => {
        const client = new SearchClient({
          store: new FilesystemStore(),
          indexName: options.index,
        });
        await client.initialize();
        const answer = await client.searchAndAsk(query, options.question);
        console.log(answer);
      });

    program.parse();
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={null}
    import click

    @click.group()
    def cli():
        pass

    @cli.command()
    @click.argument('query')
    @click.option('--index', default='my-project')
    def search(query, index):
        client = SearchClient(index)
        client.initialize()
        print(client.search(query))

    @cli.command()
    @click.argument('query')
    @click.option('--index', default='my-project')
    @click.option('--prompt')
    def ask(query, index, prompt):
        client = SearchClient(index)
        client.initialize()
        print(client.ask(query, prompt))

    if __name__ == '__main__':
        cli()
    ```
  </Tab>
</Tabs>

## Serverless Function

<Tabs>
  <Tab title="TypeScript (AWS Lambda)">
    ```typescript theme={null}
    import { SearchClient, S3Store } from "@augmentcode/context-connectors";

    let client: SearchClient | null = null;

    async function getClient() {
      if (!client) {
        client = new SearchClient({
          store: new S3Store({ bucket: "my-indexes" }),
          indexName: "my-docs",
        });
        await client.initialize();
      }
      return client;
    }

    export async function handler(event: any) {
      const body = JSON.parse(event.body || "{}");
      const { query } = body;

      const client = await getClient();
      const { results } = await client.search(query);

      return {
        statusCode: 200,
        body: JSON.stringify({ results }),
      };
    }
    ```
  </Tab>

  <Tab title="Python (AWS Lambda)">
    ```python theme={null}
    import json

    client = None

    def get_client():
        global client
        if client is None:
            client = SearchClient('my-docs')
            client.initialize()
        return client

    def lambda_handler(event, context):
        body = json.loads(event.get('body', '{}'))
        query = body.get('query')

        client = get_client()
        results = client.search(query)

        return {
            'statusCode': 200,
            'body': json.dumps({'results': results})
        }
    ```
  </Tab>
</Tabs>

## Next Steps

* [Custom Indexer](/context-services/context-connectors/advanced/custom-indexer) - Build custom indexers
* [Custom Store](/context-services/context-connectors/advanced/custom-store) - Custom storage backends
* [DirectContext API Reference](/context-services/sdk/api-reference) - Complete API docs


# Custom Indexer
Source: https://docs.augmentcode.com/context-services/context-connectors/advanced/custom-indexer

Build a custom indexer for any data source using DirectContext

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

Build a custom indexer to fetch content from any source (API, database, CMS) and index it with DirectContext.

## Basic Example

<Tabs>
  <Tab title="TypeScript">
    ```typescript theme={null}
    import { Indexer, FilesystemStore } from "@augmentcode/context-connectors";
    import type { Source, FileEntry, FileChanges, SourceMetadata, FileInfo } from "@augmentcode/context-connectors";

    // Implement the Source interface for your data source
    class ApiSource implements Source {
      readonly type = "custom" as const;

      async fetchAll(): Promise<FileEntry[]> {
        // Replace with your actual data source (API, database, CMS, etc.)
        const response = await fetch("https://api.example.com/docs");
        const docs = await response.json();
        return docs.map((doc: any) => ({
          path: doc.path,
          contents: doc.content,
        }));
      }

      async fetchChanges(previous: SourceMetadata): Promise<FileChanges | null> {
        // Return null to always do full re-index
        // Or implement incremental updates based on your data source
        return null;
      }

      async getMetadata(): Promise<SourceMetadata> {
        return {
          type: "custom",
          identifier: "api-docs",
          ref: new Date().toISOString(),
          syncedAt: new Date().toISOString(),
        };
      }

      async listFiles(directory?: string): Promise<FileInfo[]> {
        const files = await this.fetchAll();
        return files.map(f => ({ path: f.path, type: "file" as const }));
      }

      async readFile(path: string): Promise<string | null> {
        const files = await this.fetchAll();
        return files.find(f => f.path === path)?.contents ?? null;
      }
    }

    // Usage
    const source = new ApiSource();
    const store = new FilesystemStore({ basePath: "./indexes" });
    const indexer = new Indexer();

    const result = await indexer.index(source, store, "my-docs");
    console.log(`Indexed ${result.filesIndexed} files (${result.type})`);
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={null}
    from auggie_sdk.context import DirectContext, File
    import json
    import os
    from pathlib import Path

    class CustomIndexer:
        def __init__(self, store_path: str = None):
            self.store_path = store_path

        def fetch_files(self):
            """Fetch from your data source (API, database, CMS, etc.)"""
            # Replace with your actual data source
            return [
                File(path='docs/intro.md', contents='# Introduction\n...'),
                File(path='docs/api.md', contents='# API Reference\n...'),
            ]

        def index(self, index_name: str):
            index_dir = os.path.join(self.store_path, index_name)
            state_file = os.path.join(index_dir, 'state.json')

            # Load existing or create new context
            if os.path.exists(state_file):
                context = DirectContext.import_from_file(state_file)
            else:
                context = DirectContext.create()

            # Fetch and index files
            files = self.fetch_files()

            # Handle incremental updates
            indexed_paths = set(context.get_indexed_paths())
            current_paths = {f.path for f in files}
            paths_to_remove = [p for p in indexed_paths if p not in current_paths]

            if paths_to_remove:
                context.remove_from_index(paths_to_remove)

            context.add_to_index(files)

            # Export both full and search-only states
            full_state = context.export(mode='full')
            search_state = context.export(mode='search-only')

            # Save both files
            Path(index_dir).mkdir(parents=True, exist_ok=True)

            with open(os.path.join(index_dir, 'state.json'), 'w') as f:
                json.dump(full_state, f, indent=2)

            with open(os.path.join(index_dir, 'search.json'), 'w') as f:
                json.dump(search_state, f, indent=2)

    # Usage
    indexer = CustomIndexer(store_path='./indexes')
    indexer.index('my-docs')
    ```
  </Tab>
</Tabs>

<Note>
  **Index Layout:** The indexer saves two files:

  * `state.json` - Full state including file path list (for incremental indexing)
  * `search.json` - Optimized state without file list (smaller, for search clients)

  Search clients should load `search.json`. Indexers need `state.json` for incremental updates.
</Note>

## Data Source Examples

<Tabs>
  <Tab title="TypeScript">
    **REST API:**

    ```typescript theme={null}
    async fetchAll(): Promise<FileEntry[]> {
      const response = await fetch("https://api.example.com/docs");
      const docs = await response.json();
      return docs.map((doc: any) => ({ path: doc.path, contents: doc.content }));
    }
    ```

    **Database:**

    ```typescript theme={null}
    async fetchAll(): Promise<FileEntry[]> {
      const docs = await db.query("SELECT path, content FROM documents");
      return docs.map(doc => ({ path: doc.path, contents: doc.content }));
    }
    ```
  </Tab>

  <Tab title="Python">
    **REST API:**

    ```python theme={null}
    def fetch_files(self):
        response = requests.get('https://api.example.com/docs')
        return [File(path=doc['path'], contents=doc['content']) for doc in response.json()]
    ```

    **Database:**

    ```python theme={null}
    def fetch_files(self):
        docs = db.query('SELECT path, content FROM documents')
        return [File(path=doc.path, contents=doc.content) for doc in docs]
    ```
  </Tab>
</Tabs>

## Automation

**Cron (Node.js):**

```bash theme={null}
0 * * * * cd /path/to/project && npx tsx indexer.ts
```

**Cron (Python):**

```bash theme={null}
0 * * * * cd /path/to/project && python indexer.py
```

**GitHub Actions:** See [GitHub Actions Auto-Indexing](/context-services/context-connectors/quickstart/github-actions-indexing)

## Next Steps

* [Custom Store](/context-services/context-connectors/advanced/custom-store) - Custom storage backends
* [Custom Client](/context-services/context-connectors/advanced/custom-client) - Build search clients
* [DirectContext API Reference](/context-services/sdk/api-reference) - Complete API docs


# Custom Store
Source: https://docs.augmentcode.com/context-services/context-connectors/advanced/custom-store

Create custom storage backends for your indexes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

Create custom storage backends to save and load DirectContext state from local filesystem, S3, or any storage system.

## Local Filesystem Store

<Tabs>
  <Tab title="TypeScript">
    ```typescript theme={null}
    import { promises as fs } from "node:fs";
    import { join } from "node:path";
    import type { IndexStore, IndexState, IndexStateSearchOnly } from "@augmentcode/context-connectors";

    class LocalStore implements IndexStore {
      constructor(private basePath: string = "./indexes") {}

      async save(key: string, fullState: IndexState, searchState: IndexStateSearchOnly): Promise<void> {
        const indexDir = join(this.basePath, key);
        await fs.mkdir(indexDir, { recursive: true });

        // Full state for incremental indexing
        await fs.writeFile(join(indexDir, "state.json"), JSON.stringify(fullState, null, 2));
        // Search-optimized state (smaller)
        await fs.writeFile(join(indexDir, "search.json"), JSON.stringify(searchState, null, 2));
      }

      async loadState(key: string): Promise<IndexState | null> {
        try {
          const data = await fs.readFile(join(this.basePath, key, "state.json"), "utf-8");
          return JSON.parse(data);
        } catch {
          return null;
        }
      }

      async loadSearch(key: string): Promise<IndexState | null> {
        try {
          const data = await fs.readFile(join(this.basePath, key, "search.json"), "utf-8");
          return JSON.parse(data);
        } catch {
          return null;
        }
      }

      async delete(key: string): Promise<void> {
        await fs.rm(join(this.basePath, key), { recursive: true, force: true });
      }

      async list(): Promise<string[]> {
        const entries = await fs.readdir(this.basePath, { withFileTypes: true });
        return entries.filter(e => e.isDirectory()).map(e => e.name);
      }
    }
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={null}
    import json
    import os
    from pathlib import Path

    class LocalStore:
        def __init__(self, base_path: str = None):
            self.base_path = base_path

        def save(self, index_name: str, full_state, search_state):
            """Save both full state and search-optimized state."""
            index_dir = os.path.join(self.base_path, index_name)
            Path(index_dir).mkdir(parents=True, exist_ok=True)

            # Full state for incremental indexing
            with open(os.path.join(index_dir, 'state.json'), 'w') as f:
                json.dump(full_state, f, indent=2)

            # Search-optimized state (smaller)
            with open(os.path.join(index_dir, 'search.json'), 'w') as f:
                json.dump(search_state, f, indent=2)

        def load_state(self, index_name: str):
            """Load full state for incremental indexing."""
            state_path = os.path.join(self.base_path, index_name, 'state.json')
            if not os.path.exists(state_path):
                return None
            with open(state_path, 'r') as f:
                return json.load(f)

        def load_search(self, index_name: str):
            """Load search-optimized state for search operations."""
            search_path = os.path.join(self.base_path, index_name, 'search.json')
            if not os.path.exists(search_path):
                return None
            with open(search_path, 'r') as f:
                return json.load(f)

    # Usage
    store = LocalStore(base_path='./indexes')
    context = DirectContext.create()
    context.add_to_index([File(path='file.py', contents='...')])

    # Export both states
    full_state = context.export(mode='full')
    search_state = context.export(mode='search-only')

    store.save('my-project', full_state, search_state)
    ```
  </Tab>
</Tabs>

## S3 Store

<Tabs>
  <Tab title="TypeScript">
    ```typescript theme={null}
    import { S3Client, GetObjectCommand, PutObjectCommand } from "@aws-sdk/client-s3";
    import type { IndexStore, IndexState, IndexStateSearchOnly } from "@augmentcode/context-connectors";

    class S3Store implements IndexStore {
      private client: S3Client;

      constructor(
        private bucket: string,
        private prefix = "context-connectors/"
      ) {
        this.client = new S3Client({});
      }

      async save(key: string, fullState: IndexState, searchState: IndexStateSearchOnly): Promise<void> {
        await Promise.all([
          this.client.send(new PutObjectCommand({
            Bucket: this.bucket,
            Key: `${this.prefix}${key}/state.json`,
            Body: JSON.stringify(fullState, null, 2),
            ContentType: "application/json",
          })),
          this.client.send(new PutObjectCommand({
            Bucket: this.bucket,
            Key: `${this.prefix}${key}/search.json`,
            Body: JSON.stringify(searchState, null, 2),
            ContentType: "application/json",
          })),
        ]);
      }

      async loadState(key: string): Promise<IndexState | null> {
        try {
          const response = await this.client.send(new GetObjectCommand({
            Bucket: this.bucket,
            Key: `${this.prefix}${key}/state.json`,
          }));
          const body = await response.Body?.transformToString();
          return body ? JSON.parse(body) : null;
        } catch {
          return null;
        }
      }

      async loadSearch(key: string): Promise<IndexState | null> {
        try {
          const response = await this.client.send(new GetObjectCommand({
            Bucket: this.bucket,
            Key: `${this.prefix}${key}/search.json`,
          }));
          const body = await response.Body?.transformToString();
          return body ? JSON.parse(body) : null;
        } catch {
          return null;
        }
      }

      // ... delete() and list() implementations
    }

    // Usage
    const store = new S3Store("my-bucket");
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={null}
    import boto3
    import json

    class S3Store:
        def __init__(self, bucket: str, prefix: str = 'context-connectors/'):
            self.s3 = boto3.client('s3')
            self.bucket = bucket
            self.prefix = prefix

        def save(self, index_name: str, full_state, search_state):
            """Save both full state and search-optimized state."""
            state_key = f'{self.prefix}{index_name}/state.json'
            search_key = f'{self.prefix}{index_name}/search.json'

            self.s3.put_object(
                Bucket=self.bucket,
                Key=state_key,
                Body=json.dumps(full_state, indent=2)
            )
            self.s3.put_object(
                Bucket=self.bucket,
                Key=search_key,
                Body=json.dumps(search_state, indent=2)
            )

        def load_state(self, index_name: str):
            """Load full state for incremental indexing."""
            key = f'{self.prefix}{index_name}/state.json'
            try:
                response = self.s3.get_object(Bucket=self.bucket, Key=key)
                return json.loads(response['Body'].read())
            except self.s3.exceptions.NoSuchKey:
                return None

        def load_search(self, index_name: str):
            """Load search-optimized state for search operations."""
            key = f'{self.prefix}{index_name}/search.json'
            try:
                response = self.s3.get_object(Bucket=self.bucket, Key=key)
                return json.loads(response['Body'].read())
            except self.s3.exceptions.NoSuchKey:
                return None

    # Usage
    store = S3Store('my-bucket')
    store.save('my-project', full_state, search_state)
    ```
  </Tab>
</Tabs>

<Note>
  **Built-in S3 Store:** The `@augmentcode/context-connectors` package includes a built-in `S3Store` class. Use it directly:

  ```typescript theme={null}
  import { S3Store } from "@augmentcode/context-connectors";
  const store = new S3Store({ bucket: "my-bucket" });
  ```
</Note>

## Other Storage Examples

<Tabs>
  <Tab title="TypeScript">
    **Redis:**

    ```typescript theme={null}
    import { createClient } from "redis";
    import type { IndexStore, IndexState, IndexStateSearchOnly } from "@augmentcode/context-connectors";

    class RedisStore implements IndexStore {
      constructor(private redis: ReturnType<typeof createClient>) {}

      async save(key: string, fullState: IndexState, searchState: IndexStateSearchOnly): Promise<void> {
        await Promise.all([
          this.redis.set(`context:${key}:state`, JSON.stringify(fullState)),
          this.redis.set(`context:${key}:search`, JSON.stringify(searchState)),
        ]);
      }

      async loadState(key: string): Promise<IndexState | null> {
        const data = await this.redis.get(`context:${key}:state`);
        return data ? JSON.parse(data) : null;
      }

      async loadSearch(key: string): Promise<IndexState | null> {
        const data = await this.redis.get(`context:${key}:search`);
        return data ? JSON.parse(data) : null;
      }
      // ... delete() and list() implementations
    }
    ```
  </Tab>

  <Tab title="Python">
    **Redis:**

    ```python theme={null}
    class RedisStore:
        def save(self, index_name: str, full_state, search_state):
            self.redis.set(f'context:{index_name}:state', json.dumps(full_state))
            self.redis.set(f'context:{index_name}:search', json.dumps(search_state))

        def load_state(self, index_name: str):
            data = self.redis.get(f'context:{index_name}:state')
            return json.loads(data) if data else None

        def load_search(self, index_name: str):
            data = self.redis.get(f'context:{index_name}:search')
            return json.loads(data) if data else None
    ```

    **Database:**

    ```python theme={null}
    class DatabaseStore:
        def save(self, index_name: str, full_state, search_state):
            self.db.execute('''
                INSERT INTO indexes (name, full_state, search_state)
                VALUES (%s, %s, %s)
                ON CONFLICT (name) DO UPDATE
                SET full_state = %s, search_state = %s
            ''', [index_name, json.dumps(full_state), json.dumps(search_state),
                  json.dumps(full_state), json.dumps(search_state)])

        def load_state(self, index_name: str):
            row = self.db.query_one('SELECT full_state FROM indexes WHERE name = %s', [index_name])
            return json.loads(row['full_state']) if row else None

        def load_search(self, index_name: str):
            row = self.db.query_one('SELECT search_state FROM indexes WHERE name = %s', [index_name])
            return json.loads(row['search_state']) if row else None
    ```
  </Tab>
</Tabs>

## Index File Layout

Each index consists of two files:

| File          | Purpose                    | Size    | Used By                            |
| ------------- | -------------------------- | ------- | ---------------------------------- |
| `state.json`  | Full state with file paths | Larger  | Indexers (for incremental updates) |
| `search.json` | Search-optimized state     | Smaller | Search clients                     |

The `search.json` file excludes the blobs array (list of indexed file paths), making it much smaller for search-only use cases. Indexers need the full `state.json` to determine which files have changed for incremental updates.

## Next Steps

* [Custom Indexer](/context-services/context-connectors/advanced/custom-indexer) - Build custom indexers
* [Custom Client](/context-services/context-connectors/advanced/custom-client) - Build search clients
* [Store Indexes in S3](/context-services/context-connectors/quickstart/share-with-s3) - S3 storage guide


# CLI Reference
Source: https://docs.augmentcode.com/context-services/context-connectors/cli-reference

Complete command-line reference for Context Connectors

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Global Requirements

All commands require these environment variables:

```bash theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
```

## Data Storage

By default, indexes are stored at `~/.augment/context-connectors`.

Override with `--store-path` or the `CONTEXT_CONNECTORS_STORE_PATH` environment variable.

## Commands

### `index` - Index a data source

Index code from various sources using source-specific subcommands.

```bash theme={null}
npx ctxc index <source> [options]
```

#### Subcommands

| Source      | Description                  |
| ----------- | ---------------------------- |
| `github`    | Index a GitHub repository    |
| `gitlab`    | Index a GitLab project       |
| `bitbucket` | Index a Bitbucket repository |
| `website`   | Crawl and index a website    |

***

#### `index github`

```bash theme={null}
npx ctxc index github [options]
```

| Option               | Description                 | Default |
| -------------------- | --------------------------- | ------- |
| `-i, --index <name>` | Index name (required)       | -       |
| `--owner <owner>`    | Repository owner (required) | -       |
| `--repo <repo>`      | Repository name (required)  | -       |
| `--ref <ref>`        | Branch, tag, or commit      | `HEAD`  |

**Environment:** Requires `GITHUB_TOKEN` with repo read access.

***

#### `index gitlab`

```bash theme={null}
npx ctxc index gitlab [options]
```

| Option               | Description                   | Default              |
| -------------------- | ----------------------------- | -------------------- |
| `-i, --index <name>` | Index name (required)         | -                    |
| `--project <id>`     | Project ID or path (required) | -                    |
| `--ref <ref>`        | Branch, tag, or commit        | `HEAD`               |
| `--gitlab-url <url>` | GitLab base URL (self-hosted) | `https://gitlab.com` |

**Environment:** Requires `GITLAB_TOKEN` with repo read access.

***

#### `index bitbucket`

```bash theme={null}
npx ctxc index bitbucket [options]
```

| Option                  | Description                             | Default                         |
| ----------------------- | --------------------------------------- | ------------------------------- |
| `-i, --index <name>`    | Index name (required)                   | -                               |
| `--workspace <slug>`    | Workspace slug (required)               | -                               |
| `--repo <repo>`         | Repository name (required)              | -                               |
| `--ref <ref>`           | Branch, tag, or commit                  | `HEAD`                          |
| `--bitbucket-url <url>` | Bitbucket base URL (Server/Data Center) | `https://api.bitbucket.org/2.0` |

**Environment:** Requires `BITBUCKET_TOKEN` with repo read access.

***

#### `index website`

```bash theme={null}
npx ctxc index website [options]
```

| Option                    | Description                     | Default |
| ------------------------- | ------------------------------- | ------- |
| `-i, --index <name>`      | Index name (required)           | -       |
| `--url <url>`             | Website URL to crawl (required) | -       |
| `--max-depth <n>`         | Maximum crawl depth             | `3`     |
| `--max-pages <n>`         | Maximum pages to crawl          | `100`   |
| `--include <patterns...>` | URL patterns to include (glob)  | -       |
| `--exclude <patterns...>` | URL patterns to exclude (glob)  | -       |

***

#### Store Options (all index subcommands)

| Option                | Description                    | Default           |
| --------------------- | ------------------------------ | ----------------- |
| `--store <type>`      | Store type: `filesystem`, `s3` | `filesystem`      |
| `--store-path <path>` | Store base path                | Platform-specific |

**S3 Configuration (environment variables):**

| Variable                 | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `AWS_ACCESS_KEY_ID`      | AWS access key (required for S3)                 |
| `AWS_SECRET_ACCESS_KEY`  | AWS secret key (required for S3)                 |
| `CC_S3_BUCKET`           | S3 bucket name                                   |
| `CC_S3_ENDPOINT`         | Custom endpoint URL (for S3-compatible services) |
| `CC_S3_FORCE_PATH_STYLE` | Use path-style URLs (`true`/`false`)             |

#### Examples

```bash theme={null}
# Index GitHub repo
export GITHUB_TOKEN='ghp_...'
npx ctxc index github --owner facebook --repo react -i react

# Index GitLab project
export GITLAB_TOKEN='glpat-...'
npx ctxc index gitlab --project mygroup/myrepo -i myrepo

# Index Bitbucket repo
export BITBUCKET_TOKEN='...'
npx ctxc index bitbucket --workspace myws --repo myrepo -i myrepo

# Index website
npx ctxc index website --url https://docs.example.com -i docs

# Index to S3
export CC_S3_BUCKET='my-team-indexes'
npx ctxc index github --owner myorg --repo myrepo -i my-project \
  --store s3
```

***

### `list` - List local indexes

List all indexes in the local store.

```bash theme={null}
npx ctxc list [options]
```

#### Optional Options

| Option                | Description             | Default                         |
| --------------------- | ----------------------- | ------------------------------- |
| `--store-path <path>` | Store path to list from | `~/.augment/context-connectors` |

#### Examples

```bash theme={null}
# List all local indexes
npx ctxc list

# List from custom store path
npx ctxc list --store-path /data/indexes
```

***

### `delete` - Delete a local index

Delete an index from the local store.

```bash theme={null}
npx ctxc delete <name> [options]
```

#### Arguments

| Argument | Description                            |
| -------- | -------------------------------------- |
| `<name>` | Name of the index to delete (required) |

#### Optional Options

| Option                | Description                     | Default                         |
| --------------------- | ------------------------------- | ------------------------------- |
| `--store-path <path>` | Store path containing the index | `~/.augment/context-connectors` |

#### Examples

```bash theme={null}
# Delete an index
npx ctxc delete my-project

# Delete from custom store path
npx ctxc delete my-project --store-path /data/indexes
```

***

### `search` - Search indexed content

Search indexed content and answer questions using an LLM.

```bash theme={null}
npx ctxc search <query> [options]
```

#### Arguments

| Argument  | Description                        |
| --------- | ---------------------------------- |
| `<query>` | Search query / question (required) |

#### Required Options

| Option               | Description                                            |
| -------------------- | ------------------------------------------------------ |
| `-i, --index <spec>` | Index spec: `name`, `path:/path`, or `s3://bucket/key` |

#### Optional Options

| Option                 | Description                                     | Default |
| ---------------------- | ----------------------------------------------- | ------- |
| `--raw`                | Return raw search results instead of LLM answer | `false` |
| `--max-chars <number>` | Maximum output characters (only with `--raw`)   | -       |

#### Index Spec Formats

| Format | Example                   | Description                   |
| ------ | ------------------------- | ----------------------------- |
| Name   | `my-project`              | Index from default store path |
| Path   | `path:/data/indexes/proj` | Direct filesystem path        |
| S3     | `s3://bucket/prefix/proj` | S3 location                   |

#### Examples

```bash theme={null}
# Ask a question (uses LLM to answer)
npx ctxc search "How does authentication work?" -i my-project

# Raw search results (no LLM)
npx ctxc search "authentication logic" -i my-project --raw

# Search S3-stored index
npx ctxc search "API routes" -i s3://my-bucket/indexes/my-project

# Search from a specific path
npx ctxc search "database queries" -i path:/data/indexes/my-project
```

***

### `agent` - Interactive AI agent

Run an interactive AI agent that can search and read your codebase.

```bash theme={null}
npx ctxc agent [query] [options]
```

#### Arguments

| Argument  | Description            |
| --------- | ---------------------- |
| `[query]` | Optional initial query |

#### Required Options

| Option                   | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| `-i, --index <specs...>` | Index spec(s): `name`, `path:/path`, or `s3://bucket/key` |
| `--provider <name>`      | LLM provider: `openai`, `anthropic`, `google`             |

#### Optional Options

| Option            | Description                                   | Default                   |
| ----------------- | --------------------------------------------- | ------------------------- |
| `--print`         | Non-interactive mode: print response and exit | `false`                   |
| `--model <name>`  | Model to use                                  | Provider-specific default |
| `--max-steps <n>` | Maximum agent steps                           | `10`                      |
| `-v, --verbose`   | Show tool calls                               | `false`                   |
| `--search-only`   | Disable file operations                       | `false`                   |

**Environment:** Requires provider-specific API key:

* OpenAI: `OPENAI_API_KEY`
* Anthropic: `ANTHROPIC_API_KEY`
* Google: `GOOGLE_API_KEY`

**Default Models:**

* OpenAI: `gpt-5-mini`
* Anthropic: `claude-haiku-4-5`
* Google: `gemini-3-flash-preview`

#### Examples

```bash theme={null}
# Interactive mode (default)
export OPENAI_API_KEY='sk-...'
npx ctxc agent -i my-project --provider openai

# Interactive mode with initial query (continues interactively after response)
export ANTHROPIC_API_KEY='sk-ant-...'
npx ctxc agent -i my-project --provider anthropic "How does auth work?"

# Non-interactive mode (prints response and exits)
npx ctxc agent -i my-project --provider anthropic "How does auth work?" --print

# Multiple indexes
npx ctxc agent -i my-project -i s3://bucket/other-project --provider openai

# Verbose mode
npx ctxc agent -i my-project --provider openai --verbose
```

***

### `mcp stdio` - Run as MCP server (stdio)

Run as an MCP server using stdio transport for integration with MCP-compatible agents like Claude Desktop.

```bash theme={null}
npx ctxc mcp stdio [options]
```

#### Optional Options

| Option                   | Description                                               | Default     |
| ------------------------ | --------------------------------------------------------- | ----------- |
| `-i, --index <specs...>` | Index spec(s): `name`, `path:/path`, or `s3://bucket/key` | All indexes |
| `--search-only`          | Disable file operations                                   | `false`     |

When no `--index` is specified, all indexes in the default store are exposed.

#### Examples

```bash theme={null}
# Expose a specific index
npx ctxc mcp stdio -i my-project

# Multiple indexes
npx ctxc mcp stdio -i my-project -i other-project

# From S3
npx ctxc mcp stdio -i s3://my-bucket/indexes/my-project

# All indexes in default store
npx ctxc mcp stdio
```

***

### `mcp http` - Start MCP HTTP server

Start an MCP server accessible over HTTP for remote clients.

```bash theme={null}
npx ctxc mcp http [options]
```

#### Optional Options

| Option                   | Description                                               | Default     |
| ------------------------ | --------------------------------------------------------- | ----------- |
| `-i, --index <specs...>` | Index spec(s): `name`, `path:/path`, or `s3://bucket/key` | All indexes |
| `--port <number>`        | Port to listen on                                         | `3000`      |
| `--host <host>`          | Host to bind to                                           | `localhost` |
| `--cors <origins>`       | CORS origins (comma-separated, or `*`)                    | -           |
| `--base-path <path>`     | Base path for MCP endpoint                                | `/mcp`      |
| `--api-key <key>`        | API key for authentication                                | -           |
| `--search-only`          | Disable file operations                                   | `false`     |

**Environment:** Can use `MCP_API_KEY` instead of `--api-key` flag.

#### Examples

```bash theme={null}
# Basic HTTP server
npx ctxc mcp http -i my-project --port 8080

# With authentication and CORS
npx ctxc mcp http -i my-project --port 8080 \
  --api-key "secret" --cors "*"

# Accept external connections
npx ctxc mcp http -i my-project --host 0.0.0.0 --port 8080

# Search-only mode
npx ctxc mcp http -i my-project --search-only

# From S3
npx ctxc mcp http -i s3://my-bucket/indexes/my-project --port 8080
```

***

## Common Patterns

### Using S3 Storage

All commands support S3 storage for team sharing:

```bash theme={null}
# Set AWS credentials and S3 bucket
export AWS_ACCESS_KEY_ID='your-key'
export AWS_SECRET_ACCESS_KEY='your-secret'
export CC_S3_BUCKET='my-team-indexes'

# Index to S3
npx ctxc index github --owner myorg --repo myrepo -i my-project \
  --store s3

# Search from S3
npx ctxc search "query" -i s3://my-team-indexes/my-project
```

### Using S3-Compatible Services

For MinIO, DigitalOcean Spaces, Cloudflare R2, etc.:

```bash theme={null}
export CC_S3_BUCKET='my-bucket'
export CC_S3_ENDPOINT='http://localhost:9000'
export CC_S3_FORCE_PATH_STYLE='true'

npx ctxc index github --owner myorg --repo myrepo -i my-project \
  --store s3
```

### File Operations

The `--search-only` flag controls whether file operations are available:

* **Without `--search-only`**: Enables `search`, `listFiles`, and `readFile` tools
* **With `--search-only`**: Only `search` tool is available

***

## Troubleshooting

### "Index not found"

Make sure the index spec points to the correct location (name, path, or S3 URL).

### "AUGMENT\_API\_TOKEN is not set"

Set the required environment variables:

```bash theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
```

### S3 Access Denied

Verify your AWS credentials and bucket permissions:

```bash theme={null}
export AWS_ACCESS_KEY_ID='your-key'
export AWS_SECRET_ACCESS_KEY='your-secret'
```

### GitHub/GitLab/BitBucket Authentication

Make sure the appropriate token is set:

```bash theme={null}
export GITHUB_TOKEN='ghp_...'
export GITLAB_TOKEN='glpat-...'
export BITBUCKET_TOKEN='...'
```


# How It Works
Source: https://docs.augmentcode.com/context-services/context-connectors/how-it-works

Architecture and data flow of Context Connectors

Context Connectors is a pipeline that indexes your code and content for semantic search. Here's how the pieces fit together.

## Architecture

Content flows through five components:

<Steps>
  <Step title="Source" icon="folder">
    Connect to your content: GitHub, GitLab, BitBucket, or website
  </Step>

  <Step title="Indexer" icon="gear">
    Discover files, filter, chunk, and send to Context Engine for embedding
  </Step>

  <Step title="Store" icon="database">
    Persist index state (local filesystem or S3) for incremental updates
  </Step>

  <Step title="Context Engine" icon="magnifying-glass">
    Augment's semantic search backend stores embeddings and handles queries
  </Step>

  <Step title="Client" icon="terminal">
    Query via CLI, MCP server, or your own application
  </Step>
</Steps>

## Data Flow

### Indexing

When you run `ctxc index`, here's what happens:

1. **Discover** - Source connector lists all files (respects `.gitignore`)
2. **Filter** - Skip binary files, large files, excluded patterns
3. **Hash** - Compute file hashes to detect changes
4. **Diff** - Compare with stored state to find new/modified/deleted files
5. **Index** - Send changed files to Context Engine for embedding
6. **Save** - Store new state for next incremental run

### Searching

When you run `ctxc search` or query via MCP:

1. **Query** - User submits natural language query
2. **Embed** - Context Engine converts query to vector
3. **Match** - Find semantically similar code chunks
4. **Return** - Results with file paths, line numbers, and snippets

### File Reading (MCP/Agent)

When an agent needs full file content (not just search snippets):

1. **Request** - Agent requests file by path
2. **Fetch** - MCP server reads from original source (filesystem or Git API)
3. **Return** - Full file content returned to agent

This is why MCP servers need source credentials (e.g., `GITHUB_TOKEN`) - they read files on demand from the original source, not from the index.

## Incremental Updates

Context Connectors tracks file state to avoid re-indexing unchanged files:

| Scenario       | What Happens           |
| -------------- | ---------------------- |
| File unchanged | Skipped (hash matches) |
| File modified  | Re-indexed             |
| File deleted   | Removed from index     |
| New file       | Added to index         |

State is stored in your chosen store:

* **Local filesystem** - Platform-specific directory (e.g., `~/.local/share/context-connectors` on Linux)
* **S3** - `s3://bucket/index-name/` prefix

This makes subsequent runs fast - only changed files are processed.


# Overview
Source: https://docs.augmentcode.com/context-services/context-connectors/overview

An open-source library built on the Context Engine SDK that makes diverse sources searchable across agents and apps

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

**Build indexes** from Git repos (GitHub, GitLab, BitBucket) or documentation websites. Index code, documentation, runbooks, schemas, configs, and more. Use DirectContext in the Context Engine SDK for custom sources.

**Store indexes** on your local filesystem for fast & simple access, or in S3 for persistent storage in production apps.

**Search indexes** via interactive agent, MCP for AI integrations, CLI for quick searches, or DirectContext in the Context Engine SDK for custom implementations.

## Getting Started

**New to Context Connectors?** Here's a suggested path:

1. **Index and search** → [Index and Search Code](/context-services/context-connectors/quickstart/index-git-repos) (3 min)
2. **Connect an agent** → [Local MCP Server](/context-services/context-connectors/quickstart/claude-desktop-integration) (3 min)
3. **Build an app** → [Store Indexes in S3](/context-services/context-connectors/quickstart/share-with-s3) (5 min)
4. **Automate updates** → [GitHub Actions Auto-Indexing](/context-services/context-connectors/quickstart/github-actions-indexing) (5 min)

Or jump directly to any recipe below.

## Quickstart Recipes

<CardGroup>
  <Card title="Index and Search Code" icon="magnifying-glass" href="/context-services/context-connectors/quickstart/index-git-repos">
    Index a Git repository and search or chat with it (3 minutes)
  </Card>

  <Card title="Index Websites" icon="globe" href="/context-services/context-connectors/quickstart/index-website">
    Crawl and index documentation sites (3 minutes)
  </Card>

  <Card title="Local MCP Server" icon="desktop" href="/context-services/context-connectors/quickstart/claude-desktop-integration">
    Add codebase search to Claude Desktop, Claude Code, Cursor, or another agent (3 minutes)
  </Card>

  <Card title="Remote MCP Server" icon="server" href="/context-services/context-connectors/quickstart/remote-mcp-server">
    Expose indexes via MCP over HTTP for remote clients (3 minutes)
  </Card>

  <Card title="Store Indexes in S3" icon="cloud" href="/context-services/context-connectors/quickstart/share-with-s3">
    Store indexes in S3 for persistent storage in production apps (5 minutes)
  </Card>

  <Card title="GitHub Actions Auto-Indexing" icon="rotate" href="/context-services/context-connectors/quickstart/github-actions-indexing">
    Automatically re-index on every push using GitHub Actions (5 minutes)
  </Card>

  <Card title="Auto-Index with Webhooks" icon="webhook" href="/context-services/context-connectors/quickstart/auto-index-webhook">
    Custom webhook server for auto-indexing (advanced, 10 minutes)
  </Card>
</CardGroup>

## Advanced Recipes

<CardGroup>
  <Card title="Custom Indexer" icon="code" href="/context-services/context-connectors/advanced/custom-indexer">
    Build a custom indexer for any data source using DirectContext
  </Card>

  <Card title="Custom Store" icon="database" href="/context-services/context-connectors/advanced/custom-store">
    Create custom storage backends (local, S3, or any storage)
  </Card>

  <Card title="Custom Client" icon="plug" href="/context-services/context-connectors/advanced/custom-client">
    Build custom search clients for your applications
  </Card>
</CardGroup>

## Documentation

<CardGroup>
  <Card title="CLI Reference" icon="terminal" href="/context-services/context-connectors/cli-reference">
    Complete command-line reference
  </Card>
</CardGroup>


# Auto-Index with Webhooks
Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/auto-index-webhook

Set up a custom webhook server to re-index on push (advanced) in 10 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* A Vercel account (or Express server)
* Augment API credentials
* AWS credentials + S3 bucket
* A GitHub repo you control

## Steps

### 1. Create a Vercel project

```bash theme={null}
npx create-next-app@latest my-webhook --typescript --app
cd my-webhook
npm install @augmentcode/context-connectors @aws-sdk/client-s3
```

### 2. Create the webhook handler

Create `app/api/webhook/route.ts`:

```typescript theme={null}
import { createVercelHandler } from "@augmentcode/context-connectors/integrations/vercel";
import { S3Store } from "@augmentcode/context-connectors/stores";

const store = new S3Store({ bucket: process.env.INDEX_BUCKET! });

export const POST = createVercelHandler({
  store,
  secret: process.env.GITHUB_WEBHOOK_SECRET!,
  shouldIndex: (event) => event.ref === "refs/heads/main",
});
```

### 3. Set environment variables in Vercel

```
AUGMENT_API_TOKEN=your-token
AUGMENT_API_URL=https://your-tenant.api.augmentcode.com/
GITHUB_WEBHOOK_SECRET=your-secret
INDEX_BUCKET=my-indexes
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
```

### 4. Deploy

```bash theme={null}
npx vercel --prod
```

Note the URL (e.g., `https://my-webhook.vercel.app`).

### 5. Configure GitHub webhook

1. Go to your repo → Settings → Webhooks → Add webhook
2. Payload URL: `https://my-webhook.vercel.app/api/webhook`
3. Content type: `application/json`
4. Secret: same as `GITHUB_WEBHOOK_SECRET`
5. Events: Just the push event
6. Click "Add webhook"

### 6. Test it

Push a commit to main. Check Vercel logs for:

```
Indexed myorg/myrepo: 142 files indexed
```

## Done!

Your index updates automatically on every push to main.

## Also Works With

| Instead of...    | Try...                                                                     |
| ---------------- | -------------------------------------------------------------------------- |
| Vercel           | Express: `createExpressHandler()` from `integrations/express`              |
| Vercel           | Any framework: `createGitHubWebhookHandler()` + `verifyWebhookSignature()` |
| Main branch only | Customize `shouldIndex` to match any branch pattern                        |
| S3 storage       | `FilesystemStore` for local/self-hosted setups                             |


# Local MCP Server
Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/claude-desktop-integration

Add codebase search to Claude Desktop, Claude Code, Cursor, or another agent in 3 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* Claude Desktop installed
* An indexed project (see [Index and Search Code](/context-services/context-connectors/quickstart/index-git-repos))
* Augment API credentials

## Steps

### 1. Open Claude Desktop config

<Tabs>
  <Tab title="macOS">
    ```bash theme={null}
    open ~/Library/Application\ Support/Claude/claude_desktop_config.json
    ```
  </Tab>

  <Tab title="Windows">
    ```
    %APPDATA%\Claude\claude_desktop_config.json
    ```
  </Tab>
</Tabs>

### 2. Add MCP server config

<Tabs>
  <Tab title="Local Filesystem">
    ```json theme={null}
    {
      "mcpServers": {
        "my-project": {
          "command": "npx",
          "args": ["ctxc", "mcp", "stdio", "-i", "my-project"],
          "env": {
            "AUGMENT_API_TOKEN": "your-token",
            "AUGMENT_API_URL": "https://your-tenant.api.augmentcode.com/"
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="GitHub">
    ```json theme={null}
    {
      "mcpServers": {
        "my-project": {
          "command": "npx",
          "args": ["ctxc", "mcp", "stdio", "-i", "my-project"],
          "env": {
            "AUGMENT_API_TOKEN": "your-token",
            "AUGMENT_API_URL": "https://your-tenant.api.augmentcode.com/",
            "GITHUB_TOKEN": "ghp_..."
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="GitLab">
    ```json theme={null}
    {
      "mcpServers": {
        "my-project": {
          "command": "npx",
          "args": ["ctxc", "mcp", "stdio", "-i", "my-project"],
          "env": {
            "AUGMENT_API_TOKEN": "your-token",
            "AUGMENT_API_URL": "https://your-tenant.api.augmentcode.com/",
            "GITLAB_TOKEN": "glpat-..."
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="BitBucket">
    ```json theme={null}
    {
      "mcpServers": {
        "my-project": {
          "command": "npx",
          "args": ["ctxc", "mcp", "stdio", "-i", "my-project"],
          "env": {
            "AUGMENT_API_TOKEN": "your-token",
            "AUGMENT_API_URL": "https://your-tenant.api.augmentcode.com/",
            "BITBUCKET_TOKEN": "..."
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

### 3. Restart Claude Desktop

Quit and reopen Claude Desktop.

### 4. Test it

Ask Claude:

> Search for authentication logic in my-project

You should see Claude use the search tool and return code snippets.

## Done!

Your agent can now search your codebase via the local MCP server.

## Works With Other Agents

This same configuration works with any MCP-compatible agent:

* **Claude Desktop** - Follow the steps above
* **Claude Code** (VS Code extension) - Add to Claude Code's MCP settings
* **Cursor** - Configure in Cursor's MCP settings
* **GitHub Copilot** - Add to Copilot's MCP configuration
* **Custom agents** - Any tool that supports MCP stdio protocol

Each agent has its own config file location, but the MCP server configuration is the same.

## Also Works With

| Instead of... | Try...                                                         |
| ------------- | -------------------------------------------------------------- |
| One repo      | Add multiple entries to `mcpServers` for different projects    |
| Local index   | S3-stored indexes with `--store s3` and `CC_S3_BUCKET` env var |
| Search only   | Add `--search-only` to disable file reading                    |


# GitHub Actions Auto-Indexing
Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/github-actions-indexing

Automatically index your repository on every push using GitHub Actions in 5 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* A GitHub repository
* Augment API credentials

## Steps

### 1. Create the workflow file

Create `.github/workflows/augment-index.yml` in your repository:

```yaml theme={null}
name: Index Repository

on:
  push:
    branches:
      - main
  workflow_dispatch:  # Allow manual triggering

jobs:
  index:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Restore index state
        uses: actions/cache@v4
        with:
          path: .augment-index-state
          key: augment-index-${{ github.ref_name }}-${{ github.sha }}
          restore-keys: |
            augment-index-${{ github.ref_name }}-

      - name: Index repository
        run: |
          npx @augmentcode/context-connectors index github \
            --owner ${{ github.repository_owner }} \
            --repo ${{ github.event.repository.name }} \
            --ref ${{ github.sha }} \
            -i ${{ github.repository_owner }}/${{ github.event.repository.name }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          AUGMENT_API_TOKEN: ${{ secrets.AUGMENT_API_TOKEN }}
          AUGMENT_API_URL: ${{ secrets.AUGMENT_API_URL }}
```

### 2. Set up GitHub repository secrets

Go to your repository **Settings → Secrets and variables → Actions** and add:

| Secret Name         | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| `AUGMENT_API_TOKEN` | Your Augment API token                                             |
| `AUGMENT_API_URL`   | Your tenant URL (e.g., `https://your-tenant.api.augmentcode.com/`) |

**How to get your credentials:**

```bash theme={null}
# Login to Augment
auggie login

# Print your credentials
auggie token print
```

This outputs your `accessToken` (use for `AUGMENT_API_TOKEN`) and `tenantURL` (use for `AUGMENT_API_URL`).

### 3. Commit and push

```bash theme={null}
git add .github/workflows/augment-index.yml
git commit -m "Add Augment indexing workflow"
git push
```

### 4. Verify it's working

Go to your repository's **Actions** tab. You should see the "Index Repository" workflow running.

Once complete, you can search your index:

```bash theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
npx ctxc search "authentication logic" -i myorg/myrepo
```

## Done!

Your repository will now automatically re-index on every push to the main branch. The workflow uses GitHub Actions cache to store index state for efficient incremental updates.

## Also Works With

| Instead of...     | Try...                                                              |
| ----------------- | ------------------------------------------------------------------- |
| Main branch only  | Edit the workflow to add more branches: `branches: [main, develop]` |
| GitHub cache      | Use S3 storage: add `--store s3` and set `CC_S3_BUCKET` env var     |
| Custom index name | Change the `-i` value to your preferred name                        |

## How It Works

The workflow:

1. **Triggers** on every push to your main branch
2. **Restores** the previous index state from GitHub Actions cache
3. **Indexes** the repository using the GitHub API (no checkout needed for indexing)
4. **Caches** the new index state for the next run

This approach is much faster than full re-indexing on every push.

## Advanced: Using S3 Storage

For production use or team sharing, you can store indexes in S3 instead of GitHub cache:

1. Edit `.github/workflows/augment-index.yml`
2. Add S3 configuration to the command:

```yaml theme={null}
- name: Index repository
  run: |
    npx @augmentcode/context-connectors index github \
      --owner ${{ github.repository_owner }} \
      --repo ${{ github.event.repository.name }} \
      --ref ${{ github.sha }} \
      -i ${{ github.repository_owner }}/${{ github.event.repository.name }} \
      --store s3
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    AUGMENT_API_TOKEN: ${{ secrets.AUGMENT_API_TOKEN }}
    AUGMENT_API_URL: ${{ secrets.AUGMENT_API_URL }}
    AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    CC_S3_BUCKET: my-team-indexes
```

3. Add AWS credentials to repository secrets

This allows multiple repositories or team members to share the same index.


# Index and Search Code
Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/index-git-repos

Index a Git repository and search or chat with it in 3 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* Node.js 18+
* Augment API credentials (`AUGMENT_API_TOKEN`, `AUGMENT_API_URL`)
* Git provider token with repo read access:
  * GitHub: `GITHUB_TOKEN`
  * GitLab: `GITLAB_TOKEN`
  * BitBucket: `BITBUCKET_TOKEN`
* For chat: An LLM API key (OpenAI, Anthropic, or Google)

## Steps

### 1. Install

```bash theme={null}
npm install @augmentcode/context-connectors
```

### 2. Set credentials

<Tabs>
  <Tab title="GitHub">
    ```bash theme={null}
    export AUGMENT_API_TOKEN='your-token'
    export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
    export GITHUB_TOKEN='your-github-token'
    ```
  </Tab>

  <Tab title="GitLab">
    ```bash theme={null}
    export AUGMENT_API_TOKEN='your-token'
    export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
    export GITLAB_TOKEN='your-gitlab-token'
    ```
  </Tab>

  <Tab title="BitBucket">
    ```bash theme={null}
    export AUGMENT_API_TOKEN='your-token'
    export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
    export BITBUCKET_TOKEN='your-bitbucket-token'
    ```
  </Tab>
</Tabs>

### 3. Index the repository

<Tabs>
  <Tab title="GitHub">
    ```bash theme={null}
    npx ctxc index github --owner facebook --repo react -i react
    ```
  </Tab>

  <Tab title="GitLab">
    ```bash theme={null}
    npx ctxc index gitlab --project mygroup/myrepo -i myrepo
    ```
  </Tab>

  <Tab title="Bitbucket">
    ```bash theme={null}
    npx ctxc index bitbucket --workspace myws --repo myrepo -i myrepo
    ```
  </Tab>
</Tabs>

You should see:

```
Fetching file tree from facebook/react...
Indexing complete: 2847 files indexed, 156 skipped
```

### 4. Search

```bash theme={null}
npx ctxc search "How does the reconciliation algorithm work?" -i react
```

You should see an LLM-generated answer based on the codebase:

```
Answer:

Based on the code in packages/react-reconciler/src/ReactFiberReconciler.js...
```

For raw search results without LLM processing, add `--raw`:

```bash theme={null}
npx ctxc search "reconciliation" -i react --raw
```

### 5. Chat (Optional)

For an interactive AI agent that can search and read the codebase:

```bash theme={null}
export OPENAI_API_KEY='your-openai-key'
npx ctxc agent -i react --provider openai
```

You should see:

```
Agent ready. Type your question or 'exit' to quit.

>
```

Ask questions interactively:

```
> How does React handle component updates?

Searching: "component updates"...
Reading: packages/react-reconciler/src/ReactFiberWorkLoop.js...

Based on the code, React handles component updates by...
```

Type `exit` to quit.

## Done!

You can now:

* **Search** your codebase semantically with the `search` command
* **Chat** with an AI agent that understands your code using the `agent` command

No need to clone the repository locally - Context Connectors fetches files directly from the Git provider API.

## Also Works With

| Instead of...    | Try...                                                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Default branch   | `--ref main`, `--ref v1.0.0`, or `--ref abc123` for specific branch/tag/commit                                             |
| Local storage    | `--store s3` with `CC_S3_BUCKET` for team sharing                                                                          |
| Manual updates   | Set up [GitHub Actions](/context-services/context-connectors/quickstart/github-actions-indexing) to re-index on every push |
| Interactive chat | `npx ctxc agent -i react --provider openai "your question" --print` for single-question mode                               |
| OpenAI           | `--provider anthropic` or `--provider google` for other LLM providers                                                      |
| Code repos       | [Index websites](/context-services/context-connectors/quickstart/index-website) to chat with documentation sites           |


# Index Website
Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/index-website

Crawl and index a static website for semantic search in 3 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* Node.js 18+
* Augment API credentials
* For chat: An LLM API key (OpenAI, Anthropic, or Google)

## Steps

### 1. Install

```bash theme={null}
npm install @augmentcode/context-connectors
```

### 2. Set credentials

```bash theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
```

### 3. Index the site

```bash theme={null}
npx ctxc index website --url https://docs.example.com -i example-docs
```

You should see:

```
Crawling https://docs.example.com...
Indexing complete: 87 pages indexed, 12 skipped
```

### 4. Search

```bash theme={null}
npx ctxc search "how to configure SSO" -i example-docs
```

You should see an LLM-generated answer based on the documentation:

```
Answer:

Based on the documentation at https://docs.example.com/auth/sso, SSO can be configured by...
```

For raw search results without LLM processing, add `--raw`:

```bash theme={null}
npx ctxc search "SSO" -i example-docs --raw
```

### 5. Chat (Optional)

For an interactive AI agent that can search and read the documentation:

```bash theme={null}
export OPENAI_API_KEY='your-openai-key'
npx ctxc agent -i example-docs --provider openai
```

You should see:

```
Agent ready. Type your question or 'exit' to quit.

>
```

Ask questions interactively:

```
> How do I set up SSO with Okta?

Searching: "SSO Okta setup"...
Reading: https://docs.example.com/auth/sso-okta...

Based on the documentation, to set up SSO with Okta you need to...
```

Type `exit` to quit.

## Done!

You can now:

* **Search** the documentation semantically with the `search` command
* **Chat** with an AI agent that understands the docs using the `agent` command

## Limitations

* Only static HTML is indexed. JavaScript-rendered content (SPAs) won't work.
* Only pages linked from the starting URL are discovered.

## Also Works With

| Instead of...    | Try...                                                                                              |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| Single site      | Index multiple sites with different `-i` names                                                      |
| Local storage    | `--store s3` with `CC_S3_BUCKET` for team sharing                                                   |
| Interactive chat | `npx ctxc agent -i example-docs --provider openai "your question" --print` for single-question mode |
| OpenAI           | `--provider anthropic` or `--provider google` for other LLM providers                               |


# Remote MCP Server
Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/remote-mcp-server

Expose your index via MCP over HTTP for remote clients in 3 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

<Note>
  **For local MCP integration** with Claude Desktop, Claude Code, Cursor, or other agents, see [Local MCP Server](/context-services/context-connectors/quickstart/claude-desktop-integration).
</Note>

## Prerequisites

* Node.js 18+
* Augment API credentials
* An indexed project (see [Index and Search Code](/context-services/context-connectors/quickstart/index-git-repos))

## Steps

### 1. Install

```bash theme={null}
npm install @augmentcode/context-connectors @modelcontextprotocol/sdk
```

### 2. Set credentials

```bash theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
```

### 3. Start the server

```bash theme={null}
npx ctxc mcp http -i my-project --port 8080 --api-key "secret"
```

You should see:

```
MCP HTTP server running at http://localhost:8080/mcp
```

### 4. Test with curl

First, initialize a session:

```bash theme={null}
curl -X POST http://localhost:8080/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer secret" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2024-11-05",
      "capabilities": {},
      "clientInfo": { "name": "curl-test", "version": "1.0.0" }
    }
  }' -i
```

Note the `mcp-session-id` header in the response. Use it for subsequent requests:

```bash theme={null}
curl -X POST http://localhost:8080/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer secret" \
  -H "mcp-session-id: <session-id-from-initialize>" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
      "name": "search",
      "arguments": { "query": "authentication" }
    }
  }'
```

You should see JSON search results.

## Done!

Your index is accessible via MCP over HTTP at `http://localhost:8080/mcp`. Remote clients can now search your codebase using the Model Context Protocol over HTTP.

## Also Works With

| Instead of...  | Try...                                                           |
| -------------- | ---------------------------------------------------------------- |
| localhost only | `--host 0.0.0.0` to accept external connections                  |
| No CORS        | `--cors "*"` or `--cors "https://myapp.com"` for browser clients |
| Full access    | `--search-only` to disable file operations                       |
| Local storage  | `--store s3` with `CC_S3_BUCKET` for shared indexes              |


# Store Indexes in S3
Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/share-with-s3

Store indexes in S3 for team sharing or application data management in 5 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

S3 storage enables two key use cases:

* **Team Sharing**: Multiple team members can search the same index
* **Application Data**: Build apps that manage per-user indexes in S3

## Prerequisites

* Node.js 18+
* Augment API credentials
* AWS credentials with S3 read/write access
* An S3 bucket

## Steps

### 1. Install

```bash theme={null}
npm install @augmentcode/context-connectors @aws-sdk/client-s3
```

### 2. Set credentials

```bash theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
export AWS_ACCESS_KEY_ID='your-key'
export AWS_SECRET_ACCESS_KEY='your-secret'
```

### 3. Index to S3

```bash theme={null}
export CC_S3_BUCKET='my-team-bucket'
npx ctxc index github --owner myorg --repo myrepo -i my-project \
  --store s3
```

You should see:

```
Fetching file tree from myorg/myrepo...
Indexing complete: 142 files indexed, 0 skipped
Stored to s3://my-team-bucket/context-connectors/my-project/
```

### 4. Search from S3

Anyone with AWS credentials can now search:

```bash theme={null}
npx ctxc search "How does authentication work?" \
  -i s3://my-team-bucket/context-connectors/my-project
```

<Note>
  Indexes are stored under a `context-connectors/` prefix in your bucket. Include this prefix when searching.
</Note>

## Done!

Your index is stored in S3 at `s3://my-team-bucket/context-connectors/my-project/`. Share the S3 URL with your team.

## Also Works With

| Instead of...   | Try...                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| AWS S3          | MinIO: set `CC_S3_ENDPOINT` and `CC_S3_FORCE_PATH_STYLE=true`                                                 |
| AWS S3          | DigitalOcean Spaces, Backblaze B2, Cloudflare R2 (use `CC_S3_ENDPOINT`)                                       |
| Manual indexing | [Auto-index on push](/context-services/context-connectors/quickstart/auto-index-webhook) with GitHub webhooks |


# Context Engine MCP
Source: https://docs.augmentcode.com/context-services/mcp/overview

Plug Context Engine into any agent via the Model Context Protocol

## Quickstart Guides

Get started with Context Engine MCP in your favorite AI tool:

<CardGroup>
  <Card title="Claude Code" icon="terminal" href="/context-services/mcp/quickstart-claude-code">
    Set up Context Engine MCP with Claude Code
  </Card>

  <Card title="Codex" icon="terminal" href="/context-services/mcp/quickstart-codex">
    Set up Context Engine MCP with OpenAI Codex CLI
  </Card>

  <Card title="Cursor" icon="code" href="/context-services/mcp/quickstart-cursor">
    Set up Context Engine MCP with Cursor
  </Card>

  <Card title="Zed" icon="code" href="/context-services/mcp/quickstart-zed">
    Set up Context Engine MCP with Zed
  </Card>

  <Card title="GitHub Copilot" icon="github" href="/context-services/mcp/quickstart-github-copilot">
    Set up Context Engine MCP with GitHub Copilot
  </Card>

  <Card title="OpenCode" icon="code" href="/context-services/mcp/quickstart-open-code">
    Set up Context Engine MCP with OpenCode
  </Card>

  <Card title="Kilo Code" icon="code" href="/context-services/mcp/quickstart-kilo">
    Set up Context Engine MCP with Kilo Code
  </Card>

  <Card title="Kiro" icon="code" href="/context-services/mcp/quickstart-kiro">
    Set up Context Engine MCP with Kiro
  </Card>

  <Card title="AntiGravity" icon="rocket" href="/context-services/mcp/quickstart-anti-gravity">
    Set up Context Engine MCP with AntiGravity
  </Card>

  <Card title="Gemini CLI" icon="terminal" href="/context-services/mcp/quickstart-gemini-cli">
    Set up Context Engine MCP with Gemini CLI
  </Card>

  <Card title="Droid (Factory.AI)" icon="robot" href="/context-services/mcp/quickstart-droid">
    Set up Context Engine MCP with Droid
  </Card>
</CardGroup>


# Quickstart (AntiGravity)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-anti-gravity

Get started with Augment Context Engine MCP in AntiGravity in minutes

## Quick Start with AntiGravity

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in AntiGravity

* Click the MCP server icon
  <img alt="MCP server icon" />
* Click manage MCP server
  <img alt="Manage MCP server" />
* Click View raw config
  <img alt="View raw config" />

Paste this configuration:

```json theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "args": ["--mcp", "--mcp-auto-workspace"]
    }
  }
}
```

### 4. Test the integration

```
Prompt: "What is this project? Please use codebase retrieval tool to get the answer."
```

AntiGravity should confirm it has access to the `codebase-retrieval` tool.

<img alt="AntiGravity test" />


# Quickstart (Claude Code)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-claude-code

Get started with Augment Context Engine MCP in Claude Code in minutes

## Quick Start with Claude Code

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Claude Code

Add the MCP server to user scope (available in all projects):

```bash theme={null}
claude mcp add-json auggie-mcp --scope user '{"type":"stdio","command":"auggie","args":["--mcp","--mcp-auto-workspace"]}'
```

Or add to project scope (only available in the current project):

```bash theme={null}
claude mcp add-json auggie-mcp --scope project '{"type":"stdio","command":"auggie","args":["--mcp","--mcp-auto-workspace"]}'
```

### 4. Test the integration

```bash theme={null}
claude --print "Do you have access to the Augment codebase retrieval tool? Answer in one sentence."
```

Claude should confirm it has access to the `codebase-retrieval` tool.

## Advanced: Non-Interactive Setup

For non-interactive environments like CI/CD pipelines, GitHub Actions, or automated scripts where you cannot run `auggie login` interactively, you can configure authentication using environment variables.

### 1. Get your authentication token

```bash theme={null}
auggie token print
```

This will output something like:

```
TOKEN={"accessToken":"your-access-token","tenantURL":"your-tenant-url","scopes":["read","write"]}
```

Copy the `accessToken` value (the long string after `"accessToken":"`) and the `tenantURL` value.

### 2. Configure with environment variables

```bash theme={null}
claude mcp add-json auggie-mcp --scope user '{"type":"stdio","command":"auggie","args":["--mcp","--mcp-auto-workspace"],"env":{"AUGMENT_API_TOKEN":"your-access-token","AUGMENT_API_URL":"your-tenant-url"}}'
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.


# Quickstart (Codex)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-codex

Get started with Augment Context Engine MCP in OpenAI Codex CLI in minutes

## Quick Start with Codex

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Codex

Add the MCP server using the Codex CLI:

```bash theme={null}
codex mcp add codebase-retrieval -- auggie --mcp --mcp-auto-workspace
```

The `--mcp-auto-workspace` flag automatically detects your workspace when using Codex.

### 4. Test the integration

Run Codex and prompt it with:

```
"What is this project? Please use the codebase-retrieval tool to get the answer."
```

Codex should confirm it has access to the `codebase-retrieval` tool.

## Advanced: Non-Interactive Setup

For non-interactive environments like CI/CD pipelines, GitHub Actions, or automated scripts where you cannot run `auggie login` interactively, you can configure authentication using environment variables.

### 1. Get your authentication token

```bash theme={null}
auggie token print
```

This will output something like:

```
TOKEN={"accessToken":"your-access-token","tenantURL":"your-tenant-url","scopes":["read","write"]}
```

Copy the `accessToken` value (the long string after `"accessToken":"`) and the `tenantURL` value.

### 2. Configure with environment variables

```bash theme={null}
codex mcp add codebase-retrieval --env AUGMENT_API_TOKEN=your-access-token --env AUGMENT_API_URL=your-tenant-url -- auggie --mcp --mcp-auto-workspace
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.


# Quickstart (Cursor)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-cursor

Get started with Augment Context Engine MCP in Cursor in minutes

## Quick Start with Cursor

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Cursor

* Go in settings (top right)
  <img alt="Cursor settings" />
* Click on Tools & MCP on the left menu then **New MCP Server**
  <img alt="Cursor MCP" />

Paste this configuration:

```json theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "type": "local",
      "command": "auggie",
      "args": ["--mcp", "--mcp-auto-workspace"],
      "enabled": true
    }
  }
}
```

### 4. Test the integration

```
Prompt: "What is this project? Please use codebase retrieval tool to get the answer."
```

Cursor should confirm it has access to the `codebase-retrieval` tool.

<img alt="Cursor test" />

See [MCP Server Mode](/cli/reference#mcp-server-mode) for more options.


# Quickstart (Droid)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-droid

Get started with Augment Context Engine MCP in Droid in minutes

## Quick Start with Droid

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Droid

Add the Augment Context Engine MCP server:

```bash theme={null}
droid mcp add augment-code "auggie" --mcp --mcp-auto-workspace
```

### 4. Test the integration

```
Prompt: "Do you have access to the Augment codebase retrieval tool?"
```

Droid should confirm it has access to the `codebase-retrieval` tool.

## Advanced: Non-Interactive Setup

For non-interactive environments like CI/CD pipelines, GitHub Actions, or automated scripts where you cannot run `auggie login` interactively, you can configure authentication using environment variables.

### 1. Get your authentication token

```bash theme={null}
auggie token print
```

This will output something like:

```
TOKEN={"accessToken":"your-access-token","tenantURL":"your-tenant-url","scopes":["read","write"]}
```

Copy the `accessToken` value (the long string after `"accessToken":"`) and the `tenantURL` value.

### 2. Configure with environment variables

```bash theme={null}
droid mcp add augment-code "auggie" --mcp --mcp-auto-workspace --env AUGMENT_API_TOKEN=your-access-token --env AUGMENT_API_URL=your-tenant-url
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.


# Quickstart (Gemini CLI)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-gemini-cli

Get started with Augment Context Engine MCP in Gemini CLI in minutes

## Quick Start with Gemini CLI

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Gemini CLI

Gemini CLI reads the MCP server configuration from a settings file. You can configure MCP servers at either the user level (applies to all projects) or project level (applies only to that specific project):

**Configuration file locations:**

* **User settings** (global):
  * macOS/Linux: `~/.gemini/settings.json`
  * Windows: `%USERPROFILE%\.gemini\settings.json`
* **Project settings** (optional): `.gemini/settings.json` in your project's root directory

Add the following configuration to your Gemini CLI settings file:

```json theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "args": ["--mcp", "--mcp-auto-workspace"]
    }
  }
}
```

### 4. Test the integration

Prompt the Gemini CLI with:

```
Prompt: "What is this project? Please use codebase retrieval tool to get the answer."
```

Gemini CLI should confirm it has access to the `codebase-retrieval` tool.

## Advanced: Non-Interactive Setup

For non-interactive environments like CI/CD pipelines, GitHub Actions, or automated scripts where you cannot run `auggie login` interactively, you can configure authentication using environment variables.

### 1. Get your authentication token

```bash theme={null}
auggie token print
```

This will output something like:

```
TOKEN={"accessToken":"your-access-token","tenantURL":"your-tenant-url","scopes":["read","write"]}
```

Copy the `accessToken` value (the long string after `"accessToken":"`) and the `tenantURL` value.

### 2. Configure with environment variables

Add the `env` section to your configuration:

```json theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "args": ["--mcp", "--mcp-auto-workspace"],
      "env": {
        "AUGMENT_API_TOKEN": "your-access-token",
        "AUGMENT_API_URL": "your-tenant-url"
      }
    }
  }
}
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.


# Quickstart (GitHub Copilot)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-github-copilot

Get started with Augment Context Engine MCP in GitHub Copilot in minutes

## Quick Start with GitHub Copilot

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in GitHub Copilot

* Please create the following file **at the root** of your project: **.vscode/mcp.json**
* Paste this content inside and **Save**

```json theme={null}
{
  "servers": {
    "augmentcode": {
      "type": "stdio",
      "command": "auggie",
      "args": ["--mcp", "--mcp-auto-workspace"]
    }
  },
  "inputs": []
}
```

### 4. Test the integration

Prompt this in **AGENT MODE**: "What is this project? Please use codebase retrieval tool to get the answer."

Copilot should confirm it has access to the `codebase-retrieval` tool.

<img alt="Copilot test" />


# Quickstart (Kilo)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-kilo

Get started with Augment Context Engine MCP in Kilo in minutes

## Quick Start with Kilo

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Kilo

* Click the MCP server icon
  <img alt="Click the MCP server icon" />

* Click Edit Global MCP
  <img alt="Click Edit Global MCP" />

Paste this configuration:

```json theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "type": "stdio",
      "args": ["--mcp", "--mcp-auto-workspace"],
      "disabled": false,
      "alwaysAllow": ["codebase-retrieval"]
    }
  }
}
```

### 4. Test the integration

Prompt: "What is this project? Please use codebase retrieval tool to get the answer."

Kilo should confirm it has access to the `codebase-retrieval` tool.

<img alt="Kilo test" />


# Quickstart (Kiro)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-kiro

Get started with Augment Context Engine MCP in Kiro in minutes

## Quick Start with Kiro

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Kiro

Open the command palette (`Cmd + Shift + P` on Mac, `Ctrl + Shift + P` on Windows/Linux) and select:

* **Kiro: Open workspace MCP config (JSON)** - For workspace-level configuration
* **Kiro: Open user MCP config (JSON)** - For user-level configuration

Paste this configuration:

```json theme={null}
{
  "mcpServers": {
    "Augment-Context-Engine": {
      "command": "auggie",
      "args": ["--mcp", "--mcp-auto-workspace"],
      "disabled": false,
      "autoApprove": ["codebase-retrieval"]
    }
  }
}
```

### 4. Test the integration

```
Prompt: "Do you have access to the Augment codebase retrieval tool?"
```

Kiro should confirm it has access to the `codebase-retrieval` tool.


# Quickstart (OpenCode)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-open-code

Get started with Augment Context Engine MCP in OpenCode in minutes

## Quick Start with OpenCode

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in OpenCode

* Go to Folder: \~/.config/opencode/
* Create a file named: opencode.json

Paste this configuration:

```json theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "augment-context-engine": {
      "type": "local",
      "command": ["auggie", "--mcp", "--mcp-auto-workspace"],
      "enabled": true
    }
  }
}
```

### 4. Test the integration

```
Prompt: "What is this project? Please use codebase retrieval tool to get the answer."
```

OpenCode should confirm it has access to the `codebase-retrieval` tool.

<img alt="OpenCode test" />

## Advanced: Non-Interactive Setup

For non-interactive environments like CI/CD pipelines, GitHub Actions, or automated scripts where you cannot run `auggie login` interactively, you can configure authentication using environment variables.

### 1. Get your authentication token

```bash theme={null}
auggie token print
```

This will output something like:

```
TOKEN={"accessToken":"your-access-token","tenantURL":"your-tenant-url","scopes":["read","write"]}
```

Copy the `accessToken` value (the long string after `"accessToken":"`) and the `tenantURL` value.

### 2. Configure with environment variables

Add the `env` section to your configuration:

```json theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "augment-context-engine": {
      "type": "local",
      "command": ["auggie", "--mcp", "--mcp-auto-workspace"],
      "enabled": true,
      "env": {
        "AUGMENT_API_TOKEN": "your-access-token",
        "AUGMENT_API_URL": "your-tenant-url"
      }
    }
  }
}
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.


# Quickstart (Zed)
Source: https://docs.augmentcode.com/context-services/mcp/quickstart-zed

Get started with Augment Context Engine MCP in Zed in minutes

## Quick Start with Zed

### 1. Install Auggie CLI

```bash theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Get your authentication token (Only if you set it up remotely, this is not mandatory locally.)

```bash theme={null}
auggie token print
```

This will output something like:

```
TOKEN={"accessToken":"your-access-token","tenantURL":"your-tenant-url","scopes":["read","write"]}
```

Copy the `accessToken` value (the long string after `"accessToken":"`) and the `tenantURL` value for the next step.

### 4. Configure the MCP server in Zed

* Click the ... then **Add Custom Server**
  <img alt="Zed custom server" />
* Paste the config below
  <img alt="Zed MCP" />

```json theme={null}
{
  "Augment-Context-Engine": {
    "enabled": true,
    "command": "auggie",
    "args": ["--mcp", "--mcp-auto-workspace"],
    "env": {}
  }
}
```

### 5. Test the integration

Prompt: "What is this project? Please use codebase retrieval tool to get the answer."

Zed should confirm it has access to the `codebase-retrieval` tool.

<img alt="Zed test" />


# Overview
Source: https://docs.augmentcode.com/context-services/overview

Context Services provide context for agents and apps

## What Are Context Services?

Context Services provide high-quality semantic search to AI agents and applications. Whether you're building custom agents or integrating with existing AI tools, Context Services give you access to Augment's world-class context engine.

<CardGroup>
  <Card title="Context Engine MCP" icon="plug" href="/context-services/mcp/overview">
    Plug Context Engine into any agent via the Model Context Protocol
  </Card>

  <Card title="Context Engine SDK" icon="code" href="/context-services/sdk/overview">
    Build context-aware custom agents or apps using our TypeScript or Python SDK
  </Card>

  <Card title="Context Connectors" icon="database" href="/context-services/context-connectors/overview">
    Index any source and make it searchable via CLI, MCP, or HTTP
  </Card>
</CardGroup>

### Context Engine MCP

Plug Context Engine into any agent, such as Claude Code, Codex, Gemini CLI, and more via the Model Context Protocol (MCP).

**Perfect for:**

* Using Augment's context in your favorite AI tools
* Enriching any coding agent or AI with state-of-the-art codebase semantic search

[Get started with MCP →](/context-services/mcp/overview)

### Context Engine SDK

Build context-aware custom agents or apps using our TypeScript or Python SDK.

The SDK provides **FileSystem Context** to index local directories or **Direct Context** to index files from any source.

**Perfect for:**

* Building custom AI agents with codebase understanding
* Creating applications that need to understand codebase, documentation, specifications, runbooks, and other text sources
* Achieving state-of-the-art context quality in AI-powered code review, security scanning, failure analysis, migrations, and more ...

[Get started with the SDK →](/context-services/sdk/overview)

### Context Connectors

An open-source library built on the Context Engine SDK that makes diverse sources searchable across agents and apps. Index code, documentation, runbooks, schemas, and configs from GitHub, GitLab, BitBucket, websites, or local filesystem. Store indexes locally or in S3. Search via CLI, interactive agent, or MCP server.

**Perfect for:**

* Indexing repositories without cloning them locally
* Building applications with persistent indexes stored in S3
* Auto-indexing on every push via webhooks
* Indexing documentation websites

[Get started with Context Connectors →](/context-services/context-connectors/overview)


# API Reference
Source: https://docs.augmentcode.com/context-services/sdk/api-reference

Complete API documentation for the Context Engine SDK

<Warning>
  **Experimental API** - Context Engine SDK is experimental and subject to breaking changes.
</Warning>

## DirectContext

This class provides explicit file indexing via API calls with the ability to import and export state to avoid re-indexing between sessions.

***

## Examples

### Example 1: Simple Usage

Upload files and ask questions immediately:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';

  async function simpleExample() {
    // Create context (authentication is automatic)
    const context = await DirectContext.create();

    // Add files and wait for indexing (default behavior)
    const result = await context.addToIndex([
      { path: 'src/auth.ts', contents: 'export function login(user, pass) { ... }' },
      { path: 'src/user.ts', contents: 'export class User { constructor(id) { ... } }' },
      { path: 'README.md', contents: '# My Project\nAuthentication system' }
    ]);

    console.log(`Newly uploaded: ${result.newlyUploaded.length}`);

    // Ask questions about the code - files are already indexed
    const answer = await context.searchAndAsk(
      'How does the login system work?'
    );
    console.log('Answer:', answer);
  }

  simpleExample().catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File

  def simple_example():
      # Create context (authentication is automatic)
      context = DirectContext.create()

      # Add files and wait for indexing (default behavior)
      result = context.add_to_index([
          File(path='src/auth.py', contents='def login(user, password): ...'),
          File(path='src/user.py', contents='class User:\n    def __init__(self, id): ...'),
          File(path='README.md', contents='# My Project\nAuthentication system')
      ])

      print(f"Newly uploaded: {len(result.newly_uploaded)}")

      # Ask questions about the code - files are already indexed
      answer = context.search_and_ask(
          'How does the login system work?'
      )
      print('Answer:', answer)

  if __name__ == '__main__':
      simple_example()
  ```
</CodeGroup>

### Example 2: Persistent Index

Persist state between sessions to avoid re-indexing. This is useful when you want to save the index state to disk and reload it later without having to re-upload and re-index all files. The saved state file contains metadata about which files are indexed, allowing you to resume from where you left off:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';

  // First session: Upload and save
  async function uploadAndSave() {
    const context = await DirectContext.create();

    // Upload files
    await context.addToIndex([
      { path: 'src/auth.ts', contents: 'export function login() { ... }' },
      { path: 'src/user.ts', contents: 'export class User { ... }' },
      { path: 'src/database.ts', contents: 'export function connect() { ... }' }
    ]);

    // Save state for later use - this creates a JSON file containing the index metadata
    // so you can reload it later without re-indexing all files
    await context.exportToFile('./my-project-context.json');
    console.log('Context saved!');
    console.log('You can now reload this state in a future session using importFromFile()');
  }

  // Second session: Load, update incrementally, and save again
  async function updateAndSave() {
    // Load previous state - this restores the index without re-uploading files
    const context = await DirectContext.importFromFile('./my-project-context.json');
    console.log('Context loaded from previous session - no re-indexing needed!');

    // Make incremental changes - remove old file and add new one
    await context.removeFromIndex(['src/user.ts']);
    await context.addToIndex([
      { path: 'src/profile.ts', contents: 'export class Profile { /* profile logic */ }' },
      { path: 'src/settings.ts', contents: 'export function updateSettings() { /* settings */ }' }
    ]);
    console.log('Index updated incrementally');

    // Save updated state
    await context.exportToFile('./my-project-context.json');
    console.log('Updated context saved!');
  }

  // Third session: Load and search
  async function loadAndSearch() {
    // Load the updated state
    const context = await DirectContext.importFromFile('./my-project-context.json');
    console.log('Updated context loaded');

    // Search immediately - files are already indexed
    const answer = await context.searchAndAsk(
      'What user management features are implemented?'
    );
    console.log('Answer:', answer);
  }

  // Run the complete workflow: upload → update → search
  uploadAndSave()
    .then(() => updateAndSave())
    .then(() => loadAndSearch())
    .catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File

  # First session: Upload and save
  def upload_and_save():
      context = DirectContext.create()

      # Upload files
      context.add_to_index([
          File(path='src/auth.py', contents='def login(): ...'),
          File(path='src/user.py', contents='class User: ...'),
          File(path='src/database.py', contents='def connect(): ...')
      ])

      # Save state for later use - this creates a JSON file containing the index metadata
      # so you can reload it later without re-indexing all files
      context.export_to_file('./my-project-context.json')
      print('Context saved!')
      print('You can now reload this state in a future session using import_from_file()')

  # Second session: Load, update incrementally, and save again
  def update_and_save():
      # Load previous state - this restores the index without re-uploading files
      context = DirectContext.import_from_file('./my-project-context.json')
      print('Context loaded from previous session - no re-indexing needed!')

      # Make incremental changes - remove old file and add new one
      context.remove_from_index(['src/user.py'])
      context.add_to_index([
          File(path='src/profile.py', contents='class Profile: # profile logic'),
          File(path='src/settings.py', contents='def update_settings(): # settings')
      ])
      print('Index updated incrementally')

      # Save updated state
      context.export_to_file('./my-project-context.json')
      print('Updated context saved!')

  # Third session: Load and search
  def load_and_search():
      # Load the updated state
      context = DirectContext.import_from_file('./my-project-context.json')
      print('Updated context loaded')

      # Search immediately - files are already indexed
      answer = context.search_and_ask(
          'What user management features are implemented?'
      )
      print('Answer:', answer)

  # Run the complete workflow: upload → update → search
  if __name__ == '__main__':
      upload_and_save()
      update_and_save()
      load_and_search()
  ```
</CodeGroup>

### Example 3: Batch Upload Then Wait

When you need to upload many files in multiple batches, you can optimize performance by uploading all files first without waiting for indexing, then waiting once at the end. This approach is faster than waiting for indexing after each batch:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';

  async function batchExample() {
    const context = await DirectContext.create();

    // Upload multiple batches without waiting for indexing
    await context.addToIndex([
      { path: 'src/auth.ts', contents: 'export function login() { ... }' },
      { path: 'src/user.ts', contents: 'export class User { ... }' }
    ], { waitForIndexing: false });

    await context.addToIndex([
      { path: 'src/database.ts', contents: 'export function connect() { ... }' },
      { path: 'src/api.ts', contents: 'export function createServer() { ... }' }
    ], { waitForIndexing: false });

    // Wait for all files to be indexed
    console.log('Waiting for indexing to complete...');
    await context.waitForIndexing();
    console.log('All files indexed!');

    // Now search - all files are guaranteed to be indexed
    const answer = await context.searchAndAsk(
      'How do the database and auth systems work together?'
    );
    console.log('Answer:', answer);
  }

  batchExample().catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File

  def batch_example():
      context = DirectContext.create()

      # Upload multiple batches without waiting for indexing
      context.add_to_index([
          File(path='src/auth.py', contents='def login(): ...'),
          File(path='src/user.py', contents='class User: ...')
      ], wait_for_indexing=False)

      context.add_to_index([
          File(path='src/database.py', contents='def connect(): ...'),
          File(path='src/api.py', contents='def create_server(): ...')
      ], wait_for_indexing=False)

      # Wait for all files to be indexed
      print('Waiting for indexing to complete...')
      context.wait_for_indexing()
      print('All files indexed!')

      # Now search - all files are guaranteed to be indexed
      answer = context.search_and_ask(
          'How do the database and auth systems work together?'
      )
      print('Answer:', answer)

  if __name__ == '__main__':
      batch_example()
  ```
</CodeGroup>

### Example 4: Custom Prompts

Use searchAndAsk with custom prompts for diverse tasks:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';

  async function creativeExample() {
    const context = await DirectContext.create();

    // Upload some code
    await context.addToIndex([
      { path: 'src/auth.ts', contents: 'export function login(user, pass) { /* auth logic */ }' },
      { path: 'src/database.ts', contents: 'export function connect() { /* db connection */ }' },
      { path: 'README.md', contents: '# My App\nA secure authentication system' }
    ]);

    // Creative prompts with searchAndAsk
    const poem = await context.searchAndAsk(
      'authentication system',
      'Write a haiku about this authentication code'
    );
    console.log('Haiku:', poem);

    // Generate documentation
    const docs = await context.searchAndAsk(
      'database authentication flow',
      'Write a brief user guide explaining how to use the database authentication flow'
    );
    console.log('Documentation:', docs);

    // Code review style analysis
    const review = await context.searchAndAsk(
      'authentication logic',
      'Provide a code review focusing on security best practices'
    );
    console.log('Code Review:', review);
  }

  creativeExample().catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File

  def creative_example():
      context = DirectContext.create()

      # Upload some code
      context.add_to_index([
          File(path='src/auth.py', contents='def login(user, password): # auth logic'),
          File(path='src/database.py', contents='def connect(): # db connection'),
          File(path='README.md', contents='# My App\nA secure authentication system')
      ])

      # Creative prompts with search_and_ask
      poem = context.search_and_ask(
          'authentication system',
          'Write a haiku about this authentication code'
      )
      print('Haiku:', poem)

      # Generate documentation
      docs = context.search_and_ask(
          'database authentication flow',
          'Write a brief user guide explaining how to use the database authentication flow'
      )
      print('Documentation:', docs)

      # Code review style analysis
      review = context.search_and_ask(
          'authentication logic',
          'Provide a code review focusing on security best practices'
      )
      print('Code Review:', review)

  if __name__ == '__main__':
      creative_example()
  ```
</CodeGroup>

### Example 5: External LLM Integration

Use search() results with external LLM APIs:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';
  // import { Anthropic } from '@anthropic-ai/sdk';
  // import OpenAI from 'openai';

  async function externalLLMExample() {
    const context = await DirectContext.create();

    // Upload code
    await context.addToIndex([
      { path: 'src/api.ts', contents: 'export function handleRequest() { /* API logic */ }' },
      { path: 'src/auth.ts', contents: 'export function authenticate() { /* auth */ }' },
      { path: 'src/database.ts', contents: 'export function query() { /* db query */ }' }
    ]);

    // Get formatted search results for external LLMs
    const codeContext = await context.search('API request handling');

    // codeContext is a formatted string ready to embed in prompts for
    // Anthropic, OpenAI, or other LLM APIs
    console.log('Code context for LLM:', codeContext);

    // Example: Use with Anthropic Claude (uncomment to use)
    // const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
    // const response = await anthropic.messages.create({
    //   model: 'claude-sonnet-4-5-20250929',
    //   max_tokens: 1000,
    //   messages: [{
    //     role: 'user',
    //     content: `Based on this code:\n\n${codeContext}\n\nHow can I improve the error handling in the API?`
    //   }]
    // });
    // console.log('Claude response:', response.content[0].text);

    // Example: Use with OpenAI GPT-5.1 (uncomment to use)
    // const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
    // const completion = await openai.chat.completions.create({
    //   model: 'gpt-5.1',
    //   messages: [{
    //     role: 'user',
    //     content: `Based on this code:\n\n${codeContext}\n\nSuggest performance optimizations for this API.`
    //   }]
    // });
    // console.log('GPT-5.1 response:', completion.choices[0].message.content);


  }

  externalLLMExample().catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File
  # import anthropic
  # import openai

  def external_llm_example():
      context = DirectContext.create()

      # Upload code
      context.add_to_index([
          File(path='src/api.py', contents='def handle_request(): # API logic'),
          File(path='src/auth.py', contents='def authenticate(): # auth'),
          File(path='src/database.py', contents='def query(): # db query')
      ])

      # Get formatted search results for external LLMs
      code_context = context.search('API request handling')

      # code_context is a formatted string ready to embed in prompts for
      # Anthropic, OpenAI, or other LLM APIs
      print('Code context for LLM:', code_context)

      # Example: Use with Anthropic Claude (uncomment to use)
      # client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
      # response = client.messages.create(
      #     model='claude-sonnet-4-5-20250929',
      #     max_tokens=1000,
      #     messages=[{
      #         'role': 'user',
      #         'content': f'Based on this code:\n\n{code_context}\n\nHow can I improve the error handling?'
      #     }]
      # )
      # print('Claude response:', response.content[0].text)

      # Example: Use with OpenAI GPT-5.1 (uncomment to use)
      # client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])
      # completion = client.chat.completions.create(
      #     model='gpt-5.1',
      #     messages=[{
      #         'role': 'user',
      #         'content': f'Based on this code:\n\n{code_context}\n\nSuggest performance optimizations.'
      #     }]
      # )
      # print('GPT-5.1 response:', completion.choices[0].message.content)

  if __name__ == '__main__':
      external_llm_example()
  ```
</CodeGroup>

***

## API Reference

### DirectContext.create()

Create and initialize a new DirectContext instance.

<CodeGroup>
  ```typescript TypeScript theme={null}
  static async create(options?: DirectContextOptions): Promise<DirectContext>

  interface DirectContextOptions {
    apiKey?: string;      // Optional - falls back to env vars or session.json
    apiUrl?: string;      // Optional - falls back to env vars or session.json
    debug?: boolean;      // Enable debug logging (default: false)
  }
  ```

  ```python Python theme={null}
  @classmethod
  def create(
      cls,
      *,
      api_key: Optional[str] = None,
      api_url: Optional[str] = None,
      debug: bool = False,
  ) -> DirectContext
  ```
</CodeGroup>

**Parameters:**

* `options` - Optional configuration object
  * `apiKey` - API key for authentication (optional)
  * `apiUrl` - API URL for your tenant (optional)
  * `debug` - Enable debug logging (optional, default: false)

**Authentication Priority:**

1. `options.apiKey` / `options.apiUrl` (passed to create())
2. `AUGMENT_API_TOKEN` / `AUGMENT_API_URL` environment variables
3. `~/.augment/session.json` (created by `auggie login`)

**Usage:** See complete examples above for full implementation details.

**Notes:**

* The SDK is **source-agnostic** - you provide files as `{path, contents}` objects
* Files larger than 1MB are rejected during indexing
* All indexing operations are serialized to ensure consistency
* State can be saved and loaded to avoid re-indexing

***

### DirectContext.importFromFile() / import\_from\_file()

Create a DirectContext instance from a saved state file.

<CodeGroup>
  ```typescript TypeScript theme={null}
  static async importFromFile(
    filePath: string,
    options?: DirectContextOptions
  ): Promise<DirectContext>
  ```

  ```python Python theme={null}
  @classmethod
  def import_from_file(
      cls,
      file_path: str,
      *,
      api_key: Optional[str] = None,
      api_url: Optional[str] = None,
      debug: bool = False,
  ) -> DirectContext
  ```
</CodeGroup>

**Parameters:**

* `filePath` / `file_path` - Path to the saved state file
* `options` - Optional configuration object (same as `create()`)

**Returns:** A DirectContext instance with restored state

**Usage:**

<CodeGroup>
  ```typescript TypeScript theme={null}
  // Load context from saved state
  const context = await DirectContext.importFromFile('./my-context.json');
  // Files are already indexed, ready to search
  ```

  ```python Python theme={null}
  # Load context from saved state
  context = DirectContext.import_from_file('./my-context.json')
  # Files are already indexed, ready to search
  ```
</CodeGroup>

***

### DirectContext.import() / import\_state()

Create a DirectContext instance from a saved state object.

<CodeGroup>
  ```typescript TypeScript theme={null}
  static async import(
    state: DirectContextState,
    options?: DirectContextOptions
  ): Promise<DirectContext>
  ```

  ```python Python theme={null}
  @classmethod
  def import_state(
      cls,
      state: DirectContextState,
      *,
      api_key: Optional[str] = None,
      api_url: Optional[str] = None,
      debug: bool = False,
  ) -> DirectContext
  ```
</CodeGroup>

**Parameters:**

* `state` - The state object to restore from
* `options` - Optional configuration object (same as `create()`)

**Returns:** A DirectContext instance with restored state

**Usage:**

<CodeGroup>
  ```typescript TypeScript theme={null}
  // Load context from state object
  const savedState = JSON.parse(stateJson);
  const context = await DirectContext.import(savedState);
  ```

  ```python Python theme={null}
  import json
  # Load context from state object
  with open('state.json') as f:
      saved_state = DirectContextState.from_dict(json.load(f))
  context = DirectContext.import_state(saved_state)
  ```
</CodeGroup>

***

## DirectContext Methods

### addToIndex() / add\_to\_index()

Add files to the index. Files can come from any source - memory, disk, API, database, etc.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async addToIndex(
    files: File[],
    options?: { waitForIndexing?: boolean }
  ): Promise<IndexingResult>

  interface File {
    path: string;      // Relative path (e.g., "src/main.ts")
    contents: string;  // File contents as string
  }

  interface IndexingResult {
    newlyUploaded: string[];     // Paths that were uploaded and indexed
    alreadyUploaded: string[];   // Paths that were skipped (already on server)
  }
  ```

  ```python Python theme={null}
  def add_to_index(
      self,
      files: List[File],
      wait_for_indexing: bool = True
  ) -> IndexingResult

  @dataclass
  class File:
      path: str       # Relative path (e.g., "src/main.py")
      contents: str   # File contents as string

  @dataclass
  class IndexingResult:
      newly_uploaded: List[str]     # Paths that were uploaded and indexed
      already_uploaded: List[str]   # Paths that were skipped (already on server)
  ```
</CodeGroup>

**Parameters:**

* `files` - Array/list of file objects with `path` and `contents`
* `options` / `wait_for_indexing` - Optional configuration
  * `waitForIndexing` / `wait_for_indexing` - If true (default), waits for the newly added files to be indexed before returning

**Returns:** `IndexingResult` object with details about what was indexed

**Notes:**

* Files larger than 1MB will throw an error
* By default, waits for backend indexing to complete before returning (set `waitForIndexing: false` / `wait_for_indexing=False` to return immediately after upload)
* If a file with the same path already exists, it will be updated
* All operations are serialized to ensure consistency
* The SDK optimizes uploads by checking which blobs the server already has and only uploading missing ones

***

### removeFromIndex() / remove\_from\_index()

Remove files from the index by path.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async removeFromIndex(paths: string[]): Promise<void>
  ```

  ```python Python theme={null}
  def remove_from_index(self, paths: List[str]) -> None
  ```
</CodeGroup>

**Parameters:**

* `paths` - Array/list of file paths to remove

***

### clearIndex() / clear\_index()

Clear the entire index, removing all files.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async clearIndex(): Promise<void>
  ```

  ```python Python theme={null}
  def clear_index(self) -> None
  ```
</CodeGroup>

***

### getIndexedPaths() / get\_indexed\_paths()

Get the list of currently indexed file paths.

<CodeGroup>
  ```typescript TypeScript theme={null}
  getIndexedPaths(): string[]
  ```

  ```python Python theme={null}
  def get_indexed_paths(self) -> List[str]
  ```
</CodeGroup>

**Returns:** Array/list of relative file paths that are currently indexed

**Use Cases:**

* Display indexed files to users
* Verify which files are included in the index
* Filter files for targeted searches

***

### search()

Search the codebase and return formatted results as a string.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async search(
    query: string,
    options?: { maxOutputLength?: number }
  ): Promise<string>
  ```

  ```python Python theme={null}
  def search(
      self,
      query: str,
      max_output_length: Optional[int] = None
  ) -> str
  ```
</CodeGroup>

**Parameters:**

* `query` - Natural language search query
* `options` / `max_output_length` - Optional search options
  * `maxOutputLength` / `max_output_length` - Maximum character length of the formatted output (default: 20000, max: 80000)

**Returns:** Formatted string containing the search results, ready for LLM consumption

**Notes:**

* Returns a formatted string designed for use in LLM prompts
* The format includes file paths, line numbers, and code content
* Does NOT wait for indexing - ensure files are indexed before searching by either:
  * Using `addToIndex()` / `add_to_index()` with `waitForIndexing: true` / `wait_for_indexing=True` (default)
  * Calling `waitForIndexing()` / `wait_for_indexing()` explicitly before searching
* Throws an error if the index is empty

***

### searchAndAsk() / search\_and\_ask()

Search the indexed codebase and ask an LLM a question about the results.

This is a convenience method that combines `search()` with an LLM call to answer questions about your codebase.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async searchAndAsk(
    searchQuery: string,
    prompt?: string
  ): Promise<string>
  ```

  ```python Python theme={null}
  def search_and_ask(
      self,
      search_query: str,
      prompt: Optional[str] = None
  ) -> str
  ```
</CodeGroup>

**Parameters:**

* `searchQuery` / `search_query` - The semantic search query to find relevant code (also used as the prompt if no separate prompt is provided)
* `prompt` - Optional prompt to ask the LLM about the search results. If not provided, searchQuery is used as the prompt.

**Returns:** The LLM's answer to your question

**Notes:**

* Does NOT wait for indexing - ensure files are indexed before searching by either:
  * Using `addToIndex()` / `add_to_index()` with `waitForIndexing: true` / `wait_for_indexing=True` (default)
  * Calling `waitForIndexing()` / `wait_for_indexing()` explicitly before searching
* Requires `AUGMENT_API_TOKEN` and `AUGMENT_API_URL` environment variables for LLM access

**Use Cases:**

* Quick Q\&A about your codebase
* Building conversational interfaces
* Automated code analysis and documentation

***

### waitForIndexing() / wait\_for\_indexing()

Wait for all indexed files to be fully indexed on the backend.

This method polls the backend until all files that have been added to the index are confirmed to be indexed and searchable.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async waitForIndexing(): Promise<void>
  ```

  ```python Python theme={null}
  def wait_for_indexing(self) -> None
  ```
</CodeGroup>

**Returns:** Promise that resolves when all files are indexed

**Notes:**

* Throws an error if indexing times out (default: 10 minutes)
* Only waits for files that have been added to the index
* Useful when you want to control when to wait for indexing completion

**Use Cases:**

* Batch upload multiple files quickly, then wait for all to be indexed
* Ensure search results include all recently added files
* Control timing of indexing waits in complex workflows

***

### exportToFile() / export\_to\_file()

Export the current state to a file.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async exportToFile(filePath: string): Promise<void>
  ```

  ```python Python theme={null}
  def export_to_file(self, file_path: str) -> None
  ```
</CodeGroup>

**Parameters:**

* `filePath` / `file_path` - Path to save the state file

**Use Cases:**

* Persist indexing state between sessions
* Avoid re-indexing large codebases
* Share indexing state across different processes

***

### export()

Export the current state as an object (in-memory).

<CodeGroup>
  ```typescript TypeScript theme={null}
  export(): DirectContextState

  interface DirectContextState {
    checkpointId?: string;
    addedBlobs: string[];
    deletedBlobs: string[];
    blobs: BlobEntry[];  // Array of [blobName, path] tuples
  }
  ```

  ```python Python theme={null}
  def export(self) -> DirectContextState

  @dataclass
  class DirectContextState:
      checkpoint_id: Optional[str]
      added_blobs: List[str]
      deleted_blobs: List[str]
      blobs: List[Tuple[str, str]]  # List of (blob_name, path) tuples
  ```
</CodeGroup>

**Returns:** State object that can be serialized and stored

***

## FileSystemContext

This class provides automatic indexing and search capabilities for a local directory.

### FileSystemContext.create()

Create and initialize a new FileSystemContext instance.

<CodeGroup>
  ```typescript TypeScript theme={null}
  static async create(options: FileSystemContextOptions): Promise<FileSystemContext>

  interface FileSystemContextOptions {
    directory: string;      // Path to the workspace directory to index
    auggiePath?: string;    // Path to auggie executable (default: "auggie")
    debug?: boolean;        // Enable debug logging (default: false)
  }
  ```

  ```python Python theme={null}
  @classmethod
  def create(
      cls,
      directory: str,
      *,
      auggie_path: str = "auggie",
      debug: bool = False,
  ) -> FileSystemContext
  ```
</CodeGroup>

**Parameters:**

* `options` / positional args - Configuration
  * `directory` - Path to the workspace directory to index (required)
  * `auggiePath` / `auggie_path` - Path to auggie executable (optional, default: "auggie")
  * `debug` - Enable debug logging (optional, default: false)

**Usage:** See DirectContext examples above for similar patterns.

**Notes:**

* Automatically indexes the directory on startup
* Requires `auggie` CLI to be installed and accessible
* Python supports context manager (`with` statement) for automatic cleanup

***

## FileSystemContext Methods

### search()

Search the codebase and return formatted results as a string.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async search(query: string): Promise<string>
  ```

  ```python Python theme={null}
  def search(self, query: str) -> str
  ```
</CodeGroup>

**Parameters:**

* `query` - Natural language search query

**Returns:** Formatted string containing the search results, ready for LLM consumption

***

### searchAndAsk() / search\_and\_ask()

Search the indexed codebase and ask an LLM a question about the results.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async searchAndAsk(
    searchQuery: string,
    prompt?: string
  ): Promise<string>
  ```

  ```python Python theme={null}
  def search_and_ask(
      self,
      search_query: str,
      prompt: Optional[str] = None
  ) -> str
  ```
</CodeGroup>

**Parameters:**

* `searchQuery` / `search_query` - The semantic search query to find relevant code (also used as the prompt if no separate prompt is provided)
* `prompt` - Optional prompt to ask the LLM about the search results. If not provided, searchQuery is used as the prompt.

**Returns:** The LLM's answer to your question

**Notes:**

* Requires `AUGMENT_API_TOKEN` and `AUGMENT_API_URL` environment variables for LLM access

***

### close()

Close the connection and cleanup resources.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async close(): Promise<void>
  ```

  ```python Python theme={null}
  def close(self) -> None
  ```
</CodeGroup>

**Notes:**

* Always call `close()` when done to cleanup resources
* Python: Use context manager (`with` statement) for automatic cleanup

***

## Types

### File

Represents a file to be indexed (input type for `addToIndex()` / `add_to_index()`).

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface File {
    path: string;      // Relative path (e.g., "src/main.ts")
    contents: string;  // File contents as string
  }
  ```

  ```python Python theme={null}
  @dataclass
  class File:
      path: str       # Relative path (e.g., "src/main.py")
      contents: str   # File contents as string
  ```
</CodeGroup>

### IndexingResult

Result from `addToIndex()` / `add_to_index()` operation showing what was indexed.

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface IndexingResult {
    newlyUploaded: string[];     // Paths that were uploaded and indexed
    alreadyUploaded: string[];   // Paths that were skipped (already on server)
  }
  ```

  ```python Python theme={null}
  @dataclass
  class IndexingResult:
      newly_uploaded: List[str]     # Paths that were uploaded and indexed
      already_uploaded: List[str]   # Paths that were skipped (already on server)
  ```
</CodeGroup>

**Notes:**

* `newlyUploaded` / `newly_uploaded`: Files that were uploaded to the server and indexed
* `alreadyUploaded` / `already_uploaded`: Files that were skipped because:
  * They were already in the local cache with the same content, OR
  * The server already had the blob (detected via `find-missing` API)

### DirectContextOptions (TypeScript) / Keyword Arguments (Python)

Options for configuring DirectContext.

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface DirectContextOptions {
    apiKey?: string;      // API key for authentication
    apiUrl?: string;      // API URL for your Augment tenant
    debug?: boolean;      // Enable debug logging (default: false)
  }
  ```

  ```python Python theme={null}
  # In Python, these are passed as keyword arguments to create():
  DirectContext.create(
      api_key: Optional[str] = None,  # API key for authentication
      api_url: Optional[str] = None,  # API URL for your Augment tenant
      debug: bool = False,            # Enable debug logging (default: False)
  )
  ```
</CodeGroup>

### DirectContextState

State for DirectContext that can be saved/loaded.

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface DirectContextState {
    checkpointId?: string;      // Current checkpoint ID
    addedBlobs: string[];       // Blob names added (pending checkpoint)
    deletedBlobs: string[];     // Blob names deleted (pending checkpoint)
    blobs: BlobEntry[];         // List of blobs as [blobName, path] tuples
  }

  type BlobEntry = [blobName: string, path: string];
  ```

  ```python Python theme={null}
  @dataclass
  class DirectContextState:
      checkpoint_id: Optional[str]       # Current checkpoint ID
      added_blobs: List[str]             # Blob names added (pending checkpoint)
      deleted_blobs: List[str]           # Blob names deleted (pending checkpoint)
      blobs: List[Tuple[str, str]]       # List of (blob_name, path) tuples

      def to_dict(self) -> Dict[str, Any]:
          """Convert to JSON-serializable dict."""
          ...

      @classmethod
      def from_dict(cls, data: Dict[str, Any]) -> DirectContextState:
          """Create from JSON dict (e.g., from imported state file)."""
          ...
  ```
</CodeGroup>

**Serialization Example:**

<CodeGroup>
  ```typescript TypeScript theme={null}
  // DirectContextState is a plain object, use JSON.parse/stringify
  const stateJson = JSON.stringify(context.export());
  const restoredState = JSON.parse(stateJson);
  const newContext = await DirectContext.import(restoredState);
  ```

  ```python Python theme={null}
  import json

  # Export state and serialize to JSON
  state = context.export()
  state_json = json.dumps(state.to_dict())

  # Later: deserialize and import
  data = json.loads(state_json)
  restored_state = DirectContextState.from_dict(data)
  new_context = DirectContext.import_state(restored_state)
  ```
</CodeGroup>

### FileSystemContextOptions (TypeScript) / Keyword Arguments (Python)

Options for FileSystem Context.

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface FileSystemContextOptions {
    directory: string;      // Path to the workspace directory to index
    auggiePath?: string;    // Path to auggie executable (default: "auggie")
    debug?: boolean;        // Enable debug logging (default: false)
  }
  ```

  ```python Python theme={null}
  # In Python, these are passed as arguments to create():
  FileSystemContext.create(
      directory: str,                    # Path to the workspace directory to index
      auggie_path: str = "auggie",       # Path to auggie executable (default: "auggie")
      debug: bool = False,               # Enable debug logging (default: False)
  )
  ```
</CodeGroup>

***

## Authentication

The SDK automatically loads credentials from multiple sources in this priority order:

1. **Options/keyword arguments**: `apiKey`/`api_key` and `apiUrl`/`api_url` passed to `DirectContext.create()`
2. **Environment variables**: `AUGMENT_API_TOKEN` and `AUGMENT_API_URL`
3. **Session file**: `~/.augment/session.json` (created by `auggie login`)

**To get credentials:**

1. Sign in to Augment using the CLI: `auggie login`
2. Your credentials will be stored in `~/.augment/session.json`
3. The SDK will automatically use them

***

## Error Handling

The SDK exports specific error classes for better error handling:

| Error Class         | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| `BlobTooLargeError` | File exceeds 1MB limit. Includes `path` and `size` properties. |
| `APIError`          | Network or API request failures. Includes `status` property.   |

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext, APIError, BlobTooLargeError } from '@augmentcode/auggie-sdk';

  try {
    const context = await DirectContext.create();
    await context.addToIndex([
      { path: 'test.ts', contents: '...' }
    ]);
    const results = await context.search('query');
  } catch (error) {
    if (error instanceof BlobTooLargeError) {
      console.error('File too large (max 1MB):', error.path);
    } else if (error instanceof APIError) {
      console.error('API request failed:', error.message);
      console.error('Status code:', error.status);
    } else if (error.message.includes('API key is required')) {
      console.error('Missing credentials');
    } else if (error.message.includes('Index not initialized')) {
      console.error('No files indexed yet');
    } else {
      console.error('Operation failed:', error);
    }
  }
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File, APIError, BlobTooLargeError

  try:
      context = DirectContext.create()
      context.add_to_index([
          File(path='test.py', contents='...')
      ])
      results = context.search('query')
  except BlobTooLargeError as error:
      print('File too large (max 1MB):', error)
  except APIError as error:
      print('API request failed:', error)
  except ValueError as error:
      if 'API key is required' in str(error):
          print('Missing credentials')
      elif 'Index not initialized' in str(error):
          print('No files indexed yet')
      else:
          print('Operation failed:', error)
  except Exception as error:
      print('Operation failed:', error)
  ```
</CodeGroup>


# Examples
Source: https://docs.augmentcode.com/context-services/sdk/examples

Example applications using the Auggie SDK

<Warning>
  **Experimental API** - Context Engine SDK is experimental and subject to breaking changes.
</Warning>

## Available Examples

<CardGroup>
  <Card title="Direct Context" icon="code" href="#direct-context">
    API-based indexing and search
  </Card>

  <Card title="FileSystem Context" icon="folder" href="#filesystem-context">
    Local directory search
  </Card>

  <Card title="File Search Server" icon="server" href="#file-search-server">
    REST API for code search
  </Card>

  <Card title="Prompt Enhancer Server" icon="wand-magic-sparkles" href="#prompt-enhancer-server">
    Context-aware prompt enhancement
  </Card>

  <Card title="GitHub Action Indexer" icon="github" href="#github-action-indexer">
    CI/CD repository indexing
  </Card>
</CardGroup>

***

## Getting the Examples

All example code is available in the Auggie repository. To access the examples:

<CodeGroup>
  ```bash TypeScript theme={null}
  git clone https://github.com/augmentcode/auggie.git
  cd auggie/examples/typescript-sdk/context
  ```

  ```bash Python theme={null}
  git clone https://github.com/augmentcode/auggie.git
  cd auggie/examples/python-sdk/context
  ```
</CodeGroup>

Each example is a complete, runnable application demonstrating different use cases of the Auggie SDK.

## Prerequisites

Before running the examples:

1. **Runtime** - One of the following:
   * **TypeScript:** Node.js 18+
   * **Python:** Python 3.10+

2. **Auggie CLI** - Required for FileSystem Context examples
   ```bash theme={null}
   npm install -g @augmentcode/auggie@latest
   ```

3. **Authentication** - Required for all examples

   ```bash theme={null}
   auggie login
   ```

   This creates a session file at `~/.augment/session.json` with your API token.

   Alternatively, set environment variables:

   ```bash theme={null}
   export AUGMENT_API_TOKEN="your-api-token"
   export AUGMENT_API_URL="https://your-tenant.api.augmentcode.com"
   ```

## Setup

Install dependencies:

<CodeGroup>
  ```bash TypeScript theme={null}
  cd examples/typescript-sdk/context
  npm install
  ```

  ```bash Python theme={null}
  cd examples/python-sdk/context
  pip install auggie-sdk
  ```
</CodeGroup>

***

## Simple Examples

Get started quickly with these basic examples that demonstrate core SDK functionality.

### Direct Context

Demonstrates indexing files from any source and performing semantic searches with AI-powered question answering.

**Quick Start:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npm run direct-context
  ```

  ```bash Python theme={null}
  python -m direct_context
  ```
</CodeGroup>

**Or run directly:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npx tsx direct-context/index.ts
  ```

  ```bash Python theme={null}
  python direct_context/main.py
  ```
</CodeGroup>

***

### FileSystem Context

Shows how to search a local directory using automatic file discovery via the MCP protocol.

**Prerequisites:**

* Auggie CLI must be installed and in your PATH
* Authentication via `auggie login` or `AUGMENT_API_TOKEN` environment variable
* A `.gitignore` or `.augmentignore` file in the workspace directory to exclude `node_modules/` and other large directories

**Important:** The FileSystem Context indexes all files in the workspace directory. To avoid timeouts when indexing large directories (like `node_modules/`), make sure you have a `.gitignore` or `.augmentignore` file that excludes them.

**Quick Start:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npm run filesystem-context
  ```

  ```bash Python theme={null}
  python -m filesystem_context
  ```
</CodeGroup>

**Or run directly:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npx tsx filesystem-context/index.ts
  ```

  ```bash Python theme={null}
  python filesystem_context/main.py
  ```
</CodeGroup>

***

## Developer Tools

Build production-ready applications with these server examples.

### File Search Server

A REST API server that provides semantic file search with AI-powered summarization.

**Prerequisites:** Auggie CLI must be installed and in your PATH.

**Quick Start:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npm run file-search-server [workspace-directory]
  ```

  ```bash Python theme={null}
  python -m file_search_server [workspace-directory]
  ```
</CodeGroup>

Then query the API:

```bash theme={null}
curl "http://localhost:3000/search?q=typescript"
```

**Or run directly:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npx tsx file-search-server/index.ts .
  ```

  ```bash Python theme={null}
  python file_search_server/main.py .
  ```
</CodeGroup>

***

### Prompt Enhancer Server

An HTTP server that automatically enriches user prompts with relevant codebase context.

**Prerequisites:** Auggie CLI must be installed and in your PATH.

**Quick Start:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npm run prompt-enhancer-server [workspace-directory]
  ```

  ```bash Python theme={null}
  python -m prompt_enhancer_server [workspace-directory]
  ```
</CodeGroup>

Then enhance prompts:

```bash theme={null}
curl -X POST http://localhost:3001/enhance \
  -H "Content-Type: application/json" \
  -d '{"prompt": "fix the login bug"}'
```

**Or run directly:**

<CodeGroup>
  ```bash TypeScript theme={null}
  npx tsx prompt-enhancer-server/index.ts .
  ```

  ```bash Python theme={null}
  python prompt_enhancer_server/main.py .
  ```
</CodeGroup>

***

## CI/CD Integration

Integrate the SDK into your continuous integration workflows.

### GitHub Action Indexer

Automatically index your GitHub repositories with **zero-question setup** and incremental updates. Perfect for CI/CD workflows and keeping your codebase searchable.

**Key Features:**

* 🔄 **Incremental indexing** - Only processes changed files for efficiency
* 💾 **Smart caching** - Persists index state between runs
* 🚀 **30-second setup** - From zero to running GitHub Action

**Installation:**

<CodeGroup>
  ```bash TypeScript theme={null}
  # Install directly into your repository
  cd /path/to/your/repository
  npx @augment-samples/github-action-indexer install

  # Add your API secrets to GitHub repository settings
  # Push to trigger automatic indexing on every commit
  ```

  ```bash Python theme={null}
  # From the auggie repo, install into your target repository
  cd examples/python-sdk/context
  python -m github_action_indexer install /path/to/your/repository

  # Add your API secrets to GitHub repository settings
  # Push to trigger automatic indexing on every commit
  ```
</CodeGroup>

**What It Does:**

1. **Indexes** your codebase automatically on every push
2. **Updates** incrementally using GitHub's Compare API
3. **Caches** index state for fast subsequent runs
4. **Handles** large repositories with optimized performance settings

**Perfect For:**

* Keeping your codebase searchable and up-to-date
* CI/CD workflows that need codebase understanding
* Teams wanting automatic repository indexing
* Projects with frequent commits (incremental updates are fast)

**Try It Locally First:**

<CodeGroup>
  ```bash TypeScript theme={null}
  cd github-action-indexer
  npm install
  export AUGMENT_API_TOKEN="your-token"
  export AUGMENT_API_URL="https://your-tenant.api.augmentcode.com/"
  export GITHUB_TOKEN="your-github-token"
  export GITHUB_REPOSITORY="owner/repo"
  export GITHUB_SHA="$(git rev-parse HEAD)"
  npm run index
  npm run search "authentication functions"
  ```

  ```bash Python theme={null}
  cd examples/python-sdk/context
  pip install -r github_action_indexer/augment_indexer/requirements.txt
  export AUGMENT_API_TOKEN="your-token"
  export AUGMENT_API_URL="https://your-tenant.api.augmentcode.com/"
  export GITHUB_TOKEN="your-github-token"
  export GITHUB_REPOSITORY="owner/repo"
  export GITHUB_SHA="$(git rev-parse HEAD)"
  python -m github_action_indexer index
  python -m github_action_indexer search "authentication functions"
  ```
</CodeGroup>

📖 **Complete Setup Guides:**

* [TypeScript GitHub Action Indexer →](https://github.com/augmentcode/auggie/tree/main/examples/typescript-sdk/context/github-action-indexer)
* [Python GitHub Action Indexer →](https://github.com/augmentcode/auggie/tree/main/examples/python-sdk/context/github_action_indexer)

***

## Troubleshooting

### MCP Timeout in FileSystem Context

**Problem:** The FileSystem Context example times out during indexing.

**Cause:** The workspace directory contains too many files (e.g., `node_modules/` with 45,000+ files).

**Solution:** Create a `.gitignore` or `.augmentignore` file in the workspace directory to exclude large directories:

```bash theme={null}
# .gitignore or .augmentignore
node_modules/
dist/
__pycache__/
.venv/
*.log
.DS_Store
```

The auggie CLI respects both `.gitignore` and `.augmentignore` patterns and will skip excluded files during indexing.

### Authentication Errors

**Problem:** `Error: API key is required for searchAndAsk()` or `ValueError: API credentials are required`

**Cause:** The SDK cannot find your authentication credentials.

**Solution:** Run `auggie login` to authenticate, or set the `AUGMENT_API_TOKEN` and `AUGMENT_API_URL` environment variables.

***

## Next Steps

<CardGroup>
  <Card title="API Reference" icon="code" href="/context-services/sdk/api-reference">
    Complete API documentation
  </Card>

  <Card title="Quick Start" icon="rocket" href="/context-services/sdk/overview">
    Back to quick start guide
  </Card>
</CardGroup>


# Quickstart
Source: https://docs.augmentcode.com/context-services/sdk/overview

Get started with the Augment Context Engine SDK in minutes

<Warning>
  **Experimental API** - Context Engine SDK is experimental and subject to breaking changes.
</Warning>

## Installation

<CodeGroup>
  ```bash TypeScript theme={null}
  npm install -g @augmentcode/auggie@latest && npm install @augmentcode/auggie-sdk
  ```

  ```bash Python theme={null}
  npm install -g @augmentcode/auggie@latest
  pip install auggie-sdk
  ```
</CodeGroup>

## Getting Credentials

Sign in to Augment using the CLI:

```bash theme={null}
auggie login
```

Your credentials will be stored in `~/.augment/session.json` and the SDK will automatically use them.

Alternatively, you can use environment variables:

```bash theme={null}
export AUGMENT_API_TOKEN="your-api-token"
export AUGMENT_API_URL="https://your-tenant.api.augmentcode.com"
```

<Note>
  **Finding your tenant URL:** After signing in with `auggie login`, run `auggie token print` to see your API token and tenant URL. The URL format is `https://[your-organization-name].api.augmentcode.com`.
</Note>

## Direct Context

Explicitly index files from any source (APIs, databases, memory, disk) with full control over what gets indexed and the ability to save/load state:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';

  async function main() {
    // Authentication is automatic via:
    // 1. Options parameters (apiKey, apiUrl passed to create())
    // 2. Environment variables (AUGMENT_API_TOKEN, AUGMENT_API_URL)
    // 3. ~/.augment/session.json (created by `auggie login`)
    const context = await DirectContext.create();

    // Add files to index
    const result = await context.addToIndex([
      { path: 'src/main.ts', contents: 'export function main() { ... }' },
      { path: 'src/auth.ts', contents: 'export function authenticate() { ... }' }
    ]);

    console.log(`Newly uploaded: ${result.newlyUploaded.length}`);
    console.log(`Already uploaded: ${result.alreadyUploaded.length}`);

    // Search - returns formatted string ready for LLM use or display
    const results = await context.search('authentication logic');
    console.log(results);

    // Or use searchAndAsk for one-step Q&A
    const answer = await context.searchAndAsk(
      'How does authentication work?'
    );
    console.log(answer);

    // Save state to avoid re-indexing
    await context.exportToFile('/tmp/state.json');
  }

  main();
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File

  def main():
      # Authentication is automatic via:
      # 1. Options parameters (api_key, api_url passed to create())
      # 2. Environment variables (AUGMENT_API_TOKEN, AUGMENT_API_URL)
      # 3. ~/.augment/session.json (created by `auggie login`)
      context = DirectContext.create()

      # Add files to index
      result = context.add_to_index([
          File(path='src/main.py', contents='def main(): ...'),
          File(path='src/auth.py', contents='def authenticate(): ...')
      ])

      print(f"Newly uploaded: {len(result.newly_uploaded)}")
      print(f"Already uploaded: {len(result.already_uploaded)}")

      # Search - returns formatted string ready for LLM use or display
      results = context.search('authentication logic')
      print(results)

      # Or use search_and_ask for one-step Q&A
      answer = context.search_and_ask(
          'How does authentication work?'
      )
      print(answer)

      # Save state to avoid re-indexing
      context.export_to_file('/tmp/state.json')

  if __name__ == '__main__':
      main()
  ```
</CodeGroup>

## FileSystem Context

Automatically index and search a local directory - just point to a directory path and start searching, perfect for local development and testing:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { FileSystemContext } from '@augmentcode/auggie-sdk';

  async function main() {
    const context = await FileSystemContext.create({
      directory: '/path/to/workspace',
    });

    // Search the directory
    const results = await context.search('authentication logic');
    console.log(results);

    // Or ask a question
    const answer = await context.searchAndAsk(
      'How does authentication work?'
    );
    console.log(answer);

    // Clean up
    await context.close();
  }

  main();
  ```

  ```python Python theme={null}
  from auggie_sdk.context import FileSystemContext

  def main():
      # Use context manager for automatic cleanup
      with FileSystemContext.create('/path/to/workspace') as context:
          # Search the directory
          results = context.search('authentication logic')
          print(results)

          # Or ask a question
          answer = context.search_and_ask(
              'How does authentication work?'
          )
          print(answer)

  if __name__ == '__main__':
      main()
  ```
</CodeGroup>

## Next Steps

<CardGroup>
  <Card title="Examples" icon="lightbulb" href="/context-services/sdk/examples">
    See more example applications
  </Card>

  <Card title="API Reference" icon="code" href="/context-services/sdk/api-reference">
    Explore the complete API
  </Card>
</CardGroup>


# Introduction
Source: https://docs.augmentcode.com/introduction

Augment is the developer AI platform that helps you understand code, debug issues, and ship faster because it understands your codebase. Use Agent, Next Edit, and Code Completions to get more done.

<img alt="Augment Code" />

## Get started in minutes

Augment works with your favorite IDE and your favorite programming language. Download the extension, sign in, and get coding.

<CardGroup>
  <Card href="/setup-augment/install-visual-studio-code">
    <img alt="Visual Studio Code" />

    <h2>
      Visual Studio Code
    </h2>

    <p>
      Get completions, chat, and instructions in your favorite open source
      editor.
    </p>
  </Card>

  <Card href="/setup-augment/install-jetbrains-ides">
    <img alt="JetBrains IDEs" />

    <h2>
      JetBrains IDEs
    </h2>

    <p>
      Completions are available for all JetBrains IDEs, like WebStorm, PyCharm,
      and IntelliJ.
    </p>
  </Card>

  <Card href="/cli/overview">
    <img alt="Auggie CLI" />

    <h2>
      Auggie CLI
    </h2>

    <p>
      All the power of Augment's agent, context engine, and tools in your terminal.
    </p>
  </Card>
</CardGroup>

## Learn more

Get up to speed, stay in the flow, and get more done. Chat, Next Edit, and Code Completions will change the way you build software.

<CardGroup>
  <Card title="Agent" icon={<AgentIcon />} href="/using-augment/agent">
    Autonomous coding with Augment's context engine and tools can tackle tasks big and small
  </Card>

  <Card title="Next Edit" icon={<NextEditIcon />} href="/using-augment/next-edit">
    Keep moving through your tasks by guiding you step-by-step through complex or repetitive changes.
  </Card>

  <Card title="Code Completions" icon={<CodeIcon />} href="/using-augment/completions">
    Intelligent code suggestions that knows your codebase right at your
    fingertips.
  </Card>
</CardGroup>


# Agent Integrations
Source: https://docs.augmentcode.com/jetbrains/setup-augment/agent-integrations

Configure integrations for Augment Agent to access external services like GitHub, Linear, Jira, Confluence, and Notion.

## About Agent Integrations

Augment Agent can access external services through integrations to add additional context to your requests and take actions on your behalf. These integrations allow Augment Agent to seamlessly work with your development tools without leaving your editor.

Once set up, Augment Agent will automatically use the appropriate integration based on your request context. Or, you can always mention the service in your request to use the integration.

## Setting Up Integrations

To set up integrations with Augment Agent in JetBrains IDEs, follow these steps:

1. Click the Augment icon in the bottom right of your IDE and select <Command />
2. Click "Connect" for the integration you want to set up

<img alt="Set up integrations in the settings page" />

You'll be redirected to authorize the integration with the appropriate service. After authorization, the integration will be available for use with Augment Agent.

## Easy MCP Integrations

> **New:** Easy MCP launched ONLY July 30, 2025, providing one-click access to popular developer tools.

Easy MCP transforms complex MCP server setup into a single click. Available integrations include:

* **CircleCI** - Build logs, test insights, and flaky-test detection
* **MongoDB** - Data exploration, database management, and context-aware code generation
* **Redis** - Keyspace introspection, TTL audits, and migration helpers

For detailed setup instructions and examples, see [Configure MCP servers](/jetbrains/setup-augment/mcp).

## Native Integrations

## <div><div><GitHubLogo /></div> GitHub Integration</div>

Add additional context to your requests and take actions. Pull in information from a GitHub Issue, make the changes to your code (or have Agent do it for you), and open a Pull Request all without leaving your editor.

### Examples

* "Implement Issue #123 and open up a pull request"
* "Find all issues assigned to me"
* "Check the CI status of my latest commit"

For authorization details, see [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party).

## <div><div><LinearLogo /></div> Linear Integration</div>

Read, update, comment on, and resolve your Linear issues within your IDE.

### Examples

* "Fix TES-1"
* "Create Linear tickets for these TODOs"
* "Help me triage these new bug reports"

For authorization details, see [Linear documentation](https://linear.app/docs/third-party-application-approvals).

## <div><div><JiraLogo /></div> Jira Integration</div>

Work on your Jira issues, create new tickets, and update existing ones.

### Examples

* "Show me all my assigned Jira tickets"
* "Create a Jira ticket for this bug"
* "Create a PR to fix SOF-123"
* "Update the status of PROJ-123 to 'In Progress'"

For authorization details, see [Jira documentation](https://support.atlassian.com/jira-software-cloud/docs/allow-oauth-access/).

## <div><div><ConfluenceLogo /></div> Confluence Integration</div>

Query existing documentation or update pages directly from your IDE. Ensure your team's knowledge base stays current without any context switching.

### Examples

* "Summarize our Confluence page on microservice architecture"
* "Find information about our release process in Confluence"
* "Update our onboarding docs to explain how we use Bazel"

For authorization details, see [Confluence documentation](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/).

## <div><div><NotionLogo /></div> Notion Integration</div>

Search and retrieve information from your team's knowledge base - access documentation, meeting notes, and project specifications. This integration is currently READ-ONLY.

### Examples

* "Find Notion pages about our API documentation"
* "Show me the technical specs for the payment system"
* "What outstanding tasks are left from yesterday's team meeting?"

For authorization details, see [Notion documentation](https://www.notion.so/help/add-and-manage-connections-with-the-api#install-from-a-developer).

## <div><div><GleanLogo /></div> Glean Integration</div>

> **Note:** The Glean integration is in early access and thus is a little different from other integrations.
>
> * It is currently only available to enterprise customers.
> * It does not appear in the list of integrations in the settings panel.

The Glean integration lets the agent retrieve information from your team's internal data sources leveraging Glean's powerful search engine.

**To Enable the Glean Integration:** You'll need to be have administrator access to Augment and Glean. Follow the instructions on [https://app.augmentcode.com/gleanConfig](https://app.augmentcode.com/gleanConfig) and your agent will be ready to use Glean!

### Examples

* "Search Glean for past related incidents and how they were resolved"
* "Search Glean for why we're migrating to a new payment processor"

## Next Steps

* [Configure additional tools with Easy MCP or advanced MCP setup](/jetbrains/setup-augment/mcp)
* Explore one-click integrations for CircleCI, MongoDB, and Redis through Easy MCP


# Install Augment for JetBrains IDEs
Source: https://docs.augmentcode.com/jetbrains/setup-augment/install-jetbrains-ides

Are you ready for your new superpowers? Augment in JetBrains IDEs gives you powerful code completions integrated into your favorite text editor.

<Info>
  Augment requires version `2024.3` or above for all JetBrains IDEs. [See
  JetBrains documentation](https://www.jetbrains.com/help/) on how to update
  your IDE.
</Info>

<CardGroup>
  <Card title="Get the Augment Plugin" href="https://plugins.jetbrains.com/plugin/24072-augment" icon={<JetbrainsLogo />}>
    Install Augment for JetBrains IDEs
  </Card>
</CardGroup>

## About Installation

Installing <ExternalLink href="https://plugins.jetbrains.com/plugin/24072-augment" /> is easy and will take you less than a minute. Augment is compatible with all JetBrains IDEs, including WebStorm, PyCharm, and IntelliJ. You can find the Augment plugin in the JetBrains Marketplace and install it following the instructions below.

<img alt="Augment plugin in JetBrains Marketplace" />

## Installing Augment for JetBrains IDEs

<Note>
  For these instructions we'll use *JetBrains IntelliJ* as an example, anywhere
  you see *IntelliJ* replace the name of the JetBrains IDE you're using.

  In the case of Android Studio, which is based on IntelliJ, please ensure that your installation
  uses a runtime with JCEF. Go to <Command />, type <Command />
  and press <Keyboard />. Ensure the current runtime ends with `-jcef`; if not, select one **with JCEF** from the options
  below.
</Note>

<Steps>
  <Step title="Make sure you have the latest version of your IDE installed">
    You can download the latest version of JetBrains IDEs from the <ExternalLink href="https://www.jetbrains.com/ides/#choose-your-ide" />
    website. If you already have IntelliJ installed, you can update to the
    latest version by going to
    <Command />.
  </Step>

  <Step title="Open the Plugins settings in your IDE">
    From the menu bar, go to <Command />, or
    use the keyboard shortcut <Keyboard /> to open the
    Settings window. Select <Command /> from the sidebar.
  </Step>

  <Step title="Search for Augment in the marketplace">
    Using the search bar in the Plugins panel, search for
    <Command />.
  </Step>

  <Step title="Install the extension">
    Click <Command /> to install the extension. Then click
    <Command /> to close the Settings window.
  </Step>

  <Step title="Sign into Augment and get coding">
    Sign in to by clicking <Command /> in the Augment
    panel. If you do not see the Augment panel, use the shortcut
    <Keyboard /> or click the Augment icon
    <img /> in the side bar of your IDE. See more details in [Sign
    In](/setup-augment/sign-in).
  </Step>
</Steps>

## Installing Beta versions of Augment for JetBrains IDEs

In order to get a specific bug fix or feature, sometimes you may need to *temporarily* install a beta version of Augment for JetBrains IDEs.
To do this, follow the steps below:

<Steps>
  <Step title="Download an archive of the beta version">
    You can download the latest beta version of Augment from <ExternalLink href="https://plugins.jetbrains.com/plugin/24072-augment/versions/beta?noRedirect=true" />
    website. Please click <Command /> on the latest version and save the archive to disk.
  </Step>

  <Step title="Open the Plugins settings in your IDE">
    From the menu bar, go to <Command />, or
    use the keyboard shortcut <Keyboard /> to open the
    Settings window. Select <Command /> from the sidebar.
  </Step>

  <Step title="Install Augment from the downloaded archive">
    Click on the gear icon next to <Command /> tab and click <Command />.
    Select the archive you downloaded in the previous step and click <Command />.
  </Step>
</Steps>


# Keyboard Shortcuts for JetBrains IDEs
Source: https://docs.augmentcode.com/jetbrains/setup-augment/jetbrains-keyboard-shortcuts

Augment integrates with your IDE to provide keyboard shortcuts for common actions. Use these shortcuts to quickly accept suggestions, write code, and navigate your codebase.

## About keyboard shortcuts

Augment is deeply integrated into your IDE and utilizes many of the standard keyboard shortcuts you are already familiar with. These shortcuts allow you to quickly accept suggestions, write code, and navigate your codebase. We also suggest updating a few keyboard shortcuts to make working with code suggestions even easier.

<Tabs>
  <Tab title="MacOS">
    To update keyboard shortcuts, use one of the following:

    | Method   | Action                          |
    | :------- | :------------------------------ |
    | Keyboard | <Keyboard /> select <Command /> |
    | Menu bar | <Command />                     |

    ## General

    | Action             | Default shortcut |
    | :----------------- | :--------------- |
    | Open Augment panel | <Keyboard />     |

    ## Chat

    | Action                   | Default shortcut |
    | :----------------------- | :--------------- |
    | Focus or open Chat panel | <Keyboard />     |

    ## Completions

    | Action                       | Default shortcut |
    | :--------------------------- | :--------------- |
    | Accept entire suggestion     | <Keyboard />     |
    | Accept word-by-word          | <Keyboard />     |
    | Reject suggestion            | <Keyboard />     |
    | Toggle automatic completions | <Keyboard />     |
  </Tab>

  <Tab title="Windows/Linux">
    To update keyboard shortcuts, use one of the following:

    | Method   | Action                               |
    | :------- | :----------------------------------- |
    | Keyboard | <Keyboard /> then select <Command /> |
    | Menu bar | <Command />                          |

    ## General

    | Action             | Default shortcut |
    | :----------------- | :--------------- |
    | Open Augment panel | <Keyboard />     |

    ## Chat

    | Action                   | Default shortcut |
    | :----------------------- | :--------------- |
    | Focus or open Chat panel | <Keyboard />     |

    ## Completions

    | Action                       | Default shortcut |
    | :--------------------------- | :--------------- |
    | Accept entire suggestion     | <Keyboard />     |
    | Accept word-by-word          | <Keyboard />     |
    | Reject suggestion            | <Keyboard />     |
    | Toggle automatic completions | <Keyboard />     |
  </Tab>
</Tabs>


# Setup Model Context Protocol servers
Source: https://docs.augmentcode.com/jetbrains/setup-augment/mcp

Use Model Context Protocol (MCP) servers with Augment to expand Augment's capabilities with external tools and data sources.

## About Model Context Protocol servers

Augment Agent can utilize external integrations through Model Context Protocol (MCP) to access external systems for information and integrate tools to take actions. MCP is an open protocol that provides a standardized way to connect AI models to different data sources and tools. MCP servers can be used to access local or remote databases, run automated browser testing, send messages to Slack or even play music on Spotify.

## Easy MCP: One-Click Integrations

> **New:** Easy MCP launched on July 30, 2025, making it easier than ever to connect popular developer tools to Augment Code.

Easy MCP is a new feature in the Augment Code extension that transforms complex MCP server setup into a single click. Instead of manually configuring servers, hunting for GitHub repos, or editing JSON files, you can now connect popular developer tools with just an API token or OAuth approval.

### Available Easy MCP Integrations

Easy MCP provides one-click access to these popular developer tools:

#### CircleCI

* **Context:** Build logs, test insights, flaky-test detection
* **Sample prompt:** "Find the latest failed pipeline on my branch and surface the failing tests."
* **Setup:** Click "+", paste your CircleCI API token, and you're connected.

#### MongoDB

* **Context:** Data exploration, database management, and context-aware code generation
* **Sample prompt:** "Analyze my user collection schema and suggest optimizations for our new search feature."
* **Setup:** One-click OAuth connection to your MongoDB instance.

#### Redis

* **Context:** Keyspace introspection, TTL audits, and migration helpers
* **Sample prompt:** "Generate a migration script to move expiring session keys to the new namespace."
* **Setup:** Connect with your Redis credentials in seconds.

### Getting Started with Easy MCP

1. Open the Augment Code extension in your JetBrains IDE
2. Navigate to the Easy MCP pane in the settings
3. Click the "+" button next to your desired integration
4. Paste an API token or approve OAuth
5. Start using the integration immediately in your Agent conversations

<img />

From that moment on, Augment Code streams your tool's live context into every suggestion and autonomous Agent run.

## Advanced Configuration: Settings Panel

For developers who need custom MCP server configurations or want to use servers not available through Easy MCP, you can configure MCP servers manually using the Augment Settings Panel.

To access the settings panel, select the gear icon in the upper right of the Augment panel. Once the settings panel is open, you will see a section for MCP servers.

<img />

Fill in the `name` and `command` fields. The `name` field must be a unique name for the server. The `command` field is the command to run the server. Environment variables have their own section and no longer need to be specified in the command.

<img />

To add additional servers, click the `+` button next to the `MCP` header.
To edit a configuration or to delete a server, click the `...` button next to the server name.

### Add a Remote MCP server

If your MCP server runs remotely (for example, a hosted service), click the "+ Add remote MCP" button in the MCP section. Remote MCP connections support both HTTP and SSE (Server‑Sent Events).

<img />

* Connection Type: choose HTTP or SSE
* Name: a unique display name for the server
* URL: the base URL to your MCP server (e.g., [https://api.example.com](https://api.example.com))

Remote MCP servers appear alongside your local MCP servers in the list. You can edit or remove them using the "..." menu next to the server name.

## Server compatibility

Not all MCP servers are compatible with Augment's models. The MCP standard, implementation of specific servers, and Augment's MCP support are frequently being updated, so check compatibility frequently.


# Index your workspace
Source: https://docs.augmentcode.com/jetbrains/setup-augment/workspace-indexing

When your workspace is indexed, Augment can provide tailored code suggestions and answers based on your unique codebase, best practices, coding patterns, and preferences. You can always control what files are indexed.

## About indexing your workspace

When you open a workspace with Augment enabled, your codebase will be automatically uploaded to Augment's secure cloud. You can control what files get indexed using `.gitignore` and `.augmentignore` files. Indexing usually takes less than a minute but can take longer depending on the size of your codebase.

## Security and privacy

Augment stores your code securely and privately to enable our powerful context engine. We ensure code privacy through a proof-of-possession API and maintain strict internal data minimization principles. [Read more about our security](https://www.augmentcode.com/security).

## What gets indexed

Augment will index all the files in your workspace, except for the files that match patterns in your `.gitignore` file and the `.augmentignore` file.

## Ignoring files with .augmentignore

The `.augmentignore` file is a list of file patterns that Augment will ignore when indexing your workspace. Create an `.augmentignore` file in the root of your workspace. You can use any glob pattern that is supported by the [gitignore](https://git-scm.com/docs/gitignore) file.

## Including files that are .gitignored

If you have a file or directory in your `.gitignore` that you want to indexed, you can add it to your `.augmentignore` file using the `!` prefix.

For example, you may want your `node_modules` indexed to provide Augment with context about the dependencies in their project, but it is typically included in their `.gitignore`. Add `!node_modules` to your `.augmentignore` file.

<CodeGroup>
  ```bash .augmentignore theme={null}
  # Include .gitignore excluded files with ! prefix
  !node_modules

  # Exclude other files with .gitignore syntax
  data/test.json
  ```

  ```bash .gitignore theme={null}
  # Exclude dependencies
  node_modules

  # Exclude secrets
  .env

  # Exclude build artifacts
  out
  build
  ```
</CodeGroup>


# Using Agent
Source: https://docs.augmentcode.com/jetbrains/using-augment/agent

Use Agent to complete simple and complex tasks across your workflow–implementing a feature, upgrade a dependency, or writing a pull request.

## About Agent

Augment Agent is a powerful tool that can help you complete software development tasks end-to-end. From quick edits to complete feature implementation, Agent breaks down your requests into a functional plan and implements each step all while keeping you informed about what actions and changes are happening. Powered by Augment's Context Engine and powerful LLM architecture, Agent can write, document, and test like an experienced member of your team.

## Accessing Agent

To access Agent, simply open the Augment panel and select one of the Agent modes from the drop down in the input box.

<img alt="Augment Agent" />

### Choosing a model

Use the model dropdown in the Augment panel to switch between Claude Sonnet 4 and GPT-5. Your selection applies only to Agent for the current workspace and can be changed at any time. See [Available Models](/models/available-models) for details.

## Using Agent

To use Agent, simply type your request into the input box using natural language and click the submit button. You will see the default context including current workspace, current file, and Agent memories. You can add additional context by clicking <AtIcon />and selecting files or folder, or add an image as context by clicking the paperclip. Agent can create, edit, or delete code across your workspace and can use tools like the terminal and external integrations through MCP to complete your request.

### Enhancing your prompt

You can improve the quality of your  by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Reviewing changes

You can review every change Agent makes by clicking on the action to expand the view. Review diffs for file changes, see complete terminal commands and output, and the results of external integration calls.

<img alt="Augment Agent" />

### Checkpoints

Checkpoints are automatically saved snapshots of your workspace as Agent implements the plan allowing you to easily revert back to a previous step. This enables Agent to continue working while you review code changes and commands results. To revert to a previous checkpoint, click the reverse arrow to restore your code.

<img alt="Augment Agent" />

### Agent vs Agent Auto

By default, Agent will pause work when it needs to execute a terminal command or access external integrations. After reviewing the suggested action, click the blue play button to have Agent execute the command and continue working. You tell Agent to skip a specific action by clicking on the three dots and then Skip.

<img alt="Augment Agent" />

In Agent Auto, Agent will act more independently. It will edit files, execute terminal commands, and access tools like MCP servers automatically.

### Stop or guide the Agent

You can interrupt the Agent at any time by clicking Stop. This will pause the action to allow you to correct something you see the agent doing incorrectly. While Agent is working, you can also prompt the Agent to try a different approach which will automatically stop the agent and prompt it to correct its course.

<img alt="Stopping the agent" />

### Quick Ask Mode

Quick Ask Mode is a toggle button in the agent chat interface that restricts the AI to read-only tools only. When activated, it adds a visual badge to the message and focuses the AI on information gathering without making any changes to your codebase.

<img alt="Quick Ask Mode toggle and usage" />

### Comparison to Chat

Agent takes Chat to the next level by allowing Augment to do things for you-that is create and make modifications directly to your codebase. Chat can explain code, create plans, and suggest changes which you can smartly apply one-by-one, but Agent takes it a step further by automatically implementing the entire plan and all code changes for you.

| What are you trying to do?                       | Chat | Agent |
| :----------------------------------------------- | :--: | :---: |
| Ask questions about your code                    |  ☑️  |   ✅   |
| Get advice on how to refactor code               |  ☑️  |   ✅   |
| Add new features to selected lines of code       |  ☑️  |   ✅   |
| Add new feature spanning multiple files          |      |   ✅   |
| Document new features                            |      |   ✅   |
| Queue up tests for you in the terminal           |      |   ✅   |
| Open Linear tickets or start a pull request      |      |   ✅   |
| Start a new branch in GitHub from recent commits |      |   ✅   |
| Automatically perform tasks on your behalf       |      |   ✅   |

### Use cases

Use Agent to handle various aspects of your software development workflow, from simple configuration changes to complex feature implementations. Agent supports your daily engineering tasks like:

* **Make quick edits** - Create a pull request to adjust configuration values like feature flags from FALSE to TRUE
* **Perform refactoring** - Move functions between files while maintaining coding conventions and ensuring bug-free operation
* **Start a first draft for new features** - Start a pull request (PR) with implementing entirely new functionality straight from a GitHub Issue or Linear Ticket
* **Branch from GitHub** - Open a PR from GitHub based on recent commits that creates a new branch
* **Query Supabase tables directly** - Ask Agent to view the contents of a table
* **Start tickets in Linear or Jira** - Open tickets and ask Agent to suggest a plan to address the ticket
* **Add Pull Request descriptions** - Merge your PR into a branch then tell the agent to explain what the changes are and why they were made
* **Create test coverage** - Generate unit tests for your newly developed features
* **Generate documentation** - Produce comprehensive documentation for your libraries and features
* **Start a README** - Write a README for a new feature or updated function that you just wrote
* **Track development progress** - Review and summarize your recent Git commits for better visibility with the GitHub integration

## Next steps

* [Configure Agent Integrations](/jetbrains/setup-augment/agent-integrations)


# Using Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

## About Chat

Chat is a new way to work with your codebase using natural language. Chat will automatically use the current workspace as context and you can [provide focus](/using-augment/chat-context) for Augment by selecting specific code blocks, files, folders, or external documentation. Details from your current chat, including the additional context, are used to provide more relevant code suggestions as well.

<img alt="Augment Chat" />

## Accessing Chat

Access the Chat sidebar by clicking the Augment icon <img /> in the sidebar or the status bar. You can also open Chat by using one of the keyboard shortcuts below.

**Keyboard Shortcuts**

| Platform      | Shortcut     |
| :------------ | :----------- |
| MacOS         | <Keyboard /> |
| Windows/Linux | <Keyboard /> |

## Using Chat

To use Chat, simply type your question or command into the input field at the bottom of the Chat panel. You will see the currently included context which includes the workspace and current file by default. Use Chat to explain your code, investigate a bug, or use a new library. See [Example Prompts for Chat](/using-augment/chat-prompts) for more ideas on using Chat.

### Enhancing your prompt

You can improve the quality of your  by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Conversations about code

To get the best possible results, you can go beyond asking simple questions or commands, and instead have a back and forth conversation with Chat about your code. For example, you can ask Chat to explain a specific function and then ask follow-up questions about possible refactoring options. Chat can act as a pair programmer, helping you work through a technical problem or understand unfamiliar code.

### Starting a new chat

You should start a new Chat when you want to change the topic of the conversation since the current conversation is used as part of the context for your next question. To start a new chat, open the Augment panel and click the new chat icon <NewChatIcon /> at the top-right of the Chat panel.

### Previous chats

You can continue a chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel. Your previous chats will be listed in reverse chronological order, and you can continue your conversation where you left off.

### Deleting a chat

You can delete a previous chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel to show the list of previous chats. Click the delete icon <DeleteIcon /> next to the chat you want to delete. You will be asked to confirm that you want to delete the chat.


# Using Actions in Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-actions

Actions let you take common actions on code blocks without leaving Chat. Explain, improve, or find everything you need to know about your codebase.

<img alt="Augment Chat Actions" />

## Using actions in Chat

To use a quick action, you an use a <Keyboard /> command or click the up arrow icon<ArrowUpIcon />to show the available actions. For explain, fix, and test actions, first highlight the code in the editor and then use the command.

| Action       | Usage                                                                    |
| :----------- | :----------------------------------------------------------------------- |
| <Keyboard /> | Use natural language to find code or functionality                       |
| <Keyboard /> | Augment will explain the hightlighted code                               |
| <Keyboard /> | Augment will suggest improvements or find errors in the highlighted code |
| <Keyboard /> | Augment will suggest tests for the highlighted code                      |

Augment will typically include code blocks in the response to the action. See [Applying code blocks from Chat](/using-augment/chat-apply) for more details.


# Applying code blocks from Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-apply

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

<img alt="Augment Chat Apply" />

## Using code blocks from within Chat

Whenever Chat responds with code, you will have the option to add the code to your codebase. The most common option will be shown as a button and you can access the other options by clicking the overflow menu icon<MoreVertIcon />at the top-right of the code block. You can use the following options to apply the code:

* <FileCopyIcon />**Copy**
  the code from the block to your clipboard
* <FileNewIcon />**Create**
  a new file with the code from the block
* <CheckIcon />**Apply**
  the code from the block intelligently to your file


# Focusing Context in Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-context

You can specify context from files, folders, and external documentation in your conversation to focus your chat responses.

## About Chat Context

Augment intelligently includes context from your entire workspace based on the ongoing conversation–even if you don't have the relevant files open in your editor–but sometimes you want Augment to prioritize specific details for more relevant responses.

<video />

### Focusing context for your conversation

You can specify context by clicking the <AtIcon /> icon at the top-left of the Chat panel or by <Command /> in the input field. You can use fuzzy search to filter the list of context options quickly. There are a number of different types of additional context you can add to your conversation:

1. Highlighted code blocks
2. Specific files or folders within your workspace
3. 3rd party documentation, like Next.js documentation

#### Mentioning files and folders

Include specific files or folders in your context by typing `@` followed by the file or folder name. For example, `@routes.tsx` will include the `routes.tsx` file in your context. You can include multiple files or folders.

#### Mentioning 3rd party documentation

You can also mention 3rd party documentation in your context by typing `@` followed by the name of the documentation. For example, `@Next.js` will include Next.js documentation in your context. Augment provides nearly 300 documentation sets spanning across a wide range of domains such as programming languages, packages, software tools, and frameworks.


# Example Prompts for Chat
Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-prompts

Using natural language to interact with your codebase unlocks a whole new way of working. Learn how to get the most out of Chat with the following example prompts.

## About chatting with your codebase

Augment's Chat has deep understanding about your codebase, dependencies, and best practices. You can use Chat to ask questions about your code, but it also can help you with general software engineering questions, think through technical decisions, explore new libraries, and more.

## Enhancing your prompt

You can improve the quality of your  by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

## Example Prompts

### Explain code

* Explain this codebase to me
* How do I use the Twilio API to send a text message?
* Explain how generics work in TypeScript and give me a simple example

### Finding code

* Where are all the useEffect hooks that depend on the 'currentUser' variable?
* Find the decorators that implement retry logic across our microservices
* Find coroutines that handle database transactions without a timeout parameter

### Generate code

* Write a function to check if a string is a valid email address
* Generate a middleware function that rate-limits API requests using a sliding window algorithm
* Create a SQL query to find the top 5 customers who spent the most money last month

### Write tests

* Write integration tests for this API endpoint
* What edge cases have I not included in this test?
* Generate mock data for testing this customer order processing function

### Refactor and improve code

* This function is running slowly with large collections - how can I optimize it?
* Refactor this callback-based code to use async/await instead
* Rewrite this function in Rust

### Find and fix errors

* This endpoint sometimes returns a 500 error. Here's the error log - what's wrong?
* I'm getting 'TypeError: Cannot read property 'length' of undefined' in this component.
* Getting CORS errors when my frontend tries to fetch from the API


# Completions
Source: https://docs.augmentcode.com/jetbrains/using-augment/completions

Use code completions to get more done. Augment's radical context awareness means more relevant suggestions, fewer hallucinations, and less time hunting down documentation.

## About Code Completions

Augment's Code Completions integrates with your IDE's native completions system to give you autocomplete-like suggestions as you type. You can accept all of a suggestion, accept partial suggestions a word or a line at a time, or just keep typing to ignore the suggestion.

## Using Code Completions

To use code completions, simply start typing in your IDE. Augment will provide suggestions based on the context of your code. You can accept a suggestion by pressing <Keyboard />, or ignore it by continuing to type.

For example, add the following function to a TypeScript file:

```typescript theme={null}
function getUser(): Promise<User>;
```

As you type `getUser`, Augment will suggest the function signature. Press <Keyboard /> to accept the suggestion. Augment will continue to offer suggestions until the function is complete, at which point you will have a function similar to:

```typescript theme={null}
function getUser(): Promise<User> {
  return fetch("/api/user/1")
    .then((response) => response.json())
    .then((json) => {
      return json as User;
    });
}
```

### Accepting Completions

<Tabs>
  <Tab title="MacOS">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard />                           |
    | Accept next word of suggestion | <Keyboard />                           |
    | Accept next line of suggestion | None (see above)                       |
    | Reject suggestion              | <Keyboard />                           |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | VSCode: <Keyboard />                   |
    |                                | JetBrains: <Keyboard />                |
  </Tab>

  <Tab title="Windows/Linux">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard />                           |
    | Accept next word of suggestion | <Keyboard />                           |
    | Accept next line of suggestion | None (see above)                       |
    | Reject suggestion              | <Keyboard />                           |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | VSCode: <Keyboard />                   |
    |                                | JetBrains: <Keyboard />                |
  </Tab>
</Tabs>

### Disabling Completions

<Tabs>
  <Tab title="Visual Studio Code">
    You can disable automatic code completions by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command />.
  </Tab>

  <Tab title="JetBrains IDEs">
    You can disable automatic code completions by clicking the Augment icon <img /> in the status bar at the bottom right corner of your IDE, then selecting <Command />.
  </Tab>
</Tabs>

### Enable Completions

<Tabs>
  <Tab title="Visual Studio Code">
    If you've temporarily disabled completions, you can re-enable them by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command />.
  </Tab>

  <Tab title="JetBrains IDEs">
    If you've temporarily disabled completions, you can re-enable them by clicking the Augment icon <img /> in the status bar at the bottom right corner of your IDE, then selecting <Command />.
  </Tab>
</Tabs>


# Using Tasklist
Source: https://docs.augmentcode.com/jetbrains/using-augment/tasklist

Use Tasklist to break down complex problems into manageable steps, track progress, and collaborate with Agent on multi-step tasks.

## What is the Tasklist?

Augment's Tasklist helps the Agent create and refine a step-by-step plan for you to review. The Tasklist provides a structured interface for collaboration between you and the Agent, allowing you to break down complex problems into manageable, sequential steps.

<img alt="Tasklist Overview" />

## Why Tasklist?

Tasklist improves agent effectiveness on long or complex tasks by:

* **Maintaining context** across different conversations by moving your Tasklist to a new chat
* **Breaking down complex problems** into manageable, sequential steps
* **Gathering progress** across threads
* **Exploring alternative solutions** to completed tasks if you need to pivot
* **Streamlining your approach** to nebulous problems by deleting irrelevant steps once the path forward is clear

Tasklist provides a structured interface for collaboration and opens up possibilities for agent-to-agent collaboration. We hypothesize that an interface such as Tasklist could be a preferred way to interact with coding agents in the future.

## Tasklist in Action

<img alt="Tasklist demonstration" />

## Creating a New Task

### Automatic Creation

The Agent will usually create a Tasklist when it encounters a complex, multi-step problem. You can also ask the Agent to make a Tasklist for you by simply prompting "Start a Tasklist to..." then add the problem you are trying to tackle.

### Manual Creation

You can also manually create a Tasklist:

1. Switch to Tasklist using the checklist button next to Changes
2. Click the plus to add your first task
3. Alternatively, you can create a new task by typing in the gray prompt box at the bottom of the extension. Click **Add Task** from the dropdown arrow next to Send

<img alt="Creating a new task" />

## Running Tasks

To run a task, click the grey triangle (play button) next to the task. The Agent will begin executing the task and update its status as it progresses.

<img alt="Running a task" />

## Task Status Indicators

Task statuses are indicated by different colors and icons:

* **Empty circle** - Task has not yet started
* **Blue half circle** - Task is currently in progress
* **Green checkbox** - Task has been completed and is ready for review

<img alt="Task status indicators" />

## Subtasks

Augment Code automatically generates subtasks when needed. The Agent will automatically add and nest required subtasks under your initial tasks. You can edit and expand these subtasks just like any other task in the list. Likewise, you can remove subtasks you deem unnecessary.

<img alt="Subtasks example" />

## Managing Running Tasks

### Stopping a Task

You can treat any in-progress task like any prompt you might send the Agent. To stop what the Agent is doing and offer a corrective action, click the red square (stop button) and tell the Agent what you want it to do instead.

### Running All Tasks

The Agent can complete all the tasks sequentially by clicking the triangle (play button) at the top of the Tasklist.

## Reviewing Changes

You can review the changes made by the Agent after a task is completed by toggling between the Tasks and Changes view to see the diffs (differences) of the work done by the agent for each task.

<img alt="Reviewing changes in Tasks and Changes view" />

## Integration with Task Management Tools

### Jira and Linear Integration

The Tasklist is a perfect pairing with existing task management tools like Jira or Linear:

* Ask the Agent to create a Tasklist based on tickets inside Jira or Linear
* Further break down complex tickets into manageable steps
* Once your Tasklist is completed, you can ask the Agent to resolve the issue inside Jira or Linear and append the steps taken as a comment

### Standalone Usage

Don't use an issue tracker? No problem - use Tasklist to track issues you need to tackle across Threads.

## Best Practices

* **Be specific** when creating tasks to help the Agent understand exactly what needs to be done
* **Review and edit** the automatically generated subtasks to ensure they align with your goals
* **Use the stop function** to provide course corrections when the Agent is heading in the wrong direction
* **Leverage the Changes view** to review all modifications made during task execution
* **Move Tasklists** between conversations to maintain context across different chat sessions

## Next Steps

* [Learn more about Agent](/jetbrains/using-augment/agent)
* [Configure Agent Integrations](/jetbrains/setup-augment/agent-integrations)


# Available Models
Source: https://docs.augmentcode.com/models/available-models

The LLMs currently available in Augment and how we use them.

## Current models

Augment uses world-class large language models together with our Context Engine. We currently support the following models:

* Claude Haiku 4.5 by Anthropic
* Claude Opus 4.5 by Anthropic
* Claude Sonnet 4 by Anthropic
* Claude Sonnet 4.5 by Anthropic
* GPT-5.1 by OpenAI
* GPT-5.2 by OpenAI

## Choosing a model

You can select the model directly using the Model Picker in the Augment.

* In VS Code and JetBrains, open the Augment panel and use the model dropdown near the input box to switch models.
* In Auggie CLI, use the `/model` slash command or pass the `--model` flag with the desired model.
* Your selection applies only to Agent in that workspace and can be changed at any time.

If you don't pick a model, Augment will use your last selection or the default set by your organization.

## Model pricing

Augment uses a credit-based pricing system. Different models consume credits at different rates based on their capabilities and costs:

* **Sonnet 4.5**: Baseline credit consumption for balanced, complex tasks
* **Opus 4.5**: \~167% of Sonnet's cost - most capable model for the hardest tasks
* **Haiku 4.5**: \~30% of Sonnet's cost - ideal for quick, simple tasks
* **GPT-5.1**: \~75% of Sonnet's cost - great for medium-complexity work
* **GPT-5.2**: \~133% of Sonnet's cost - enhanced reasoning for complex tasks

<Card title="Credit-Based Pricing" icon="credit-card" href="/models/credit-based-pricing">
  Learn more about credit costs, see detailed examples, and discover tips for optimizing your credit usage
</Card>

## Feature compatibility

Both models support the core Augment Agent features:

* Deep code understanding with Augment's Context Engine
* Tool use (integrations and MCP), file edits, and multi-step planning

Some behaviors (e.g., wording or style) may vary slightly between models. We'll continue to refine prompts and guardrails to provide a consistent developer experience.

## Notes and transparency

* We may roll out model updates gradually. If you're part of a staged rollout, different workspaces or teammates may see updates at different times.
* For troubleshooting, you can share the request ID with our support team; they can confirm which model handled a specific request.

If you have questions about model availability or want to participate in early access programs, please reach out via Support.


# Credit-Based Pricing
Source: https://docs.augmentcode.com/models/credit-based-pricing

Understand how credits work and how different models consume credits at different rates.

## Overview

Augment uses a credit-based pricing system where different models consume credits at different rates to reflect their power and cost. This gives you the flexibility to choose the right model for each task based on complexity and budget.

## Credit costs by model

Each model consumes credits at different rates based on its capabilities and underlying costs. Here's how the models compare:

| Model                 | Credits per task\* | Relative cost   | Best for                                                                                                                 |
| :-------------------- | :----------------- | :-------------- | :----------------------------------------------------------------------------------------------------------------------- |
| **Claude Sonnet 4.5** | 293 credits        | Baseline (100%) | Balanced capability. Ideal for medium or large tasks and is optimized for complex or multi-step work.                    |
| **Claude Opus 4.5**   | 488 credits        | 167% of Sonnet  | Most capable model. Best for the hardest tasks requiring deep reasoning, nuanced understanding, and exceptional quality. |
| **Claude Haiku 4.5**  | 88 credits         | 30% of Sonnet   | Lightweight, fast reasoning. Best for quick edits and small tasks.                                                       |
| **GPT-5.1**           | 219 credits        | 75% of Sonnet   | Advanced reasoning and context. Builds great plans and works well for medium-size tasks.                                 |
| **GPT-5.2**           | 390 credits        | 133% of Sonnet  | Enhanced reasoning capabilities. Excellent for complex tasks requiring long chains of thought.                           |

<Info>
  \*Based on a standard medium-complexity task. Actual credit consumption varies based on task complexity, context size, and response length.
</Info>

## Example tasks

To illustrate the credit differences, here are examples of tasks and how much they cost with each model.

### Sonnet task: Fix a 500 error in an API endpoint

> The `/api/users/:id` endpoint returns 500 errors when a user has no associated organization. Add null checking and return a 404 with a clear error message instead. Test that users with organizations still work correctly.

**Credit cost:** 293 credits with Sonnet 4.5

| Model          | Credits     | Savings              |
| :------------- | :---------- | :------------------- |
| **Sonnet 4.5** | 293 credits | —                    |
| **Opus 4.5**   | 488 credits | Use for harder tasks |
| **GPT-5.2**    | 390 credits | Use for harder tasks |
| **Haiku 4.5**  | 88 credits  | 205 credits saved    |
| **GPT-5.1**    | 219 credits | 74 credits saved     |

***

### Opus task: Design and implement a multi-tenant billing system

> Our B2B SaaS platform needs a multi-tenant billing system. Currently we have a simple Stripe integration for single subscriptions, but we need to support:
>
> 1. **Usage-based billing**: Track API calls per tenant with tiered pricing (first 10k calls free, then \$0.001/call)
> 2. **Seat-based licensing**: Charge per active user with volume discounts
> 3. **Hybrid plans**: Combine base subscription + usage overages
> 4. **Invoice generation**: Monthly invoices with line-item breakdown by workspace
> 5. **Billing isolation**: Each tenant's billing data must be completely isolated
>
> Design the database schema, implement the metering service, integrate with Stripe's usage-based billing API, and ensure we handle edge cases like mid-cycle plan changes, prorations, and failed payments. Consider how this will scale to 10k+ tenants.

**Credit cost:** 976 credits with Opus 4.5

## Monitoring credit usage

You can track your credit consumption in multiple places:

### In your IDE

* **VS Code**: View credit usage in the Augment panel
* **JetBrains**: Check the Augment tool window for usage stats
* **Auggie CLI**: Monitor credits used per session

### On the web

Visit [app.augmentcode.com](https://app.augmentcode.com) to access detailed dashboards that show:

* Total credits used by your team
* Credit usage per team member
* Breakdown by model and activity
* Usage trends over time
* Remaining credits in your plan

<Note>
  Team administrators can access more detailed analytics to help optimize team usage and identify opportunities to save credits by using more efficient models for appropriate tasks.
</Note>

## Understanding your usage breakdown

When you view your usage analytics, you'll see credits organized by both **model** and **activity type**. Here's what each activity type means:

### Session types

These are the main session types you can use with Augment:

| Activity        | What it is                               |
| :-------------- | :--------------------------------------- |
| **Chat**        | Conversational chat session              |
| **Agent**       | Local agent session (in your IDE)        |
| **RemoteAgent** | Cloud-based agent session (asynchronous) |
| **CliAgent**    | Command-line agent session (Auggie CLI)  |

### Optional features

| Activity            | What it is                                                                                   |
| :------------------ | :------------------------------------------------------------------------------------------- |
| **Prompt Enhancer** | Appears when you use the Prompt Enhancer feature to improve your prompts before sending them |
| **Code Review**     | Automated code review for pull requests (when enabled for your repository)                   |

### Background activities

Augment performs lightweight processing in the background to keep your experience smooth:

| Activity                | What it does                                                              |
| :---------------------- | :------------------------------------------------------------------------ |
| **Context Compression** | Summarizes conversation history to keep long sessions fast and responsive |
| **System**              | General background processing that helps Augment work smoothly            |

These background activities use a small fraction of your total credit consumption. In most workflows, they're a minor part of overall usage.

## Tips for optimizing credit usage

1. **Match the model to the task**: Use Haiku for simple tasks, GPT-5.1 for medium tasks, Sonnet for complex work, and Opus for the hardest challenges
2. **Be specific in your prompts**: Clear, detailed instructions help models work more efficiently
3. **Break down large tasks**: Sometimes splitting a complex task into smaller ones can be more credit-efficient
4. **Review usage patterns**: Check your dashboards regularly to identify optimization opportunities
5. **Set team guidelines**: Establish best practices for model selection within your team

## Frequently asked questions

<AccordionGroup>
  <Accordion title="How are credits calculated?">
    Credits are consumed based on the model used, the size of the context (code being analyzed), and the length of the response generated. More complex tasks that require analyzing more code or generating longer responses will consume more credits.
  </Accordion>

  <Accordion title="What happens if I run out of credits?">
    When you run out of credits, you'll need to upgrade your plan or wait until your credits reset at the beginning of your next billing cycle. Team administrators can purchase additional credits or upgrade the team plan at any time.
  </Accordion>

  <Accordion title="Can I switch models mid-conversation?">
    Currently, you can switch models mid-conversation in **Auggie CLI** using the `/model` command. Each message will consume credits based on the model selected for that specific message. Model switching mid-conversation is not yet available in the IDE extensions (VS Code, JetBrains), but you can change your model selection between separate conversations.
  </Accordion>
</AccordionGroup>

## Related resources

<CardGroup>
  <Card title="Available Models" icon="brain" href="/models/available-models">
    Learn about the different AI models available in Augment
  </Card>

  <Card title="Pricing Plans" icon="credit-card" href="https://augmentcode.com/pricing">
    View current pricing plans and credit allocations
  </Card>

  <Card title="Teams Admin Guide" icon="users" href="/teams/teams-admin-guide">
    Manage team subscriptions and billing
  </Card>

  <Card title="Blog: Credit-Based Plans" icon="newspaper" href="https://www.augmentcode.com/blog/our-new-credit-based-plans-are-now-live">
    Read the full announcement about credit-based pricing
  </Card>
</CardGroup>


# Quickstart
Source: https://docs.augmentcode.com/quickstart

Augment is the developer AI for teams that deeply understands your codebase and how you build software. Your code, your dependencies, and your best practices are all at your fingertips.

### 1. Install the Augment extension

<CardGroup>
  <Card href="https://marketplace.visualstudio.com/items?itemName=augment.vscode-augment">
    <img alt="Visual Studio Code" />

    <h2>
      Visual Studio Code
    </h2>

    <p>Install Augment for Visual Studio Code</p>
  </Card>

  <Card href="https://plugins.jetbrains.com/plugin/24072-augment">
    <img alt="JetBrains IDEs" />

    <h2>
      JetBrains IDEs
    </h2>

    <p>Install Augment for JetBrains IDEs, including WebStorm, PyCharm, and IntelliJ</p>
  </Card>

  <Card href="/cli/setup-auggie/install-auggie-cli">
    <img alt="Auggie CLI" />

    <h2>
      Auggie CLI
    </h2>

    <p>
      All the power of Augment's agent, context engine, and tools in your terminal.
    </p>
  </Card>
</CardGroup>

### 2. Sign-in and sync your repository

For VS Code and JetBrains IDEs, follow the prompts in the Augment panel to [sign in](/setup-augment/sign-in) and [index your workspace](/setup-augment/workspace-indexing). If you don't see the Augment panel, press <Keyboard /> or click the Augment icon in the side panel of your IDE.

For Auggie CLI, use the command `auggie login` to sign in.

### 3. Start coding with Augment

<Steps>
  <Step title="Using Agent">
    Augment agent enables you to complete tasks using natural language. Ask Agent to explain your codebase, debugging an
    issue, or writing entire functions, tests, or features. See [Using
    Agent](/using-augment/agent) for more details.
  </Step>

  <Step title="Using Next Edit">
    Augment Next Edit keeps you moving through your tasks by guiding you step-by-step through complex or repetitive changes. Jump to the next suggestion–in the same file or across your codebase–by pressing <Keyboard />. See
    [Using Next Edit](/using-augment/next-edit) for more details.
  </Step>

  <Step title="Using instructions">
    Start using an Instruction by hitting <Keyboard /> and quickly write tests, refactor code, or craft any prompt in natural language to transform your code. See [Using
    Instructions](/using-augment/instructions) for more details.
  </Step>

  <Step title="Using completions">
    Augment provides inline code suggestions as you type. To accept the full
    suggestions, press <Keyboard />, or accept the suggestion one
    word at a time with <Keyboard />. See [Using
    Completions](/using-augment/completions) for more details.
  </Step>
</Steps>

<Next>
  * [Disable other code assistants](/troubleshooting/disable-copilot)
  * [Use keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts)
  * [Configure indexing](/setup-augment/workspace-indexing)
</Next>


# Agent Integrations
Source: https://docs.augmentcode.com/setup-augment/agent-integrations

Configure integrations for Augment Agent to access external services like GitHub, Linear, Jira, Confluence, Notion, Sentry, and Stripe.

## About Agent Integrations

Augment Agent can access external services through integrations to add additional context to your requests and take actions on your behalf. These integrations allow Augment Agent to seamlessly work with your development tools without leaving your editor.

Once set up, Augment Agent will automatically use the appropriate integration based on your request context. Or, you can always mention the service in your request to use the integration.

## Setting Up Integrations

To set up integrations with Augment Agent in VS Code, follow these steps:

1. Click the settings icon in the top right of Augment's chat window or press <Keyboard /> and select <Command />
2. Click "Connect" for the integration you want to set up

<img alt="Set up integrations in the settings page" />

You'll be redirected to authorize the integration with the appropriate service. After authorization, the integration will be available for use with Augment Agent.

## Native Integrations

## <div><div><GitHubLogo /></div> GitHub Integration</div>

Add additional context to your requests and take actions. Pull in information from a GitHub Issue, make the changes to your code (or have Agent do it for you), and open a Pull Request all without leaving your editor.

### Examples

* "Implement Issue #123 and open up a pull request"
* "Find all issues assigned to me"
* "Check the CI status of my latest commit"

For authorization details, see [GitHub documentation](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps).

## <div><div><LinearLogo /></div> Linear Integration</div>

Read, update, comment on, and resolve your Linear issues within your IDE.

### Examples

* "Fix TES-1"
* "Create Linear tickets for these TODOs"
* "Help me triage these new bug reports"

For authorization details, see [Linear documentation](https://linear.app/docs/third-party-application-approvals).

## <div><div><JiraLogo /></div> Jira Integration</div>

Work on your Jira issues, create new tickets, and update existing ones.

### Examples

* "Show me all my assigned Jira tickets"
* "Create a Jira ticket for this bug"
* "Create a PR to fix SOF-123"
* "Update the status of PROJ-123 to 'In Progress'"

For authorization details, see [Jira documentation](https://support.atlassian.com/jira-software-cloud/docs/allow-oauth-access/).

## <div><div><ConfluenceLogo /></div> Confluence Integration</div>

Query existing documentation or update pages directly from your IDE. Ensure your team's knowledge base stays current without any context switching.

### Examples

* "Summarize our Confluence page on microservice architecture"
* "Find information about our release process in Confluence"
* "Update our onboarding docs to explain how we use Bazel"

For authorization details, see [Confluence documentation](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/).

## <div><div><NotionLogo /></div> Notion Integration</div>

Search and retrieve information from your team's knowledge base - access documentation, meeting notes, and project specifications. This integration is currently READ-ONLY.

### Examples

* "Find Notion pages about our API documentation"
* "Show me the technical specs for the payment system"
* "What outstanding tasks are left from yesterday's team meeting?"

For authorization details, see [Notion documentation](https://www.notion.so/help/add-and-manage-connections-with-the-api#install-from-a-developer).

## <div><div><GleanLogo /></div> Glean Integration</div>

> **Note:** The Glean integration is in early access and thus is a little different from other integrations.
>
> * It is currently only available to enterprise customers.
> * It does not appear in the list of integrations in the settings panel.

The Glean integration lets the agent retrieve information from your team's internal data sources leveraging Glean's powerful search engine.

**To Enable the Glean Integration:** You'll need to be have administrator access to Augment and Glean. Follow the instructions on [https://app.augmentcode.com/gleanConfig](https://app.augmentcode.com/gleanConfig) and your agent will be ready to use Glean!

### Examples

* "Search Glean for past related incidents and how they were resolved"
* "Search Glean for why we're migrating to a new payment processor"

## Enhanced Native Integrations

> **New:** Enhanced native integrations for Sentry and Stripe launched on July 30, 2025, providing deeper, more seamless access to your error tracking and payment data.

### <div><div><SentryLogo /></div> Sentry Integration</div>

Search issues, errors, traces, logs, and releases. Create RCAs and AI-Generated fixes with Seer integration for comprehensive error tracking and resolution.

#### Examples

* "Diagnose the top unresolved crashes in my React Native app and propose fixes"
* "Show me all errors from the latest release and their impact"
* "Create a root cause analysis for the payment processing errors"
* "Find similar issues that were resolved and suggest fixes"

### <div><div><StripeLogo /></div> Stripe Integration</div>

Real-time payment events, refund status, subscription metrics, and secure tokenization. Available via both remote and local MCP servers with OAuth MCP support in public preview.

#### Examples

* "Create a dashboard showing failed payment intents in the last 24 hours and suggest retry logic"
* "Analyze subscription churn patterns and recommend retention strategies"
* "Show me all refunds processed this week and their reasons"
* "Generate a report on payment method performance"

## Next Steps

* [Configure additional tools with Easy MCP or advanced MCP setup](/setup-augment/mcp)
* Explore one-click integrations for CircleCI, MongoDB, and Redis through Easy MCP


# Rules & Guidelines for Agent and Chat
Source: https://docs.augmentcode.com/setup-augment/guidelines

You can provide custom rules and guidelines written in natural language to improve Agent and Chat with your preferences, best practices, styles, and technology stack.

## What are Rules & Guidelines?

Agent and Chat rules and guidelines are natural language instructions that can help Augment reply with more accurate and relevant responses. Rules and guidelines are perfect for telling Augment to take into consideration specific preferences, package versions, styles, and other implementation details that can’t be managed with a linter or compiler. You can create guidelines for a specific workspace or globally for all chats in your IDE; guidelines do not currently apply to Completions, Instructions, or Next Edit.

User Guidelines are defined under Settings and stored within your IDE to be used to guide preferences inside of the Agent and Chat. Workspace Guidelines and Rules are stored directly in your repository.

## Working with User Guidelines

<Info>
  User Guidelines are stored locally in your IDE and will be applied to all future chats in that IDE. Guidelines defined in VSCode will not propagate to JetBrains IDEs and vice versa.
</Info>

<img alt="Adding user guidelines" />

You can add user guidelines by clicking Context menu (@), starting an @-mention inside Chat, or clicking Settings > Rules and User Guidelines.

### Navigating from the Context menu (@) User Guidelines

1. @ mention and select `User Guidelines`
2. Enter your guidelines (see below for tips)
3. Press Escape to save or wait for autosave

### Navigating from Settings > User Guidelines and Rules

<img alt="Open rules and guidelines" />

1. In the top right corner, select the hamburger menu (⋯)
2. Select Settings
3. From the left menu in Augment Settings, select User Guidelines and Rules

## Working with Rules

You can craft Rules to guide Augment towards specific documentation, frameworks, workflows or workstyles.

Rules are files that live in the `.augment/rules` directory. Currently, we support 3 types of rules:

* **Always**: contents will be included in every user prompt
* **Manual**: needs to be tagged through @ attaching the Rules file manually
* **Auto**: Agent will automatically detect and attach rules based on a description field

### User Rules vs Workspace Rules

Rules can be defined at two levels:

| Scope     | Location                           | Availability                        |
| :-------- | :--------------------------------- | :---------------------------------- |
| User      | `~/.augment/rules/`                | Available in all workspaces         |
| Workspace | `<workspace_root>/.augment/rules/` | Available in current workspace only |

**User rules** are stored in your home directory and apply to all projects. Use these for personal preferences, coding style guidelines, or conventions you want to follow across all your work. User rules are always treated as **Always** type and are automatically included in every prompt regardless of any frontmatter configuration.

**Workspace rules** are stored in the project repository and apply only to that specific project. Use these for project-specific guidelines that should be shared with your team via version control. Workspace rules support all three types (Always, Manual, Auto) via frontmatter configuration.

### Hierarchical Rules

In addition to workspace-level rules, Augment supports **hierarchical rules** through `AGENTS.md` and `CLAUDE.md` files placed in subdirectories. When working on files in a subdirectory, Augment automatically discovers and applies rule files from that directory and all parent directories.

**How it works:**

1. When you work on a file, Augment looks for `AGENTS.md` and `CLAUDE.md` in the file's directory
2. It walks up the directory tree, checking each parent directory for these files
3. All discovered rules are included in the context for that work session
4. The search stops at the workspace root (workspace root rules are loaded separately)

**Example:**

```
my-project/
  AGENTS.md                  <- Always included (workspace root)
  src/
    AGENTS.md                <- Included when working in src/ or subdirs
    components/
      AGENTS.md              <- Included when working in src/components/
      Button.tsx
```

When working on `src/components/Button.tsx`, all three `AGENTS.md` files are loaded.

**Use cases:**

* Framework-specific guidelines (React rules in frontend/, Node.js rules in backend/)
* Module-specific conventions (API design patterns in api/)
* Team boundaries (different teams maintain their own standards)

<Note>Only `AGENTS.md` and `CLAUDE.md` files are discovered hierarchically. Files in `.augment/rules/` are only loaded from the workspace root.</Note>

### Importing Rules

**Augment** will automatically import rules if they are detected in the current workspace. Augment will look for markdown files, e.g., files ending with `*.md` or `*.mdx`. You can also manually import rules inside of Settings > Import rules.

<img alt="Import rules" />

### Importing Augment Memories into Rules or User Guidelines

Augment Memories are automatically created by the Agent. If you’ve ever modified the Memories or prompted the Agent to remember something you can import these preferences as Rules or User Guidelines.

1. From the prompt box, click on Augment Memories
2. Select the item you'd like to import and then click User Guidelines at the top of Augment Memories from inside the editor.
3. To add the memory as a Rule, you'll first need to add at least one rule using +Create new rule file. Now, you can select any information inside the Augment Memories and save it as a Rule.

<img alt="Move memories" />

## Working with Workspace Guidelines `.augment-guidelines` (legacy)

You can add an `.augment-guidelines` file to the root of a repository to specify a set of guidelines that Augment will follow for all Agent and Chat sessions on the codebase. The `.augment-guidelines` file should be added to your version control system so that everyone working on the codebase has the same guidelines.

### Tips for good rules and guidelines

* Provide guidelines as a list
* Use simple, clear, and concise language for your guidelines
* Asking for shorter or code-only answers may hurt response quality

### Examples

<AccordionGroup>
  <Accordion title="User Guideline Examples">
    * Ask for additional explanation e.g. `For Typescript code, explain what the code is doing in more detail`

    * Set a preferred language e.g. `Respond to questions in Spanish`
  </Accordion>

  <Accordion title="Rule Examples">
    * Add links to Google Docs, Notion or Confluence files that define goals, product requirements, or project objectives

    * Point to specific documentation e.g. `Python 3.13.5` for the dependencies inside your project

    * Outline templates or example code commonly used in your project

    * Establish consistent frameworks, coding styles, and architectural patterns across your codebase

    * Provide examples on codebase style. For example:
      * Information that ONLY applies to the specific files, functions, or code snippets
      * Vague or obvious preferences that aren't actionable
      * General statements about good programming practices that any user would want
  </Accordion>

  <Accordion title="Workspace Guideline Examples">
    * Identifying preferred libraries e.g. `pytest vs unittest`
    * Identifying specific patterns e.g. `For NextJS, use the App Router and server components`
    * Rejecting specific anti-patterns e.g. `a deprecated internal module`
    * Defining naming conventions e.g. `functions start with verbs`
  </Accordion>
</AccordionGroup>

## FAQs

<AccordionGroup>
  <Accordion title="How are Rules different from Guidelines?">
    Guidelines and Rules differ in how they are stored and their scope of influence.

    * **User Guidelines** are stored in the user’s local IDE storage that will persist across Chat & Agent sessions; however, they do not persist across workspaces.
    * **User Rules** are stored in `~/.augment/rules/` and apply to all workspaces. They are always treated as "Always" type and automatically included in every prompt.
    * **Workspace Rules** are stored within the repository under the `.augment/rules` root that will allow you to split up previous Guidelines into multiple files to more precisely define your preferences. Workspace rules support all three types (Always, Manual, Auto).
    * **Workspace Guidelines** (legacy) stored within the repository under the `.augment-guidelines` file are a legacy set of rules that can be edited by editing the `.augment-guidelines` in your repository. Augment will automatically import Workspace Guidelines as Rules which you can access under Settings > User Guidelines and Rules.
  </Accordion>

  <Accordion title="What are the current limitations?">
    * User Guidelines are currently limited to a maximum of 24,576 characters.
    * Workspace Guidelines + Rules are limited to a maximum of 49,512 characters. If we exceed these limits, the user will be notified in app and be applied in order of (manual rules, always + auto rules, .augment-guidelines)
    * For VSCode, Guidelines are available in plugin version 0.492.0 and above
    * For JetBrains IDEs, Rules are available in plugin version 0.249.1 and above
  </Accordion>
</AccordionGroup>

## See Also

* [Custom Rules and Guidelines (CLI)](/cli/rules) - Configure rules for Auggie CLI
* [Workspace Context](/setup-augment/workspace-context-vscode) - Understanding workspace configuration in VSCode
* [Chat Context](/using-augment/chat-context) - Learn about context in Chat


# Install Augment for Slack
Source: https://docs.augmentcode.com/setup-augment/install-slack-app

Ask Augment questions about your codebase right in Slack.

<Note>
  The Augment GitHub App is compatible with GitHub.com and GitHub Enterprise Cloud. GitHub Enterprise Server is not currently supported.
</Note>

## About Augment for Slack

Augment for Slack brings the power of Augment Chat to your team's Slack workspace. Mention <Command /> in any channel or start a DM with Augment to have deep codebase-aware conversations with your team.

*To protect your confidential information, Augment will not include repository context in responses when used in shared channels with external members.*

## Installing Augment for Slack

### 1. Install GitHub App

<CardGroup>
  <Card title="Install Augment GitHub App" href="https://github.com/apps/augmentcode/installations/new" icon={<GitHubLogo />}>
    GitHub App for Augment Chat in Slack
  </Card>
</CardGroup>

To enable Augment's rich codebase-awareness, install the Augment GitHub App and grant access to your desired repositories. Organization owners and repository admins can install the app directly; others will need owner approval. See [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) for details.

We recommend authorizing only the few active repositories you want accessible to Augment Slack users. You can modify repository access anytime in the GitHub App settings.

<img alt="Installing the GitHub app on a single repository" />

### 2. Install Slack App

<CardGroup>
  <Card title="Install Augment for Slack" href="https://slack.com/oauth/v2/authorize?client_id=3751018318864.7878669571030&scope=app_mentions:read,channels:history,channels:read,chat:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,mpim:read,mpim:write,reactions:read,reactions:write,users.profile:read,users:read,users:read.email,groups:write,commands,assistant:write&user_scope=identity.basic" icon={<SlackLogo />}>
    Slack App for Augment Code
  </Card>
</CardGroup>

Once you have the GitHub App installed, install the Augment Slack App. You'll need an Augment account and correct permissions to install Slack apps for your workspace.

Any workspace member can use the Slack app once installed. Contact us if you need to restrict access to specific channels or users.

### 3. Add Augment to the Slack Navigation Bar

Make Augment easily accessible by adding it to Slack's assistant-view navigation bar:

1. Click your profile picture → **Preferences** → **Navigation**
2. Under **App agents & assistants**, select **Augment**

*Note: Each user can customize this setting in their preferences.*

<Next>
  [Using Augment for Slack](/using-augment/slack)
</Next>


# Install Augment for Visual Studio Code
Source: https://docs.augmentcode.com/setup-augment/install-visual-studio-code

Augment in Visual Studio Code gives you powerful code completions, transformations, and chat capabilities integrated into your favorite code editor.

<CardGroup>
  <Card title="Get the Augment Extension" href="https://marketplace.visualstudio.com/items?itemName=augment.vscode-augment" icon={<VscodeLogo />}>
    Install Augment for Visual Studio Code
  </Card>
</CardGroup>

## About Installation

Installing <ExternalLink href="https://marketplace.visualstudio.com/items?itemName=augment.vscode-augment" /> is easy and will take you less than a minute. You can install the extension directly from the Visual Studio Code Marketplace or follow the instructions below.

<img alt="Augment extension in Visual Studio Code Marketplace" />

## Installing Augment for Visual Studio Code

<Steps>
  <Step title="Make sure you have the latest version of Visual Studio Code installed">
    You can download the latest version of Visual Studio Code from the <ExternalLink href="https://code.visualstudio.com/" />. If you already have Visual Studio Code installed, you can update to the latest version by going to <Command />.
  </Step>

  <Step title="Open the Extensions panel in Visual Studio Code">
    Click the Extensions icon in the sidebar to show
    the Extensions panel.
  </Step>

  <Step title="Search for Augment in the marketplace">
    Using the search bar in the Extensions panel, search for
    <Command />.
  </Step>

  <Step title="Install the extension">
    Click <Command /> to install the extension.
  </Step>

  <Step title="Sign into Augment and get coding">
    Sign in to by clicking <Command /> in the Augment
    panel. If you do not see the Augment panel, use the shortcut
    <Keyboard /> or click the Augment icon
    <img /> in the side bar of your IDE. See more details in [Sign
    In](/setup-augment/sign-in).
  </Step>
</Steps>

## About pre-release versions

We regularly publish pre-release versions of the Augment extension. To use the pre-release version, go to the Augment extension in the Extensions panel and click <Command /> and then <Command />.

Pre-release versions may sometimes contain bugs or otherwise be unstable. As with the released version, please report any problems by sending us [feedback](/troubleshooting/feedback).


# Setup Model Context Protocol servers
Source: https://docs.augmentcode.com/setup-augment/mcp

Use Model Context Protocol (MCP) servers with Augment to expand Augment's capabilities with external tools and data sources.

## About Model Context Protocol servers

Augment Agent can utilize external integrations through Model Context Protocol (MCP) to access external systems for information and integrate tools to take actions. MCP is an open protocol that provides a standardized way to connect AI models to different data sources and tools. MCP servers can be used to access local or remote databases, run automated browser testing, send messages to Slack, or even play music on Spotify.

## Easy MCP: One-Click Integrations

> **New:** Easy MCP launched on July 30, 2025, making it easier than ever to connect popular developer tools to Augment Code.

Easy MCP is a new feature in the Augment Code extension that transforms complex MCP server setup into a single click. Instead of manually configuring servers, hunting for GitHub repos, or editing JSON files, you can now connect popular developer tools with just an API token or OAuth approval.

### Available Easy MCP Integrations

Easy MCP provides one-click access to these popular developer tools:

#### CircleCI

* **Context:** Build logs, test insights, flaky-test detection
* **Sample prompt:** "Find the latest failed pipeline on my branch and surface the failing tests."
* **Setup:** Click "+", paste your CircleCI API token, and you're connected.

#### MongoDB

* **Context:** Data exploration, database management, and context-aware code generation
* **Sample prompt:** "Analyze my user collection schema and suggest optimizations for our new search feature."
* **Setup:** One-click OAuth connection to your MongoDB instance.

#### Redis

* **Context:** Keyspace introspection, TTL audits, and migration helpers
* **Sample prompt:** "Generate a migration script to move expiring session keys to the new namespace."
* **Setup:** Connect with your Redis credentials in seconds.

### Getting Started with Easy MCP

1. Open the Augment Code extension in VS Code
2. Navigate to the Easy MCP pane in the settings
3. Click the "+" button next to your desired integration
4. Paste an API token or approve OAuth
5. Start using the integration immediately in your Agent conversations

<img />

From that moment on, Augment Code streams your tool's live context into every suggestion and autonomous Agent run.

## Advanced MCP Configuration

For developers who need custom MCP server configurations or want to use servers not available through Easy MCP, you can still configure MCP servers manually.

There are three ways to configure MCP servers in Augment:

1. **Easy MCP** (recommended) - One-click integrations for popular tools
2. **Augment Settings Panel** - Manual configuration with a GUI
3. **Import from JSON** - Paste a JSON config to quickly add servers

MCP servers configured through the Settings Panel or Import from JSON are managed in the same place. After importing, you can edit or remove servers in the Settings Panel.

## Configure in the Augment Settings Panel

The easiest way to configure MCP servers is to use the Augment Settings Panel.
To access the settings panel, open the options menu in the upper right of the Augment panel and click the Settings option. Once the settings panel is open, you will see a section for MCP servers.

<img />

Fill in the `name` and `command` fields. The `name` field must be a unique name for the server. The `command` field is the command to run the server. Environment variables have their own section and no longer need to be specified in the command.

<img />

To add additional servers, click the `+` button next to the `MCP` header.
To edit a configuration, or to delete a server, click the `...` button next to the server name.

### Add a Remote MCP server

If your MCP server runs remotely (for example, a hosted service), click the "+ Add remote MCP" button in the MCP section. Remote MCP connections support both HTTP and SSE (Server‑Sent Events).

<img />

* Connection Type: choose HTTP or SSE
* Name: a unique display name for the server
* URL: the base URL to your MCP server (e.g., [https://api.example.com](https://api.example.com))

Remote MCP servers appear alongside your local MCP servers in the list. You can edit or remove them using the "..." menu next to the server name.

## Import from JSON

You can quickly add MCP servers by importing a JSON configuration from the Augment Settings Panel:

1. Open the Settings Panel (gear icon in the Augment panel)
2. In the MCP section, click <strong>Import from JSON</strong>
3. Paste a configuration like the following and click Save

<img />

**Example: Local command (Context7 via npx)**

```json theme={null}
{
  "mcpServers": {
    "Context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

**Example: Remote SSE endpoint**

```json theme={null}
{
  "mcpServers": {
    "test": {
      "url": "http://localhost:3001/sse",
      "type": "sse"
    }
  }
}
```

After importing, servers appear in the list where you can edit, test, or remove them. Ensure any required dependencies for the server are installed on your machine.

## Server compatibility

Not all MCP servers are compatible with Augment's models. The MCP standard, implementation of specific servers, and Augment's MCP support are frequently being updated, so check compatibility frequently.


# Sign in and out
Source: https://docs.augmentcode.com/setup-augment/sign-in

After you have installed the Augment extension, you will need to sign in to your account.

## About Authentication

You can sign in to Augment using one of the supported identity providers–Google or Microsoft–or sign in using your email address and a single-use code we send to you. During the process, you will be redirected to your browser to sign in to your account.

## Sign in

<Steps>
  <Step title="Sign in to Augment">
    Click the <Command /> button in the Augment panel. If you do not see the Augment panel press <Keyboard />. If you are using Visual Studio Code, you be asked to confirm going to Augment's authentication portal.
  </Step>

  <Step title="Sign in with your email">
    In your browser, you may sign in with Google, Microsoft, or by receiving a single-use code in your email.
  </Step>

  <Step title="Accept the terms and conditions">
    If this is the first time you've signed in to Augment, you will be asked to accept the terms and conditions.
  </Step>

  <Step title="Return to your IDE">
    You will be automically redirected back to your IDE and you will see the Augment icon
    change to
    <img /> in the status bar.
  </Step>

  <Step title="Sync your workspace">
    If this is your first time using Augment, or you are working on a new workspace, you will see the <Command /> in the Augment panel. Click the <Command /> button in the Augment panel to enable Augment's rich codebase awareness. See [Syncing your workspace](/setup-augment/workspace-indexing) to customize syncing behavior and learn more.
  </Step>
</Steps>

## Sign out

<Steps>
  <Step title="Show the Augment command menu">
    Press <Keyboard /> to show the Augment command menu.
  </Step>

  <Step title="Click Sign Out">Click <Command /> from the bottom of the commands menu.</Step>

  <Step title="You are now signed out of Augment">
    You will see the status bar icon change to orange and you will be signed out of Augment in all of your active workspaces.
  </Step>
</Steps>


# Allow Augment traffic from static IPs
Source: https://docs.augmentcode.com/setup-augment/static-ip-support

Locate Augment static IP addresses and configure firewalls, allowlists, and network policies for Augment Agent and its integrations.

Augment routes all outbound integration and remote-agent traffic through region specific static IP addresses. Add these IPs to your firewalls and allowlists when you need predictable source addresses for compliance or access control.

## When static IP support helps

**You likely need static IPs when**

* Your GitHub organization enforces IP allowlists.
* Internal APIs, artifact registries, or databases sit behind IP restricted networks.
* Corporate firewalls require a known source IP before allowing outbound agent traffic.
* You are connecting Augment remote agents to private cloud or on-prem systems.
* Compliance policies mandate tracking specific egress addresses.

**You probably do not need static IPs when**

* Integrated services such as GitHub, Linear, Slack, and others are accessible without IP restrictions.
* You only use Augment with SaaS tools that do not enforce IP allowlists.
* Your network does not block traffic based on source IP.

## Get the IP addresses for your region

<Callout type="info">
  Always perform the lookup from a network that mirrors the environment enforcing the allowlist so you can detect DNS filtering or caching differences.
</Callout>

### US region

```bash theme={null}
dig +short us-static.augmentcode.com
```

### EU region

```bash theme={null}
dig +short eu-static.augmentcode.com
```

The DNS record returns the exact set of IP addresses Augment uses for outbound traffic in that region. Addresses are stable, and repeated lookups should return the same list. Rerun the lookup periodically or set up monitoring so you are alerted if Augment adds new addresses.

## Add the IPs to common services

### GitHub Enterprise with IP restrictions

1. Run the lookup for your region.
2. In GitHub, open **Settings** -> **Security** -> **IP allow list**.
3. Add each Augment IP address with a clear description such as `Augment Agent`.

### Private artifact registries

Add the IP addresses to the allowlist for the registry host. For example, with a private npm registry include the addresses in the service configuration before agents pull packages.

### Corporate firewalls

1. Allow inbound traffic to your services from the Augment IP addresses.
2. Note the rules in your change management system for auditing.
3. Monitor firewall logs for denied connections from Augment IPs.

### API gateways

```yaml theme={null}
apiVersion: networking.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-augment
spec:
  rules:
  - from:
    - source:
        ipBlocks:
        - "203.0.113.10/32"  # Replace with the Augment IPs you looked up
        - "203.0.113.11/32"
```

### Databases with IP allowlists

```sql theme={null}
-- PostgreSQL pg_hba.conf example
host    all    augment_user    203.0.113.10/32    md5
host    all    augment_user    203.0.113.11/32    md5
```

## Implementation checklist

* Use the DNS entry for the region where your Augment deployment runs (`us-static` or `eu-static`).
* Document which services rely on Augment IPs and who owns the configuration.
* Limit access to only the systems Augment needs, following least privilege.
* Review and confirm allowlist entries during regular security audits.
* Configure alerts for DNS changes or repeated blocked traffic from Augment IPs.

## Troubleshooting

**If integrations stop working**

1. Rerun `dig +short <region>-static.augmentcode.com` and confirm the addresses match your allowlists.
2. Review firewall or service logs for blocked requests from Augment IPs.
3. Update the allowlist if any addresses changed or were missed.

**If DNS queries fail**

```bash theme={null}
nslookup us-static.augmentcode.com
dig us-static.augmentcode.com A
dig us-static.augmentcode.com +noall +answer
```

Ensure local DNS resolvers can reach the Augment records and that caching layers are not serving stale results.

## Need help?

Contact Augment Support with your region, the affected integrations, and relevant firewall or allowlist details so the team can help you validate the configuration.


# Secrets Manager
Source: https://docs.augmentcode.com/setup-augment/user-secrets

Securely store and manage secrets for your development environment, including API keys, tokens, and credentials.

<Availability />

The Secrets Manager allows you to securely store and manage user-defined secrets that can be used in your development environment. It supports two types of secrets: **Environment Variables** and **Mounted Files**.

## Overview

The Secrets Manager provides a secure way to store sensitive information like API keys, database credentials, and configuration secrets. All secrets are encrypted and stored securely, with automatic redaction in logs to prevent accidental exposure.

## Accessing the Secrets Manager

Open the Settings Panel (gear icon in the Augment panel) and navigate to the **Secrets** section to manage your secrets.

## Secret Types

### Environment Variables

Environment variables are injected into your development environment and accessible via standard environment variable access patterns.

**Use cases:**

* API keys (GitHub tokens, OpenAI keys)
* Database connection strings
* Service endpoints
* Configuration flags

**How they work:**

* Secrets are made available as environment variables in your workspace
* Generated profile script at `/etc/profile.d/15-augment-secrets.sh`
* Automatically loaded in shell sessions

### Mounted Files

Mounted files are stored as actual files in your workspace filesystem at specified paths.

**Use cases:**

* SSH private keys
* Certificate files
* Configuration files
* Large secret content

**How they work:**

* Files are mounted to `/run/augment_secrets/` by default
* You specify the mount path when creating the secret
* Files are accessible via standard filesystem operations

## Security Features

* Secret values are never displayed by default
* All secret values are redacted in logs
* Each user can only access their own secrets

## Limits and Quotas

| Limit                | Default Value  |
| -------------------- | -------------- |
| Max secrets per user | 100            |
| Max secret size      | 4KB            |
| Max name length      | 255 characters |
| Max tags per secret  | 50             |

## Security Best Practices

1. **Use descriptive names**: Make secret purposes clear without exposing sensitive info
2. **Regular cleanup**: Remove unused secrets to minimize exposure
3. **Avoid logging values**: The system automatically redacts secrets in logs
4. **Use appropriate type**: Choose environment variables for simple values, mounted files for complex content


# Keyboard Shortcuts for Visual Studio Code
Source: https://docs.augmentcode.com/setup-augment/vscode-keyboard-shortcuts

Augment integrates with your IDE to provide keyboard shortcuts for common actions. Use these shortcuts to quickly accept suggestions, write code, and navigate your codebase.

## About keyboard shortcuts

Augment is deeply integrated into your IDE and utilizes many of the standard keyboard shortcuts you are already familiar with. These shortcuts allow you to quickly accept suggestions, write code, and navigate your codebase. We also suggest updating a few keyboard shortcuts to make working with code suggestions even easier.

<Tabs>
  <Tab title="MacOS">
    To update keyboard shortcuts, use one of the following:

    | Method          | Action                               |   |
    | :-------------- | :----------------------------------- | - |
    | Keyboard        | <Keyboard /> then <Keyboard />       |   |
    | Menu bar        | <Command />                          |   |
    | Command palette | <Keyboard /> then search <Command /> |   |

    ## General

    | Action                | Recommended shortcut |
    | :-------------------- | :------------------- |
    | Open Augment panel    | <Keyboard />         |
    | Show Augment commands | <Keyboard />         |

    ## Chat

    | Action                   | Default shortcut |
    | :----------------------- | :--------------- |
    | Focus or open Chat panel | <Keyboard />     |

    ## Next Edit

    | Action            | Default shortcut |
    | :---------------- | :--------------- |
    | Go to next        | <Keyboard />     |
    | Go to previous    | <Keyboard />     |
    | Accept suggestion | <Keyboard />     |
    | Reject suggestion | <Keyboard />     |

    ## Instructions

    | Action            | Default shortcut |
    | :---------------- | :--------------- |
    | Start instruction | <Keyboard />     |
    | Accept            | <Keyboard />     |
    | Reject            | <Keyboard />     |

    ## Completions

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard />                           |
    | Accept next word of suggestion | <Keyboard />                           |
    | Accept next line of suggestion | None (see below)                       |
    | Reject suggestion              | <Keyboard />                           |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | <Keyboard />                           |

    **Recommended shortcuts**

    We recommend updating your keybindings to include the following shortcuts to
    make working with code suggestions even easier. These changes update the
    default behavior of Visual Studio Code.

    | Action                         | Recommended shortcut |
    | :----------------------------- | :------------------- |
    | Accept next line of suggestion | <Keyboard />         |
  </Tab>

  <Tab title="Windows/Linux">
    To update keyboard shortcuts, use one of the following:

    | Method          | Action                               |
    | :-------------- | :----------------------------------- |
    | Keyboard        | <Keyboard /> then <Keyboard />       |
    | Menu bar        | <Command />                          |
    | Command palette | <Keyboard /> then search <Command /> |

    ## General

    | Action                | Recommended shortcut |
    | :-------------------- | :------------------- |
    | Open Augment panel    | <Keyboard />         |
    | Show Augment commands | <Keyboard />         |

    ## Chat

    | Action                   | Default shortcut |
    | :----------------------- | :--------------- |
    | Focus or open Chat panel | <Keyboard />     |

    ## Next Edit

    | Action            | Default shortcut |
    | :---------------- | :--------------- |
    | Go to next        | <Keyboard />     |
    | Go to previous    | <Keyboard />     |
    | Accept suggestion | <Keyboard />     |
    | Reject suggestion | <Keyboard />     |

    ## Instructions

    | Action            | Default shortcut |
    | :---------------- | :--------------- |
    | Start instruction | <Keyboard />     |
    | Accept            | <Keyboard />     |
    | Reject            | <Keyboard />     |

    ## Completions

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard />                           |
    | Accept next word of suggestion | <Keyboard />                           |
    | Accept next line of suggestion | None (see below)                       |
    | Reject suggestion              | <Keyboard />                           |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | <Keyboard />                           |

    **Recommended shortcuts**

    We recommend updating your keybindings to include the following shortcuts to
    make working with code suggestions even easier. These changes update default
    behavior of Visual Studio Code.

    | Action                         | Recommended shortcut |
    | :----------------------------- | :------------------- |
    | Accept next line of suggestion | <Keyboard />         |
  </Tab>
</Tabs>


# Add context to your workspace
Source: https://docs.augmentcode.com/setup-augment/workspace-context-vscode

You can add additional context to your workspace–such as additional repositories and folders–to give Augment a full view of your system.

<Availability />

## About Workspace Context

Augment is powered by its deep understanding of your code. Sometimes important parts of your system exist outside of the current workspace you have open in your IDE. For example, you may have seperate frontend and backend repositories or have many services across multiple repositories. Adding additional context to your workspace will improve the code suggestions and chat responses from Augment.

## View Workspace Context

To view your Workspace Context, click the folder icon <Icon icon="folder-open" /> in the top right corner of the Augment sidebar panel.

<img alt="Workspace Context" />

## Add context to your workspace

To add context to your workspace, click <Command /> at the bottom of the Source Folders section of the context manager. From the file browser select the folders you want to add to your workspace context and click <Command />.

## View sync status

When viewing Workspace Context, each file and folder will have an icon that indicates whether its sync status. The following icons indicate the sync status of each file in your workspace:

| Indicator | Status                                  |
| :-------: | :-------------------------------------- |
|  <img />  | Synced, or sync in progress             |
|  <img />  | Not synced                              |
|  <img />  | Some files within the folder are synced |


# Index your workspace
Source: https://docs.augmentcode.com/setup-augment/workspace-indexing

When your workspace is indexed, Augment can provide tailored code suggestions and answers based on your unique codebase, best practices, coding patterns, and preferences. You can always control what files are indexed.

## About indexing your workspace

When you open a workspace with Augment enabled, your codebase will be automatically uploaded to Augment's secure cloud. You can control what files get indexed using `.gitignore` and `.augmentignore` files. Indexing usually takes less than a minute but can take longer depending on the size of your codebase. In Visual Studio Code, you can use Workspace Context to [view what files are indexed](/setup-augment/workspace-context-vscode#view-index-status-in-visual-studio-code) and [add additional context](/setup-augment/workspace-context-vscode#add-context-to-your-workspace).

## Security and privacy

Augment stores your code securely and privately to enable our powerful context engine. We ensure code privacy through a proof-of-possession API and maintain strict internal data minimization principles. [Read more about our security](https://www.augmentcode.com/security).

## What gets indexed

Augment will index all the files in your workspace, except for the files that match patterns in your `.gitignore` file and the `.augmentignore` file. You can [view what files are indexed](/setup-augment/workspace-context-vscode#view-sync-status-in-visual-studio-code) in Workspace Context.

## Ignoring files with .augmentignore

The `.augmentignore` file is a list of file patterns that Augment will ignore when indexing your workspace. Create an `.augmentignore` file in the root of your workspace. You can use any glob pattern that is supported by the [gitignore](https://git-scm.com/docs/gitignore) file.

## Including files that are .gitignored

If you have a file or directory in your `.gitignore` that you want to indexed, you can add it to your `.augmentignore` file using the `!` prefix.

For example, you may want your `node_modules` indexed to provide Augment with context about the dependencies in their project, but it is typically included in their `.gitignore`. Add `!node_modules` to your `.augmentignore` file.

<CodeGroup>
  ```bash .augmentignore theme={null}
  # Include .gitignore excluded files with ! prefix
  !node_modules

  # Exclude other files with .gitignore syntax
  data/test.json
  ```

  ```bash .gitignore theme={null}
  # Exclude dependencies
  node_modules

  # Exclude secrets
  .env

  # Exclude build artifacts
  out
  build
  ```
</CodeGroup>


# Using Teams
Source: https://docs.augmentcode.com/teams/teams-admin-guide

Use Teams to collect individual Augment Code accounts (Indie, Standard, or Max plans) into a Team. Once established you can bundle billing for your organization.

## About Teams

If multiple people from your organization use Augment Code through our [Indie, Standard or Max plan](https://augmentcode.com/pricing), Teams gathers accounts together for better collaboration. Teams simplify account management, offer better access control and centralize billing. Team administrators have special privileges to invite members, manage seats, change plans, and control team settings. Teams are not available for Enterprise plans since this plan by defaults groups the entire organization.

<Note>
  Team settings and billing management are only accessible to accounts assigned as the administrator. Individual team members can view team information but cannot modify settings or manage subscriptions. To change which account is set as the administrator, contact [Augment Code Support](https://portal.usepylon.com/augment-code/forms/augment-support)
</Note>

## Team Roles and Permissions

### Administrator Role

* Can invite new team members or cancel pending invitations
* Can remove team members
* Can manage team seats (increase/decrease)
* Can change team plans
* Can view and manage billing information

### Member Role

* Can view team information
* Can leave the team (remove themselves)
* Cannot invite or remove other members
* Cannot manage billing or change plans

## Adding Team Members

To add team members, you must be an administrator with available seats on your plan.

1. **Navigate to Team from Account** - Go to your [Account](https://app.augmentcode.com/account/), and then select the "Team" tab

2. **Initiate Invitation** - Click "Add team member," enter the email address, and click "Send invitation"

3. **Invitation Status** - The invitation appears as "Pending" in your team members list and counts toward your seat allocation

4. **Acceptance** - The invitee receives an email with instructions to join. Once they authenticate with their Augment account (or create one), they become an active team member

<Note>
  Invitations expire after 7 days. Pending invitations can be cancelled before acceptance. If your team is at capacity, add more seats before inviting new members. You can send multiple invitations simultaneously using comma-separated emails.
</Note>

## Removing Team Members

To remove team members, you must be an administrator. Members can also remove themselves from a team.

1. **Navigate to Team from Account** - Go to your [Account](https://app.augmentcode.com/account/), select the "Team" tab, and find the member you want to remove

2. **Remove Member** - Click the three-dot menu (⋮) next to the member's name, select "Remove Member," and confirm the removal

3. **After Removal** - The member immediately loses access to team resources and their account reverts to individual status. For paid plans, the seat becomes available at the next billing cycle.

<Note>
  Leaving? [Ask Augment Code Support](https://support.augmentcode.com/) to grant administrator access to another account before removing yourself if you're the only administrator.
</Note>

### Cancelling Pending Invitations

To cancel a pending invitation, navigate to the team members list, filter by "Pending" status, click the three-dot menu next to the pending invitation, and select "Cancel Invitation."

## Managing Team Plans and Subscriptions

Augment offers flexible plans to meet your team's needs. Visit [augmentcode.com/pricing](https://augmentcode.com/pricing) for current plan options and pricing.

### Changing Plans

To change your team's plan, you must be a team administrator with a valid payment method for paid plans.

1. **Access Plan Selection** - Go to [Account](https://app.augmentcode.com/account/) then select Subscription and click "Change Plan" or "Upgrade"

2. **Select New Plan** - Review available plans, pricing, and included features for your team size

3. **Configure Details** - Set the number of seats needed and review pricing calculations

4. **Confirm** - Add or update your payment method if needed, review prorated charges or credits, and confirm the plan change

<Note>
  Plan changes may be immediate (upgrades, free to paid, trial to paid) or take effect at the end of your billing cycle (downgrades). Prorated charges and credits are calculated automatically for mid-cycle changes.
</Note>

### Managing Seats

**Adding Seats**

1. **Navigate to Team Settings** - Go to [Account](https://app.augmentcode.com/account/) then the Team tab and click "Manage Seats"

2. **Increase Seat Count** - Use the number control to increase seats and review the new monthly cost

3. **Save Changes** - Click "Save changes" to confirm. Additional seats are billed immediately (prorated) and the new monthly rate takes effect immediately

**Removing Seats**

1. **Check Current Usage** - Ensure you have unused seats. You cannot reduce seats below your active members plus pending invitations

2. **Decrease Seat Count** - Navigate to "Manage Seats," reduce the number using the control, and save changes

3. **Billing Impact** - Removed seats remain active until the next billing cycle. Credits are applied at the next billing period

## Troubleshooting

**Cannot add members - no seats available**

* Purchase additional seats or remove inactive members
* Cancel pending invitations to free up seat allocation

**Payment method required**

* Add a valid credit card in Account > Billing
* Ensure your payment method is not expired
* Contact support for payment issues

**Cannot remove last admin**

* Promote another member to admin first before removing yourself

**Invitation expired**

* Resend the invitation from the Team tab
* Verify the correct email address was used
* Check spam folders for the invitation email

For additional help, contact [Support](https://portal.usepylon.com/augment-code/forms/augment-support) or visit [docs.augmentcode.com](https://docs.augmentcode.com).

## Best Practices

**Regular Audits** - Review team membership monthly, remove inactive members promptly, and monitor seat utilization to optimize costs.

**Invitation Management** - Verify email addresses before sending invitations and follow up with invitees directly. Cancel unaccepted invitations after 48 hours to free up seats.

**Billing Optimization** - Right-size your seat count and plan seat changes for billing cycle boundaries to avoid prorated charges.

**Security** - Remove members immediately upon departure, regularly review admin permissions, and use company email addresses for all team members.


# Feedback
Source: https://docs.augmentcode.com/troubleshooting/feedback

We love feedback, and want to hear from you. We want to make the best AI-powered code assistant so you can get more done.

Feedback helps us improve, and we encourage you to share your feedback on every aspect of using Augment—from suggestion and chat response quality, to user experience nusances, and even how we can improve getting your feedback.

### Reporting a bug

To report a bug, please [contact support](https://support.augmentcode.com/). Include as much detail to reproduce the problem as possible; screenshots and videos are very helpful.

### Feedback on completions

We are always balancing the needs for speed and accuracy. We want to know when you get a poor suggestion, hallucination, or a completion that actually doesn't work. The History panel has a log of all of your completions; we encourage you to use it to send us feedback on the completions you've received.

<Note>
  Providing feedback directly in your IDE through the History panel is currently
  only available in Visual Studio Code.
</Note>

<Steps>
  <Step title="Open the History panel">
    Open the History panel by pressing <Keyboard />
    and then searching for `Augment: Show History` in the command menu.
  </Step>

  <Step title="Find the completion you want to report">
    Recent completions are listed in reverse chronological order. Locate the
    completion you want to report and add complete the feedback form.
  </Step>

  <Step title="Submit your feedback">
    After completing the form, click either the red button for bad completions
    or the green button for good completions.
  </Step>
</Steps>

### Feedback on chat

After each Chat interaction, you have the opportunity to provide feedback on the quality of the response. At the bottom of the response click either the thumbs up <Icon icon="thumbs-up" /> or thumbs down <Icon icon="thumbs-down" /> icon. Add additional information in the feedback field, and click `Send Feedback`.


# Jetbrains UI issues
Source: https://docs.augmentcode.com/troubleshooting/jetbrains-rendering-issues

Fix issues where the Augment panel is white, blank or not showing anything in JetBrains IDEs.

## About UI issues in JetBrains IDEs

Some users on newer versions of JetBrains IDEs (2025.1 and above) have reported that the Augment panel is white, blank or not
displaying anything at all. These issues stem from a change to the way JetBrains renders webviews, which is now
done in an out-of-process manner. Disabling out-of-process rendering has resolved a number of problems for users.

This is a known issue that impacts multiple plugins in the Jetbrains ecosystem. JetBrains is tracking the issue in IJPL-186252.

**Note**: If you are using a **JetBrains IDE 2025.2.3 on Windows**, we do not recommend disabling out-of-process rendering due
to a bug where the WebViews will render JS and CSS in plain text making it difficult to use Augment and any other WebViews. There
is a workaround for this issue <a href="https://youtrack.jetbrains.com/issue/JBR-9462/Markdown-rendering-broken-with-ide.browser.jcef.out-of-process.enabledfalse-after-upgrading-to-PyCharm-2025.2.3#focus=Comments-27-12792022.0-0">described here</a>.

If you experience issues after following the steps below, please [contact support](https://support.augmentcode.com/)
for further assistance.

### Disable out-of-process rendering

<Steps>
  <Step title="Open the Custom Properties editor">
    From the menu bar, go to <Command />. If the `idea.properties` file doesn't exist yet, you'll be prompted to create it.
  </Step>

  <Step title="Add the out-of-process rendering property">
    Add the following line to the properties file:

    ```
    ide.browser.jcef.out-of-process.enabled=false
    ```
  </Step>

  <Step title="Save and restart your IDE">
    Save the file and restart your JetBrains IDE for the changes to take effect.
  </Step>
</Steps>

After restarting, the Augment panel should render more consistently.


# Jetbrains panel steals focus
Source: https://docs.augmentcode.com/troubleshooting/jetbrains-stealing-focus

Fix issue where the Augment panel takes focus while typing in JetBrains IDEs.

## About focus issues in JetBrains IDEs

Some users on Linux systems have reported that the Augment Chat window steals focus from the editor while typing. This can interrupt your workflow and make it difficult to use the IDE effectively. This issue can be resolved by enabling off-screen rendering in your JetBrains IDE.

### Enable off-screen rendering

<Steps>
  <Step title="Open the Custom Properties editor">
    From the menu bar, go to <Command />. If the `idea.properties` file doesn't exist yet, you'll be prompted to create it.
  </Step>

  <Step title="Add the off-screen rendering property">
    Add the following line to the properties file:

    ```
    augment.off.screen.rendering=true
    ```
  </Step>

  <Step title="Save and restart your IDE">
    Save the file and restart your JetBrains IDE for the changes to take effect.
  </Step>
</Steps>

After restarting, the Augment panel should no longer steal focus from the editor while you're typing.


# Request IDs
Source: https://docs.augmentcode.com/troubleshooting/request-id

Request IDs are generated with every code suggestion and chat interaction. Our team may ask you to provide the request ID when you report a bug or issue.

## Finding a Request ID for Chat

<Steps>
  <Step title="Open the Chat panel">
    Open the Chat panel by clicking the Augment icon

    <img />

    in the action bar on the left side of your editor.
  </Step>

  <Step title="Open the chat thread">
    If the chat reply you are interested is in a previous chat thread, find the
    chat thread by clicking the <Icon icon="chevron-right" /> at the top of the
    chat panel and clicking the relevant chat thread.
  </Step>

  <Step title="Find the request ID">
    Find the reply in question and click the <Icon icon="link-simple" /> icon
    above the reply to copy the request ID to your clipboard.
  </Step>
</Steps>

## Finding a Request ID for Completions

<Steps>
  <Step title="Open the History panel">
    Open the History panel by pressing <Keyboard />
    and then searching for `Augment: Show History` in the command menu.
  </Step>

  <Step title="Find the request ID">
    Recent requests are listed in reverse chronological order. Locate the
    request you are interested in and copy the request ID by clicking on the
    request ID, for example:
    <br /> `-- Request ID: 7f67c0dd-4c80-4167-9383-8013b18836cb`
  </Step>
</Steps>


# Using Agent
Source: https://docs.augmentcode.com/using-augment/agent

Use Agent to complete simple and complex tasks across your workflow–implementing a feature, upgrade a dependency, or writing a pull request.

## About Agent

Augment Agent is a powerful tool that can help you complete software development tasks end-to-end. From quick edits to complete feature implementation, Agent breaks down your requests into a functional plan and implements each step all while keeping you informed about what actions and changes are happening. Powered by Augment's Context Engine and powerful LLM architecture, Agent can write, document, and test like an experienced member of your team.

## Accessing Agent

To access Agent, simply open the Augment panel and select one of the Agent modes from the drop down in the input box.

<img alt="Augment Agent" />

### Choosing a model

Use the model dropdown in the Augment panel to switch between models. Your selection applies only to Agent for the current workspace and can be changed at any time. See [Available Models](/models/available-models) for details.

## Using Agent

To use Agent, simply type your request into the input box using natural language and click the submit button. You will see the default context including current workspace, current file, and Agent memories. You can add additional context by clicking <AtIcon />and selecting files or folder, or add an image as context by clicking the paperclip. Agent can create, edit, or delete code across your workspace and can use tools like the terminal and external integrations through MCP to complete your request.

### Enhancing your prompt

You can improve the quality of your  by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Reviewing changes

You can review every change Agent makes by clicking on the action to expand the view. Review diffs for file changes, see complete terminal commands and output, and the results of external integration calls.

<img alt="Augment Agent" />

### Checkpoints

Checkpoints are automatically saved snapshots of your workspace as Agent implements the plan allowing you to easily revert back to a previous step. This enables Agent to continue working while you review code changes and commands results. To revert to a previous checkpoint, click the reverse arrow icon to restore your code.

<img alt="Augment Agent" />

### Agent memories

Memories help the Agent remember important details about your workspace and your preferences for working in it. Memories are stored locally and are applied to all Agent requests. Memories can be added automatically by Agent, by clicking the remember button under a message, asking Agent to remember something, or by editing the Memories files directly.

<img alt="Stopping the agent" />

### Agent vs Agent Auto

By default, Agent will pause work when it needs to execute a terminal command or access external integrations. After reviewing the suggested action, click the blue play button to have Agent execute the command and continue working. You tell Agent to skip a specific action by clicking on the three dots and then Skip.

<img alt="Augment Agent" />

In Agent Auto, Agent will act more independently. It will edit files, execute terminal commands, and access tools like MCP servers automatically.

### Stop or guide the Agent

You can interrupt the Agent at any time by clicking Stop. This will pause the action to allow you to correct something you see the agent doing incorrectly. While Agent is working, you can also prompt the Agent to try a different approach which will automatically stop the agent and prompt it to correct its course.

<img alt="Stopping the agent" />

### Quick Ask Mode

Quick Ask Mode is a toggle button in the agent chat interface that restricts the AI to read-only tools only. When activated, it adds a visual badge to the message and focuses the AI on information gathering without making any changes to your codebase.

<img alt="Quick Ask Mode toggle and usage" />

### Comparison to Chat

Agent takes Chat to the next level by allowing Augment to do things for you-that is create and make modifications directly to your codebase. Chat can explain code, create plans, and suggest changes which you can smartly apply one-by-one, but Agent takes it a step further by automatically implementing the entire plan and all code changes for you.

| What are you trying to do?                       | Chat | Agent |
| :----------------------------------------------- | :--: | :---: |
| Ask questions about your code                    |  ☑️  |   ✅   |
| Get advice on how to refactor code               |  ☑️  |   ✅   |
| Add new features to selected lines of code       |  ☑️  |   ✅   |
| Add new feature spanning multiple files          |      |   ✅   |
| Document new features                            |      |   ✅   |
| Queue up tests for you in the terminal           |      |   ✅   |
| Open Linear tickets or start a pull request      |      |   ✅   |
| Start a new branch in GitHub from recent commits |      |   ✅   |
| Automatically perform tasks on your behalf       |      |   ✅   |

### Use cases

Use Agent to handle various aspects of your software development workflow, from simple configuration changes to complex feature implementations. Agent supports your daily engineering tasks like:

* **Make quick edits** - Create a pull request to adjust configuration values like feature flags from FALSE to TRUE
* **Perform refactoring** - Move functions between files while maintaining coding conventions and ensuring bug-free operation
* **Start a first draft for new features** - Start a pull request (PR) with implementing entirely new functionality straight from a GitHub Issue or Linear Ticket
* **Branch from GitHub** - Open a PR from GitHub based on recent commits that creates a new branch
* **Query Supabase tables directly** - Ask Agent to view the contents of a table
* **Start tickets in Linear or Jira** - Open tickets and ask Agent to suggest a plan to address the ticket
* **Add Pull Request descriptions** - Merge your PR into a branch then tell the agent to explain what the changes are and why they were made
* **Create test coverage** - Generate unit tests for your newly developed features
* **Generate documentation** - Produce comprehensive documentation for your libraries and features
* **Start a README** - Write a README for a new feature or updated function that you just wrote
* **Track development progress** - Review and summarize your recent Git commits for better visibility with the GitHub integration

## Next steps

* [Configure Agent Integrations](/setup-augment/agent-integrations)
* [Configure other tools with MCP](/setup-augment/mcp)


# Using Chat
Source: https://docs.augmentcode.com/using-augment/chat

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

## About Chat

Chat is a new way to work with your codebase using natural language. Chat will automatically use the current workspace as context and you can [provide focus](/using-augment/chat-context) for Augment by selecting specific code blocks, files, folders, or external documentation. Details from your current chat, including the additional context, are used to provide more relevant code suggestions as well.

<img alt="Augment Chat" />

## Accessing Chat

Access the Chat sidebar by clicking the Augment icon <img /> in the sidebar or the status bar. You can also open Chat by using one of the keyboard shortcuts below.

**Keyboard Shortcuts**

| Platform      | Shortcut     |
| :------------ | :----------- |
| MacOS         | <Keyboard /> |
| Windows/Linux | <Keyboard /> |

## Using Chat

To use Chat, simply type your question or command into the input field at the bottom of the Chat panel. You will see the currently included context which includes the workspace and current file by default. Use Chat to explain your code, investigate a bug, or use a new library. See [Example Prompts for Chat](/using-augment/chat-prompts) for more ideas on using Chat.

### Conversations about code

To get the best possible results, you can go beyond asking simple questions or commands, and instead have a back and forth conversation with Chat about your code. For example, you can ask Chat to explain a specific function and then ask follow-up questions about possible refactoring options. Chat can act as a pair programmer, helping you work through a technical problem or understand unfamiliar code.

### Enhancing your prompt

You can improve the quality of your  by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Starting a new chat

You should start a new Chat when you want to change the topic of the conversation since the current conversation is used as part of the context for your next question. To start a new chat, open the Augment panel and click the new chat icon <NewChatIcon /> at the top-right of the Chat panel.

### Previous chats

You can continue a chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel. Your previous chats will be listed in reverse chronological order, and you can continue your conversation where you left off.

### Deleting a chat

You can delete a previous chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel to show the list of previous chats. Click the delete icon <DeleteIcon /> next to the chat you want to delete. You will be asked to confirm that you want to delete the chat.


# Using Actions in Chat
Source: https://docs.augmentcode.com/using-augment/chat-actions

Actions let you take common actions on code blocks without leaving Chat. Explain, improve, or find everything you need to know about your codebase.

<img alt="Augment Chat Actions" />

## Using actions in Chat

To use a quick action, you an use a <Keyboard /> command or click the up arrow icon<ArrowUpIcon />to show the available actions. For explain, fix, and test actions, first highlight the code in the editor and then use the command.

| Action       | Usage                                                                    |
| :----------- | :----------------------------------------------------------------------- |
| <Keyboard /> | Use natural language to find code or functionality                       |
| <Keyboard /> | Augment will explain the hightlighted code                               |
| <Keyboard /> | Augment will suggest improvements or find errors in the highlighted code |
| <Keyboard /> | Augment will suggest tests for the highlighted code                      |

Augment will typically include code blocks in the response to the action. See [Applying code blocks from Chat](/using-augment/chat-apply) for more details.


# Applying code blocks from Chat
Source: https://docs.augmentcode.com/using-augment/chat-apply

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

<img alt="Augment Chat Apply" />

## Using code blocks from within Chat

Whenever Chat responds with code, you will have the option to add the code to your codebase. The most common option will be shown as a button and you can access the other options by clicking the overflow menu icon<MoreVertIcon />at the top-right of the code block. You can use the following options to apply the code:

* <FileCopyIcon />**Copy**
  the code from the block to your clipboard
* <FileNewIcon />**Create**
  a new file with the code from the block
* <CheckIcon />**Apply**
  the code from the block intelligently to your file


# Focusing Context in Chat
Source: https://docs.augmentcode.com/using-augment/chat-context

You can specify context from files, folders, and external documentation in your conversation to focus your chat responses.

## About Chat Context

Augment intelligently includes context from your entire workspace based on the ongoing conversation–even if you don't have the relevant files open in your editor–but sometimes you want Augment to prioritize specific details for more relevant responses.

<video />

### Focusing context for your conversation

You can specify context by clicking the <AtIcon /> icon at the top-left of the Chat panel or by <Command /> in the input field. You can use fuzzy search to filter the list of context options quickly. There are a number of different types of additional context you can add to your conversation:

1. Highlighted code blocks
2. Specific files or folders within your workspace
3. 3rd party documentation, like Next.js documentation

#### Mentioning files and folders

Include specific files or folders in your context by typing `@` followed by the file or folder name. For example, `@routes.tsx` will include the `routes.tsx` file in your context. You can include multiple files or folders.

#### Mentioning 3rd party documentation

You can also mention 3rd party documentation in your context by typing `@` followed by the name of the documentation. For example, `@Next.js` will include Next.js documentation in your context. Augment provides nearly 300 documentation sets spanning across a wide range of domains such as programming languages, packages, software tools, and frameworks.


# Example Prompts for Chat
Source: https://docs.augmentcode.com/using-augment/chat-prompts

Using natural language to interact with your codebase unlocks a whole new way of working. Learn how to get the most out of Chat with the following example prompts.

## About chatting with your codebase

Augment's Chat has deep understanding about your codebase, dependencies, and best practices. You can use Chat to ask questions about your code, but it also can help you with general software engineering questions, think through technical decisions, explore new libraries, and more.

## Enhancing your prompt

You can improve the quality of your  by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

## Example Prompts

### Explain code

* Explain this codebase to me
* How do I use the Twilio API to send a text message?
* Explain how generics work in TypeScript and give me a simple example

### Finding code

* Where are all the useEffect hooks that depend on the 'currentUser' variable?
* Find the decorators that implement retry logic across our microservices
* Find coroutines that handle database transactions without a timeout parameter

### Generate code

* Write a function to check if a string is a valid email address
* Generate a middleware function that rate-limits API requests using a sliding window algorithm
* Create a SQL query to find the top 5 customers who spent the most money last month

### Write tests

* Write integration tests for this API endpoint
* What edge cases have I not included in this test?
* Generate mock data for testing this customer order processing function

### Refactor and improve code

* This function is running slowly with large collections - how can I optimize it?
* Refactor this callback-based code to use async/await instead
* Rewrite this function in Rust

### Find and fix errors

* This endpoint sometimes returns a 500 error. Here's the error log - what's wrong?
* I'm getting 'TypeError: Cannot read property 'length' of undefined' in this component.
* Getting CORS errors when my frontend tries to fetch from the API


# Completions
Source: https://docs.augmentcode.com/using-augment/completions

Use code completions to get more done. Augment's radical context awareness means more relevant suggestions, fewer hallucinations, and less time hunting down documentation.

## About Code Completions

Augment's Code Completions integrates with your IDE's native completions system to give you autocomplete-like suggestions as you type. You can accept all of a suggestion, accept partial suggestions a word or a line at a time, or just keep typing to ignore the suggestion.

## Using Code Completions

To use code completions, simply start typing in your IDE. Augment will provide suggestions based on the context of your code. You can accept a suggestion by pressing <Keyboard />, or ignore it by continuing to type.

For example, add the following function to a TypeScript file:

```typescript theme={null}
function getUser(): Promise<User>;
```

As you type `getUser`, Augment will suggest the function signature. Press <Keyboard /> to accept the suggestion. Augment will continue to offer suggestions until the function is complete, at which point you will have a function similar to:

```typescript theme={null}
function getUser(): Promise<User> {
  return fetch("/api/user/1")
    .then((response) => response.json())
    .then((json) => {
      return json as User;
    });
}
```

### Accepting Completions

<Tabs>
  <Tab title="MacOS">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard />                           |
    | Accept next word of suggestion | <Keyboard />                           |
    | Accept next line of suggestion | None (see above)                       |
    | Reject suggestion              | <Keyboard />                           |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | VSCode: <Keyboard />                   |
    |                                | JetBrains: <Keyboard />                |
  </Tab>

  <Tab title="Windows/Linux">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard />                           |
    | Accept next word of suggestion | <Keyboard />                           |
    | Accept next line of suggestion | None (see above)                       |
    | Reject suggestion              | <Keyboard />                           |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | VSCode: <Keyboard />                   |
    |                                | JetBrains: <Keyboard />                |
  </Tab>
</Tabs>

### Disabling Completions

<Tabs>
  <Tab title="Visual Studio Code">
    You can disable automatic code completions by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command />.
  </Tab>

  <Tab title="JetBrains IDEs">
    You can disable automatic code completions by clicking the Augment icon <img /> in the status bar at the bottom right corner of your IDE, then selecting <Command />.
  </Tab>
</Tabs>

### Enable Completions

<Tabs>
  <Tab title="Visual Studio Code">
    If you've temporarily disabled completions, you can re-enable them by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command />.
  </Tab>

  <Tab title="JetBrains IDEs">
    If you've temporarily disabled completions, you can re-enable them by clicking the Augment icon <img /> in the status bar at the bottom right corner of your IDE, then selecting <Command />.
  </Tab>
</Tabs>


# Instructions
Source: https://docs.augmentcode.com/using-augment/instructions

Use Instructions to write or modify blocks of code using natural language. Refactor a function, write unit tests, or craft any prompt to transform your code.

<Availability />

## About Instructions

Augment's Instructions let you use natural language prompts to insert new code or modify your existing code. Instructions can be initiated by hitting <Keyboard /> and entering an instruction inside the input box that appears in the diff view. The change will be applied as a diff to be reviewed before accepting.

## Using Instructions

To start a new Instruction, there are two options. You can select & highlight the code you want to change or place your cursor where you want new code to be added, then press <Keyboard />. You'll be taken to a diff view where you can enter your prompt and see the results.

For example, you can generate new functions based on existing code:

```
> Add a getUser function that takes userId as a parameter
```

<img alt="Augment Instructions Diff" />

Your change will be made as a diff, so you can review the suggested updates before modifying your code. Use the following shortcuts or click the options in the UI to accept or reject the changes.

<Tabs>
  <Tab title="MacOS">
    | Action            | Shortcut     |
    | :---------------- | :----------- |
    | Start instruction | <Keyboard /> |
    | Accept            | <Keyboard /> |
    | Reject            | <Keyboard /> |
  </Tab>

  <Tab title="Windows/Linux">
    | Action            | Shortcut     |
    | :---------------- | :----------- |
    | Start instruction | <Keyboard /> |
    | Accept            | <Keyboard /> |
    | Reject            | <Keyboard /> |
  </Tab>
</Tabs>


# Next Edit
Source: https://docs.augmentcode.com/using-augment/next-edit

Use Next Edit to flow through complex changes across your codebase. Cut down the time you spend on repetitive work like refactors, library upgrades, and schema changes.


<Availability />

## About Next Edit

<iframe title="Feature Intro: Augment Next Edit" />

Next Edit helps you complete your train of thought by suggesting changes based on
your recent work and other context. You can jump to the next edit and quickly accept or
reject the suggested change with a single keystroke.

## Using Next Edit

<img />

When Next Edit has a suggestion available, you will see a gutter icon and a summary
of the change in gray at the end of the line.
To jump to the next suggestion, press <Keyboard /> and
after reviewing the change, press <Keyboard /> to accept
or <Keyboard /> to reject. If there are multiple
changes, press <Keyboard /> to accept and go to the
next suggestion.

<img />

<img />

By default, Next Edit will briefly highlight which parts of the existing code will
change before applying the change and highlighting the new code. Use Undo
(<Keyboard />) and Redo
(<Keyboard />) to manually review the change.
You can configure this behavior in your Augment extension settings.

### Keyboard Shortcuts

<Tabs>
  <Tab title="MacOS">
    | Action            | Default shortcut |
    | :---------------- | :--------------- |
    | Go to next        | <Keyboard />     |
    | Go to previous    | <Keyboard />     |
    | Accept suggestion | <Keyboard />     |
    | Reject suggestion | <Keyboard />     |
  </Tab>

  <Tab title="Windows/Linux">
    | Action            | Default shortcut |
    | :---------------- | :--------------- |
    | Go to next        | <Keyboard />     |
    | Go to previous    | <Keyboard />     |
    | Accept suggestion | <Keyboard />     |
    | Reject suggestion | <Keyboard />     |
  </Tab>
</Tabs>

### Next Edit Indicators And Actions

There are several indicators to let you know Next Edits are available:

<img />

1. **Editor Title Icon** (Top Right): Changes colors when next edits are available.
   Click on the <NextEditPencil /> icon to open the next edit menu for
   additional actions like enabling/disabling the feature or accessing settings.
2. **Gutter Icon** (Left) - Indicates which lines will be changed by the suggestion
   and whether it will insert, delete or change code.
3. **Grey Text** (Right) -  appears on the line with the suggestion on screen with a
   brief summary of the change and the keybinding to press (typically
   <Keyboard />).

<img />

4. **Hint Box** (Bottom Left) - appears when the next suggestion is off screen with
   brief summary of the change and the keybinding to press (typically
   <Keyboard />).

The tooltip also presents a few actions as icons:

* <NextEditDiffIcon /> Toggles showing diffs for suggestions in the tooltip.
* <NextEditSettingsIcon /> Opens Next Edit settings.

### Next Edit Settings

You can configure Next Edit settings in your Augment extension settings.
To open Augment extension settings, either navigate to the option through the pencil
menu, or open the Augment Commands panel by pressing
<Keyboard /> and select <Command />.

Here are some notable settings:

* <Command />: Use to enable or
  disable the feature.
* <Command />: When enabled, Next
  Edits will suggest changes in other files via the hint box.
* <Command />: When enabled, Next
  Edits will automatically apply changes when you jump to them.
* <Command />: When enabled,
  Next Edits will show a diff of the suggested change in the hover.
* <Command />: When enabled,
  Next Edits will highlight all lines with a suggestion in addition to showing gutter
  icons and grey text.


# Using Remote Agent
Source: https://docs.augmentcode.com/using-augment/remote-agent

Use Remote Agent to complete tasks across your workflow–implementing a feature, upgrade a dependency, or writing a pull request–all from the cloud and with the full power of Visual Studio Code when you need it.

## About Remote Agent

Augment Remote Agent is a powerful tool that can help you complete software development tasks end-to-end that runs in a secure, cloud environment. You can run multiple agents in parallel on independent tasks, and you'll monitor and manage their progress from within Visual Studio Code. Remote Agents can run in normal or auto mode, just like IDE-based agents, and will notify you when they need attention.

### How is Remote Agent different from Agent?

Remote Agent is a cloud version of the IDE-bound Agent. Each Remote Agent runs on its own secure environment, with its own workspace-all of which is managed for you. Each Remote Agent works independently and on its own branch, so you can have multiple agents working on the same repository at the same time.

## Accessing Remote Agent

To start a new Remote Agent, simply open the Augment panel and select Remote Agent from the drop down in the input box.

<img alt="Augment Remote Agent" />

### Agent dashboard

You can view all of your remote agents in the Remote Agent dashboard by clicking the <Command /> icon in the top of the Augment panel. From the dashboard you are able to see the status of all of your agents, connect to them through SSH, or delete them when they are no longer needed.

<img alt="Augment Agent" />

## Using Remote Agent

Remote Agents function nearly identically to IDE-bound agents as you work through your tasks and projects. Because they run asynchronously in the cloud, you can access and manage them while working on other projects in your editor. Access your Remote Agents from the threads menu at the top of the Augment panel or through the Remote Agent dashboard.

You can create and manage a Remote Agent for any repository you have access to through GitHub regardless of which project you are currently working on in your editor.

### Create a remote agent

<Note>
  Before you can use Remote Agent, you will need to connect your GitHub account to enable the agent to clone your repository, create branches, and open pull requests. See [Agent Integrations](/setup-augment/agent-integrations) for setup instructions.
</Note>

1. **Select the repository** you want the agent to work on
2. **Select the branch** or let the agent create a new branch for you
3. **Select an environment** or [create a new one](/using-augment/remote-agent-environment) for the agent to run in
4. Enter your prompt into the input box using natural language and click **Create agent**

<img alt="Create a Remote Agent" />

#### Agent environment

Each Remote Agent runs in an secure, independent environment in the cloud. This enables each agent to have its own workspace, copy of the repository, and virtualized operating system to run other tools and commands. You can use the [base environment](/using-augment/remote-agent-environment#base-environment), or setup a custom environment using a bash script to configure the tools the agent will need to complete the task.

See [Remote Agent Environment](/using-augment/remote-agent-environment) for more details on customizing the agent environment.

### Agent notifications

By default, you will receive a notification in VS Code when the agent has completed a task or needs your attention. You can disable notifications for a remote agent by clicking the bell icon in the theads list of the Augment panel.

### Iterating with an agent

Once an agent has completed the task, you can continue to iterate with the agent by sending additional messages. The agent will continue to work on the task, using its past conversations as context. If you need to switch to editing files directly, you can connect to the agent environment over SSH. See [Connecting to a Remote Agent](#connecting-to-a-remote-agent-environment) for more details.

### Reviewing changes

You can review every change Agent makes by clicking on the action to expand the view. Review diffs for file changes, see complete terminal commands and output, and the results of external integration calls.

<img alt="Augment Agent" />

### Stop or guide the Agent

You can interrupt the Agent at any time by clicking Stop. This will pause the action to allow you to correct something you see the agent doing incorrectly. While Agent is working, you can also prompt the Agent to try a different approach which will automatically stop the agent and prompt it to correct its course.

<img alt="Stopping the agent" />

### Connecting to a Remote Agent environment

<Note>
  You will need to have the [Remote-SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) installed in Visual Studio Code to connect to a remote agent. If you do not have it installed, you will be prompted to install it automatically.
</Note>

From time to time you may need to connect to a remote agent to view or edit files directly, in that case you can connect to the agent environment over SSH. From the Remote Agent dashboard, click the <Command /> button in the agent card you with to connect to.

This will open a Visual Studio Code window connected to the agent's environment. If this is your first time opening the connection, you will be prompted by VS Code to trust the files in the remote folder. Click <Command /> to continue.

<img alt="Augment Agent" />

You can use the new VS Code window to view and edit files, run commands in the terminal, and generally interact with the agent just like you would a local IDE-bound agent.

### Opening a Pull Request

When the agent has completed the work, you can open a pull request to have your changes opened for review and merging into the main branch. Select the agent from the threads list and click <Command />. The agent will create a branch, commit the changes, and open a pull request for you. This will count against your credits quota.

<img alt="Augment Agent Pull Request" />

### Resuming a Remote Agent

Remote Agents automatically pause after completing a request or remaining idle for a period of time. To resume a paused Remote Agent, either click <Command /> or send a new message to the agent. Both actions will count against your credits quota.

## Comparison chart

Agent takes Chat to the next level by allowing Augment to do things for you-that is create and make modifications directly to your codebase. Chat can explain code, create plans, and suggest changes which you can smartly apply one-by-one, but Agent takes it a step further by automatically implementing the entire plan and all code changes for you.

| What are you trying to do?                       | Chat | Agent | Remote Agent |
| :----------------------------------------------- | :--: | :---: | :----------: |
| Ask questions about your code                    |  ☑️  |   ✅   |       ✅      |
| Get advice on how to refactor code               |  ☑️  |   ✅   |       ✅      |
| Add new features to selected lines of code       |  ☑️  |   ✅   |       ✅      |
| Add new feature spanning multiple files          |      |   ✅   |       ✅      |
| Document new features                            |      |   ✅   |       ✅      |
| Open Linear tickets or start a pull request      |      |   ✅   |       ✅      |
| Start a new branch in GitHub from recent commits |      |   ✅   |       ✅      |
| Automatically perform tasks on your behalf       |      |   ✅   |       ✅      |
| Work on multiple tasks in the same repository    |      |       |       ✅      |
| Continue working after closing VS Code           |      |       |       ✅      |

## Use cases

Use Remote Agent to handle various aspects of your software development workflow, from simple configuration changes to feature implementations. Remote Agent is best for discreet tasks that can be completed in isolation from other work. Remote Agent supports your daily engineering tasks like:

* **Make quick edits** - Create a pull request to adjust configuration values like feature flags from FALSE to TRUE
* **Fix papercuts** - Fix small bugs or issues in the codebase that never make it to the top of your TODO list
* **Perform refactoring** - Move functions between files while maintaining coding conventions and ensuring bug-free operation
* **Explore alternatives** - Run multiple remote agents to create alternative solutions to a problem
* **Start a first draft for new features** - Start a pull request (PR) with implementing entirely new functionality straight from a GitHub Issue or Linear Ticket
* **Start tickets in Linear or Jira** - Open tickets and ask Agent to suggest a plan to address the ticket
* **Create test coverage** - Generate unit tests for your newly developed features
* **Generate documentation** - Produce comprehensive documentation for your libraries and features

## Remote Agent Clean-up

Remote Agents automatically pause after completing a request or remaining idle for a period of time. Agents that remain idle for 30 days are automatically cleaned up by the system. This cleanup process removes all files in the Remote Workspace, conversation history, and any pending diffs.

## Next steps

* [Configure Agent Integrations](/setup-augment/agent-integrations)
* [Configure other tools with MCP](/setup-augment/mcp)


# Using Augment for Slack
Source: https://docs.augmentcode.com/using-augment/slack

Chat with Augment directly in Slack to explore your codebase, get instant help, and collaborate with your team on technical problems.

## About Augment for Slack

Augment for Slack brings the power of Augment Chat to your team's Slack workspace. Mention <Command /> in any channel or start a DM with Augment to have deep codebase-aware conversations with your team. Before you can use Augment for Slack, you will need to [install the Augment Slack App](/setup-augment/install-slack-app).

<img alt="Augment for Slack" />

## Adding Augment to Channels

Mention <Command /> to add it to any public or private channel.

*Note: To protect your code, Augment excludes repository context in channels with external members.*

## Starting Conversations in Channels

Mention <Command /> anywhere in your message or thread to start a conversation. Augment will consider the entire thread's context when responding. Remove messages by adding a ❌ reaction.

## Direct Messages

While group discussions help share knowledge, you can also have private conversations with Augment. Access it by:

* Clicking the Augment logo in the top right of your Slack workspace
* Finding it under <Command /> in the Slack sidebar
* Pressing <Keyboard /> and searching for <Command />

If you don't see the Augment logo, add it to your [navigation bar](/setup-augment/install-slack-app#3-add-augment-to-the-slack-navigation-bar). *If you don't see this option, contact your workspace admin to [re-install the App](/setup-augment/install-slack-app#2-install-slack-app).*

You do not need to mention Augment in direct messages - it will respond to every message!

## Restricting where Augment can be used

Augment already avoids responding with codebase context in external channels, to protect your codebase from Slack users outside of your organization. Beyond this, you can also further restrict what channels Augment can be used in, with an allowlist. If configured, Augment will only respond in channels or DMs that are in the allowlist. To use this feature, contact us.

## Repository Context

Augment uses the default branch (typically `main`) of your linked repositories. Currently, other branches aren't accessible.

If you have multiple repositories installed, use <Command /> to choose which repository Augment should use for the current conversation. This selection applies to the specific channel or DM where you run the command, allowing you to work with different repositories in different conversations.

## Feedback

Help us improve by reacting with 👍 or 👎 to Augment's responses, or use the `Send feedback` message shortcut. We love hearing from you!


# Using Tasklist
Source: https://docs.augmentcode.com/using-augment/tasklist

Use Tasklist to break down complex problems into manageable steps, track progress, and collaborate with Agent on multi-step tasks.

## About the Tasklist?

Augment's Tasklist helps the Agent in the IDE create and refine a step-by-step plan for you to review. The Tasklist provides a structured interface for collaboration between you and the Agent, allowing you to break down complex problems into manageable, sequential steps.

<img alt="Tasklist Overview" />

## Getting started with Tasklist?

Tasklist improves agent effectiveness on long or complex tasks by:

* **Maintaining context** across different conversations by moving your Tasklist to a new chat
* **Breaking down complex problems** into manageable, sequential steps
* **Gathering progress** across threads
* **Exploring alternative solutions** to completed tasks if you need to pivot
* **Streamlining your approach** to nebulous problems by deleting irrelevant steps once the path forward is clear

Tasklist provides a structured interface for collaboration and opens up possibilities for agent-to-agent collaboration. We hypothesize that an interface such as Tasklist could be a preferred way to interact with coding agents in the future.

## Creating a New Task

### Automatic Creation

The Agent will usually create a Tasklist when it encounters a complex, multi-step problem. You can also ask the Agent to make a Tasklist for you by simply prompting "Start a Tasklist to..." then add the problem you are trying to tackle.

### Manual Creation

You can also manually create a Tasklist:

1. Switch to Tasklist using the checklist button next to Changes
2. Click the plus to add your first task
3. Alternatively, you can create a new task by typing in the gray prompt box at the bottom of the extension. Click **Add Task** from the dropdown arrow next to Send

<img alt="Creating a new task" />

## Running Tasks

To run a task, click the grey triangle (play button) next to the task. The Agent will begin executing the task and update its status as it progresses.

<img alt="Running a task" />

## Task Status Indicators

Task statuses are indicated by different colors and icons:

* **Empty circle** - Task has not yet started
* **Blue half circle** - Task is currently in progress
* **Green checkbox** - Task has been completed and is ready for review

<img alt="Task status indicators" />

## Subtasks

Augment Code automatically generates subtasks when needed. The Agent will automatically add and nest required subtasks under your initial tasks. You can edit and expand these subtasks just like any other task in the list. Likewise, you can remove subtasks you deem unnecessary.

<img alt="Subtasks example" />

## Managing Running Tasks

### Stopping a Task

You can treat any in-progress task like any prompt you might send the Agent. To stop what the Agent is doing and offer a corrective action, click the red square (stop button) and tell the Agent what you want it to do instead.

### Running All Tasks

The Agent can complete all the tasks sequentially by clicking the triangle (play button) at the top of the Tasklist.

## Reviewing Changes

You can review the changes made by the Agent after a task is completed by toggling between the Tasks and Changes view to see the diffs (differences) of the work done by the agent for each task.

<img alt="Reviewing changes in Tasks and Changes view" />

## Integration with Task Management Tools

### Jira and Linear Integration

The Tasklist is a perfect pairing with existing task management tools like Jira or Linear:

* Ask the Agent to create a Tasklist based on tickets inside Jira or Linear
* Further break down complex tickets into manageable steps
* Once your Tasklist is completed, you can ask the Agent to resolve the issue inside Jira or Linear and append the steps taken as a comment

### Standalone Usage

Don't use an issue tracker? No problem - use Tasklist to track issues you need to tackle across Threads.

## Best Practices

* **Be specific** when creating tasks to help the Agent understand exactly what needs to be done
* **Review and edit** the automatically generated subtasks to ensure they align with your goals
* **Use the stop function** to provide course corrections when the Agent is heading in the wrong direction
* **Leverage the Changes view** to review all modifications made during task execution
* **Move Tasklists** between conversations to maintain context across different chat sessions

## Next Steps

* [Learn more about Agent](/using-augment/agent)
* [Configure Agent Integrations](/setup-augment/agent-integrations)


# Install Augment for Vim and Neovim
Source: https://docs.augmentcode.com/vim/setup-augment/install-vim-neovim

Augment for Vim and Neovim gives you powerful code completions and chat capabilities integrated into your favorite code editor.

<CardGroup>
  <Card title="Get the Augment Extension" href="https://github.com/augmentcode/augment.vim" icon={<NeoVimLogo />}>
    View Augment for Vim and Neovim on GitHub
  </Card>
</CardGroup>

## About Installation

Installing <ExternalLink href="https://github.com/augmentcode/augment.vim" /> is easy and will take you less than a minute. You can install the extension manually or you can use your favorite plugin manager.

## Prerequisites

Augment for Vim and Neovim requires a compatible version of Vim or Neovim, and Node.js:

| Dependency                                                                                     | Minimum version |
| :--------------------------------------------------------------------------------------------- | :-------------- |
| [Vim](https://github.com/vim/vim?tab=readme-ov-file#installation)                              | 9.1.0           |
| [Neovim](https://github.com/neovim/neovim/tree/master?tab=readme-ov-file#install-from-package) | 0.10.0          |
| [Node.js](https://nodejs.org/en/download/package-manager/all)                                  | 22.0.0          |

## 1. Install the extension

<Tabs>
  <Tab title="Neovim">
    ### Manual Installation

    ```sh theme={null}
    git clone https://github.com/augmentcode/augment.vim.git ~/.config/nvim/pack/augment/start/augment.vim
    ```

    ### Using Lazy.nvim

    Add the following to your `init.lua` file, then run `:Lazy sync` in Neovim. See more details about using [Lazy.nvim on GitHub](https://github.com/folke/lazy.nvim).

    ```lua theme={null}
    require('lazy').setup({
      -- Your other plugins here
      'augmentcode/augment.vim',
    })
    ```
  </Tab>

  <Tab title="Vim">
    ### Manual Installation

    ```sh theme={null}
    git clone https://github.com/augmentcode/augment.vim.git ~/.vim/pack/augment/start/augment.vim
    ```

    ### Using Vim Plug

    Add the following to your `.vimrc` file, then run `:PlugInstall` in Vim. See more details about using [Vim Plug on GitHub](https://github.com/junegunn/vim-plug).

    ```vim theme={null}
    call plug#begin()

    " Your other plugins here
    Plug 'augmentcode/augment.vim'

    call plug#end()
    ```
  </Tab>
</Tabs>

## 2. Configure your workspace context

Add your project root to your workspace context by setting `g:augment_workspace_folders` in your `.vimrc` or `init.lua` file before the plugin is loaded. For example:

```vim theme={null}
" Add to your .vimrc
let g:augment_workspace_folders = ['/path/to/project']

" Add to your init.lua
vim.g.augment_workspace_folders = {'/path/to/project'}
```

Augment's Context Engine provides the best suggestions when it has access to your project's codebase and any related repositories. See more details in
[Configure additional workspace context](/vim/setup-augment/workspace-context-vim).

## 3. Sign-in to Augment

Open Vim or Neovim and sign-in to Augment with the following command:

```vim theme={null}
:Augment signin
```

<Next>
  * [Using Chat with Vim and Neovim](/vim/using-augment/vim-chat)
  * [Using Completions with Vim and Neovim](/vim/using-augment/vim-completions)
  * [Configure keyboard shortcuts](/vim/setup-augment/vim-keyboard-shortcuts)
</Next>


# Commands and shortcuts for Vim and Neovim
Source: https://docs.augmentcode.com/vim/setup-augment/vim-keyboard-shortcuts

Augment flexibly integrates with your editor to provide keyboard shortcuts for common actions. Customize your keymappings to quickly accept suggestions and chat with Augment.

## All available commands

| Command      | Action                                      |
| :----------- | :------------------------------------------ |
| <Keyboard /> | Globally enable suggestions (on by default) |
| <Keyboard /> | Globally disable suggestions                |
| <Keyboard /> | Send a chat message to Augment              |
| <Keyboard /> | Start a new chat conversation               |
| <Keyboard /> | Toggle the chat panel visibility            |
| <Keyboard /> | Start the sign in flow                      |
| <Keyboard /> | Sign out of Augment                         |
| <Keyboard /> | View the current status of the plugin       |
| <Keyboard /> | View the plugin log                         |

## Creating custom shortcuts

You can create custom shortcuts for any of the above commands by adding mappings to your `.vimrc` or `init.lua` file. For example, to create a shortcut for the :Augment chat\* commands, you can add the following mappings:

```vim theme={null}
" Send a chat message in normal and visual mode
nnoremap <leader>ac :Augment chat<CR>
vnoremap <leader>ac :Augment chat<CR>

" Start a new chat conversation
nnoremap <leader>an :Augment chat-new<CR>

" Toggle the chat panel visibility
nnoremap <leader>at :Augment chat-toggle<CR>
```

## Customizing accepting a completion suggestion

By default <Keyboard /> is used to accept a suggestion. If you want to use a key other than <Keyboard /> to accept a suggestion, create a mapping that calls `augment#Accept()`. The function takes an optional arugment used to specify the fallback text to insert if no suggestion is available.

```vim theme={null}
" Use Ctrl-Y to accept a suggestion
inoremap <c-y> <cmd>call augment#Accept()<cr>

" Use enter to accept a suggestion, falling back to a newline if no suggestion
" is available
inoremap <cr> <cmd>call augment#Accept("\n")<cr>
```

You can disable the default <Keyboard /> mapping by setting `g:augment_disable_tab_mapping = v:true` before the plugin is loaded.


# Add context to your workspace
Source: https://docs.augmentcode.com/vim/setup-augment/workspace-context-vim

You can add additional context to your workspace–such as additional repositories and folders–to give Augment a full view of your system.

<Availability />

## About Workspace Context

Augment is powered by its deep understanding of your code. You'll need to configure your project's source in your workspace context to get full codebase understanding in your chats and suggestions.

Sometimes important parts of your system exist outside of the current project. For example, you may have seperate frontend and backend repositories or have many services across multiple repositories. Adding additional codebases to your workspace context will improve the code suggestions and chat responses from Augment.

## Add context to your workspace

<Note>
  Be sure to set `g:augment_workspace_folders` before the Augment plugin is loaded.
</Note>

To add context to your workspace, in your `.vimrc` set `g:augment_workspace_folders` to a list of paths to the folders you want to add to your workspace context. For example:

```vim theme={null}
let g:augment_workspace_folders = ['/path/to/folder', '~/path/to/another/folder']
```

You may want to ignore specific folders, like `node_modules`, see [Ignoring files with .augmentignore](/setup-augment/workspace-indexing#ignoring-files-with-augmentignore) for more details.

After adding a workspace folder and restarting Vim, the output of the <Keyboard /> command will include the syncing progress for the added folder.


# Index your workspace
Source: https://docs.augmentcode.com/vim/setup-augment/workspace-indexing

When your workspace is indexed, Augment can provide tailored code suggestions and answers based on your unique codebase, best practices, coding patterns, and preferences. You can always control what files are indexed.

## About indexing your workspace

When you open a workspace with Augment enabled, your codebase will be automatically uploaded to Augment's secure cloud. You can control what files get indexed using `.gitignore` and `.augmentignore` files. Indexing usually takes less than a minute but can take longer depending on the size of your codebase.

## Security and privacy

Augment stores your code securely and privately to enable our powerful context engine. We ensure code privacy through a proof-of-possession API and maintain strict internal data minimization principles. [Read more about our security](https://www.augmentcode.com/security).

## What gets indexed

Augment will index all the files in your workspace, except for the files that match patterns in your `.gitignore` file and the `.augmentignore` file.

## Ignoring files with .augmentignore

The `.augmentignore` file is a list of file patterns that Augment will ignore when indexing your workspace. Create an `.augmentignore` file in the root of your workspace. You can use any glob pattern that is supported by the [gitignore](https://git-scm.com/docs/gitignore) file.

## Including files that are .gitignored

If you have a file or directory in your `.gitignore` that you want to indexed, you can add it to your `.augmentignore` file using the `!` prefix.

For example, you may want your `node_modules` indexed to provide Augment with context about the dependencies in their project, but it is typically included in their `.gitignore`. Add `!node_modules` to your `.augmentignore` file.

<CodeGroup>
  ```bash .augmentignore theme={null}
  # Include .gitignore excluded files with ! prefix
  !node_modules

  # Exclude other files with .gitignore syntax
  data/test.json
  ```

  ```bash .gitignore theme={null}
  # Exclude dependencies
  node_modules

  # Exclude secrets
  .env

  # Exclude build artifacts
  out
  build
  ```
</CodeGroup>


# Chat
Source: https://docs.augmentcode.com/vim/using-augment/vim-chat

Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

## Using chat

Chat is a new way to work with your codebase using natural language. Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

| Command      | Action                           |
| :----------- | :------------------------------- |
| <Keyboard /> | Send a chat message to Augment   |
| <Keyboard /> | Start a new chat conversation    |
| <Keyboard /> | Toggle the chat panel visibility |

### Sending a message

You can send a message to Chat using the <Keyboard /> command. You can send your message as an optional argument to the command or enter it into the command-line when prompted. Each new message will continue the current conversation which will be used as context for your next message.

**Focusing on selected text**

If you have text selected in `visual mode`, Augment will automatically include it in your message. This is useful for asking questions about specific code or requesting changes to the selected code.

### Starting a new conversation

You can start a new conversation by using the <Keyboard /> command.

<Next>
  * [Using Completions](/vim/using-augment/vim-completions)
  * [Configure keyboard shortcuts](/vim/setup-augment/vim-keyboard-shortcuts)
</Next>


# Completions
Source: https://docs.augmentcode.com/vim/using-augment/vim-completions

Use code completions to get more done. Augment’s radical context awareness means more relevant suggestions, fewer hallucinations, and less time hunting down documentation.

## Using completions

Augment’s code completions integrates with Vim and Neovim to give you autocomplete-like suggestions as you type. Completions are enable by default and you can use <Keyboard /> to accept a suggestion.

| Command      | Action                                      |
| :----------- | :------------------------------------------ |
| <Keyboard /> | Accept the current suggestion               |
| <Keyboard /> | Globally enable suggestions (on by default) |
| <Keyboard /> | Globally disable suggestions                |

### Customizing accepting a suggestion

If you want to use a key other than <Keyboard /> to accept a suggestion, create a mapping that calls `augment#Accept()`. The function takes an optional arugment used to specify the fallback text to insert if no suggestion is available.

```vim theme={null}
" Use Ctrl-Y to accept a suggestion
inoremap <c-y> <cmd>call augment#Accept()<cr>

" Use enter to accept a suggestion, falling back to a newline if no suggestion
" is available
inoremap <cr> <cmd>call augment#Accept("\n")<cr>
```

You can disable the default <Keyboard /> mapping by setting `g:augment_disable_tab_mapping = v:true` before the plugin is loaded.

<Next>
  * [Using Chat](/vim/using-augment/vim-chat)
  * [Configure keyboard shortcuts](/vim/setup-augment/vim-keyboard-shortcuts)
</Next>


