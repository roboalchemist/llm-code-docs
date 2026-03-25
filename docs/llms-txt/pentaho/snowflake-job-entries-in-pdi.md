# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-and-snowflake-cp/snowflake-job-entries-in-pdi.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-and-snowflake-cp/snowflake-job-entries-in-pdi.md

# Snowflake job entries in PDI

PDI has six job entries you can use to load data and manage warehouses in Snowflake.

In PDI, you can bulk load files into your Snowflake data warehouse:

* [**Bulk load into Snowflake**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake)

  Using this job entry, you can load a vast amount of data into a warehouse on Snowflake in a single session, provided you have sized your warehouse correctly. You can load data from Snowflake stages using the Snowflake VFS connection or directly from AWS S3 using the S3 VFS connection. For example, you may want to upload six months of ORC data from an S3 bucket. Using this job entry, you can define the source and type of data to load, specify the target data warehouse, and provide any needed parameters.

In PDI, you can create, modify, and even delete a Snowflake virtual warehouse to help you automate your virtual warehouse scaling activities. These orchestration entries include:

* [**Create Snowflake warehouse**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/create-warehouse-pdi-job-entry)

  You can use this job entry to create a Snowflake virtual warehouse. You can set size, scaling, automated suspension, and other properties for your warehouse.
* [**Modify Snowflake warehouse**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/modify-warehouse-pdi-job-entry)

  Once you create a warehouse, you can edit its settings using this job entry. Modifying a warehouse is useful if your users typically perform simple queries and only require a small warehouse. However, to meet your ETL service-level agreements (SLA), you may need a larger warehouse during the ETL process. Using this job entry, you can modify the warehouse at the beginning of the ETL process to scale it up, and then modify it to scale it back down when the ETL process is complete.
* [**Delete Snowflake warehouse**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/delete-snowflake-warehouse)

  Use this job entry to delete virtual warehouses. Deleting unwanted virtual warehouses helps you clean up the Snowflake management console.

In PDI, you can dynamically start and stop Snowflake virtual warehouses to help you better control your Snowflake costs. For example, if your employees only work 8 hours a day, then you don’t need to keep your warehouse up for 24 hours a day. Using the Start and Stop job entries, you can turn on the warehouse from 8 AM to 5 PM for day-to-day business activities and again from 11 PM to 2 AM while your ETL processes are running.

See the [Snowflake Documentation](https://docs.snowflake.net/manuals/index.html) to learn more about how credits are billed for running virtual warehouses in Snowflake.

* [**Start Snowflake warehouse**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/start-snowflake-warehouse)

  Use this job entry to start/resume a virtual warehouse on Snowflake. Warehouses consume credits while running.
* [**Stop Snowflake warehouse**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/stop-snowflake-warehouse)

  You can set this job entry to stop/suspend a virtual warehouse on Snowflake. Suspending a warehouse stops the warehouse from consuming credits once all the servers shut down.
