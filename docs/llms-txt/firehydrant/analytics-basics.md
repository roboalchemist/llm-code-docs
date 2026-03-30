# Source: https://docs.firehydrant.com/docs/analytics-basics.md

# Analytics Basics

> 📘 Note:
>
> Analytics require [Enterprise tier](https://firehydrant.com/pricing/). By default, all `GAMEDAY` and `MAINTENANCE` severity incidents are excluded from analytics.

FireHydrant provides in-depth analytics so you can understand the health and state of your organization. The Analytics are split into the following subpages:

* **[Incidents and Impact](https://docs.firehydrant.com/docs/analytics-incidents-and-impact)** - Statistics and metrics on incidents by components, severity, and more
* **[Resources and Tasks](https://docs.firehydrant.com/docs/analytics-resources-and-tasks)** - Graphs and charts of Retrospectives, Tasks/Follow-Ups completion, and incidents by team
* **[Alerting Analytics](https://docs.firehydrant.com/docs/analytics-alerts)** - Statistics on alerts, acknowledgments, and incidents, as well as MTTA and MTTR. Groupable and filterable by components, teams, tags, and more
* **[Exporting Data](https://docs.firehydrant.com/docs/analytics-exporting-data)** - FireHydrant supports exporting data in a variety of ways, including via API and throughout multiple pages in the web interface

To read more about each of these, visit the corresponding pages for each section.

## Quickstart

<Image align="center" alt="Filters at the top of each Analytics page" border={false} caption="Filters at the top of each Analytics page" src="https://files.readme.io/311cf28-image.png" width="650px" />

### Filtering Data

FireHydrant allows filtering the data shown on the analytics pages so you can see the information you're interested in.

1. **Grouped by** - The MTTX analytics page has a grouping dropdown where you can lay out the data and group results according to specific entities. Some options include:
   1. **Service** - Impacted services on incidents
   2. **Environment** - Impacted environments on incidents
   3. **Functionality** - Impacted functionalities on incidents
   4. **Team** - Assigned Teams on incidents
   5. **Severity** - Severity of incidents
   6. **User** - Assigned users on incidents
   7. **Custom Fields** - Any custom fields created and managed by your organization
2. **Select a date range** - By default, the Date Range is set to the previous 30 days and filters in UTC timestamps. For example, if you select a date range of `03/20/2022 - 03/23/2022`, we will pull data between `03/20/2022 00:00:00 UTC` and `03/23/2022 23:59:59 UTC`. There are also quick date ranges available such as **Last 7 Days**, **Last Week**, and various others.

   <Image align="center" alt="Date range filter options on FireHydrant" border={false} caption="Date range filter options on FireHydrant" src="https://files.readme.io/3ab23d7-CleanShot_2024-08-09_at_15.45.08.png" width="650px" />
3. **Search query** - Some pages allow for querying specific incidents by name
4. **Choose a resolution** - Some pages have a Resolution dropdown which defaults to weekly, but you can change it to daily or monthly if desired. This will largely depend on what date range you are looking at.
5. **Display options** - Some pages allow toggling between **Grid** format, which displays each chart in a grid two graphs wide, or **List** format, which shows all the charts in single-column format. Responsiveness settings will automatically convert the page to **List** format if your screen/window is not wide enough to reasonably display in a grid.
6. **ptional] AAdd some filters**\*\* Conditional filters can be used to refine the specificity of your query. You can apply multiple filters and also save them into Saved Views. For example, you can specify filters for specific Teams or Services and save them as custom views for said teams. FireHydrant supports the following filters:
   1. **Core**
      1. **Severity** - Filter for incidents of specified severity or severities
      2. **Priority** - Filter for incidents of specified priority or priorities
      3. **Current milestone** - Filter for incidents currently at specified milestone(s). This is only supported for some Analytics pages
      4. **Incident Tags** - Filter for incidents with the specified tag(s)
      5. **Started after** - Incidents whose *Started* milestone are on or after selected date
      6. **Started before** - Incidents whose *Started* milestone are on or before selected date
      7. **Resolved after** - Incidents whose *Resolved* milestone are on or after selected date
      8. **Resolved before** - Incidents whose *Resolved* milestone are on or before selected date
      9. **Closed after** - Incidents whose *Closed* milestone are on or after selected date
      10. **Closed before** - Incidents whose *Closed* milestone are on or before selected date
      11. **Declared after** - Incidents declared on or after selected date
      12. **Declared before** - Incidents declared on or before selected date
      13. **Incident Labels** - Filter for incidents with the specified label(s)
      14. **Visibility** (private or public) - Filter for private or public incidents
      15. **Incident Type** - Filter for incidents created from the specified incident type(s)
   2. **Responders**
      1. **Service owning team** - Filter for incidents where specified team(s) had a service or functionality impacted. These teams may or may not have been directly assigned to the incident
      2. **Assigned team** - Filter for incidents where specified team(s) were explicitly assigned
      3. **Incident openers** - Filter for incidents declared by specified person(s)
      4. **Role assigned** - Filter for incidents where specified user(s) was assigned to specified role(s)
      5. **Role unassigned** - Filter for incidents where specified user(s) were unassigned from specified role(s)
   3. **Catalog**
      1. **Impacted services** - Filter for incidents where specified service(s) were impacted
      2. **Impacted functionalities** - Filter for incidents where specified functionality/functionalities were impacted
      3. **Impacted environments** - Filter for incidents where specified environment(s) were impacted
   4. **Ticketing**
      1. **Has tasks/follow-ups the given states** - Filter for incidents where there are tasks and/or follow-ups in the specified state(s)
   5. **\[[Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields) ]** - Filter for incidents where your custom field(s) are the specified value(s)
   6. **Other** - Other miscellaneous filters
      1. **Watched** - Incidents that the user is specifically watching
      2. **Archived** - Incidents that have been archived

> 📘 \*\*Note:
>
> These filters are also available on your Incidents page to search and filter the list of incidents.

### Exporting Graphs and CSV

Once you've filtered the data you'd like to see, each chart has a download icon at the top right, allowing you to export the image to PNG or export the data via CSV.

<Image align="center" alt="Exporting a specific chart" border={false} caption="Exporting a specific chart" src="https://files.readme.io/cd0d6fe-image.png" width="650px" />

Other pages, such as the MTTX Analytics page, will have CSV export capabilities for the data tables.

## Active Incidents

The **Incidents and Impact** and **Resources and Tasks** subpages show statistics for all incidents that were ***active*** at any point within the time window. For example, if your time window is set to one day, an incident created more than a day ago but is still ongoing would be included in the metrics. This may be why the number of incidents Created is mismatched with the number Resolved.

The **MTTX Analytics** and **Alerts** subpages only count statistics for resolved incidents.

## Private Incidents

[Private Incidents](https://docs.firehydrant.com/docs/private-incidents) will have their visibility and impact on Analytics determined by the specific user viewing the page. For example, if a user has Private permissions, they will see the full list of all incidents and impact in the analytics, (e.g., four public incidents and one private incident totaling 5).

But users with only Public permissions would not see the private incidents, so they'd only see statistics and metrics for four public incidents total.

## Next Steps

* Browse each of the specific analytics subpages we offer:
  * [Incidents and Impact](https://docs.firehydrant.com/docs/analytics-incidents-and-impact)
  * [Resources and Tasks](https://docs.firehydrant.com/docs/analytics-resources-and-tasks)
  * [Alerting Analytics](https://docs.firehydrant.com/docs/analytics-alerts)
  * [Exporting Data](https://docs.firehydrant.com/docs/analytics-exporting-data)
  * [Other Analytics](https://docs.firehydrant.com/docs/analytics-other)