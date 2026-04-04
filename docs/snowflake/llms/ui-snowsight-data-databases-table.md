# Source: https://docs.snowflake.com/en/user-guide/ui-snowsight-data-databases-table.md

# Working with tables in Snowsight

You can work with [tables](../guides-overview-db.md) in SQL or using Snowsight.
For details about the available SQL commands for working with tables, see [Table, view, & sequence DDL](../sql-reference/ddl-table.md)

In Snowsight, in the navigation menu, select Catalog » Database Explorer, and then search for or browse to the table.
Select the table to do any of the following:

* Explore details about the table and the columns defined in the table.
* Preview the data in the table.
* [Load data into the table from files](data-load-web-ui.md).
* Monitor the data loading activity for the table using the [table-level Copy History](data-load-monitor.md).

> **Note:**
>
> To work with tables in Snowsight, you must use a role with the relevant [table privileges](security-access-control-privileges.md).

## Explore table details in Snowsight

After opening a table in Snowsight, you can review the table name and the database and schema that contain the table.

You can also review the following details:

* The type of table
* The owner role of the table
* When the table was created. Hover over the time to see the exact date and time.
* The number of rows in the table
* The size of the table. For example, 2.5 KB for a very small table.

You can review the SQL definition for the table on the Table Details tab in the Table definition section.
The Columns tab provides information about the columns in the table. Use the Search option to find columns by name.

Manage privileges for the table in the Privileges section of the Table Details tab.
See [Manage object privileges with Snowsight](security-access-control-configure.md).

## Manage a table in Snowsight

You can perform the following basic management tasks for a table in Snowsight:

* To edit the table name or add a comment, select  » Edit.
* To clone the table, select  » Clone.
* To drop the table, select  » Drop.
* To transfer ownership of the table to another role, select  » Transfer Ownership.
* To [load data into the table from files](data-load-web-ui.md), select Load Data.

## Preview data in a table

The Data Preview tab provides a preview of up to the first 100 rows of the table.

Select  to manipulate the preview data:

* Sort the data in ascending or descending order.
* Increase or decrease the decimal precision.
* Show thousands separators in numbers.
* Display the data in the column as percentages.

The options available to you depend on the type of data in the column.

> **Note:**
>
> The preview requires a warehouse. By default, Snowsight uses the default warehouse for your user profile, or you can select
> a different warehouse.
