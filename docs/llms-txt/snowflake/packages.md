# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/oracle/pl-sql-to-snowflake-scripting/packages.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/packages.md

# PACKAGES view

This Information Schema view displays a row for each Snowpark package version supported for use in the PACKAGES clause in the
[CREATE FUNCTION](../sql/create-function.md) and [CREATE PROCEDURE](../sql/create-procedure.md) commands. For Python, this view also displays a
row for each version of a third-party package that you can install. For details, see
[Using third-party packages](../../developer-guide/udf/python/udf-python-packages.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| PACKAGE_NAME | VARCHAR | The name of the package |
| VERSION | VARCHAR | The version number of the package |
| LANGUAGE | VARCHAR | The programming language for the package |

## Usage notes

Currently, the package versions with the following are supported:

* `language = java`
* `language = python`
* `language = scala`
