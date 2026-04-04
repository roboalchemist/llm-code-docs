# Source: https://docs.port.io/guides/all/visualize-github-copilot-metrics.md

# Visualize GitHub Copilot metrics

This guide demonstrates how to set up a monitoring dashboard to gain insights into your GitHub Copilot usage using Port. You'll learn how to visualize key metrics like acceptance rates, active users, chat productivity, and track team adoption over time.

![](/img/ai-agents/copilotDashboard.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Monitor Copilot usage trends and adoption across teams.
* Track code suggestion acceptance rates to measure productivity gains.
* Analyze chat productivity and user engagement with Copilot.
* Report on ROI of GitHub Copilot investment to leadership.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [GitHub Copilot integration](/build-your-software-catalog/sync-data-to-catalog/ai-agents/github-copilot/.md) is installed and syncing data.

## Create the dashboard[â](#create-the-dashboard "Direct link to Create the dashboard")

1. Navigate to your [software catalog](https://app.getport.io/organization/catalog).

2. Click on the **`+ New`** button in the left sidebar.

3. Select **New dashboard**.

4. Name the dashboard **Copilot Insights**.

5. Input `Monitor Copilot usage and performance metrics across teams` under **Description**.

6. Select the `Github` icon.

7. Click **Create**.

You now have a blank dashboard where you can add widgets to visualize your GitHub Copilot metrics.

## Add widgets[â](#add-widgets "Direct link to Add widgets")

Create the following widgets to gain insights into your GitHub Copilot usage:

### Total active users widget[â](#total-active-users-widget "Direct link to Total active users widget")

**Total active users (click to expand)**

1. Click on **`+ Widget`** and select **Number Chart**.

2. Fill in the following details:

   * **Title**: `Total Active Users (Avg)`.
   * **Description**: `Average number of active users using Copilot per day`.
   * **Icon**: `Users`.
   * **Blueprint**: `github_copilot_usage`.
   * **Chart type**: Select `Aggregate by property`.
   * **Property**: `total_active_users`.
   * **Function**: `Average`.
   * **Average of**: `day`.
   * **Measure time by**: `createdAt`.
   * **Custom unit**: `users`.

3. Click **Save**.

### Overall acceptance rate widget[â](#overall-acceptance-rate-widget "Direct link to Overall acceptance rate widget")

**Overall acceptance rate (click to expand)**

1. Click on **`+ Widget`** and select **Number Chart**.

2. Fill in the following details:

   * **Title**: `Overall Acceptance Rate (%)`.
   * **Description**: `How often Copilot suggestions are accepted`.
   * **Icon**: `metric`.
   * **Blueprint**: `github_copilot_usage`.
   * **Chart type**: Select `Aggregate by property`.
   * **Property**: `acceptance_rate`.
   * **Function**: `Average`.
   * **Average of**: `total`.
   * **Unit**: `%`.

3. Click **Save**.

### Total suggestions generated widget[â](#total-suggestions-generated-widget "Direct link to Total suggestions generated widget")

**Total suggestions generated (click to expand)**

1. Click on **`+ Widget`** and select **Number Chart**.

2. Fill in the following details:

   * **Title**: `Total Suggestions Generated`.
   * **Description**: `Average suggested lines of code per day`.
   * **Blueprint**: `github_copilot_usage`.
   * **Chart type**: Select `Aggregate by property`.
   * **Property**: `total_lines_suggested`.
   * **Function**: `Average`.
   * **Average of**: `day`.
   * **Measure time by**: `createdAt`.
   * **Custom unit**: `suggested lines of code`.

3. Click **Save**.

### Chat productivity widget[â](#chat-productivity-widget "Direct link to Chat productivity widget")

**Chat productivity (click to expand)**

1. Click on **`+ Widget`** and select **Number Chart**.

2. Fill in the following details:

   * **Title**: `Chat Productivity`.
   * **Description**: `Average chat turns per day`.
   * **Icon**: `Chat`.
   * **Blueprint**: `github_copilot_usage`.
   * **Chart type**: Select `Aggregate by property`.
   * **Property**: `total_chat_turns`.
   * **Function**: `Average`.
   * **Average of**: `day`.
   * **Measure time by**: `createdAt`.
   * **Custom unit**: `chats`.

3. Click **Save**.

### Usage by team widget[â](#usage-by-team-widget "Direct link to Usage by team widget")

**Usage by team (click to expand)**

1. Click on **`+ Widget`** and select **Pie Chart**.

2. Fill in the following details:

   * **Title**: `Usage by Team`.
   * **Description**: `Contribution of each team to copilot usage`.
   * **Icon**: `Pie`.
   * **Blueprint**: `github_copilot_usage`.
   * **Breakdown by Property**: `github_team`.

3. Click **Save**.

### Acceptance rate over time widget[â](#acceptance-rate-over-time-widget "Direct link to Acceptance rate over time widget")

**Acceptance rate over time (click to expand)**

1. Click on **`+ Widget`** and select **Line Chart**.

2. Fill in the following details:

   * **Title**: `Acceptance Rate Over Time`.
   * **Description**: `See quality improvements (or declines) over time`.
   * **Icon**: `LineChart`.
   * **Blueprint**: `github_copilot_usage`.
   * **Chart type**: Select `Aggregate properties(All Entities)`.
   * **Properties**: `total_acceptances_count`.
   * **Function**: `average`.
   * **Time interval**: `Week`.
   * **Time range**: `In the past 30 days`.
   * **Measure time by**: `createdAt`.

3. Click **Save**.

### Active users over time widget[â](#active-users-over-time-widget "Direct link to Active users over time widget")

**Active users over time (click to expand)**

1. Click on **`+ Widget`** and select **Line Chart**.

2. Fill in the following details:

   * **Title**: `Active Users Over Time`.
   * **Description**: `Shows if team usage is growing`.
   * **Icon**: `LineChart`.
   * **Blueprint**: `github_copilot_usage`.
   * **Chart type**: Select `Aggregate properties(All Entities)`.
   * **Properties**: `total_active_users`, `total_active_chat_users`.
   * **Function**: `average`.
   * **Time interval**: `Week`.
   * **Time range**: `In the past 30 days`.
   * **Measure time by**: `createdAt`.

3. Click **Save**.

### Chat productivity over time widget[â](#chat-productivity-over-time-widget "Direct link to Chat productivity over time widget")

**Chat productivity over time (click to expand)**

1. Click on **`+ Widget`** and select **Line Chart**.

2. Fill in the following details:

   * **Title**: `Chat Productivity Over Time`.
   * **Description**: `Reveals growing reliance on Copilot Chat`.
   * **Icon**: `LineChart`.
   * **Blueprint**: `github_copilot_usage`.
   * **Chart type**: Select `Aggregate properties(All Entities)`.
   * **Properties**: `total_chat_turns`, `total_chat_acceptances`.
   * **Function**: `average`.
   * **Time interval**: `Week`.
   * **Time range**: `In the past 30 days`.
   * **Measure time by**: `createdAt`.

3. Click **Save**.

### Total suggestions vs. acceptances over time widget[â](#total-suggestions-vs-acceptances-over-time-widget "Direct link to Total suggestions vs. acceptances over time widget")

**Total suggestions vs. acceptances over time (click to expand)**

1. Click on **`+ Widget`** and select **Line Chart**.

2. Fill in the following details:

   * **Title**: `Total Suggestions vs. Acceptances Over Time`.
   * **Description**: `How Copilot suggestions and acceptances change over time to track usage and engagement`.
   * **Icon**: `LineChart`.
   * **Blueprint**: `github_copilot_usage`.
   * **Chart type**: Select `Aggregate properties(All Entities)`.
   * **Properties**: `total_suggestions_count`, `total_acceptances_count`.
   * **Function**: `average`.
   * **Time interval**: `Week`.
   * **Time range**: `In the past 30 days`.
   * **Measure time by**: `createdAt`.

3. Click **Save**.
