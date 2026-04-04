# Source: https://docs.snowflake.com/en/user-guide/data-load-local-file-system.md

# Bulk loading from a local file system

This set of topics describes how to use the COPY command to bulk load data from a local file system into tables using an internal (i.e.
Snowflake-managed) stage. For instructions on loading data from a cloud storage location that you manage, refer to [Bulk loading from Amazon S3](data-load-s3.md), [Bulk loading from Google Cloud Storage](data-load-gcs.md), or [Bulk loading from Microsoft Azure](data-load-azure.md).

As illustrated in the diagram below, loading data from a local file system is performed in two, separate steps:

Step 1:
:   Upload (i.e. stage) one or more data files to a Snowflake stage (named internal stage or table/user stage) using the [PUT](../sql-reference/sql/put.md) command.

Step 2:
:   Use the [COPY INTO <table>](../sql-reference/sql/copy-into-table.md) command to load the contents of the staged file(s) into a Snowflake database table.

    Regardless of the stage you use, this step requires a running virtual warehouse that is also the current (i.e. in use) warehouse for the session. The warehouse provides the compute resources to
    perform the actual insertion of rows into the table.

> **Tip:**
>
> The instructions in this set of topics assume you have read [Preparing to load data](data-load-prepare.md) and have created a named file format, if desired.
>
> Before you begin, you may also want to read [Data loading considerations](data-load-considerations.md) for best practices, tips, and other guidance.

**Next Topics:**

* **Configuration tasks (complete as needed):**

  * [Choosing an internal stage for local files](data-load-local-file-system-create-stage.md)
* **Data loading tasks (complete for each set of files you load):**

  * [Staging data files from a local file system](data-load-local-file-system-stage.md)
  * [Copy data from an internal stage](data-load-local-file-system-copy.md)
