# Source: https://docs.port.io/guides/all/visualize-jira-lead-time.md

# Visualize lead time using Jira

This guide demonstrates how to track and visualize Jira lead time metrics in Port. Lead time measures the duration from when an issue is created until it reaches a "Done" state, giving you a clear signal of how quickly your teams deliver work.

By the end of this guide, you will have:

* A **calculation property** on each Jira issue that computes its lead time in days.
* **Aggregation properties** on Jira projects that surface average and median lead time.
* An optional setup to connect Jira issues to services for **team-level** lead time tracking.
* A **dashboard** with widgets showing weekly averages, monthly averages, lead time distribution, and resolved issue tables.

![](/img/guides/jira-lead-time-dashboard.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Identify bottlenecks by comparing lead time across projects and teams.
* Track whether process improvements are reducing delivery times week over week.
* Give engineering managers a real-time view of team velocity without leaving Port.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [Jira integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/) is installed and syncing issues.

## Set up the data model[â](#set-up-the-data-model "Direct link to Set up the data model")

The Jira integration ships with a `jiraIssue` blueprint that already includes `created` and `resolutionDate` properties. We will build on this foundation by adding a calculation property for per-issue lead time, then aggregation properties on `jiraProject` for project-level averages.

### Add a lead time calculation property to Jira issues

The default `jiraIssue` blueprint includes a `handlingDuration` calculation property that computes the number of days between issue creation and resolution. If you already have this property, you can skip this step.

If it is missing, add it:

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Select the **Jira Issue** blueprint.

3. Click on `{...} Edit JSON`.

4. Add the following inside the `calculationProperties` object, then click **Save**:

   ```
   "handlingDuration": {
       "title": "Lead Time (Days)",
       "icon": "Clock",
       "description": "Days from issue creation to resolution",
       "calculation": "if (.properties.resolutionDate != null and .properties.created != null) then (((.properties.resolutionDate[0:19] + \"Z\" | fromdateiso8601) - (.properties.created[0:19] + \"Z\" | fromdateiso8601)) / 86400) else null end",
       "type": "number"
   }
   ```

Every resolved issue will now display its lead time in days.

### Add aggregation properties to Jira projects

Next, add aggregation properties to the `jiraProject` blueprint so you can see average and median lead time per project.

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Select the **Jira Project** blueprint.

3. Click on `{...} Edit JSON`.

4. Add the following inside the `aggregationProperties` object, then click **Save**:

   **Lead time aggregation properties (click to expand)**

   ```
   "avgLeadTimeDays": {
     "title": "Average Lead Time (Days)",
     "icon": "Clock",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "isNotEmpty"
         }
       ]
     },
     "calculationSpec": {
       "func": "average",
       "averageOf": "total",
       "property": "handlingDuration",
       "calculationBy": "property"
     }
   },
   "medianLeadTimeDays": {
     "title": "Median Lead Time (Days)",
     "icon": "Clock",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "isNotEmpty"
         }
       ]
     },
     "calculationSpec": {
       "func": "median",
       "property": "handlingDuration",
       "calculationBy": "property"
     }
   },
   "resolvedIssuesCount": {
     "title": "Resolved Issues",
     "icon": "DefaultProperty",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "isNotEmpty"
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   }
   ```

Each Jira project entity will now show **average lead time**, **median lead time**, and a **resolved issue count** computed from its related issues.

## Connect Jira issues to services[â](#connect-jira-issues-to-services "Direct link to Connect Jira issues to services")

The Jira integration creates a `service` relation on the `jiraIssue` blueprint by default, but the relation is not populated automatically. To get team-level lead time metrics, you need to map each issue to its service through the integration configuration.

The recommended approach is to use Jira labels that match your service identifiers in Port. Prefix labels with a consistent term (e.g. `port-`) so they can be distinguished from other labels.

1. In Jira, add a label to your issues following the pattern `port-<service-identifier>`. For example, if your service in Port is identified as `auth-service`, label the issue with `port-auth-service`.

2. Go to your [Data Sources](https://app.getport.io/settings/data-sources) page and select the Jira integration.

3. In the `issue` mapping, add the following `service` relation under `relations`:

   ```
   relations:
     project: .fields.project.key
     parentIssue: .fields.parent.key
     subtasks: .fields.subtasks | map(.key)
     service: .fields.labels | map(select(startswith("port-"))) | map(sub("port-"; ""; "g")) | .[0]
   ```

   This JQ expression filters labels that start with `port-`, strips the prefix, and uses the first match as the service identifier.

4. Click **Save & Resync**.

Issues with matching labels will now be linked to their respective service entities.

Automate labeling for new issues

To automatically add the `port-` label when creating issues from Port, see the [Open Jira issue with automatic label](https://docs.port.io/guides/all/open-jira-issue-with-automatic-label) guide. For a full walkthrough of the label-based connection, see [Connect Jira issue to a service](https://docs.port.io/guides/all/connect-jira-issue-to-service).

### Add aggregation properties to services

Once issues are connected to services, you can surface lead time metrics at the service (and therefore team) level.

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Select the **Service** blueprint.

3. Click on `{...} Edit JSON`.

4. Add the following inside the `aggregationProperties` object, then click **Save**:

   **Service lead time aggregation properties (click to expand)**

   ```
   "jiraAvgLeadTimeDays": {
     "title": "Avg Jira Lead Time (Days)",
     "icon": "Clock",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "isNotEmpty"
         }
       ]
     },
     "calculationSpec": {
       "func": "average",
       "averageOf": "total",
       "property": "handlingDuration",
       "calculationBy": "property"
     }
   },
   "jiraMedianLeadTimeDays": {
     "title": "Median Jira Lead Time (Days)",
     "icon": "Clock",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "isNotEmpty"
         }
       ]
     },
     "calculationSpec": {
       "func": "median",
       "property": "handlingDuration",
       "calculationBy": "property"
     }
   },
   "jiraResolvedIssues": {
     "title": "Resolved Jira Issues",
     "icon": "DefaultProperty",
     "type": "number",
     "target": "jiraIssue",
     "query": {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "isNotEmpty"
         }
       ]
     },
     "calculationSpec": {
       "func": "count",
       "calculationBy": "entities"
     }
   }
   ```

Since services relate to teams, you can now view lead time per team by navigating the service-to-team ownership chain in your catalog.

## Ensure resolved issues are ingested[â](#ensure-resolved-issues-are-ingested "Direct link to Ensure resolved issues are ingested")

The default Jira integration mapping uses a JQL filter that limits ingested issues. To ensure resolved issues are available for lead time calculations, verify your JQL includes recently resolved items.

Go to your [Data Sources](https://app.getport.io/settings/data-sources) page, select the Jira integration, and check the `jql` selector for the `issue` kind:

```
- kind: issue
  selector:
    query: "true"
    jql: "(statusCategory != Done) OR (created >= -4w) OR (updated >= -4w)"
```

Wider time range for historical data

To capture more historical lead time data, widen the JQL window. For example, change `-4w` to `-12w` or `-26w` to include issues resolved in the last 3 or 6 months. Keep in mind that a wider window increases the number of ingested entities.

## Create a lead time dashboard[â](#create-a-lead-time-dashboard "Direct link to Create a lead time dashboard")

With the data model in place, create a dashboard to visualize lead time metrics.

1. Navigate to the [Catalog](https://app.getport.io/organization/catalog) page.
2. Click **+ New** in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard **Jira Lead Time**.
5. Set the description to `Track lead time from issue creation to resolution`.
6. Select the `Jira` icon.
7. Click **Create**.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In the new dashboard, create the following widgets:

**Weekly average lead time (click to expand)**

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Weekly Avg Lead Time`.
3. Select `Aggregate by property` **Chart type** and choose **Jira Issue** as the **Blueprint**.
4. Select `Lead Time (Days)` for the **Property** and `average` for the **Function**.
5. Select `total` for **Average of**.
6. Add this filter to scope to issues resolved in the past week:
   <!-- -->
   ```

     {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "between",
           "value": {
             "preset": "lastWeek"
           }
         }
       ]
     }
   ```
7. Select `custom` as the **Unit** and input `days` as the **Custom unit**.
8. Click **Save**.

**Monthly average lead time (click to expand)**

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Monthly Avg Lead Time`.
3. Select `Aggregate by property` **Chart type** and choose **Jira Issue** as the **Blueprint**.
4. Select `Lead Time (Days)` for the **Property** and `average` for the **Function**.
5. Select `total` for **Average of**.
6. Add this filter to scope to issues resolved in the past month:
   <!-- -->
   ```

     {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "between",
           "value": {
             "preset": "lastMonth"
           }
         }
       ]
     }
   ```
7. Select `custom` as the **Unit** and input `days` as the **Custom unit**.
8. Click **Save**.

**Issues resolved per week (click to expand)**

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Issues Resolved per Week` (add the `Jira` icon).
3. Select `Count entities` **Chart type** and choose **Jira Issue** as the **Blueprint**.
4. Select `count` for the **Function**.
5. Add this filter:
   <!-- -->
   ```

     {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "isNotEmpty"
         },
         {
           "property": "resolutionDate",
           "operator": "between",
           "value": {
             "preset": "lastWeek"
           }
         }
       ]
     }
   ```
6. Select `custom` as the **Unit** and input `issues` as the **Custom unit**.
7. Click **Save**.

**Lead time by project (click to expand)**

1. Click `+ Widget` and select **Table**.

2. Title: `Lead Time by Project`.

3. Choose the **Jira Project** blueprint.

4. Add this filter to show only resolved issues:
   <!-- -->
   ```
     {
       "combinator": "and",
       "rules": [
         {
           "value": 0,
           "property": "resolvedIssuesCount",
           "operator": "!="
         }
       ]
     }
   ```

5. Click **Save**.

6. Click the `...` button on the widget and select **Customize table**.

7. Click **Manage Properties** and add:

   <!-- -->

   * **Average Lead Time (Days)**.
   * **Median Lead Time (Days)**.
   * **Resolved Issues**.
   * **Project URL**.

8. Click the **save icon** to save the customized table.

**Lead time distribution by issue type (click to expand)**

1. Click `+ Widget` and select **Pie chart**.
2. Title: `Lead Time by Issue Type` (add the `Jira` icon).
3. Choose the **Jira Issue** blueprint.
4. Under **Breakdown by property**, select the **Type** property.
5. Add this filter to only include resolved issues:
   <!-- -->
   ```

     {
       "combinator": "and",
       "rules": [
         {
           "property": "resolutionDate",
           "operator": "isNotEmpty"
         }
       ]
     }
   ```
6. Click **Save**.

## Summary[â](#summary "Direct link to Summary")

You now have a complete lead time tracking setup:

* **Issue level**: Each resolved Jira issue displays its lead time in days via the `handlingDuration` calculation property.
* **Project level**: Each Jira project shows average and median lead time through aggregation properties.
* **Service and team level** (optional): By connecting Jira issues to services, lead time metrics flow up through the service-to-team ownership chain.
* **Dashboard**: Weekly and monthly averages, project comparisons, and a sorted table of slowest issues give you actionable visibility.
