# Source: https://docs.port.io/guides/all/track-ai-adoption-and-impact.md

# Track AI adoption and impact

Tracking AI adoption provides visibility into how engineering teams are leveraging AI coding agents and the impact these tools have on delivery outcomes. Without visibility into AI usage patterns, teams struggle to understand adoption rates, measure productivity gains, and identify which teams or services benefit most from AI assistance.

This guide helps engineering managers, platform engineers, and product leaders answer critical questions about AI adoption:

* **Adoption**: Which teams and services are using AI coding tools?
* **Impact**: How does AI assistance affect PR throughput and cycle time?
* **Effectiveness**: Are AI-assisted PRs delivering faster or higher quality outcomes?
* **Cost optimization**: Are AI tool licenses being fully utilized?

By the end of this guide, you will have dashboards that track AI adoption metrics, enabling you to understand usage patterns, measure productivity impact, and make informed decisions about AI tool investments across your organization.

![](/img/guides/ai-adoption-dashboard.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Compare PR throughput and cycle time between AI-assisted and traditional workflows.
* Identify teams and services with the highest AI adoption rates.
* Track AI usage trends over time to understand adoption patterns.
* Monitor AI tool license utilization and revoke unused licenses to optimize costs.
* Correlate AI adoption with operational metrics like bug rates and incident resolution time.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [GitHub integration](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) is installed in your account.
* The `githubPullRequest` and `githubRepository` blueprints are already created (these are created when you install the GitHub integration).
* For **Cursor tracking**: Port's [Cursor integration](/build-your-software-catalog/sync-data-to-catalog/ai-agents/cursor/.md) is installed in your account, with the `cursor_usage_record`, `cursor_user_usage_record`, and `cursor_team_usage_record` blueprints created as described in the [Cursor integration setup](/build-your-software-catalog/sync-data-to-catalog/ai-agents/cursor/.md#set-up-data-model).
* For **Copilot tracking**: Port's [GitHub Copilot integration](/build-your-software-catalog/sync-data-to-catalog/ai-agents/github-copilot/.md) is installed in your account.
* For **AI impact on operations**: Port's [Jira integration](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/.md) is installed in your account (optional, for tracking bugs, security issues, and incidents).
* For the **AI Impact Insights** widget: [Port AI](/ai-interfaces/port-ai/overview.md) is enabled in your account.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

We will create and update blueprints to support AI adoption tracking.

### Update the User blueprint[â](#update-the-user-blueprint "Direct link to Update the User blueprint")

Depending on which AI tool you want to track, you need to update the User blueprint with the appropriate properties.

* Cursor
* GitHub Copilot

Ensure you have installed the [Cursor integration](/build-your-software-catalog/sync-data-to-catalog/ai-agents/cursor/.md) before proceeding.

Add properties to track Cursor license and usage status.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find the `User` blueprint and click on it.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add the following properties to the `properties` section:

   **Cursor license properties for User blueprint (click to expand)**

   ```
   "cursor_licensed": {
     "title": "Cursor Licensed",
     "type": "boolean",
     "description": "Whether the user has a Cursor license"
   },
   "cursor_active": {
     "title": "Cursor Active",
     "type": "boolean",
     "description": "Whether the user has used Cursor in the last 90 days"
   },
   "cursor_last_active": {
     "title": "Cursor Last Active",
     "type": "string",
     "format": "date-time",
     "description": "Last time the user used Cursor"
   }
   ```

5. Click `Save` to update the blueprint.

Ensure you have installed the [GitHub Copilot integration](/build-your-software-catalog/sync-data-to-catalog/ai-agents/github-copilot/.md) before proceeding.

Add properties to track Copilot license and usage status.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find the `User` blueprint and click on it.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add the following properties to the `properties` section:

   **Copilot license properties for User blueprint (click to expand)**

   ```
   "copilot_licensed": {
     "title": "Copilot Licensed",
     "type": "boolean",
     "description": "Whether the user has a GitHub Copilot license"
   },
   "copilot_active": {
     "title": "Copilot Active",
     "type": "boolean",
     "description": "Whether the user has used Copilot in the last 90 days"
   },
   "copilot_last_active": {
     "title": "Copilot Last Active",
     "type": "string",
     "format": "date-time",
     "description": "Last time the user used Copilot"
   }
   ```

5. Click `Save` to update the blueprint.

### Update the pull request blueprint[â](#update-the-pull-request-blueprint "Direct link to Update the pull request blueprint")

Regardless of which AI tool you're tracking, you need to add a property to identify AI-assisted PRs.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find the `githubPullRequest` blueprint and click on it.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add the following property to the `properties` section:

   **AI agent property for Pull Request blueprint (click to expand)**

   ```
   "created_by_agent": {
     "type": "boolean",
     "title": "Created By AI Agent",
     "description": "Determines whether or not the PR was created by an AI agent such as Copilot, Claude, or Devin"
   }
   ```

5. Click `Save` to update the blueprint.

### Update the Jira issue blueprint[â](#update-the-jira-issue-blueprint "Direct link to Update the Jira issue blueprint")

To correlate AI adoption with operational metrics like bug resolution and incident response time, we need to add properties to track issue categories and lead time.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find the `jiraIssue` blueprint and click on it.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add the following properties to the `properties` section:

   **Issue category and lead time properties (click to expand)**

   ```
   "issue_category": {
     "title": "Issue Category",
     "type": "string",
     "enum": ["Bug", "Security Issues", "Incidents", "Other"],
     "enumColors": {
       "Bug": "red",
       "Security Issues": "orange",
       "Incidents": "pink",
       "Other": "lightGray"
     },
     "description": "Category of the issue for tracking purposes"
   },
   "lead_time_hours": {
     "title": "Lead Time (Hours)",
     "type": "number",
     "description": "Time from issue creation to resolution in hours"
   }
   ```

5. Click `Save` to update the blueprint.

## Update integration mapping[â](#update-integration-mapping "Direct link to Update integration mapping")

Now we'll configure the GitHub integration to detect AI-assisted PRs and Jira issues to populate the issue category and lead time properties.

### Github Integration mapping

1. Go to your [Data Source](https://app.getport.io/settings/data-sources) page.

2. Select the GitHub integration.

3. Add or update the following YAML block in the editor:

   **GitHub integration configuration (click to expand)**

   ```
   resources:
     - kind: repository
       selector:
         query: 'true'
         teams: true
       port:
         entity:
           mappings:
             identifier: .full_name
             title: .name
             blueprint: '"githubRepository"'
             properties:
               readme: file://README.md
               url: .html_url
               defaultBranch: .default_branch
               last_push: .pushed_at
               visibility: .visibility
               language: .language
     - kind: pull-request
       selector:
         query: 'true'
         closedPullRequests: true
       port:
         entity:
           mappings:
             identifier: .id|tostring
             title: .title
             blueprint: '"githubPullRequest"'
             properties:
               status: .status
               closedAt: .closed_at
               updatedAt: .updated_at
               mergedAt: .merged_at
               createdAt: .created_at
               link: .html_url
               created_by_agent: .user.login | ascii_downcase | test("(copilot|claude|devin)")
               leadTimeHours: >-
                 (.created_at as $createdAt | .merged_at as $mergedAt | ($createdAt
                 | sub("\\..*Z$"; "Z") | strptime("%Y-%m-%dT%H:%M:%SZ") | mktime)
                 as $createdTimestamp | ($mergedAt | if . == null then null else
                 sub("\\..*Z$"; "Z") | strptime("%Y-%m-%dT%H:%M:%SZ") | mktime end)
                 as $mergedTimestamp | if $mergedTimestamp == null then null else
                 (((($mergedTimestamp - $createdTimestamp) / 3600) * 100 | floor) /
                 100) end)
               pr_age: >-
                 ((now - (.created_at | sub("\\.[0-9]+Z$"; "Z") | fromdateiso8601))
                 / 86400) | round
               cycle_time: >-
                 if .merged_at then (((.merged_at   | sub("\\.[0-9]+Z$"; "Z") |
                 fromdateiso8601) - (.created_at | sub("\\.[0-9]+Z$"; "Z") |
                 fromdateiso8601)) / 86400 | round) else null end
             relations:
               repository: .head.repo.full_name
   ```

   AI agent detection

   The mapping uses a regex pattern to detect AI agents by checking if the PR creator's username contains "copilot", "claude", or "devin" (case-insensitive). You can customize this pattern to match your organization's AI agent naming conventions.

4. Click `Save & Resync` to apply the mapping.

### Configure Jira integration mapping

1. Go to your [Data Source](https://app.getport.io/settings/data-sources) page.

2. Select the Jira integration.

3. Update the `jiraIssue` mapping to include the new properties:

   **Jira integration mapping for issue properties (click to expand)**

   ```
   - kind: issue
     selector:
       query: 'true'
     port:
       entity:
         mappings:
           identifier: .key
           title: .fields.summary
           blueprint: '"jiraIssue"'
           properties:
             # ... existing properties ...
             issue_category: |
               if .fields.labels | any(. == "security") then "Security Issues"
               elif .fields.issuetype.name == "Bug" then "Bug"
               elif .fields.issuetype.name == "Incident" then "Incidents"
               else "Other" end
             lead_time_hours: |
               if .fields.resolutiondate != null then
                 ((.fields.resolutiondate | fromdateiso8601) - (.fields.created | fromdateiso8601)) / 3600 | round
               else
                 null
               end
   ```

   Issue category logic

   The mapping categorizes issues based on labels and issue type. Issues with a "security" label are classified as Security Issues, Bug types as Bug, and Incident types as Incidents. You can customize this logic to match your organization's issue classification.

4. Click `Save & Resync` to apply the mapping.

## Visualize metrics[â](#visualize-metrics "Direct link to Visualize metrics")

Once the data is synced, we can create a dedicated dashboard in Port to monitor and analyze AI adoption and impact metrics.

![](/img/guides/visualizeAIAdoptionMetrics.png)

### Create a dashboard[â](#create-a-dashboard "Direct link to Create a dashboard")

1. Navigate to your [software catalog](https://app.getport.io/organization/catalog).
2. Click on the **`+ New`** button in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard **AI Adoption and Impact**.
5. Click `Create`.

We now have a blank dashboard where we can start adding widgets to visualize AI adoption metrics.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In the new dashboard, create the following widgets to match the [demo dashboard](https://demo.port.io/ai_insights). Some widgets require the Cursor integration, while others work with any AI tool.

Cursor integration widgets

Widgets that use the `cursor_usage_record`, `cursor_user_usage_record`, or `cursor_team_usage_record` blueprints require Port's [Cursor integration](/build-your-software-catalog/sync-data-to-catalog/ai-agents/cursor/.md) to be installed and syncing data.

**AI Impact Insights chat widget (click to expand)**

This widget provides an interactive AI chat interface for exploring your AI adoption data, allowing users to ask questions and get AI-powered insights.

1. Click `+ Widget` and select **AI Chat**.

2. Title: `AI Impact Insights`.

3. Add the following **conversation starters**:

   <!-- -->

   * `Where are we paying for AI licenses but seeing low usage?`
   * `How does AI usage impact engineering performance?`
   * `Is AI usage trending up or down over time?`

4. Click **Save**.

**AI Agent insights recommendations markdown widget (click to expand)**

This widget provides a quick link to a detailed AI impact report generated using Port MCP.

1. Click `+ Widget` and select **Markdown**.

2. Title: `AI Agent insights recommendations`.

3. Add the following content:

   ```
   [View the full AI Impact report generated using Port MCP](https://docs.port.io/ai-interfaces/port-mcp-server/overview-and-installation)
   ```

4. Click **Save**.

**AI Tool License Utilization table (click to expand)**

This table shows all users with their AI tool license and usage status across both Cursor and Copilot, allowing you to identify unused licenses for cost optimization.

1. Click `+ Widget` and select **Table**.

2. Title: `AI Tool License Utilization`.

3. Description: `Track Cursor and Copilot usage. Revoke unused licenses to optimize costs.`

4. Choose the **User** blueprint.

5. Click **Save** to add the widget to the dashboard.

6. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

7. In the top right corner of the table, click on `Manage Properties` and add the following columns:

   <!-- -->

   * **Title**: User's name.
   * **Cursor Licensed**: Whether user has a Cursor license.
   * **Cursor Active**: Whether user has used Cursor in last 90 days.
   * **Copilot Licensed**: Whether user has a Copilot license.
   * **Copilot Active**: Whether user has used Copilot in last 90 days.

8. Click on the **save icon** in the top right corner of the widget to save the customized table.

**Cursor adoption across users pie chart (click to expand)**

This chart shows the distribution of active vs inactive Cursor users, giving a quick view of adoption across your organization.

1. Click **`+ Widget`** and select **Pie chart**.
2. Title: `Cursor Adoption Across Users`.
3. Description: `Based on active usage`.
4. Choose the **User** blueprint.
5. Under `Breakdown by property`, select the **Cursor Active** property.
6. Click **Save**.

**Total number of active Cursor users (monthly) line chart (click to expand)**

1. Click `+ Widget` and select **Line Chart**.
2. Title: `Total Number of Active Cursor Users (Monthly)`.
3. Description: `Active Cursor Users during the month`.
4. Select `Aggregate Property (All Entities)` **Chart type** and choose **Cursor Usage Record** as the **Blueprint**.
5. Select `total_active_users` as the **Property**.
6. Select `sum` for the **Function**.
7. Input `Number of Users` as the **Y axis** **Title**.
8. Input `Date` as the **X axis** **Title**.
9. Select `record_date` for **Measure time by**.
10. Set **Time Interval** to `month` and **Time Range** to `In the past 6 months`.
11. Click `Save`.

**AI Cursor usage trend over time line chart (click to expand)**

This chart tracks AI coding activity over time, showing the trend of rejected suggestions and lines of code added or deleted.

1. Click `+ Widget` and select **Line Chart**.
2. Title: `AI Cursor Usage Trend Over Time`.
3. Description: `Track AI coding activity over time`.
4. Select `Aggregate Property (All Entities)` **Chart type** and choose **Cursor Usage Record** as the **Blueprint**.
5. Select the following properties: `Total Rejects`, `Total Lines Added`, `Total Lines Deleted`.
6. Select `average` for the **Function**.
7. Select `record_date` for **Measure time by**.
8. Set **Time Interval** to `week` and **Time Range** to `In the past 30 days`.
9. Click `Save`.

**Daily cost trends line chart (click to expand)**

1. Click `+ Widget` and select **Line Chart**.
2. Title: `Daily Cost Trends`.
3. Description: `Track AI usage costs over time`.
4. Select `Aggregate Property (All Entities)` **Chart type** and choose **Cursor Usage Record** as the **Blueprint**.
5. Select `total_cents` as the **Property**.
6. Select `sum` for the **Function**.
7. Select `record_date` for **Measure time by**.
8. Set **Time Interval** to `week` and **Time Range** to `In the past 30 days`.
9. Click `Save`.

**Average Lead Time (Monthly) line chart (click to expand)**

1. Click `+ Widget` and select **Line Chart**.

2. Title: `Average Lead Time (Monthly)`.

3. Description: `Shows the average number of days from issue creation to resolution`.

4. Select `Aggregate Property (All Entities)` **Chart type** and choose **Pull Request** as the **Blueprint**.

5. Select `leadTimeHours` as the **Property**.

6. Select `average` for the **Function**.

7. Input `Lead Time (Days)` as the **Y axis** **Title**.

8. Input `Date` as the **X axis** **Title**.

9. Select `createdAt` for **Measure time by**.

10. Set **Time Interval** to `month` and **Time Range** to `In the past 6 months`.

11. Add this JSON to the **Additional filters** editor:

    ```
    {
      "combinator": "and",
      "rules": [
        {
          "value": "merged",
          "property": "status",
          "operator": "="
        }
      ]
    }
    ```

12. Click `Save`.

**PR Throughput (Monthly) line chart (click to expand)**

1. Click `+ Widget` and select **Line Chart**.

2. Title: `PR Throughput (Monthly)`.

3. Description: `Monthly PRs merged`.

4. Select `Count Entities (All Entities)` **Chart type** and choose **Pull Request** as the **Blueprint**.

5. Select `count` for the **Function**.

6. Input `Pull Requests` as the **Y axis** **Title**.

7. Input `Date` as the **X axis** **Title**.

8. Select `createdAt` for **Measure time by**.

9. Set **Time Interval** to `month` and **Time Range** to `In the past 6 months`.

10. Add this JSON to the **Additional filters** editor:

    ```
    {
      "combinator": "and",
      "rules": [
        {
          "value": "merged",
          "property": "status",
          "operator": "="
        }
      ]
    }
    ```

11. Click `Save`.

**PR Cycle Time (Monthly) line chart (click to expand)**

1. Click `+ Widget` and select **Line Chart**.

2. Title: `PR Cycle Time (Monthly)`.

3. Description: `Monthly average PR time to merge (hours)`.

4. Select `Aggregate Property (All Entities)` **Chart type** and choose **Pull Request** as the **Blueprint**.

5. Select `cycle_time` as the **Property**.

6. Select `average` for the **Function**.

7. Input `Lead time (Hours)` as the **Y axis** **Title**.

8. Input `Date` as the **X axis** **Title**.

9. Select `createdAt` for **Measure time by**.

10. Set **Time Interval** to `month` and **Time Range** to `In the past 6 months`.

11. Add this JSON to the **Additional filters** editor:

    ```
    {
      "combinator": "and",
      "rules": [
        {
          "value": "merged",
          "property": "status",
          "operator": "="
        }
      ]
    }
    ```

12. Click `Save`.

**AI adoption impact on operations line chart (click to expand)**

This chart shows the monthly trend of bugs, security issues, and incidents to help correlate AI adoption with operational quality.

1. Click `+ Widget` and select **Line Chart**.

2. Title: `AI Adoption Impact On Operations`.

3. Description: `Issues created each month`.

4. Select `Count Entities (All Entities)` **Chart type** and choose **Jira Issue** as the **Blueprint**.

5. Under `Breakdown by property`, select the **Issue Category** property.

6. Input `Issues` as the **Y axis** **Title**.

7. Input `Date` as the **X axis** **Title**.

8. Select `createdAt` for **Measure time by**.

9. Set **Time Interval** to `month` and **Time Range** to `In the past 6 months`.

10. Add this JSON to the **Additional filters** editor to only show relevant categories:

    ```
    {
      "combinator": "and",
      "rules": [
        {
          "property": "issue_category",
          "operator": "in",
          "value": ["Bug", "Security Issues", "Incidents"]
        }
      ]
    }
    ```

11. Click `Save`.

**Teams with the most AI-created PRs bar chart (click to expand)**

1. Click **`+ Widget`** and select **Bar Chart**.

2. Title: `Teams with the most AI-created PRs`.

3. Choose the **Pull Request** blueprint.

4. Under `Breakdown by property`, select the **Owning Team** property (via repository relation).

5. Add this JSON to the **Additional filters** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "value": true,
         "property": "created_by_agent",
         "operator": "="
       }
     ]
   }
   ```

6. Click **Save**.

**PRs created with AI pie chart (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.
2. Title: `PRs Created with AI`.
3. Choose the **Pull Request** blueprint.
4. Under `Breakdown by property`, select the **Created By AI Agent** property.
5. Click **Save**.

**AI model usage distribution pie chart (click to expand)**

This chart shows which AI models are being used most frequently across your organization.

1. Click **`+ Widget`** and select **Pie chart**.
2. Title: `AI Model Usage Distribution`.
3. Description: `Which AI models are being used most frequently`.
4. Choose the **Cursor Usage Record** blueprint.
5. Under `Breakdown by property`, select the **Most Used Model** property.
6. Click **Save**.

**Team activity breakdown table (click to expand)**

This table provides a per-team view of Cursor AI usage, showing how each team is adopting AI tools and their acceptance rates.

1. Click `+ Widget` and select **Table**.

2. Title: `Team Activity Breakdown`.

3. Description: `Detailed view of team productivity and AI usage patterns`.

4. Choose the **Cursor Team Usage Record** blueprint.

5. Click **Save** to add the widget to the dashboard.

6. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

7. In the top right corner of the table, click on `Manage Properties` and add the following columns:

   <!-- -->

   * **Team**: The team name.
   * **Total Lines Added**: Total lines of code added with AI assistance.
   * **Agent Requests**: Number of AI agent requests made.
   * **Input Tokens**: Total input tokens consumed.
   * **Output Tokens**: Total output tokens generated.
   * **Total Rejects**: Number of AI suggestions rejected.
   * **Total Accepts**: Number of AI suggestions accepted.
   * **Acceptance Rate**: Percentage of AI suggestions accepted.

8. Click on the **save icon** in the top right corner of the widget to save the customized table.

**Total cost number chart (click to expand)**

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Total Cost`.
3. Description: `Total cost of Cursor AI usage`.
4. Choose the **Cursor Usage Record** blueprint.
5. Select `Aggregate by property` **Chart type**.
6. Select `total_cents` as the **Property**.
7. Select `sum` for the **Function**.
8. Select `$` as the **Unit**.
9. Click **Save**.

## Set up self-service actions (optional)[â](#set-up-self-service-actions-optional "Direct link to Set up self-service actions (optional)")

You can set up self-service actions to activate or revoke AI tool licenses. These actions allows you to easily activate or revoke licenses for users in your organization directly from your Port dashboard.

* Cursor
* GitHub Copilot

**Activate Cursor License action (click to expand)**

This action calls the Cursor API to add a user to your team, which provisions their license.

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on `+ Action`.

3. Select the **User** blueprint.

4. Copy and paste the following JSON schema:

   Create in Port

   ```
   {
     "identifier": "activate_cursor_license",
     "title": "Activate Cursor License",
     "icon": "Cursor",
     "description": "Activate a Cursor license for this user",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "confirm": {
             "type": "boolean",
             "title": "Confirm Activation",
             "description": "Check this box to confirm you want to activate a Cursor license"
           }
         },
         "required": ["confirm"]
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.cursor.com/teams/members",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Authorization": "Bearer {{ .secrets.CURSOR_API_KEY }}",
         "Content-Type": "application/json"
       },
       "body": {
         "email": "{{ .entity.properties.email }}"
       }
     }
   }
   ```

5. Click `Create` to save the action.

6. Add your Cursor API key as a secret named `CURSOR_API_KEY` in your [Port secrets](https://app.getport.io/settings/portal/secrets).

**Revoke Cursor License action (click to expand)**

This action calls the Cursor API to remove a user from your team, which revokes their license.

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on `+ Action`.

3. Select the **User** blueprint.

4. Copy and paste the following JSON schema:

   Create in Port

   ```
   {
     "identifier": "revoke_cursor_license",
     "title": "Revoke Cursor License",
     "icon": "Cursor",
     "description": "Revoke the Cursor license for this user",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "confirm": {
             "type": "boolean",
             "title": "Confirm Revocation",
             "description": "Check this box to confirm you want to revoke the Cursor license"
           }
         },
         "required": ["confirm"]
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.cursor.com/teams/members/{{ .entity.properties.email }}",
       "agent": false,
       "synchronized": true,
       "method": "DELETE",
       "headers": {
         "Authorization": "Bearer {{ .secrets.CURSOR_API_KEY }}",
         "Content-Type": "application/json"
       }
     }
   }
   ```

5. Click `Create` to save the action.

6. Add your Cursor API key as a secret named `CURSOR_API_KEY` in your [Port secrets](https://app.getport.io/settings/portal/secrets).

Cursor API

The Cursor API endpoint `DELETE /teams/members/{email}` removes a user from your Cursor team. Refer to the [Cursor API documentation](https://docs.cursor.com/account/teams/api) for more details.

**Activate Copilot License action (click to expand)**

This action calls the GitHub API to add a user to the Copilot subscription.

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on `+ Action`.

3. Select the **User** blueprint.

4. Copy and paste the following JSON schema:

   Create in Port

   ```
   {
     "identifier": "activate_copilot_license",
     "title": "Activate Copilot License",
     "icon": "Github",
     "description": "Activate a GitHub Copilot license for this user",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "confirm": {
             "type": "boolean",
             "title": "Confirm Activation",
             "description": "Check this box to confirm you want to activate a Copilot license"
           }
         },
         "required": ["confirm"]
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.github.com/orgs/YOUR_ORG/copilot/billing/selected_users",
       "agent": false,
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Authorization": "Bearer {{ .secrets.GITHUB_COPILOT_ADMIN_TOKEN }}",
         "Accept": "application/vnd.github+json",
         "X-GitHub-Api-Version": "2022-11-28"
       },
       "body": {
         "selected_usernames": ["{{ .entity.properties.github_username }}"]
       }
     }
   }
   ```

5. Replace `YOUR_ORG` with your GitHub organization name.

6. Click `Create` to save the action.

7. Add your GitHub token as a secret named `GITHUB_COPILOT_ADMIN_TOKEN` in your [Port secrets](https://app.getport.io/settings/portal/secrets). The token requires the `manage_billing:copilot` scope.

**Revoke Copilot License action (click to expand)**

This action calls the GitHub API to remove a user's Copilot license assignment.

1. Go to the [Self-service](https://app.getport.io/self-serve) page of your portal.

2. Click on `+ Action`.

3. Select the **User** blueprint.

4. Copy and paste the following JSON schema:

   Create in Port

   ```
   {
     "identifier": "revoke_copilot_license",
     "title": "Revoke Copilot License",
     "icon": "Github",
     "description": "Revoke the GitHub Copilot license for this user",
     "trigger": {
       "type": "self-service",
       "operation": "DAY-2",
       "userInputs": {
         "properties": {
           "confirm": {
             "type": "boolean",
             "title": "Confirm Revocation",
             "description": "Check this box to confirm you want to revoke the Copilot license"
           }
         },
         "required": ["confirm"]
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://api.github.com/orgs/YOUR_ORG/copilot/billing/selected_users",
       "agent": false,
       "synchronized": true,
       "method": "DELETE",
       "headers": {
         "Authorization": "Bearer {{ .secrets.GITHUB_COPILOT_ADMIN_TOKEN }}",
         "Accept": "application/vnd.github+json",
         "X-GitHub-Api-Version": "2022-11-28"
       },
       "body": {
         "selected_usernames": ["{{ .entity.properties.github_username }}"]
       }
     }
   }
   ```

5. Replace `YOUR_ORG` with your GitHub organization name.

6. Click `Create` to save the action.

7. Add your GitHub token as a secret named `GITHUB_COPILOT_ADMIN_TOKEN` in your [Port secrets](https://app.getport.io/settings/portal/secrets). The token requires the `manage_billing:copilot` scope.

GitHub Copilot API

The GitHub API endpoint `DELETE /orgs/{org}/copilot/billing/selected_users` removes Copilot access for specified users. Refer to the [GitHub Copilot API documentation](https://docs.github.com/en/rest/copilot/copilot-user-management#remove-users-from-the-copilot-subscription-for-an-organization) for more details.

![](/img/guides/activateOrRevokeLicence.png)

## Related guides[â](#related-guides "Direct link to Related guides")

* [Visualize Cursor metrics](/guides/all/visualize-cursor-metrics.md)
* [Visualize GitHub Copilot metrics](/guides/all/visualize-github-copilot-metrics.md)
* [Track AI-driven pull requests](/guides/all/track-ai-driven-pull-requests.md)
* [Measure and track delivery performance](/guides/all/measure-and-track-delivery-performance.md)
* [Measure reliability and stability of delivery pipeline](/guides/all/measure-reliability-and-stability.md)
