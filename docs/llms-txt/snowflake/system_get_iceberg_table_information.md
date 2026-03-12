# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_iceberg_table_information.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_ICEBERG_TABLE_INFORMATION

Returns the location of the root metadata file and status of the latest snapshot for an [Apache Iceberg™ table](../../user-guide/tables-iceberg.md).

The SYSTEM$GET_ICEBERG_TABLE_INFORMATION function works differently according to table type:

* For Snowflake-managed Iceberg tables or Delta-based tables, calling the function generates metadata for data manipulation language (DML)
  operations or other table updates that have occurred since Snowflake last generated metadata for the table.

  If there are no updates, the function returns the location of the latest metadata file,
  but does not generate new metadata.
* For other externally managed Iceberg tables, the function returns information about the latest refreshed snapshot.

## Syntax

```sqlsyntax
SYSTEM$GET_ICEBERG_TABLE_INFORMATION('<iceberg_table_name>')
```

## Arguments

`'iceberg_table_name'`
:   The name of the Iceberg table for which you want to retrieve information. The table name is a string, so it must be enclosed in single
    quotes.

    * If the Iceberg table name is fully qualified, such as `'<db>.<schema>.<iceberg_table_name>'`,
      the entire name must be enclosed in single quotes, including the database and schema.
    * If the Iceberg table name is case-sensitive or includes any special characters or spaces,
      double quotes are required to process the case/characters.
      The double quotes must be enclosed within the single quotes, for example, `'"<case_sensitive_iceberg_table_name>"'`.

## Returns

The function returns a JSON object containing the following name/value pairs:

> {“metadataLocation”:”<value>”,”status”:”<value>”}

Where:

> `metadataLocation`
> :   Location of the root metadata file updated or retrieved by the function.
>
> `status`
> :   Status of the operation. This field returns a success or failure message.

## Usage notes

* Calling this function requires a role that has the OWNERSHIP privilege on the Iceberg table.

## Examples

Generate a snapshot for the Iceberg table `it1` in the schema `db1.schema1`:

```sqlexample
SELECT SYSTEM$GET_ICEBERG_TABLE_INFORMATION('db1.schema1.it1');
```

Output:

```output
+-----------------------------------------------------------------------------------------------------------+
| SYSTEM$GET_ICEBERG_TABLE_INFORMATION('DB1.SCHEMA1.IT1')                                                   |
|-----------------------------------------------------------------------------------------------------------|
| {"metadataLocation":"s3://mybucket/metadata/v1.metadata.json","status":"success"}                         |
+-----------------------------------------------------------------------------------------------------------+
```
