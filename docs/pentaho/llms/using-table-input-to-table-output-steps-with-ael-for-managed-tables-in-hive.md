# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/using-table-input-to-table-output-steps-with-ael-for-managed-tables-in-hive.md

# Using Table input to Table output steps with AEL for managed tables in Hive

If you are using managed tables in Hive and want to join a Table input step to a Table output step, use the following workflow when executing on AEL to ensure correct processing. This workflow includes creating separate transformations for the steps and then joining the transformations using a job entry.

See the **Administer Pentaho Data Integration and Analytics** document for further configuration information when using Hive with Spark on AEL.
