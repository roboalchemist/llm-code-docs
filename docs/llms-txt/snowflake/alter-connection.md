# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-connection.md

# ALTER CONNECTION

Modifies the properties for an existing [connection](../../user-guide/client-redirect.md).

See also:
:   [CREATE CONNECTION](create-connection.md) , [DROP CONNECTION](drop-connection.md) , [SHOW CONNECTIONS](show-connections.md)

## Syntax

```sqlsyntax
ALTER CONNECTION [ IF EXISTS ] <name> ENABLE FAILOVER TO ACCOUNTS <organization_name>.<account_name> [ , <organization_name>.<account_name> ... ]
                        [ IGNORE EDITION CHECK ]

ALTER CONNECTION [ IF EXISTS ] <name> DISABLE FAILOVER [ TO ACCOUNTS <organization_name>.<account_name> [ , <organization_name>.<account_name> ... ] ]

ALTER CONNECTION [ IF EXISTS ] <name> PRIMARY

ALTER CONNECTION [ IF EXISTS ] <name> SET COMMENT = '<string_literal>'

ALTER CONNECTION [ IF EXISTS ] <name> UNSET COMMENT
```

## Parameters

`name`
:   Identifier for the connection to alter.

`ENABLE FAILOVER TO ACCOUNTS organization_name.account_name [ , organization_name.account_name ... ]`
:   Specifies a comma-separated list of accounts in your organization where a secondary connection for this primary connection can be
    promoted to serve as the primary connection. Include your organization name for each account in the list.

    Each account in the list must be located in a different region than the account with the primary connection. Otherwise,
    the command fails.

`DISABLE FAILOVER [ TO ACCOUNTS organization_name.account_name [ , organization_name.account_name ... ] ]`
:   Disables failover for this primary connection, meaning no secondary connection for this primary connection can be promoted to serve as the primary
    connection.

    To disable failover to selected accounts (rather than to all accounts), specify a comma-delimited list of those accounts.

`PRIMARY`
:   Promote connection to serve as primary connection.

`SET ...`
:   Specifies the properties to set for the connection:

    `COMMENT = 'string'`
    :   Adds a comment or overwrites an existing comment for the connection.

`UNSET ...`
:   Specifies the properties to unset for the connection, which resets them to the defaults.

    Currently, the only property you can unset is `COMMENT`, which removes the comment, if one exists, for the connection.

## Usage notes

* Only account administrators (users with the ACCOUNTADMIN role) can execute this SQL command.
* If private connectivity to the Snowflake service is enabled for your Snowflake account, your network administrator must update the
  DNS CNAME record for your connection URL when a connection is promoted to serve as the primary connection. For more information, see
  [Configuring the DNS settings for private connectivity to the Snowflake service](../../user-guide/client-redirect.md).
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Allow accounts `myaccount2` and `myaccount3` in the `myorg` organization to each store a secondary connection for the
`myconnection` connection:

```sqlexample
ALTER CONNECTION myconnection ENABLE FAILOVER TO ACCOUNTS myorg.myaccount2, myorg.myaccount3;
```

Add a comment for a connection:

```sqlexample
ALTER CONNECTION myconnection SET COMMENT = 'New comment for connection';
```

Promote a secondary connection to primary connection:

```sqlexample
ALTER CONNECTION myconnection PRIMARY;
```
