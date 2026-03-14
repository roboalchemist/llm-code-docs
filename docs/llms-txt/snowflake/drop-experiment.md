# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-experiment.md

# DROP EXPERIMENT

Removes the specified [experiment](../../developer-guide/snowflake-ml/experiments.md) from the current/specified schema.

See also:
:   [CREATE EXPERIMENT](create-experiment.md) , [ALTER EXPERIMENT](alter-experiment.md) , [SHOW EXPERIMENTS](show-experiments.md) , [SHOW RUNS IN EXPERIMENT](show-runs-in-experiment.md) , [SHOW RUN … IN EXPERIMENT](show-run-in-experiment.md)

## Syntax

```sqlsyntax
DROP EXPERIMENT <name>;
```

## Parameters

`name`
:   Specifies the identifier for the experiment to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Experiment |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).
