# Source: https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/delete-snowflake-warehouse.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/delete-snowflake-warehouse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/delete-snowflake-warehouse.md

# Delete Snowflake warehouse

The Delete Snowflake warehouse job entry deletes/drops a virtual warehouse from your Snowflake environment. Dropping unwanted virtual warehouses helps you clean up the Snowflake management console from PDI. For more information about working with Snowflake in PDI, see [PDI and Snowflake](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-and-snowflake-cp).

When you drop a warehouse, Snowflake immediately halts processing of all SQL queries and statements which stops consumption of additional credits. To prevent any in-progress actions from terminating, use the [**Stop Snowflake warehouse**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/stop-snowflake-warehouse) job entry to suspend processing before dropping the warehouse.

**Note:** A dropped virtual warehouse cannot be recovered. It can only be recreated.

For more information about using Snowflake, see the [Snowflake](https://docs.snowflake.net/manuals/index.html) documentation.
