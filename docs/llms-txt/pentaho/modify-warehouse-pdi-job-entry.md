# Source: https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/modify-warehouse-pdi-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/modify-warehouse-pdi-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/modify-warehouse-pdi-job-entry.md

# Modify Snowflake warehouse

You can use the Modify Snowflake warehouse job entry to edit warehouse settings. For more information about working with Snowflake in PDI, see [PDI and Snowflake](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-and-snowflake-cp)

Modifying a warehouse is useful if your data and usage needs change through the day, week, month, or year. For example, your users might only perform simple queries which require a small warehouse. However, to meet your ETL service-level agreements (SLA), you may need a larger warehouse during the ETL process. Using this job entry, you can modify the warehouse at the beginning of the ETL process to scale it up, and then modify it to scale it back down when the ETL process is complete.

For more information about Snowflake warehouse settings, see the [Snowflake](https://docs.snowflake.net/manuals/index.html) documentation.
