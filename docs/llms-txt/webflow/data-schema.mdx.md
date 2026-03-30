# Source: https://developers.webflow.com/browser/data-exports/data-schema.mdx

***

title: Data schema
slug: data-exports/data-schema
description: Data models and schema reference for Data Exports
--------------------------------------------------------------

This page documents the data models available through Data Exports, including the tables and fields exported for Analyze, Optimize, and customers with both products.

## Overview

Data Exports delivers your Webflow analytics and optimization data as structured tables in your chosen destination. The specific data available depends on your Webflow subscription:

| Add-on             | Available data                      |
| ------------------ | ----------------------------------- |
| Analyze            | Page views and element clicks       |
| Optimize           | Variation viewed data               |
| Analyze & Optimize | All analytics and optimization data |

## Data freshness

* **Export frequency**: Data is exported on a nightly basis (every 24 hours)
* **Data latency**: Exported data reflects activity from the previous day
* **Historical data**: Not included. Only data from the established connection date going forward is exported

## Analyze data models

The following tables are available for customers with Webflow Analyze.

### Page views (`analyze_page_viewed`)

Records each page view on your site.

| Column        | Type      | Description                                                              |
| ------------- | --------- | ------------------------------------------------------------------------ |
| `customer_id` | string    | Your Analyze/Optimize customer ID                                        |
| `user_id`     | string    | Unique user identifier (useful for joining with other internal datasets) |
| `session_id`  | string    | Session identifier                                                       |
| `page_id`     | string    | Unique identifier for the page                                           |
| `page_url`    | string    | URL of the page viewed                                                   |
| `event_time`  | timestamp | Timestamp when the page was viewed (UTC)                                 |
| `event_date`  | string    | Date of the event (YYYY-MM-DD)                                           |

### Click events (`analyze_element_clicked`)

Records each element click event on your site.

| Column         | Type      | Description                                                              |
| -------------- | --------- | ------------------------------------------------------------------------ |
| `customer_id`  | string    | Your Analyze/Optimize customer ID                                        |
| `user_id`      | string    | Unique user identifier (useful for joining with other internal datasets) |
| `session_id`   | string    | Session identifier                                                       |
| `page_id`      | string    | Unique identifier for the page                                           |
| `page_url`     | string    | URL of the page where the click occurred                                 |
| `element_id`   | string    | Unique identifier for the clicked element                                |
| `element_name` | string    | Name of the clicked element                                              |
| `event_time`   | timestamp | Timestamp when the element was clicked (UTC)                             |
| `event_date`   | string    | Date of the event (YYYY-MM-DD)                                           |

## Optimize data models

The following tables are available for customers with Webflow Optimize.

### Variation views (`optimize_variation_viewed`)

Records each time a visitor views a variation in an optimization.

| Column              | Type      | Description                                                              |
| ------------------- | --------- | ------------------------------------------------------------------------ |
| `customer_id`       | string    | Your Analyze/Optimize customer ID                                        |
| `user_id`           | string    | Unique user identifier (useful for joining with other internal datasets) |
| `session_id`        | string    | Session identifier                                                       |
| `variation_id`      | string    | Unique identifier for the variation                                      |
| `optimization_id`   | string    | Unique identifier for the optimization                                   |
| `variation_name`    | string    | Name of the variation                                                    |
| `optimization_name` | string    | Name of the optimization                                                 |
| `event_time`        | timestamp | Timestamp when the variation was viewed (UTC)                            |
| `event_date`        | string    | Date of the event (YYYY-MM-DD)                                           |

## Schema evolution

As Data Exports evolves over time:

* New columns may be added to existing tables
* New tables may be introduced
* Existing columns will not be removed or renamed without advance notice

For data warehouse destinations, schema changes are handled automatically. For object storage destinations, you may need to handle schema evolution in your downstream processing.

## Data types by destination

Data types are mapped appropriately for each destination:

| Source type | Snowflake      | BigQuery  | Redshift  | PostgreSQL       |
| ----------- | -------------- | --------- | --------- | ---------------- |
| string      | VARCHAR        | STRING    | VARCHAR   | TEXT             |
| integer     | INTEGER        | INT64     | INTEGER   | INTEGER          |
| float       | FLOAT          | FLOAT64   | FLOAT     | DOUBLE PRECISION |
| boolean     | BOOLEAN        | BOOL      | BOOLEAN   | BOOLEAN          |
| timestamp   | TIMESTAMP\_NTZ | TIMESTAMP | TIMESTAMP | TIMESTAMP        |
| date        | DATE           | DATE      | DATE      | DATE             |
