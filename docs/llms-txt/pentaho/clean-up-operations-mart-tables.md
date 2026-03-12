# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/clean-up-operations-mart-tables.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/clean-up-operations-mart-tables.md

# Clean up DI Operations Mart tables

Cleaning the DI Operation Mart consists of running either a job or transformation that deletes data older than a specified maximum age. The transformation and job for cleaning up the DI Operations Mart can be found in the `etl` folder.

Perform the following steps to clean up the DI Operations Mart:

1. Using the PDI client (Spoon), open either `Clean_up_PDI_Operations_Mart.kjb` for jobs or the `Clean_up_PDI_Operations_Mart_fact_table.ktr` for transformations.
2. Set the following parameters:
   * **max.age.days (required)**

     The maximum age in days of the data.
   * **schema.prefix (optional)**

     For PostgreSQL databases, enter the schema name followed by a period (.). This prefix is applied to the SQL statements. For other databases, leave the value blank.
3. Run the job or transformation.

   Running the job or transformation deletes the data that is older than the maximum age from the data mart.

See the **Pentaho Data Integration** document for details on scheduling regular clean-up of the DI Operations Mart.
