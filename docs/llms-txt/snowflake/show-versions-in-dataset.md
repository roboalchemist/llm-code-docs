# Source: https://docs.snowflake.com/en/sql-reference/sql/show-versions-in-dataset.md

# SHOW VERSIONS IN DATASET

Displays information about the datasets in your account at either the schema or database level.

See also:
:   [SHOW DATASETS](show-datasets.md) , [ALTER DATASET](alter-dataset.md), [CREATE DATASET](create-dataset.md)

## Syntax

```sqlsyntax
SHOW VERSIONS [ LIKE '<pattern>' ] IN DATASET <dataset_name>
  [ LIMIT <rows>]
```

## Parameters

`IN DATASET dataset_name`
:   Name of dataset for which versions are displayed.

`LIKE pattern`
:   Restricts the list of returned datasets to those matching the specified pattern. Matching is case-insensitive.

`LIMIT num`
:   Limits the maximum number of rows returned.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP or USAGE | Dataset | Provides the privilege to show the dataset versions within the account. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).
