# Source: https://docs.snowflake.com/en/sql-reference/info-schema/model_versions.md

# MODEL_VERSIONS view

This Information Schema view displays a row for each machine learning model version defined in the specified (or current) database.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| DATABASE_NAME | TEXT | Database to which the model version belongs. |
| SCHEMA_NAME | TEXT | Schema to which the model version belongs. |
| MODEL_NAME | TEXT | Model to which the model version belongs. |
| MODEL_VERSION_NAME | TEXT | Name of the model version. |
| VERSION_ALIASES | ARRAY | List of aliases of the model version. |
| COMMENT | TEXT | Comment for the model version. |
| OWNER | TEXT | Name of the role that owns the model version. |
| CREATED | TIMESTAMP_LTZ | Date and time when model version was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time when the model version was last updated. |
| FUNCTIONS | TEXT | Functions in the model version. |
| MODEL_TYPE | TEXT | Type of the model to which the model version belongs. |
| PYTHON_VERSION | TEXT | Version of Python required by the model version. |
| LANGUAGE | TEXT | Language in which the model version is implemented. |
| DEPENDENCIES | TEXT | Dependencies of the model version. |
| METADATA | TEXT | Metadata of the model version. |
| USERDATA | TEXT | User data of the model version. |

## Usage notes

* The view only displays objects for which the current role for the session has been granted access privileges.
* The view does not include model versions that have been dropped.

## Examples

Retrieve the names of all model versions, functions, and the model they belong to, in the `mydatabase` database:

```sqlexample
SELECT model_version_name, model_name, functions, schema_name, database_name
    FROM mydatabase.INFORMATION_SCHEMA.MODEL_VERSIONS;
```
