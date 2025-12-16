# Source: https://www.metabase.com/docs/latest/usage-and-performance-tools/usage-analytics

<div>

1.  [Home](/docs/latest/)
2.  [Usage and Performance Tools](/docs/latest/usage-and-performance-tools/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Usage analytics

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Usage analytics is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

The **Usage analytics** collection is a special collection that contains view-only questions, dashboards, and models that help you understand how people are using your Metabase.

![Usage analytics collection](./images/metabase-analytics.png)

You can find the **Usage analytics** collection under **collections** in the left navigation sidebar. You can also create custom reports.

These resources are useful for:

-   **Understanding Usage**: Understand how people use your Metabase (e.g., new questions, most active people and groups, and so on).
-   **Auditing activity**: Know who viewed or did what and when, including tracking dashboard and question views, queries, downloads, and other activity like changing settings or inviting people to your Metabase.
-   **Improving operations**: Know the slowest dashboards and questions, how your database's are performing, who's consuming the most resources, and so on.

> Metabase creates some default user accounts that you might see in your usage analytics, like `internal@metabase.com`. See [Default accounts](../people-and-groups/managing#default-user-accounts).

## Access to Usage analytics

You can find the **Usage analytics** collection under **collections** in the navigation sidebar. By default, only admins can see the Usage analytics collection, but admins can grant other groups view access to it. You can manage permissions for the collection in **Admin settings** \> **Permissions** \> **Collections**.

There are only two access types for the Usage analytics collection: **View** and **No access**. Even admins can't curate Usage analytics.

Additionally, this Usage analytics collection has a default sub-collection called "Custom reports" which you can use to save duplicated/modified questions, dashboards, and models. This sub-collection inherits the same permissions, but it's not view-only; admins have curate access by default, and can grant other groups view access.

> If you're upgrading from a version older than 48, people in groups with monitoring access will also get access to the Usage analytics collection. But after that initial grandfathering in, the monitoring access privilege is unrelated to the Usage analytics collection; you'll need to specifically grant groups access to the Usage analytics collection.

## Viewing usage insights for a question, dashboard, or model

> Only people in groups with view access to the Usage analytics collection will see this Usage insights option.

To view usage analytics for a question, dashboard, or model:

-   Visit the item.
-   Click on the info button in the upper right.
-   Click **Insights**.

Metabase will take you to the relevant usage dashboard and plug in the item's ID.

## How long Metabase keeps usage data

By default, Metabase will keep the data about [activity](#activity-log-model), [views](#view-log-model), and [query execution](#query-log-model) for **720 days**. Twice a day, Metabase will delete rows older than this threshold. You can change this limit by adjusting the environment variable [`MB_AUDIT_MAX_RETENTION_DAYS`](../configuring-metabase/environment-variables#mb_audit_max_retention_days).

If you're on the Metabase Open Source Edition, or on the [Metabase Cloud Starter plan](/pricing/), Metabase doesn't collect [Activity](#activity-log-model) and [View](#view-log-model) data. If you upgrade to a Pro or Enterprise plan, either self-hosted or Cloud, you'll only see View and Activity data in Usage Analytics *starting from the time when you upgraded*.

## Creating custom reports

You can duplicate any of the questions, dashboards and models in the Usage analytics collection and tweak them to your liking, but you'll need to save them to a different collection.

### Custom reports collection

While you *can* save custom questions, models, and dashboards wherever you like (except for the Usage analytics collection), we recommend that you save your custom Usage analytics reports in the conveniently named "Custom reports" sub-collection. That way these items inherit the same permissions as the parent Usage analytics collection.

There is one thing to know about the Custom reports collection: its metadata resets whenever Metabase restarts. While you are able to temporarily rename the Custom reports collection, or give it a description or an Official badge, Metabase will drop this collection's metadata when it restarts. But rest assured that Metabase will preserve any questions, models, events, or dashboards that you add to the Custom reports collection.

## Dashboards

The Usage analytics collection includes a set of read-only dashboards.

### Metabase metrics dashboard

General information about people viewing and creating dashboards, questions, subscriptions, and alerts. Cards include:

-   Active users last week
-   Question views last week
-   Questions created last week
-   Dashboards created last week
-   Alerts and subscriptions created last week
-   Weekly active users
-   Question views per week
-   Most active users
-   Most active creators
-   Most viewed dashboards
-   Most viewed cards

### Most viewed content dashboard

View the most relevant content in your Metabase. Cards include:

-   Most viewed dashboards
-   Most viewed questions
-   Most viewed tables

### Person overview dashboard

See what someone's been up to in your Metabase. Cards include:

-   Member of
-   Active alerts
-   Questions created per month
-   Question views per month
-   Most viewed dashboards
-   Most viewed questions
-   Last viewed dashboards
-   Last viewed questions
-   Last viewed tables
-   Recent activity
-   Last queries

### Dashboard overview dashboard

Information about dashboards, questions, models, and tables. Cards include:

-   Dashboard metadata
-   Dashboard views per month
-   Question performance
-   Most active people on this dashboard
-   Questions in this dashboard
-   Most active people on this dashboard
-   Questions in this dashboard
-   Recent activity on dashboard
-   Subscriptions on this dashboard

### Question overview dashboard

Views, performance, activity, and other data for a particular question. Cards include:

-   Question metadata
-   Question views per month
-   Question performance
-   Most active people on this question
-   Dashboards with this question
-   Last activity on this question
-   Alerts on this question

### Performance overview dashboard

Question, dashboard and database performance. Cards include:

-   Slowest dashboards
-   Dashboards consuming most resources
-   Slowest questions
-   Questions consuming the most resources
-   Dashboards with more questions in the same tab
-   Users consuming the most resources

> If you're using MySQL or MariaDB as your application database, the Performance overview dashboard won't display results for the cards displaying the 50th and 90th percentile query running times, because MySQL and MariaDB don't support the [Percentile aggregation](../questions/query-builder/expressions-list#percentile). We recommend using PostgreSQL as your application database.

### Content with cobwebs dashboard

Dashboards and questions that you could consider archiving. Cards include:

-   Dashboards without recent reviews
-   Questions without recent reviews
-   Questions that don't belong to a dashboard

## Models

The Usage analytics collection includes a bunch of useful models based on Metabase's application database.

## Activity log model

Each row of this model describes one event of a particular topic. Fields include:

-   ID
-   Topic
-   Timestamp
-   End Timestamp
-   User ID
-   Model
-   Model ID
-   Details

The topics include:

-   alert-create
-   alert-delete
-   card-create
-   card-delete
-   card-update
-   dashboard-add-cards
-   dashboard-create
-   dashboard-delete
-   dashboard-remove-cards
-   install
-   metric-create
-   metric-delete
-   metric-update
-   segment-create
-   segment-delete
-   segment-update
-   setting-update
-   subscription-create
-   subscription-delete
-   user-joined

## View log model

Tracks views cards (which includes models), dashboards, and tables. Fields include:

-   ID
-   Timestamp
-   User ID
-   Entity Type (card, dashboard, or table)
-   Entity ID
-   Entity Qualified ID

## Query log model

Information about all queries Metabase ran across all dashboards. Fields include:

-   Entity ID
-   Started At
-   Running Time Seconds
-   Result Rows
-   Is Native
-   Query Source
-   Error
-   User ID
-   Card ID
-   Card Qualified ID
-   Dashboard ID
-   Dashboard Qualified ID
-   Pulse ID
-   Database ID
-   Database Qualified ID
-   Cache Hit
-   Action ID

Query sources include:

-   action
-   ad-hoc
-   collection
-   csv-download
-   dashboard
-   embedded-dashboard
-   embedded-csv-download
-   embedded-json-download
-   embedded-question
-   embedded-xlsx-download
-   json-download
-   map-tiles
-   metabot (experimental)
-   public-dashboard
-   public-question
-   pulse (which includes dashboard subscriptions and alerts)
-   question
-   xlsx-download

## Alerts model

All alerts, both active and archived.

-   Entity ID
-   Entity Qualified ID
-   Created At
-   Updated At
-   Creator ID
-   Card ID
-   Card Qualified ID
-   Alert Condition
-   Schedule Type
-   Schedule Day
-   Schedule Hour
-   Archived
-   Recipient Type
-   Recipients
-   Recipient External

### Content model

Questions, dashboards, models, events, and collections.

-   Entity ID
-   Entity Qualified ID
-   Entity Type
-   Created At
-   Updated At
-   Creator ID
-   Name
-   Description
-   Collection ID
-   Made Public By User
-   Is Embedding Enabled
-   Archived
-   Action Type
-   Action Model ID
-   Collection Is Official
-   Collection Is Personal
-   Question Viz Type
-   Question Database ID
-   Question Is Native
-   Event Timestamp

Entity types include:

-   action
-   collection
-   dashboard
-   event
-   model
-   question

## People model

Everyone in your Metabase, including deactivated accounts. Fields include:

-   User ID
-   Email
-   First Name
-   Last Name
-   Full Name
-   Date Joined
-   Last Login
-   Updated At
-   Is Admin
-   Is Active
-   SSO Source
-   Locale

## Dashboard subscriptions model

Which subscriptions are active, who created them, who's subscribed to them, when they're sent, and more.

-   Entity ID
-   Entity Qualified ID
-   Created At
-   Updated At
-   Creator ID
-   Archived
-   Dashboard Qualified ID
-   Schedule Type
-   Schedule Day
-   Schedule Hour
-   Recipient Type
-   Recipients
-   Recipient External
-   Parameters

## Dashboard cards model

Each row is a dashboard card: either a question card or a text card. Fields include:

-   ID
-   Dashboard ID
-   Dashboardtab ID
-   Question ID
-   Created At
-   Updated At
-   Size X
-   Size Y
-   Visualization Settings
-   Parameter Mappings

## Databases model

Information about your connected data sources. Fields include:

-   Entity ID
-   Entity Qualified ID
-   Created At
-   Updated At
-   Name
-   Description
-   Database Type
-   Metadata Sync Schedule
-   Cache Field Values Schedule
-   Timezone
-   Is On Demand
-   Auto Run Queries
-   Cache Ttl
-   Creator ID
-   Db Version

## Tables model

List of all tables across all connected data sources. Fields include:

-   Entity ID
-   Entity Qualified ID
-   Created At
-   Updated At
-   Name
-   Display Name
-   Description
-   Active
-   Database ID
-   Schema
-   Is Upload

## Fields model

All fields from all connected data sources. Fields include:

-   Entity ID
-   Entity Qualified ID
-   Created At
-   Updated At
-   Name
-   Display Name
-   Description
-   Base Type
-   Visibility Type
-   Fk Target Field ID
-   Has Field Values
-   Active
-   Table ID

## System tasks model

Describes the last 14 days of Metabase internal processes tasks.

-   ID
-   Task
-   Database Qualified ID
-   Started At
-   Ended At
-   Duration Seconds
-   Details

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/usage-and-performance-tools/usage-analytics.md) ]