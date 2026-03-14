# Source: https://docs.snowflake.com/en/guides-overview-unloading-data.md

# Unload data from Snowflake

Snowflake supports bulk unloading of data from a database table into flat, delimited text files.
The following topics detail the processes and procedures associated with unloading data.

[Overview of data unloading](user-guide/data-unload-overview.md)
:   Introduction and overview of unloading data.

[Summary of Data Unloading Features](user-guide/intro-summary-unloading.md)
:   Reference of the supported features for using the [COPY INTO <location>](sql-reference/sql/copy-into-location.md) command to unload data from Snowflake tables into flat files.

[Data unloading considerations](user-guide/data-unload-considerations.md)
:   Best practices, general guidelines, and important considerations for unloading data.

[File formats to unload data](user-guide/data-unload-prepare.md)
:   Supported data file formats for unloading data.

[Unload into a Snowflake stage](user-guide/data-unload-snowflake.md)
:   Instructions on using the COPY command to unload data from a table into an internal (i.e. Snowflake) stage.

[Unload into Amazon S3](user-guide/data-unload-s3.md)
:   Instructions on using the COPY command to unload data from a table into an Amazon S3 bucket.

[Unload into Google Cloud Storage](user-guide/data-unload-gcs.md)
:   Instructions on using the COPY command to unload data from a table into an Google Cloud Storage bucket.

[Unload into Microsoft Azure](user-guide/data-unload-azure.md)
:   Instructions on using the COPY command to unload data from a table into an Azure container.
