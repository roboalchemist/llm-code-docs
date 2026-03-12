# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-mcp-server.md

# DROP MCP SERVER

Removes the specified MCP (Model Context Protocol) server from the current/specified schema.

See also:
:   [CREATE MCP SERVER](create-mcp-server.md) , [DESCRIBE MCP SERVER](desc-mcp-server.md) , [SHOW MCP SERVERS](show-mcp-servers.md)

## Syntax

```sqlsyntax
DROP MCP SERVER [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the MCP server to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object |
| --- | --- |
| OWNERSHIP or MODIFY | MCP server |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage Notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

* Dropping an MCP server removes the server object and its tool configurations. Any MCP clients currently connected to the server will lose access.
* The underlying objects referenced by the MCP server tools (Cortex Search Services, Cortex Agents, UDFs, stored procedures) are not affected by dropping the MCP server.

## Examples

The following example drops the MCP server named `my_mcp_server`:

```sqlexample
DROP MCP SERVER my_mcp_server;
```

```output
+----------------------------------------+
| status                                 |
|----------------------------------------|
| MY_MCP_SERVER successfully dropped.    |
+----------------------------------------+
```

The following example drops the MCP server named `my_mcp_server` if it exists:

```sqlexample
DROP MCP SERVER IF EXISTS my_mcp_server;
```
