# Source: https://docs.port.io/guides/all/measure-pr-delivery-metrics.md

# Measure PR delivery metrics

Understanding how pull requests flow through your engineering organization is essential for identifying delivery bottlenecks, measuring team efficiency, and driving continuous improvement. Without PR-level visibility, engineering leaders lack the data needed to spot stale reviews, unbalanced workloads, or degrading cycle times before they impact delivery.

This guide walks you through building a comprehensive PR delivery metrics dashboard in Port that answers critical questions at both the **service level** and **team level**:

* **Throughput**: How many PRs are being merged weekly and monthly?
* **Cycle time**: How long does it take from PR creation to merge?
* **Staleness**: Which PRs have been open for more than 7 days, and what share do they represent?
* **Quality indicators**: Do open PRs have reviewers and assignees assigned?

By the end of this guide, you will have a dashboard that provides full visibility into PR delivery health across services and teams, helping you identify improvement areas and track progress over time.

![](/img/guides/pr-delivery-metrics-dashboard.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Track PR cycle time trends to identify slowdowns in code review and CI processes.
* Monitor PR throughput to understand team delivery capacity and detect regressions.
* Surface stale PRs that have been open longer than 7 days to unblock delivery.
* Identify PRs without assigned reviewers or assignees to improve process compliance.
* Compare delivery metrics across teams to understand organizational performance.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [GitHub integration](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) is installed in your account.
* The `githubPullRequest`, `githubRepository`, `githubUser`, and `githubTeam` blueprints already exist (these are created automatically when you install the GitHub integration).

## Key metrics overview[â](#key-metrics-overview "Direct link to Key metrics overview")

This dashboard tracks PR delivery metrics across two levels â individual services and teams:

| Metric                 | What it measures                                     | Why it matters                                                  |
| ---------------------- | ---------------------------------------------------- | --------------------------------------------------------------- |
| **Open PRs**           | Total number of currently open PRs                   | Shows current work in progress and potential bottleneck signals |
| **PR throughput**      | Number of PRs merged per week/month                  | Indicates delivery flow and team output capacity                |
| **Throughput trend**   | Weekly vs. monthly throughput direction              | Reveals whether delivery velocity is improving or degrading     |
| **Stale PRs**          | PRs open longer than 7 days                          | Highlights blocked work, unclear ownership, or review delays    |
| **Stale PR share (%)** | Percentage of open PRs that are stale                | Quantifies the severity of staleness across the portfolio       |
| **Cycle time**         | Hours from PR creation to merge (weekly/monthly avg) | Exposes friction in reviews, CI, and approval processes         |
| **Cycle time trend**   | Weekly vs. monthly cycle time direction              | Shows whether review and merge speed is improving over time     |
| **Reviewer coverage**  | Whether open PRs have reviewers assigned             | Signals process compliance and review readiness                 |
| **Assignee coverage**  | Whether open PRs have assignees assigned             | Indicates ownership clarity for open work                       |

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

The GitHub integration automatically creates the `githubPullRequest`, `githubRepository`, `githubUser`, and `githubTeam` blueprints with default properties. The pull request blueprint comes with `status`, `createdAt`, `mergedAt`, `closedAt`, `updatedAt`, `prNumber`, `link`, `branch`, and `leadTimeHours` out of the box, along with relations for `repository`, `git_hub_creator`, `git_hub_assignees`, `git_hub_reviewers`, and a dynamic `service` relation.

We need to extend these default blueprints with additional properties for cycle time, staleness tracking, and quality indicators, then add aggregation and calculation properties to the `service` and `Team` blueprints to surface metrics at those levels.

### Update the GitHub pull request blueprint

Add properties for cycle time measurement, quality indicators, and staleness tracking to the existing `githubPullRequest` blueprint.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find the **GitHub Pull Request** blueprint and click on it.

3. Click on the `{...}` button in the top right corner, and choose **Edit JSON**.

4. Add the following properties to the `properties` section of the `schema` object (alongside the existing default properties):

   **Additional PR properties (click to expand)**

   ```
   "cycle_time_hours": {
     "title": "PR Cycle Time (Hours)",
     "type": "number",
     "description": "Time from PR creation to merge in hours"
   },
   "has_assignees": {
     "title": "Has Assignees",
     "type": "boolean",
     "description": "Whether the PR has at least one assignee"
   },
   "has_reviewers": {
     "title": "Has Reviewers",
     "type": "boolean",
     "description": "Whether the PR has at least one reviewer assigned"
   },
   "reviewDecision": {
     "title": "Review Decision",
     "type": "string"
   }
   ```

5. Add the following entry to the existing `mirrorProperties` section. This mirror traverses the `service â team` relation chain to surface the owning team's name on each PR, which the "Teams with Highest PR Throughput" bar chart uses as its breakdown property:

   **PR mirror property (click to expand)**

   ```
   "team_name": {
     "title": "Team",
     "path": "service.team.$title"
   }
   ```

6. Add the following entries to the existing `calculationProperties` section:

   **PR calculation properties (click to expand)**

   ```
   "days_old": {
     "title": "Days Old",
     "type": "number",
     "calculation": "(now / 86400) - (.properties.createdAt | capture(\"(?<date>\\\\d{4}-\\\\d{2}-\\\\d{2})\") | .date | strptime(\"%Y-%m-%d\") | mktime / 86400) | floor"
   },
   "is_stale": {
     "title": "Is Stale (7d+)",
     "type": "boolean",
     "calculation": "if .properties.status == \"open\" then ((now - (.properties.createdAt | sub(\"\\\\.[0-9]+Z$\"; \"Z\") | fromdateiso8601)) / 86400) > 7 else false end"
   },
   "pr_age_label": {
     "title": "PR Age Label",
     "type": "string",
     "calculation": "((now - (.properties.createdAt | sub(\"\\\\.[0-9]+Z$\"; \"Z\") | fromdateiso8601)) / 86400 | round) as $age | if $age <= 3 then \"0-3 days\" elif $age <= 7 then \"3-7 days\" elif $age <= 30 then \"7-30 days\" else \">30 days\" end",
     "colorized": true,
     "colors": {
       "0-3 days": "green",
       "3-7 days": "orange",
       "7-30 days": "red",
       ">30 days": "red"
     }
   }
   ```

   Existing relations

   The default `githubPullRequest` blueprint already includes relations for `repository`, `git_hub_creator`, `git_hub_assignees`, `git_hub_reviewers`, and a dynamic `service` relation. No changes to relations are needed.

7. Click **Save** to update the blueprint.

### Update the service blueprint

Add aggregation and calculation properties to the `service` blueprint so that each service displays its own PR delivery metrics.

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Find the **Service** blueprint and click on it.

3. Click on the `{...}` button in the top right corner, and choose **Edit JSON**.

4. Add the following entry to the `relations` section of the blueprint. This relation links each service to the team that owns it, enabling team-level aggregation of PR metrics through the `PR â service â team` path:

   **Service team relation (click to expand)**

   ```
   "team": {
     "title": "Team",
     "target": "_team",
     "required": false,
     "many": false
   }
   ```

5. Add the following entry to the `mirrorProperties` section of the blueprint. This mirror surfaces the parent team name on each service, allowing the dashboard to group services by their parent team in the "Service Performance Overview" table:

   **Service mirror property (click to expand)**

   ```
   "parent_team_name": {
     "title": "Parent Team",
     "path": "team.parent_team.$title"
   }
   ```

6. Add the following entries to the `aggregationProperties` section of the blueprint:

   **Service aggregation properties (click to expand)**

   ```
   "open_prs": {
     "title": "Open PRs",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "status",
           "operator": "=",
           "value": "open"
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   },
   "stale_prs_7d": {
     "title": "Stale PRs (7d)",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "status",
           "operator": "=",
           "value": "open"
         },
         {
           "property": "createdAt",
           "operator": "notBetween",
           "value": {
             "preset": "lastWeek"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   },
   "merged_prs_last_week": {
     "title": "Merged PRs (Last Week)",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "mergedAt",
           "operator": "between",
           "value": {
             "preset": "lastWeek"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   },
   "merged_prs_last_month": {
     "title": "Merged PRs (Last Month)",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "mergedAt",
           "operator": "between",
           "value": {
             "preset": "lastMonth"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   },
   "pr_cycle_time": {
     "title": "Monthly PR Cycle Time",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "mergedAt",
           "operator": "between",
           "value": {
             "preset": "lastMonth"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "average",
       "averageOf": "total",
       "calculationBy": "property",
       "property": "cycle_time_hours",
       "measureTimeBy": "$createdAt"
     }
   },
   "pr_cycle_time_weekly": {
     "title": "Weekly PR Cycle Time",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "mergedAt",
           "operator": "between",
           "value": {
             "preset": "lastWeek"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "average",
       "averageOf": "total",
       "calculationBy": "property",
       "property": "cycle_time_hours",
       "measureTimeBy": "$createdAt"
     }
   }
   ```

7. Add the following entries to the `calculationProperties` section of the blueprint:

   **Service calculation properties (click to expand)**

   ```
   "stale_pr_share_percent": {
     "title": "Stale PR Share (%)",
     "type": "number",
     "calculation": "if (.properties.open_prs != null and .properties.open_prs != 0) then (.properties.stale_prs_7d / .properties.open_prs) * 100 else 0 end"
   },
   "cycle_time_trend": {
     "title": "Cycle Time Trend",
     "type": "string",
     "colorized": true,
     "colors": {
       "Improving": "green",
       "Degrading": "red",
       "Stable": "blue"
     },
     "calculation": "((.properties.pr_cycle_time // 0) - (.properties.pr_cycle_time_weekly // 0)) as $diff | if $diff > 0 then \"Improving\" elif $diff < 0 then \"Degrading\" else \"Stable\" end"
   },
   "throughput_trend": {
     "title": "Throughput Trend",
     "type": "string",
     "colorized": true,
     "colors": {
       "Improving": "green",
       "Degrading": "red",
       "Stable": "blue"
     },
     "calculation": "((.properties.merged_prs_last_week // 0) * 30 - (.properties.merged_prs_last_month // 0) * 7) as $diff | if $diff > 0 then \"Improving\" elif $diff < 0 then \"Degrading\" else \"Stable\" end"
   }
   ```

8. Click **Save** to update the blueprint.

### Update the team blueprint

Add relations, mirror properties, and aggregation properties to the `Team` blueprint to aggregate delivery metrics across all services owned by each team. The aggregations use `pathFilter` to traverse the `PR â service â team` relation chain and compute metrics directly from pull request data.

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Find the **Team** blueprint and click on it.

3. Click on the `{...}` button in the top right corner, and choose **Edit JSON**.

4. Add the following entry to the `relations` section of the blueprint. This self-relation allows teams to be organized into a hierarchy (e.g., a "Frontend" team under an "Engineering" parent), which the dashboard uses to group team metrics by parent team:

   **Team parent relation (click to expand)**

   ```
   "parent_team": {
     "title": "Parent Team",
     "target": "_team",
     "required": false,
     "many": false
   }
   ```

5. Add the following entry to the `mirrorProperties` section of the blueprint. This mirror resolves the parent team's name so the "Team Performance" table can group rows by parent team:

   **Team mirror property (click to expand)**

   ```
   "parent_team_name": {
     "title": "Parent Team",
     "path": "parent_team.$title"
   }
   ```

6. Add the following entries to the `aggregationProperties` section of the blueprint:

   **Team aggregation properties (click to expand)**

   ```
   "services_count": {
     "title": "Services Count",
     "type": "number",
     "target": "service",
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     },
     "pathFilter": [
       {
         "fromBlueprint": "service",
         "path": ["team"]
       }
     ]
   },
   "open_prs": {
     "title": "Open PRs",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "status",
           "operator": "=",
           "value": "open"
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     },
     "pathFilter": [
       {
         "fromBlueprint": "githubPullRequest",
         "path": ["service", "team"]
       }
     ]
   },
   "stale_prs_7d": {
     "title": "Stale PRs (7d)",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "status",
           "operator": "=",
           "value": "open"
         },
         {
           "property": "createdAt",
           "operator": "notBetween",
           "value": {
             "preset": "lastWeek"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     },
     "pathFilter": [
       {
         "fromBlueprint": "githubPullRequest",
         "path": ["service", "team"]
       }
     ]
   },
   "merged_prs_last_week": {
     "title": "Merged PRs (Last Week)",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "mergedAt",
           "operator": "between",
           "value": {
             "preset": "lastWeek"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     },
     "pathFilter": [
       {
         "fromBlueprint": "githubPullRequest",
         "path": ["service", "team"]
       }
     ]
   },
   "merged_prs_last_month": {
     "title": "Merged PRs (Last Month)",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "mergedAt",
           "operator": "between",
           "value": {
             "preset": "lastMonth"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     },
     "pathFilter": [
       {
         "fromBlueprint": "githubPullRequest",
         "path": ["service", "team"]
       }
     ]
   },
   "pr_cycle_time_weekly": {
     "title": "Weekly PR Cycle Time",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "mergedAt",
           "operator": "between",
           "value": {
             "preset": "lastWeek"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "average",
       "averageOf": "total",
       "calculationBy": "property",
       "property": "cycle_time_hours",
       "measureTimeBy": "$createdAt"
     },
     "pathFilter": [
       {
         "fromBlueprint": "githubPullRequest",
         "path": ["service", "team"]
       }
     ]
   },
   "pr_cycle_time": {
     "title": "Monthly PR Cycle Time",
     "type": "number",
     "target": "githubPullRequest",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "mergedAt",
           "operator": "between",
           "value": {
             "preset": "lastMonth"
           }
         }
       ]
     },
     "calculationSpec": {
       "func": "average",
       "averageOf": "total",
       "calculationBy": "property",
       "property": "cycle_time_hours",
       "measureTimeBy": "$createdAt"
     },
     "pathFilter": [
       {
         "fromBlueprint": "githubPullRequest",
         "path": ["service", "team"]
       }
     ]
   }
   ```

7. Add the following entries to the `calculationProperties` section of the blueprint:

   **Team calculation properties (click to expand)**

   ```
   "stale_pr_share_percent": {
     "title": "Stale PR Share (%)",
     "type": "number",
     "calculation": "if (.properties.open_prs != null and .properties.open_prs != 0) then (.properties.stale_prs_7d / .properties.open_prs) * 100 else 0 end"
   },
   "cycle_time_trend": {
     "title": "Cycle Time Trend",
     "type": "string",
     "colorized": true,
     "colors": {
       "Improving": "green",
       "Degrading": "red",
       "Stable": "blue"
     },
     "calculation": "((.properties.pr_cycle_time // 0) - (.properties.pr_cycle_time_weekly // 0)) as $diff | if $diff > 0 then \"Improving\" elif $diff < 0 then \"Degrading\" else \"Stable\" end"
   },
   "throughput_trend": {
     "title": "Throughput Trend",
     "type": "string",
     "colorized": true,
     "colors": {
       "Improving": "green",
       "Degrading": "red",
       "Stable": "blue"
     },
     "calculation": "((.properties.merged_prs_last_week // 0) * 30 - (.properties.merged_prs_last_month // 0) * 7) as $diff | if $diff > 0 then \"Improving\" elif $diff < 0 then \"Degrading\" else \"Stable\" end"
   },
   "merged_prs_per_service_last_month": {
     "title": "Merged PRs per Service (Monthly)",
     "type": "number",
     "calculation": "if (.properties.services_count != null and .properties.services_count != 0) then (.properties.merged_prs_last_month / .properties.services_count) else 0 end"
   },
   "open_prs_per_service": {
     "title": "Open PRs per Service",
     "type": "number",
     "calculation": "if (.properties.services_count != null and .properties.services_count != 0) then (.properties.open_prs / .properties.services_count) else 0 end"
   },
   "stale_prs_per_service_7d": {
     "title": "Stale PRs per Service (7d)",
     "type": "number",
     "calculation": "if (.properties.services_count != null and .properties.services_count != 0) then (.properties.stale_prs_7d / .properties.services_count) else 0 end"
   }
   ```

8. Click **Save** to update the blueprint.

Relation chain

The aggregation properties on the `Team` blueprint use a `pathFilter` that traverses the relation chain `PR â service â team`. For team-level metrics to populate, each service must have its `team` relation set to the appropriate team entity.

## Update integration mapping[â](#update-integration-mapping "Direct link to Update integration mapping")

Now we'll update the GitHub integration mapping to populate the new properties we added to the pull request blueprint. The default mapping already handles `status`, `createdAt`, `mergedAt`, `closedAt`, `prNumber`, `link`, `branch`, `leadTimeHours`, and all user/repository relations. We only need to add mappings for the new fields.

1. Go to your [Data Source](https://app.getport.io/settings/data-sources) page.

2. Select the GitHub integration.

3. Find the first `pull-request` resource block in the mapping and add these additional property mappings alongside the existing ones:

   **Additional pull request property mappings (click to expand)**

   ```
   # Add these properties to the first pull-request resource mapping
   # alongside the existing properties (status, closedAt, mergedAt, etc.)
               reviewDecision: .review_decision
               cycle_time_hours: >-
                 (.created_at as $createdAt | .merged_at as $mergedAt |
                 ($createdAt | sub("\\..*Z$"; "Z") |
                 strptime("%Y-%m-%dT%H:%M:%SZ") | mktime) as
                 $createdTimestamp | ($mergedAt | if . == null then null
                 else sub("\\..*Z$"; "Z") |
                 strptime("%Y-%m-%dT%H:%M:%SZ") | mktime end) as
                 $mergedTimestamp | if $mergedTimestamp == null then null
                 else (((($mergedTimestamp - $createdTimestamp) / 3600) *
                 100 | floor) / 100) end)
               has_assignees: .assignees | length > 0
               has_reviewers: .requested_reviewers | length > 0
   ```

4. Also in the first `pull-request` resource block, set `closedPullRequests: true` in the `selector` to ensure merged and closed PRs are ingested:

   ```
     - kind: pull-request
       selector:
         query: 'true'
         closedPullRequests: true
   ```

5. Click **Save & Resync** to apply the mapping.

Closed PRs

By default, the GitHub integration only fetches open pull requests. Setting `closedPullRequests: true` ensures that merged and closed PRs are also ingested, which is required for cycle time and throughput calculations.

## Visualize metrics[â](#visualize-metrics "Direct link to Visualize metrics")

We will create a dedicated dashboard to monitor PR delivery metrics using Port's customizable widgets. The dashboard is organized into sections covering high-level metrics, service performance, team performance, stale PR analysis, and PR quality indicators.

### Create the dashboard[â](#create-the-dashboard "Direct link to Create the dashboard")

First, let's create an **Engineering Intelligence** folder to organize your dashboards, then add the **Delivery Performance** dashboard inside it:

1. Navigate to your [software catalog](https://app.getport.io/organization/catalog).
2. Click on the **`+ New`** button in the left sidebar.
3. Select **New folder**.
4. Name the folder **Engineering Intelligence** and click **Create**.
5. Inside the **Engineering Intelligence** folder, click **`+ New`** again.
6. Select **New dashboard**.
7. Name the dashboard **Delivery Performance** and click **Create**.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

You can populate the dashboard using either an API script or by manually creating each widget through the UI.

* API script
* Manual setup

The fastest way to set up the dashboard is by using Port's API to create all widgets at once.

#### Get your Port API token

1. In your Port portal, click on your **profile picture** in the bottom left corner.

2. Select **Credentials**.

3. Click **Generate API token**.

4. Copy the generated token and store it as an environment variable:

   ```
   export PORT_ACCESS_TOKEN="YOUR_GENERATED_TOKEN"
   ```

EU region

If your portal is hosted in the EU region, replace `api.port.io` with `api.port-eu.io` in the dashboard creation command below.

#### Create the dashboard with widgets

Save the following JSON to a file named `dp_dashboard.json`:

**Dashboard JSON payload (click to expand)**

```
{
  "identifier": "delivery_performance",
  "title": "Delivery Performance",
  "icon": "Apps",
  "type": "dashboard",
  "parent": "engineering_intelligence",
  "widgets": [
    {
      "id": "dpDashboardWidget",
      "type": "dashboard-widget",
      "layout": [
        {
          "height": 400,
          "columns": [
            {"id": "avgCycleTime", "size": 4},
            {"id": "prCycleTimeTrend", "size": 4},
            {"id": "prThroughputTrend", "size": 4}
          ]
        },
        {
          "height": 400,
          "columns": [
            {"id": "totalOpenPrs", "size": 4},
            {"id": "stalePrShare", "size": 4},
            {"id": "teamThroughputBar", "size": 4}
          ]
        },
        {
          "height": 400,
          "columns": [
            {"id": "servicePerformance", "size": 12}
          ]
        },
        {
          "height": 400,
          "columns": [
            {"id": "teamPerformance", "size": 12}
          ]
        },
        {
          "height": 484,
          "columns": [
            {"id": "stalePrTable", "size": 8},
            {"id": "prAgeDistribution", "size": 4}
          ]
        },
        {
          "height": 489,
          "columns": [
            {"id": "noReviewerTable", "size": 8},
            {"id": "reviewerCoverage", "size": 4}
          ]
        },
        {
          "height": 486,
          "columns": [
            {"id": "noAssigneeTable", "size": 8},
            {"id": "assigneeCoverage", "size": 4}
          ]
        },
        {
          "height": 400,
          "columns": [
            {"id": "openPrTable", "size": 12}
          ]
        }
      ],
      "widgets": [
        {
          "id": "avgCycleTime",
          "type": "entities-number-chart",
          "title": "Avg PR Cycle Time (Hours)",
          "icon": "Metric",
          "description": "Average time from PR creation to merge across all services (last month)",
          "blueprint": "githubPullRequest",
          "chartType": "aggregateByProperty",
          "calculationBy": "property",
          "func": "average",
          "property": "cycle_time_hours",
          "averageOf": "total",
          "unit": "none",
          "dataset": {
            "combinator": "and",
            "rules": [
              {"operator": "between", "property": "mergedAt", "value": {"preset": "lastMonth"}}
            ]
          }
        },
        {
          "id": "totalOpenPrs",
          "type": "entities-number-chart",
          "title": "Total open PRs",
          "icon": "Metric",
          "description": "Total number of open PRs across all services in the organisation",
          "blueprint": "githubPullRequest",
          "chartType": "countEntities",
          "calculationBy": "entities",
          "func": "count",
          "unit": "none",
          "dataset": {
            "combinator": "and",
            "rules": [
              {"property": "status", "operator": "=", "value": "open"}
            ]
          }
        },
        {
          "id": "stalePrShare",
          "type": "entities-number-chart",
          "title": "Stale PR Share (%)",
          "icon": "Metric",
          "description": "Percentage of open PRs that have been open for more than 7 days",
          "blueprint": "_team",
          "chartType": "aggregateByProperty",
          "calculationBy": "property",
          "func": "average",
          "property": "stale_pr_share_percent",
          "averageOf": "total",
          "displayFormatting": "round",
          "unit": "none",
          "dataset": {"combinator": "and", "rules": []}
        },
        {
          "id": "prCycleTimeTrend",
          "type": "line-chart",
          "title": "PR Cycle Time Trend (Monthly Trend)",
          "icon": "LineChart",
          "description": "Displays average time from PR creation to merge over time.",
          "blueprint": "githubPullRequest",
          "chartType": "aggregatePropertiesValues",
          "func": "average",
          "properties": ["properties.cycle_time_hours"],
          "measureTimeBy": "mergedAt",
          "timeInterval": "isoWeek",
          "timeRange": {"preset": "lastMonth"},
          "xAxisTitle": "Date",
          "yAxisTitle": "Cycle Time",
          "dataset": {"combinator": "and", "rules": []}
        },
        {
          "id": "prThroughputTrend",
          "type": "line-chart",
          "title": "PR Throughput (Monthly Trend)",
          "icon": "LineChart",
          "description": "Shows merged PR volume over time.",
          "blueprint": "githubPullRequest",
          "chartType": "countEntities",
          "func": "count",
          "measureTimeBy": "mergedAt",
          "timeInterval": "month",
          "timeRange": {"preset": "last6Months"},
          "xAxisTitle": "Date",
          "yAxisTitle": "PRs Merged",
          "dataset": {"combinator": "and", "rules": []}
        },
        {
          "id": "teamThroughputBar",
          "type": "bar-chart",
          "title": "Teams with Highest PR Throughput",
          "icon": "Bar",
          "description": "Number of PRs merged per team in the last 30 days",
          "blueprint": "githubPullRequest",
          "property": "mirror-property#team_name",
          "dataset": {
            "combinator": "and",
            "rules": [
              {"property": "status", "operator": "=", "value": "merged"},
              {"property": "mergedAt", "operator": "between", "value": {"preset": "lastMonth"}}
            ]
          }
        },
        {
          "id": "prAgeDistribution",
          "type": "entities-pie-chart",
          "title": "PR Age Distribution",
          "icon": "Pie",
          "description": "PRs opened for: 0-3 days | 3-7 days | 7-30 days | >30 days",
          "blueprint": "githubPullRequest",
          "property": "calculation-property#pr_age_label",
          "dataset": {
            "combinator": "and",
            "rules": [
              {"property": "status", "operator": "=", "value": "open"}
            ]
          }
        },
        {
          "id": "reviewerCoverage",
          "type": "entities-pie-chart",
          "title": "Open PR Reviewer Coverage",
          "icon": "Pie",
          "description": "Shows Open PRs with and without assigned reviewers.",
          "blueprint": "githubPullRequest",
          "property": "property#has_reviewers",
          "dataset": {
            "combinator": "and",
            "rules": [
              {"property": "status", "operator": "=", "value": "open"}
            ]
          }
        },
        {
          "id": "assigneeCoverage",
          "type": "entities-pie-chart",
          "title": "Open PR Assignment Coverage",
          "icon": "Pie",
          "description": "Shows open PRs with and without assigned owners.",
          "blueprint": "githubPullRequest",
          "property": "property#has_assignees",
          "dataset": {
            "combinator": "and",
            "rules": [
              {"property": "status", "operator": "=", "value": "open"}
            ]
          }
        },
        {
          "id": "servicePerformance",
          "type": "table-entities-explorer",
          "displayMode": "widget",
          "title": "Service Performance Overview",
          "icon": "Table",
          "description": "Delivery metrics across services",
          "blueprint": "service",
          "dataset": {"combinator": "and", "rules": []},
          "excludedFields": [],
          "blueprintConfig": {
            "service": {
              "groupSettings": {"groupBy": ["parent_team_name", "team"]},
              "propertiesSettings": {
                "order": ["team", "parent_team_name", "$icon", "$title", "delivery_performance", "pr_cycle_time", "cycle_time_trend", "merged_prs_last_month", "throughput_trend", "stale_pr_share_percent", "open_prs", "stale_prs_7d", "FROZEN_RIGHT_COLUMN"],
                "shown": ["$title", "readme", "parent_team_name", "cycle_time_trend", "stale_pr_share_percent", "throughput_trend", "merged_prs_last_month", "open_prs", "pr_cycle_time", "stale_prs_7d", "delivery_performance", "team"]
              },
              "filterSettings": {"filterBy": {"combinator": "and", "rules": []}},
              "sortSettings": {"sortBy": []}
            }
          }
        },
        {
          "id": "teamPerformance",
          "type": "table-entities-explorer",
          "displayMode": "widget",
          "title": "Team Performance",
          "icon": "Table",
          "description": "Delivery metrics aggregated per team",
          "blueprint": "_team",
          "dataset": {"combinator": "and", "rules": []},
          "excludedFields": [],
          "blueprintConfig": {
            "_team": {
              "groupSettings": {"groupBy": ["parent_team_name"]},
              "propertiesSettings": {
                "order": ["$title", "merged_prs_last_month", "throughput_trend", "pr_cycle_time", "cycle_time_trend", "stale_pr_share_percent", "open_prs", "stale_prs_7d", "services_count"],
                "shown": ["$title", "stale_pr_share_percent", "services_count", "open_prs", "stale_prs_7d", "merged_prs_last_month", "throughput_trend", "pr_cycle_time", "cycle_time_trend"]
              },
              "filterSettings": {"filterBy": {"combinator": "and", "rules": []}},
              "sortSettings": {"sortBy": []}
            }
          }
        },
        {
          "id": "stalePrTable",
          "type": "table-entities-explorer",
          "displayMode": "widget",
          "title": "Stale Pull Requests",
          "icon": "Table",
          "description": "Pull requests that have been open for more than 7 days",
          "blueprint": "githubPullRequest",
          "dataset": {"combinator": "and", "rules": []},
          "excludedFields": [],
          "blueprintConfig": {
            "githubPullRequest": {
              "groupSettings": {"groupBy": ["team_name", "service", "repository"]},
              "propertiesSettings": {
                "order": ["repository", "service", "team_name", "link", "$title", "$updatedAt", "git_hub_creator"],
                "shown": ["$updatedAt", "$title", "link", "git_hub_creator"]
              },
              "filterSettings": {
                "filterBy": {
                  "combinator": "and",
                  "rules": [
                    {"property": "is_stale", "operator": "=", "value": true}
                  ]
                }
              },
              "sortSettings": {"sortBy": []}
            }
          }
        },
        {
          "id": "openPrTable",
          "type": "table-entities-explorer",
          "displayMode": "widget",
          "title": "All Open Pull Requests",
          "icon": "Table",
          "description": "All currently open pull requests across repositories",
          "blueprint": "githubPullRequest",
          "dataset": {
            "combinator": "and",
            "rules": [
              {"property": "status", "operator": "=", "value": "open"}
            ]
          },
          "excludedFields": [],
          "blueprintConfig": {
            "githubPullRequest": {
              "groupSettings": {"groupBy": ["team_name", "service", "repository"]},
              "propertiesSettings": {
                "order": ["repository", "service", "team_name", "link", "$title", "git_hub_creator", "$updatedAt", "days_old"],
                "shown": ["$updatedAt", "$title", "has_assignees", "has_reviewers", "link", "team_name", "days_old", "is_stale", "service", "git_hub_creator"]
              },
              "filterSettings": {"filterBy": {"combinator": "and", "rules": []}},
              "sortSettings": {"sortBy": []}
            }
          }
        },
        {
          "id": "noReviewerTable",
          "type": "table-entities-explorer",
          "displayMode": "widget",
          "title": "PRs Without Assigned Reviewers",
          "icon": "Table",
          "description": "Lists pull requests that currently have no reviewers assigned.",
          "blueprint": "githubPullRequest",
          "dataset": {
            "combinator": "and",
            "rules": [
              {"property": "status", "operator": "=", "value": "open"},
              {"property": "has_reviewers", "operator": "=", "value": false}
            ]
          },
          "excludedFields": [],
          "blueprintConfig": {
            "githubPullRequest": {
              "groupSettings": {"groupBy": ["team_name", "service", "repository"]},
              "propertiesSettings": {
                "order": ["repository", "service", "team_name", "link", "$title", "git_hub_creator", "$updatedAt", "days_old"],
                "shown": ["$updatedAt", "$title", "link", "days_old", "git_hub_creator"]
              },
              "filterSettings": {"filterBy": {"combinator": "and", "rules": []}},
              "sortSettings": {"sortBy": [{"property": "$identifier", "order": "asc"}]}
            }
          }
        },
        {
          "id": "noAssigneeTable",
          "type": "table-entities-explorer",
          "displayMode": "widget",
          "title": "PRs Without Assignees",
          "icon": "Table",
          "description": "Lists pull requests that currently have no assignees assigned.",
          "blueprint": "githubPullRequest",
          "dataset": {
            "combinator": "and",
            "rules": [
              {"property": "status", "operator": "=", "value": "open"},
              {"property": "has_assignees", "operator": "=", "value": false}
            ]
          },
          "excludedFields": [],
          "blueprintConfig": {
            "githubPullRequest": {
              "groupSettings": {"groupBy": ["team_name", "service", "repository"]},
              "propertiesSettings": {
                "order": ["repository", "service", "team_name", "$icon", "link", "$title", "git_hub_creator", "$updatedAt", "days_old", "FROZEN_RIGHT_COLUMN"],
                "shown": ["$updatedAt", "$title", "link", "days_old", "git_hub_creator"]
              },
              "filterSettings": {"filterBy": {"combinator": "and", "rules": []}},
              "sortSettings": {"sortBy": [{"property": "$identifier", "order": "asc"}]}
            }
          }
        }
      ]
    }
  ]
}
```

Then run the following command to create the dashboard with all widgets:

```
curl -s -X POST "https://api.port.io/v1/pages" \
  -H "Authorization: Bearer $PORT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d @dp_dashboard.json | python3 -m json.tool
```

Engineering Intelligence folder

The script assumes an `engineering_intelligence` folder already exists in your catalog. If you haven't created it yet, follow step 1-4 in the [create the dashboard](#create-the-dashboard) section first else you will run into an error when you run the script

#### High-level PR metrics

Start with summary widgets that give an at-a-glance view of PR delivery health.

**Avg PR cycle time (hours) (click to expand)**

1. Click **`+ Widget`** and select **Number Chart**.

2. Title: `Avg PR Cycle Time (Hours)`.

3. Description: `Average time from PR creation to merge across all services`.

4. Select `Aggregate Property (All Entities)` **Chart type** and choose **GitHub Pull Request** as the **Blueprint**.

5. Select `cycle_time_hours` as the **Property**.

6. Select `average` for the **Function**.

7. Select `total` for **Average of**.

8. Add this JSON to the **Additional filters** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "mergedAt",
         "operator": "between",
         "value": {
           "preset": "lastMonth"
         }
       }
     ]
   }
   ```

9. Select `custom` as the **Unit** and input `hours` as the **Custom unit**.

10. Click **Save**.

**PR cycle time trend (monthly) (click to expand)**

1. Click **`+ Widget`** and select **Line Chart**.
2. Title: `PR Cycle Time Trend (Monthly Trend)`.
3. Description: `Displays average time from PR creation to merge over time`.
4. Select `Aggregate Property (All Entities)` **Chart type** and choose **GitHub Pull Request** as the **Blueprint**.
5. Input `Cycle Time` as the **Y axis** **Title**.
6. Select `average` for the **Function**.
7. Select `PR cycle time (hours)` as the **Property**.
8. Input `Date` as the **X axis** **Title**.
9. Select `mergedAt` for **Measure time by**.
10. Set **Time Interval** to `Week` and **Time Range** to `In the past 30 days`.
11. Click **Save**.

**PR throughput (monthly trend) (click to expand)**

1. Click **`+ Widget`** and select **Line Chart**.
2. Title: `PR Throughput (Monthly Trend)`.
3. Description: `Shows merged PR volume over time`.
4. Select `Count Entities (All Entities)` **Chart type** and choose **GitHub Pull Request** as the **Blueprint**.
5. Input `PRs Merged` as the **Y axis** **Title**.
6. Select `count` for the **Function**.
7. Input `Date` as the **X axis** **Title**.
8. Select `mergedAt` for **Measure time by**.
9. Set **Time Interval** to `month` and **Time Range** to `In the past 180 days`.
10. Click **Save**.

**Total open PRs (click to expand)**

1. Click **`+ Widget`** and select **Number Chart**.

2. Title: `Total open PRs`.

3. Description: `Total number of open PRs across all services in the organisation`.

4. Select `Count entities` **Chart type** and choose **GitHub Pull Request** as the **Blueprint**.

5. Select `count` for the **Function**.

6. Add this JSON to the **Dataset filter** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "status",
         "operator": "=",
         "value": "open"
       }
     ]
   }
   ```

7. Click **Save**.

**Stale PR share (%) (click to expand)**

1. Click **`+ Widget`** and select **Number Chart**.
2. Title: `Stale PR Share (%)`.
3. Description: `Percentage of open PRs that have been open for more than 7 days`.
4. Select `Aggregate Property (All Entities)` **Chart type** and choose **Team** as the **Blueprint**.
5. Select `Stale PR Share (%)` as the **Property**.
6. Select `average` for the **Function**.
7. Select `total` for **Average of**.
8. Select `custom` as the **Unit** and input `%` as the **unit** and align the unit to the right.
9. Click **Save**.

**Teams with highest PR throughput (click to expand)**

1. Click **`+ Widget`** and select **Bar Chart**.

2. Title: `Teams with Highest PR Throughput`.

3. Description: `Number of PRs merged per team in the last 30 days`.

4. Select **GitHub Pull Request** as the **Blueprint**.

5. Select `Team` as the **Breakdown by property**.

6. Add this JSON to the **Additional filters** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "value": "merged",
         "property": "status",
         "operator": "="
       },
       {
         "property": "mergedAt",
         "operator": "between",
         "value": {
           "preset": "lastMonth"
         }
       }
     ]
   }
   ```

7. Click **Save**.

![](/img/guides/pr-delivery-metrics-dashboard-1.png)

#### Service performance

Track delivery metrics at the individual service level using a table that aggregates key PR metrics per service.

**Service performance overview (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `Service Performance Overview`.

3. Description: `Delivery metrics across services`.

4. Choose the **Service** blueprint.

5. Click **Save**.

6. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

7. In the top right corner of the table, click on **Manage Properties** and add the following columns:

   <!-- -->

   * **Parent Team**: The parent team of the service's owning team.
   * **Team**: The team that owns the service.
   * **Title**: The service name.
   * **Delivery Performance**: The delivery performance scorecard level.
   * **Monthly PR Cycle Time** (`pr_cycle_time`): Average cycle time across PRs in the last month.
   * **Cycle Time Trend** (`cycle_time_trend`): Sparkline showing cycle time direction.
   * **Monthly PR Throughput** (`merged_prs_last_month`): Number of PRs merged in the last 30 days.
   * **Throughput Trend** (`throughput_trend`): Sparkline showing throughput direction.
   * **Stale PR Share (%)** (`stale_pr_share_percent`): Percentage of open PRs that are stale.
   * **Open PRs** (`open_prs`): Number of currently open PRs.

8. Select `parent_team_name` and `team` as the **Group by** column.

9. Click on the **save icon** in the top right corner of the widget to save the customized table.

#### Team performance

Aggregate delivery metrics at the team level to compare performance across teams.

**Team performance (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `Team Performance`.

3. Description: `Delivery metrics aggregated per team`.

4. Choose the **Team** blueprint.

5. Click **Save**.

6. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

7. In the top right corner of the table, click on **Manage Properties** and add the following columns:

   <!-- -->

   * **Parent Team**: The parent team of the team.
   * **Title**: The team name.
   * **Monthly PR Throughput** (`merged_prs_last_month`): Number of PRs merged in the last 30 days.
   * **Throughput Trend** (`throughput_trend`): Whether throughput is improving, degrading, or stable.
   * **Monthly PR Cycle Time** (`pr_cycle_time`): Average PR cycle time for the last month.
   * **Cycle Time Trend** (`cycle_time_trend`): Whether cycle time is improving, degrading, or stable.
   * **Stale PR Share (%)** (`stale_pr_share_percent`): Percentage of open PRs that are stale.
   * **Open PRs** (`open_prs`): Number of currently open PRs.
   * **Stale PRs (7d+)** (`stale_prs_7d`): Number of PRs open longer than 7 days.
   * **Number of Services** (`services_count`): Number of services owned by the team.

8. Select `parent_team_name` as the **Group by** column.

9. Click on the **save icon** in the top right corner of the widget to save the customized table.

![](/img/guides/pr-delivery-metrics-dashboard-2.png)

#### Stale PR analysis

Surface PRs that have been open too long and understand the age distribution across your organization.

**Stale pull requests table (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `Stale Pull Requests`.

3. Description: `Pull requests that have been open for more than 7 days`.

4. Choose the **GitHub Pull Request** blueprint.

5. Click **Save**.

6. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

7. In the top right corner of the table, click on **Manage Properties** and add the following columns:

   <!-- -->

   * **Team**: The owning team (via `team_name` mirror property).
   * **Service**: The related service.
   * **Repository**: The related repository.
   * **Link**: The URL to the pull request.
   * **Title**: The PR title.
   * **Last Update**: The last updated date.
   * **Creator**: The PR creator.

8. Select `team_name`, `service` and `repository` as the **Group by** columns.

9. On the filter section, select the `is_stale` property and set the operator to `=` and the value to `true`.

10. Click on the **save icon** in the top right corner of the widget to save the customized table.

**PR age distribution (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `PR Age Distribution`.

3. Description: `PRs opened for: 0-3 days | 3-7 days | 7-30 days | >30 days`.

4. Choose the **GitHub Pull Request** blueprint.

5. Under **Breakdown by property**, select the `PR Age` property.

6. Add this JSON to the **Additional filters** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "status",
         "operator": "=",
         "value": "open"
       }
     ]
   }
   ```

7. Click **Save**.

![](/img/guides/pr-delivery-metrics-dashboard-3.png)

#### PR quality indicators

Track whether open PRs have proper reviewer and assignee coverage, which are key indicators of process health.

**PRs without assigned reviewers (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `PRs Without Assigned Reviewers`.

3. Description: `Lists pull requests that currently have no reviewers assigned`.

4. Choose the **GitHub Pull Request** blueprint.

5. Add this JSON to the **Initial filters** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "status",
         "operator": "=",
         "value": "open"
       },
       {
         "property": "has_reviewers",
         "operator": "=",
         "value": false
       }
     ]
   }
   ```

6. Click **Save**.

7. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

8. In the top right corner of the table, click on **Manage Properties** and add the following columns:

   * **Team**: The owning team.
   * **Service**: The related service.
   * **Repository**: The related repository.
   * **Link**: The URL to the pull request.
   * **Title**: The PR title.
   * **Creator**: The PR creator.
   * **Last Update**: The last updated date.

9. Select `team_name`, `service` and `repository` as the **Group by** columns.

10. Click on the **save icon** in the top right corner of the widget to save the customized table.

**Open PR reviewer coverage (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Open PR Reviewer Coverage`.

3. Description: `Shows Open PRs with and without assigned reviewers`.

4. Choose the **GitHub Pull Request** blueprint.

5. Under **Breakdown by property**, select the `has_reviewers` property.

6. Add this JSON to the **Additional filters** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "status",
         "operator": "=",
         "value": "open"
       }
     ]
   }
   ```

7. Click **Save**.

**PRs without assignees (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `PRs Without Assignees`.

3. Description: `Lists pull requests that currently have no assignees assigned`.

4. Choose the **GitHub Pull Request** blueprint.

5. Add this JSON to the **Initial filters** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "status",
         "operator": "=",
         "value": "open"
       },
       {
         "property": "has_assignees",
         "operator": "=",
         "value": false
       }
     ]
   }
   ```

6. Click **Save**.

7. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

8. In the top right corner of the table, click on **Manage Properties** and add the following columns:

   * **Team**: The owning team.
   * **Service**: The related service.
   * **Repository**: The related repository.
   * **Link**: The URL to the pull request.
   * **Title**: The PR title.
   * **Creator**: The PR creator.
   * **Last Update**: The last updated date.

9. Select `team_name`, `service` and `repository` as the **Group by** columns.

10. Click on the **save icon** in the top right corner of the widget to save the customized table.

**Open PR assignment coverage (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Open PR Assignment Coverage`.

3. Description: `Shows open PRs with and without assigned owners`.

4. Choose the **GitHub Pull Request** blueprint.

5. Under **Breakdown by property**, select the `has_assignees` property.

6. Add this JSON to the **Additional filters** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "status",
         "operator": "=",
         "value": "open"
       }
     ]
   }
   ```

7. Click **Save**.

**All open pull requests (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `All Open Pull Requests`.

3. Description: `All currently open pull requests across repositories`.

4. Choose the **GitHub Pull Request** blueprint.

5. Add this JSON to the **Initial filters** editor:

   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "status",
         "operator": "=",
         "value": "open"
       }
     ]
   }
   ```

6. Click **Save**.

7. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

8. In the top right corner of the table, click on **Manage Properties** and add the following columns:

   * **Team**: The owning team.
   * **Service**: The related service.
   * **Repository**: The related repository.
   * **Link**: The URL to the pull request.
   * **Title**: The PR title.
   * **Creator**: The PR creator.
   * **Last Update**: The last updated date.
   * **Days Old** (`days_old`): How many days the PR has been open.
   * **Has assignees** (`has_assignees`): Whether the PR has assignees.
   * **Has reviewers** (`has_reviewers`): Whether the PR has reviewers.
   * **Is Stale (7d+)** (`is_stale`): Whether the PR has been open for more than 7 days.

9. Select `team_name`, `service` and `repository` as the **Group by** columns.

10. Click on the **save icon** in the top right corner of the widget to save the customized table.

![](/img/guides/pr-delivery-metrics-dashboard-4.png)

## Next steps[â](#next-steps "Direct link to Next steps")

Once your Delivery Performance dashboard is in place, consider these additional improvements:

* **Set up scorecards** to automatically evaluate services and teams against delivery performance targets.
* **Create automations** to send Slack notifications when stale PR share exceeds a threshold or when PRs have been open without reviewers for more than 48 hours.
* **Add an AI agent** to provide natural language insights into your delivery data. See the [delivery performance guide](/guides/all/measure-and-track-delivery-performance.md) for configuration details.

## Related guides[â](#related-guides "Direct link to Related guides")

* [Gain visibility into delivery performance](/guides/all/measure-and-track-delivery-performance.md)
* [Measure delivery reliability and stability](/guides/all/measure-reliability-and-stability.md)
* [Track standards adherence](/guides/all/measure-standards.md)
