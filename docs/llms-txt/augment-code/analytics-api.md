# Source: https://docs.augmentcode.com/analytics/analytics-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics API

> Access usage metrics and analytics for your organization.

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

    ```bash  theme={null}
    curl -X GET "https://api.augmentcode.com/analytics/v0/dau-count" \
      -H "Authorization: Bearer <your-api-token>"
    ```

    For more details on service accounts, see the [Service Accounts documentation](/cli/automation/service-accounts).
  </Step>
</Steps>

## Available Endpoints

The Analytics API provides several endpoints to access different types of usage data:

<CardGroup cols={2}>
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

<CardGroup cols={2}>
  <Card title="API Reference" icon="book" href="/analytics/api-reference">
    View detailed API endpoint documentation
  </Card>

  <Card title="Service Accounts" icon="key" href="/cli/automation/service-accounts">
    Learn more about service accounts and authentication
  </Card>
</CardGroup>
