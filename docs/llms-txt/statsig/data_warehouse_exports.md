# Source: https://docs.statsig.com/integrations/data-exports/data_warehouse_exports.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Warehouse Exports

## Introduction

You can export your data from Statsig to your Data Warehouse with a Data Connection. This lets you send exposures and events directly to your warehouse for further analysis. We currently support connections to the following providers:

1. [Snowflake](/data-warehouse-ingestion/snowflake)
2. [Redshift](/data-warehouse-ingestion/redshift)
3. [S3](/data-warehouse-ingestion/s3)
4. [BigQuery](/data-warehouse-ingestion/bigquery)
5. [Databricks](/data-warehouse-ingestion/databricks)

<Info>
  Data Warehouse Exports are an Enterprise-only feature. If you are on the Developer or Pro tiers and wish to upgrade to Enterprise, feel free to reach out to our team [here](https://www.statsig.com/contact/demo) or via support.
</Info>

## How to Begin

1. Go to Statsig Console
2. Navigate to the Help and Tools Section on the side navigation bar
3. Go to “Exports List”

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/F2X5gKBIv-x0KuI9/images/exports-list.png?fit=max&auto=format&n=F2X5gKBIv-x0KuI9&q=85&s=201dc41d1f53c59a4078bfa40c21ffee" alt="Statsig Help and Tools menu showing Exports List option" width="3420" height="1804" data-path="images/exports-list.png" />
</Frame>

On the Exports page, you will find an Export History tab and a Schedule Export tab. The Export History tab shows you a list of all previous experimentation exports triggered from the Experiment Results page. To understand how to export one-off experimentation results, check out the documentation [here](/integrations/data-exports/experiment_result_exports).

Under the Scheduled Export tab, you will be prompted to set up a data warehouse connection. You will be required to set up connections with necessary credentials and grant Statsig Read, Write, and Delete permissions. Check out the example [Snowflake Connection Set Up](/data-warehouse-ingestion/snowflake) page for more information.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/F2X5gKBIv-x0KuI9/images/exports-schedule.png?fit=max&auto=format&n=F2X5gKBIv-x0KuI9&q=85&s=2101705eed7741a397c4d9bd3cc603a3" alt="Scheduled export setup form for Snowflake connection with credential fields" width="3330" height="1508" data-path="images/exports-schedule.png" />
</Frame>

## Table Schema

Statsig will allow you to export both Exposures and Events to your warehouse. During the set up process, we will prompt you to set up a table with the following schema:

### Exposures

| Field name                 | Type      | Mode     |
| -------------------------- | --------- | -------- |
| company\_id                | STRING    | NULLABLE |
| unit\_id                   | STRING    | NULLABLE |
| unit\_type                 | STRING    | NULLABLE |
| exposure\_type             | STRING    | NULLABLE |
| name                       | STRING    | NULLABLE |
| rule                       | STRING    | NULLABLE |
| experiment\_group          | STRING    | NULLABLE |
| first\_exposure\_utc       | TIMESTAMP | NULLABLE |
| first\_exposure\_pst\_date | DATE      | NULLABLE |
| as\_of\_pst\_date          | DATE      | NULLABLE |
| percent                    | FLOAT     | NULLABLE |
| rollout                    | INTEGER   | NULLABLE |
| user\_dimensions           | STRING    | NULLABLE |
| inserted\_at               | TIMESTAMP | NULLABLE |
| rule\_name                 | STRING    | NULLABLE |
| group\_id                  | STRING    | NULLABLE |
| non\_analytics             | BOOLEAN   | NULLABLE |

### Events

| Field name        | Type      | Mode     |
| ----------------- | --------- | -------- |
| user\_id          | STRING    | NULLABLE |
| stable\_id        | STRING    | NULLABLE |
| custom\_ids       | STRING    | NULLABLE |
| timestamp         | TIMESTAMP | NULLABLE |
| event\_name       | STRING    | NULLABLE |
| event\_value      | STRING    | NULLABLE |
| user\_object      | STRING    | NULLABLE |
| statsig\_metadata | STRING    | NULLABLE |
| company\_metadata | STRING    | NULLABLE |

## Troubleshooting Exports

If you set up an Export flow in Statsig, Statsig can notify you if your data connection is failing. To enable notifications, go to Settings → My Account → Email Notifications → Edit and click Alerts to subscribe to these notifications.

If your Exports are failing, make sure your warehouse is connected with up-to-date credentials and the necessary Read, Write, and Delete permissions.


Built with [Mintlify](https://mintlify.com).