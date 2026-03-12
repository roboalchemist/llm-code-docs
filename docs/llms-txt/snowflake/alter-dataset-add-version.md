# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-dataset-add-version.md

# ALTER DATASET … ADD VERSION

Adds a version to a dataset. When you add a version, you can specify properties such as partitioning, comments, or custom metadata.

See also:
:   [ALTER DATASET](alter-dataset.md) , [ALTER DATASET … DROP VERSION](alter-dataset-drop-version.md)

## Syntax

```sqlsyntax
ALTER DATASET <name> ADD VERSION <version_name>
  FROM <select_statement>
  [ PARTITION BY <string_expr> ]
  [ COMMENT = <string_literal> ]
  [ METADATA = <json_string_literal> ]
```

## Parameters

`name`
:   The name of the dataset that you’re altering.

`ADD VERSION version_name`
:   The name of the new dataset version that you’re creating.

`FROM select_statement`
:   The SQL statement that defines the data for the new dataset version.

`PARTITION BY string_expr`
:   The partitioning expression for the new dataset version.

`COMMENT = string_literal`
:   A comment for the new dataset version.

`METADATA = json_string_literal`
:   A JSON string containing metadata for the new dataset version.
    The following is an example of a JSON string.

    ```json
    {"source": "my_table", "job_id": "123"}
    ```

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Dataset | Provides the privilege to both read and modify the dataset. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

The following example adds version `v1` to the `abc` dataset with partitioning:

```sqlexample
ALTER DATASET abc
ADD VERSION 'v1' FROM (
    SELECT seq4() as ID, uniform(1, 10, random(721)) as PART
    FROM TABLE(GENERATOR(ROWCOUNT => 100000)) v)
PARTITION BY PART
COMMENT = 'Initial version'
METADATA = '{"source":"some_table","created_by":"analyst1"}';
```
