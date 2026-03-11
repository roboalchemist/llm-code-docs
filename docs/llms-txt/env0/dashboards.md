# Source: https://docs.envzero.com/guides/cloud-analyst/cloud-analyst/dashboards.md

# Source: https://docs.envzero.com/guides/admin-guide/dashboards.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Dashboards

> Monitor organization activity with summary and activity dashboards showing deployments, users, and trends

Dashboards are divided into 2 tabs: Summary and Activity.

# Summary

## Counts

Shows total users, teams, projects, and templates.

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/bee5863-counts.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=d9fdcbd70aa4ef7976f1d70f5cce2bc1" alt="" width="1350" height="760" data-path="images/guides/admin-guide/bee5863-counts.png" />

## Environments Pie Chart

All environments, sliced by status(Active, \[type] Failed, and Waiting for approval)

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/3445750-environmentspiechart.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=355ff3bc0b222468f9136a797ffe4459" alt="" width="1322" height="640" data-path="images/guides/admin-guide/3445750-environmentspiechart.png" />

## Environments Table

Contains all environments which can be filtered by several attributes such as name, project, status, etc...

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/d4c6028-screen_shot_2021-11-18_at_11.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=2c69ba463f88d5f1e61c6c035dc78d21" alt="" width="1381" height="613" data-path="images/guides/admin-guide/d4c6028-screen_shot_2021-11-18_at_11.png" />

# Activity

Here you can choose a time range using the dropdown menu at the right corner, by last week, month, or quarter.

## Deployments Pie Chart

All deployments, sliced by type (Deploy, Destroy, PR Plan). Hovering on it, shows the number.

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/8a58c66-deploymentspiechart.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=13e8e493c9c22e33958191438b53bd11" alt="" width="1060" height="994" data-path="images/guides/admin-guide/8a58c66-deploymentspiechart.png" />

## Top Deploying Users

All users, ordered by default by total number of deployments from highest to lowest (can be ordered by other criteria as well).

<img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/guides/admin-guide/1f20b05-screen_shot_2021-11-18_at_14.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=5a7382e72a5e52998060e14b9073de12" alt="" width="800" height="423" data-path="images/guides/admin-guide/1f20b05-screen_shot_2021-11-18_at_14.png" />

## Number of Deployments Per Day

Contains a line chart of each deployment type.

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/6d0ad32-numberofdeploymentsperday.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=87e10dc2c07a4bac311bd1d73ad7d6aa" alt="" width="2710" height="1022" data-path="images/guides/admin-guide/6d0ad32-numberofdeploymentsperday.png" />

## Active Environments Bar Chart

Shows the number of active environments per day. This data is refreshed every 24 hours.

<img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/guides/admin-guide/195b927-screen_shot_2021-11-18_at_14.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=3ff2eeb445f1a6b5a16a80ce0da560e1" alt="" width="824" height="296" data-path="images/guides/admin-guide/195b927-screen_shot_2021-11-18_at_14.png" />

## Environments Table

The same table from the [Summary](/guides/admin-guide/dashboards/#environments-table) tab, but here you can select a time range.

<Info>
  **Calculations**

  The data presented in the dashboards is calculated during each page load or refresh. Except for the Active Environments bar chart, which is updated using a schedule task, once a day.
</Info>

<Warning>
  Excluded Data

  Archived projects and environments are excluded from the aggregations.
</Warning>

# Weekly email digest

env zero will email organization admins a weekly summary of env zero platform usage, detailing how your teams are using env zero.\
This will include details about your environments, most active users, and deployments per day.

The env zero digest email aggregates data from the past week into four graphs:

1. Number of deployments
2. Deployments per day
3. Active environments per day
4. Top deploying users

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/ee6be3a-weekly-email.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=84142675a905b5fc09a0f0dabc7e9d52" alt="" width="777" height="1076" data-path="images/guides/admin-guide/ee6be3a-weekly-email.png" />

Built with [Mintlify](https://mintlify.com).
