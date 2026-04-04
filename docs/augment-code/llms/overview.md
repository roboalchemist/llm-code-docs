# Source: https://docs.augmentcode.com/context-services/sdk/overview.md

# Source: https://docs.augmentcode.com/context-services/overview.md

# Source: https://docs.augmentcode.com/context-services/mcp/overview.md

# Source: https://docs.augmentcode.com/context-services/context-connectors/overview.md

# Source: https://docs.augmentcode.com/codereview/overview.md

# Source: https://docs.augmentcode.com/cli/overview.md

# Source: https://docs.augmentcode.com/cli/automation/overview.md

# Source: https://docs.augmentcode.com/analytics/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview of Analytics

> Monitor team usage patterns and analyze Augment Code adoption across your organization.

<Note>
  **Enterprise-Only Feature**

  Exclusive to Enterprise customers, access the Team Usage under Analytics at [app.augmentcode.com/dashboard](https://app.augmentcode.com/dashboard).
</Note>

## Feature Metrics at a Glance

<CardGroup cols={1}>
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

<CardGroup cols={2}>
  <Card title="Contact Sales" icon="briefcase">
    Reach out to your sales representative for strategic guidance
  </Card>

  <Card title="Contact Support" icon="life-ring" href="https://support.augmentcode.com">
    Get technical support at support.augmentcode.com
  </Card>
</CardGroup>

## Related Resources

<CardGroup cols={2}>
  <Card title="Analytics API" icon="code" href="/analytics/analytics-api">
    Programmatic access to usage metrics via REST API
  </Card>

  <Card title="API Reference" icon="book" href="/analytics/api-reference">
    Detailed API endpoint documentation
  </Card>
</CardGroup>
