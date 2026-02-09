# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.product_analytics.dataset.md

---
title: Product Analytics
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Product Analytics
---

# Product Analytics

This dataset represents Product Analytics data collected by Datadog, built on top of Real User Monitoring (RUM). Product Analytics provides insights into user behavior, engagement, and conversion across web and mobile applications. It enables analysis of user journeys, funnels, feature adoption, and product usage patterns to drive data-driven product decisions.

```
dd.product_analytics
```
Product Analytics Public Documentation 
{% icon name="icon-external-link" /%}
 Product Analytics Explorer Documentation 
{% icon name="icon-external-link" /%}
 
## Query Parameters

This dataset uses a **polymorphic table function**. You must specify parameters when querying.

| Parameter        | Type            | Required | Description                                                                                                                                                |
| ---------------- | --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `columns`        | `array<string>` | Yes      | List of fields to return for each event (e.g., 'timestamp', '@session.id', '@view.url', '@action.name'). Must follow with AS (â¦) to name and type outputs. |
| `event_type`     | `string`        | No       | Optional event subtype to filter by (e.g., event_type => 'action').                                                                                        |
| `filter`         | `string`        | No       | Optional search string. For example: filter => '@application.name:my-app AND @action.type:click'.                                                          |
| `from_timestamp` | `string`        | No       | Lower time bound for the query; defaults to the query context if omitted.                                                                                  |
| `to_timestamp`   | `string`        | No       | Upper time bound for the query; defaults to the query context if omitted.                                                                                  |

## Example Queries

```sql
-- Analyze user actions for funnel analysis
SELECT * FROM dd.product_analytics(
  columns => ARRAY[
    'timestamp',
    '@session.id',
    '@usr.id',
    '@view.url',
    '@action.name',
    '@action.type',
    '@device.type',
    '@geo.country'
  ],
  event_type => 'action',
  filter => '@application.name:checkout-app',
  from_timestamp => now() - interval '7 days',
  to_timestamp => now()
) AS (
  ts           TIMESTAMP,
  session_id   VARCHAR,
  user_id      VARCHAR,
  page_url     VARCHAR,
  action_name  VARCHAR,
  action_type  VARCHAR,
  device_type  VARCHAR,
  country      VARCHAR
);
```

## Fields

| Title                     | ID                             | Type            | Data Type | Description                                                                                                                                |
| ------------------------- | ------------------------------ | --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Timestamp                 | timestamp                      | core            | timestamp | Time the event was recorded. Applies to: all.                                                                                              |
| Event Type                | @type                          | event_attribute | string    | Type of event (session, view, action). Applies to: all.                                                                                    |
| Application ID            | @application.id                | event_attribute | string    | Unique identifier for the application. Applies to: all.                                                                                    |
| Application Name          | @application.name              | event_attribute | string    | Name of the application (e.g., my-web-app). Applies to: all.                                                                               |
| Session ID                | @session.id                    | event_attribute | string    | Unique identifier for the user session. Applies to: all.                                                                                   |
| Session Type              | @session.type                  | event_attribute | string    | Type of session (user, synthetics). Applies to: all.                                                                                       |
| Session Active            | @session.is_active             | event_attribute | bool      | Whether the session is currently active. Applies to: session.                                                                              |
| Session Time Spent        | @session.time_spent            | event_attribute | int64     | Total time spent in the session in nanoseconds. Applies to: session.                                                                       |
| Session View Count        | @session.view.count            | event_attribute | int64     | Number of page views in the session. Applies to: session.                                                                                  |
| Session Action Count      | @session.action.count          | event_attribute | int64     | Number of user actions in the session. Applies to: session.                                                                                |
| Session Error Count       | @session.error.count           | event_attribute | int64     | Number of errors in the session. Applies to: session.                                                                                      |
| Session Frustration Count | @session.frustration.count     | event_attribute | int64     | Number of frustration signals in the session. Applies to: session.                                                                         |
| Session Referrer          | @session.referrer              | event_attribute | string    | Referrer URL that led to the session. Applies to: session.                                                                                 |
| Landing Page Path         | @session.initial_view.url_path | event_attribute | string    | Path of the first page viewed in the session. Applies to: session.                                                                         |
| Exit Page Path            | @session.last_view.url_path    | event_attribute | string    | Path of the last page viewed in the session. Applies to: session.                                                                          |
| View ID                   | @view.id                       | event_attribute | string    | Unique identifier for the page view. Applies to: view, action.                                                                             |
| View URL                  | @view.url                      | event_attribute | string    | Full URL of the page. Applies to: view, action.                                                                                            |
| View URL Host             | @view.url_host                 | event_attribute | string    | Host portion of the view URL. Applies to: view, action.                                                                                    |
| View URL Path             | @view.url_path                 | event_attribute | string    | Path portion of the view URL. Applies to: view, action.                                                                                    |
| View URL Path Group       | @view.url_path_group           | event_attribute | string    | Parameterized path group for grouping similar pages. Applies to: view, action.                                                             |
| View Name                 | @view.name                     | event_attribute | string    | User-friendly name for the page/view. Applies to: view, action.                                                                            |
| View Time Spent           | @view.time_spent               | event_attribute | int64     | Time spent on the page in nanoseconds. Applies to: view.                                                                                   |
| View Action Count         | @view.action.count             | event_attribute | int64     | Number of user actions on the page. Applies to: view.                                                                                      |
| View Error Count          | @view.error.count              | event_attribute | int64     | Number of errors on the page. Applies to: view.                                                                                            |
| View Frustration Count    | @view.frustration.count        | event_attribute | int64     | Number of frustration signals on the page. Applies to: view.                                                                               |
| Action ID                 | @action.id                     | event_attribute | string    | Unique identifier for the user action. Applies to: action.                                                                                 |
| Action Type               | @action.type                   | event_attribute | string    | Type of action (click, tap, scroll, custom). Applies to: action.                                                                           |
| Action Name               | @action.name                   | event_attribute | string    | User-friendly name for the action (e.g., 'Add to Cart', 'Submit Form'). Applies to: action.                                                |
| Action Target             | @action.target.name            | event_attribute | string    | Name or identifier of the target element. Applies to: action.                                                                              |
| Action Loading Time       | @action.loading_time           | event_attribute | int64     | Time to complete the action in nanoseconds. Applies to: action.                                                                            |
| Frustration Type          | @action.frustration.type       | event_attribute | string    | Type of frustration signal (dead_click, rage_click, error_click). Applies to: action.                                                      |
| User ID                   | @usr.id                        | event_attribute | string    | Unique identifier for the user. Applies to: all.                                                                                           |
| User Email                | @usr.email                     | event_attribute | string    | Email address of the user. Applies to: all.                                                                                                |
| User Name                 | @usr.name                      | event_attribute | string    | Display name of the user. Applies to: all.                                                                                                 |
| Device Type               | @device.type                   | event_attribute | string    | Type of device (desktop, mobile, tablet). Applies to: all.                                                                                 |
| Device Brand              | @device.brand                  | event_attribute | string    | Brand of the device (e.g., Apple, Samsung). Applies to: all.                                                                               |
| Device Model              | @device.model                  | event_attribute | string    | Model of the device. Applies to: all.                                                                                                      |
| OS Name                   | @os.name                       | event_attribute | string    | Operating system name (e.g., iOS, Android, Windows). Applies to: all.                                                                      |
| OS Version                | @os.version                    | event_attribute | string    | Operating system version. Applies to: all.                                                                                                 |
| Browser Name              | @browser.name                  | event_attribute | string    | Browser name (e.g., Chrome, Safari, Firefox). Applies to: all.                                                                             |
| Browser Version           | @browser.version               | event_attribute | string    | Browser version. Applies to: all.                                                                                                          |
| Country                   | @geo.country                   | event_attribute | string    | Country name from geo IP lookup. Applies to: all.                                                                                          |
| Country ISO Code          | @geo.country_iso_code          | event_attribute | string    | ISO country code from geo IP lookup. Applies to: all.                                                                                      |
| City                      | @geo.city                      | event_attribute | string    | City name from geo IP lookup. Applies to: all.                                                                                             |
| Continent                 | @geo.continent                 | event_attribute | string    | Continent name from geo IP lookup. Applies to: all.                                                                                        |
| Region                    | @geo.region                    | event_attribute | string    | Region or state name from geo IP lookup. Applies to: all.                                                                                  |
| Page Referrer             | @view.referrer                 | event_attribute | string    | Referrer URL for the page view. Applies to: view.                                                                                          |
| UTM Source                | @session.referrer_utm_source   | event_attribute | string    | UTM source parameter from the referrer. Applies to: session.                                                                               |
| Event ID                  | id                             | core            | string    | A unique identifier for the event.                                                                                                         |
| Discovery Timestamp       | discovery_timestamp            | core            | int64     | The time when Datadog first received the event (milliseconds since Unix epoch). May differ from timestamp if there was an ingestion delay. |
| Tiebreaker                | tiebreaker                     | core            | int64     | A value used to establish deterministic ordering among events that share the same timestamp.                                               |
| Ingest Size               | ingest_size_in_bytes           | core            | int64     | The size of the event payload in bytes at the time of ingestion, before any processing.                                                    |
| Random Draw               | random_draw                    | core            | float64   | A random value between 0.0 and 1.0 assigned at ingestion, useful for consistent sampling across queries.                                   |
