# Source: https://docs.snowflake.com/en/sql-reference/functions/system_evaluate_data_quality_expectations.md

Categories:
:   [System functions](../functions-system.md), [Table functions](../functions-table.md)

# SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS

Returns the [expectations](../../user-guide/data-quality-expectations.md) for associations between data metric functions (DMFs) and a table,
including whether an expectation is currently violated.

## Syntax

```sqlsyntax
SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS(
  REF_ENTITY_NAME  => '<object>'
  [ , SKIP_SUSPENDED_DMF => { TRUE | FALSE } ] )
```

## Arguments

`REF_ENTITY_NAME => 'object'`
:   Name of the table or view that has at least one DMF with one or more expectations. Must be fully qualified.

`SKIP_SUSPENDED_DMF => { TRUE | FALSE }`
:   If set to TRUE, the function doesn’t return expectations that are defined for associations between the `object` and suspended
    DMFs. A suspended DMF doesn’t run on the object’s specified schedule.

    Default: TRUE

## Returns

Returns a table with the following columns:

| Column | Data type | Description |
| --- | --- | --- |
| `metric_database` | VARCHAR | Name of the database that contains the DMF. |
| `metric_schema` | VARCHAR | Name of the schema that contains the DMF. |
| `metric_name` | VARCHAR | Name of the DMF. |
| `expectation_name` | VARCHAR | Name that the user assigned the expectation when adding it to the association between the DMF and the table. |
| `expectation_id` | NUMBER | System-generated identifier. |
| `expectation_expression` | VARCHAR | Boolean expression of the expectation. See [Defining what meets the expectation](../../user-guide/data-quality-expectations.md). |
| `arguments` | ARRAY | Columns with which the DMF is associated. |
| `value` | VARIANT | The result of the DMF evaluation. |
| `expectation_violated` | BOOLEAN | If TRUE, the expectation was violated. An expectation is violated when the `expectation_expression` evaluates to FALSE. |

## Access control privileges

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| SELECT | Table or view |  |
| USAGE | Data metric function (DMF) |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Example

Return the expectations for the associations between DMFs AND table `t1`. The DMFs are executed to determine if the expectations are
currently violated.

```sqlexample
SELECT *
  FROM TABLE(SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS(
      REF_ENTITY_NAME => 'my_db.sch.t1'));
```
