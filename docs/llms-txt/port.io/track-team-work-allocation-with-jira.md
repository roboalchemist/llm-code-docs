# Source: https://docs.port.io/guides/all/track-team-work-allocation-with-jira.md

# Track team work allocation with Jira

Understanding how engineering effort is distributed across different types of work is critical for healthy teams. Without visibility into work allocation, teams can drift into reactive patterns where support and technical debt crowd out planned roadmap delivery.

This guide walks you through building a work allocation tracking system in Port that uses **Jira labels** to categorize issues into three work categories:

* **Roadmap**: planned features, product initiatives, and new capabilities.
* **Tech Debt**: refactoring, infrastructure improvements, and maintenance.
* **Support**: bug fixes, incidents, and customer-reported issues.

By the end of this guide, you will have aggregation properties on your team blueprint that automatically compute each category's share of the total work, along with dashboards that show allocation breakdowns per team.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Detect when a team's support burden is crowding out roadmap delivery.
* Track whether tech debt investment targets (e.g. 20% of effort) are being met.
* Give engineering leaders a cross-team view of where effort is going.
* Identify trends over time, is support load growing or shrinking?

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [Jira integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira/) is installed and syncing issues.
* Your Jira issues have a **team** relation set up (either via a Jira custom field or manually assigned in Port).

Label convention

This guide uses Jira labels as the categorization mechanism because they are lightweight, easy to adopt, and don't require Jira admin changes. You can start using them immediately by asking teams to apply the labels described below to their issues.

## Define your label convention[â](#define-your-label-convention "Direct link to Define your label convention")

Before configuring Port, establish a labelling standard in Jira. Each issue should carry **one** label from the following groups:

| Category      | Accepted labels                                          | Examples                                      |
| ------------- | -------------------------------------------------------- | --------------------------------------------- |
| **Roadmap**   | `roadmap`, `feature`, `product`                          | New user onboarding flow, API v2 endpoints    |
| **Tech Debt** | `tech-debt`, `refactor`, `maintenance`, `infrastructure` | Migrate to new ORM, upgrade Node.js           |
| **Support**   | `support`, `bug-fix`, `incident`, `hotfix`               | Fix login redirect, resolve production outage |

Issues that don't carry any of these labels are treated as **Uncategorized** and excluded from allocation percentages.

Flexibility

You can adjust the accepted labels to match your team's existing conventions. The important thing is that each category maps to a clearly defined set of labels and that the mapping is consistent across teams.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

### Add work category to the Jira issue blueprint[â](#add-work-category-to-the-jira-issue-blueprint "Direct link to Add work category to the Jira issue blueprint")

We will add a **calculation property** to the `Jira Issue` blueprint that automatically classifies each issue into a work category based on its labels.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find the **Jira Issue** blueprint and click on it.

3. Click on the `...` button in the top right corner, and choose `{...} Edit JSON`.

4. Add the following calculation property inside the `calculationProperties` object:

   **Work category calculation property (click to expand)**

   ```
   {
     "workCategory": {
       "title": "Work Category",
       "icon": "Star",
       "description": "Classifies work into Roadmap, Tech Debt, or Support based on Jira labels",
       "calculation": "if (.properties.labels != null) then (if (.properties.labels | map(ascii_downcase) | any(. == \"roadmap\" or . == \"feature\" or . == \"product\")) then \"Roadmap\" elif (.properties.labels | map(ascii_downcase) | any(. == \"tech-debt\" or . == \"refactor\" or . == \"maintenance\" or . == \"infrastructure\")) then \"Tech Debt\" elif (.properties.labels | map(ascii_downcase) | any(. == \"support\" or . == \"bug-fix\" or . == \"incident\" or . == \"hotfix\")) then \"Support\" else \"Uncategorized\" end) else \"Uncategorized\" end",
       "type": "string",
       "colorized": true,
       "colors": {
         "Roadmap": "blue",
         "Tech Debt": "orange",
         "Support": "red",
         "Uncategorized": "lightGray"
       }
     }
   }
   ```

5. Click `Save`.

Each issue will now display a color-coded **Work Category** badge based on its labels. The priority order is Roadmap > Tech Debt > Support, so if an issue carries multiple category labels, the first match wins.

### Add aggregation properties to the team blueprint[â](#add-aggregation-properties-to-the-team-blueprint "Direct link to Add aggregation properties to the team blueprint")

Next, we add aggregation properties to the **Team** blueprint that count how many issues fall into each category. These roll up from all Jira issues related to a team.

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Find the **Team** blueprint and click on it.

3. Click on the `...` button in the top right corner, and choose `{...} Edit JSON`.

4. Add the following aggregation properties inside the `aggregationProperties` object:

   **Work allocation aggregation properties (click to expand)**

   ```
   {
     "roadmapIssues": {
       "title": "Roadmap Issues",
       "icon": "Star",
       "type": "number",
       "target": "jiraIssue",
       "description": "Count of issues labelled as Roadmap",
       "query": {
         "combinator": "or",
         "rules": [
           { "property": "labels", "operator": "contains", "value": "roadmap" },
           { "property": "labels", "operator": "contains", "value": "feature" },
           { "property": "labels", "operator": "contains", "value": "product" }
         ]
       },
       "calculationSpec": {
         "func": "count",
         "calculationBy": "entities"
       }
     },
     "techDebtIssues": {
       "title": "Tech Debt Issues",
       "icon": "DefaultProperty",
       "type": "number",
       "target": "jiraIssue",
       "description": "Count of issues labelled as Tech Debt",
       "query": {
         "combinator": "or",
         "rules": [
           { "property": "labels", "operator": "contains", "value": "tech-debt" },
           { "property": "labels", "operator": "contains", "value": "refactor" },
           { "property": "labels", "operator": "contains", "value": "maintenance" },
           { "property": "labels", "operator": "contains", "value": "infrastructure" }
         ]
       },
       "calculationSpec": {
         "func": "count",
         "calculationBy": "entities"
       }
     },
     "supportIssues": {
       "title": "Support Issues",
       "icon": "Alert",
       "type": "number",
       "target": "jiraIssue",
       "description": "Count of issues labelled as Support",
       "query": {
         "combinator": "or",
         "rules": [
           { "property": "labels", "operator": "contains", "value": "support" },
           { "property": "labels", "operator": "contains", "value": "bug-fix" },
           { "property": "labels", "operator": "contains", "value": "incident" },
           { "property": "labels", "operator": "contains", "value": "hotfix" }
         ]
       },
       "calculationSpec": {
         "func": "count",
         "calculationBy": "entities"
       }
     },
     "totalCategorizedIssues": {
       "title": "Total Categorized Issues",
       "icon": "DefaultProperty",
       "type": "number",
       "target": "jiraIssue",
       "description": "Count of all Jira issues with a work category label",
       "query": {
         "combinator": "or",
         "rules": [
           { "property": "labels", "operator": "contains", "value": "roadmap" },
           { "property": "labels", "operator": "contains", "value": "feature" },
           { "property": "labels", "operator": "contains", "value": "product" },
           { "property": "labels", "operator": "contains", "value": "tech-debt" },
           { "property": "labels", "operator": "contains", "value": "refactor" },
           { "property": "labels", "operator": "contains", "value": "maintenance" },
           { "property": "labels", "operator": "contains", "value": "infrastructure" },
           { "property": "labels", "operator": "contains", "value": "support" },
           { "property": "labels", "operator": "contains", "value": "bug-fix" },
           { "property": "labels", "operator": "contains", "value": "incident" },
           { "property": "labels", "operator": "contains", "value": "hotfix" }
         ]
       },
       "calculationSpec": {
         "func": "count",
         "calculationBy": "entities"
       }
     }
   }
   ```

   You can also add **story point** aggregations for a weighted allocation view:

   **Story point aggregation properties (click to expand)**

   ```
   {
     "roadmapStoryPoints": {
       "title": "Roadmap Story Points",
       "icon": "Star",
       "type": "number",
       "target": "jiraIssue",
       "description": "Total story points for Roadmap work",
       "query": {
         "combinator": "or",
         "rules": [
           { "property": "labels", "operator": "contains", "value": "roadmap" },
           { "property": "labels", "operator": "contains", "value": "feature" },
           { "property": "labels", "operator": "contains", "value": "product" }
         ]
       },
       "calculationSpec": {
         "func": "sum",
         "calculationBy": "property",
         "property": "storyPoints"
       }
     },
     "techDebtStoryPoints": {
       "title": "Tech Debt Story Points",
       "icon": "DefaultProperty",
       "type": "number",
       "target": "jiraIssue",
       "description": "Total story points for Tech Debt work",
       "query": {
         "combinator": "or",
         "rules": [
           { "property": "labels", "operator": "contains", "value": "tech-debt" },
           { "property": "labels", "operator": "contains", "value": "refactor" },
           { "property": "labels", "operator": "contains", "value": "maintenance" },
           { "property": "labels", "operator": "contains", "value": "infrastructure" }
         ]
       },
       "calculationSpec": {
         "func": "sum",
         "calculationBy": "property",
         "property": "storyPoints"
       }
     },
     "supportStoryPoints": {
       "title": "Support Story Points",
       "icon": "Alert",
       "type": "number",
       "target": "jiraIssue",
       "description": "Total story points for Support work",
       "query": {
         "combinator": "or",
         "rules": [
           { "property": "labels", "operator": "contains", "value": "support" },
           { "property": "labels", "operator": "contains", "value": "bug-fix" },
           { "property": "labels", "operator": "contains", "value": "incident" },
           { "property": "labels", "operator": "contains", "value": "hotfix" }
         ]
       },
       "calculationSpec": {
         "func": "sum",
         "calculationBy": "property",
         "property": "storyPoints"
       }
     }
   }
   ```

5. Click `Save`.

### Add percentage calculation properties[â](#add-percentage-calculation-properties "Direct link to Add percentage calculation properties")

Now add calculation properties to the **Team** blueprint that compute each category's share of the total.

1. In the same **Team** blueprint JSON editor, add the following inside the `calculationProperties` object:

   **Allocation percentage calculations (click to expand)**

   ```
   {
     "roadmapPercent": {
       "title": "Roadmap Allocation (%)",
       "icon": "Star",
       "description": "Percentage of categorized issues that are Roadmap",
       "calculation": "if (.properties.totalCategorizedIssues != null and .properties.totalCategorizedIssues > 0) then ((.properties.roadmapIssues / .properties.totalCategorizedIssues) * 100 | floor) else null end",
       "type": "number"
     },
     "techDebtPercent": {
       "title": "Tech Debt Allocation (%)",
       "icon": "DefaultProperty",
       "description": "Percentage of categorized issues that are Tech Debt",
       "calculation": "if (.properties.totalCategorizedIssues != null and .properties.totalCategorizedIssues > 0) then ((.properties.techDebtIssues / .properties.totalCategorizedIssues) * 100 | floor) else null end",
       "type": "number"
     },
     "supportPercent": {
       "title": "Support Allocation (%)",
       "icon": "Alert",
       "description": "Percentage of categorized issues that are Support",
       "calculation": "if (.properties.totalCategorizedIssues != null and .properties.totalCategorizedIssues > 0) then ((.properties.supportIssues / .properties.totalCategorizedIssues) * 100 | floor) else null end",
       "type": "number"
     }
   }
   ```

2. Click `Save`.

Once saved, each team entity will automatically show its allocation percentages. For example, a team might display: **Roadmap 60% Â· Tech Debt 20% Â· Support 20%**.

Ensure labels are synced from Jira

If the `labels` property is missing from your mapping, add it by going to your [Data sources](https://app.getport.io/settings/data-sources) page, selecting the Jira integration, and updating the mapping configuration to include the `labels` property like below:

```
kind: issue
selector:
  query: "true"
  port:
    entity:
      mappings:
      # ... existing mappings ...
      identifier: ".key",
      title: ".fields.summary",
      blueprint: "\"jiraIssue\"",
        labels: ".fields.labels"
```

## Visualize work allocation[â](#visualize-work-allocation "Direct link to Visualize work allocation")

With the data model in place and labels flowing from Jira, we can add widgets directly on the team entity page. Widgets created on any team entity automatically appear on every other team entity, scoped to that team's data.

![](/img/guides/work-allocation-widgets.png)

### Add widgets to the team entity page[â](#add-widgets-to-the-team-entity-page "Direct link to Add widgets to the team entity page")

1. Navigate to your [software catalog](https://app.getport.io/organization/catalog) and open any **Team** entity.
2. Click `+ Widget` on the entity page to start adding the following widgets.

**Roadmap issues (click to expand)**

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Roadmap issues` (add the `Star` icon).
3. Select `Count entities` as the **Chart type** and choose **Jira Issue** as the **Blueprint**.
4. Select `count` for the **Function**.
5. Add this JSON to the **Additional filters** editor:
   <!-- -->
   ```
   {
     "combinator": "or",
     "rules": [
       { "property": "labels", "operator": "contains", "value": "roadmap" },
       { "property": "labels", "operator": "contains", "value": "feature" },
       { "property": "labels", "operator": "contains", "value": "product" }
     ]
   }
   ```
6. Select `custom` as the **Unit** and input `issues` as the **Custom unit**.
7. Click `Save`.

**Tech debt issues (click to expand)**

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Tech debt issues` (add the `DefaultProperty` icon).
3. Select `Count entities` as the **Chart type** and choose **Jira Issue** as the **Blueprint**.
4. Select `count` for the **Function**.
5. Add this JSON to the **Additional filters** editor:
   <!-- -->
   ```
   {
     "combinator": "or",
     "rules": [
       { "property": "labels", "operator": "contains", "value": "tech-debt" },
       { "property": "labels", "operator": "contains", "value": "refactor" },
       { "property": "labels", "operator": "contains", "value": "maintenance" },
       { "property": "labels", "operator": "contains", "value": "infrastructure" }
     ]
   }
   ```
6. Select `custom` as the **Unit** and input `issues` as the **Custom unit**.
7. Click `Save`.

**Support issues (click to expand)**

1. Click `+ Widget` and select **Number Chart**.
2. Title: `Support issues` (add the `Alert` icon).
3. Select `Count entities` as the **Chart type** and choose **Jira Issue** as the **Blueprint**.
4. Select `count` for the **Function**.
5. Add this JSON to the **Additional filters** editor:
   <!-- -->
   ```
   {
     "combinator": "or",
     "rules": [
       { "property": "labels", "operator": "contains", "value": "support" },
       { "property": "labels", "operator": "contains", "value": "bug-fix" },
       { "property": "labels", "operator": "contains", "value": "incident" },
       { "property": "labels", "operator": "contains", "value": "hotfix" }
     ]
   }
   ```
6. Select `custom` as the **Unit** and input `issues` as the **Custom unit**.
7. Click `Save`.

**Work category distribution (click to expand)**

1. Click `+ Widget` and select **Pie chart**.
2. Title: `Work category distribution` (add the `Jira` icon).
3. Choose the **Jira Issue** blueprint.
4. Under `Breakdown by property`, select the **Work Category** property.
5. Add this JSON to the **Additional filters** editor:
   <!-- -->
   ```
   {
     "combinator": "and",
     "rules": [
       {
         "property": "labels",
         "operator": "isNotEmpty"
       }
     ]
   }
   ```
6. Click **Save**.

The allocation percentages (**Roadmap Allocation (%)**, **Tech Debt Allocation (%)**, **Support Allocation (%)**) are already visible as properties on each team entity, so they don't need separate widgets. For cross-team comparison, open the [Team catalog page](https://app.getport.io/_teams) and add these columns to the table view.

## Summary[â](#summary "Direct link to Summary")

You now have a complete work allocation tracking system that:

* **Categorizes** Jira issues into Roadmap, Tech Debt, and Support using a lightweight label convention.
* **Aggregates** issue counts and story points per category at the team level.
* **Computes** allocation percentages automatically using calculation properties.
* **Visualizes** each team's allocation with a pie chart, trend line, and drill-down table directly on the team entity page.

This gives engineering leaders the data they need to have informed conversations about where effort is going and whether the balance is right for each team.
