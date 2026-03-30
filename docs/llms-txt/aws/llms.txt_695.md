# Source: https://docs.aws.amazon.com/redshift/latest/dg/llms.txt

# Amazon Redshift Database Developer Guide

> Create and manage a data warehouse with Amazon Redshift, an enterprise-level, petabyte scale, fully managed data warehousing service.

- [Tutorials](https://docs.aws.amazon.com/redshift/latest/dg/tutorials-redshift.html)
- [Data Catalog views](https://docs.aws.amazon.com/redshift/latest/dg/data-catalog-views-overview.html)
- [Document history](https://docs.aws.amazon.com/redshift/latest/dg/doc-history.html)

## [Introduction](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html)

### [Amazon Redshift architecture](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift_system_overview.html)

Provides an overview and architecture of the Amazon Redshift system.

- [Data warehouse architecture](https://docs.aws.amazon.com/redshift/latest/dg/c_high_level_system_architecture.html): Provides an architectural diagram of the Amazon Redshift data warehouse system.
- [Performance](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html): Describes the performance features that Amazon Redshift uses to achieve extremely fast query run.
- [Columnar storage](https://docs.aws.amazon.com/redshift/latest/dg/c_columnar_storage_disk_mem_mgmnt.html): Describes how columnar storage for database tables optimizes analytic query performance.
- [Workload management](https://docs.aws.amazon.com/redshift/latest/dg/c_workload_mngmt_classification.html): Describes workload management (WLM), which enables users to flexibly manage priorities within workloads.
- [Using Amazon Redshift with other services](https://docs.aws.amazon.com/redshift/latest/dg/using-redshift-with-other-services.html): Lists the other AWS services with which Amazon Redshift integrates to move, transform, and load your data.
- [Sample database](https://docs.aws.amazon.com/redshift/latest/dg/c_sampledb.html): This section describes a sample database called TICKIT that most examples in the Amazon Redshift documentation use.


## [Best practices](https://docs.aws.amazon.com/redshift/latest/dg/best-practices.html)

- [Conduct a proof of concept](https://docs.aws.amazon.com/redshift/latest/dg/proof-of-concept-playbook.html): Conduct a proof of concept for Amazon Redshift.

### [Best practices for designing tables](https://docs.aws.amazon.com/redshift/latest/dg/c_designing-tables-best-practices.html)

As you plan your database, certain key table design decisions heavily influence overall query performance.

- [Choose the best sort key](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key.html): Amazon Redshift stores your data on disk in sorted order according to the sort key.
- [Choose the best distribution style](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-best-dist-key.html): When you run a query, the query optimizer redistributes the rows to the compute nodes as needed to perform any joins and aggregations.
- [Use automatic compression](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-use-auto-compression.html): You can specify compression encodings when you create a table, but in most cases, automatic compression produces the best results.
- [Define constraints](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-defining-constraints.html): Define primary key and foreign key constraints between tables wherever appropriate.
- [Use the smallest possible column size](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-smallest-column-size.html): Don't make it a practice to use the maximum column size for convenience.
- [Use date/time data types for date columns](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-timestamp-date-columns.html): Amazon Redshift stores DATE and TIMESTAMP data more efficiently than CHAR or VARCHAR, which results in better query performance.

### [Best practices for loading data](https://docs.aws.amazon.com/redshift/latest/dg/c_loading-data-best-practices.html)

Loading very large datasets can take a long time and consume a lot of computing resources.

- [Learn how to load data](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-loading-take-loading-data-tutorial.html): walks you beginning to end through the steps to upload data to an Amazon S3 bucket and then use the COPY command to load the data into your tables.
- [Use a COPY command to load data](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-use-copy.html): The COPY command loads data in parallel from Amazon S3, Amazon EMR, Amazon DynamoDB, or multiple data sources on remote hosts.
- [Use a single COPY command](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-single-copy-command.html): Amazon Redshift can automatically load in parallel from multiple compressed data files.
- [Loading data files](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-use-multiple-files.html): Loading data from a single, large compressed file or from smaller files.
- [Compressing your data files](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-compress-data-files.html): When you want to compress large load files, we recommend that you use gzip, lzop, bzip2, or Zstandard to compress them and split the data into multiple smaller files.
- [Verify data files before and after a load](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-verifying-data-files.html): Before you load data from Amazon S3, first verify that your Amazon S3 bucket contains all the correct files, and only those files.
- [Use a multi-row insert](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-multi-row-inserts.html): If a COPY command is not an option and you require SQL inserts, use a multi-row insert whenever possible.
- [Use a bulk insert](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-bulk-inserts.html): Use a bulk insert operation with a SELECT clause for high-performance data insertion.
- [Load data in sort key order](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key-order.html): Load your data in sort key order to avoid needing to vacuum.
- [Load data in sequential blocks](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-load-data-in-sequential-blocks.html): If you need to add a large quantity of data, load the data in sequential blocks according to sort order to eliminate the need to vacuum.
- [Use time-series tables](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-time-series-tables.html): If your data has a fixed retention period, you can organize your data as a sequence of time-series tables.
- [Schedule around maintenance windows](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-avoid-maintenance.html): If a scheduled maintenance occurs while a query is running, the query is terminated and rolled back and you need to restart it.
- [Best practices for designing queries](https://docs.aws.amazon.com/redshift/latest/dg/c_designing-queries-best-practices.html): To maximize query performance, follow these recommendations when creating queries:

### [Follow Advisor recommendations](https://docs.aws.amazon.com/redshift/latest/dg/advisor.html)

To help you improve the performance and decrease the operating costs for your Amazon Redshift cluster, Amazon Redshift Advisor offers you specific recommendations about changes to make.

- [Viewing Advisor recommendations](https://docs.aws.amazon.com/redshift/latest/dg/access-advisor.html): You can access Amazon Redshift Advisor recommendations using the Amazon Redshift console, Amazon Redshift API, or AWS CLI.
- [Advisor recommendations](https://docs.aws.amazon.com/redshift/latest/dg/advisor-recommendations.html): Amazon Redshift Advisor offers recommendations about how to optimize your Amazon Redshift cluster to increase performance and save on operating costs.


## [Automatic database optimization](https://docs.aws.amazon.com/redshift/latest/dg/c_autonomics.html)

- [Allocating extra compute resources](https://docs.aws.amazon.com/redshift/latest/dg/t_extra-compute-autonomics.html): Amazon Redshift can allocate extra compute resources to ensure that your database is always being optimized.
- [Billing for autonomics operations](https://docs.aws.amazon.com/redshift/latest/dg/t_autonomics-billing.html): Amazon Redshift doesn't bill for autonomics operations by default.
- [Usage metrics for autonomics operations](https://docs.aws.amazon.com/redshift/latest/dg/t_autonomics-usage-metrics.html): Amazon Redshift tracks information on automatic optimization operations in the Amazon Redshift console and system tables.


## [Automatic table optimization](https://docs.aws.amazon.com/redshift/latest/dg/t_Creating_tables.html)

- [Enabling, disabling, and monitoring automatic table optimization](https://docs.aws.amazon.com/redshift/latest/dg/c_ato-enabling-disabling-monitoring.html): Learn how to enable, disable, and monitor automatic table optimization for Amazon Redshift.
- [Managing workload exclusions from Autonomics](https://docs.aws.amazon.com/redshift/latest/dg/t_Manage_workload_exclusion.html): You can exclude specific provisioned endpoints or serverless workgroups from influencing autonomics decisions like distribution key and sort key through a denylist feature.

### [Column compression](https://docs.aws.amazon.com/redshift/latest/dg/t_Compressing_data_on_disk.html)

Compression in Amazon Redshift is a column-level operation that reduces the size of data when it is stored.

- [Compression encodings](https://docs.aws.amazon.com/redshift/latest/dg/c_Compression_encodings.html): Work with compression encoding, which specifies the type of Amazon Redshift compression that is applied to a column of data values as rows are added to a table.
- [Testing compression encodings](https://docs.aws.amazon.com/redshift/latest/dg/t_Verifying_data_compression.html): How to test the various compression types in Amazon Redshift if you decide to manually specify column encodings.

### [Data distribution](https://docs.aws.amazon.com/redshift/latest/dg/t_Distributing_data.html)

How to choose the data distribution style that determines how Amazon Redshift distributes the rows of the table to the compute nodes when you load data.

- [Distribution styles](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html): When you create a table, you can designate one of the following distribution styles: AUTO, EVEN, KEY, or ALL.
- [Viewing distribution styles](https://docs.aws.amazon.com/redshift/latest/dg/viewing-distribution-styles.html): How to view the data distribution style of a table, with examples of each distribution style.
- [Evaluating query patterns](https://docs.aws.amazon.com/redshift/latest/dg/t_evaluating_query_patterns.html): How to evaluate query patterns as part of the making good choices for distributions styles for your Amazon Redshift application.
- [Designating distribution styles](https://docs.aws.amazon.com/redshift/latest/dg/t_designating_distribution_styles.html): How to designate distributions styles for your Amazon Redshift tables.
- [Evaluating the query plan](https://docs.aws.amazon.com/redshift/latest/dg/c_data_redistribution.html): Evaluate the query plan to identify candidates for optimizing the distribution styles for your database.
- [Query plan example](https://docs.aws.amazon.com/redshift/latest/dg/t_explain_plan_example.html): Provides an example of how to evaluate a query plan to find opportunities to optimize the distribution.
- [Distribution examples](https://docs.aws.amazon.com/redshift/latest/dg/c_Distribution_examples.html): Provides examples of how data is distributed according to the options you defined when you created the table.

### [Sort keys](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html)

When you create a table, you can define one or more of its columns as sort keys.

- [Multidimensional data layout sorting](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_mutidimensional-sort-key.html): A multidimensional data layout sort key is a type of AUTO sort key that is based on repetitive predicates found in a workload.
- [Compound sort key](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data-compound.html): A compound key is made up of all of the columns listed in the sort key definition, in the order they are listed.
- [Interleaved sort key](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data-interleaved.html): An interleaved sort gives equal weight to each column, or subset of columns, in the sort key.
- [Table constraints](https://docs.aws.amazon.com/redshift/latest/dg/t_Defining_constraints.html): Uniqueness, primary key, and foreign key constraints are informational only; they are not enforced by Amazon Redshift.


## [Loading data](https://docs.aws.amazon.com/redshift/latest/dg/t_Loading_data.html)

### [Loading tables with COPY](https://docs.aws.amazon.com/redshift/latest/dg/t_Loading_tables_with_the_COPY_command.html)

Use the COPY command to load data in parallel from files on Amazon S3, from a DynamoDB table, or from one or more remote hosts.

- [Credentials and access permissions](https://docs.aws.amazon.com/redshift/latest/dg/loading-data-access-permissions.html): To load or unload data using another AWS resource, such as Amazon S3, Amazon DynamoDB, Amazon EMR, or Amazon EC2, Amazon Redshift must have permission to access the resource and perform the necessary actions to access the data.
- [Preparing your input data](https://docs.aws.amazon.com/redshift/latest/dg/t_preparing-input-data.html): Prepare your input data to ensure that your input data is valid.

### [Loading data from Amazon S3](https://docs.aws.amazon.com/redshift/latest/dg/t_Loading-data-from-S3.html)

Read and load data in parallel from files in an Amazon S3 bucket using the COPY command.

- [Loading data from compressed and uncompressed files](https://docs.aws.amazon.com/redshift/latest/dg/t_splitting-data-files.html): Learn how to load data from compressed and uncompressed files in Amazon Redshift.

### [Uploading files](https://docs.aws.amazon.com/redshift/latest/dg/t_uploading-data-to-S3.html)

Upload your files into your Amazon S3 bucket after you have split your files.

- [Managing data consistency](https://docs.aws.amazon.com/redshift/latest/dg/managing-data-consistency.html): Ensure your application loads the correct data and manage the data consistency.
- [Uploading encrypted data](https://docs.aws.amazon.com/redshift/latest/dg/t_uploading-encrypted-data.html): Upload encrypted data to an Amazon S3 bucket and load the data using the COPY command with the ENCRYPTED option and a private encryption key to provide greater security.
- [Verifying that the correct files are present in your bucket](https://docs.aws.amazon.com/redshift/latest/dg/verifying-that-correct-files-are-present.html): Verify that the correct files are present in your Amazon S3 bucket and that no unwanted files are present.

### [Using the COPY command](https://docs.aws.amazon.com/redshift/latest/dg/t_loading-tables-from-s3.html)

Use the COPY command to load a table in parallel from data files on Amazon S3.

- [Using a manifest to specify data files](https://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html): Use a manifest to ensure that the COPY command loads all of the required files, and only the required files, for a data load.
- [Loading compressed files](https://docs.aws.amazon.com/redshift/latest/dg/t_loading-gzip-compressed-data-files-from-S3.html): Load compressed data files from an Amazon S3 bucket where the files are compressed using gzip, lzop, or bzip2.
- [Loading fixed-width data](https://docs.aws.amazon.com/redshift/latest/dg/t_loading_fixed_width_data.html): Load fixed-width data from Amazon S3 into an existing table.
- [Loading multibyte data](https://docs.aws.amazon.com/redshift/latest/dg/t_loading_unicode_data.html): Load multibyte data with up to four-byte UTF-8 characters from your Amazon S3 bucket with a limit.
- [Loading encrypted data files](https://docs.aws.amazon.com/redshift/latest/dg/c_loading-encrypted-files.html): Load encrypted data files from your Amazon S3 bucket with the ENCRYPTED option.
- [Loading data from Amazon EMR](https://docs.aws.amazon.com/redshift/latest/dg/loading-data-from-emr.html): Load data from an Amazon EMR cluster.
- [Loading data from remote hosts](https://docs.aws.amazon.com/redshift/latest/dg/loading-data-from-remote-hosts.html): Load data files from one or more of your remote hosts in parallel.
- [Loading from Amazon DynamoDB](https://docs.aws.amazon.com/redshift/latest/dg/t_Loading-data-from-dynamodb.html): How to load data from a single Amazon DynamoDB table.
- [Verifying that the data loaded correctly](https://docs.aws.amazon.com/redshift/latest/dg/verifying-that-data-loaded-correctly.html): How to verify that the expected files are loaded correctly.
- [Validating input data](https://docs.aws.amazon.com/redshift/latest/dg/t_Validating_input_files.html): How to validate that the input data was loaded correctly.
- [Loading tables with automatic compression](https://docs.aws.amazon.com/redshift/latest/dg/c_Loading_tables_auto_compress.html): How to activate automatic compression when loading tables.
- [Optimizing for narrow tables](https://docs.aws.amazon.com/redshift/latest/dg/c_load_compression_hidden_cols.html): How to optimize your storage for narrow tables.
- [Loading default column values](https://docs.aws.amazon.com/redshift/latest/dg/c_loading_default_values.html): How to load default values for your columns.

### [Troubleshooting data loads](https://docs.aws.amazon.com/redshift/latest/dg/t_Troubleshooting_load_errors.html)

Troubleshoot issues that you may encounter when loading data.

- [Troubleshooting S3 event integration and COPY JOB errors](https://docs.aws.amazon.com/redshift/latest/dg/s3-integration-troubleshooting.html): Lists some of the common S3 event integration and COPY JOB errors that you might encounter.
- [S3ServiceException errors](https://docs.aws.amazon.com/redshift/latest/dg/s3serviceexception-error.html): Lists some of the common s3ServiceException errors that you may encounter.
- [System tables for troubleshooting data loads](https://docs.aws.amazon.com/redshift/latest/dg/system-tables-for-troubleshooting-data-loads.html): Lists the Amazon Redshift system tables that can help you troubleshoot issues that you may encounter when loading data.
- [Multibyte character load errors](https://docs.aws.amazon.com/redshift/latest/dg/multi-byte-character-load-errors.html): Lists some of the common multibyte character load issues that you might encounter.
- [Error reference](https://docs.aws.amazon.com/redshift/latest/dg/r_Load_Error_Reference.html): Lists error codes and descriptions for errors that might occur while loading data.
- [Create an S3 event integration to automatically copy files](https://docs.aws.amazon.com/redshift/latest/dg/loading-data-copy-job.html): Automatically load data into your tables from files that are stored in an Amazon S3 bucket.

### [Loading tables with DML](https://docs.aws.amazon.com/redshift/latest/dg/t_Updating_tables_with_DML_commands.html)

Update Amazon Redshift tables using data manipulation language (DML) commands.

### [Updating and inserting](https://docs.aws.amazon.com/redshift/latest/dg/t_updating-inserting-using-staging-tables-.html)

Update or insert new data, in existing tables using the MERGE command.

- [Creating a temporary staging table](https://docs.aws.amazon.com/redshift/latest/dg/merge-create-staging-table.html): The staging table is a temporary table that holds all of the data that will be used to make changes to the target table, including both updates and inserts.
- [Performing a merge operation by replacing existing rows](https://docs.aws.amazon.com/redshift/latest/dg/merge-replacing-existing-rows.html): When you run the merge operation detailed in the procedure, put all of the steps except for creating and dropping the temporary staging table in a single transaction.
- [Performing a merge operation by specifying a column list without using the MERGE command](https://docs.aws.amazon.com/redshift/latest/dg/merge-specify-a-column-list.html): When you run the merge operation detailed in the procedure, put all of the steps in a single transaction.
- [Merge examples](https://docs.aws.amazon.com/redshift/latest/dg/merge-examples.html): The following examples perform a merge to update the SALES table.
- [Performing a deep copy](https://docs.aws.amazon.com/redshift/latest/dg/performing-a-deep-copy.html): Recreate and repopulate a table by using a bulk insert, known as a deep copy, which is useful for tables with large unsorted regions.
- [Analyzing tables](https://docs.aws.amazon.com/redshift/latest/dg/t_Analyzing_tables.html): The ANALYZE operation updates the statistical metadata that the query planner uses to build and choose optimal plans.

### [Vacuuming tables](https://docs.aws.amazon.com/redshift/latest/dg/t_Reclaiming_storage_space202.html)

Vacuum tables whenever you have performed a significant number of deletes or updates.

- [Minimizing vacuum times](https://docs.aws.amazon.com/redshift/latest/dg/vacuum-managing-vacuum-times.html): Use the listed approaches to minimize vacuum times.

### [Managing concurrent write operations](https://docs.aws.amazon.com/redshift/latest/dg/c_Concurrent_writes.html)

Amazon Redshift allows tables to be read while they are being incrementally loaded or modified.

- [Isolation levels](https://docs.aws.amazon.com/redshift/latest/dg/c_serial_isolation.html): Concurrent write operations are supported in Amazon Redshift the principle of serializable isolation, preserving the illusion that a transaction running against a table is the only transaction that is running against that table.
- [Write and read/write operations](https://docs.aws.amazon.com/redshift/latest/dg/c_write_readwrite.html): Manage the specific behavior of concurrent write and read/write operations by deciding when and how to run different types of commands.
- [Concurrent write examples](https://docs.aws.amazon.com/redshift/latest/dg/r_Serializable_isolation_example.html): Provides examples of how to perform concurrent write transactions using specific operations.
- [Troubleshooting](https://docs.aws.amazon.com/redshift/latest/dg/c_serial_isolation-serializable-isolation-troubleshooting.html)
- [Tutorial: Loading data from Amazon S3](https://docs.aws.amazon.com/redshift/latest/dg/tutorial-loading-data.html): Learn how to load data into Amazon Redshift database tables from data files in an Amazon S3 bucket.


## [Unloading data](https://docs.aws.amazon.com/redshift/latest/dg/c_unloading_data.html)

- [Unloading data to Amazon S3](https://docs.aws.amazon.com/redshift/latest/dg/t_Unloading_tables.html): Unload data from database tables to a set of files in an Amazon S3 bucket.
- [Unloading encrypted data files](https://docs.aws.amazon.com/redshift/latest/dg/t_unloading_encrypted_files.html): Create encrypted data files in Amazon S3 by using the UNLOAD command with the ENCRYPTED option.
- [Unloading data in delimited or fixed-width format](https://docs.aws.amazon.com/redshift/latest/dg/t_unloading_fixed_width_data.html): Learn how to unload data in delimited format or fixed-width format.
- [Reloading unloaded data](https://docs.aws.amazon.com/redshift/latest/dg/t_Reloading_unload_files.html): Reload the results of an unload operation using the COPY command.


## [User-defined functions](https://docs.aws.amazon.com/redshift/latest/dg/user-defined-functions.html)

- [UDF security and permissions](https://docs.aws.amazon.com/redshift/latest/dg/udf-security-and-privileges.html): To create a UDF, you must have permission for usage on language for SQL or plpythonu (Python).
- [Preventing UDF naming conflicts](https://docs.aws.amazon.com/redshift/latest/dg/udf-naming-udfs.html): You can avoid potential conflicts and unexpected results considering your UDF naming conventions before implementation.

### [Scalar SQL UDFs](https://docs.aws.amazon.com/redshift/latest/dg/udf-creating-a-scalar-sql-udf.html)

A scalar SQL UDF incorporates a SQL SELECT clause that runs when the function is called and returns a single value.

- [Example](https://docs.aws.amazon.com/redshift/latest/dg/udf-scalar-sql-function-example.html): The following example creates a function that compares two numbers and returns the larger value.

### [Scalar Python UDFs](https://docs.aws.amazon.com/redshift/latest/dg/udf-creating-a-scalar-udf.html)

A scalar Python UDF incorporates a Python program that runs when the function is called and returns a single value.

- [Example](https://docs.aws.amazon.com/redshift/latest/dg/udf-scalar-function-example.html): The following example creates a function that compares two numbers and returns the larger value.
- [Python UDF data types](https://docs.aws.amazon.com/redshift/latest/dg/udf-data-types.html): Python UDFs can use any standard Amazon Redshift data type for the input arguments and the function's return value.

### [Python language support](https://docs.aws.amazon.com/redshift/latest/dg/udf-python-language-support.html)

You can create a custom UDF based on the Python programming language.

- [Example](https://docs.aws.amazon.com/redshift/latest/dg/udf-importing-custom-python-library-modules.html): You define scalar functions using Python language syntax.
- [Constraints](https://docs.aws.amazon.com/redshift/latest/dg/udf-constraints.html): Within the constraints listed in this topic, you can use UDFs anywhere you use the Amazon Redshift built-in scalar functions.
- [Logging errors and warnings](https://docs.aws.amazon.com/redshift/latest/dg/udf-logging-messages.html): You can use the Python logging module to create user-defined error and warning messages in your UDFs.
- [Scalar Lambda UDFs](https://docs.aws.amazon.com/redshift/latest/dg/udf-creating-a-lambda-sql-udf.html): Amazon Redshift can use custom functions defined in AWS Lambda as part of SQL queries.
- [Use case examples for UDFs](https://docs.aws.amazon.com/redshift/latest/dg/udf-example-uses.html): Explore how others used user-defined functions.


## [Creating stored procedures](https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-overview.html)

### [Stored procedure overview](https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-create.html)

Create and run a stored procedure in Amazon Redshift.

- [Naming stored procedures](https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-naming.html): Name a stored procedure in Amazon Redshift.
- [Security and privileges](https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-security-and-privileges.html): Learn about the privileges needed to create and run a stored procedure in Amazon Redshift.
- [Returning a result set](https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-result-set.html): Return a result set from a stored procedure in Amazon Redshift.
- [Managing transactions](https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-transaction-management.html): Manage transactions for stored procedures in Amazon Redshift.
- [Trapping errors](https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-trapping-errors.html): Trap errors in a stored procedure in Amazon Redshift.
- [Logging stored procedures](https://docs.aws.amazon.com/redshift/latest/dg/c_PLpgSQL-logging.html): Log stored procedures in certain system tables and views in Amazon Redshift.
- [Limitations](https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-constraints.html): Find out about considerations and differences of Amazon Redshift stored procedures compared to stored procedures in PostgreSQL.

### [PL/pgSQL language reference](https://docs.aws.amazon.com/redshift/latest/dg/c_pl_pgSQL_reference.html)

Work with the PL/pgSQL language that Amazon Redshift uses.

- [PL/pgSQL reference conventions](https://docs.aws.amazon.com/redshift/latest/dg/c_PL_reference_conventions.html): Find the conventions used to write the PL/pgSQL language that is used in Amazon Redshift.
- [Structure of PL/pgSQL](https://docs.aws.amazon.com/redshift/latest/dg/c_PLpgSQL-structure.html): Learn about the structure of the PL/pgSQL language that is used in Amazon Redshift.
- [Supported PL/pgSQL statements](https://docs.aws.amazon.com/redshift/latest/dg/c_PLpgSQL-statements.html): Work with the PL/pgSQL statements supported by Amazon Redshift.


## [Materialized views](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html)

- [Materialized view queries](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-query.html): Using a materialized view in a SQL query.
- [Automatic query rewriting to use materialized views](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-auto-rewrite.html): Amazon Redshift can rewrite queries to use a materialized view.
- [Materialized views on external data lake tables](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-external-table.html): Use a materialized view on an external data lake table.
- [Refreshing a materialized view](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-refresh.html): Update the data in a materialized view by using REFRESH.
- [Automated materialized views](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-auto-mv.html): Learn about automated materialized views.
- [Using a user-defined function (UDF) in a materialized view](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-UDFs.html): You can use a scalar UDF in an Amazon Redshift materialized view.

### [Streaming ingestion to a materialized view](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion.html)

Learn about using streaming ingestion to stream data from streaming services into Amazon Redshift.

- [Getting started with streaming ingestion from Amazon Kinesis Data Streams](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion-getting-started.html): Learn how to set up streaming ingestion from Amazon Kinesis Data Streams.

### [Getting Started with streaming ingestion from Apache Kafka](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion-getting-started-MSK.html)

Learn how to set up streaming ingestion from Apache Kafka sources, including Amazon Managed Streaming for Apache Kafka and Confluent Cloud.

- [Authentication with mTLS for Redshift streaming ingestion from Apache Kafka](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion-mtls.html): Authentication with mTLS for Redshift streaming ingestion from Apache Kafka.
- [Electric vehicle station-data streaming ingestion tutorial, using Kinesis](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion-example-station-data.html): Learn about a scenario that demonstrates the usefulness of streaming ingestion.


## [Querying spatial data](https://docs.aws.amazon.com/redshift/latest/dg/geospatial-overview.html)

- [Tutorial: Using spatial SQL functions](https://docs.aws.amazon.com/redshift/latest/dg/spatial-tutorial.html): Use this tutorial to learn about how to use spatial SQL functions with Amazon Redshift.
- [Loading a shapefile](https://docs.aws.amazon.com/redshift/latest/dg/spatial-copy-shapefile.html): Copy a shapefile into Amazon Redshift tables for further processing.
- [Terminology](https://docs.aws.amazon.com/redshift/latest/dg/spatial-terminology.html): Learn terminology for use with Amazon Redshift spatial functions.
- [Considerations](https://docs.aws.amazon.com/redshift/latest/dg/spatial-limitations.html): Some Amazon Redshift features don't support spatial data, and this section provides the limitations.


## [Querying data with federated queries](https://docs.aws.amazon.com/redshift/latest/dg/federated-overview.html)

- [Getting started with using federated queries to PostgreSQL](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-federated.html): To create a federated query, you follow this general approach:
- [Getting started using federated queries to PostgreSQL with CloudFormation](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-federated-CF.html): Automate federated query setup in Amazon Redshift by using an AWS CloudFormation stack.
- [Getting started with using federated queries to MySQL](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-federated-mysql.html): To create a federated query to MySQL databases, you follow this general approach:
- [Creating a secret and an IAM role](https://docs.aws.amazon.com/redshift/latest/dg/federated-create-secret-iam-role.html): Create a secret and an IAM role to use with federated queries with Amazon Redshift.
- [Examples of using a federated query](https://docs.aws.amazon.com/redshift/latest/dg/federated_query_example.html): Work with examples that show how to run a federated query for Amazon Redshift.
- [Data type differences](https://docs.aws.amazon.com/redshift/latest/dg/federated-data-types.html): Learn how Amazon Redshift data types are mapped to RDS PostgreSQL or Aurora PostgreSQL data types.
- [Considerations](https://docs.aws.amazon.com/redshift/latest/dg/federated-limitations.html): Some Amazon Redshift features don't support access to federated data, and this section provides the limitations and considerations.


## [Federated permissions](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions.html)

- [Considerations](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-considerations.html): The following are considerations and limitations for sharing Amazon Redshift data with AWS Glue Data Catalog using federated permissions.
- [Prerequisites](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-prereqs.html)
- [Onboarding](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-onboarding.html)
- [Querying catalogs](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-querying.html): When you register an Amazon Redshift data warehouse to the AWS Glue Data Catalog using Amazon Redshift federated permissions, the databases in that namespace are automatically mounted in all Amazon Redshift instances in that AWS account and Region.
- [Access control](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-managing-access.html): With Amazon Redshift federated permissions, users can define both coarse-grained and fine-grained access controls from any Redshift warehouse in the AWS account.
- [Examples](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-end-examples.html): The following is an end-to-end example showing how you can create and manage comprehensive data governance policies using Amazon Redshift Federated Permissions.
- [Federated user configuration](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-user-cofig.html): With Amazon Redshift federated permissions, users authenticated with IAM or IAM Identity Center (IdC) credentials can get a consistent experience across all their Amazon Redshift warehouses.

### [Disabling IAM Identity Center propagation](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-offboarding.html)

Before you can disable AWS IAM Identity Center propagation, you must have Amazon Redshift Cluster or Amazon Redshift Serverless Namespace has registered with AWS Glue Data Catalog and associated with a Lakehouse Redshift IdC Application.

- [Deregister from AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/dg/federated-permisisons-offboarding-deregister-catalog.html)


## [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html)

### [Amazon Redshift Spectrum overview](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-overview.html)

This topic describes details for using Redshift Spectrum to efficiently read from Amazon S3.

- [Amazon Redshift Spectrum limitations](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-considerations.html): This topic describes limitations for using Redshift Spectrum.
- [Getting started with Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html): In this tutorial, you learn how to use Amazon Redshift Spectrum to query data directly from files on Amazon S3.
- [IAM policies for Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-iam-policies.html): Learn about IAM policies for Amazon Redshift Spectrum.
- [Redshift Spectrum and Lake Formation](https://docs.aws.amazon.com/redshift/latest/dg/spectrum-lake-formation.html): This topic describes how to use Redshift Spectrum with Lake Formation.
- [Data files for queries in Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-data-files.html): This section describes how to create data files in Amazon S3 in a format that Redshift Spectrum supports.
- [External schemas](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-external-schemas.html): This topic describes how to create and use external schemas with Redshift Spectrum.
- [External tables](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-external-tables.html): This topic describes how to create and use external tables with Redshift Spectrum.

### [Using Apache Iceberg tables](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)

Use Amazon Redshift to query Apache Iceberg tables using Apache Parquet data files cataloged in the Data Catalog.

- [Supported data types](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg-supported-data-types.html): This topic describes the supported data types that Redshift Spectrum can read from tables in Apache Iceberg format.
- [Referencing Iceberg tables](https://docs.aws.amazon.com/redshift/latest/dg/referencing-iceberg-tables.html): Learn how to reference and access Apache Iceberg tables in Amazon Redshift using external schemas and three-part notation.

### [Writing to Apache Iceberg tables](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-writes.html)

Learn how to create and write to Apache Iceberg tables stored on Amazon S3 and Amazon S3 table buckets using Amazon Redshift.

- [SQL commands](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-writes-sql-syntax.html): SQL syntax for creating, inserting, and managing Iceberg tables in Amazon Redshift.
- [Transaction semantics](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-writes-transaction-semantics.html): ACID properties and transaction behavior for Iceberg write operations in Amazon Redshift.
- [Best practices](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-writes-best-practices.html): Best practices for writes to Apache Iceberg tables.
- [Amazon Redshift Spectrum query performance](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-external-performance.html): This topic describes how to improve Redshift Spectrum query performance.
- [Data handling options](https://docs.aws.amazon.com/redshift/latest/dg/t_setting-data-handling-options.html): Learn how to set data handling configuration options.
- [Performing correlated subqueries](https://docs.aws.amazon.com/redshift/latest/dg/c_performing-correlated-subqueries-spectrum.html): Learn how to perform correlated subqueries in Redshift Spectrum.
- [Metrics](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-metrics.html): This topic describes system views that you can use to monitor Redshift Spectrum queries.
- [Query troubleshooting](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-troubleshooting.html)

### [Tutorial: Querying nested data with Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/tutorial-query-nested-data.html)

Query nested data with Amazon Redshift Spectrum.

- [Nested data use cases](https://docs.aws.amazon.com/redshift/latest/dg/nested-data-use-cases.html): This topic describes use cases for nested data.
- [Nested data limitations (preview)](https://docs.aws.amazon.com/redshift/latest/dg/nested-data-restrictions.html): This topic describes limitations for reading nested data with Redshift Spectrum.
- [Serializing complex nested JSON](https://docs.aws.amazon.com/redshift/latest/dg/serializing-complex-JSON.html): This topic demonstrates how to serialize nested data in JSON format.


## [HyperLogLog sketches](https://docs.aws.amazon.com/redshift/latest/dg/hyperloglog-overview.html)

- [Considerations](https://docs.aws.amazon.com/redshift/latest/dg/hyperloglog-functions-usage-notes.html): This topic describes usage details for HyperLogLog in Amazon Redshift.
- [Limitations](https://docs.aws.amazon.com/redshift/latest/dg/hyperloglog-functions-limitations.html): This topic describes limitations for HyperLogLog in Amazon Redshift.
- [Examples](https://docs.aws.amazon.com/redshift/latest/dg/r_HLL-examples.html): This section contains examples for using HyperLogLog with Amazon Redshift.


## [Cross-database queries](https://docs.aws.amazon.com/redshift/latest/dg/cross-database-overview.html)

- [Considerations](https://docs.aws.amazon.com/redshift/latest/dg/cross-database_usage.html): This topic describes usage details for cross-database queries in Amazon Redshift.
- [Limitations](https://docs.aws.amazon.com/redshift/latest/dg/cross-database_limitation.html): This topic describes limitations for cross-database queries in Amazon Redshift.
- [Examples](https://docs.aws.amazon.com/redshift/latest/dg/cross-database_example.html): Work with examples that show how to run a cross-database query for Amazon Redshift.
- [Using cross-database queries with the query editor](https://docs.aws.amazon.com/redshift/latest/dg/cross-database_console.html): This topic explains how to use cross-database queries with the query editor.


## [Apache Iceberg compatibility](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-integration_overview.html)

- [IAM policy requirements](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-integration-iam.html): This topic describes the required IAM permissions for registering provisioned clusters and serverless namespaces to the Data Catalog and accessing them with Amazon Redshift.
- [Registering clusters and namespaces](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-integration-register.html): You can add Amazon Redshift provisioned clusters and serverless namespaces to the AWS Glue Data Catalog to access them using the Apache Iceberg REST API.
- [Deregistering clusters and namespaces](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-integration-deregister.html): You can deregister a provisioned cluster or serverless namespace from the AWS Glue Data Catalog using the Amazon Redshift console or the AWS CLI.
- [Managed workgroups](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-integration-managed-workgroups.html): When you register a provisioned cluster or serverless namespace to the AWS Glue Data Catalog and create a catalog from it, AWS Glue creates a managed workgroup to provide compute resources for any SQL query engine that accesses that catalog.
- [Querying catalogs registered in the AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-integration-querying.html): After you register an Amazon Redshift data warehouse to the AWS Glue Data Catalog and set permissions for the resulting catalog in AWS Lake Formation, the catalog is automatically mounted in all Amazon Redshift instances with access to the source data warehouse in the same account and AWS Region.


## [Data sharing](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html)

### [Considerations](https://docs.aws.amazon.com/redshift/latest/dg/datashare-considerations.html)

With Amazon Redshift data sharing, you can securely share access to live data across Amazon Redshift clusters, workgroups, AWS accounts, and AWS Regions without manually moving or copying the data.

- [General considerations for data sharing](https://docs.aws.amazon.com/redshift/latest/dg/considerations-datashare-general.html): The following are general considerations when working with datashares in Amazon Redshift:
- [Considerations for data sharing reads and writes](https://docs.aws.amazon.com/redshift/latest/dg/considerations-datashare-reads-writes.html)
- [Considerations for data sharing in serverless restore](https://docs.aws.amazon.com/redshift/latest/dg/considerations-datashare-serverless-restore.html): Consider following when working with datashares during Amazon Redshift Serverless restore operations:
- [Considerations for data sharing with data lake tables](https://docs.aws.amazon.com/redshift/latest/dg/considerations-datashare-datalake.html): The following are considerations when working with data lake tables in Amazon Redshift:
- [Considerations for data sharing with AWS Lake Formation](https://docs.aws.amazon.com/redshift/latest/dg/lake-formation-considerations.html): The following are considerations and limitations for sharing Amazon Redshift data with Lake Formation.
- [Considerations for data sharing with AWS Data Exchange](https://docs.aws.amazon.com/redshift/latest/dg/adx-considerations.html): Learn about some considerations when using AWS Data Exchange for Amazon Redshift.
- [Permissions you can grant to datashares](https://docs.aws.amazon.com/redshift/latest/dg/permissions-datashares.html): Different object types and various permissions you can grant to them in a data sharing context.
- [Supported SQL statements for data sharing writes on consumers](https://docs.aws.amazon.com/redshift/latest/dg/multi-warehouse-writes-sql-statements.html): The following Data Definition Language (DDL) statements are supported for data sharing with writes:
- [Unsupported SQL statements for data sharing writes on consumers](https://docs.aws.amazon.com/redshift/latest/dg/multi-warehouse-writes-sql-statements-unsupported.html): The following aren't supported:
- [Available AWS Regions](https://docs.aws.amazon.com/redshift/latest/dg/data_sharing_regions.html): The following table lists availability for both data sharing read and write capabilities.

### [Getting started](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-datasharing.html)

Get started with data sharing by following one of the guides in this section

### [Getting started with read-only data sharing in the console](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-datashare-read-only.html)

With Amazon Redshift, you can manage data sharing with writes using the console to control access and govern data across Amazon Redshift clusters and AWS accounts.

- [Connecting to a database](https://docs.aws.amazon.com/redshift/latest/dg/connect-database-console.html): Connect to a database to view databases and objects within databases in this cluster or to view datashares.
- [Creating datashares](https://docs.aws.amazon.com/redshift/latest/dg/datashare-creation.html): With Amazon Redshift, you can share live data across Amazon Redshift clusters or AWS accounts using datashares.
- [Authorizing or removing authorization from datashares](https://docs.aws.amazon.com/redshift/latest/dg/authorize-datashare-console.html): Authorize or remove authorization from datashares.
- [Managing datashares from other accounts as a consumer](https://docs.aws.amazon.com/redshift/latest/dg/manage-datashare-other-console.html)
- [Managing existing datashares](https://docs.aws.amazon.com/redshift/latest/dg/manage-datashare-existing-console.html): With Amazon Redshift, you can manage existing datashares to control access to your data in an Amazon Redshift cluster.
- [Querying datashares](https://docs.aws.amazon.com/redshift/latest/dg/query-datashare-console.html): With Amazon Redshift, you can query data across datashares from producer clusters to securely access live data without copying or transferring it.
- [Managing AWS Data Exchange datashares](https://docs.aws.amazon.com/redshift/latest/dg/manage-adx-datashare-console.html): With Amazon Redshift, you can securely share and receive live data from AWS Data Exchange without having to create and manage data extracts or pipelines.

### [Getting started with read-only data sharing with the SQL interface](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-datashare-sql.html)

With Amazon Redshift, you can securely share data across Amazon Redshift clusters, enabling data consumers to query and access live data without copying or replicating it.

- [Sharing read access to data within an AWS account](https://docs.aws.amazon.com/redshift/latest/dg/within-account.html): With Amazon Redshift, you can share read access to data across different database users or groups within the same AWS account.
- [Working with views](https://docs.aws.amazon.com/redshift/latest/dg/datashare-views.html): A producer cluster can share regular, late-binding, and materialized views.
- [Adding data lake tables to a datashare](https://docs.aws.amazon.com/redshift/latest/dg/create-datashare-external-views.html): You can add tables from the AWS data catalog to a Redshift datashare.

### [Sharing data across AWS accounts](https://docs.aws.amazon.com/redshift/latest/dg/across-account.html)

You can share data for read purposes across AWS accounts.

- [producer administrator actions](https://docs.aws.amazon.com/redshift/latest/dg/producer-cluster-admin.html): With Amazon Redshift, you can perform administrative tasks on producer clusters to manage data ingestion and load processing.
- [Consumer account administrator actions](https://docs.aws.amazon.com/redshift/latest/dg/consumer-account-admin.html): With Amazon Redshift, you can manage consumer accounts and control their access to your data warehousing resources.
- [consumer administrator actions](https://docs.aws.amazon.com/redshift/latest/dg/consumer-cluster-admin.html): With Amazon Redshift, you can perform administrative tasks on consumer clusters to manage data ingestion and load processing.

### [Sharing data across AWS Regions](https://docs.aws.amazon.com/redshift/latest/dg/across-region.html)

You can share data for read purposes across Amazon Redshift clusters in AWS Regions.

- [Managing cost control for cross-Region data sharing](https://docs.aws.amazon.com/redshift/latest/dg/cross-region-billing.html): Managing billing and cost control for cross-Region data sharing

### [Sharing licensed Amazon Redshift data on AWS Data Exchange](https://docs.aws.amazon.com/redshift/latest/dg/adx-getting-started.html)

When creating AWS Data Exchange datashares and adding them to an AWS Data Exchange product, providers can license data in Amazon Redshift that consumers can discover, subscribe to, and query up-to-date data in Amazon Redshift when they have active AWS Data Exchange subscriptions.

- [Working with AWS Data Exchange datashares as a producer](https://docs.aws.amazon.com/redshift/latest/dg/adx-getting-started-producer.html): With Amazon Redshift, you can share live data products with AWS Data Exchange as a producer by creating and managing datashares.

### [Getting started with AWS Lake Formation-managed datashares](https://docs.aws.amazon.com/redshift/latest/dg/lf-getting-started.html)

With Amazon Redshift, you can access and share live data across AWS accounts and Amazon Redshift clusters through AWS Lake Formation-managed datashares.

- [Working with Lake Formation-managed datashares as a producer](https://docs.aws.amazon.com/redshift/latest/dg/lake-formation-getting-started-producer.html): With Amazon Redshift, you can access and analyze data shared through AWS Lake Formation datashares.
- [Working with Lake Formation-managed datashares as a consumer](https://docs.aws.amazon.com/redshift/latest/dg/lake-formation-getting-started-consumer.html): With Amazon Redshift, you can access and analyze data shared with you through AWS Lake Formation datashares.

### [Getting started with multi-warehouse writes](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-datashare-writes.html)

You can share database objects for both reads and writes across different Amazon Redshift clusters or Amazon Redshift Serverless workgroups within the same AWS account, across accounts, and across regions.

- [Connecting to a database](https://docs.aws.amazon.com/redshift/latest/dg/connect-database-console-writes.html): Connect to a database to view databases and objects within databases in this cluster or to view datashares.

### [Producer actions for new datashares](https://docs.aws.amazon.com/redshift/latest/dg/writes-producer-new.html)

As a producer administrator, you can create datashares from the Database or Datashares tabs in the Cluster details page.

- [Creating a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-creating-datashare.html): As a producer administrator, you can create datashares.
- [Adding objects to a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-adding-datashare.html): You can add objects to the datashare while creating the datashare.
- [Adding data consumers to a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-adding-data-consumer.html): You can add data consumers to the datashare while creating the datashare.
- [Authorizing a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-authorizing.html): You can authorize the datashare while creating the datashare.

### [Consumer actions for new datashares](https://docs.aws.amazon.com/redshift/latest/dg/writes-consumer-new.html)

As a consumer, you can configure access, create databases from datashares, grant object level permissions, and query shared data.

- [Associating a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-associating.html): As a consumer administrator, you can associate one or more datashares that are shared from other accounts.
- [Creating a database from a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-creating-database.html): As a consumer administrator, you can create a database from a datashare.
- [Granting object level permissions](https://docs.aws.amazon.com/redshift/latest/dg/writes-granting.html): As a consumer administrator, you can grant permissions.
- [Querying data in a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-querying.html): As a consumer administrator, you can query data in shared objects in a datashare.

### [Producer actions for existing datashares](https://docs.aws.amazon.com/redshift/latest/dg/writes-producer-existing.html)

As a producer administrator, you can take actions for existing datashares.

- [Viewing a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-viewing.html): View datashares.
- [Editing a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-editing.html): Edit datashares created in your account.
- [Removing authorization from a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-removing-authorization.html): With Amazon Redshift, you can control access to datashares by revoking authorization for specified consumers.
- [Removing datashare objects from a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-removing-datashare-object.html): You can remove objects from datashares.
- [Removing data consumers from a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-removing-data-consumer.html): You can remove one or more data consumers from a datashare.
- [Deleting a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-deleting.html): Delete datashares created in your account.

### [Consumer actions for existing datashares](https://docs.aws.amazon.com/redshift/latest/dg/writes-consumer-existing.html)

As a producer administrator, you can take specific actions for existing datashares.

- [Managing permissions for a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-managing-permissions.html): As a producer administrator, you retain control for the datasets you are sharing.
- [Removing association of a datashare from data consumers](https://docs.aws.amazon.com/redshift/latest/dg/writes-disassociating-datashare.html): As a consumer administrator, you can remove association of datashares from data consumers.
- [Declining a datashare](https://docs.aws.amazon.com/redshift/latest/dg/writes-declining-datashare.html): As a consumer administrator, you can decline one or more Amazon Redshift datashares that are shared from other accounts.
- [Getting started with CloudFormation](https://docs.aws.amazon.com/redshift/latest/dg/data-sharing-within-account-CF.html): Automate data sharing setup in Amazon Redshift by using an AWS CloudFormation stack.

### [Types of datashares](https://docs.aws.amazon.com/redshift/latest/dg/datashare-types.html)

A datashare is the unit of sharing data in Amazon Redshift.

- [Standard datashares](https://docs.aws.amazon.com/redshift/latest/dg/standard_datashare.html): With standard datashares, you can share data across provisioned clusters, serverless workgroups, Availability Zones, AWS accounts, and AWS Regions.
- [AWS Data Exchange datashares](https://docs.aws.amazon.com/redshift/latest/dg/adx_datashare_overview.html): You can use AWS Data Exchange datashares to manage billing for Amazon Redshift data sharing.
- [AWS Lake Formation-managed datashares](https://docs.aws.amazon.com/redshift/latest/dg/lf_datashare_overview.html): With Amazon Redshift, you can access and share live data across AWS accounts and Amazon Redshift clusters through AWS Lake Formation-managed datashares.
- [Datashare status](https://docs.aws.amazon.com/redshift/latest/dg/datashare_status.html): With Amazon Redshift, you can securely share live data across Amazon Redshift clusters without having to copy or transfer data.
- [Managing access to data sharing API operations with IAM policies](https://docs.aws.amazon.com/redshift/latest/dg/iam-policy.html): To control the access to the data sharing API operations, use IAM action-based policies.
- [Connecting to consumer databases](https://docs.aws.amazon.com/redshift/latest/dg/database-direct-connect.html): Learn how to connect to consumer databases.
- [Monitoring and auditing data sharing](https://docs.aws.amazon.com/redshift/latest/dg/auditing.html): With Amazon Redshift, you can monitor and audit data sharing activities to ensure compliance and security.


## [Semi-structured data in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/super-overview.html)

- [PartiQL for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/super-partiql.html): Amazon Redshift supports PartiQL, an SQL-compatible query language, to select, insert, update, and delete data in Amazon Redshift.

### [Loading semi-structured data](https://docs.aws.amazon.com/redshift/latest/dg/ingest-super.html)

Use the SUPER data type to parse and query hierarchical and generic data in Amazon Redshift.

- [Using JSON_PARSE to insert JSON data](https://docs.aws.amazon.com/redshift/latest/dg/parse_json.html): You can insert or update JSON data into a SUPER column using the .
- [Using COPY to load JSON data](https://docs.aws.amazon.com/redshift/latest/dg/copy_json.html): In the following sections, you can learn about different ways to use the COPY command to load JSON data into Amazon Redshift.
- [Unloading semi-structured data](https://docs.aws.amazon.com/redshift/latest/dg/unload-super.html): With Amazon Redshift, you can export semi-structured data from your Amazon Redshift cluster to Amazon S3 in a variety of formats, including text, Apache Parquet, Apache ORC, and Avro.
- [Querying semi-structured data](https://docs.aws.amazon.com/redshift/latest/dg/query-super.html): In Amazon Redshift, you can work with the PartiQL language for SQL-compatible access to semi-structured data.
- [Operators and functions](https://docs.aws.amazon.com/redshift/latest/dg/operators-functions.html): With Amazon Redshift, you can perform advanced analytics on large datasets using SUPER data using operators and functions.
- [SUPER configurations](https://docs.aws.amazon.com/redshift/latest/dg/super-configurations.html): You can configure your SUPER data for specific scenarios.
- [Limitations](https://docs.aws.amazon.com/redshift/latest/dg/limitations-super.html): With Amazon Redshift, you can work with the SUPER data type to store and query semi-structured data like JSON, Avro, or Ion.

### [SUPER data type and materialized views](https://docs.aws.amazon.com/redshift/latest/dg/r_SUPER_MV.html)

Amazon Redshift supports SUPER data type and PartiQL in materialized views.

- [Shredding semi-structured data into SUPER columns with materialized views](https://docs.aws.amazon.com/redshift/latest/dg/r_shred_super.html): You can use materialized views to accelerate PartiQL queries that navigate and/or unnest hierarchical data in SUPER columns.
- [Creating Amazon Redshift scalar columns out of shredded data](https://docs.aws.amazon.com/redshift/latest/dg/r_create_scalar.html): Learn how schemaless data stored into SUPER can affect the performance of Amazon Redshift.
- [Examples](https://docs.aws.amazon.com/redshift/latest/dg/super-examples.html): The following examples demonstrate how to work with semi-structured data in Amazon Redshift using PartiQL syntax.


## [Machine learning](https://docs.aws.amazon.com/redshift/latest/dg/machine_learning.html)

- [Machine learning overview](https://docs.aws.amazon.com/redshift/latest/dg/machine_learning_overview.html): By using Amazon Redshift ML, you can train machine learning models using SQL statements and invoke them in SQL queries for prediction.
- [Machine learning for novices and experts](https://docs.aws.amazon.com/redshift/latest/dg/novice_expert.html): Learn how Amazon Redshift ML makes training easier.
- [Costs for using Amazon Redshift ML](https://docs.aws.amazon.com/redshift/latest/dg/cost.html): Learn about the costs for using Amazon Redshift machine learning.
- [Getting started: Amazon Redshift ML](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-machine-learning.html): Get started with Amazon Redshift machine learning (ML), which makes it easy for SQL users to create, train, and deploy machine learning models using familiar SQL commands.

### [Tutorials for Amazon Redshift ML](https://docs.aws.amazon.com/redshift/latest/dg/tutorials_for_amazon_redshift_ml.html)

Use these tutorials to create Amazon Redshift machine learning models and perform predictions.

- [Tutorial: Build customer churn models](https://docs.aws.amazon.com/redshift/latest/dg/tutorial_customer_churn.html): Use this tutorial for an end-to-end example of creating an Amazon Redshift machine learning model and running inference queries.
- [Tutorial: Building K-means clustering models](https://docs.aws.amazon.com/redshift/latest/dg/tutorial_k-means_clustering.html): Use this tutorial for an end-to-end example of creating an Amazon Redshift machine learning model and running inference queries.
- [Tutorial: Building multi-class classification models](https://docs.aws.amazon.com/redshift/latest/dg/tutorial_multi-class_classification.html): Use this tutorial for an end-to-end example of creating an Amazon Redshift machine learning model and running inference queries.
- [Tutorial: Building XGBoost models](https://docs.aws.amazon.com/redshift/latest/dg/tutorial_xgboost.html): Use this tutorial for an end-to-end example of creating an Amazon Redshift machine learning model and running inference queries.
- [Tutorial: Building regression models](https://docs.aws.amazon.com/redshift/latest/dg/tutorial_regression.html): Use this tutorial for an end-to-end example of creating an Amazon Redshift machine learning model and running inference queries.
- [Tutorial: Building regression models with linear learner](https://docs.aws.amazon.com/redshift/latest/dg/tutorial_linear_learner_regression.html): Use this tutorial for an end-to-end example of creating an Amazon Redshift machine learning model and running inference queries.
- [Tutorial: Building multi-class classification models with linear learner](https://docs.aws.amazon.com/redshift/latest/dg/tutorial_linear_learner_multi-class_classification.html): Use this tutorial for an end-to-end example of creating an Amazon Redshift machine learning model and running inference queries.
- [Amazon Redshift ML integration with Amazon Bedrock](https://docs.aws.amazon.com/redshift/latest/dg/machine-learning-br.html): Get started with Amazon Redshift machine learning (ML) integration with Amazon Bedrock, which makes it easy for SQL users to use external LLMs using familiar SQL. commands.


## [Query performance tuning](https://docs.aws.amazon.com/redshift/latest/dg/c-optimizing-query-performance.html)

### [Query processing](https://docs.aws.amazon.com/redshift/latest/dg/c-query-processing.html)

Describes how queries are processed in Amazon Redshift, and how to read the query plan produced by the EXPLAIN command to get the specifics on a particular query.

- [Query planning and execution workflow](https://docs.aws.amazon.com/redshift/latest/dg/c-query-planning.html): The following illustration provides a high-level view of the query planning and execution workflow.
- [Creating and interpreting a query plan](https://docs.aws.amazon.com/redshift/latest/dg/c-the-query-plan.html): Describes how to interpret a query plan.
- [Reviewing query plan steps](https://docs.aws.amazon.com/redshift/latest/dg/reviewing-query-plan-steps.html): You can see the steps in a query plan by running the EXPLAIN command.
- [Factors affecting query performance](https://docs.aws.amazon.com/redshift/latest/dg/c-query-performance.html): Describes how to interpret a query plan.

### [Query analysis and improvement](https://docs.aws.amazon.com/redshift/latest/dg/c-query-tuning.html)

Describes how to use query plan and query summary information to tune query performance.

- [Query analysis workflow](https://docs.aws.amazon.com/redshift/latest/dg/c-query-analysis-process.html): If a query is taking longer than expected, use the following steps to identify and correct issues that might be negatively affecting the queryâs performance.
- [Reviewing query alerts](https://docs.aws.amazon.com/redshift/latest/dg/c-reviewing-query-alerts.html): Describes how to use the STL_ALERT_EVENT_LOG table to identify query performance issues.
- [Analyzing the query plan](https://docs.aws.amazon.com/redshift/latest/dg/c-analyzing-the-query-plan.html): Describes how to analyze a query plan to determine potential performance improvements.

### [Analyzing the query summary](https://docs.aws.amazon.com/redshift/latest/dg/c-analyzing-the-query-summary.html)

Describes how to analyze query summary information to determine potential performance improvements.

- [Using the SVL_QUERY_SUMMARY view](https://docs.aws.amazon.com/redshift/latest/dg/using-SVL-Query-Summary.html): To analyze query summary information by stream using , do the following:
- [Using the SVL_QUERY_REPORT view](https://docs.aws.amazon.com/redshift/latest/dg/using-SVL-Query-Report.html): To analyze query summary information by slice using , do the following:
- [Mapping the query plan to the query summary](https://docs.aws.amazon.com/redshift/latest/dg/query-plan-summary-map.html): When analyzing the query summary, you can get further details by mapping the operations from the query plan to the steps (identified by the label field values) in the query summary.
- [Query improvement](https://docs.aws.amazon.com/redshift/latest/dg/query-performance-improvement-opportunities.html): This topic identifies common issues that affect query performance, how to diagnose them, and how to resolve them.

### [Diagnostic queries for query tuning](https://docs.aws.amazon.com/redshift/latest/dg/diagnostic-queries-for-query-tuning.html)

This topic provides queries to identify issues with queries or their underlying tables that can affect query performance.

- [Identifying queries that are top candidates for tuning](https://docs.aws.amazon.com/redshift/latest/dg/identify-queries-that-are-top-candidates-for-tuning.html): The following query identifies the top 50 most time-consuming statements that have been run in the last 7 days.
- [Identifying tables with data skew or unsorted rows](https://docs.aws.amazon.com/redshift/latest/dg/identify-tables-with-data-skew-or-unsorted-rows.html): The following query identifies tables that have uneven data distribution (data skew) or a high percentage of unsorted rows.
- [Identifying queries with nested loops](https://docs.aws.amazon.com/redshift/latest/dg/identify-queries-with-nested-loops.html): The following query identifies queries that have had alert events logged for nested loops.
- [Reviewing queue wait times for queries](https://docs.aws.amazon.com/redshift/latest/dg/review-queue-wait-times-for-queries.html): The following query shows how long recent queries waited for an open slot in a query queue before running.
- [Reviewing query alerts by table](https://docs.aws.amazon.com/redshift/latest/dg/review-query-alerts-by-table.html): The following query identifies tables that have had alert events logged for them, and also identifies what type of alerts are most frequently raised.
- [Identifying tables with missing statistics](https://docs.aws.amazon.com/redshift/latest/dg/identify-tables-with-missing-statistics.html): The following query provides a count of the queries that you are running against tables that are missing statistics.

### [Query troubleshooting](https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting.html)

This section provides a quick reference for identifying and addressing some of the most common and most serious issues that you are likely to encounter with Amazon Redshift queries.

- [Connection fails](https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting-connection-fails.html): Your query connection can fail because for the following reasons.
- [Query hangs](https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting-query-hangs.html): Your query can hang, or stop responding, for the following reasons.
- [Query takes too long](https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting-query-takes-too-long.html): Your query can take too long for the following reasons.
- [Load fails](https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting-load-fails.html): Your data load can fail for the following reasons.
- [Load takes too long](https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting-load-takes-too-long.html): Your load operation can take too long for the following reasons.
- [Load data is incorrect](https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting-load-data-incorrect.html): Your COPY operation can load incorrect data in the following ways.
- [Setting the JDBC fetch size parameter](https://docs.aws.amazon.com/redshift/latest/dg/set-the-JDBC-fetch-size-parameter.html): By default, the Redshift JDBC driver uses a ring buffer to manage memory efficiently and prevent out-of-memory errors.


## [Workload management](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-implementing-workload-management.html)

### [Automatic WLM](https://docs.aws.amazon.com/redshift/latest/dg/automatic-wlm.html)

With automatic workload management (WLM), Amazon Redshift manages query concurrency and memory allocation.

- [Query priority](https://docs.aws.amazon.com/redshift/latest/dg/query-priority.html): With Amazon Redshift, you can manage query prioritization and resource allocation across concurrent queries and workloads using Workload Management (WM).

### [Manual WLM](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-defining-query-queues.html)

Define query queues by modifying the manual WLM configuration in Amazon Redshift for a cluster to define up to eight query queues in addition to the superuser queue.

- [WLM query queue hopping](https://docs.aws.amazon.com/redshift/latest/dg/wlm-queue-hopping.html): With Amazon Redshift, you can manage workload concurrency and resource allocation by enabling WLM (Workload Management) query queue hopping.
- [Tutorial: Configuring manual WLM queues](https://docs.aws.amazon.com/redshift/latest/dg/tutorial-configuring-workload-management.html): Learn about and configure workload management (WLM) manual queues in Amazon Redshift.
- [Concurrency scaling](https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html): With the Concurrency Scaling feature, you can support thousands of concurrent users and concurrent queries, with consistently fast query performance.
- [Short query acceleration](https://docs.aws.amazon.com/redshift/latest/dg/wlm-short-query-acceleration.html): Short query acceleration (SQA) in Amazon Redshift prioritizes selected short-running queries ahead of longer-running queries.
- [WLM queue assignment rules](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-queue-assignment-rules.html): When a user runs a query, Amazon Redshift WLM assigns the query to the first matching queue, based on these rules.
- [Assigning queries to queues](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-executing-queries.html): Find examples of how to assign queries to queues according to user roles, user groups, and query groups in Amazon Redshift.

### [Dynamic and static properties](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-dynamic-properties.html)

If you change any of the WLM dynamic properties in Amazon Redshift, you don't need to reboot your cluster for the changes to take effect.

- [WLM dynamic memory allocation](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-dynamic-memory-allocation.html): In each queue, WLM creates a number of query slots equal to the queue's concurrency level.
- [Dynamic WLM example](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-dynamic-example.html): With Amazon Redshift, you can automatically manage workload distribution and resource allocation across your Amazon Redshift clusters using Dynamic WLM (Workload Management).
- [Query monitoring rules](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html): In Amazon Redshift workload management (WLM), query monitoring rules define metrics-based performance boundaries for WLM queues and specify what action to take when a query goes beyond those boundaries.
- [WLM system tables and views](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-system-tables-and-views.html): View the status of Amazon Redshift queries, queues, and service classes by using WLM-specific system tables.


## [Database security](https://docs.aws.amazon.com/redshift/latest/dg/r_Database_objects.html)

- [Amazon Redshift security overview](https://docs.aws.amazon.com/redshift/latest/dg/c_security-overview.html): Describes the features that Amazon Redshift provides to manage database security.
- [Default database user permissions](https://docs.aws.amazon.com/redshift/latest/dg/r_Privileges.html): Lists the default user permissions that you have when you create a database object or if you are a superuser.
- [Superusers](https://docs.aws.amazon.com/redshift/latest/dg/r_superusers.html): Lists the default user permissions that you have when you are a database superuser.

### [Users](https://docs.aws.amazon.com/redshift/latest/dg/r_Users.html)

Describes how to create, change, and delete users for Amazon Redshift.

- [Creating, altering, and deleting users](https://docs.aws.amazon.com/redshift/latest/dg/r_Users-creatingaltering-and-deleting-users.html): Database users are global across a data warehouse cluster (and not for each individual database).

### [Groups](https://docs.aws.amazon.com/redshift/latest/dg/r_Groups.html)

Describes how to create, change, and delete groups, which are collections of users.

- [Creating, altering, and deleting groups](https://docs.aws.amazon.com/redshift/latest/dg/r_Groups-creating-altering-and-deleting-groups.html): Only a superuser can create, alter, or drop groups.
- [Example for controlling user and group access](https://docs.aws.amazon.com/redshift/latest/dg/t_user_group_examples.html): Provides an example for controlling user and group access to an Amazon Redshift database.

### [Schemas](https://docs.aws.amazon.com/redshift/latest/dg/r_Schemas_and_tables.html)

Describes how to create, change, and delete schemas.

- [Creating, altering, and deleting schemas](https://docs.aws.amazon.com/redshift/latest/dg/r_Schemas_and_tables-creating-altering-and-deleting-schemas.html): Any user can create schemas and alter or drop schemas they own.
- [Permissions](https://docs.aws.amazon.com/redshift/latest/dg/r_Schemas_and_tables-schema-based-privileges.html): Schema-based permissions are determined by the owner of the schema:

### [Role-based access control](https://docs.aws.amazon.com/redshift/latest/dg/t_Roles.html)

Create, change, and delete roles for role-based access control (RBAC) in Amazon Redshift.

- [Role hierarchy](https://docs.aws.amazon.com/redshift/latest/dg/t_role_hierarchy.html): Learn about role hierarchy and role authorization cycle when working with role-based access control (RBAC) in Amazon Redshift.
- [Role assignment](https://docs.aws.amazon.com/redshift/latest/dg/t_role_assignment.html): Learn how to create and grant roles for role-based access control (RBAC) in Amazon Redshift.
- [Amazon Redshift system-defined roles](https://docs.aws.amazon.com/redshift/latest/dg/r_roles-default.html): Learn about the system-defined roles that are defined with specific permissions by Amazon Redshift.
- [System permissions](https://docs.aws.amazon.com/redshift/latest/dg/r_roles-system-privileges.html): Find a list of system permissions that you can grant to or revoke from a role when using role-based access control (RBAC) in Amazon Redshift.
- [Database object permissions](https://docs.aws.amazon.com/redshift/latest/dg/r_roles-database-privileges.html): Find a list of database object permissions for use with role-based access control (RBAC) in Amazon Redshift.
- [ALTER DEFAULT PRIVILEGES for RBAC](https://docs.aws.amazon.com/redshift/latest/dg/r_roles-alter-default-privileges.html): Set ALTER DEFAULT PRIVILEGES for RBAC.
- [Considerations for role usage](https://docs.aws.amazon.com/redshift/latest/dg/r_role-usage-notes.html): Learn about considerations for role usage when using role-based access control (RBAC) in Amazon Redshift.
- [Managing roles](https://docs.aws.amazon.com/redshift/latest/dg/r_roles-managing.html): Manage roles in role-based access control (RBAC) in Amazon Redshift.
- [Tutorial: Creating roles and querying with RBAC](https://docs.aws.amazon.com/redshift/latest/dg/r_tutorial-RBAC.html): Learn about creating roles and querying when using role-based access control (RBAC) in Amazon Redshift.

### [Row-level security](https://docs.aws.amazon.com/redshift/latest/dg/t_rls.html)

Amazon Redshift uses security policies to provide granular access control to user data.

- [Using RLS policies in SQL statements](https://docs.aws.amazon.com/redshift/latest/dg/t_rls_statements.html): Describes how RLS policies are used in SQL statements.
- [Combining multiple policies per user](https://docs.aws.amazon.com/redshift/latest/dg/t_rls_combine_policies.html): Describes how to combine multiple policies per user.
- [RLS policy ownership and management](https://docs.aws.amazon.com/redshift/latest/dg/t_rls_ownership.html): Describes RLS policy ownership and management.
- [Policy-dependent objects and principles](https://docs.aws.amazon.com/redshift/latest/dg/t_rls_object_dependency.html): Describes policy-dependent objects and principles.
- [Considerations and limitations](https://docs.aws.amazon.com/redshift/latest/dg/t_rls_usage.html): Describes RLS policy considerations.
- [Best practices](https://docs.aws.amazon.com/redshift/latest/dg/t_rls_performance.html): Describes best practices to ensure better performance from Amazon Redshift on tables protected by RLS.
- [End-to-end example](https://docs.aws.amazon.com/redshift/latest/dg/t_rls-example.html): An end-to-end example of using row-level security policies in Amazon Redshift.
- [Metadata security](https://docs.aws.amazon.com/redshift/latest/dg/t_metadata_security.html): Amazon Redshift lets you enable metadata security viewing so users can view metadata related to objects they have access to.

### [Dynamic data masking](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm.html)

Amazon Redshift uses dynamic data masking to obfuscate customer data at the time of SQL command runtime.

- [SQL commands for DDM policies](https://docs.aws.amazon.com/redshift/latest/dg/r_ddm-procedures.html): Lists the SQL commands for manipulating dynamic data masking masking policies.
- [DDM policy hierarchy](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm-hierarchy.html): Describes the hierarchy when applying multiple dynamic data masking policies to a single column.
- [Using DDM with SUPER type paths](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm-super.html): Describes attaching dynamic data masking policies to SUPER type paths.
- [Conditional dynamic data masking](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm-conditional.html): Describes using conditional expressions to apply DDM policies at the cell level.
- [DDM system views](https://docs.aws.amazon.com/redshift/latest/dg/r_ddm-svv.html): List of system views for DDM.
- [Considerations](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm-considerations.html): When using dynamic data masking, consider the following:
- [End-to-end example](https://docs.aws.amazon.com/redshift/latest/dg/ddm-example.html): The following is an end-to-end example showing how you can create and attach masking policies to a column.

### [Scoped permissions](https://docs.aws.amazon.com/redshift/latest/dg/t_scoped-permissions.html)

Learn about granting database- or schema-scoped permissions in Amazon Redshift.

- [Considerations](https://docs.aws.amazon.com/redshift/latest/dg/t_scoped-permissions-considerations.html): When using scoped permissions, consider the following:


## [SQL reference](https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_SQLCommandRef.html)

### [Amazon Redshift SQL](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift-sql.html)

Describes the industry-standard SQL functions with the added functionality that Amazon Redshift uses.

- [SQL functions supported on the leader node](https://docs.aws.amazon.com/redshift/latest/dg/c_sql-functions-leader-node.html): Describes the SQL functions that Amazon Redshift supports on the leader node.

### [Amazon Redshift and PostgreSQL](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift-and-postgres-sql.html)

Describes the design differences between Amazon Redshift and PostgreSQL.

- [Amazon Redshift and PostgreSQL JDBC and ODBC](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift-postgres-jdbc.html): Describes the Amazon Redshift implementation of PostgreSQL JDBC and ODBC drivers.
- [Features that are implemented differently](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift-sql-implementated-differently.html): Lists the features that are implemented differently from the equivalent PostgreSQL implementation.
- [Unsupported PostgreSQL features](https://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-features.html): Lists the PostgreSQL features that are not supported in Amazon Redshift.
- [Unsupported PostgreSQL data types](https://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-datatypes.html): Lists the PostgreSQL data types that are not supported in Amazon Redshift.
- [Unsupported PostgreSQL functions](https://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-functions.html): Lists the PostgreSQL functions that are not supported in Amazon Redshift.

### [Using SQL](https://docs.aws.amazon.com/redshift/latest/dg/c_SQL_reference.html)

Describes how to use the SQL commands and functions with Amazon Redshift.

- [SQL reference conventions](https://docs.aws.amazon.com/redshift/latest/dg/c_SQL_reference_conventions.html): Lists the conventions used to write the synopses for the SQL expressions, commands, and functions.

### [Basic elements](https://docs.aws.amazon.com/redshift/latest/dg/c_Basic_elements.html)

Describes the rules for working with database object names, literals, nulls, and data types used in Amazon Redshift.

- [Names and identifiers](https://docs.aws.amazon.com/redshift/latest/dg/r_names.html): Describes the rules for working with database object names and identifiers supported by Amazon Redshift.
- [Literals](https://docs.aws.amazon.com/redshift/latest/dg/r_Literals.html): Describes the rules for working with database literals or constants supported by Amazon Redshift.
- [Nulls](https://docs.aws.amazon.com/redshift/latest/dg/r_Nulls.html): Describes the rules for working with database nulls supported by Amazon Redshift.

### [Data types](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html)

Describes the rules for working with database data type supported by Amazon Redshift.

### [Numeric types](https://docs.aws.amazon.com/redshift/latest/dg/r_Numeric_types201.html)

Describes the rules for working with numeric types supported by Amazon Redshift.

- [Computations with numeric values](https://docs.aws.amazon.com/redshift/latest/dg/r_numeric_computations201.html): Describes the rules for performing computations with numeric values supported by Amazon Redshift.
- [Integer and floating-point literals](https://docs.aws.amazon.com/redshift/latest/dg/r_numeric_literals201.html): Describes the rules for working with integers and floating-point literals supported by Amazon Redshift.
- [Examples with numeric types](https://docs.aws.amazon.com/redshift/latest/dg/r_Examples_with_numeric_types201.html): Lists examples of working with numeric types supported by Amazon Redshift.

### [Character types](https://docs.aws.amazon.com/redshift/latest/dg/r_Character_types.html)

Describes the rules for working with character types supported by Amazon Redshift.

- [Examples with character types](https://docs.aws.amazon.com/redshift/latest/dg/r_Examples_with_character_types.html): Lists examples of working with character types supported by Amazon Redshift.

### [Datetime types](https://docs.aws.amazon.com/redshift/latest/dg/r_Datetime_types.html)

Describes the rules for working with datetime types supported by Amazon Redshift.

- [Examples with datetime types](https://docs.aws.amazon.com/redshift/latest/dg/r_Examples_with_datetime_types.html): Find examples of working with datetime types supported by Amazon Redshift.
- [Date, time, and timestamp literals](https://docs.aws.amazon.com/redshift/latest/dg/r_Date_and_time_literals.html): Find rules for working with date, time, and timestamp literals supported by Amazon Redshift.

### [Interval data types and literals](https://docs.aws.amazon.com/redshift/latest/dg/r_interval_data_types.html)

Find rules for working with interval data types and literals supported by Amazon Redshift.

- [Examples of interval literals without qualifier syntax](https://docs.aws.amazon.com/redshift/latest/dg/r_interval_literals.html): Shows examples of using interval literals without qualifier syntax.
- [Boolean type](https://docs.aws.amazon.com/redshift/latest/dg/r_Boolean_type.html): Describes the rules for working with Boolean data types supported by Amazon Redshift.
- [HLLSKETCH type](https://docs.aws.amazon.com/redshift/latest/dg/r_HLLSKTECH_type.html): Describes the HLLSKETCH data type supported by Amazon Redshift.
- [SUPER type](https://docs.aws.amazon.com/redshift/latest/dg/r_SUPER_type.html): Describes the SUPER data type supported by Amazon Redshift.
- [VARBYTE type](https://docs.aws.amazon.com/redshift/latest/dg/r_VARBYTE_type.html): Describes the VARBYTE data type supported by Amazon Redshift.
- [Collation sequences](https://docs.aws.amazon.com/redshift/latest/dg/c_collation_sequences.html): Amazon Redshift does not support locale-specific or user-defined collation sequences.

### [Expressions](https://docs.aws.amazon.com/redshift/latest/dg/r_expressions.html)

Describes the rules for working with expressions supported by Amazon Redshift.

- [Compound expressions](https://docs.aws.amazon.com/redshift/latest/dg/r_compound_expressions.html): Describes the rules for working with compound expressions supported by Amazon Redshift.
- [Expression lists](https://docs.aws.amazon.com/redshift/latest/dg/r_expression_lists.html): Describes the rules for working with expression lists supported by Amazon Redshift.
- [Scalar subqueries](https://docs.aws.amazon.com/redshift/latest/dg/r_scalar_subqueries.html): Describes the rules for working with scalar subqueries supported by Amazon Redshift.
- [Function expressions](https://docs.aws.amazon.com/redshift/latest/dg/r_function_expressions.html): Describes the rules for working with function expressions supported by Amazon Redshift.

### [Conditions](https://docs.aws.amazon.com/redshift/latest/dg/r_conditions.html)

Describes the rules for working with conditions supported by Amazon Redshift.

- [Comparison condition](https://docs.aws.amazon.com/redshift/latest/dg/r_comparison_condition.html): Describes the rules for working with comparison conditions supported by Amazon Redshift.
- [Logical conditions](https://docs.aws.amazon.com/redshift/latest/dg/r_logical_condition.html): Describes the rules for working with logical conditions supported by Amazon Redshift.

### [Pattern-matching conditions](https://docs.aws.amazon.com/redshift/latest/dg/pattern-matching-conditions.html)

A pattern-matching operator searches a string for a pattern specified in the conditional expression and returns true or false depend on whether it finds a match.

- [LIKE](https://docs.aws.amazon.com/redshift/latest/dg/r_patternmatching_condition_like.html): Describes the pattern-matching condition LIKE operator supported by Amazon Redshift.
- [SIMILAR TO](https://docs.aws.amazon.com/redshift/latest/dg/pattern-matching-conditions-similar-to.html): Matches a string expression with a SQL standard regular expression pattern that can include a set of pattern-matching metacharacters, including the two supported by the LIKE operator.
- [POSIX operators](https://docs.aws.amazon.com/redshift/latest/dg/pattern-matching-conditions-posix.html): POSIX regular expression patterns can match any portion of a string, unlike the SIMILAR TO operator, which returns true only if its pattern matches the entire string.
- [BETWEEN range condition](https://docs.aws.amazon.com/redshift/latest/dg/r_range_condition.html): Tests expressions for inclusion in a range of values, using the keywords BETWEEN and AND.
- [Null condition](https://docs.aws.amazon.com/redshift/latest/dg/r_null_condition.html): Tests for nulls, when a value is missing or unknown.
- [EXISTS condition](https://docs.aws.amazon.com/redshift/latest/dg/r_exists_condition.html): Tests for the existence of rows in a subquery, and return true if a subquery returns at least one row.
- [IN Condition](https://docs.aws.amazon.com/redshift/latest/dg/r_in_condition.html): Tests a value for membership in a set of values or in a subquery.

### [SQL commands](https://docs.aws.amazon.com/redshift/latest/dg/c_SQL_commands.html)

Learn about the standard SQL commands that Amazon Redshift uses to create database objects, run queries, load tables, and modify the data in tables.

- [ABORT](https://docs.aws.amazon.com/redshift/latest/dg/r_ABORT.html): Stops the currently running transaction and discards all updates made by that transaction.
- [ALTER DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_DATABASE.html): Changes the attributes of a database.
- [ALTER DATASHARE](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_DATASHARE.html): Alters a datashare.
- [ALTER DEFAULT PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_DEFAULT_PRIVILEGES.html): Defines the default set of access permissions that will be applied to objects created in the future by the specified user.
- [ALTER EXTERNAL SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_EXTERNAL_SCHEMA.html): Alters an existing external schema in the current database.
- [ALTER EXTERNAL VIEW](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_EXTERNAL_VIEW.html): Changes a user group, such as adding users to the group, dropping users from the group, or renaming the group.
- [ALTER FUNCTION](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_FUNCTION.html): Renames a function or changes the owner.
- [ALTER GROUP](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_GROUP.html): Changes a user group, such as adding users to the group, dropping users from the group, or renaming the group.
- [ALTER IDENTITY PROVIDER](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_IDENTITY_PROVIDER.html): Alters an identity provider to assign new parameters and values.
- [ALTER MASKING POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_MASKING_POLICY.html): Alters an existing dynamic data masking policy.

### [ALTER MATERIALIZED VIEW](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_MATERIALIZED_VIEW.html)

Changes the attributes of a materialized view.

- [DISTSTYLE and SORTKEY examples](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_MATERIALIZED_VIEW-DISTSTYLE-SORTKEY-examples.html): The examples in this topic show you how to perform DISTSTYLE and SORTKEY changes, using ALTER MATERIALIZED VIEW.
- [ALTER RLS POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_RLS_POLICY.html): Alter an existing row-level security policy on a table.
- [ALTER ROLE](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_ROLE.html): Renames a role or changes the owner.
- [ALTER PROCEDURE](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_PROCEDURE.html): Renames a procedure or changes the owner.
- [ALTER SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_SCHEMA.html): Changes the definition of an existing schema.
- [ALTER SYSTEM](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_SYSTEM.html): Changes a system-level configuration option.

### [ALTER TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_TABLE.html)

Changes the definition of a Amazon Redshift table.

- [ALTER TABLE examples](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_TABLE_examples_basic.html): Provides examples of how to perform basic tasks using the ALTER TABLE command.
- [ALTER EXTERNAL TABLE examples](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_TABLE_external-table.html): Provides examples of how to alter an external table.
- [ALTER TABLE ADD and DROP COLUMN examples](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_TABLE_COL_ex-add-drop.html): Provides examples of how to add and drop a basic table column using the ALTER TABLE ADD and DROP COLUMN commands.
- [ALTER TABLE APPEND](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_TABLE_APPEND.html): Appends rows to a target table by moving data from an existing source table.
- [ALTER TEMPLATE](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_TEMPLATE.html): Modifies an existing template definition.
- [ALTER USER](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_USER.html): Changes a database user.
- [ANALYZE](https://docs.aws.amazon.com/redshift/latest/dg/r_ANALYZE.html): Updates the table statistics for use by the query planner.
- [ANALYZE COMPRESSION](https://docs.aws.amazon.com/redshift/latest/dg/r_ANALYZE_COMPRESSION.html): Performs compression analysis and produces a report with the suggested column encoding schemes and an estimate of the potential reduction for the tables analyzed.
- [ATTACH MASKING POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_ATTACH_MASKING_POLICY.html): Attaches an existing dynamic data masking policy to a column.
- [ATTACH RLS POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_ATTACH_RLS_POLICY.html): Attach a row-level security policy on a table to one or more users or roles..
- [BEGIN](https://docs.aws.amazon.com/redshift/latest/dg/r_BEGIN.html): Starts a transaction.
- [CALL](https://docs.aws.amazon.com/redshift/latest/dg/r_CALL_procedure.html): Runs a stored procedure.
- [CANCEL](https://docs.aws.amazon.com/redshift/latest/dg/r_CANCEL.html): Cancels a database query that is currently running.
- [CLOSE](https://docs.aws.amazon.com/redshift/latest/dg/close.html): Closes all of the free resources that are associated with an open cursor.
- [COMMENT](https://docs.aws.amazon.com/redshift/latest/dg/r_COMMENT.html): Creates or changes a comment about a database object.
- [COMMIT](https://docs.aws.amazon.com/redshift/latest/dg/r_COMMIT.html): Commits the current transaction to the database.

### [COPY](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html)

Loads data into a table from data files or from an Amazon DynamoDB table.

- [COPY JOB](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY-JOB.html): Manages COPY commands that load Amazon S3 file data into a table.
- [COPY with TEMPLATE](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY-WITH-TEMPLATE.html): You can use Redshift templates with COPY commands to simplify command syntax and ensure consistency across data loading operations.

### [COPY parameter reference](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY-parameters.html)

COPY has many parameters that can be used in many situations.

### [Data sources](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-source.html)

You can load data from text files in an Amazon S3 bucket, in an Amazon EMR cluster, or on a remote host that your cluster can access using an SSH connection.

- [COPY from Amazon S3](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-source-s3.html): To load data from files located in one or more S3 buckets, use the FROM clause to indicate how COPY locates the files in Amazon S3.
- [COPY from Amazon EMR](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-source-emr.html): You can use the COPY command to load data in parallel from an Amazon EMR cluster configured to write text files to the cluster's Hadoop Distributed File System (HDFS) in the form of fixed-width files, character-delimited files, CSV files, JSON-formatted files, or Avro files.
- [COPY from remote host (SSH)](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-source-ssh.html): You can use the COPY command to load data in parallel from one or more remote hosts, such Amazon Elastic Compute Cloud (Amazon EC2) instances or other computers.
- [COPY from Amazon DynamoDB](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-source-dynamodb.html): To load data from an existing DynamoDB table, use the FROM clause to specify the DynamoDB table name.
- [Authorization parameters](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-authorization.html): The COPY command needs authorization to access data in another AWS resource, including in Amazon S3, Amazon EMR, Amazon DynamoDB, and Amazon EC2.
- [Column mapping options](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-column-mapping.html): By default, COPY inserts values into the target table's columns in the same order as fields occur in the data files.
- [Data format parameters](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-format.html): By default, the COPY command expects the source data to be character-delimited UTF-8 text.
- [File compression parameters](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-file-compression.html): You can load from compressed data files by specifying the following parameters.
- [Data conversion parameters](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-conversion.html): As it loads the table, COPY attempts to implicitly convert the strings in the source data to the data type of the target column.
- [Data load operations](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-load.html): Manage the default behavior of the load operation for troubleshooting or to reduce load times by specifying the following parameters.
- [Alphabetical parameter list](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY-alphabetical-parm-list.html): The following list provides links to each COPY command parameter description, sorted alphabetically.

### [Usage notes](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_usage_notes.html)

Describes the usage notes for using the COPY command.

- [Access permissions](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-access-permissions.html): To move data between your cluster and another AWS resource, such as Amazon S3, Amazon DynamoDB, Amazon EMR, or Amazon EC2, your cluster must have permission to access the resource and perform the necessary actions.
- [Using COPY with Amazon S3 access point aliases](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-s3-access-point-alias.html): You can use Amazon S3 access point aliases with COPY commands.
- [Loading multibyte data from Amazon S3](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-multi-byte.html): Describes loading multibyte data from Amazon S3 if your data includes non-ASCII characters such as Chinese or Cyrillic characters.
- [Loading a column of the GEOMETRY or GEOGRAPHY data type](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-spatial-data.html): Find out about loading a column of the GEOMETRY or GEOGRAPHY data type for Amazon Redshift,
- [Loading the HLLSKETCH data type](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-hll.html): Find out about loading the HLLSKETCH data type for Amazon Redshift.
- [Loading a column of the VARBYTE data type](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage-varbyte.html): You can load data from a file in CSV, Parquet, and ORC format.
- [Errors when reading multiple files](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-multiple-files.html): Find out about how the COPY command handles errors when reading multiple files for Amazon Redshift.
- [COPY from JSON](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-copy-from-json.html): Describes how to use the Amazon Redshift COPY command to load tables from data in JSON format.
- [COPY from columnar data formats](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-copy-from-columnar.html): COPY can load data from Amazon S3 in the following columnar formats:
- [DATEFORMAT and TIMEFORMAT strings](https://docs.aws.amazon.com/redshift/latest/dg/r_DATEFORMAT_and_TIMEFORMAT_strings.html): Describes the DATEFORMAT and TIMEFORMAT options in the COPY command.
- [Using automatic recognition with DATEFORMAT and TIMEFORMAT](https://docs.aws.amazon.com/redshift/latest/dg/automatic-recognition.html): Describes how to automatically recognize and convert the date format or time format in your source data.
- [COPY examples](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html): Provides examples of how to use the COPY to load data from a variety of sources.
- [CREATE DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATABASE.html): Creates a new database.
- [CREATE DATASHARE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATASHARE.html): Creates a new datashare.
- [CREATE EXTERNAL FUNCTION](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_FUNCTION.html): Creates a scalar user-defined function (UDF) based on AWS Lambda for Amazon Redshift.
- [CREATE EXTERNAL MODEL](https://docs.aws.amazon.com/redshift/latest/dg/r_create_external_model.html): The CREATE EXTERNAL MODEL statement creates an interface for using Amazon Bedrock to generate text using a LLM based on user data.
- [CREATE EXTERNAL SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_SCHEMA.html): Creates a new external schema.

### [CREATE EXTERNAL TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_TABLE.html)

Creates a new external table in the current database.

- [Usage notes](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_TABLE_usage.html): This topic contains usage notes for .
- [Examples](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_TABLE_examples.html): Provides examples that demonstrate how to use the CREATE EXTERNAL TABLE command.
- [CREATE EXTERNAL VIEW](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_VIEW.html): Changes a user group, such as adding users to the group, dropping users from the group, or renaming the group.
- [CREATE FUNCTION](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_FUNCTION.html): Creates a new scalar user-defined function (UDF) using either a SQL SELECT clause or a Python program.
- [CREATE GROUP](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_GROUP.html): Defines a new user group.
- [CREATE IDENTITY PROVIDER](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_IDENTITY_PROVIDER.html): Defines a new identity provider.
- [CREATE LIBRARY](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_LIBRARY.html): Installs a Python library, which is available for users to incorporate when creating a user-defined function (UDF) with the command.
- [CREATE MASKING POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_MASKING_POLICY.html): Creates a new dynamic data masking policy to obfuscate data of a given format.
- [CREATE MATERIALIZED VIEW](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-create-sql-command.html): Creates a materialized view.

### [CREATE MODEL](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_MODEL.html)

The CREATE MODEL statement offers flexibility in the number of parameters used to create the model.

- [Usage notes](https://docs.aws.amazon.com/redshift/latest/dg/r_create_model_usage_notes.html): When using CREATE MODEL, consider the following:
- [Use cases](https://docs.aws.amazon.com/redshift/latest/dg/r_create_model_use_cases.html): Information about the various cases of CREATE MODEL.
- [CREATE PROCEDURE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_PROCEDURE.html): Creates a new stored procedure or replaces an existing procedure for the current database.
- [CREATE RLS POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_RLS_POLICY.html): Creates a new row-level security policy to provide granular access to database objects.
- [CREATE ROLE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_ROLE.html): Creates a new role.
- [CREATE SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_SCHEMA.html): Defines a new schema for the current database.

### [CREATE TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_NEW.html)

Creates a new table in the current database.

- [Examples](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_examples.html): Provides examples that demonstrate how to use the CREATE TABLE command.

### [CREATE TABLE AS](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_AS.html)

Creates a new table based on a query.

- [CTAS usage notes](https://docs.aws.amazon.com/redshift/latest/dg/r_CTAS_usage_notes.html): Describes the basic usage that you need to know about using the CREATE TABLE AS command.
- [CTAS examples](https://docs.aws.amazon.com/redshift/latest/dg/r_CTAS_examples.html): Provides examples of using the CREATE TABLE AS command.
- [CREATE TEMPLATE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TEMPLATE.html): Creates reusable templates for Amazon Redshift commands like COPY, UNLOAD and CREATE MODEL.
- [CREATE USER](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html): Creates a new database user.
- [CREATE VIEW](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_VIEW.html): Creates a view in a database.
- [DEALLOCATE](https://docs.aws.amazon.com/redshift/latest/dg/r_DEALLOCATE.html): Deallocates a prepared statement.
- [DECLARE](https://docs.aws.amazon.com/redshift/latest/dg/declare.html): Defines a new cursor within a transaction block.
- [DELETE](https://docs.aws.amazon.com/redshift/latest/dg/r_DELETE.html): Deletes rows from a table or materialized view.
- [DESC DATASHARE](https://docs.aws.amazon.com/redshift/latest/dg/r_DESC_DATASHARE.html): Displays a list of the database objects within a datashare that are added to it using ALTER DATASHARE.
- [DESC IDENTITY PROVIDER](https://docs.aws.amazon.com/redshift/latest/dg/r_DESC_IDENTITY_PROVIDER.html): Displays information about an identity provider.
- [DETACH MASKING POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_DETACH_MASKING_POLICY.html): Detaches an attached dynamic data masking policy from a column.
- [DETACH RLS POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_DETACH_RLS_POLICY.html): Detach a row-level security policy on a table from one or more users or roles.
- [DROP DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_DATABASE.html): Drops a database.
- [DROP DATASHARE](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_DATASHARE.html): Drops a datashare.
- [DROP EXTERNAL VIEW](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_EXTERNAL_VIEW.html): Changes a user group, such as adding users to the group, dropping users from the group, or renaming the group.
- [DROP FUNCTION](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_FUNCTION.html): Removes a user-defined function (UDF) from the database.
- [DROP GROUP](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_GROUP.html): Deletes a user group but doesn't delete the individual users in a group.
- [DROP IDENTITY PROVIDER](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_IDENTITY_PROVIDER.html): Deletes an identity provider.
- [DROP LIBRARY](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_LIBRARY.html): Removes a custom Python library from the database.
- [DROP MASKING POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_MASKING_POLICY.html): Drops a dynamic data masking policy from all databases.
- [DROP MODEL](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_MODEL.html): Removes a model from the database.
- [DROP MATERIALIZED VIEW](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-drop-sql-command.html): Removes a materialized view.
- [DROP PROCEDURE](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_PROCEDURE.html): Drops a procedure.
- [DROP RLS POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_RLS_POLICY.html): Drops a row-level security policy for all tables in all databases.
- [DROP ROLE](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_ROLE.html): Removes a role from a database.
- [DROP SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_SCHEMA.html): Deletes a schema.
- [DROP TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_TABLE.html): Removes a table from a database.
- [DROP TEMPLATE](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_TEMPLATE.html): Drops a template from a database.
- [DROP USER](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_USER.html): Drops a user from a database.
- [DROP VIEW](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_VIEW.html): Removes a view from the database.
- [END](https://docs.aws.amazon.com/redshift/latest/dg/r_END.html): Commits the current transaction.
- [EXECUTE](https://docs.aws.amazon.com/redshift/latest/dg/r_EXECUTE.html): Runs a previously prepared statement.
- [EXPLAIN](https://docs.aws.amazon.com/redshift/latest/dg/r_EXPLAIN.html): Displays the execution plan for a query statement without running the query.
- [FETCH](https://docs.aws.amazon.com/redshift/latest/dg/fetch.html): Retrieves rows using a cursor.

### [GRANT](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT.html)

Defines access privileges for a user or user group.

- [Usage notes](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT-usage-notes.html): Guidelines for using the GRANT SQL command.
- [Examples](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT-examples.html): Examples of how to use the GRANT SQL command.

### [INSERT](https://docs.aws.amazon.com/redshift/latest/dg/r_INSERT_30.html)

Inserts new rows into a table.

- [INSERT examples](https://docs.aws.amazon.com/redshift/latest/dg/c_Examples_of_INSERT_30.html): Provides examples of how to use the INSERT command.
- [INSERT (external table)](https://docs.aws.amazon.com/redshift/latest/dg/r_INSERT_external_table.html): Inserts the results of a SELECT query into existing partitioned or non-partitioned external tables.
- [LOCK](https://docs.aws.amazon.com/redshift/latest/dg/r_LOCK.html): Restricts access to a database table.
- [MERGE](https://docs.aws.amazon.com/redshift/latest/dg/r_MERGE.html): Inserts, updates, and deletes values in a table based on values from a source table.
- [PREPARE](https://docs.aws.amazon.com/redshift/latest/dg/r_PREPARE.html): Prepares a statement for execution.
- [REFRESH MATERIALIZED VIEW](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-refresh-sql-command.html): Refreshes a materialized view.
- [RESET](https://docs.aws.amazon.com/redshift/latest/dg/r_RESET.html): Restores the value of a configuration parameter to its default value.

### [REVOKE](https://docs.aws.amazon.com/redshift/latest/dg/r_REVOKE.html)

Removes access permissions, such as permissions to create, drop, or update tables, from a user or role.

- [Usage notes](https://docs.aws.amazon.com/redshift/latest/dg/r_REVOKE-usage-notes.html): Guidelines for using the REVOKE SQL command.
- [Examples](https://docs.aws.amazon.com/redshift/latest/dg/r_REVOKE-examples.html): Examples of how to use the REVOKE SQL command.
- [ROLLBACK](https://docs.aws.amazon.com/redshift/latest/dg/r_ROLLBACK.html): Stops the current transaction and discards all updates made by that transaction.

### [SELECT](https://docs.aws.amazon.com/redshift/latest/dg/r_SELECT_synopsis.html)

Returns rows from tables, views, and user-defined functions.

- [WITH clause](https://docs.aws.amazon.com/redshift/latest/dg/r_WITH_clause.html): Defines one or more subqueries.
- [SELECT list](https://docs.aws.amazon.com/redshift/latest/dg/r_SELECT_list.html): Names the columns, functions, and expressions that you want the query to return.
- [EXCLUDE column_list](https://docs.aws.amazon.com/redshift/latest/dg/r_EXCLUDE_list.html): Names the columns that are excluded from the query results.

### [FROM clause](https://docs.aws.amazon.com/redshift/latest/dg/r_FROM_clause30.html)

Lists the table references (tables, views, and subqueries) in a query to show where the data is selected from.

- [PIVOT and UNPIVOT examples](https://docs.aws.amazon.com/redshift/latest/dg/r_FROM_clause-pivot-unpivot-examples.html): Contains examples for outputting rows to columns with PIVOT or columns to rows with UNPIVOT.
- [JOIN examples](https://docs.aws.amazon.com/redshift/latest/dg/r_Join_examples.html): Provides join query examples.
- [UNNEST examples](https://docs.aws.amazon.com/redshift/latest/dg/r_FROM_clause-unnest-examples.html): Contains examples for shredding semi-structured data using the UNNEST operation in the FROM clause.

### [WHERE clause](https://docs.aws.amazon.com/redshift/latest/dg/r_WHERE_clause.html)

Contains the conditions that either join tables or apply predicates to columns in tables.

- [Oracle-Style outer joins in the WHERE clause](https://docs.aws.amazon.com/redshift/latest/dg/r_WHERE_oracle_outer.html): Describes the Oracle outer-join operator (+) in WHERE clause join conditions for Oracle compatibility.

### [GROUP BY clause](https://docs.aws.amazon.com/redshift/latest/dg/r_GROUP_BY_clause.html)

Identifies the grouping columns for the query.

- [Aggregation extensions](https://docs.aws.amazon.com/redshift/latest/dg/r_GROUP_BY_aggregation-extensions.html): Amazon Redshift supports aggregation extensions to do the work of multiple GROUP BY operations in a single statement.
- [HAVING clause](https://docs.aws.amazon.com/redshift/latest/dg/r_HAVING_clause.html): Applies a condition to the intermediate grouped result set that a query returns.
- [QUALIFY clause](https://docs.aws.amazon.com/redshift/latest/dg/r_QUALIFY_clause.html): Filters results of a previously computed window function according to userâspecified search conditions

### [UNION, INTERSECT, and EXCEPT](https://docs.aws.amazon.com/redshift/latest/dg/r_UNION.html)

Compare and merge the results of two separate query expressions.

- [Example UNION queries](https://docs.aws.amazon.com/redshift/latest/dg/c_example_union_query.html): Provides examples of how to use UNION queries.
- [Example UNION ALL query](https://docs.aws.amazon.com/redshift/latest/dg/c_example_unionall_query.html): Provides examples of how to use a UNION ALL query.
- [Example INTERSECT queries](https://docs.aws.amazon.com/redshift/latest/dg/c_example_intersect_query.html): Provides examples of how to use INTERSECT queries.
- [Example EXCEPT query](https://docs.aws.amazon.com/redshift/latest/dg/c_Example_MINUS_query.html): Provides an example of how to use the EXCEPT query.

### [ORDER BY clause](https://docs.aws.amazon.com/redshift/latest/dg/r_ORDER_BY_clause.html)

Sorts the result set of a query.

- [Examples with ORDER BY](https://docs.aws.amazon.com/redshift/latest/dg/r_Examples_with_ORDER_BY.html): Provides examples of how to use the ORDER BY clause.
- [CONNECT BY clause](https://docs.aws.amazon.com/redshift/latest/dg/r_CONNECT_BY_clause.html): Specifies the relationship between rows in a hierarchy.
- [Subquery examples](https://docs.aws.amazon.com/redshift/latest/dg/r_Subquery_examples.html): Provides examples of subqueries that fit into SELECT and WHERE.
- [Correlated subqueries](https://docs.aws.amazon.com/redshift/latest/dg/r_correlated_subqueries.html): Provides examples of how to use correlated subqueries in the WHERE clause.
- [SELECT INTO](https://docs.aws.amazon.com/redshift/latest/dg/r_SELECT_INTO.html): Selects rows defined by any query and inserts them into a new table.
- [SET](https://docs.aws.amazon.com/redshift/latest/dg/r_SET.html): Sets the value of a server configuration parameter.
- [SET SESSION AUTHORIZATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SET_SESSION_AUTHORIZATION.html): Sets the user name for the current session.
- [SET SESSION CHARACTERISTICS](https://docs.aws.amazon.com/redshift/latest/dg/r_SET_SESSION_CHARACTERISTICS.html): This command is deprecated in Amazon Redshift.
- [SHOW](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW.html): Displays the current value of a server configuration parameter.
- [SHOW COLUMN GRANTS](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_COLUMN_GRANTS.html): Displays grants on a column within a table.
- [SHOW COLUMNS](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_COLUMNS.html): Shows the columns contained in a table.
- [SHOW CONSTRAINTS](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_CONSTRAINTS.html): Shows a list of primary key and foreign key constraints in a table.
- [SHOW EXTERNAL TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_EXTERNAL_TABLE.html): Shows the definition of an external table.
- [SHOW DATABASES](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_DATABASES.html): Displays databases from a Data Catalog or an Amazon Redshift data warehouse.
- [SHOW FUNCTIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_FUNCTIONS.html): Shows a list of functions in a schema, along with information about the listed objects.
- [SHOW GRANTS](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_GRANTS.html): Displays grants for a user, role, or object.
- [SHOW MODEL](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_MODEL.html): Shows useful information about a machine learning model.
- [SHOW DATASHARES](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_DATASHARES.html): Displays the inbound and outbound shares in a cluster either from the same account.
- [SHOW PARAMETERS](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_PARAMETERS.html): Shows a list of parameters for a function/procedure, along with some information about the parameters.
- [SHOW POLICIES](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_POLICIES.html): Displays the row-level security (RLS) and dynamic data masking (DDM) policies defined in a database, as well as the RLS and DDM policies applied to specific relations.
- [SHOW PROCEDURE](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_PROCEDURE.html): Shows the definition of a given stored procedure, including its signature.
- [SHOW PROCEDURES](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_PROCEDURES.html): Shows a list of procedures in a schema, along with information about the listed objects.
- [SHOW SCHEMAS](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_SCHEMAS.html): Shows the schemas contained in a database.
- [SHOW TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_TABLE.html): Shows the definition of the table.
- [SHOW TABLES](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_TABLES.html): Shows the tables contained in a schema.
- [SHOW TEMPLATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_TEMPLATE.html): Shows the definition of the template.
- [SHOW TEMPLATES](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_TEMPLATES.html): Shows the templates contained in a schema.
- [SHOW VIEW](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_VIEW.html): Shows the definition of the view.
- [START TRANSACTION](https://docs.aws.amazon.com/redshift/latest/dg/r_START_TRANSACTION.html): Starts a transaction.
- [TRUNCATE](https://docs.aws.amazon.com/redshift/latest/dg/r_TRUNCATE.html): Deletes all of the rows from a table without doing a table scan.

### [UNLOAD](https://docs.aws.amazon.com/redshift/latest/dg/r_UNLOAD.html)

Unloads the result of a query to one or more files on Amazon Simple Storage Service(Amazon S3).

- [UNLOAD examples](https://docs.aws.amazon.com/redshift/latest/dg/r_UNLOAD_command_examples.html): Provides examples of how to use the UNLOAD command.

### [UPDATE](https://docs.aws.amazon.com/redshift/latest/dg/r_UPDATE.html)

Updates values in one or more table columns when a condition is satisfied.

- [Examples of UPDATE statements](https://docs.aws.amazon.com/redshift/latest/dg/c_Examples_of_UPDATE_statements.html): Provides examples of how to use the UPDATE command.
- [USE](https://docs.aws.amazon.com/redshift/latest/dg/r_USE_command.html): Changes the database on which queries run.
- [VACUUM](https://docs.aws.amazon.com/redshift/latest/dg/r_VACUUM_command.html): Re-sorts rows and reclaims space in either a specified table or all tables in the current database.

### [SQL functions reference](https://docs.aws.amazon.com/redshift/latest/dg/c_SQL_functions.html)

Work with the standard SQL functions and extensions to the SQL standards that Amazon Redshift supports.

- [Leader nodeâonly functions](https://docs.aws.amazon.com/redshift/latest/dg/c_SQL_functions_leader_node_only.html): Work with the leader-node only functions for SQL that Amazon Redshift supports.

### [Aggregate functions](https://docs.aws.amazon.com/redshift/latest/dg/c_Aggregate_Functions.html)

Work with the aggregate functions for SQL that Amazon Redshift supports.

- [ANY_VALUE](https://docs.aws.amazon.com/redshift/latest/dg/r_ANY_VALUE.html): Returns any value from the input expression values nondeterministically.
- [APPROXIMATE PERCENTILE_DISC](https://docs.aws.amazon.com/redshift/latest/dg/r_APPROXIMATE_PERCENTILE_DISC.html): An inverse distribution function that assumes a continuous distribution model.
- [AVG](https://docs.aws.amazon.com/redshift/latest/dg/r_AVG.html): Returns the average (arithmetic mean) of the input expression values.
- [COUNT](https://docs.aws.amazon.com/redshift/latest/dg/r_COUNT.html): Counts the rows defined by the expression.
- [LISTAGG](https://docs.aws.amazon.com/redshift/latest/dg/r_LISTAGG.html): For each group in a query, the LISTAGG aggregate function orders the rows for that group according to the ORDER BY expression, then concatenates the values into a single string.
- [MAX](https://docs.aws.amazon.com/redshift/latest/dg/r_MAX.html): Returns the maximum value in a set of rows.
- [MEDIAN](https://docs.aws.amazon.com/redshift/latest/dg/r_MEDIAN.html): Calculates the median value for the range of values.
- [MIN](https://docs.aws.amazon.com/redshift/latest/dg/r_MIN.html): Returns the minimum value in a set of rows.
- [PERCENTILE_CONT](https://docs.aws.amazon.com/redshift/latest/dg/r_PERCENTILE_CONT.html): An inverse distribution function that assumes a continuous distribution model.
- [STDDEV_SAMP and STDDEV_POP](https://docs.aws.amazon.com/redshift/latest/dg/r_STDDEV_functions.html): Returns the sample and population standard deviation of a set of numeric values (integer, decimal, or floating-point).
- [SUM](https://docs.aws.amazon.com/redshift/latest/dg/r_SUM.html): Returns the sum of the input column or expression values.
- [VAR_SAMP and VAR_POP](https://docs.aws.amazon.com/redshift/latest/dg/r_VARIANCE_functions.html): Returns the sample and population variance of a set of numeric values (integer, decimal, or floating-point).

### [Array functions](https://docs.aws.amazon.com/redshift/latest/dg/c_Array_Functions.html)

Work with the array functions for SQL that Amazon Redshift supports to access and manipulate arrays.

- [ARRAY](https://docs.aws.amazon.com/redshift/latest/dg/r_array.html): Creates an array of the SUPER data type.
- [ARRAY_CONCAT](https://docs.aws.amazon.com/redshift/latest/dg/r_array_concat.html): Concatenates two arrays.
- [ARRAY_CONTAINS](https://docs.aws.amazon.com/redshift/latest/dg/array_contains.html): Checks if the array contains the given value and returns TRUE if found.
- [ARRAY_DISTINCT](https://docs.aws.amazon.com/redshift/latest/dg/array_distinct.html): Creates a new array containing only unique elements from the input array, removing all duplicates.
- [ARRAY_EXCEPT](https://docs.aws.amazon.com/redshift/latest/dg/array_except.html): Returns the difference between two arrays - keeping elements from the first array that don't exist in the second array.
- [ARRAY_FLATTEN](https://docs.aws.amazon.com/redshift/latest/dg/array_flatten.html): Merges multiple arrays into a single array of SUPER type.
- [ARRAY_INTERSECTION](https://docs.aws.amazon.com/redshift/latest/dg/array_intersection.html): Returns a new array containing only the elements that exist in both input arrays.
- [ARRAY_POSITION](https://docs.aws.amazon.com/redshift/latest/dg/array_position.html): Returns the position (index) of the first occurrence of a specified element in an array.
- [ARRAY_POSITIONS](https://docs.aws.amazon.com/redshift/latest/dg/array_positions.html): Returns an array of positions (indices) where the specified element appears in the input array.
- [ARRAY_SORT](https://docs.aws.amazon.com/redshift/latest/dg/array_sort.html): Creates a sorted version of the input array in either ascending or descending order.
- [ARRAY_UNION](https://docs.aws.amazon.com/redshift/latest/dg/array_union.html): .
- [ARRAYS_OVERLAP](https://docs.aws.amazon.com/redshift/latest/dg/arrays_overlap.html): Checks whether two arrays have any common elements.
- [GET_ARRAY_LENGTH](https://docs.aws.amazon.com/redshift/latest/dg/get_array_length.html): Returns the length of the specified array.
- [SPLIT_TO_ARRAY](https://docs.aws.amazon.com/redshift/latest/dg/split_to_array.html): Uses a delimiter as an optional parameter.
- [SUBARRAY](https://docs.aws.amazon.com/redshift/latest/dg/r_subarray.html): Extracts a portion of an array starting from a specified position.

### [Bit-wise aggregate functions](https://docs.aws.amazon.com/redshift/latest/dg/c_bitwise_aggregate_functions.html)

Learn about the bit-wise aggregate functions for SQL that Amazon Redshift supports.

- [BIT_AND](https://docs.aws.amazon.com/redshift/latest/dg/r_BIT_AND.html): Work with the syntax and arguments used in the BIT_AND function for Amazon Redshift.
- [BIT_OR](https://docs.aws.amazon.com/redshift/latest/dg/r_BIT_OR.html): Work with the syntax and arguments used in the BIT_OR function for Amazon Redshift.
- [BOOL_AND](https://docs.aws.amazon.com/redshift/latest/dg/r_BOOL_AND.html): Work with the syntax and arguments used in the BOOL_AND function for Amazon Redshift.
- [BOOL_OR](https://docs.aws.amazon.com/redshift/latest/dg/r_BOOL_OR.html): Work with the syntax and arguments used in the BOOL_OR function for Amazon Redshift.

### [Conditional expressions](https://docs.aws.amazon.com/redshift/latest/dg/c_conditional_expressions.html)

Work with the conditional expressions that are extensions to the SQL standard that Amazon Redshift supports.

- [CASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CASE_function.html): Specifies a result when there are multiple conditions.
- [DECODE](https://docs.aws.amazon.com/redshift/latest/dg/r_DECODE_expression.html): Replaces a specific value with either another specific value or a default value, depending on the result of an equality condition.
- [GREATEST and LEAST](https://docs.aws.amazon.com/redshift/latest/dg/r_GREATEST_LEAST.html): Returns the largest or smallest value from a list of expressions.
- [NVL and COALESCE](https://docs.aws.amazon.com/redshift/latest/dg/r_NVL_function.html): Returns the value of the first expression that isn't null in a series of expressions.
- [NVL2](https://docs.aws.amazon.com/redshift/latest/dg/r_NVL2.html): Returns one of two values based on whether a specified expression evaluates to NULL or NOT NULL.
- [NULLIF](https://docs.aws.amazon.com/redshift/latest/dg/r_NULLIF_function.html): Compares two arguments and returns null if the arguments are equal.

### [Data type formatting functions](https://docs.aws.amazon.com/redshift/latest/dg/r_Data_type_formatting.html)

Work with the data type formatting functions for SQL that Amazon Redshift supports.

- [CAST](https://docs.aws.amazon.com/redshift/latest/dg/r_CAST_function.html): Perform runtime conversions between compatible data types by using the CAST function.
- [CONVERT](https://docs.aws.amazon.com/redshift/latest/dg/r_CONVERT_function.html): Perform runtime conversions between compatible data types by using the CONVERT function.
- [TEXT_TO_INT_ALT](https://docs.aws.amazon.com/redshift/latest/dg/r_TEXT_TO_INT_ALT.html): Learn to perform text-to-integer data type conversions with Teradata-style formatting.
- [TEXT_TO_NUMERIC_ALT](https://docs.aws.amazon.com/redshift/latest/dg/r_TEXT_TO_NUMERIC_ALT.html): Learn to perform Teradata-style cast operations to convert text strings to numeric data types.
- [TO_CHAR](https://docs.aws.amazon.com/redshift/latest/dg/r_TO_CHAR.html): Converts a timestamp or numeric expression to a character-string data format.
- [TO_DATE](https://docs.aws.amazon.com/redshift/latest/dg/r_TO_DATE_function.html): Converts a date represented in a character string to a DATE data type.
- [TO_NUMBER](https://docs.aws.amazon.com/redshift/latest/dg/r_TO_NUMBER.html): Converts a string to a numeric (decimal) value.
- [TRY_CAST](https://docs.aws.amazon.com/redshift/latest/dg/r_TRY_CAST.html): Attempts to cast the expression to the specified type, and returns null if unsuccessful.
- [Datetime format strings](https://docs.aws.amazon.com/redshift/latest/dg/r_FORMAT_strings.html): Provides a reference for datetime format strings.
- [Numeric format strings](https://docs.aws.amazon.com/redshift/latest/dg/r_Numeric_formating.html): Provides a reference for numeric format strings.
- [Teradata-style formatting for numeric data](https://docs.aws.amazon.com/redshift/latest/dg/r_Numeric-format-teradata.html): Learn how to use Teradata-style formatting characters for numeric data.

### [Date and time functions](https://docs.aws.amazon.com/redshift/latest/dg/Date_functions_header.html)

Find descriptions of the date and time scalar functions for SQL that Amazon Redshift supports.

- [+ (Concatenation) operator](https://docs.aws.amazon.com/redshift/latest/dg/r_DATE-CONCATENATE_function.html): Concatenates a DATE to a TIME or TIMETZ on either side of the + symbol and returns a TIMESTAMP or TIMESTAMPTZ.
- [ADD_MONTHS](https://docs.aws.amazon.com/redshift/latest/dg/r_ADD_MONTHS.html): Adds the specified number of months to a date or timestamp value or expression.
- [AT TIME ZONE](https://docs.aws.amazon.com/redshift/latest/dg/r_AT_TIME_ZONE.html): Specifies which time zone to use with a TIMESTAMP or TIMESTAMPTZ expression.
- [CONVERT_TIMEZONE](https://docs.aws.amazon.com/redshift/latest/dg/CONVERT_TIMEZONE.html): Converts a time from one time zone to another.
- [CURRENT_DATE](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_DATE_function.html): CURRENT_DATE returns a date in the current session time zone (UTC by default) in the default format: YYYY-MM-DD.
- [DATE_CMP](https://docs.aws.amazon.com/redshift/latest/dg/r_DATE_CMP.html): Compares two dates and returns 0 if the dates are identical, 1 if date1 is greater, and -1 if date2 is greater.
- [DATE_CMP_TIMESTAMP](https://docs.aws.amazon.com/redshift/latest/dg/r_DATE_CMP_TIMESTAMP.html): Compares a date to a timestamp and returns 0 if the values are identical, 1 if the date is greater and -1 if the timestamp is greater.
- [DATE_CMP_TIMESTAMPTZ](https://docs.aws.amazon.com/redshift/latest/dg/r_DATE_CMP_TIMESTAMPTZ.html): Compares the value of a timestamp to a specified date and returns an integer.
- [DATEADD](https://docs.aws.amazon.com/redshift/latest/dg/r_DATEADD_function.html): Increments a DATE, TIME, TIMETZ, or TIMESTAMP value by a specified interval.
- [DATEDIFF](https://docs.aws.amazon.com/redshift/latest/dg/r_DATEDIFF_function.html): DATEDIFF returns the difference between the date parts of two date or time expressions.
- [DATE_PART](https://docs.aws.amazon.com/redshift/latest/dg/r_DATE_PART_function.html): Extracts date part values from an expression.
- [DATE_PART_YEAR](https://docs.aws.amazon.com/redshift/latest/dg/r_DATE_PART_YEAR.html): Extracts the year from a date.
- [DATE_TRUNC](https://docs.aws.amazon.com/redshift/latest/dg/r_DATE_TRUNC.html): Truncates any timestamp expression or literal based on the time interval that you specify, such as hour, day, or month.
- [EXTRACT](https://docs.aws.amazon.com/redshift/latest/dg/r_EXTRACT_function.html): Returns a date or time part from a TIMESTAMP, TIMESTAMPTZ, TIME, TIMETZ, INTERVAL YEAR TO MONTH, or INTERVAL DAY TO SECOND value.
- [GETDATE](https://docs.aws.amazon.com/redshift/latest/dg/r_GETDATE.html): GETDATE returns the current date and time in the current session time zone (UTC by default).
- [INTERVAL_CMP](https://docs.aws.amazon.com/redshift/latest/dg/r_INTERVAL_CMP.html): Compares two intervals and returns 1 if the first interval is greater, -1 if the second interval is greater, and 0 if the intervals are equal.
- [LAST_DAY](https://docs.aws.amazon.com/redshift/latest/dg/r_LAST_DAY.html): Returns the date of the last day of the month that contains date.
- [MONTHS_BETWEEN](https://docs.aws.amazon.com/redshift/latest/dg/r_MONTHS_BETWEEN_function.html): Determines the number of months between two dates.
- [NEXT_DAY](https://docs.aws.amazon.com/redshift/latest/dg/r_NEXT_DAY.html): NEXT_DAY returns the date of the first instance of the specified day that is later than the given date.
- [SYSDATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SYSDATE.html): Returns the current date and time according to the system clock on the leader node.
- [TIMEOFDAY](https://docs.aws.amazon.com/redshift/latest/dg/r_TIMEOFDAY_function.html): TIMEOFDAY is a special alias used to return the weekday, date, and time as a string value.
- [TIMESTAMP_CMP](https://docs.aws.amazon.com/redshift/latest/dg/r_TIMESTAMP_CMP.html): Compares the value of two timestamps and returns an integer.
- [TIMESTAMP_CMP_DATE](https://docs.aws.amazon.com/redshift/latest/dg/r_TIMESTAMP_CMP_DATE.html): Compares the value of a timestamp to a specified date and returns an integer.
- [TIMESTAMP_CMP_TIMESTAMPTZ](https://docs.aws.amazon.com/redshift/latest/dg/r_TIMESTAMP_CMP_TIMESTAMPTZ.html): Compares the value of a timestamp to a timestamp with time zone and returns an integer.
- [TIMESTAMPTZ_CMP](https://docs.aws.amazon.com/redshift/latest/dg/r_TIMESTAMPTZ_CMP.html): Compares the value of two timestamp with time zone values and returns an integer.
- [TIMESTAMPTZ_CMP_DATE](https://docs.aws.amazon.com/redshift/latest/dg/r_TIMESTAMPTZ_CMP_DATE.html): Compares the value of a timestamp to a specified date and returns an integer.
- [TIMESTAMPTZ_CMP_TIMESTAMP](https://docs.aws.amazon.com/redshift/latest/dg/r_TIMESTAMPTZ_CMP_TIMESTAMP.html): Compares the value of a timestamp to a specified date and returns an integer.
- [TIMEZONE](https://docs.aws.amazon.com/redshift/latest/dg/r_TIMEZONE.html): Specifies which time zone to use with a TIMESTAMP or TIMESTAMPTZ expression.
- [TO_TIMESTAMP](https://docs.aws.amazon.com/redshift/latest/dg/r_TO_TIMESTAMP.html): TO_TIMESTAMP converts a TIMESTAMP string to TIMESTAMPTZ.
- [TRUNC](https://docs.aws.amazon.com/redshift/latest/dg/r_TRUNC_date.html): Truncates a TIMESTAMP and returns a DATE.
- [Date parts for date or timestamp functions](https://docs.aws.amazon.com/redshift/latest/dg/r_Dateparts_for_datetime_functions.html): Find the date part and time part names and abbreviations that are accepted as arguments for date and time functions in Amazon Redshift.

### [Hash functions](https://docs.aws.amazon.com/redshift/latest/dg/hash-functions.html)

Work with the HASH functions for SQL that Amazon Redshift supports.

- [CHECKSUM](https://docs.aws.amazon.com/redshift/latest/dg/r_CHECKSUM.html): Computes a checksum value for building a hash index.
- [farmFingerprint64](https://docs.aws.amazon.com/redshift/latest/dg/r_FARMFINGERPRINT64.html): Computes the farmhash value of the input argument using the Fingerprint64 function.
- [FUNC_SHA1](https://docs.aws.amazon.com/redshift/latest/dg/FUNC_SHA1.html): Synonym of SHA1 function
- [FNV_HASH](https://docs.aws.amazon.com/redshift/latest/dg/r_FNV_HASH.html): Computes the 64-bit FNV-1a non-cryptographic hash function for all basic data types.
- [MD5](https://docs.aws.amazon.com/redshift/latest/dg/r_MD5.html): Uses the MD5 cryptographic hash function to convert a variable-length string into a 32-character string.
- [SHA](https://docs.aws.amazon.com/redshift/latest/dg/SHA.html): Synonym of SHA1 function
- [SHA1](https://docs.aws.amazon.com/redshift/latest/dg/SHA1.html): Uses the SHA1 cryptographic hash function to convert a variable-length string into a 40-character string.
- [SHA2](https://docs.aws.amazon.com/redshift/latest/dg/SHA2.html): The SHA2 function uses the SHA cryptographic hash function to convert a variable-length string into a character string.
- [MURMUR3_32_HASH](https://docs.aws.amazon.com/redshift/latest/dg/MURMUR3_32_HASH.html): The MURMUR3_32_HASH function computes the 32-bit Murmur3A non-cryptographic hash for all common data types including numeric and string types.

### [HyperLogLog functions](https://docs.aws.amazon.com/redshift/latest/dg/hyperloglog-functions.html)

Work with the HyperLogLog functions for SQL that Amazon Redshift supports.

- [HLL](https://docs.aws.amazon.com/redshift/latest/dg/r_HLL_function.html): Work with the HLL function for Amazon Redshift.
- [HLL_CREATE_SKETCH](https://docs.aws.amazon.com/redshift/latest/dg/r_HLL_CREATE_SKETCH.html): Work with the HLL_CREATE_SKETCH function for Amazon Redshift.
- [HLL_CARDINALITY](https://docs.aws.amazon.com/redshift/latest/dg/r_HLL_CARDINALITY.html): Work with the HLL_CARDINALITY function for Amazon Redshift.
- [HLL_COMBINE](https://docs.aws.amazon.com/redshift/latest/dg/r_HLL_COMBINE.html): Work with the HLL_COMBINE aggregate function for Amazon Redshift.
- [HLL_COMBINE_SKETCHES](https://docs.aws.amazon.com/redshift/latest/dg/r_HLL_COMBINE_SKETCHES.html): Work with the HLL_COMBINE_SKETCHES function for Amazon Redshift.

### [JSON functions](https://docs.aws.amazon.com/redshift/latest/dg/json-functions.html)

Work with the JSON functions for SQL that Amazon Redshift supports.

- [JSON_PARSE](https://docs.aws.amazon.com/redshift/latest/dg/JSON_PARSE.html): Parses data in JSON format and converts it into the SUPER representation.
- [CAN_JSON_PARSE](https://docs.aws.amazon.com/redshift/latest/dg/CAN_JSON_PARSE.html): Parses data in JSON format and returns true if the result can be converted to a SUPER value using JSON_PARSE.
- [JSON_SERIALIZE](https://docs.aws.amazon.com/redshift/latest/dg/JSON_SERIALIZE.html): Serializes a SUPER expression into textual JSON representation as per RFC 8259.
- [JSON_SERIALIZE_TO_VARBYTE](https://docs.aws.amazon.com/redshift/latest/dg/JSON_SERIALIZE_TO_VARBYTE.html): Converts a SUPER expression to a JSON string in VARBYTE format.

### [Text-based JSON functions](https://docs.aws.amazon.com/redshift/latest/dg/text-json-functions.html)

JSON functions that operate on text and not the SUPER-data type.

- [IS_VALID_JSON](https://docs.aws.amazon.com/redshift/latest/dg/IS_VALID_JSON.html): Validates a JSON string.
- [IS_VALID_JSON_ARRAY](https://docs.aws.amazon.com/redshift/latest/dg/IS_VALID_JSON_ARRAY.html): Validates a JSON array.
- [JSON_ARRAY_LENGTH](https://docs.aws.amazon.com/redshift/latest/dg/JSON_ARRAY_LENGTH.html): Returns the number of elements in the outer array of a JSON string.
- [JSON_EXTRACT_ARRAY_ELEMENT_TEXT](https://docs.aws.amazon.com/redshift/latest/dg/JSON_EXTRACT_ARRAY_ELEMENT_TEXT.html): Returns a JSON array element in the outermost array of a JSON string, using a zero-based index.
- [JSON_EXTRACT_PATH_TEXT](https://docs.aws.amazon.com/redshift/latest/dg/JSON_EXTRACT_PATH_TEXT.html): Returns the value for the key-value pair referenced by a series of path elements in a JSON string.

### [Machine learning functions](https://docs.aws.amazon.com/redshift/latest/dg/ml-function.html)

Work with the machine learning functions for SQL that Amazon Redshift supports.

- [EXPLAIN_MODEL function](https://docs.aws.amazon.com/redshift/latest/dg/r_explain_model_function.html): Work with the EXPLAIN_MODEL function for Amazon Redshift.

### [Math functions](https://docs.aws.amazon.com/redshift/latest/dg/Math_functions.html)

Work with the mathematical operators and functions for SQL that Amazon Redshift supports.

- [Mathematical operator symbols](https://docs.aws.amazon.com/redshift/latest/dg/r_OPERATOR_SYMBOLS.html): Lists the mathematical operators supported by Amazon Redshift.
- [ABS](https://docs.aws.amazon.com/redshift/latest/dg/r_ABS.html): Calculates the absolute value of a number, where that number can be a literal or an expression that evaluates to a number.
- [ACOS](https://docs.aws.amazon.com/redshift/latest/dg/r_ACOS.html): Returns the arc cosine of a number.
- [ASIN](https://docs.aws.amazon.com/redshift/latest/dg/r_ASIN.html): Returns the arc sine of a number.
- [ATAN](https://docs.aws.amazon.com/redshift/latest/dg/r_ATAN.html): Returns the arc tangent of a number.
- [ATAN2](https://docs.aws.amazon.com/redshift/latest/dg/r_ATAN2.html): Returns the arc tangent of one number divided by another number.
- [CBRT](https://docs.aws.amazon.com/redshift/latest/dg/r_CBRT.html): >Calculates the cube root of a number.
- [CEILING (or CEIL)](https://docs.aws.amazon.com/redshift/latest/dg/r_CEILING_FLOOR.html): Rounds a number up to the next whole number.
- [COS](https://docs.aws.amazon.com/redshift/latest/dg/r_COS.html): Returns the cosine of a number.
- [COT](https://docs.aws.amazon.com/redshift/latest/dg/r_COT.html): Returns the cotangent of a number.
- [DEGREES](https://docs.aws.amazon.com/redshift/latest/dg/r_DEGREES.html): Converts an angle in radians to its equivalent in degrees.
- [DEXP](https://docs.aws.amazon.com/redshift/latest/dg/r_DEXP.html): Returns the exponentialSPLI value in scientific notation for a DOUBLE PRECISION number.
- [DLOG1](https://docs.aws.amazon.com/redshift/latest/dg/r_DLOG1.html): Returns the natural logarithm of the input parameter.
- [DLOG10](https://docs.aws.amazon.com/redshift/latest/dg/r_DLOG10.html): Returns the base 10 logarithm of the input parameter of the LOG function.
- [EXP](https://docs.aws.amazon.com/redshift/latest/dg/r_EXP.html): Returns the exponential value in DOUBLE PRECISION for a numeric expression.
- [FLOOR](https://docs.aws.amazon.com/redshift/latest/dg/r_FLOOR.html): Rounds a number down to the next whole number.
- [LN](https://docs.aws.amazon.com/redshift/latest/dg/r_LN.html): Returns the natural logarithm of the input parameter.
- [LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_LOG.html): Returns the logarithm of a number.
- [MOD](https://docs.aws.amazon.com/redshift/latest/dg/r_MOD.html): Returns the remainder after a number is divided by another.
- [PI](https://docs.aws.amazon.com/redshift/latest/dg/r_PI.html): Returns the value of pi to 14 decimal places.
- [POWER](https://docs.aws.amazon.com/redshift/latest/dg/r_POWER.html): Raises a numeric expression to the power of a second numeric expression.
- [RADIANS](https://docs.aws.amazon.com/redshift/latest/dg/r_RADIANS.html): Converts an angle in degrees to its equivalent in radians.
- [RANDOM](https://docs.aws.amazon.com/redshift/latest/dg/r_RANDOM.html): Generates a random value greater than or equal to 0.0 and less than 1.0.
- [ROUND](https://docs.aws.amazon.com/redshift/latest/dg/r_ROUND.html): Rounds numbers to the nearest integer or decimal.
- [SIN](https://docs.aws.amazon.com/redshift/latest/dg/r_SIN.html): Returns the sine of a number.
- [SIGN](https://docs.aws.amazon.com/redshift/latest/dg/r_SIGN.html): Returns the sign (positive or negative) of a number.
- [SQRT](https://docs.aws.amazon.com/redshift/latest/dg/r_SQRT.html): Returns the square root of a numeric value.
- [TAN](https://docs.aws.amazon.com/redshift/latest/dg/r_TAN.html): Returns the tangent of a number.
- [TRUNC](https://docs.aws.amazon.com/redshift/latest/dg/r_TRUNC.html): Truncates a number and right-fills it with zeros from the position specified.

### [Object functions](https://docs.aws.amazon.com/redshift/latest/dg/Object_Functions.html)

Use Amazon Redshift to create user-defined SUPER type objects composed of key-value pairs.

- [GET_NUMBER_ATTRIBUTES](https://docs.aws.amazon.com/redshift/latest/dg/get_number_attributes.html): Returns a count of how many key-value pairs exist at the root level of a dictionary object.
- [LOWER_ATTRIBUTE_NAMES](https://docs.aws.amazon.com/redshift/latest/dg/r_lower_attribute_names.html): Converts all attribute names in a SUPER value to lowercase.
- [OBJECT](https://docs.aws.amazon.com/redshift/latest/dg/r_object_function.html): Creates an object of the SUPER data type.
- [OBJECT_TRANSFORM](https://docs.aws.amazon.com/redshift/latest/dg/r_object_transform_function.html): Transforms a SUPER object.
- [UPPER_ATTRIBUTE_NAMES](https://docs.aws.amazon.com/redshift/latest/dg/r_upper_attribute_names.html): Converts all attribute names in a SUPER value to uppercase.

### [Spatial functions](https://docs.aws.amazon.com/redshift/latest/dg/geospatial-functions.html)

Describes the spatial functions in Amazon Redshift.

- [AddBBox](https://docs.aws.amazon.com/redshift/latest/dg/AddBBox-function.html): AddBBox returns a copy of the input geometry that supports encoding with a precomputed bounding box.
- [DropBBox](https://docs.aws.amazon.com/redshift/latest/dg/DropBBox-function.html): DropBBox returns a copy of the input geometry that doesn't support encoding with a precomputed bounding box.
- [GeometryType](https://docs.aws.amazon.com/redshift/latest/dg/GeometryType-function.html): GeometryType returns the subtype of an input geometry as a string.
- [H3_Boundary](https://docs.aws.amazon.com/redshift/latest/dg/H3_Boundary-function.html): H3_Boundary returns the boundary of an H3 cell ID from an input index.
- [H3_Center](https://docs.aws.amazon.com/redshift/latest/dg/H3_Center-function.html): H3_Center returns the centroid of an H3 cell ID from an input index.
- [H3_FromLongLat](https://docs.aws.amazon.com/redshift/latest/dg/H3_FromLongLat-function.html): H3_FromLongLat returns the corresponding H3 cell ID from an input longitude, latitude, and resolution.
- [H3_FromPoint](https://docs.aws.amazon.com/redshift/latest/dg/H3_FromPoint-function.html): H3_FromPoint returns the corresponding H3 cell ID from an input geometry point and resolution.
- [H3_IsValid](https://docs.aws.amazon.com/redshift/latest/dg/H3_IsValid-function.html): H3_IsValid returns true if the input represents an H3 cell ID, otherwise false.
- [H3_Polyfill](https://docs.aws.amazon.com/redshift/latest/dg/H3_Polyfill-function.html): H3_Polyfill returns the corresponding H3 cell IDs that correspond to the hexagons and pentagons that are contained in the input polygon of the given resolution.
- [H3_Resolution](https://docs.aws.amazon.com/redshift/latest/dg/H3_Resolution-function.html): H3_Resolution returns the resolution of an H3 cell ID from an input index.
- [H3_ToChildren](https://docs.aws.amazon.com/redshift/latest/dg/H3_ToChildren-function.html): H3_ToChildren returns a list of child H3 cell IDs at a specified resolution for a given H3 index.
- [H3_ToParent](https://docs.aws.amazon.com/redshift/latest/dg/H3_ToParent-function.html): H3_ToParent returns the parent H3 cell ID at a specified parent resolution for a given H3 index.
- [ST_AddPoint](https://docs.aws.amazon.com/redshift/latest/dg/ST_AddPoint-function.html): ST_AddPoint returns a linestring geometry that is the input geometry with a point added.
- [ST_Angle](https://docs.aws.amazon.com/redshift/latest/dg/ST_Angle-function.html): ST_Angle returns the angle in radians between points measured clockwise.
- [ST_Area](https://docs.aws.amazon.com/redshift/latest/dg/ST_Area-function.html): For an input geometry, ST_Area returns the Cartesian area of the 2D projection.
- [ST_AsBinary](https://docs.aws.amazon.com/redshift/latest/dg/ST_AsBinary-function.html): ST_AsBinary returns the hexadecimal well-known binary (WKB) representation of an input geometry.
- [ST_AsEWKB](https://docs.aws.amazon.com/redshift/latest/dg/ST_AsEWKB-function.html): ST_AsEWKB returns the extended well-known binary (EWKB) representation of an input geometry.
- [ST_AsEWKT](https://docs.aws.amazon.com/redshift/latest/dg/ST_AsEWKT-function.html): ST_AsEWKT returns the extended well-known text (EWKT) representation of an input geometry or geography.
- [ST_AsGeoJSON](https://docs.aws.amazon.com/redshift/latest/dg/ST_AsGeoJSON-function.html): ST_AsGeoJSON returns the GeoJSON representation of an input geometry or geography.
- [ST_AsHexWKB](https://docs.aws.amazon.com/redshift/latest/dg/ST_AsHexWKB-function.html): ST_AsHexWKB returns the hexadecimal well-known binary (WKB) representation of an input geometry or geography using ASCII hexadecimal characters (0â9, AâF).
- [ST_AsHexEWKB](https://docs.aws.amazon.com/redshift/latest/dg/ST_AsHexEWKB-function.html): ST_AsHexEWKB returns the extended well-known binary (EWKB) representation of an input geometry or geography using ASCII hexadecimal characters (0â9, AâF).
- [ST_AsText](https://docs.aws.amazon.com/redshift/latest/dg/ST_AsText-function.html): ST_AsText returns the well-known text (WKT) representation of an input geometry or geography.
- [ST_Azimuth](https://docs.aws.amazon.com/redshift/latest/dg/ST_Azimuth-function.html): ST_Azimuth returns the north-based Cartesian azimuth using the 2D projections of the two input points.
- [ST_Boundary](https://docs.aws.amazon.com/redshift/latest/dg/ST_Boundary-function.html): ST_Boundary returns the boundary of an input geometry.
- [ST_Buffer](https://docs.aws.amazon.com/redshift/latest/dg/ST_Buffer-function.html): ST_Buffer returns the boundary of an input geometry.
- [ST_Centroid](https://docs.aws.amazon.com/redshift/latest/dg/ST_Centroid-function.html): ST_Centroid returns a point that represents a centroid of a geometry.
- [ST_Collect](https://docs.aws.amazon.com/redshift/latest/dg/ST_Collect-function.html): ST_Collect creates a geometry collection from the input geometries or geometries from a geometry column.
- [ST_Contains](https://docs.aws.amazon.com/redshift/latest/dg/ST_Contains-function.html): ST_Contains returns true if the 2D projection of the first input geometry contains the 2D projection of the second input geometry.
- [ST_ContainsProperly](https://docs.aws.amazon.com/redshift/latest/dg/ST_ContainsProperly-function.html): SST_ContainsProperly returns true if both input geometries are nonempty, and all points of the 2D projection of the second geometry are interior points of the 2D projection of the first geometry.
- [ST_ConvexHull](https://docs.aws.amazon.com/redshift/latest/dg/ST_ConvexHull-function.html): ST_ConvexHull returns a geometry that represents the convex hull of the nonempty points contained in the input geometry.
- [ST_CoveredBy](https://docs.aws.amazon.com/redshift/latest/dg/ST_CoveredBy-function.html): ST_CoveredBy returns true if the 2D projection of the first input geometry is covered by the 2D projection of the second input geometry.
- [ST_Covers](https://docs.aws.amazon.com/redshift/latest/dg/ST_Covers-function.html): ST_Covers returns true if the 2D projection of the first input geometry covers the 2D projection of the second input geometry.
- [ST_Crosses](https://docs.aws.amazon.com/redshift/latest/dg/ST_Crosses-function.html): ST_Crosses returns true if the 2D projections of the two input geometries cross each other.
- [ST_Dimension](https://docs.aws.amazon.com/redshift/latest/dg/ST_Dimension-function.html): ST_Dimension returns the inherent dimension of an input geometry.
- [ST_Disjoint](https://docs.aws.amazon.com/redshift/latest/dg/ST_Disjoint-function.html): ST_Disjoint returns true if the 2D projections of the two input geometries have no points in common.
- [ST_Distance](https://docs.aws.amazon.com/redshift/latest/dg/ST_Distance-function.html): For input geometries, ST_Distance returns the minimum Euclidean distance between the 2D projections of the two input geometry values.
- [ST_DistanceSphere](https://docs.aws.amazon.com/redshift/latest/dg/ST_DistanceSphere-function.html): ST_DistanceSphere returns the distance between two point geometries lying on a sphere.
- [ST_DWithin](https://docs.aws.amazon.com/redshift/latest/dg/ST_DWithin-function.html): ST_DWithin returns true if the Euclidean distance between the 2D projections of the two input geometry values is not larger than a threshold value.
- [ST_EndPoint](https://docs.aws.amazon.com/redshift/latest/dg/ST_EndPoint-function.html): ST_EndPoint returns the last point of an input linestring.
- [ST_Envelope](https://docs.aws.amazon.com/redshift/latest/dg/ST_Envelope-function.html): ST_Envelope returns the minimum bounding box of the input geometry.
- [ST_Equals](https://docs.aws.amazon.com/redshift/latest/dg/ST_Equals-function.html): ST_Equals returns true if the 2D projections of the input geometries are geometrically equal.
- [ST_ExteriorRing](https://docs.aws.amazon.com/redshift/latest/dg/ST_ExteriorRing-function.html): ST_ExteriorRing returns a closed linestring that represents the exterior ring of an input polygon.
- [ST_Force2D](https://docs.aws.amazon.com/redshift/latest/dg/ST_Force2D-function.html): ST_Force2D returns a 2D geometry of the input geometry.
- [ST_Force3D](https://docs.aws.amazon.com/redshift/latest/dg/ST_Force3D-function.html): ST_Force3D is an alias of ST_Force3DZ.
- [ST_Force3DM](https://docs.aws.amazon.com/redshift/latest/dg/ST_Force3DM-function.html): ST_Force3DM returns a 3DM geometry of the input geometry.
- [ST_Force3DZ](https://docs.aws.amazon.com/redshift/latest/dg/ST_Force3DZ-function.html): ST_Force3DZ returns a 3DZ geometry of the input geometry.
- [ST_Force4D](https://docs.aws.amazon.com/redshift/latest/dg/ST_Force4D-function.html): ST_Force4D returns a 4D geometry of the input geometry.
- [ST_GeoHash](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeoHash-function.html): ST_GeoHash returns the geohash representation of the input point with the specified precision.
- [ST_GeogFromText](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeogFromText-function.html): ST_GeogFromText constructs a geography object from a well-known text (WKT) or extended well-known text (EWKT) representation of an input geography.
- [ST_GeogFromWKB](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeogFromWKB-function.html): ST_GeogFromWKB constructs a geography object from a hexadecimal well-known binary (WKB) representation of an input geography.
- [ST_GeometryN](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeometryN-function.html): ST_GeometryN returns a geometry pointed to by the input index of the input geometry.
- [ST_GeometryType](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeometryType-function.html): ST_GeometryType returns the subtype of an input geometry as a string.
- [ST_GeomFromEWKB](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeomFromEWKB-function.html): ST_GeomFromEWKB constructs a geometry object from the extended well-known binary (EWKB) representation of an input geometry.
- [ST_GeomFromEWKT](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeomFromEWKT-function.html): ST_GeomFromEWKT constructs a geometry object from the extended well-known text (EWKT) representation of an input geometry.
- [ST_GeomFromGeoHash](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeomFromGeoHash-function.html): ST_GeomFromGeoHash constructs a geometry object from the geohash representation of an input geometry.
- [ST_GeomFromGeoJSON](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeomFromGeoJSON-function.html): ST_GeomFromGeoJSON constructs a geometry object from the GeoJSON representation of an input geometry.
- [ST_GeomFromGeoSquare](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeomFromGeoSquare-function.html): ST_GeomFromGeoSquare returns a geometry that covers the area that is represented by an input geosquare value.
- [ST_GeomFromText](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeomFromText-function.html): ST_GeomFromText constructs a geometry object from a well-known text (WKT) representation of an input geometry.
- [ST_GeomFromWKB](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeomFromWKB-function.html): ST_GeomFromWKB constructs a geometry object from a hexadecimal well-known binary (WKB) representation of an input geometry.
- [ST_GeoSquare](https://docs.aws.amazon.com/redshift/latest/dg/ST_GeoSquare-function.html): ST_GeoSquare recursively subdivides the domain ([-180, 180], [-90, 90]) into equal square regions called geosquares.
- [ST_InteriorRingN](https://docs.aws.amazon.com/redshift/latest/dg/ST_InteriorRingN-function.html): ST_InteriorRingN returns a closed linestring corresponding to the interior ring of an input polygon at the index position.
- [ST_Intersects](https://docs.aws.amazon.com/redshift/latest/dg/ST_Intersects-function.html): ST_Intersects returns true if the 2D projections of the two input geometries have at least one point in common.
- [ST_Intersection](https://docs.aws.amazon.com/redshift/latest/dg/ST_Intersection-function.html): ST_Intersection returns a geometry representing the point-set intersection of two geometries.
- [ST_IsPolygonCCW](https://docs.aws.amazon.com/redshift/latest/dg/ST_IsPolygonCCW-function.html): ST_IsPolygonCCW returns true if the 2D projection of the input polygon or multipolygon is counterclockwise.
- [ST_IsPolygonCW](https://docs.aws.amazon.com/redshift/latest/dg/ST_IsPolygonCW-function.html): ST_IsPolygonCW returns true if the 2D projection of the input polygon or multipolygon is clockwise.
- [ST_IsClosed](https://docs.aws.amazon.com/redshift/latest/dg/ST_IsClosed-function.html): ST_IsClosed returns true if the 2D projection of the input geometry is closed.
- [ST_IsCollection](https://docs.aws.amazon.com/redshift/latest/dg/ST_IsCollection-function.html): ST_IsCollection returns true if the input geometry is one of the following subtypes: GEOMETRYCOLLECTION, MULTIPOINT, MULTILINESTRING, or MULTIPOLYGON.
- [ST_IsEmpty](https://docs.aws.amazon.com/redshift/latest/dg/ST_IsEmpty-function.html): ST_IsEmpty returns true if the input geometry is empty.
- [ST_IsRing](https://docs.aws.amazon.com/redshift/latest/dg/ST_IsRing-function.html): ST_IsRing returns true if the input linestring is a ring.
- [ST_IsSimple](https://docs.aws.amazon.com/redshift/latest/dg/ST_IsSimple-function.html): ST_IsSimple returns true if the 2D projection of the input geometry is simple.
- [ST_IsValid](https://docs.aws.amazon.com/redshift/latest/dg/ST_IsValid-function.html): ST_IsValid returns true if the 2D projection of the input geometry is valid.
- [ST_Length](https://docs.aws.amazon.com/redshift/latest/dg/ST_Length-function.html): For a linear geometry, ST_Length returns the Cartesian length of a 2D projection.
- [ST_LengthSphere](https://docs.aws.amazon.com/redshift/latest/dg/ST_LengthSphere-function.html): ST_LengthSphere returns the length of a linear geometry in meters.
- [ST_Length2D](https://docs.aws.amazon.com/redshift/latest/dg/ST_Length2D-function.html): ST_Length2D is an alias of ST_Length.
- [ST_LineFromMultiPoint](https://docs.aws.amazon.com/redshift/latest/dg/ST_LineFromMultiPoint-function.html): ST_LineFromMultiPoint returns a linestring from a multipoint geometry.
- [ST_LineInterpolatePoint](https://docs.aws.amazon.com/redshift/latest/dg/ST_LineInterpolatePoint-function.html): ST_LineInterpolatePoint returns a point along a line at a fractional distance from the start of the line.
- [ST_M](https://docs.aws.amazon.com/redshift/latest/dg/ST_M-function.html): ST_M returns the m coordinate of an input point.
- [ST_MakeEnvelope](https://docs.aws.amazon.com/redshift/latest/dg/ST_MakeEnvelope-function.html): ST_MakeEnvelope returns a geometry.
- [ST_MakeLine](https://docs.aws.amazon.com/redshift/latest/dg/ST_MakeLine-function.html): ST_MakeLine creates a linestring from the input geometries.
- [ST_MakePoint](https://docs.aws.amazon.com/redshift/latest/dg/ST_MakePoint-function.html): ST_MakePoint returns a point geometry whose coordinate values are the input values.
- [ST_MakePolygon](https://docs.aws.amazon.com/redshift/latest/dg/ST_MakePolygon-function.html): ST_MakePolygon returns a polygon geometry whose outer ring is the input linestring or two input geometries.
- [ST_MemSize](https://docs.aws.amazon.com/redshift/latest/dg/ST_MemSize-function.html): ST_MemSize returns the amount of memory space (in bytes) used by the input geometry.
- [ST_MMax](https://docs.aws.amazon.com/redshift/latest/dg/ST_MMax-function.html): ST_MMax returns the maximum m coordinate of an input geometry.
- [ST_MMin](https://docs.aws.amazon.com/redshift/latest/dg/ST_MMin-function.html): ST_MMin returns the minimum m coordinate of an input geometry.
- [ST_Multi](https://docs.aws.amazon.com/redshift/latest/dg/ST_Multi-function.html): ST_Multi converts a geometry to the corresponding multi-type.
- [ST_NDims](https://docs.aws.amazon.com/redshift/latest/dg/ST_NDims-function.html): ST_NDims returns the coordinate dimension of a geometry.
- [ST_NPoints](https://docs.aws.amazon.com/redshift/latest/dg/ST_NPoints-function.html): ST_NPoints returns the number of nonempty points in an input geometry or geography.
- [ST_NRings](https://docs.aws.amazon.com/redshift/latest/dg/ST_NRings-function.html): ST_NRings returns the number of rings in an input geometry.
- [ST_NumGeometries](https://docs.aws.amazon.com/redshift/latest/dg/ST_NumGeometries-function.html): ST_NumGeometries returns the number of geometries in an input geometry.
- [ST_NumInteriorRings](https://docs.aws.amazon.com/redshift/latest/dg/ST_NumInteriorRings-function.html): ST_NumInteriorRings returns the number of rings in an input polygon geometry.
- [ST_NumPoints](https://docs.aws.amazon.com/redshift/latest/dg/ST_NumPoints-function.html): ST_NumPoints returns the number of points in an input geometry.
- [ST_Perimeter](https://docs.aws.amazon.com/redshift/latest/dg/ST_Perimeter-function.html): For an input areal geometry, ST_Perimeter returns the Cartesian perimeter (length of the boundary) of the 2D projection.
- [ST_Perimeter2D](https://docs.aws.amazon.com/redshift/latest/dg/ST_Perimeter2D-function.html): ST_Perimeter2D is an alias of ST_Perimeter.
- [ST_Point](https://docs.aws.amazon.com/redshift/latest/dg/ST_Point-function.html): ST_Point returns a point geometry from the input coordinate values.
- [ST_PointN](https://docs.aws.amazon.com/redshift/latest/dg/ST_PointN-function.html): ST_PointN returns a point in a linestring as specified by an index value.
- [ST_Points](https://docs.aws.amazon.com/redshift/latest/dg/ST_Points-function.html): ST_Points returns a multipoint geometry containing all nonempty points in the input geometry.
- [ST_Polygon](https://docs.aws.amazon.com/redshift/latest/dg/ST_Polygon-function.html): ST_Polygon returns a polygon geometry whose outer ring is the input linestring with the value that was input for the spatial reference system identifier (SRID).
- [ST_RemovePoint](https://docs.aws.amazon.com/redshift/latest/dg/ST_RemovePoint-function.html): ST_RemovePoint returns a linestring geometry that has the point of the input geometry at an index position removed.
- [ST_Reverse](https://docs.aws.amazon.com/redshift/latest/dg/ST_Reverse-function.html): ST_Reverse reverses the order of the vertices for linear and areal geometries.
- [ST_SetPoint](https://docs.aws.amazon.com/redshift/latest/dg/ST_SetPoint-function.html): ST_SetPoint takes as input a linestring, an index, and a point.
- [ST_SetSRID](https://docs.aws.amazon.com/redshift/latest/dg/ST_SetSRID-function.html): ST_SetSRID returns a geometry that is the same as input geometry, except updated with the value input for the spatial reference system identifier (SRID).
- [ST_Simplify](https://docs.aws.amazon.com/redshift/latest/dg/ST_Simplify-function.html): ST_Simplify returns a simplified copy of the input geometry using the Ramer-Douglas-Peucker algorithm with the given tolerance.
- [ST_SRID](https://docs.aws.amazon.com/redshift/latest/dg/ST_SRID-function.html): ST_SRID returns the spatial reference system identifier (SRID) of an input geometry.
- [ST_StartPoint](https://docs.aws.amazon.com/redshift/latest/dg/ST_StartPoint-function.html): ST_StartPoint returns the first point of an input linestring.
- [ST_Touches](https://docs.aws.amazon.com/redshift/latest/dg/ST_Touches-function.html): ST_Touches returns true if the 2D projections of the two input geometries touch.
- [ST_Transform](https://docs.aws.amazon.com/redshift/latest/dg/ST_Transform-function.html): ST_Transform returns a new geometry with coordinates that are transformed in a spatial reference system defined by the input spatial reference system identifier (SRID).
- [ST_Union](https://docs.aws.amazon.com/redshift/latest/dg/ST_Union-function.html): ST_Union returns a geometry representing the union of two geometries.
- [ST_Within](https://docs.aws.amazon.com/redshift/latest/dg/ST_Within-function.html): ST_Within returns true if the 2D projection of the first input geometry is within the 2D projection of the second input geometry.
- [ST_X](https://docs.aws.amazon.com/redshift/latest/dg/ST_X-function.html): ST_X returns the first coordinate of an input point.
- [ST_XMax](https://docs.aws.amazon.com/redshift/latest/dg/ST_XMax-function.html): ST_XMax returns the maximum first coordinate of an input geometry.
- [ST_XMin](https://docs.aws.amazon.com/redshift/latest/dg/ST_XMin-function.html): ST_XMin returns the minimum first coordinate of an input geometry.
- [ST_Y](https://docs.aws.amazon.com/redshift/latest/dg/ST_Y-function.html): ST_Y returns the second coordinate of an input point.
- [ST_YMax](https://docs.aws.amazon.com/redshift/latest/dg/ST_YMax-function.html): ST_YMax returns the maximum second coordinate of an input geometry.
- [ST_YMin](https://docs.aws.amazon.com/redshift/latest/dg/ST_YMin-function.html): ST_YMin returns the minimum second coordinate of an input geometry.
- [ST_Z](https://docs.aws.amazon.com/redshift/latest/dg/ST_Z-function.html): ST_Z returns the z coordinate of an input point.
- [ST_ZMax](https://docs.aws.amazon.com/redshift/latest/dg/ST_ZMax-function.html): ST_ZMax returns the maximum z coordinate of an input geometry.
- [ST_ZMin](https://docs.aws.amazon.com/redshift/latest/dg/ST_ZMin-function.html): ST_ZMin returns the minimum z coordinate of an input geometry.
- [SupportsBBox](https://docs.aws.amazon.com/redshift/latest/dg/SupportsBBox-function.html): SupportsBBox returns true if the input geometry supports encoding with a precomputed bounding box.

### [String functions](https://docs.aws.amazon.com/redshift/latest/dg/String_functions_header.html)

Work with the string functions that process and manipulate character strings or expressions that evaluate to character strings.

- [|| (Concatenation) Operator](https://docs.aws.amazon.com/redshift/latest/dg/r_concat_op.html): Concatenates two expressions on either side of the || symbol and returns the concatenated expression.
- [ASCII](https://docs.aws.amazon.com/redshift/latest/dg/r_ASCII.html): Returns the ASCII code, or the Unicode code-point, of the first character in the string that you specify.
- [BPCHARCMP](https://docs.aws.amazon.com/redshift/latest/dg/r_BPCHARCMP.html): Compares the value of two strings and returns an integer.
- [BTRIM](https://docs.aws.amazon.com/redshift/latest/dg/r_BTRIM.html): Trims a string by removing leading and trailing blanks or by removing leading and trailing characters that match an optional specified string.
- [BTTEXT_PATTERN_CMP](https://docs.aws.amazon.com/redshift/latest/dg/r_BTTEXT_PATTERN_CMP.html): Synonym for the BPCHARCMP function.
- [CHAR_LENGTH](https://docs.aws.amazon.com/redshift/latest/dg/r_CHAR_LENGTH.html): Synonym of the LEN function.
- [CHARACTER_LENGTH](https://docs.aws.amazon.com/redshift/latest/dg/r_CHARACTER_LENGTH.html): Synonym of the LEN function.
- [CHARINDEX](https://docs.aws.amazon.com/redshift/latest/dg/r_CHARINDEX.html): Returns the location of the specified substring within a string.
- [CHR](https://docs.aws.amazon.com/redshift/latest/dg/r_CHR.html): Returns the character that matches the ASCII code point value specified by of the input parameter.
- [COLLATE](https://docs.aws.amazon.com/redshift/latest/dg/r_COLLATE.html): Overrides the collation of a string column or expression.
- [CONCAT](https://docs.aws.amazon.com/redshift/latest/dg/r_CONCAT.html): Concatenates two expressions and returns the resulting expression.
- [CRC32](https://docs.aws.amazon.com/redshift/latest/dg/crc32-function.html): Uses a CRC32 algorithm to detect changes between source and target data as an error-detecting function.
- [DIFFERENCE](https://docs.aws.amazon.com/redshift/latest/dg/DIFFERENCE.html): Returns an INTEGER to indicate the difference between two strings compared as Soundex codes.
- [INITCAP](https://docs.aws.amazon.com/redshift/latest/dg/r_INITCAP.html): Capitalizes the first letter of each word in a specified string.
- [LEFT and RIGHT](https://docs.aws.amazon.com/redshift/latest/dg/r_LEFT.html): Returns the specified number of leftmost or rightmost characters from a character string.
- [LEN](https://docs.aws.amazon.com/redshift/latest/dg/r_LEN.html): Returns the length of the specified string as the number of characters.
- [LENGTH](https://docs.aws.amazon.com/redshift/latest/dg/r_LENGTH.html): Synonym of the LEN function.
- [LOWER](https://docs.aws.amazon.com/redshift/latest/dg/r_LOWER.html): Converts a string to lowercase.
- [LPAD and RPAD](https://docs.aws.amazon.com/redshift/latest/dg/r_LPAD.html): Prepend or append characters to a string, based on a specified length.
- [LTRIM](https://docs.aws.amazon.com/redshift/latest/dg/r_LTRIM.html): The LTRIM function trims a specified set of characters from the beginning of a string.
- [OCTETINDEX](https://docs.aws.amazon.com/redshift/latest/dg/OCTETINDEX.html): Returns the location of a substring within a string as a number of bytes.
- [OCTET_LENGTH](https://docs.aws.amazon.com/redshift/latest/dg/r_OCTET_LENGTH.html): Returns the length of the specified string as the number of bytes.
- [POSITION](https://docs.aws.amazon.com/redshift/latest/dg/r_POSITION.html): Returns the location of the specified substring within a string.
- [QUOTE_IDENT](https://docs.aws.amazon.com/redshift/latest/dg/r_QUOTE_IDENT.html): Returns the specified string as a string in double quotation marks so that it can be used as an identifier in a SQL statement.
- [QUOTE_LITERAL](https://docs.aws.amazon.com/redshift/latest/dg/r_QUOTE_LITERAL.html): Returns the specified string as a quoted string so that it can be used as a string literal in a SQL statement.
- [REGEXP_COUNT](https://docs.aws.amazon.com/redshift/latest/dg/REGEXP_COUNT.html): Searches a string for a regular expression pattern and returns an integer that indicates the number of times the pattern occurs in the string.
- [REGEXP_INSTR](https://docs.aws.amazon.com/redshift/latest/dg/REGEXP_INSTR.html): Returns the characters extracted from a string by searching for a regular expression pattern.
- [REGEXP_REPLACE](https://docs.aws.amazon.com/redshift/latest/dg/REGEXP_REPLACE.html): Searches a string for a regular expression pattern and replaces every occurrence of the pattern with the specified string.
- [REGEXP_SUBSTR](https://docs.aws.amazon.com/redshift/latest/dg/REGEXP_SUBSTR.html): Returns the characters extracted from a string by searching for a regular expression pattern.
- [REPEAT](https://docs.aws.amazon.com/redshift/latest/dg/r_REPEAT.html): Repeats a string the specified number of times.
- [REPLACE](https://docs.aws.amazon.com/redshift/latest/dg/r_REPLACE.html): Replaces all occurrences of a set of characters within an existing string with other specified characters.
- [REPLICATE](https://docs.aws.amazon.com/redshift/latest/dg/r_REPLICATE.html): Synonym for the REPEAT function.
- [REVERSE](https://docs.aws.amazon.com/redshift/latest/dg/r_REVERSE.html): Operates on a string and returns the characters in reverse order.
- [RTRIM](https://docs.aws.amazon.com/redshift/latest/dg/r_RTRIM.html): Trims a specified set of characters from the end of a string.
- [SOUNDEX](https://docs.aws.amazon.com/redshift/latest/dg/SOUNDEX.html): Returns the American Soundex value of the string that you specify.
- [SPLIT_PART](https://docs.aws.amazon.com/redshift/latest/dg/SPLIT_PART.html): Splits a string on the specified delimiter and returns the part at the specified position.
- [STRPOS](https://docs.aws.amazon.com/redshift/latest/dg/r_STRPOS.html): Returns the position of a substring within a specified string.
- [STRTOL](https://docs.aws.amazon.com/redshift/latest/dg/r_STRTOL.html): Converts a string expression of a number of the specified base to the equivalent integer value.
- [SUBSTRING](https://docs.aws.amazon.com/redshift/latest/dg/r_SUBSTRING.html): Returns the subset of a string based on the specified start position.
- [TEXTLEN](https://docs.aws.amazon.com/redshift/latest/dg/r_TEXTLEN.html): Synonym of LEN function.
- [TRANSLATE](https://docs.aws.amazon.com/redshift/latest/dg/r_TRANSLATE.html): >For a given expression, replaces all occurrences of specified characters with specified substitutes.
- [TRIM](https://docs.aws.amazon.com/redshift/latest/dg/r_TRIM.html): Trims a string by removing blanks or specified characters.
- [UPPER](https://docs.aws.amazon.com/redshift/latest/dg/r_UPPER.html): Converts a string to uppercase.

### [SUPER type information functions](https://docs.aws.amazon.com/redshift/latest/dg/c_Type_Info_Functions.html)

Work with the type information functions for SQL that Amazon Redshift supports to derive the dynamic information from inputs of the SUPER data type.

- [DECIMAL_PRECISION](https://docs.aws.amazon.com/redshift/latest/dg/r_decimal_precision.html): Checks the precision of the maximum total number of DECIMAL digits to be stored.
- [DECIMAL_SCALE](https://docs.aws.amazon.com/redshift/latest/dg/r_decimal_scale.html): Checks the number of decimal digits to be stored to the right of the decimal point.
- [IS_ARRAY](https://docs.aws.amazon.com/redshift/latest/dg/r_is_array.html): Checks whether a variable is an array.
- [IS_BIGINT](https://docs.aws.amazon.com/redshift/latest/dg/r_is_bigint.html): Checks whether a value is a BIGINT.
- [IS_BOOLEAN](https://docs.aws.amazon.com/redshift/latest/dg/r_is_boolean.html): Checks whether a value is a BOOLEAN.
- [IS_CHAR](https://docs.aws.amazon.com/redshift/latest/dg/r_is_char.html): Checks whether a value is a CHAR.
- [IS_DECIMAL](https://docs.aws.amazon.com/redshift/latest/dg/r_is_decimal.html): Checks whether a value is a decimal.
- [IS_FLOAT](https://docs.aws.amazon.com/redshift/latest/dg/r_is_float.html): Checks whether a value is a floating point number.
- [IS_INTEGER](https://docs.aws.amazon.com/redshift/latest/dg/r_is_integer.html): Returns true for numbers of scale 0 in the 32-bit range, and false for anything else (including null and floating point numbers).
- [IS_OBJECT](https://docs.aws.amazon.com/redshift/latest/dg/r_is_object.html): Checks whether a variable is an object.
- [IS_SCALAR](https://docs.aws.amazon.com/redshift/latest/dg/r_is_scalar.html): Checks whether a variable is a scalar.
- [IS_SMALLINT](https://docs.aws.amazon.com/redshift/latest/dg/r_is_smallint.html): Checks whether a variable is a smallint.
- [IS_VARCHAR](https://docs.aws.amazon.com/redshift/latest/dg/r_is_varchar.html): Checks whether a variable is a VARCHAR.
- [JSON_SIZE](https://docs.aws.amazon.com/redshift/latest/dg/r_json_size.html): The JSON_SIZE function returns an integer representing the number of bytes in the given SUPER expression when serialized into a string.
- [JSON_TYPEOF](https://docs.aws.amazon.com/redshift/latest/dg/r_json_typeof.html): The JSON_TYPEOF scalar function returns a VARCHAR with values boolean, number, string, object, array, or null, depending on the dynamic type of the SUPER value.
- [SIZE](https://docs.aws.amazon.com/redshift/latest/dg/r_SIZE.html): Returns the binary in-memory size of a SUPER type constant or expression as an integer.

### [VARBYTE functions](https://docs.aws.amazon.com/redshift/latest/dg/varbyte-functions.html)

Describes the VARBYTE functions and operators in Amazon Redshift.

- [VARBYTE operators](https://docs.aws.amazon.com/redshift/latest/dg/r_VARBYTE_OPERATORS.html): Lists the VARBYTE operator symbols supported by Amazon Redshift.
- [FROM_HEX](https://docs.aws.amazon.com/redshift/latest/dg/r_FROM_HEX.html): Converts a hexadecimal to a binary value.
- [FROM_VARBYTE](https://docs.aws.amazon.com/redshift/latest/dg/r_FROM_VARBYTE.html): Converts a binary value to a character string in the specified format.
- [GETBIT](https://docs.aws.amazon.com/redshift/latest/dg/r_GETBIT.html): Returns the bit value of a binary value at the specified index.
- [TO_HEX](https://docs.aws.amazon.com/redshift/latest/dg/r_TO_HEX.html): Converts a number or binary value to a hexadecimal representation.
- [TO_VARBYTE](https://docs.aws.amazon.com/redshift/latest/dg/r_TO_VARBYTE.html): Converts a string in a specified format to a binary value.

### [Window functions](https://docs.aws.amazon.com/redshift/latest/dg/c_Window_functions.html)

Create analytic business queries more efficiently using the window functions for SQL that Amazon Redshift supports.

- [AVG](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_AVG.html): Returns the average (arithmetic mean) of the input expression values.
- [COUNT](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_COUNT.html): Counts the rows defined by the expression.
- [CUME_DIST](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_CUME_DIST.html): An inverse distribution function that assumes a continuous distribution model.
- [DENSE_RANK](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_DENSE_RANK.html): Determines the rank of a value in a group of values, based on the ORDER BY expression in the OVER clause.
- [FIRST_VALUE](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_first_value.html): Returns the value of the specified expression with respect to the first row in the window frame given an ordered set of rows.
- [LAG](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_LAG.html): Returns the values for a row at a given offset above (before) the current row in the partition.
- [LAST_VALUE](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_last_value.html): Returns the value of the specified expression with respect to the first row in the window frame given an ordered set of rows.
- [LEAD](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_LEAD.html): Returns the values for a row at a given offset below (after) the current row in the partition.
- [LISTAGG](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_LISTAGG.html): For each group in a query, the LISTAGG window function orders the rows for that group according to the ORDER BY expression, then concatenates the values into a single string.
- [MAX](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_MAX.html): Returns the maximum of the input expression values.
- [MEDIAN](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_MEDIAN.html): Calculates the median value for the range of values in a window or partition.
- [MIN](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_MIN.html): Returns the minimum of the input expression values.
- [NTH_VALUE](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_NTH.html): Returns the expression value of the specified row of the window frame relative to the first row of the window.
- [NTILE](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_NTILE.html): Divides ordered rows in the partition into the specified number of ranked groups of as equal size as possible and returns the group that a given row falls into.
- [PERCENT_RANK](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_PERCENT_RANK.html): Calculates the percent rank of a given row.
- [PERCENTILE_CONT](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_PERCENTILE_CONT.html): An inverse distribution function that assumes a continuous distribution model.
- [PERCENTILE_DISC](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_PERCENTILE_DISC.html): An inverse distribution function that assumes a continuous distribution model.
- [RANK](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_RANK.html): Determines the rank of a value in a group of values, based on the ORDER BY expression in the OVER clause.
- [RATIO_TO_REPORT](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_RATIO_TO_REPORT.html): Calculates the ratio of a value to the sum of the values in a window or partition.
- [ROW_NUMBER](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_ROW_NUMBER.html): Assigns the row number of the current row within a group of rows, based on the ORDER BY expression in the OVER clause.
- [STDDEV_SAMP and STDDEV_POP](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_STDDEV.html): Returns the sample and population standard deviation of a set of numeric values (integer, decimal, or floating-point).
- [SUM](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_SUM.html): Returns the sum of the input column or expression values.
- [VAR_SAMP and VAR_POP](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_VARIANCE.html): Return the sample and population variance of a set of numeric values (integer, decimal, or floating-point).

### [System administration functions](https://docs.aws.amazon.com/redshift/latest/dg/r_System_administration_functions.html)

Work with the system administration functions for SQL that Amazon Redshift supports.

- [CHANGE_QUERY_PRIORITY](https://docs.aws.amazon.com/redshift/latest/dg/r_CHANGE_QUERY_PRIORITY.html): CHANGE_QUERY_PRIORITY enables superusers to modify the priority of a query that is either running or waiting in workload management (WLM).
- [CHANGE_SESSION_PRIORITY](https://docs.aws.amazon.com/redshift/latest/dg/r_CHANGE_SESSION_PRIORITY.html): CHANGE_SESSION_PRIORITY enables superusers to modify the priority of a query that is either running or waiting in workload management (WLM).
- [CHANGE_USER_PRIORITY](https://docs.aws.amazon.com/redshift/latest/dg/r_CHANGE_USER_PRIORITY.html): CHANGE_USER_PRIORITY enables superusers to modify the priority of all queries issued by a user that are either running or waiting in workload management (WLM).
- [CURRENT_SETTING](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_SETTING.html): Returns the current value of the specified configuration parameter.
- [PG_CANCEL_BACKEND](https://docs.aws.amazon.com/redshift/latest/dg/PG_CANCEL_BACKEND.html): Cancels a query.
- [PG_TERMINATE_BACKEND](https://docs.aws.amazon.com/redshift/latest/dg/PG_TERMINATE_BACKEND.html): Terminates a session.
- [REBOOT_CLUSTER](https://docs.aws.amazon.com/redshift/latest/dg/r_REBOOT_CLUSTER.html): Reboot the Amazon Redshift cluster without terminating the connections to the cluster.
- [SET_CONFIG](https://docs.aws.amazon.com/redshift/latest/dg/r_SET_CONFIG.html): Sets a configuration parameter to a new setting.

### [System information functions](https://docs.aws.amazon.com/redshift/latest/dg/r_System_information_functions.html)

Work with the system information functions for SQL that Amazon Redshift supports.

- [CURRENT_AWS_ACCOUNT](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_AWS_ACCOUNT.html): Returns the AWS account associated with the Amazon Redshift cluster that submitted a query.
- [CURRENT_DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_DATABASE.html): Returns the name of the database where you are currently connected.
- [CURRENT_NAMESPACE](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_NAMESPACE.html): Returns the cluster namespace of the current Amazon Redshift cluster.
- [CURRENT_SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_SCHEMA.html): Returns the name of the schema at the front of the search path.
- [CURRENT_SCHEMAS](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_SCHEMAS.html): Returns an array of the names of any schemas in the current search path.
- [CURRENT_SESSION_ARN](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_SESSION_ARN.html): Returns the ARN of the currently authorized datalake user.
- [CURRENT_USER](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_USER.html): Returns the user name of the current "effective" user of the database, as applicable to checking permissions.
- [CURRENT_USER_ID](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_USER_ID.html): Returns the unique identifier for the Amazon Redshift user logged in to the current session.
- [DEFAULT_IAM_ROLE](https://docs.aws.amazon.com/redshift/latest/dg/r_DEFAULT_IAM_ROLE.html): Returns the default IAM role currently associated with the Amazon Redshift cluster.
- [GET_MOUNTED_ROLE](https://docs.aws.amazon.com/redshift/latest/dg/GET_MOUNTED_ROLE.html): When invoked as part of a multi-dialect AWS Glue view, it allows returning the IAM role used to mount the Lake Formation schema or database.
- [HAS_ASSUMEROLE_PRIVILEGE](https://docs.aws.amazon.com/redshift/latest/dg/r_HAS_ASSUMEROLE_PRIVILEGE.html): Returns true if the user has the specified IAM role with the privilege to run the specified command.
- [HAS_DATABASE_PRIVILEGE](https://docs.aws.amazon.com/redshift/latest/dg/r_HAS_DATABASE_PRIVILEGE.html): Returns true if the user has the specified privilege for the specified database.
- [HAS_SCHEMA_PRIVILEGE](https://docs.aws.amazon.com/redshift/latest/dg/r_HAS_SCHEMA_PRIVILEGE.html): Returns true if the user has the specified privilege for the specified schema.
- [HAS_TABLE_PRIVILEGE](https://docs.aws.amazon.com/redshift/latest/dg/r_HAS_TABLE_PRIVILEGE.html): Returns true if the user has the specified privilege for the specified table.
- [LAST_USER_QUERY_ID](https://docs.aws.amazon.com/redshift/latest/dg/LAST_USER_QUERY_ID.html): Returns the query ID of the most recently completed query run by a user in the current session.
- [PG_BACKEND_PID](https://docs.aws.amazon.com/redshift/latest/dg/PG_BACKEND_PID.html): Returns the process ID (PID) of the server process handling the current session.
- [PG_GET_COLS](https://docs.aws.amazon.com/redshift/latest/dg/PG_GET_COLS.html): Returns the column metadata for a table or view definition.
- [PG_GET_GRANTEE_BY_IAM_ROLE](https://docs.aws.amazon.com/redshift/latest/dg/PG_GET_GRANTEE_BY_IAMROLE.html): Returns all users and groups granted a specified IAM role.
- [PG_GET_IAM_ROLE_BY_USER](https://docs.aws.amazon.com/redshift/latest/dg/PG_GET_IAM_ROLE_BY_USER.html): Returns all IAM roles and command privileges granted to a user.
- [PG_GET_LATE_BINDING_VIEW_COLS](https://docs.aws.amazon.com/redshift/latest/dg/PG_GET_LATE_BINDING_VIEW_COLS.html): Returns the column metadata for all late-binding views in the database.
- [PG_GET_SESSION_ROLES](https://docs.aws.amazon.com/redshift/latest/dg/PG_GET_SESSION_ROLES.html): Returns information about session roles.
- [PG_LAST_COPY_COUNT](https://docs.aws.amazon.com/redshift/latest/dg/PG_LAST_COPY_COUNT.html): Returns the number of rows that were loaded by the last COPY command run in the current session.
- [PG_LAST_COPY_ID](https://docs.aws.amazon.com/redshift/latest/dg/PG_LAST_COPY_ID.html): Returns the query ID of the most recently completed COPY command in the current session.
- [PG_LAST_UNLOAD_ID](https://docs.aws.amazon.com/redshift/latest/dg/PG_LAST_UNLOAD_ID.html): Returns the query ID of the most recently completed UNLOAD command.
- [PG_LAST_QUERY_ID](https://docs.aws.amazon.com/redshift/latest/dg/PG_LAST_QUERY_ID.html): Returns the query ID of the most recently completed query in the current session.
- [PG_LAST_UNLOAD_COUNT](https://docs.aws.amazon.com/redshift/latest/dg/PG_LAST_UNLOAD_COUNT.html): Returns the number of rows that were loaded by the last COPY command completed in the current session.
- [SLICE_NUM](https://docs.aws.amazon.com/redshift/latest/dg/r_SLICE_NUM.html): Returns an integer corresponding to the slice number in the cluster where the data for a row is located.
- [USER](https://docs.aws.amazon.com/redshift/latest/dg/r_USER.html): Synonym for CURRENT_USER.
- [ROLE_IS_MEMBER_OF](https://docs.aws.amazon.com/redshift/latest/dg/r_ROLE_IS_MEMBER_OF.html): Returns true if the role is a member of another role.
- [USER_IS_MEMBER_OF](https://docs.aws.amazon.com/redshift/latest/dg/r_USER_IS_MEMBER_OF.html): Returns true if the user is a member of a role or group.
- [VERSION](https://docs.aws.amazon.com/redshift/latest/dg/r_VERSION.html): Returns details about the currently installed release, with specific Amazon Redshift version information at the end.
- [Reserved words](https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html): Lists the reserved words used in Amazon Redshift.


## [System tables and views reference](https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_system-tables.html)

### [SVV metadata views](https://docs.aws.amazon.com/redshift/latest/dg/svv_views.html)

SVV views are system views in Amazon Redshift that contain information about database objects.

- [SVV_ACTIVE_CURSORS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ACTIVE_CURSORS.html): SVV_ACTIVE_CURSORS displays details for currently open cursors.
- [SVV_ALL_COLUMNS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ALL_COLUMNS.html): Use SVV_ALL_COLUMNS to view a union of columns from Amazon Redshift tables as shown in SVV_REDSHIFT_COLUMNS tables and the consolidated list of all external columns from all external tables.
- [SVV_ALL_SCHEMAS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ALL_SCHEMAS.html): Use SVV_ALL_SCHEMAS to view a union of Amazon Redshift schemas as shown in SVV_REDSHIFT_SCHEMAS and the consolidated list of all external schemas from all databases.
- [SVV_ALL_TABLES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ALL_TABLES.html): Use SVV_ALL_TABLES to view a union of Amazon Redshift tables as shown in SVV_REDSHIFT_TABLES and the consolidated list of all external tables from all external schemas.
- [SVV_ALTER_TABLE_RECOMMENDATIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ALTER_TABLE_RECOMMENDATIONS.html): Records the current Amazon Redshift Advisor recommendations for tables.
- [SVV_ATTACHED_MASKING_POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ATTACHED_MASKING_POLICY.html): Use SVV_ATTACHED_MASKING_POLICY to view all the relations and roles/users with policies attached on the currently connected database.
- [SVV_COLUMNS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_COLUMNS.html): Use SVV_COLUMNS to view tables in local and external catalogs.
- [SVV_COLUMN_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_COLUMN_PRIVILEGES.html): Use SVV_COLUMN_PRIVILEGES to view the column permissions that are explicitly granted to users, roles, and groups in the current database.
- [SVV_COPY_JOB_INTEGRATIONS](https://docs.aws.amazon.com/redshift/latest/dg/SVV_COPY_JOB_INTEGRATIONS.html): Use SVV_COPY_JOB_INTEGRATIONS to view details of COPY JOB commands.
- [SVV_DATABASE_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DATABASE_PRIVILEGES.html): Use SVV_DATABASE_PRIVILEGES to view the database permissions that are explicitly granted to users, roles, and groups in your Amazon Redshift cluster.
- [SVV_DATASHARE_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DATASHARE_PRIVILEGES.html): Use SVV_DATASHARE_PRIVILEGES to view the datashare permissions that are explicitly granted to users, roles, and groups in your Amazon Redshift cluster.
- [SVV_DATASHARES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DATASHARES.html): Use SVV_DATASHARES to view a list of datashares created on the cluster, and datashares shared with the cluster.
- [SVV_DATASHARE_CONSUMERS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DATASHARE_CONSUMERS.html): Use SVV_DATASHARE_CONSUMERS to view a list of consumers for a datashare created on a cluster.
- [SVV_DATASHARE_OBJECTS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DATASHARE_OBJECTS.html): Use SVV_DATASHARE_OBJECTS to view a list of objects in all datashares created on the cluster or shared with the cluster .
- [SVV_DEFAULT_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DEFAULT_PRIVILEGES.html): Contains information about the default privileges a user has access to.
- [SVV_DISKUSAGE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DISKUSAGE.html): Contains information about data allocation for the tables in a database.
- [SVV_EXTERNAL_COLUMNS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_EXTERNAL_COLUMNS.html): Use SVV_EXTERNAL_COLUMNS to view details for columns in external tables.
- [SVV_EXTERNAL_DATABASES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_EXTERNAL_DATABASES.html): Use SVV_EXTERNAL_DATABASES to view details for external databases.
- [SVV_EXTERNAL_PARTITIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_EXTERNAL_PARTITIONS.html): Use SVV_EXTERNAL_PARTITIONS to view details for partitions in external tables.
- [SVV_EXTERNAL_SCHEMAS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_EXTERNAL_SCHEMAS.html): Stores information about external schemas.
- [SVV_EXTERNAL_TABLES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_EXTERNAL_TABLES.html): Use SVV_EXTERNAL_TABLES to view details for external tables.
- [SVV_FUNCTION_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_FUNCTION_PRIVILEGES.html): Use SVV_FUNCTION_PRIVILEGES to view the function permissions that are explicitly granted to users, roles, and groups in the current database.
- [SVV_GEOGRAPHY_COLUMNS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_GEOGRAPHY_COLUMNS.html): Use SVV_GEOGRAPHY_COLUMNS to view the list of GEOGRAPHY columns.
- [SVV_GEOMETRY_COLUMNS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_GEOMETRY_COLUMNS.html): Use SVV_GEOMETRY_COLUMNS to view the list of GEOMETRY columns.
- [SVV_IAM_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_IAM_PRIVILEGES.html): Use SVV_IAM_PRIVILEGES to view explicitly granted IAM privileges on users, roles, and groups.
- [SVV_IDENTITY_PROVIDERS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_IDENTITY_PROVIDERS.html): The SVV_IDENTITY_PROVIDERS view returns the name and properties for identity providers.
- [SVV_INTEGRATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION.html): SVV_INTEGRATION displays details about the configuration of integrations.
- [SVV_INTEGRATION_TABLE_MAPPING](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION_TABLE_MAPPING.html): SVV_INTEGRATION_TABLE_MAPPING displays details about the mapping of source metadata values to target.
- [SVV_INTEGRATION_TABLE_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION_TABLE_STATE.html): SVV_INTEGRATION_TABLE_STATE displays details about table-level integration information.
- [SVV_INTERLEAVED_COLUMNS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTERLEAVED_COLUMNS.html): Use the SVV_INTERLEAVED_COLUMNS view to help determine whether a table that uses interleaved sort keys should be reindexed using a VACUUM REINDEX.
- [SVV_LANGUAGE_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_LANUGAGE_PRIVILEGES.html): Use SVV_LANGUAGE_PRIVILEGES to view the language permissions that are explicitly granted to users, roles, and groups in the current database.
- [SVV_MASKING_POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_MASKING_POLICY.html): Use SVV_MASKING_POLICY to view all masking policies created on the cluster.
- [SVV_ML_MODEL_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ML_MODEL_INFO.html): State information about the current state of the machine learning models.
- [SVV_ML_MODEL_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ML_MODEL_PRIVILEGES.html): Use SVV_ML_MODEL_PRIVILEGES to view the machine learning model permissions that are explicitly granted to users, roles, and groups in the cluster.
- [SVV_MV_DEPENDENCY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_MV_DEPENDENCY.html): The SVV_MV_DEPENDENCY table shows the dependencies of materialized views on other materialized views within Amazon Redshift.
- [SVV_MV_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_MV_INFO.html): The SVV_MV_INFO table contains a row for every materialized view, whether the data is stale, and state information.
- [SVV_QUERY_INFLIGHT](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_QUERY_INFLIGHT.html): Determines what queries are currently running on the database.
- [SVV_QUERY_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_QUERY_STATE.html): View information about the runtime of currently running queries.
- [SVV_REDSHIFT_COLUMNS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_REDSHIFT_COLUMNS.html): Use SVV_REDSHIFT_COLUMNS to view a list of all columns that a user has access to.
- [SVV_REDSHIFT_DATABASES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_REDSHIFT_DATABASES.html): Use SVV_ REDSHIFT_DATABASES to view a list of all the databases that a user has access to.
- [SVV_REDSHIFT_FUNCTIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_REDSHIFT_FUNCTIONS.html): Use SVV_REDSHIFT_FUNCTIONS to view a list of all functions that a user has access to.
- [SVV_REDSHIFT_SCHEMA_QUOTA](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_REDSHIFT_SCHEMA_QUOTA.html): Displays the quota and the current disk usage for each schema.
- [SVV_REDSHIFT_SCHEMAS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_REDSHIFT_SCHEMAS.html): Use SVV_REDSHIFT_SCHEMAS to view a list of all schemas that a user has access to.
- [SVV_REDSHIFT_TABLES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_REDSHIFT_TABLES.html): Use SVV_REDSHIFT_TABLES to view a list of all tables that a user has access to.
- [SVV_RELATION_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_RELATION_PRIVILEGES.html): Use SVV_RELATION_PRIVILEGES to view the relation (tables and views) permissions that are explicitly granted to users, roles, and groups in the current database.
- [SVV_RLS_APPLIED_POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_RLS_APPLIED_POLICY.html): Use SVV_RLS_APPLIED_POLICY to trace the application of RLS policies on queries that reference RLS-protected relations.
- [SVV_RLS_ATTACHED_POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_RLS_ATTACHED_POLICY.html): Use SVV_RLS_ATTACHED_POLICY to view a list of all relations and users that have one or more row-level security policies attached on the currently connected database.
- [SVV_RLS_POLICY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_RLS_POLICY.html): Use SVV_RLS_POLICY to view a list of all row-level security policies created on the Amazon Redshift cluster.
- [SVV_RLS_RELATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_RLS_RELATION.html): Use SVV_RLS_RELATION to view a list of all relations that are RLS-protected.
- [SVV_ROLE_GRANTS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ROLE_GRANTS.html): Use SVV_ROLE_GRANTS to view a list of roles that are explicitly granted roles in the cluster.
- [SVV_ROLES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_ROLES.html): Use SVV_ROLES to view role information.
- [SVV_SCHEMA_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_SCHEMA_PRIVILEGES.html): Use SVV_SCHEMA_PRIVILEGES to view the schema permissions that are explicitly granted to users, roles, and groups in the current database.
- [SVV_SCHEMA_QUOTA_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_SCHEMA_QUOTA_STATE.html): Displays the quota and the current disk usage for each schema.
- [SVV_SYSTEM_PRIVILEGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_SYSTEM_PRIVILEGES.html): Use SVV_SYSTEM_PRIVILEGES to view the users and roles that are explicitly granted system permissions in the Amazon Redshift cluster.
- [SVV_TABLE_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html): View summary information for tables in an Amazon Redshift database.
- [SVV_TABLES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLES.html): Use SVV_TABLES to view tables in local and external catalogs.
- [SVV_TRANSACTIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TRANSACTIONS.html): Records information about transactions that currently hold locks on tables in the database.
- [SVV_USER_GRANTS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_USER_GRANTS.html): Use SVV_USER_GRANTS to view the list of users that are explicitly granted roles in the cluster.
- [SVV_USER_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_USER_INFO.html): Provides data about users of the Amazon Redshift database.
- [SVV_VACUUM_PROGRESS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_VACUUM_PROGRESS.html): Returns an estimate of how much time it will take to complete a vacuum operation that is currently in progress.
- [SVV_VACUUM_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_VACUUM_SUMMARY.html): Summarizes information about the vacuum operations logged by the system.

### [SYS monitoring views](https://docs.aws.amazon.com/redshift/latest/dg/serverless_views-monitoring.html)

Monitoring views are system views in Amazon Redshift that are used to monitor query and workload resource usage of provisioned clusters and serverless workgroups.

- [SYS_ANALYZE_COMPRESSION_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_ANALYZE_COMPRESSION_HISTORY.html): Records details for commands that do compression analysis.
- [SYS_ANALYZE_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_ANALYZE_HISTORY.html): Logs details for ANALYZE operations
- [SYS_APPLIED_MASKING_POLICY_LOG](https://docs.aws.amazon.com/redshift/latest/dg/SYS_APPLIED_MASKING_POLICY_LOG.html): Logs details for dynamic data masking policies applied on queries referencing DDM-protected relations.
- [SYS_AUTOMATIC_OPTIMIZATION](https://docs.aws.amazon.com/redshift/latest/dg/SYS_AUTOMATIC_OPTIMIZATION.html): Use SYS_AUTOMATIC_OPTIMIZATION to view details on the tasks that Amazon Redshift runs for automatic optimization.
- [SYS_AUTO_TABLE_OPTIMIZATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_AUTO_TABLE_OPTIMIZATION.html): Records automated actions taken by Amazon Redshift on tables defined for automatic optimization.
- [SYS_CHILD_QUERY_TEXT](https://docs.aws.amazon.com/redshift/latest/dg/SYS_CHILD_QUERY_TEXT.html): Returns the SQL text of a child query.
- [SYS_CONNECTION_LOG](https://docs.aws.amazon.com/redshift/latest/dg/SYS_CONNECTION_LOG.html): Logs authentication attempts and connections and disconnections.
- [SYS_COPY_JOB](https://docs.aws.amazon.com/redshift/latest/dg/SYS_COPY_JOB.html): Use SYS_COPY_JOB to view details of COPY JOB commands.
- [SYS_COPY_JOB_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_COPY_JOB_DETAIL.html): Use SYS_COPY_JOB_DETAIL to view details of COPY JOB commands.
- [SYS_COPY_JOB_INFO](https://docs.aws.amazon.com/redshift/latest/dg/SYS_COPY_JOB_INFO.html): Use SYS_COPY_JOB_INFO to view information about COPY JOB commands.
- [SYS_COPY_REPLACEMENTS](https://docs.aws.amazon.com/redshift/latest/dg/SYS_COPY_REPLACEMENTS.html): Displays a log that records when invalid UTF-8 characters were replaced by the COPY command with the ACCEPTINVCHARS option.
- [SYS_DATASHARE_CHANGE_LOG](https://docs.aws.amazon.com/redshift/latest/dg/SYS_DATASHARE_CHANGE_LOG.html): Records the consolidated view for tracking changes to datashares on both producer and consumer clusters.
- [SYS_DATASHARE_CROSS_REGION_USAGE](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_DATASHARE_CROSS_REGION_USAGE.html): Use the SYS_DATASHARE_CROSS_REGION_USAGE view to get a summary of cross-Region data transferred usage caused by a cross-Region datasharing query.
- [SYS_DATASHARE_USAGE_CONSUMER](https://docs.aws.amazon.com/redshift/latest/dg/SYS_DATASHARE_USAGE_CONSUMER.html): Records the activity and usage of datashares.
- [SYS_DATASHARE_USAGE_PRODUCER](https://docs.aws.amazon.com/redshift/latest/dg/SYS_DATASHARE_USAGE_PRODUCER.html): Records the activity and usage of datashares.
- [SYS_EXTERNAL_QUERY_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_EXTERNAL_QUERY_DETAIL.html): Use SYS_EXTERNAL_QUERY_DETAIL to view details of user queries.
- [SYS_EXTERNAL_QUERY_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/SYS_EXTERNAL_QUERY_ERROR.html): Learn how to query the system view SYS_EXTERNAL_QUERY_ERROR to get information about Redshift Spectrum scan errors.
- [SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION](https://docs.aws.amazon.com/redshift/latest/dg/SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION.html): Use SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION to view the usage periods in which Amazon Redshift ran automatic optimization tasks using extra compute resources.
- [SYS_INTEGRATION_ACTIVITY](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_INTEGRATION_ACTIVITY.html): SYS_INTEGRATION_ACTIVITY displays details about completed integration runs.
- [SYS_INTEGRATION_TABLE_ACTIVITY](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_INTEGRATION_TABLE_ACTIVITY.html): SYS_INTEGRATION_TABLE_ACTIVITY displays details of insert, delete, and update activity of zero-ETL integrations.
- [SYS_INTEGRATION_TABLE_STATE_CHANGE](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_INTEGRATION_TABLE_STATE_CHANGE.html): SYS_INTEGRATION_TABLE_STATE_CHANGE displays details about table state change logs for integrations.
- [SYS_LOAD_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_LOAD_DETAIL.html): Returns information to track or troubleshoot a data load.
- [SYS_LUDF_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_LUDF_DETAIL.html): Records information and metrics for Lambda User Defined Functions (LUDFs) that were used in a particular query.
- [SYS_LOAD_ERROR_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_LOAD_ERROR_DETAIL.html): Use SYS_LOAD_ERROR_DETAIL to view details of copy queries.
- [SYS_LOAD_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_LOAD_HISTORY.html): Use SYS_LOAD_HISTORY to view details of user queries.
- [SYS_MV_REFRESH_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_MV_REFRESH_HISTORY.html): The results include information about the refresh history of all materialized views.
- [SYS_MV_STATE](https://docs.aws.amazon.com/redshift/latest/dg/SYS_MV_STATE.html): The results include information about the state of all materialized views.
- [SYS_PROCEDURE_CALL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_PROCEDURE_CALL.html): Use the SYS_PROCEDURE_CALL view to get information about stored procedure calls, including start time, end time, status of a stored procedure call, and call hierarchy for nested stored procedure calls.
- [SYS_PROCEDURE_MESSAGES](https://docs.aws.amazon.com/redshift/latest/dg/SYS_PROCEDURE_MESSAGES.html): Use the SYS_PROCEDURE_MESSAGES view to get information about stored procedure messages.
- [SYS_QUERY_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_QUERY_DETAIL.html): Use SYS_QUERY_DETAIL to view details of user queries.
- [SYS_QUERY_EXPLAIN](https://docs.aws.amazon.com/redshift/latest/dg/SYS_QUERY_EXPLAIN.html): Use SYS_QUERY_EXPLAIN to view the EXPLAIN plans for user queries.
- [SYS_QUERY_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_QUERY_HISTORY.html): Use SYS_QUERY_HISTORY to view details of user queries.
- [SYS_QUERY_TEXT](https://docs.aws.amazon.com/redshift/latest/dg/SYS_QUERY_TEXT.html): Use SYS_QUERY_TEXT to view details of user queries.
- [SYS_REDSHIFT_TEMPLATE](https://docs.aws.amazon.com/redshift/latest/dg/SYS_REDSHIFT_TEMPLATE.html): Use SYS_REDSHIFT_TEMPLATE to view details of TEMPLATES.
- [SYS_RESTORE_LOG](https://docs.aws.amazon.com/redshift/latest/dg/SYS_RESTORE_LOG.html): Use SYS_RESTORE_LOG to monitor the migration progress of each table in the cluster during a classic resize to or from RA3 nodes.
- [SYS_RESTORE_STATE](https://docs.aws.amazon.com/redshift/latest/dg/SYS_RESTORE_STATE.html): Use SYS_RESTORE_STATE to monitor the migration progress of each table during a classic resize.
- [SYS_SCHEMA_QUOTA_VIOLATIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_SCHEMA_QUOTA_VIOLATIONS.html): Records the occurrence, transaction ID, and other useful information when a schema quota is exceeded.
- [SYS_SERVERLESS_USAGE](https://docs.aws.amazon.com/redshift/latest/dg/SYS_SERVERLESS_USAGE.html): Use SYS_SERVERLESS_USAGE to view details of Amazon Redshift Serverless usage of resources.
- [SYS_SESSION_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_SESSION_HISTORY.html): Use the SYS_SESSION_HISTORY to view information about the current active sessions and session history.
- [SYS_SPATIAL_SIMPLIFY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_SPATIAL_SIMPLIFY.html): Get information about simplified spatial geometry objects using the COPY command by using the system view SYS_SPATIAL_SIMPLIFY.
- [SYS_STREAM_SCAN_ERRORS](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_STREAM_SCAN_ERRORS.html): Use SYS_STREAM_SCAN_ERRORS shows errors for streaming ingestion.
- [SYS_STREAM_SCAN_STATES](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_STREAM_SCAN_STATES.html): Use SYS_STREAM_SCAN_STATES shows states for streaming ingestion.
- [SYS_TRANSACTION_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_TRANSACTION_HISTORY.html): Use SYS_TRANSACTION_HISTORY to see details of a transaction when tracking a query.
- [SYS_UDF_LOG](https://docs.aws.amazon.com/redshift/latest/dg/SYS_UDF_LOG.html): Logs error and warning messages generated during UDF execution
- [SYS_UNLOAD_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/SYS_UNLOAD_DETAIL.html): Use SYS_UNLOAD_DETAIL to view details of an UNLOAD operation.
- [SYS_UNLOAD_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_UNLOAD_HISTORY.html): Use SYS_UNLOAD_HISTORY to view details of user queries.
- [SYS_USERLOG](https://docs.aws.amazon.com/redshift/latest/dg/SYS_USERLOG.html): Records details for the following changes to a database user:
- [SYS_VACUUM_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_VACUUM_HISTORY.html): Use SYS_VACUUM_HISTORY to view details of vacuum queries.
- [System view mapping for migrating to SYS monitoring views](https://docs.aws.amazon.com/redshift/latest/dg/sys_view_migration.html): SYS views consolidate and streamline the content of multiple non-SYS system views, giving you the information needed to monitor Amazon Redshift.

### [System monitoring (provisioned only)](https://docs.aws.amazon.com/redshift/latest/dg/c_intro_system_views.html)

System monitoring tables and views contain a subset of data found in several of the Amazon Redshift system tables.

### [STL views for logging](https://docs.aws.amazon.com/redshift/latest/dg/c_intro_STL_tables.html)

Describes the STL system views that are generated from Amazon Redshift log files to provide a history of the system.

- [STL_AGGR](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_AGGR.html): Analyzes aggregate execution steps for queries.
- [STL_ALERT_EVENT_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_ALERT_EVENT_LOG.html): Records an alert when the query optimizer identifies conditions that might indicate performance issues.
- [STL_ANALYZE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_ANALYZE.html): Records details for ANALYZE operations.
- [STL_ANALYZE_COMPRESSION](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_ANALYZE_COMPRESSION.html): Records details for commands that do compression analysis.
- [STL_BCAST](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_BCAST.html): Logs information about network activity during execution of query steps that broadcast data.
- [STL_COMMIT_STATS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_COMMIT_STATS.html): Provides metrics related to commit performance, including the timing of the various stages of commit and the number of blocks committed.
- [STL_CONNECTION_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_CONNECTION_LOG.html): Logs authentication attempts and connections and disconnections.
- [STL_DDLTEXT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_DDLTEXT.html): Captures DDL statements that were run on the system.
- [STL_DELETE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_DELETE.html): Analyzes delete execution steps for queries.
- [STL_DISK_FULL_DIAG](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_DISK_FULL_DIAG.html): Logs information about errors recorded when the disk is full.
- [STL_DIST](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_DIST.html): Logs information about network activity during execution of query steps that distribute data.
- [STL_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_ERROR.html): Records all errors that occur while running queries.
- [STL_EXPLAIN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_EXPLAIN.html): Displays the EXPLAIN plan for a query that has been submitted for execution.
- [STL_FILE_SCAN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_FILE_SCAN.html): Returns the files that Amazon Redshift read while loading data by using the COPY command.
- [STL_HASH](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_HASH.html): Analyzes hash execution steps for queries.
- [STL_HASHJOIN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_HASHJOIN.html): Analyzes hash join execution steps for queries.
- [STL_INSERT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_INSERT.html): Analyzes insert execution steps for queries.
- [STL_LIMIT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_LIMIT.html): Analyzes the execution steps that occur when a LIMIT clause is used in a SELECT query.
- [STL_LOAD_COMMITS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_LOAD_COMMITS.html): Returns information to track or troubleshoot a data load.
- [STL_LOAD_ERRORS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_LOAD_ERRORS.html): Displays the records of all Amazon Redshift load errors.
- [STL_LOADERROR_DETAIL](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_LOADERROR_DETAIL.html): Displays a log of data parse errors that occurred while using a COPY command to load tables.
- [STL_MERGE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_MERGE.html): Analyzes merge execution steps for queries.
- [STL_MERGEJOIN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_MERGEJOIN.html): Analyzes merge join execution steps for queries.
- [STL_MV_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_MV_STATE.html): Log of each state transition of a materialized views.
- [STL_NESTLOOP](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_NESTLOOP.html): Analyzes nested-loop join execution steps for queries.
- [STL_PARSE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_PARSE.html): Analyzes query steps that parse strings into binary values for loading.
- [STL_PLAN_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_PLAN_INFO.html): Displays the EXPLAIN output for a query in terms of a set of rows.
- [STL_PROJECT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_PROJECT.html): Contains rows for query steps that are used to evaluate expressions.
- [STL_QUERY](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_QUERY.html): Returns execution information about a database query.
- [STL_QUERY_METRICS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_QUERY_METRICS.html): View metrics information for queries running in user-defined query queues (service classes).
- [STL_QUERYTEXT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_QUERYTEXT.html): Captures the query text for SQL commands.
- [STL_REPLACEMENTS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_REPLACEMENTS.html): Displays a log that records when invalid UTF-8 characters were replaced by the COPY command with the ACCEPTINVCHARS option.
- [STL_RESTARTED_SESSIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_RESTARTED_SESSIONS.html): When Amazon Redshift restarts a session, STL_RESTARTED_SESSIONS records the new process ID (PID) and the original PID.
- [STL_RETURN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_RETURN.html): Contains details for return steps in queries.
- [STL_S3CLIENT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_S3CLIENT.html): Records transfer time and other performance metrics.
- [STL_S3CLIENT_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_S3CLIENT_ERROR.html): Records errors encountered by a slice while loading a file from Amazon S3.
- [STL_SAVE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SAVE.html): Contains details for save steps in queries.
- [STL_SCAN](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SCAN.html): Analyzes table scan steps for queries.
- [STL_SCHEMA_QUOTA_VIOLATIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SCHEMA_QUOTA_VIOLATIONS.html): Records the occurrence, timestamp, XID, and other useful information when a schema quota is exceeded.
- [STL_SESSIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SESSIONS.html): Returns information about user session history.
- [STL_SORT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SORT.html): Displays sort execution steps for queries, such as steps that use ORDER BY processing.
- [STL_SSHCLIENT_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_SSHCLIENT_ERROR.html): Records all errors seen by the SSH client.
- [STL_STREAM_SEGS](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_STREAM_SEGS.html): Lists the relationship between streams and concurrent segments.
- [STL_TR_CONFLICT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_TR_CONFLICT.html): Displays information to identify and resolve transaction conflicts with database tables.
- [STL_UNDONE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_UNDONE.html): Displays information about transactions that have been undone.
- [STL_UNIQUE](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_UNIQUE.html): Analyzes execution steps that occur when a DISTINCT function is used in the SELECT list or when duplicates are removed in a UNION or INTERSECT query.
- [STL_UNLOAD_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_UNLOAD_LOG.html): Records the details for an unload operation.
- [STL_USAGE_CONTROL](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_USAGE_CONTROL.html): Contains information that is logged when a usage limit is reached.
- [STL_USERLOG](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_USERLOG.html): Records the details for changes to a database user.
- [STL_UTILITYTEXT](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_UTILITYTEXT.html): Captures the text of non-SELECT SQL commands run on the database.
- [STL_VACUUM](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_VACUUM.html): Displays the row and block statistics for tables that have been vacuumed.
- [STL_WINDOW](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_WINDOW.html): Analyzes query steps that perform window functions.
- [STL_WLM_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_WLM_ERROR.html): Records all WLM-related errors as they occur.
- [STL_WLM_RULE_ACTION](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_WLM_RULE_ACTION.html): Records details about actions resulting from WLM query monitoring rules associated with user-defined queues.
- [STL_WLM_QUERY](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_WLM_QUERY.html): Contains a record of each attempted execution of a query in a service class handled by WLM.

### [STV tables for snapshot data](https://docs.aws.amazon.com/redshift/latest/dg/c_intro_STV_tables.html)

Work with the STV tables in Amazon Redshift, which are virtual system tables that contain snapshots of the current system data.

- [STV_ACTIVE_CURSORS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_ACTIVE_CURSORS.html): See details for currently open cursors.
- [STV_BLOCKLIST](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_BLOCKLIST.html): Contains the number of 1 MB disk blocks that are used by each slice, table, or column in a database.
- [STV_CURSOR_CONFIGURATION](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_CURSOR_CONFIGURATION.html): Displays cursor configuration constraints.
- [STV_DB_ISOLATION_LEVEL](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_DB_ISOLATION_LEVEL.html): Displays isolation level of databases.
- [STV_EXEC_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_EXEC_STATE.html): Displays information about queries and query steps that are actively running on Amazon Redshift compute nodes.
- [STV_INFLIGHT](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_INFLIGHT.html): Determines what queries are currently running on the cluster.
- [STV_LOAD_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_LOAD_STATE.html): Displays information about the current state of ongoing COPY statements.
- [STV_LOCKS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_LOCKS.html): View any current updates on the tables in the database.
- [STV_ML_MODEL_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_ML_MODEL_INFO.html): State information about the current state of the machine learning models.
- [STV_MV_DEPS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_MV_DEPS.html): The STV_MV_DEPS table shows the dependencies of materialized views on other materialized views within Amazon Redshift.
- [STV_MV_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_MV_INFO.html): The STV_MV_INFO table contains a row for every materialized view, whether the data is stale, and state information.
- [STV_NODE_STORAGE_CAPACITY](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_NODE_STORAGE_CAPACITY.html): Shows details of total storage capacity.
- [STV_PARTITIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_PARTITIONS.html): View the disk speed performance and disk utilization for Amazon Redshift.
- [STV_QUERY_METRICS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_QUERY_METRICS.html): View the disk speed performance and disk utilization for Amazon Redshift.
- [STV_RECENTS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_RECENTS.html): View information about the currently active and recently run queries against an Amazon Redshift database.
- [STV_SESSIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_SESSIONS.html): View information about the active user sessions for Amazon Redshift.
- [STV_SLICES](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_SLICES.html): View the current mapping of a slice to a node.
- [STV_STARTUP_RECOVERY_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_STARTUP_RECOVERY_STATE.html): Records the state of tables that are temporarily locked during cluster restart operations.
- [STV_TBL_PERM](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_TBL_PERM.html): View information about the permanent tables in Amazon Redshift.
- [STV_TBL_TRANS](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_TBL_TRANS.html): Find information about the transient database tables that are currently in memory.
- [STV_WLM_CLASSIFICATION_CONFIG](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_WLM_CLASSIFICATION_CONFIG.html): Contains the current classification rules for WLM.
- [STV_WLM_QMR_CONFIG](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_WLM_QMR_CONFIG.html): Records the configuration for WLM query monitoring rules (QMR).
- [STV_WLM_QUERY_QUEUE_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_WLM_QUERY_QUEUE_STATE.html): Records the current state of the query queues for the service classes.
- [STV_WLM_QUERY_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_WLM_QUERY_STATE.html): Records the current state of queries being tracked by WLM.
- [STV_WLM_QUERY_TASK_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_WLM_QUERY_TASK_STATE.html): Contains the current state of service class query tasks.
- [STV_WLM_SERVICE_CLASS_CONFIG](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_WLM_SERVICE_CLASS_CONFIG.html): Records the service class configurations for WLM.
- [STV_WLM_SERVICE_CLASS_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_WLM_SERVICE_CLASS_STATE.html): Contains the current state of the WLM service classes.
- [STV_XRESTORE_ALTER_QUEUE_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_STV_XRESTORE_ALTER_QUEUE_STATE.html): Find information on the migration progress of tables during a classic resize.

### [SVCS views for main and concurrency scaling clusters](https://docs.aws.amazon.com/redshift/latest/dg/svcs_views.html)

SVCS system views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters.

- [SVCS_ALERT_EVENT_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_ALERT_EVENT_LOG.html): Records an alert when the query optimizer identifies conditions that might indicate performance issues.
- [SVCS_COMPILE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_COMPILE.html): Records compile time and location for each query segment of queries, including queries run on a scaling cluster as well as queries run on the main cluster.
- [SVCS_CONCURRENCY_SCALING_USAGE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_CONCURRENCY_SCALING_USAGE.html): Records the usage periods for concurrency scaling.
- [SVCS_EXPLAIN](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_EXPLAIN.html): Displays the EXPLAIN plan for a query that has been submitted for execution.
- [SVCS_PLAN_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_PLAN_INFO.html): Displays the EXPLAIN output for a query in terms of a set of rows.
- [SVCS_QUERY_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_QUERY_SUMMARY.html): Find general information about the execution of a query.
- [SVCS_S3LIST](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_S3LIST.html): Use the SVCS_S3LIST system view to get details about Amazon Redshift Spectrum queries at the segment level.
- [SVCS_S3LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_S3LOG.html): Use the SVCS_S3LOG system view to get troubleshooting details about Redshift Spectrum queries at the segment level.
- [SVCS_S3PARTITION_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_S3PARTITION_SUMMARY.html): Use the SVCS_S3PARTITION_SUMMARY view to get a summary of Redshift Spectrum queries partition processing at the segment level.
- [SVCS_S3QUERY_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_S3QUERY_SUMMARY.html): Use the SVCS_S3QUERY_SUMMARY view to get a summary of all Redshift Spectrum queries (S3 queries) that have been run on the system.
- [SVCS_STREAM_SEGS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_STREAM_SEGS.html): Lists the relationship between streams and concurrent segments.
- [SVCS_UNLOAD_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVCS_UNLOAD_LOG.html): Records the details for an unload operation.

### [SVL views for main cluster](https://docs.aws.amazon.com/redshift/latest/dg/svl_views.html)

SVL views are system views in Amazon Redshift that contain references to STL tables and logs for more detailed information.

- [SVL_AUTO_WORKER_ACTION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_AUTO_WORKER_ACTION.html): Records automated actions taken by Amazon Redshift on tables defined for automatic optimization.
- [SVL_COMPILE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_COMPILE.html): Records compile time and location for each query segment of queries.
- [SVL_DATASHARE_CHANGE_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_DATASHARE_CHANGE_LOG.html): Records the consolidated view for tracking changes to datashares on both producer and consumer clusters.
- [SVL_DATASHARE_CROSS_REGION_USAGE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_DATASHARE_CROSS_REGION_USAGE.html): Use the SVL_DATASHARE_CROSS_REGION_USAGE view to get a summary of cross-Region data transferred usage caused by a cross-Region datasharing query.
- [SVL_DATASHARE_USAGE_CONSUMER](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_DATASHARE_USAGE_CONSUMER.html): Records the activity and usage of datashares.
- [SVL_DATASHARE_USAGE_PRODUCER](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_DATASHARE_USAGE_PRODUCER.html): Records the activity and usage of datashares.
- [SVL_FEDERATED_QUERY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_FEDERATED_QUERY.html): Use the SVL_FEDERATED_QUERY view to view information about a federated query call.
- [SVL_MULTI_STATEMENT_VIOLATIONS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_MULTI_STATEMENT_VIOLATIONS.html): Use the SVL_MULTI_STATEMENT_VIOLATIONS view to get a complete record of all of the SQL commands run on the system that have violations.
- [SVL_MV_REFRESH_STATUS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_MV_REFRESH_STATUS.html): Refresh status of materialized views.
- [SVL_QERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QERROR.html): The SVL_QERROR view is deprecated.
- [SVL_QLOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QLOG.html): Contains a log of all queries run against the database.
- [SVL_QUERY_METRICS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_METRICS.html): View metrics information for queries running in user-defined query queues (service classes).
- [SVL_QUERY_METRICS_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_METRICS_SUMMARY.html): View metrics information for queries running in user-defined query queues (service classes).
- [SVL_QUERY_QUEUE_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_QUEUE_INFO.html): Summarizes details for queries that spent time in a workload management (WLM) query queue or a commit queue.
- [SVL_QUERY_REPORT](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_REPORT.html): Lists the information about completed queries by slice and by step, which can help with troubleshooting node and slice issues in the Amazon Redshift cluster.
- [SVL_QUERY_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_QUERY_SUMMARY.html): Find general information about the execution of a query.
- [SVL_RESTORE_ALTER_TABLE_PROGRESS](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_RESTORE_ALTER_TABLE_PROGRESS.html): Find information on the migration progress of tables during a classic resize.
- [SVL_S3LIST](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3LIST.html): Use the SVL_S3LIST system view to get details about Amazon Redshift Spectrum queries at the segment level.
- [SVL_S3LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3LOG.html): Use the SVL_S3LOG system view to get details about Amazon Redshift Spectrum queries at the segment and node slice level.
- [SVL_S3PARTITION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3PARTITION.html): Use the SVL_S3PARTITION view to get details about Amazon Redshift Spectrum queries (S3 queries) at the segment and node slice level.
- [SVL_S3PARTITION_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3PARTITION_SUMMARY.html): Use the SVL_S3PARTITION_SUMMARY view to get a summary of Redshift Spectrum queries partition processing at the segment level.
- [SVL_S3QUERY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3QUERY.html): Use the SVL_S3QUERY view to get details about Amazon Redshift Spectrum queries (S3 queries) at the segment and node slice level.
- [SVL_S3QUERY_SUMMARY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3QUERY_SUMMARY.html): Use the SVL_S3QUERY_SUMMARY view to get a summary of all Amazon Redshift Spectrum queries (S3 queries) that have been run on the system.
- [SVL_S3RETRIES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_S3RETRIES.html): Use the SVL_S3RETRIES view to get information about why an Amazon Redshift Spectrum query based on Amazon S3 has failed.
- [SVL_SPATIAL_SIMPLIFY](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_SPATIAL_SIMPLIFY.html): Get information about simplified spatial geometry objects using the COPY command by using the system view SVL_SPATIAL_SIMPLIFY.
- [SVL_SPECTRUM_SCAN_ERROR](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_SPECTRUM_SCAN_ERROR.html): Learn how to query the system view SVL_SPECTRUM_SCAN_ERROR to get information about Redshift Spectrum scan errors.
- [SVL_STATEMENTTEXT](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_STATEMENTTEXT.html): Get a complete record of all of the SQL commands that have been run on the system.
- [SVL_STORED_PROC_CALL](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_STORED_PROC_CALL.html): Get information about stored procedure calls.
- [SVL_STORED_PROC_MESSAGES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_STORED_PROC_MESSAGES.html): Get information about stored procedure messages.
- [SVL_TERMINATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_TERMINATE.html): Use SVL_TERMINATE to view contains processes that are cancelled or terminated.
- [SVL_UDF_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_UDF_LOG.html): Provides data about the errors and warnings generated by user-defined functions.
- [SVL_USER_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_USER_INFO.html): Provides data about users of the Amazon Redshift database.
- [SVL_VACUUM_PERCENTAGE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVL_VACUUM_PERCENTAGE.html): Reports the percentage of data blocks allocated to a table after performing a vacuum.

### [System catalog tables](https://docs.aws.amazon.com/redshift/latest/dg/c_intro_catalog_views.html)

Describes the system catalogs that store schema metadata for Amazon Redshift.

- [PG_ATTRIBUTE_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_ATTRIBUTE_INFO.html): PG_ATTRIBUTE_INFO is an Amazon Redshift system view built on the PostgreSQL catalog table PG_ATTRIBUTE and the internal catalog table PG_ATTRIBUTE_ACL.
- [PG_CLASS_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_CLASS_INFO.html): PG_CLASS_INFO is an Amazon Redshift system view built on the PostgreSQL catalog tables PG_CLASS and PG_CLASS_EXTENDED.
- [PG_DATABASE_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_DATABASE_INFO.html): PG_DATABASE_INFO is an Amazon Redshift system view that extends the PostgreSQL catalog table PG_DATABASE.
- [PG_DEFAULT_ACL](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_DEFAULT_ACL.html): Stores information about default access privileges.
- [PG_EXTERNAL_SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_EXTERNAL_SCHEMA.html): Stores information about external schemas.
- [PG_LIBRARY](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_LIBRARY.html): Stores information about user-defined libraries.
- [PG_PROC_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_PROC_INFO.html): PG_PROC_INFO is an Amazon Redshift system view built on the PostgreSQL catalog table PG_PROC and the internal catalog table PG_PROC_EXTENDED.
- [PG_STATISTIC_INDICATOR](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_STATISTIC_INDICATOR.html): Stores information about the number of rows inserted or deleted since the last ANALYZE.
- [PG_TABLE_DEF](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_TABLE_DEF.html): Stores information about table columns for Amazon Redshift.
- [PG_USER_INFO](https://docs.aws.amazon.com/redshift/latest/dg/pg_user_info.html): PG_USER_INFO is an Amazon Redshift system view that shows user information, such as user ID and password expiration time.

### [Querying the catalog tables](https://docs.aws.amazon.com/redshift/latest/dg/c_join_PG.html)

Query the catalog tables to join catalog tables and views using Amazon Redshift.

- [Examples of catalog queries](https://docs.aws.amazon.com/redshift/latest/dg/c_join_PG_examples.html): Lists examples of how to use catalog queries to get useful information about an Amazon Redshift database.


## [Configuration reference](https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_ConfigurationRef.html)

- [analyze_threshold_percent](https://docs.aws.amazon.com/redshift/latest/dg/r_analyze_threshold_percent.html): Sets the threshold for percentage of rows changed for analyzing a table.
- [cast_super_null_on_error](https://docs.aws.amazon.com/redshift/latest/dg/r_cast_super_null_on_error.html): Specifies that when you try to access a nonexistent member of an object or element of an array, Amazon Redshift returns a NULL value if your query is run in the default lax mode.
- [datashare_break_glass_session_var](https://docs.aws.amazon.com/redshift/latest/dg/r_datashare_break_glass_session_var.html): Applies a permission that allows certain operations that generally aren't recommended for an AWS Data Exchange datashare.
- [datestyle](https://docs.aws.amazon.com/redshift/latest/dg/r_datestyle.html): Sets the display format for date and time values and also the rules for interpreting ambiguous date input values using datestyle.
- [default_array_search_null_handling](https://docs.aws.amazon.com/redshift/latest/dg/r_default_array_search_null_handling.html): Specifies the null handling behavior for array search operations.
- [default_geometry_encoding](https://docs.aws.amazon.com/redshift/latest/dg/r_default_geometry_encoding.html): Specifies if spatial geometries created during a session are encoded with a bounding box.
- [describe_field_name_in_uppercase](https://docs.aws.amazon.com/redshift/latest/dg/r_describe_field_name_in_uppercase.html): Specifies whether column names returned by SELECT statements are uppercase or lowercase.
- [downcase_delimited_identifier](https://docs.aws.amazon.com/redshift/latest/dg/r_downcase_delimited_identifier.html): Enables the super parser to read JSON fields that are in uppercase or mixed-case.
- [enable_case_sensitive_identifier](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_case_sensitive_identifier.html): Activates a configuration value that determines whether name identifiers of databases, schemas, tables, and columns are case sensitive.
- [enable_case_sensitive_super_attribute](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_case_sensitive_super_attribute.html): Activates a configuration value that determines whether users can navigate SUPER data type values in a case-sensitive way without using quotes.
- [enable_numeric_rounding](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_numeric_rounding.html): Specifies whether to use numeric rounding.
- [enable_result_cache_for_session](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_result_cache_for_session.html): Specifies whether to use query results caching.
- [enable_vacuum_boost](https://docs.aws.amazon.com/redshift/latest/dg/r_enable_vacuum_boost.html): Specifies whether to enable the vacuum boost option for all VACUUM commands run in a session.
- [error_on_nondeterministic_update](https://docs.aws.amazon.com/redshift/latest/dg/r_error_on_nondeterministic_update.html): Specifies whether UPDATE queries with multiple matches per row throw an error.
- [extra_float_digits](https://docs.aws.amazon.com/redshift/latest/dg/r_extra_float_digits.html): Sets the number of digits displayed for floating-point values, including float4 and float8 using extra_float_digits.
- [interval_forbid_composite_literals](https://docs.aws.amazon.com/redshift/latest/dg/r_interval_forbid_composite_literals.html): Specifies a session configuration that modifies the value of an interval that contain both YEAR TO MONTH and DAY TO SECOND parts.
- [json_serialization_enable](https://docs.aws.amazon.com/redshift/latest/dg/r_json_serialization_enable.html): Specifies whether to enable the JSON serialization option in a session.
- [json_serialization_parse_nested_strings](https://docs.aws.amazon.com/redshift/latest/dg/r_json_serialization_parse_nested_strings.html): Specifies whether to enable serialization of JSON strings inline in a session.
- [max_concurrency_scaling_clusters](https://docs.aws.amazon.com/redshift/latest/dg/r_max_concurrency_scaling_clusters.html): Sets the maximum number of concurrency scaling clusters allowed when concurrency scaling is enabled.
- [max_cursor_result_set_size](https://docs.aws.amazon.com/redshift/latest/dg/max_cursor_result_set_size.html): The max_cursor_result_set_size Â parameter is no longer in use.
- [mv_enable_aqmv_for_session](https://docs.aws.amazon.com/redshift/latest/dg/r_mv_enable_aqmv_for_session.html): Specifies whether Amazon Redshift can perform automatic query rewriting of materialized views at the session level.
- [navigate_super_null_on_error](https://docs.aws.amazon.com/redshift/latest/dg/r_navigate_super_null_on_error.html): Specifies that when you try to navigate a nonexistent member of an object or element of an array, Amazon Redshift returns a NULL value if your query is run in the default lax mode.
- [parse_super_null_on_error](https://docs.aws.amazon.com/redshift/latest/dg/r_parse_super_null_on_error.html): Specifies that when Amazon Redshift tries to parse a nonexistent member of an object or element of an array, Amazon Redshift returns a NULL value if your query is run in the strict mode.
- [pg_federation_repeatable_read](https://docs.aws.amazon.com/redshift/latest/dg/r_pg_federation_repeatable_read.html): Specifies whether to enable serialization of JSON strings inline in a session.
- [query_group](https://docs.aws.amazon.com/redshift/latest/dg/r_query_group.html): Applies a user-defined label to a group of queries that are run during the same session using query_group.
- [search_path](https://docs.aws.amazon.com/redshift/latest/dg/r_search_path.html): Specifies the order in which schemas are searched when an object is referenced by a simple name with no schema component with search_path.
- [spectrum_enable_pseudo_columns](https://docs.aws.amazon.com/redshift/latest/dg/r_spectrum_enable_pseudo_columns.html): Learn how you can disable the creation of pseudocolumns for a session by setting the spectrum_enable_pseudo_columns configuration parameter to false.
- [enable_spectrum_oid](https://docs.aws.amazon.com/redshift/latest/dg/r_spectrum_enable_spectrum_oid.html): Learn how to disable the $spectrum_oid pseudocolumn by setting the enable_spectrum_oid configuration parameter to false.
- [spectrum_query_maxerror](https://docs.aws.amazon.com/redshift/latest/dg/r_spectrum_query_maxerror.html): Learn how to specify a maximum number of errors to accept before canceling the query.
- [statement_timeout](https://docs.aws.amazon.com/redshift/latest/dg/r_statement_timeout.html): Cancels any statement that exceeds the specified number of milliseconds with statement_timeout.
- [stored_proc_log_min_messages](https://docs.aws.amazon.com/redshift/latest/dg/r_stored_proc_log_min_messages.html): Specifies the minimum logging level of raised messages.
- [timezone](https://docs.aws.amazon.com/redshift/latest/dg/r_timezone_config.html): Sets the time zone for the current session.
- [use_fips_ssl](https://docs.aws.amazon.com/redshift/latest/dg/use_fips_ssl.html): Specifies whether to enable FIPS-compliant SSL mode.
- [wlm_query_slot_count](https://docs.aws.amazon.com/redshift/latest/dg/r_wlm_query_slot_count.html): Sets the number of query slots that a query uses with wlm_query_slot_count.
