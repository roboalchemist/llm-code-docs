# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.rum.dataset.md

---
title: RUM Events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RUM Events
---

# RUM Events

This dataset represents Real User Monitoring (RUM) events collected by Datadog. It captures user sessions, page views, user actions, frontend errors, resource loading, and performance metrics from web and mobile applications. RUM data enables analysis of user experience, frontend performance, and application behavior across browsers, devices, and geographic regions.

```
dd.rum
```
Real User Monitoring Public Documentation
{% icon name="icon-external-link" /%}
 RUM Browser Data Collected Documentation
{% icon name="icon-external-link" /%}

## Query Parameters

This dataset uses a **polymorphic table function**. You must specify parameters when querying.

| Parameter        | Type            | Required | Description                                                                                                                                                      |
| ---------------- | --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `columns`        | `array<string>` | Yes      | List of fields to return for each RUM event (e.g., 'timestamp', '@session.id', '@view.url', '@error.message'). Must follow with AS (â¦) to name and type outputs. |
| `event_type`     | `string`        | No       | Optional event subtype to filter by (e.g., event_type => 'error').                                                                                               |
| `filter`         | `string`        | No       | Optional search string. For example: filter => '@application.name:my-app AND @error.source:source'.                                                              |
| `from_timestamp` | `string`        | No       | Lower time bound for the query; defaults to the query context if omitted.                                                                                        |
| `to_timestamp`   | `string`        | No       | Upper time bound for the query; defaults to the query context if omitted.                                                                                        |

## Example Queries

```sql
-- Fetch recent RUM errors for a specific application
SELECT * FROM dd.rum(
  columns => ARRAY[
    'timestamp',
    '@session.id',
    '@view.url',
    '@error.source',
    '@error.type',
    '@error.message',
    '@usr.id'
  ],
  event_type => 'error',
  filter => '@application.name:my-web-app',
  from_timestamp => now() - interval '1 hour',
  to_timestamp => now()
) AS (
  ts           TIMESTAMP,
  session_id   VARCHAR,
  view_url     VARCHAR,
  error_source VARCHAR,
  error_type   VARCHAR,
  error_msg    VARCHAR,
  user_id      VARCHAR
);
```

## Fields

| Title                     | ID                              | Type            | Data Type | Description                                                                                                                                |
| ------------------------- | ------------------------------- | --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Timestamp                 | timestamp                       | core            | timestamp | Time the RUM event was recorded. Applies to: all.                                                                                          |
| Event Type                | @type                           | event_attribute | string    | Type of RUM event (session, view, action, error, resource, long_task). Applies to: all.                                                    |
| Application ID            | @application.id                 | event_attribute | string    | Unique identifier for the RUM application. Applies to: all.                                                                                |
| Application Name          | @application.name               | event_attribute | string    | Name of the RUM application (e.g., my-web-app). Applies to: all.                                                                           |
| Session ID                | @session.id                     | event_attribute | string    | Unique identifier for the user session. Applies to: all.                                                                                   |
| Session Type              | @session.type                   | event_attribute | string    | Type of session (user, synthetics). Applies to: all.                                                                                       |
| Session Active            | @session.is_active              | event_attribute | bool      | Whether the session is currently active. Applies to: session.                                                                              |
| Session Time Spent        | @session.time_spent             | event_attribute | int64     | Time spent in the session in nanoseconds. Applies to: session.                                                                             |
| Session View Count        | @session.view.count             | event_attribute | int64     | Number of views in the session. Applies to: session.                                                                                       |
| Session Error Count       | @session.error.count            | event_attribute | int64     | Number of errors in the session. Applies to: session.                                                                                      |
| Session Resource Count    | @session.resource.count         | event_attribute | int64     | Number of resources loaded in the session. Applies to: session.                                                                            |
| Session Action Count      | @session.action.count           | event_attribute | int64     | Number of actions in the session. Applies to: session.                                                                                     |
| Session Referrer          | @session.referrer               | event_attribute | string    | Referrer URL for the session. Applies to: session.                                                                                         |
| View ID                   | @view.id                        | event_attribute | string    | Unique identifier for the page view. Applies to: all.                                                                                      |
| View URL                  | @view.url                       | event_attribute | string    | URL of the page view. Applies to: all.                                                                                                     |
| View URL Host             | @view.url_host                  | event_attribute | string    | Host portion of the view URL. Applies to: all.                                                                                             |
| View URL Path             | @view.url_path                  | event_attribute | string    | Path portion of the view URL. Applies to: all.                                                                                             |
| View URL Path Group       | @view.url_path_group            | event_attribute | string    | Parameterized path group for the view URL. Applies to: all.                                                                                |
| View Loading Time         | @view.loading_time              | event_attribute | int64     | Time to fully load the page in nanoseconds. Applies to: view.                                                                              |
| View Time Spent           | @view.time_spent                | event_attribute | int64     | Time spent on the view in nanoseconds. Applies to: view.                                                                                   |
| First Contentful Paint    | @view.first_contentful_paint    | event_attribute | int64     | Time to first contentful paint in nanoseconds. Applies to: view.                                                                           |
| Largest Contentful Paint  | @view.largest_contentful_paint  | event_attribute | int64     | Time to largest contentful paint in nanoseconds. Applies to: view.                                                                         |
| First Input Delay         | @view.first_input_delay         | event_attribute | int64     | First input delay in nanoseconds. Applies to: view.                                                                                        |
| Interaction to Next Paint | @view.interaction_to_next_paint | event_attribute | int64     | Interaction to next paint (INP) in nanoseconds. Applies to: view.                                                                          |
| Cumulative Layout Shift   | @view.cumulative_layout_shift   | event_attribute | float64   | Cumulative layout shift score. Applies to: view.                                                                                           |
| DOM Interactive           | @view.dom_interactive           | event_attribute | int64     | Time to DOM interactive in nanoseconds. Applies to: view.                                                                                  |
| DOM Content Loaded        | @view.dom_content_loaded        | event_attribute | int64     | Time to DOM content loaded in nanoseconds. Applies to: view.                                                                               |
| DOM Complete              | @view.dom_complete              | event_attribute | int64     | Time to DOM complete in nanoseconds. Applies to: view.                                                                                     |
| Load Event                | @view.load_event                | event_attribute | int64     | Time to load event in nanoseconds. Applies to: view.                                                                                       |
| View Error Count          | @view.error.count               | event_attribute | int64     | Number of errors in the view. Applies to: view.                                                                                            |
| View Resource Count       | @view.resource.count            | event_attribute | int64     | Number of resources loaded in the view. Applies to: view.                                                                                  |
| View Action Count         | @view.action.count              | event_attribute | int64     | Number of actions in the view. Applies to: view.                                                                                           |
| View Frustration Count    | @view.frustration.count         | event_attribute | int64     | Number of frustration signals in the view. Applies to: view.                                                                               |
| Action ID                 | @action.id                      | event_attribute | string    | Unique identifier for the user action. Applies to: action.                                                                                 |
| Action Type               | @action.type                    | event_attribute | string    | Type of action (click, tap, scroll, custom). Applies to: action.                                                                           |
| Action Name               | @action.name                    | event_attribute | string    | User-friendly name for the action. Applies to: action.                                                                                     |
| Action Target Name        | @action.target.name             | event_attribute | string    | Name of the target element. Applies to: action.                                                                                            |
| Action Loading Time       | @action.loading_time            | event_attribute | int64     | Time to complete the action in nanoseconds. Applies to: action.                                                                            |
| Frustration Type          | @action.frustration.type        | event_attribute | string    | Type of frustration signal (dead_click, rage_click, error_click). Applies to: action.                                                      |
| Error Source              | @error.source                   | event_attribute | string    | Source of the error (source, network, agent, console, custom). Applies to: error.                                                          |
| Error Type                | @error.type                     | event_attribute | string    | Type or class of the error. Applies to: error.                                                                                             |
| Error Message             | @error.message                  | event_attribute | string    | Error message text. Applies to: error.                                                                                                     |
| Error Stack               | @error.stack                    | event_attribute | string    | Stack trace for the error. Applies to: error.                                                                                              |
| Resource Type             | @resource.type                  | event_attribute | string    | Type of resource (xhr, fetch, css, js, image, font, document). Applies to: resource.                                                       |
| Resource Method           | @resource.method                | event_attribute | string    | HTTP method for the resource request. Applies to: resource.                                                                                |
| Resource Status Code      | @resource.status_code           | event_attribute | int64     | HTTP status code of the resource response. Applies to: resource.                                                                           |
| Resource URL              | @resource.url                   | event_attribute | string    | URL of the resource. Applies to: resource.                                                                                                 |
| Resource Duration         | @resource.duration              | event_attribute | int64     | Time to load the resource in nanoseconds. Applies to: resource.                                                                            |
| Resource Size             | @resource.size                  | event_attribute | int64     | Size of the resource in bytes. Applies to: resource.                                                                                       |
| Resource Provider Name    | @resource.provider.name         | event_attribute | string    | Name of the third-party provider. Applies to: resource.                                                                                    |
| Resource Provider Type    | @resource.provider.type         | event_attribute | string    | Type of the third-party provider. Applies to: resource.                                                                                    |
| Long Task Duration        | @long_task.duration             | event_attribute | int64     | Duration of the long task in nanoseconds. Applies to: long_task.                                                                           |
| Device Type               | @device.type                    | event_attribute | string    | Type of device (desktop, mobile, tablet). Applies to: all.                                                                                 |
| Device Brand              | @device.brand                   | event_attribute | string    | Brand of the device (e.g., Apple, Samsung). Applies to: all.                                                                               |
| Device Model              | @device.model                   | event_attribute | string    | Model of the device (e.g., iPhone 14). Applies to: all.                                                                                    |
| OS Name                   | @os.name                        | event_attribute | string    | Operating system name (e.g., iOS, Android, Windows). Applies to: all.                                                                      |
| OS Version                | @os.version                     | event_attribute | string    | Operating system version. Applies to: all.                                                                                                 |
| OS Major Version          | @os.version_major               | event_attribute | string    | Major version of the operating system. Applies to: all.                                                                                    |
| Browser Name              | @browser.name                   | event_attribute | string    | Browser name (e.g., Chrome, Safari, Firefox). Applies to: all.                                                                             |
| Browser Version           | @browser.version                | event_attribute | string    | Browser version. Applies to: all.                                                                                                          |
| Browser Major Version     | @browser.version_major          | event_attribute | string    | Major version of the browser. Applies to: all.                                                                                             |
| Country                   | @geo.country                    | event_attribute | string    | Country name from geo IP lookup. Applies to: all.                                                                                          |
| Country ISO Code          | @geo.country_iso_code           | event_attribute | string    | ISO country code from geo IP lookup. Applies to: all.                                                                                      |
| City                      | @geo.city                       | event_attribute | string    | City name from geo IP lookup. Applies to: all.                                                                                             |
| Continent                 | @geo.continent                  | event_attribute | string    | Continent name from geo IP lookup. Applies to: all.                                                                                        |
| User ID                   | @usr.id                         | event_attribute | string    | Unique identifier for the user. Applies to: all.                                                                                           |
| User Email                | @usr.email                      | event_attribute | string    | Email address of the user. Applies to: all.                                                                                                |
| User Name                 | @usr.name                       | event_attribute | string    | Display name of the user. Applies to: all.                                                                                                 |
| Event ID                  | id                              | core            | string    | A unique identifier for the event.                                                                                                         |
| Discovery Timestamp       | discovery_timestamp             | core            | int64     | The time when Datadog first received the event (milliseconds since Unix epoch). May differ from timestamp if there was an ingestion delay. |
| Tiebreaker                | tiebreaker                      | core            | int64     | A value used to establish deterministic ordering among events that share the same timestamp.                                               |
| Ingest Size               | ingest_size_in_bytes            | core            | int64     | The size of the event payload in bytes at the time of ingestion, before any processing.                                                    |
| Random Draw               | random_draw                     | core            | float64   | A random value between 0.0 and 1.0 assigned at ingestion, useful for consistent sampling across queries.                                   |
