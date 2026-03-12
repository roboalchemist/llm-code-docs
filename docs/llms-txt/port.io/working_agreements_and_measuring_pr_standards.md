# Source: https://docs.port.io/guides/all/working_agreements_and_measuring_pr_standards.md

# Measuring pull request standards

This guide is aimed at helping engineering teams implement working agreements and measure pull request (PR) standards.<br /><!-- -->We will implement working agreements using Port's scorecards and measure PR standards using aggregation properties.<br /><!-- -->By the end of this guide, you will be able to track teams' performance based on pull requests metrics as shown here:

![](/img/guides/teamPRMetricTable.png)

## Overview[â](#overview "Direct link to Overview")

Effective collaboration and clear expectations are crucial for high-performing engineering teams.<br />**Working agreements** establish shared processes and standards, enhancing teamwork.

Measuring **Pull request (PR)** standards is essential for assessing code quality, review processes, and team efficiency.

By integrating working agreements with measurable PR metrics, teams can monitor adherence to best practices and continuously improve workflows.

We will discuss how to implement working agreements and measure PR standards using Port.

Metrics

Metrics are essential for assessing how well teams adhere to their working agreements.<br /><!-- -->They enable teams to track compliance, identify bottlenecks, and drive continuous improvement.

For detailed insights into key metrics like `deployment frequency`, `lead time for changes`, and `change failure rate`,<br /><!-- -->please refer to our [DORA Metrics guide](https://docs.port.io/guides/all/create-and-track-dora-metrics-in-your-portal).

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [Port onboarding process](https://docs.port.io/quickstart).
* Access to a GitHub repository that is connected to Port via the onboarding process.

## Working agreements[â](#working-agreements "Direct link to Working agreements")

The following working agreements and PR checks have been implemented in our [demo environment](https://demo.port.io/scorecard_overview):

* [**PR Description Cannot be Empty**](#pr-description-cannot-be-empty): Ensures that every PR has a description.
* [**PR Has Linked Issue**](#pr-has-linked-issue): Verifies that each PR is linked to an issue.
* [**PR Has No Unchecked Checkboxes**](#pr-has-no-unchecked-checkboxes): Checks that there are no unchecked items in the PR description.
* [**PR Requires Reviewers**](#pr-requires-reviewers): Confirms that at least one reviewer is assigned to the PR.
* [**PR Is Linked to a Milestone**](#pr-is-linked-to-a-milestone): Ensures the PR is associated with a milestone.
* [**PR Changed X Files or Less**](#pr-changed-x-files-or-less): Validates that the number of changed files is within acceptable limits.
* [**PR Has Been Open for X Days**](#pr-has-been-open-for-x-days): Monitors how long a PR has been open.
* [**PR Batch Size Calculation**](#pr-batch-size-calculation): Calculates the batch size of the PR.

These checks are implemented using Port's [scorecards](/scorecards/overview.md).

## Implementation[â](#implementation "Direct link to Implementation")

This section will guide you through implementing the working agreements and PR checks in your Port environment. Follow the steps below:

1. Add the properties to the `pull request` blueprint.

   * Go to the [Builder](https://app.getport.io/settings/data-model) in your Port portal.
   * Select the `pull request` blueprint.
   * Click on the `...` button in the top right corner, and choose "Edit JSON".
   * Add the properties and mapping configurations as described below.
   * Save the changes.

   <br />

   Expected JSON

   This is the expected JSON definition after adding the properties.

   ![](/img/guides/prBPPropertyAdd.png)

<br />

2. Add the **mapping configuration** to the data source.

   * Go to the [Data Sources](https://app.getport.io/settings/data-sources) in your Port portal.
   * Select the data source connected to your GitHub repository
   * Add the mapping configurations as described below.
     <!-- -->
     ![](/img/guides/addMappingConfigDS.png)
   * Save the changes.

3. Add the **scorecard** definitions to the `pull request` blueprint.

   * Go to the [Builder](https://app.getport.io/settings/data-model) in your Port portal.
   * Select the `pull request` blueprint.
   * Click on the **Scorecard**
   * Click on the `+ New Scorecard` button.

   ![](/img/guides/scorecardOnPRAdd.png)

   * Paste the scorecard definitions as described below.
   * Save the changes.

### PR Description Cannot be Empty[â](#pr-description-cannot-be-empty "Direct link to PR Description Cannot be Empty")

#### Scorecard Definition

**Scorecard definition (click to expand)**

```
{
  "identifier": "pr_descr_not_empty",
  "title": "PR Description Cannot be Empty",
  "description": "Ensures that the PR description is not empty.",
  "level": "Bronze",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "isNotEmpty",
        "property": "prDescription"
      }
    ]
  }
}
```

#### Property

Add the `prDescription` property to the **pull request** blueprint:

**Add property (click to expand)**

```
"prDescription": {
  "title": "PR Description",
  "type": "string"
}
```

#### Mapping Configuration

Map the PR's `body` field from your data source to the `prDescription` property:

**Mapping config (click to expand)**

```
  - kind: pull-request
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .head.repo.name + (.id|tostring)
          title: .title
          blueprint: '"githubPullRequest"'
          properties:
            #other properties
            prDescription: .body
```

### PR Has Linked Issue[â](#pr-has-linked-issue "Direct link to PR Has Linked Issue")

#### Scorecard Definition

**Scorecard definition (click to expand)**

```
{
  "identifier": "pr_has_issue_link",
  "title": "PR Has Linked Issue",
  "description": "Ensures that the PR is linked to an issue.",
  "level": "Silver",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "isNotEmpty",
        "property": "issueUrl"
      }
    ]
  }
}
```

#### Property

Add the `issueUrl` property to the **pull request** blueprint:

**Add property (click to expand)**

```
"issueUrl": {
  "title": "Issue URL",
  "type": "string",
  "format": "url"
}
```

#### Mapping Configuration

Map the issue URL from your data source to the `issueurl` property:

**Mapping config (click to expand)**

```
  - kind: pull-request
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .head.repo.name + (.id|tostring)
          title: .title
          blueprint: '"githubPullRequest"'
          properties:
            #other properties
            issueUrl: .issue_url
```

### PR Has No Unchecked Checkboxes[â](#pr-has-no-unchecked-checkboxes "Direct link to PR Has No Unchecked Checkboxes")

#### Scorecard Definition

**Scorecard definition (click to expand)**

```
{
  "identifier": "pr_no_unchecked_chk",
  "title": "PR Has No Unchecked Checkboxes",
  "description": "Ensures that there are no unchecked checkboxes in the PR description.",
  "level": "Silver",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "doesNotContains",
        "property": "prDescription",
        "value": "- [ ]"
      }
    ]
  }
}
```

Property addition

If you haven't added the `prDescription` property and its relative mapping config, please refer to the [PR Description Cannot be Empty](#pr-description-cannot-be-empty) section.

### PR Requires Reviewers[â](#pr-requires-reviewers "Direct link to PR Requires Reviewers")

#### Scorecard Definition

**Scorecard definition (click to expand)**

```
{
  "identifier": "pr_has_reviewers_req",
  "title": "PR Requires Reviewers",
  "description": "Ensures that the PR has at least one reviewer requested.",
  "level": "Bronze",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "isNotEmpty",
        "property": "reviewers"
      }
    ]
  }
}
```

#### Property

Add the `reviewers` property to the **pull request** blueprint if it doesn't exist:

**Add property (click to expand)**

```
"reviewers": {
  "title": "Reviewers",
  "type": "array"
}
```

#### Mapping Configuration

Map the list of reviewers from your data source to the `reviewers` property:

**Mapping config (click to expand)**

```
  - kind: pull-request
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .head.repo.name + (.id|tostring)
          title: .title
          blueprint: '"githubPullRequest"'
          properties:
            #other properties
            reviewers: '[.requested_reviewers[].login]'
```

### PR Is Linked to a Milestone[â](#pr-is-linked-to-a-milestone "Direct link to PR Is Linked to a Milestone")

#### Scorecard Definition

**Scorecard definition (click to expand)**

```
{
  "identifier": "pr_linked_milestone",
  "title": "PR Is Linked to a Milestone",
  "description": "Ensures that the PR is linked to a milestone.",
  "level": "Gold",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "isNotEmpty",
        "property": "milestone"
      }
    ]
  }
}
```

#### Property

**Add property (click to expand)**

Add the `milestone` property to the **pull request** blueprint:

```
"milestone": {
  "title": "Milestone",
  "type": "object"
}
```

#### Mapping Configuration

**Mapping config (click to expand)**

Map the milestone information from your data source to the `milestone` property.

```
  - kind: pull-request
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .head.repo.name + (.id|tostring)
          title: .title
          blueprint: '"githubPullRequest"'
          properties:
            #other properties
            milestone: .milestone
```

### PR Changed X Files or Less[â](#pr-changed-x-files-or-less "Direct link to PR Changed X Files or Less")

GitHub API Limitation

This feature is only available with live-events and not during ingestion due to GitHub API limitations. The `changed_files` property is not available through the GitHub REST API for historical pull requests.

#### Scorecard Definition

This agreement has multiple levels based on the number of files changed.

**Scorecard definition (click to expand)**

**Bronze level scorecard definition (click to expand)**

```
{
  "identifier": "pr_file_limit_bronze",
  "title": "PR Can't Have More than 15 Changed Files",
  "description": "Ensures that the PR does not have more than 15 changed files.",
  "level": "Bronze",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "<=",
        "property": "changedFiles",
        "value": 15
      }
    ]
  }
}
```

**Silver level scorecard definition (click to expand)**

```
{
  "identifier": "pr_file_limit_silver",
  "title": "PR Can't Have More than 10 Changed Files",
  "description": "Ensures that the PR does not have more than 10 changed files.",
  "level": "Silver",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "<=",
        "property": "changedFiles",
        "value": 10
      }
    ]
  }
}
```

**Gold level scorecard definition (click to expand)**

```
{
  "identifier": "pr_file_limit_gold",
  "title": "PR Can't Have More than 5 Changed Files",
  "description": "Ensures that the PR does not have more than 5 changed files.",
  "level": "Gold",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "<=",
        "property": "changedFiles",
        "value": 5
      }
    ]
  }
}
```

value adjustment

You can adjust the value based on your team's requirements.

#### Property

Add the `changedFiles` property to the **pull request** blueprint:

**Add property (click to expand)**

```
    "changedFiles": {
      "title": "Changed Files",
      "type": "number"
    }
```

#### Mapping Configuration

Map the number of `changed_files` from the data source to the `changedFiles` property:

**Mapping config (click to expand)**

```
  - kind: pull-request
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .head.repo.name + (.id|tostring)
          title: .title
          blueprint: '"githubPullRequest"'
          properties:
            #other properties
            changedFiles: .changed_files
```

### PR Has Been Open for X Days[â](#pr-has-been-open-for-x-days "Direct link to PR Has Been Open for X Days")

#### Scorecard Definition

**Scorecard definition (click to expand)**

```
{
  "identifier": "pr_open_for_less_than_10_days",
  "title": "PR Has Been Open for Less Than 10 Days",
  "description": "Ensures that the PR has not been open for more than 10 days.",
  "level": "Silver",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "<=",
        "property": "days_old",
        "value": 10
      },
      {
        "operator": "=",
        "property": "status",
        "value": "open"
      }
    ]
  }
}
```

#### Property

Add a calculation property `days_old` to compute how many days the PR has been open:

**Add property (click to expand)**

```
"days_old": {
  "title": "Days Old",
  "icon": "DefaultProperty",
  "calculation": "(now / 86400) - (.properties.updatedAt | capture(\"(?<date>\\\\d{4}-\\\\d{2}-\\\\d{2})\") | .date | strptime(\"%Y-%m-%d\") | mktime / 86400) | floor",
  "type": "number"
}
```

Required properties

Ensure that `createdAt` and `mergedAt` properties are correctly mapped from your data source.

### PR Batch Size Calculation[â](#pr-batch-size-calculation "Direct link to PR Batch Size Calculation")

GitHub API Limitation

This feature is only available with live-events and not during ingestion due to GitHub API limitations. The `additions`, `deletions`, `commits`, and `changed_files` properties required for batch size calculation are not available through the GitHub REST API for historical pull requests.

#### Scorecard Definition

This agreement has levels based on the batch size.

**Scorecard definition (click to expand)**

**Bronze level scorecard definition (click to expand)**

```
{
  "identifier": "pr_batch_size_bronze",
  "title": "PR Cannot Have Large or Gigantic Batch Size",
  "description": "Ensures that the PR does not have a Large or Gigantic batch size.",
  "level": "Bronze",
  "query": {
    "combinator": "or",
    "conditions": [
      {
        "operator": "!=",
        "property": "batchSize",
        "value": "Large"
      },
      {
        "operator": "!=",
        "property": "batchSize",
        "value": "Gigantic"
      }
    ]
  }
}
```

**Silver level scorecard definition (click to expand)**

```
{
  "identifier": "pr_batch_size_silver",
  "title": "PR Has Medium Batch Size",
  "description": "Ensures that the PR has a Medium batch size.",
  "level": "Silver",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "=",
        "property": "batchSize",
        "value": "Medium"
      }
    ]
  }
}
```

**Gold level scorecard definition (click to expand)**

```
{
  "identifier": "pr_batch_size_gold",
  "title": "PR Has Small Batch Size",
  "description": "Ensures that the PR has a Small batch size.",
  "level": "Gold",
  "query": {
    "combinator": "and",
    "conditions": [
      {
        "operator": "=",
        "property": "batchSize",
        "value": "Small"
      }
    ]
  }
}
```

#### Property

Add a property `batchSize` to categorize the PR's batch size:

**Add property (click to expand)**

```
"batchSize": {
  "title": "Batch Size",
  "type": "string",
  "enum": [
    "Small",
    "Medium",
    "Large",
    "Gigantic"
  ],
  "enumColors": {
    "Small": "lightGray",
    "Medium": "orange",
    "Large": "yellow",
    "Gigantic": "red"
  }
}
```

#### Mapping Configuration

Map the PR's `additions`, `deletions`, and `changedFiles` properties to the `batchSize` property:

**Mapping config (click to expand)**

```
    - kind: pull-request
      selector:
        query: 'true'
        port:
        entity:
            mappings:
            identifier: .head.repo.name + (.id|tostring)
            title: .title
            blueprint: '"githubPullRequest"'
            properties:
                #other properties
            batchSize: >
             if (.commits <= 3 and (.additions + .deletions) <= 50 and
             .changed_files <= 3) then "Small" elif (.commits <= 10 and
             (.additions + .deletions) <= 200 and .changed_files <= 7) then
             "Medium" elif (.commits <= 20 and (.additions + .deletions) <= 500
             and .changed_files <= 15) then "Large" else "Gigantic" end
```

Batch size calculation

You can adjust the thresholds based on your team's requirements.

### Add total LOC changed property[â](#add-total-loc-changed-property "Direct link to Add total LOC changed property")

Add the **calculation property** `totalLocChanged` on the **pull request** blueprint:

**Calculation property (click to expand)**

```
"totalLocChanged": {
  "title": "Total LOC Changed",
  "type": "number",
  "calculation": ".properties.additions + .properties.deletions"
}
```

## Pull request metrics aggregation[â](#pull-request-metrics-aggregation "Direct link to Pull request metrics aggregation")

To measure PR standards effectively, add aggregation properties on the **service** blueprint. This will allow us to capture important metrics such as:

* PR Average Duration (Service Level)
* PRs Opened (Service & Organization Level)
* PRs Merged (Service & Organization Level)
* Average Commits per PR (Service & Organization Level)
* Average Lines of Code (LOC) Changed (Service & Organization Level)

<br />

Aggregation on higher hierarchy

* To aggregate on an organization level, apply the same settings to a higher hierarchy.
* If you want to see it on a team level, you need to make sure services are related to teams and add the same aggregations to team

Adding Aggregation to Blueprints

To add aggregation properties to your blueprints, follow these steps:

1. Go to the [Builder](https://app.getport.io/settings/data-model) in your Port portal.
2. Locate and select your **blueprint**.
3. Click the `{...}` button in the top right corner, and choose **Edit JSON**.
4. Insert the respective **aggregation** or **calculation properties** under the `aggregationProperties` or `calculationProperties` section in the blueprint's JSON schema.
5. Save your changes to apply the new aggregation configuration.

<br />

* Average PR Duration
* PRs Opened
* PRs Merged
* Average Commits per PR
* Average LOC Changed

Add the following aggregation property to the **service** blueprint:

**Aggregation property (click to expand)**

```
"averagePrDuration": {
  "title": "Average PR Duration",
  "type": "number",
  "target": "githubPullRequest",
  "calculationSpec": {
    "func": "average",
    "averageOf": "week",
    "calculationBy": "property",
    "property": "days_old"
  },
  "query": {
    "combinator": "and",
    "rules": [
      {
        "property": "mergedAt",
        "operator": "isNotEmpty"
      }
    ]
  }
}
```

Add the following aggregation property to the **service** blueprint:

**Aggregation property (click to expand)**

```
"openPrs": {
  "title": "Open PRs",
  "type": "number",
  "target": "githubPullRequest",
  "calculationSpec": {
    "func": "count",
    "calculationBy": "entities"
  },
  "query": {
    "combinator": "and",
    "rules": [
      {
        "property": "status",
        "operator": "=",
        "value": "open"
      }
    ]
  }
}
```

Add the following aggregation property to the **service** blueprint:

**Aggregation property (click to expand)**

```
"mergedPrs": {
  "title": "Merged PRs",
  "type": "number",
  "target": "githubPullRequest",
  "calculationSpec": {
    "func": "count",
    "calculationBy": "entities"
  },
  "query": {
    "combinator": "and",
    "rules": [
      {
        "property": "status",
        "operator": "=",
        "value": "merged"
      }
    ]
  }
}
```

Add the following aggregation property to the **service** blueprint:

**Aggregation property (click to expand)**

```
"averageCommitsPerPr": {
  "title": "Average Commits per PR",
  "type": "number",
  "target": "githubPullRequest",
  "calculationSpec": {
    "averageOf": "week",
    "func": "average",
    "calculationBy": "property",
    "property": "commits",
    "measureTimeBy": "$createdAt"
  }
}
```

Add the following aggregation property to the **service** and **organization** blueprints:

**Aggregation property (click to expand)**

```
"averagePrLinesOfCode": {
  "title": "Average PR Lines of Code",
  "type": "number",
  "target": "githubPullRequest",
  "calculationSpec": {
    "func": "average",
    "averageOf": "week",
    "calculationBy": "property",
    "property": "totalLocChanged"
  }
}
```

By implementing these aggregation properties, you can effectively measure and monitor PR standards at both the service and organization levels.

## Visualization[â](#visualization "Direct link to Visualization")

By leveraging Port's Dashboards, you can create custom dashboards to track the pr metrics and monitor your team's performance over time.

![](/img/guides/scorecardsOverview.png)

### Dashboard setup[â](#dashboard-setup "Direct link to Dashboard setup")

![](/img/guides/prMetricsDashboardComp.png)

1. Go to your [software catalog](https://app.getport.io/organization/catalog).
2. Click on the `+ New` button in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard (PR Metrics), choose an icon if desired, and click `Create`.

This will create a new empty dashboard. Let's get ready-to-add widgets

### Adding widgets[â](#adding-widgets "Direct link to Adding widgets")

**Average Pr Merged per month (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Average Pr's Merged per month`, (add the `GitPullRequest` icon).

3. Select `Aggregate by property` and choose **Service** as the **Blueprint**.

4. Choose `Merged PRs` as the **Property**.

5. Select `average` for the **Function** and choose `month` for **Average of**.

6. Select `Created At` for **Measure time by**.

7. Select `custom` as the **Unit** and input `Pull Request merged per month` as the **Custom unit**.

   ![](/img/guides/averagePRMergedPerMonth.png)

8. Click `Save`.

**Total Pr's Merged (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Total Pr's Merged `, (add the `GitPullRequest` icon).

3. Select `Aggregate by property` and choose **Service** as the **Blueprint**.

4. Choose `Merged PRs` as the **Property**.

5. Select `sum` for the **Function**.

   ![](/img/guides/totalPrsMerged.png)

6. Click `Save`.

**Mean Time to Merge (Days) (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Mean Time to Merge (Days)`, (add the `Merge` icon).

3. Select `Display single property` and choose **Service** the **Entity**.

4. Choose `Averge Time to Merge` as the **Property**.

   ![](/img/guides/meanTimeToMergePr.png)

5. Click `Save`.

**Total Weekly Pr commits (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Total Weekly Pr commits`, (add the `GitPullRequest` icon).

3. Select `Aggregate by property` and choose **Service** as the **Blueprint**.

4. Choose `Averge Commits per PRs` as the **Property**.

5. Select `average` for the **Function** and choose `week` for **Average of**.

6. Select `Created At` for **Measure time by**.

7. Select `custom` as the **Unit** and input `Weekly` as the **Custom unit**.

   ![](/img/guides/totalWeeklyPrCommits.png)

8. Click `Save`.

**Service Scorecard Performance by Team (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title the widget **Team Service Scorecard Performance**.

3. Choose the **Service** blueprint.

   ![](/img/guides/teamScorecardTable.png)

4. Click **Save** to add the widget to the dashboard.

5. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

6. In the top right corner of the table, click on `Manage Properties` and add the following properties:

   * **Title**: The name of each service.
   * **PR Metrics**: PR Metrics scorecard aggregation on service.
   * **Owning Team**: The team that owns the service.

7. Click on the `Group by any Column` on the top right conner and select **Owning Team**.

   ![](/img/guides/groupByAnyColumn.png)

8. Click on the **save icon** in the top right corner of the widget to save the customized table.

## Notification automation[â](#notification-automation "Direct link to Notification automation")

Add this automation feature to notify a Slack channel when a scorecard value changes

Automation for sending Slack notifications on scorecard value change (click to expand)

Create in Port

```
{
  "identifier": "scorecardValueChanged",
  "title": "Notify Slack on Scorecard Value Change",
  "icon": "Slack",
  "description": "Sends a Slack message when the scorecard value changes.",
  "trigger": {
    "type": "automation",
    "event": {
      "type": "ENTITY_UPDATED",
      "blueprintIdentifier": "githubPullRequest"
    },
    "condition": {
      "type": "JQ",
      "expressions": [
        ".diff.after.scorecardsStats != .diff.before.scorecardsStats"
      ],
      "combinator": "and"
    }
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "{{ .event.diff.after.properties.serviceSlackUrl }}",
    "agent": false,
    "synchronized": true,
    "body": {
      "channel": "{{ .event.diff.after.properties.serviceSlackChannel }}",
      "text": "*Scorecard value changed for PR <{{ .event.diff.after.properties.link }}|{{ .event.diff.after.title }}>*\n\n*Title:* {{ .event.diff.after.title }}\n\n*Old Scorecard Value:* {{ .event.diff.before.scorecardsStats }}\n\n*New Scorecard Value:* {{ .event.diff.after.scorecardsStats }}\n\n*Link:* <{{ .event.diff.after.properties.link }}|View PR>\n\n"
    }
  },
  "publish": true
}
```

<br />

Adding Automations

To add new automations, follow the steps outlined in the [Automation Setup](/actions-and-automations/define-automations/setup-action.md) section of this guide.<br /><!-- -->and remember to set the `serviceSlackUrl` and `serviceSlackChannel` properties on the **service** blueprint.
