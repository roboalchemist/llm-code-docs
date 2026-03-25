# Source: https://docs.port.io/guides/all/visualize-your-wiz-vulnerabilities.md

# Visualize your Wiz security issues

This guide demonstrates how to set up a monitoring solution to gain visibility into security issues from your Wiz account.<br /><!-- -->We will see how to visualize vulnerabilities across your projects and track them over time using Port's **Wiz** integration.

![](/img/guides/wizVulnDashboard.png) ![](/img/guides/wizVulnDashboard2.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Monitor open and resolved Wiz issues across projects.
* Understand the distribution of issues by severity and status.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* Port's [Wiz integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/code-quality-security/wiz/) is installed in your account.

## Visualize metrics[â](#visualize-metrics "Direct link to Visualize metrics")

Once the Wiz data is synced to the catalog, we can create a dedicated dashboard in Port to monitor and analyze vulnerabilities using customizable widgets.

### Create a dashboard[â](#create-a-dashboard "Direct link to Create a dashboard")

1. Navigate to your [software catalog](https://app.getport.io/organization/catalog).
2. Click on the **`+ New`** button in the left sidebar.
3. Select **New dashboard**.
4. Name the dashboard **Wiz Security Insight**.
5. Select the `Wiz` icon.
6. Click `Create`.

We now have a blank dashboard where we can start adding widgets to visualize insights from the Wiz issues.

### Add widgets[â](#add-widgets "Direct link to Add widgets")

In the new dashboard, create the following widgets:

**Issue by severity (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Issue by severity`.

3. Choose the **Wiz Issue** blueprint.

4. Under `Breakdown by property`, select the **Severity** property

   ![](/img/guides/wizIssueSeverityPieChart.png)

5. Click **Save**.

**Issue by status (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Issue by status`.

3. Choose the **Wiz Issue** blueprint.

4. Under `Breakdown by property`, select the **Status** property

   ![](/img/guides/wizIssueStatusPieChart.png)

5. Click **Save**.

**Total number of issues (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Total issues`.

3. Select `Count entities` **Chart type** and choose **Wiz Issue** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Select `custom` as the **Unit** and input `issues` as the **Custom unit**.

   ![](/img/guides/totalWizIssues.png)

6. Click `Save`.

**Open issue created in the last 6 months (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Open issues` (add the `Alert` icon).

3. Select `Count entities` **Chart type** and choose **Wiz Issue** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter `OPEN` issues created in the last 6 months:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"status",
                   "operator":"=",
                   "value":"OPEN"
               },
               {
                   "property":"createdAt",
                   "operator":"between",
                   "value":{
                   "preset":"last6Months"
                   }
               }
           ]
       }
   ]
   ```

   ![](/img/guides/openWizIssues.png)

6. Click `Save`.

**Resolved issues (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Resolved issues`.

3. Select `Count entities` **Chart type** and choose **Wiz Issue** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter `RESOLVED` issues:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"status",
                   "operator":"=",
                   "value":"RESOLVED"
               }
           ]
       }
   ]
   ```

   ![](/img/guides/resolvedWizIssues.png)

6. Click `Save`.

**Open critical issues (click to expand)**

1. Click `+ Widget` and select **Number Chart**.

2. Title: `Open critical issues`.

3. Select `Count entities` **Chart type** and choose **Wiz Issue** as the **Blueprint**.

4. Select `count` for the **Function**.

5. Add this JSON to the **Additional filters** editor to filter `OPEN` and `CRITICAL` issues:

   ```
   [
       {
           "combinator":"and",
           "rules":[
               {
                   "property":"status",
                   "operator":"=",
                   "value":"OPEN"
               },
               {
                   "property":"severity",
                   "operator":"=",
                   "value":"CRITICAL"
               }
           ]
       }
   ]
   ```

   ![](/img/guides/openCriticalIssues.png)

6. Click `Save`.
