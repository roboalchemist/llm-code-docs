# Source: https://docs.statsig.com/statsig-warehouse-native/guides/connect.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Your Warehouse

<Note>
  Warehouse Native is part of Statsig's Enterprise tier. Please [contact us](https://statsig.com/contact/demo) to get started
</Note>

To run analysis on your warehouse, Statsig needs to connect to your warehouse via a service user. You control the access this user gets to your warehouse. In general, Statsig will require:

* Read access to metric data and exposures data
* Write access to an isolated Statsig Staging database for writing results and exporting data
* Access to run jobs and queries

## Choose Your Warehouse

The following warehouses/tools are currently supported in Statsig Warehouse Native:

* [Snowflake](/statsig-warehouse-native/connecting-your-warehouse/snowflake)
* [Athena](/statsig-warehouse-native/connecting-your-warehouse/athena)
* [Bigquery](/statsig-warehouse-native/connecting-your-warehouse/bigquery)
* [Databricks](/statsig-warehouse-native/connecting-your-warehouse/databricks)
* [Redshift](/statsig-warehouse-native/connecting-your-warehouse/redshift)
* [Trino](/statsig-warehouse-native/connecting-your-warehouse/trino)
* [Clickhouse](/statsig-warehouse-native/connecting-your-warehouse/clickhouse)
* [Fabric](/statsig-warehouse-native/connecting-your-warehouse/fabric)


Built with [Mintlify](https://mintlify.com).