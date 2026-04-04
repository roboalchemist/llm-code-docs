# Source: https://docs.port.io/guides/all/measure-sprint-health-with-jira.md

# Measure sprint health with Jira

This guide walks you through measuring and visualizing sprint health at the team level. You will learn how to ingest sprint data from Jira issues, define sprint health metrics like completion rate and scope change, roll those metrics up to teams using aggregation properties, build trend visualizations, and enforce maturity standards with a scorecard.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Track delivery predictability**: Measure how consistently teams complete planned sprint work.
* **Detect scope creep**: Surface teams where mid-sprint additions are undermining planning.
* **Reduce carryover**: Identify teams that routinely carry unfinished work into the next sprint.
* **Drive continuous improvement**: Use maturity levels to encourage teams toward healthier sprint practices.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [Jira integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/) is installed and syncing issues.
* You have identified the custom field ID for the Sprint field in your Jira instance (see [ingesting sprint data](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/#ingesting-sprint-field-for-issue-kind)).

## Understanding sprint health metrics[â](#understanding-sprint-health-metrics "Direct link to Understanding sprint health metrics")

Before configuring Port, let's define the three metrics that form the foundation of sprint health measurement:

| Metric              | What it measures                                                               | Formula                                                                |
| ------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Completion rate** | Percentage of sprint-committed issues that were resolved by sprint end.        | `(issues done in sprint / total issues in sprint) Ã 100`               |
| **Scope change %**  | Percentage of issues added to the sprint after it started.                     | `(issues added mid-sprint / total issues in sprint) Ã 100`             |
| **Carryover rate**  | Percentage of issues carried from the previous sprint without being completed. | `(unresolved issues from prior sprint / total issues in sprint) Ã 100` |

A healthy sprint typically shows a high completion rate (>90%), low scope change (<10%), and low carryover (<10%).

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

We will extend the Jira issue blueprint with sprint-related fields and then add aggregation properties to the `_team` blueprint to roll up sprint health metrics.

### Extend the Jira issue blueprint[â](#extend-the-jira-issue-blueprint "Direct link to Extend the Jira issue blueprint")

Add properties that capture sprint context for each issue. These fields let us distinguish between issues that were planned, added mid-sprint, or carried over.

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Search for the `Jira Issue` blueprint and click on it.

3. Click on the `...` button in the top right corner, and choose `{...} Edit JSON`.

4. Merge the following properties into the `properties` object of your existing blueprint:

   **Sprint health properties for Jira issue (click to expand)**

   ```
   "sprint": {
     "title": "Sprint",
     "type": "string",
     "description": "The name of the current or most recent sprint for this issue"
   },
   "sprintState": {
     "title": "Sprint State",
     "type": "string",
     "enum": ["active", "closed", "future"],
     "description": "Whether the sprint is active, closed, or planned"
   },
   "storyPoints": {
     "title": "Story Points",
     "type": "number",
     "description": "The estimated effort for this issue"
   },
   "addedMidSprint": {
     "title": "Added Mid-Sprint",
     "type": "boolean",
     "description": "Whether this issue was added after the sprint started"
   },
   "carriedOver": {
     "title": "Carried Over",
     "type": "boolean",
     "description": "Whether this issue was carried from a previous sprint"
   }
   ```

5. Click `Save` to update the blueprint.

### Add a team relation to Jira issues[â](#add-a-team-relation-to-jira-issues "Direct link to Add a team relation to Jira issues")

To roll up sprint metrics per team, we need a relation from `Jira Issue` to the `_team` blueprint. If your issues already have a team relation (for example, via the assignee's team), you can skip this step.

1. In the `Jira Issue` blueprint, click on the `...` button in the top right corner, and choose `{...} Edit JSON`.

2. Add the following to the `relations` object:

   ```
   "team": {
     "target": "_team",
     "title": "Team",
     "description": "The team responsible for this issue",
     "required": false,
     "many": false
   }
   ```

3. Click `Save`.

### Add aggregation properties to the team blueprint[â](#add-aggregation-properties-to-the-team-blueprint "Direct link to Add aggregation properties to the team blueprint")

Now we will add [aggregation properties](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/aggregation-property) to the `_team` blueprint to compute sprint health metrics from the related Jira issues.

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Search for the `Team` blueprint (`_team`) and click on it.

3. Click on the `...` button in the top right corner, and choose `{...} Edit JSON`.

4. Add the following aggregation properties:

   **Sprint health aggregation properties (click to expand)**

   ```
   "sprintIssuesTotal": {
     "title": "Sprint Issues (Total)",
     "icon": "DefaultProperty",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "sprintState",
           "operator": "=",
           "value": "active"
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   },
   "sprintIssuesDone": {
     "title": "Sprint Issues (Done)",
     "icon": "DefaultProperty",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "sprintState",
           "operator": "=",
           "value": "active"
         },
         {
           "property": "status",
           "operator": "=",
           "value": "Done"
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   },
   "sprintIssuesAddedMidSprint": {
     "title": "Sprint Issues (Added Mid-Sprint)",
     "icon": "DefaultProperty",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "sprintState",
           "operator": "=",
           "value": "active"
         },
         {
           "property": "addedMidSprint",
           "operator": "=",
           "value": true
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   },
   "sprintIssuesCarriedOver": {
     "title": "Sprint Issues (Carried Over)",
     "icon": "DefaultProperty",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "sprintState",
           "operator": "=",
           "value": "active"
         },
         {
           "property": "carriedOver",
           "operator": "=",
           "value": true
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   },
   "sprintStoryPointsTotal": {
     "title": "Sprint Story Points (Total)",
     "icon": "DefaultProperty",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "sprintState",
           "operator": "=",
           "value": "active"
         }
       ]
     },
     "calculationSpec": {
       "func": "sum",
       "calculationBy": "property",
       "property": "storyPoints"
     }
   },
   "sprintStoryPointsDone": {
     "title": "Sprint Story Points (Done)",
     "icon": "DefaultProperty",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "sprintState",
           "operator": "=",
           "value": "active"
         },
         {
           "property": "status",
           "operator": "=",
           "value": "Done"
         }
       ]
     },
     "calculationSpec": {
       "func": "sum",
       "calculationBy": "property",
       "property": "storyPoints"
     }
   }
   ```

5. Click `Save`.

### Add calculation properties for percentages[â](#add-calculation-properties-for-percentages "Direct link to Add calculation properties for percentages")

Aggregation properties give us the raw counts. To turn them into percentages, add [calculation properties](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/calculation-property/) to the `_team` blueprint:

1. In the `Team` blueprint JSON, click on the `...` button in the top right corner, and choose `{...} Edit JSON`. Then add the following to the `calculationProperties` object:

   **Sprint health calculation properties (click to expand)**

   ```
   "sprintCompletionRate": {
     "title": "Sprint Completion Rate (%)",
     "icon": "Star",
     "type": "number",
     "calculation": "if .properties.sprintIssuesTotal > 0 then ((.properties.sprintIssuesDone / .properties.sprintIssuesTotal) * 100 | floor) else null end"
   },
   "sprintScopeChangePercent": {
     "title": "Sprint Scope Change (%)",
     "icon": "Alert",
     "type": "number",
     "calculation": "if .properties.sprintIssuesTotal > 0 then ((.properties.sprintIssuesAddedMidSprint / .properties.sprintIssuesTotal) * 100 | floor) else null end"
   },
   "sprintCarryoverRate": {
     "title": "Sprint Carryover Rate (%)",
     "icon": "Clock",
     "type": "number",
     "calculation": "if .properties.sprintIssuesTotal > 0 then ((.properties.sprintIssuesCarriedOver / .properties.sprintIssuesTotal) * 100 | floor) else null end"
   }
   ```

2. Click `Save`.

## Set up data source mapping[â](#set-up-data-source-mapping "Direct link to Set up data source mapping")

Update your Jira integration mapping to populate the new sprint health fields. The mapping uses the Jira sprint custom field to extract sprint name, state, and derived flags for mid-sprint additions and carryover.

1. Go to your [Data Sources](https://app.getport.io/settings/data-sources) page.

2. Select your Jira integration.

3. Update the `issue` resource mapping to include the sprint health properties:

   **Issue mapping with sprint health fields (click to expand)**

   ```
   - kind: issue
     selector:
       query: "true"
       jql: "sprint is not EMPTY AND ((statusCategory != Done) OR (updated >= -4w))"
     port:
       entity:
         mappings:
           identifier: .key
           title: .fields.summary
           blueprint: '"jiraIssue"'
           properties:
             url: (.self | split("/") | .[:3] | join("/")) + "/browse/" + .key
             status: .fields.status.name
             issueType: .fields.issuetype.name
             components: .fields.components
             creator: .fields.creator.emailAddress
             priority: .fields.priority.name
             labels: .fields.labels
             created: .fields.created
             updated: .fields.updated
             sprint: .fields.customfield_XXXXX[-1].name // ""
             sprintState: .fields.customfield_XXXXX[-1].state // null
             storyPoints: .fields.customfield_YYYYY // null
             addedMidSprint: >-
               (
                 (.fields.customfield_XXXXX[-1].startDate // null) as $start |
                 if $start != null then
                   ((.fields.created[0:19] + "Z" | fromdateiso8601) > ($start[0:19] + "Z" | fromdateiso8601))
                 else false end
               )
             carriedOver: >-
               (
                 (.fields.customfield_XXXXX | length) as $count |
                 if $count > 1 then
                   (.fields.customfield_XXXXX[-2].state == "closed"
                     and (.fields.status.statusCategory.key != "done"))
                 else false end
               )
           relations:
             project: .fields.project.key
             parentIssue: .fields.parent.key
             subtasks: .fields.subtasks | map(.key)
             team: .fields.customfield_ZZZZZ.value // null
   ```

   Replace custom field IDs

   * Replace `customfield_XXXXX` with your Sprint field ID.
   * Replace `customfield_YYYYY` with your Story Points field ID.
   * Replace `customfield_ZZZZZ` with the field you use to assign teams (e.g. a custom "Team" field, or derive it from the assignee). Adjust the jq expression to match your Jira schema.

4. Click `Save & Resync`.

After the resync completes, each team entity will display its sprint health metrics automatically.

## Set up scorecard[â](#set-up-scorecard "Direct link to Set up scorecard")

Before building the dashboard, we will create a [scorecard](https://docs.port.io/promote-scorecards/) on the `_team` blueprint to assign maturity levels based on sprint health metrics. Setting this up first lets us include scorecard results in the dashboard widgets.

The levels reflect increasing discipline in sprint planning and execution:

| Level      | Criteria                                           |
| ---------- | -------------------------------------------------- |
| **Basic**  | Default level for all teams (no rules passed yet). |
| **Bronze** | Team has sprint data and completion rate > 60%.    |
| **Silver** | Completion rate > 75% and scope change < 20%.      |
| **Gold**   | Completion rate > 90% and scope change < 10%.      |

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Search for the `Team` (`_team`) blueprint and select it.

3. Click on the **Scorecards** tab.

4. Click on `+ New Scorecard`.

5. Click on the `...` button in the top right corner, and choose `{...} Edit JSON` and paste this JSON configuration:

   **Sprint health scorecard (click to expand)**

   ```
   {
     "identifier": "sprintHealth",
     "title": "Sprint Health",
     "levels": [
       {
         "color": "paleBlue",
         "title": "Basic"
       },
       {
         "color": "bronze",
         "title": "Bronze"
       },
       {
         "color": "silver",
         "title": "Silver"
       },
       {
         "color": "gold",
         "title": "Gold"
       }
     ],
     "rules": [
       {
         "identifier": "hasSprintData",
         "title": "Has sprint data",
         "description": "The team has at least one issue associated with an active sprint",
         "level": "Bronze",
         "query": {
           "combinator": "and",
           "conditions": [
             {
               "property": "sprintIssuesTotal",
               "operator": ">",
               "value": 0
             }
           ]
         }
       },
       {
         "identifier": "completionAbove60",
         "title": "Completion rate above 60%",
         "description": "At least 60% of sprint issues are completed",
         "level": "Bronze",
         "query": {
           "combinator": "and",
           "conditions": [
             {
               "property": "sprintCompletionRate",
               "operator": ">",
               "value": 60
             }
           ]
         }
       },
       {
         "identifier": "completionAbove75",
         "title": "Completion rate above 75%",
         "description": "At least 75% of sprint issues are completed",
         "level": "Silver",
         "query": {
           "combinator": "and",
           "conditions": [
             {
               "property": "sprintCompletionRate",
               "operator": ">",
               "value": 75
             }
           ]
         }
       },
       {
         "identifier": "scopeChangeBelow20",
         "title": "Scope change below 20%",
         "description": "Fewer than 20% of sprint issues were added after the sprint started",
         "level": "Silver",
         "query": {
           "combinator": "and",
           "conditions": [
             {
               "property": "sprintScopeChangePercent",
               "operator": "<",
               "value": 20
             }
           ]
         }
       },
       {
         "identifier": "completionAbove90",
         "title": "Completion rate above 90%",
         "description": "At least 90% of sprint issues are completed",
         "level": "Gold",
         "query": {
           "combinator": "and",
           "conditions": [
             {
               "property": "sprintCompletionRate",
               "operator": ">",
               "value": 90
             }
           ]
         }
       },
       {
         "identifier": "scopeChangeBelow10",
         "title": "Scope change below 10%",
         "description": "Fewer than 10% of sprint issues were added after the sprint started",
         "level": "Gold",
         "query": {
           "combinator": "and",
           "conditions": [
             {
               "property": "sprintScopeChangePercent",
               "operator": "<",
               "value": 10
             }
           ]
         }
       }
     ]
   }
   ```

6. Click `Save`.

After the scorecard evaluates, each team entity will display its sprint health maturity level. Teams can view their level in the **Scorecards** tab on their entity page and track progress toward higher levels.

## Visualize sprint metrics[â](#visualize-sprint-metrics "Direct link to Visualize sprint metrics")

With sprint metrics and scorecard levels in place, let's build a team-level dashboard that surfaces the three core sprint health indicators i.e. **completion rate**, **scope change %**, and **carryover rate** alongside scorecard maturity levels.

![](/img/guides/sprint-health-dashboard.png)

### Create the dashboard[â](#create-the-dashboard "Direct link to Create the dashboard")

1. Navigate to the [Catalog](https://app.getport.io/organization/catalog) page.
2. Click on the **`+`** button in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard **Sprint Health**.
5. Set the description to `Track sprint delivery metrics across teams`.
6. Select the `Jira` icon.
7. Click `Create`.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

##### Add high-level summary widgets

These widgets give a high-level picture of where teams stand right now.

**Scorecard maturity distribution (click to expand)**

Shows how many teams are at each maturity level (Basic, Bronze, Silver, Gold).

1. Click `+ Widget` and select **Pie Chart**.
2. Title: `Sprint health maturity`.
3. Choose the **Team** (`_team`) blueprint.
4. Under `Breakdown by property`, select the **Sprint Health** scorecard level.
5. Click `Save`.

**Average completion rate (click to expand)**

A single number showing the organization-wide average sprint completion rate, with color thresholds aligned to the scorecard levels.

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Avg completion rate`.
3. Select `Aggregate by property` as the chart type.
4. Choose the **Team** (`_team`) blueprint.
5. Select `Sprint Completion Rate (%)` for the **Property**.
6. Set the **Function** to `average`.
7. Select `total` for **Average of**.
8. Select `Round` for **Display formatting**.
9. Select `custom` as the **Unit** and input `%` as the custom unit.
10. Add a condition: operator `>=`, value `90`, color `green`, message `Gold`.
11. Add a condition: operator `>=`, value `75`, color `blue`, message `Silver`.
12. Add a condition: operator `>=`, value `60`, color `orange`, message `Bronze`.
13. Add a condition: operator `<`, value `60`, color `red`, message `Below target`.
14. Click `Save`.

**Average scope change (click to expand)**

A single number showing the organization-wide average mid-sprint scope change.

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Avg scope change`.
3. Select `Aggregate by property` as the chart type.
4. Choose the **Team** (`_team`) blueprint.
5. Select `Sprint Scope Change (%)` for the **Property**.
6. Set the **Function** to `average`.
7. Select `total` for **Average of**.
8. Select `Round` for **Display formatting**.
9. Select `custom` as the **Unit** and input `%` as the custom unit.
10. Add a condition: operator `<`, value `10`, color `green`, message `Gold`.
11. Add a condition: operator `<`, value `20`, color `blue`, message `Silver`.
12. Add a condition: operator `>=`, value `20`, color `red`, message `High scope change`.
13. Click `Save`.

**Average carryover rate (click to expand)**

A single number showing how much unfinished work is carried between sprints.

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Avg carryover rate`.
3. Select `Aggregate by property` as the chart type.
4. Choose the **Team** (`_team`) blueprint.
5. Select `Sprint Carryover Rate (%)` for the **Property**.
6. Set the **Function** to `average`.
7. Select `total` for **Average of**.
8. Select `Round` for **Display formatting**.
9. Select `custom` as the **Unit** and input `%` as the custom unit.
10. Add a condition: operator `<=`, value `10`, color `green`, message `Healthy`.
11. Add a condition: operator `>`, value `20`, color `red`, message `High carryover`.
12. Click `Save`.

#### Add per-sprint trend widgets

These line charts track how each metric evolves over time, making it easy to spot regressions or improvements sprint over sprint.

**Completion rate trend (click to expand)**

Tracks the completion rate for all teams over successive sprints.

1. Click `+ Widget` and select **Line Chart**.

2. Title: `Completion rate trend`.

3. Select **Aggregate property (all entities)** as the chart type.

4. Choose the **Team** (`_team`) blueprint.

5. Under the **Y axis**:

   <!-- -->

   * Title: `Completion rate (%)`.
   * Set the aggregation function to `average`.

6. Under the **X axis**:

   <!-- -->

   * Title: `Sprint`.
   * Measure time by `$updatedAt`.
   * Set the time interval to `Week` (or match your sprint cadence).
   * Set the time range to `Last 180 days`.

7. Click `Save`.

**Scope change trend (click to expand)**

Shows how mid-sprint scope change evolves across all teams over time.

1. Click `+ Widget` and select **Line Chart**.

2. Title: `Scope change trend`.

3. Select **Aggregate property (all entities)** as the chart type.

4. Choose the **Team** (`_team`) blueprint.

5. Under the **Y axis**:

   <!-- -->

   * Title: `Scope change (%)`.
   * Choose the `Sprint Scope Change (%)` property.
   * Set the aggregation function to `average`.

6. Under the **X axis**:

   <!-- -->

   * Title: `Time`.
   * Measure time by `$updatedAt`.
   * Set the time interval to `Week`.
   * Set the time range to `Last 3 months`.

7. Click `Save`.

**Carryover rate trend (click to expand)**

Shows whether carryover is improving or worsening across teams over time.

1. Click `+ Widget` and select **Line Chart**.

2. Title: `Carryover rate trend`.

3. Select **Aggregate property (all entities)** as the chart type.

4. Choose the **Team** (`_team`) blueprint.

5. Under the **Y axis**:

   <!-- -->

   * Title: `Carryover rate (%)`.
   * Choose the `Sprint Carryover Rate (%)` property.
   * Set the aggregation function to `average`.

6. Under the **X axis**:

   <!-- -->

   * Title: `Time`.
   * Measure time by `$updatedAt`.
   * Set the time interval to `Week`.
   * Set the time range to `Last 3 months`.

7. Click `Save`.

#### Add team comparison widgets

These widgets let you compare teams side by side and drill into the active sprint.

**Sprint issues by status (click to expand)**

A breakdown of all active sprint issues by their current status, showing how much work is done, in progress, or not yet started.

1. Click `+ Widget` and select **Pie Chart**.
2. Title: `Sprint issue status`.
3. Choose the **Jira Issue** blueprint.
4. Under `Breakdown by property`, select **Status**.
5. Add this filter to scope to the active sprint:
   <!-- -->
   ```
   [
     {
       "combinator": "and",
       "rules": [
         {
           "property": "sprintState",
           "operator": "=",
           "value": "active"
         }
       ]
     }
   ]
   ```
6. Click `Save`.

**Team sprint health table (click to expand)**

A comparison table showing every team's scorecard level and all three sprint health metrics in one view.

1. Click `+ Widget` and select **Table**.

2. Title: `Team sprint health`.

3. Choose the **Team** (`_team`) blueprint.

4. Click `Save`, then click the `...` button on the widget and select **Customize table**.

5. Click `Manage Properties` and add:

   <!-- -->

   * **Sprint Health** (scorecard level).
   * **Sprint Completion Rate (%)**.
   * **Sprint Scope Change (%)**.
   * **Sprint Carryover Rate (%)**.
   * **Sprint Issues (Total)**.
   * **Sprint Issues (Done)**.
   * **Sprint Story Points (Total)**.
   * **Sprint Story Points (Done)**.

6. Click the **save icon** to persist the table layout.

## Next steps[â](#next-steps "Direct link to Next steps")

* **Set up automations**: Use Port [automations](https://docs.port.io/actions-and-automations/define-automations/) to send Slack notifications when a team's sprint health drops below a threshold.
* **Compare across teams**: Use the [dashboard table widget](https://docs.port.io/customize-pages-dashboards-and-plugins/dashboards/data-widgets/#table) with sorting and grouping to benchmark teams against each other.
* **Track story points alongside issue counts**: Use the story point aggregation properties already configured to create a parallel set of story-point-based completion metrics for teams that estimate with points.
