# Source: https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake.md

# Bulk load into Snowflake

The **Bulk load into Snowflake** job entry in PDI loads vast amounts of data into a Snowflake virtual warehouse in a single session. For more information about working with Snowflake in PDI, see [PDI and Snowflake](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-and-snowflake-cp).

This entry automates Snowflake's COPY INTO command to populate your Snowflake data warehouse with your PDI data, eliminating the need for repetitive SQL scripting. To use the **Bulk load into Snowflake** job entry, you must size your virtual warehouse, define the source and type of data to load, specify the target data warehouse, then provide any needed parameters.

For more information about using Snowflake, including best practices for bulk loading data, see the [Snowflake](https://docs.snowflake.net/manuals/index.html) documentation.
