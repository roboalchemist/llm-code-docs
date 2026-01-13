# Source: https://docs.datadoghq.com/service_level_objectives.md

---
title: Service Level Objectives
description: Track the status of your SLOs
breadcrumbs: Docs > Service Level Objectives
source_url: https://docs.datadoghq.com/index.html
---

# Service Level Objectives

{% callout %}
##### Join an enablement webinar session

Explore and register for Foundation Enablement sessions. Learn how you can prioritize and address the issues that matter most to your business with native SLO and SLA tracking.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=SLOs&tags.topics-1=Monitors)
{% /callout %}

## Overview{% #overview %}

Service Level Objectives, or SLOs, are a key part of the site reliability engineering toolkit. SLOs provide a framework for defining clear targets around application performance, which ultimately help teams provide a consistent customer experience, balance feature development with platform stability, and improve communication with internal and external users.

**Tip**: To open Service Level Objectives from Datadog's global search, press `Cmd`/`Ctrl` + `K` and search for `slo`.

## Key terminology{% #key-terminology %}

{% dl %}

{% dt %}
Service Level Indicator (SLI)
{% /dt %}

{% dd %}
A quantitative measurement of a service's performance or reliability. In Datadog SLOs an SLI is a metric or an aggregation of one or more monitors.
{% /dd %}

{% dt %}
Service Level Objective (SLO)
{% /dt %}

{% dd %}
A target percentage for an SLI over a specific period of time.
{% /dd %}

{% dt %}
Service Level Agreement (SLA)
{% /dt %}

{% dd %}
An explicit or implicit agreement between a client and service provider stipulating the client's reliability expectations and service provider's consequences for not meeting them.
{% /dd %}

{% dt %}
Error Budget
{% /dt %}

{% dd %}
The allowed amount of unreliability derived from an SLO's target percentage (100% - target percentage) that is meant to be invested into product development.
{% /dd %}

{% /dl %}

## SLO types{% #slo-types %}

When creating SLOs, you can choose from the following types:

- **Metric-based SLOs**: can be used when you want the SLI calculation to be count-based, the SLI is calculated as the sum of good events divided by the sum of total events.
- **Monitor-based SLOs**: can be used when you want the SLI calculation to be time-based, the SLI is based on the Monitor's uptime. Monitor-based SLOs must be based on a new or existing Datadog monitor, any adjustments must be made to the underlying monitor (cannot be done through SLO creation).
- **Time Slice SLOs**: can be used when you want the SLI calculation to be time-based, the SLI is based on your custom uptime definition (amount of time your system exhibits good behavior divided by the total time). Time Slice SLOs do not require a Datadog monitor, you can try out different metric filters and thresholds and instantly explore downtime during SLO creation.

For a full comparison, see the [SLO Type Comparison](https://docs.datadoghq.com/service_level_objectives/guide/slo_types_comparison/) chart.

## Setup{% #setup %}

Use Datadog's [Service Level Objectives manage page](https://app.datadoghq.com/slo) to create new SLOs or to view and manage all your existing SLOs.

### Configuration{% #configuration %}

1. On the [SLO manage page](https://app.datadoghq.com/slo), select **New SLO +**.
1. Select the SLO type. You can create an SLO with any of the following types: [Metric-based](https://docs.datadoghq.com/service_level_objectives/metric/), [Monitor-based](https://docs.datadoghq.com/service_level_objectives/monitor/), or [Time Slices](https://docs.datadoghq.com/service_level_objectives/time_slice/).
1. Set a target and a rolling time window (past 7, 30, or 90 days) for the SLO. Datadog recommends you make the target stricter than your stipulated SLAs. If you configure more than one time window, select one to be the primary time window. This time window is displayed on SLO lists. By default, the shortest time window is selected.
1. Finally, give the SLO a title, describe it in more detail or add links in the description, add tags, and save it.

After you set up the SLO, select it from the [Service Level Objectives list view](https://app.datadoghq.com/slo) to open the details side panel. The side panel displays the overall status percentage and remaining error budget for each of the SLO's targets, as well as status bars (monitor-based SLOs) or bar graphs (metric-based SLOs) of the SLI's history. If you created a grouped monitor-based SLO using one [multi alert monitor](https://docs.datadoghq.com/monitors/types/metric/?tab=threshold#alert-grouping) or a grouped metric-based SLO using the [`sum by` clause](https://docs.datadoghq.com/service_level_objectives/metric/#define-queries), the status percentage and remaining error budget for each individual group is displayed in addition to the overall status percentage and remaining error budget.

**Example:** If you create a monitor-based SLO to track latency per availability-zone, the status percentages and remaining error budget for the overall SLO and for each individual availability-zone that the SLO is tracking are displayed.

**Note:** The remaining error budget is displayed as a percentage and is calculated using the following formula:

$$\text"error budget remaining" = 100 * {\text"current status" - \text" target"} / { 100 - \text"target"}$$

### Setting SLO targets{% #setting-slo-targets %}

To leverage the benefits of error budgets and error budget alerts, you must set SLO target values strictly below 100%.

Setting a 100% target means having an error budget of 0% since error budget is equal to 100%âSLO target. Without error budget representing acceptable risk, you face difficulty finding alignment between the conflicting priorities of maintaining customer-facing reliability and investing in feature development. In addition, SLOs with target values of 100% lead to division by zero errors in SLO alert evaluation.

**Note:** The number of decimal places you can specify for your SLOs differs depending on the type of SLO and the time windows you choose. Refer to the links below for more information for each respective SLO type.

[Monitor-based SLOs](https://docs.datadoghq.com/service_level_objectives/monitor/#set-your-slo-targets): Up to two decimal places are allowed for 7-day and 30-day targets, up to three decimal places are allowed for 90-day targets.

[Metric-based SLOs](https://docs.datadoghq.com/service_level_objectives/metric/#set-your-slo-targets): Up to three decimal places are allowed for all targets.

## Edit an SLO{% #edit-an-slo %}

To edit an SLO, hover over the SLO's row in the list view and click the edit pencil icon that appears at the right of the row, or click on the row to open the details side panel and select the edit button from the cog icon in the top right of the panel.

## Permissions{% #permissions %}

### Role based access{% #role-based-access %}

All users can view SLOs and SLO status corrections, regardless of their associated [role](https://docs.datadoghq.com/account_management/rbac/). Only users attached to roles with the `slos_write` permission can create, edit, and delete SLOs.

To create, edit, and delete status corrections, users require the `slos_corrections` permissions. A user with this permission can make status corrections, even if they do not have permission to edit those SLOs. For the full list of permissions, see the [RBAC documentation](https://docs.datadoghq.com/account_management/rbac/permissions/#service-level-objectives/).

### Granular access controls{% #granular-access-controls %}

Restrict access to individual SLOs by specifying a list of [roles](https://docs.datadoghq.com/account_management/rbac/) that are allowed to edit it.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo_set_permissions.8701629b5d044607a2db67c2adf9039f.png?auto=format"
   alt="SLO permissions option in the cog menu" /%}

1. Click on the SLO to open the details side panel.
1. Click the cog icon in the upper right of the panel.
1. Select **Permissions**.
1. Click **Restrict Access**.
1. The dialog box updates to show that members of your organization have **Viewer** access by default.
1. Use the drop-down to select one or more roles, teams, or users that may edit the SLO.
1. Click **Add**.
1. The dialog box updates to show that the role you selected has the **Editor** permission.
1. Click **Save**

To maintain your edit access to the SLO, the system requires you to include at least one role that you are a member of before saving. Users on the access control list can add roles and can only remove roles other than their own.

**Note**: Users can create SLOs on any monitor even if they do not have write permissions to the monitor. Similarly, users can create SLO alerts even if they do not have write permissions to the SLO. For more information on RBAC permissions for Monitors, see the [RBAC documentation](https://docs.datadoghq.com/account_management/rbac/permissions/#monitors) or the [guide on how to set up RBAC for Monitors](https://docs.datadoghq.com/monitors/guide/how-to-set-up-rbac-for-monitors/).

## Searching SLOs{% #searching-slos %}

The [Service Level Objectives manage page](https://app.datadoghq.com/slo) lets you run an advanced search of all SLOs so you can find, view, edit, clone or delete SLOs from the search results.

Advanced search lets you query SLOs by any combination of SLO attributes:

- `name` and `description` - text search
- `time window` - 7d, 30d, 90d
- `type` - metric, monitor
- `creator`
- `tags` - datacenter, env, service, team, etc.

To run a search, use the facet checkboxes on the left and the search bar at the top. When you check the boxes, the search bar updates with the equivalent query. Likewise, when you modify the search bar query (or write one from scratch), the checkboxes update to reflect the change. Query results update in real-time as you edit the query; there's no 'Search' button to click.

## Viewing SLOs{% #viewing-slos %}

Group your SLOs by *any* tag to get a summary view of your data. You can quickly analyze how many SLOs are in each state (breached, warning, OK, and no data), grouped by service, team, user journey, tier, or any other tag set on your SLOs.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo_group_by_new.f1069736af79e9552c85689b157e011f.png?auto=format"
   alt="Summary view of SLOs grouped by Team" /%}

Sort SLOs by the *status* and *error budget* columns to prioritize which SLOs need your attention. The SLO list displays the details of SLOs over the primary time window selected in your configuration. All other configuration time windows are available to view in the individual side panel. Open the SLO details side panel by clicking the respective table row.

**Note**: You can view your SLOs from your mobile device home screen by downloading the [Datadog Mobile App](https://docs.datadoghq.com/mobile), available on the [Apple App Store](https://apps.apple.com/app/datadog/id1391380318) and [Google Play Store](https://play.google.com/store/apps/details?id=com.datadog.app).

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slos-mobile.2e3f7eb20e329a0c8d3a98fc612abf50.png?auto=format"
   alt="SLOs on iOS and Android" /%}

### SLO tags{% #slo-tags %}

SLO tags can be used for filtering on the [SLO manage page](https://app.datadoghq.com/slo), creating [SLO saved views](https://docs.datadoghq.com/service_level_objectives/#saved-views), or grouping SLOs to view. Tags can be added to SLOs in the following ways:

- When you create or edit an SLO, you can add tags
- From the SLO list view, you can add and update tags in bulk using the *Edit Tags* and the *[Edit Teams](https://docs.datadoghq.com/account_management/teams/#associate-resources-with-team-handles)* dropdown options at the top of the SLO list.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo_bulk_tag.1b5eb16502ae2be839adc2c9b05e1f26.png?auto=format"
   alt="SLO list page displays the Edit Tag dropdown for bulk tag editing" /%}

### SLO burn rate indicator{% #slo-burn-rate-indicator %}

Burn rate indicators use a rolling 2-hour window to evaluate which SLOs are consuming their error budget too quickly. Burn rate indicators appear next to the applicable SLO names on the [SLO manage page](https://app.datadoghq.com/slo).

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo_burn_rate_indicator.5dcfb0541cc7e89e3566f7693a2e8a72.png?auto=format"
   alt="The SLO manage page in Datadog. A red icon appears next to the name of an SLO in the list. Mousing over the red icon displays a modal with further information, a burn rate visualization, and a link to the SLO's corresponding service page." /%}

There are two possible indicator types:

- A red icon indicating a critical burn rate above 6 in the past 2 hours.
- A yellow icon indicating an elevated burn rate between 1 and 6 in the past 2 hours.

A visual chart accompanies each indicator to show where the burn rate falls relative to the elevated and critical thresholds, allowing quick assessment of the severity.

SLOs can be filtered by burn rate status: Critical, Elevated, and Healthy. For SLOs with a service tag, each burn rate indicator includes a direct link to the related service page for further investigation.

### SLO default view{% #slo-default-view %}

The default SLO view is loaded when you land on the SLO list view.

The default view includes:

- An empty search query
- A list of all defined SLOs in your organization
- A list of available facets in left side facet list

### Saved views{% #saved-views %}

Saved views allow you to save and share customized searches in the SLO list view for SLOs that are most relevant for you and your team by sharing:

- A search query
- A selected subset of facets

After you query for a subset of SLOs on the list view, you can add that query as a saved view.

#### Add a saved view{% #add-a-saved-view %}

To add a saved view:

1. Query for your SLOs.
1. Click **Save View +** at the top left of the page.
1. Name your view and save.

#### Load a saved view{% #load-a-saved-view %}

To load a saved view, open the *Saved Views* panel by pressing the **Show Views** button at the top left of the page and select a saved view from the list. You can also search for saved views in the *Filter Saved Views* search box at the top of that same *Saved Views* panel.

#### Share a saved view{% #share-a-saved-view %}

Hover over a saved view from the list and select the hyperlink icon to copy the link to the saved view to share it with your teammates.

#### Manage saved views{% #manage-saved-views %}

Once you are using a saved view, you can update it by selecting that saved view, modifying the query, and clicking the *Update* button below its name in the *Saved Views* panel. To change the saved view's name or delete a saved view, hover over its row in the *Saved Views* panel and click the pencil icon or trash can icon, respectively.

## SLO and SLO status correction audit events{% #slo-and-slo-status-correction-audit-events %}

SLO audit events allow you to track the history of your SLO configurations using the [Event Explorer](https://docs.datadoghq.com/events/explorer/) or the **Audit History** tab in the SLO details. Audit events are added to the Event Explorer every time you create, modify, or delete an SLO or SLO status correction. Each event includes information on the configuration of an SLO or SLO status correction, and the stream provides a history of the configuration changes over time.

### SLO audit events{% #slo-audit-events %}

Each event includes the following SLO configuration information:

- Name
- Description
- Target percentages and time windows
- Datasources (monitor IDs or metric query)

Three types of SLO audit events appear in the Event Explorer:

- `SLO Created` events show the SLO configuration information at creation time
- `SLO Modified` events show what configuration information changed during a modification
- `SLO Deleted` events show the configuration information the SLO had before it was deleted

### Status correction audit events{% #status-correction-audit-events %}

Each event includes the following SLO status correction configuration information:

- SLO Name
- Status correction start and end times with timezone
- Status correction category

Three types of SLO status correction audit events appear in the Event Explorer:

- `SLO Correction Created` events show the status correction configuration information at creation time
- `SLO Correction Modified` events show what configuration information changed during a modification
- `SLO Correction Deleted` events show the configuration information the status correction had before it was deleted

To get a full list of all SLO audit events, enter the search query `tags:(audit AND slo)` in the Event Explorer. To view the list of audit events for a specific SLO, enter `tags:audit,slo_id:<SLO ID>` with the ID of the desired SLO. You can also query the Event Explorer programmatically using the [Datadog Events API](https://docs.datadoghq.com/api/latest/events/).

**Note:** If you don't see events appear in the UI, be sure to set the time frame of the Event Explorer to a longer period, for example, the past 7 days.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo-audit-events.d430b3fef301d4e7ef9707902252d483.png?auto=format"
   alt="SLO audit events" /%}

You can also use the "Audit History" tab in the SLO details to view all audit events for an individual SLO:

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo_audit_history_tab.5bd082f9f2619b39bf1f6aa4cc8159a1.png?auto=format"
   alt="SLO details audit history tab" /%}

With [Event Monitors](https://docs.datadoghq.com/monitors/types/event/), you can set up notifications to track SLO audit events. For example, if you wish to be notified when a specific SLO's configuration is modified, set an Event Monitor to track the text `[SLO Modified]` over the tags `audit,slo_id:<SLO ID>`.

## SLO widgets{% #slo-widgets %}

{% callout %}
##### Try Creating Business-Critical Insights Using Dashboards and SLOs in the Learning Center

Learn without cost on real cloud compute capacity and a Datadog trial account. Enroll today to learn more about building Dashboards to track SLOs.

[ENROLL NOW](https://learn.datadoghq.com/courses/dashboards-slos)
{% /callout %}

After creating your SLO, you can visualize the data through Dashboards and widgets.

- Use the SLO widget to visualize the status of a single SLO
- Use the SLO List widget to visualize a set of SLOs
- Graph 15 months' worth of metric-based SLO data with the [SLO data source](https://docs.datadoghq.com/dashboards/guide/slo_data_source/) in both timeseries and scalar (query value, top list, table, change) widgets.

For more information about SLO Widgets, see the [SLO widget](https://docs.datadoghq.com/dashboards/widgets/slo/) and [SLO List widget](https://docs.datadoghq.com/dashboards/widgets/slo_list/) pages. For more information on the SLO data source, see the guide on how to [Graph historical SLO data on Dashboards](https://docs.datadoghq.com/dashboards/guide/slo_data_source/).

## SLO status corrections{% #slo-status-corrections %}

Status corrections allow you to exclude specific time periods from SLO status and error budget calculations. This way, you can:

- Prevent expected downtime, such as scheduled maintenance, from depleting your error budget
- Ignore non-business hours, where you're not expected to conform to your SLOs
- Ensure that temporary issues caused by deployments do not negatively impact your SLOs

When you apply a correction, the time period you specify is dropped from the SLO's calculation.

- For monitor-based SLOs, the correction time window is not counted.
- For metric-based SLOs, all good and bad events in the correction window are not counted.
- For Time Slice SLOs, the correction time window is treated as uptime.

You have the option to create one-time corrections for ad hoc adjustments, or recurring corrections for predictable adjustments that occur on a regular cadence. One-time corrections require a start and end time, while recurring corrections require a start time, duration, and interval. Recurring corrections are based on [iCalendar RFC 5545's RRULE specification](https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html). The supported rules are `FREQ`, `INTERVAL`, `COUNT`, and `UNTIL`. Specifying an end date for recurring corrections is optional in case you need the correction to repeat indefinitely.

For either type of correction, you must select a correction category that states why the correction is being made. The available categories are `Scheduled Maintenance`, `Outside Business Hours`, `Deployment`, and `Other`. You can optionally include a description to provide additional context if necessary.

Each SLO has a maximum limit of corrections that can be configured to ensure query performance. These limits only apply to the past 90 days per SLO, so corrections for time periods before the past 90 days do not count towards your limit. This means that:

- If the end time of a one-time correction is before the past 90 days, it does count towards your limit.
- If the end time of the final repetition of a recurring correction is before the past 90 days, it does not count towards your limit.

The 90-day limits per SLO are as follows:

| Correction Type   | Limit per SLO |
| ----------------- | ------------- |
| One-time          | 100           |
| Daily recurring   | 2             |
| Weekly recurring  | 3             |
| Monthly recurring | 5             |

You may configure status corrections through the UI by selecting `Correct Status` in your SLO's side panel, the [SLO status corrections API](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/), or a [Terraform resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/slo_correction).

#### Access in the UI{% #access-in-the-ui %}

To access SLO status corrections in the UI:

1. Create a new SLO or click on an existing one.
1. Navigate to an SLO's details side panel view.
1. Under the gear icon, select **Correct Status** to access the **Status Corrections** creation modal.
1. Choose between `One-Time` and `Recurring` in the **Select the Time Correction Window**, and specify the time period you wish to correct.
1. Select a **Correction Type**.
1. Optionally add **Notes**.
1. Click **Apply Correction**.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo-corrections-ui.afd5b3f2d7335f013a5045214751e871.png?auto=format"
   alt="SLO correction UI" /%}

To view, edit, and delete existing status corrections, click on the **Corrections** tab at the top of an SLO's detailed side panel view.

#### Visualizing status corrections{% #visualizing-status-corrections %}

For Metric-based and Time Slice SLOs with status corrections, there is a toggle in the SLO detail view that lets you enable or disable corrections in the UI. The toggle controls the charts and data in the "History" section of the SLO detail view. **Note:** Your overall SLO status and error budget will always take status corrections into consideration.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/correction-toggle.941b960707b8c99c00dd038615d1d9ab.png?auto=format"
   alt="SLO correction UI" /%}

## SLO calendar view{% #slo-calendar-view %}

The SLO Calendar View is available on the [SLO manage page](https://app.datadoghq.com/slo). On the top right corner, switch from the "Primary" view to the "Daily", "Weekly", or "Monthly" view to see 12 months of historical SLO status data. The Calendar View is supported for Metric-based SLOs and Time Slice SLOs.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo-calendar-view-2.a0b169a7eee7cc9c57841ec9a64e93b4.png?auto=format"
   alt="SLO calendar view" /%}

## SLO CSV export{% #slo-csv-export %}

{% callout %}
##### Try Out the SLO CSV Export Feature

The CSV Export feature is in Preview. Complete the form to request access.

[Request Access](https://forms.gle/GQkcHDqaL5qWMss38)
{% /callout %}

The SLO CSV Export feature is available on the [SLO manage page](https://app.datadoghq.com/slo) once you switch to the "Weekly" or "Monthly" Calendar View. In these views, you can access the new "Export to CSV" option to download a CSV of your historical SLO data with the following information:

- SLO id, name, and type
- SLO tags
- SLO target
- Historical SLO status values

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo-csv-export.ce6610526ad806f193f622fb5ecd7b50.png?auto=format"
   alt="SLO calendar view" /%}

The following time windows are available for the CSV export:

- **Weekly:** The SLO statuses are based on calendar-aligned weeks (Sunday 12am - Saturday 11:59pm)
- **Monthly:** The SLO statuses are based on calendar-aligned months (First day of the month 12am - last day of the month 11:59pm)

These times are based on the user's timezone setting in Datadog.

The SLO statuses are calculated based on the SLO type:

- **Metric-based SLOs:** Percent of good events out of total events for the time window
- **Time Slice SLOs:** Percent of good minutes out of total minutes for the time window

**Notes:**

- The SLOs that are exported are based on your search query.
- The Calendar View is supported for Metric-based and Time Slice SLOs. If you export any Monitor-based SLOs, only the SLO ID and name are included in the CSV (not the SLO's status history data).
- There is a limit of 1000 SLOs per export.

## Further Reading{% #further-reading %}

- [Track the status and error budget of your SLOs with Datadog](https://www.datadoghq.com/blog/slo-monitoring-tracking/)
- [Introduction to Service Level Objectives](https://learn.datadoghq.com/courses/intro-to-slo)
- [Service Telemetry, Error Tracking, SLOs and more](https://www.datadoghq.com/blog/service-page/)
- [Proactively monitor service performance with SLO alerts](https://www.datadoghq.com/blog/monitor-service-performance-with-slo-alerts/)
- [Key questions to ask when setting SLOs](https://www.datadoghq.com/blog/slo-key-questions/)
- [Best practices for managing your SLOs with Datadog](https://www.datadoghq.com/blog/define-and-manage-slos/)
- [Create and manage SLOs with Terraform](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/service_level_objective)
- [Burn Rate is a Better Error Rate](https://www.datadoghq.com/blog/burn-rate-is-better-error-rate/)
