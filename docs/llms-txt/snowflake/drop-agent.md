# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-agent.md

# DROP AGENT

Removes the specified [Cortex Agent](../../user-guide/snowflake-cortex/cortex-agents.md) with the specified name from the current or specified database and schema.

See also:
:   [ALTER AGENT](alter-agent.md), [CREATE AGENT](create-agent.md), [DESCRIBE AGENT](desc-agent.md), [SHOW AGENTS](show-agents.md), [DATA_AGENT_RUN (SNOWFLAKE.CORTEX)](../functions/data_agent_run-snowflake-cortex.md)

## Syntax

```sqlsyntax
DROP AGENT [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the Cortex Agent to be dropped.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Agent |  |
| MODIFY | Agent |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

The following example drops the agent named `my_agent` in the current schema:

```sqlexample
DROP AGENT my_agent;
```

The following example drops the agent named `my_agent` in the `mydb` database and `myschema` schema. This command fails if the agent does not exist:

```sqlexample
DROP AGENT mydb.myschema.my_agent;
```

The following example drops the agent named `my_agent` in the `mydb` database and `myschema` schema only if it exists:

```sqlexample
DROP AGENT IF EXISTS mydb.myschema.my_agent;
```
