# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-dataset-drop-version.md

# ALTER DATASET … DROP VERSION

Drops a dataset version.

See also:
:   [ALTER DATASET](alter-dataset.md) , [ALTER DATASET … ADD VERSION](alter-dataset-add-version.md)

## Syntax

```sqlsyntax
ALTER DATASET [ IF EXISTS ] <name> DROP VERSION <version_name>
```

## Parameters

`name`
:   The name of the dataset that you’re dropping.

`DROP VERSION version_name`
:   The name of the dataset version that you’re dropping.

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

The following example drops version `v1` of the `my_dataset` dataset:

```sqlexample
ALTER DATASET my_dataset
DROP VERSION 'v1';
```
