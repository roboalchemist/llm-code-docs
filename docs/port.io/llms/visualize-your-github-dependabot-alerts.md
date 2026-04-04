# Source: https://docs.port.io/guides/all/visualize-your-github-dependabot-alerts.md

# Visualize your GitHub dependency security alerts

This guide demonstrates how to set up a monitoring solution to gain visibility into security alerts from GitHubâs Dependabot. Youâll learn how to visualize vulnerability alerts across your repositories and track them over time using Port's **GitHub** integration.

![](/img/guides/gitHubDependabotInsightDashboard.png) ![](/img/guides/gitHubDependabotInsightDashboard2.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Monitor open and resolved Dependabot alerts across repositories.
* Identify repositories with a high number of unresolved alerts.
* Understand the distribution of alerts by severity and package ecosystem (e.g., npm, Maven, PyPI).

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [GitHub app](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) is installed in your account.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

When installing the GitHub app in Port, the `Repository` blueprint is created by default.<br /><!-- -->However, the `Dependabot Alert` blueprint is not created automatically, so we will need to create it manually.

### Create the Github dependabot alert blueprint[â](#create-the-github-dependabot-alert-blueprint "Direct link to Create the Github dependabot alert blueprint")

Follow the steps below to create the `Dependabot Alert` blueprint.<br />**Skip** to the [set up data source mapping](#set-up-data-source-mapping) section if you already have the blueprint.

1. Go to your [Builder](https://app.getport.io/settings/data-model) page.

2. Click on `+ Blueprint`.

3. Click on the `{...}` button in the top right corner, and choose `Edit JSON`.

4. Add this JSON schema:

   **GitHub dependabot alert blueprint (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "githubDependabotAlert",
       "title": "Dependabot Alert",
       "icon": "Github",
       "schema": {
           "properties": {
           "severity": {
               "title": "Severity",
               "type": "string",
               "enum": ["low", "medium", "high", "critical"],
               "enumColors": {
               "low": "yellow",
               "medium": "orange",
               "high": "red",
               "critical": "red"
               },
               "icon": "DefaultProperty"
           },
           "state": {
               "title": "State",
               "type": "string",
               "enum": ["auto_dismissed", "dismissed", "fixed", "open"],
               "enumColors": {
               "auto_dismissed": "green",
               "dismissed": "green",
               "fixed": "green",
               "open": "red"
               },
               "icon": "DefaultProperty"
           },
           "packageName": {
               "icon": "DefaultProperty",
               "title": "Package Name",
               "type": "string"
           },
           "packageEcosystem": {
               "title": "Package Ecosystem",
               "type": "string"
           },
           "manifestPath": {
               "title": "Manifest Path",
               "type": "string"
           },
           "scope": {
               "title": "Scope",
               "type": "string"
           },
           "ghsaID": {
               "title": "GHSA ID",
               "type": "string"
           },
           "cveID": {
               "title": "CVE ID",
               "type": "string"
           },
           "cvssScore": {
               "type": "number",
               "title": "CVSS Score"
           },
           "url": {
               "title": "URL",
               "type": "string",
               "format": "url"
           },
           "references": {
               "icon": "Vulnerability",
               "title": "References",
               "type": "array",
               "items": {
               "type": "string",
               "format": "url"
               }
           },
           "alertCreatedAt": {
               "icon": "DefaultProperty",
               "type": "string",
               "title": "Alert Created At",
               "format": "date-time"
           },
           "alertUpdatedAt": {
               "icon": "DefaultProperty",
               "type": "string",
               "title": "Alert Updated At",
               "format": "date-time"
           }
           },
           "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "relations": {
           "repository": {
           "title": "Repository",
           "target": "githubRepository",
           "required": true,
           "many": false
           }
       }
   }
   ```

5. Click `Save` to create the blueprint.

## Set up data source mapping[â](#set-up-data-source-mapping "Direct link to Set up data source mapping")

1. Go to your [Data Source](https://app.getport.io/settings/data-sources) page.

2. Select the GitHub integration.

3. Add the following YAML block into the editor to ingest data from GitHub:

   **GitHub integration configuration (Click to expand)**

   ```
   resources:
   - kind: repository
       selector:
       query: 'true'
       port:
       entity:
           mappings:
           identifier: .name
           title: .name
           blueprint: '"githubRepository"'
           properties:
               readme: file://README.md
               url: .html_url
               defaultBranch: .default_branch
               visibility: .visibility

   - kind: dependabot-alert
       selector:
       query: "true"
       port:
       entity:
           mappings:
           identifier: .repo.name + "-" + (.number | tostring)
           title: .number | tostring
           blueprint: '"githubDependabotAlert"'
           properties:
               state: .state
               severity: .security_advisory.severity
               packageName: .dependency.package.name
               packageEcosystem: .dependency.package.ecosystem
               manifestPath: .dependency.manifest_path
               scope: .dependency.scope
               ghsaID: .security_advisory.ghsa_id
               cveID: .security_advisory.cve_id
               cvssScore: .security_advisory.cvss.score
               url: .html_url
               references: "[.security_advisory.references[].url]"
               alertCreatedAt: .created_at
               alertUpdatedAt: .updated_at
           relations:
               repository: .repo.name
   ```

4. Click `Save & Resync` to apply the mapping.

## Visualize metrics[â](#visualize-metrics "Direct link to Visualize metrics")

Once the GitHub data is synced, we can create a dedicated dashboard in Port to monitor and analyze dependency vulnerability alerts using customizable widgets.

### Create a dashboard[â](#create-a-dashboard "Direct link to Create a dashboard")

1. Navigate to your [software catalog](https://app.getport.io/organization/catalog).
2. Click on the **`+ New`** button in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard **Dependabot Alert Insights**.
5. Select the `Vulnerability` icon.
6. Click `Create`.

We now have a blank dashboard where we can start adding widgets to visualize insights from the Dependabot alerts.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In the new dashboard, create the following widgets:

**Vulnerability by severity (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Vulnerability by severity`.

3. Choose the **Dependabot Alert** blueprint.

4. Under `Breakdown by property`, select the **Severity** property

   ![](/img/guides/gitHubvulnSeverityPieChart.png)

5. Click **Save**.

**Vulnerability by package type (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Vulnerability by package type`.

3. Choose the **Dependabot Alert** blueprint.

4. Under `Breakdown by property`, select the **Package Ecosystem** property

   ![](/img/guides/gitHubVulnPackageTypePieChart.png)

5. Click **Save**.

**Open alerts updated in the last 6 months (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Open alerts` (add the `Alert` icon).

3. Select `Count entities` **Chart type** and choose **Dependabot Alert** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter `open` alerts updated in the last 6 months:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"state",
                   "operator":"=",
                   "value":"open"
               },
               {
                   "property":"alertUpdatedAt",
                   "operator":"between",
                   "value":{
                   "preset":"last6Months"
                   }
               }
           ]
       }
   ]
   ```

6. You may optionally configure **conditional formatting** to contextualize the numbers on the widget.

   ![](/img/guides/openDependabotAlerts.png) ![](/img/guides/openDependabotAlertsFormatting.png)

7. Click `Save`.

**Fixed alerts (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Fixed alerts` (add the `BadgeAlert` icon).

3. Select `Count entities` **Chart type** and choose **Dependabot Alert** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter `fixed` alerts:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"state",
                   "operator":"=",
                   "value":"fixed"
               }
           ]
       }
   ]
   ```

   ![](/img/guides/fixedDependabotAlerts.png)

6. Click `Save`.

**Dismissed alerts (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Dismissed alerts`.

3. Select `Count entities` **Chart type** and choose **Dependabot Alert** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter `Dismissed alerts` alerts:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"state",
                   "operator":"=",
                   "value":"auto_dismissed"
               }
           ]
       }
   ]
   ```

   ![](/img/guides/dismissedDependabotAlerts.png)

6. Click `Save`.

**Average CVSS score over time (click to expand)**

1. Click `+ Widget` and select **Line Chart**.

2. Title: `Average CVSS Score Over Time`, (add the `LineChart` icon).

3. Select `Aggregate Property (All Entities)` **Chart type** and choose **Dependabot Alert** as the **Blueprint**.

4. Input `CVSS Score` as the **Y axis** **Title** and choose `CVSS Score` as the **Property**.

5. Set `average` as the **Function**.

6. Input `Months` as the **X axis** **Title** and choose `alertCreatedAt` as the **Measure time by**.

7. Set **Time Interval** to `Month` and **Time Range** to `In the past 365 days`.

   ![](/img/guides/avgCsvvAlertsChart.png) ![](/img/guides/avgCsvvAlertsChartAxisConfig.png)

8. Click `Save`.

**Repos with unresolved critical alerts (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title the widget **Repos with unresolved alerts**.

3. Choose the **Dependabot Alert** blueprint.

   ![](/img/guides/githubReposWithCriticalAlerts.png)

4. Click **Save** to add the widget to the dashboard.

5. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

6. In the top right corner of the table, click on `Manage Properties` and add the following properties:

   * **Repositry**: The name of each related repository.
   * **Package Name**: The name of the package.
   * **CVE-ID**: The ID of the vulnerability.

7. Click on the `Group by any Column` on the top right conner and select **Repository**.

8. Click on the **save icon** in the top right corner of the widget to save the customized table.
