# Source: https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/stop-snowflake-warehouse.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/stop-snowflake-warehouse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/stop-snowflake-warehouse.md

# Stop Snowflake warehouse

The Stop Snowflake warehouse entry stops/suspends a virtual warehouse in Snowflake from PDI. For more information about working with Snowflake in PDI, see [PDI and Snowflake](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-and-snowflake-cp).

You can use this entry with the [Start Snowflake warehouse](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/start-snowflake-warehouse) job entry to limit the run-time of your warehouse to reduce costs. For example, if your employees only work 8 hours a day, then you don’t need to keep your warehouse running for 24 hours a day. Using the Start and Stop job entries, you can turn on the warehouse from 8 AM to 5 PM for day-to-day business activities and again from 11 PM to 2 AM while your ETL processes are running.

For more information about using Snowflake, including best practices for suspending warehouses, see the [Snowflake](https://docs.snowflake.net/manuals/index.html) documentation.
