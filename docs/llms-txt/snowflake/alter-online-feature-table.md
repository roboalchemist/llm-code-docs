# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-online-feature-table.md

# ALTER ONLINE FEATURE TABLE

Modifies the properties of an existing [online feature table](create-online-feature-table.md).

See also:
:   [CREATE ONLINE FEATURE TABLE](create-online-feature-table.md) , [DESCRIBE ONLINE FEATURE TABLE](desc-online-feature-table.md), [DROP ONLINE FEATURE TABLE](drop-online-feature-table.md) , [SHOW ONLINE FEATURE TABLES](show-online-feature-tables.md)

## Syntax

```sqlsyntax
ALTER ONLINE FEATURE TABLE [ IF EXISTS ] <name> { SUSPEND | RESUME }

ALTER ONLINE FEATURE TABLE [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER ONLINE FEATURE TABLE [ IF EXISTS ] <name> REFRESH

ALTER ONLINE FEATURE TABLE [ IF EXISTS ] <name> SET COMMENT = '<string_literal>'

ALTER ONLINE FEATURE TABLE [ IF EXISTS ] <name> SET
  [ TARGET_LAG = '<num> { seconds | minutes | hours | days }' ]
  [ WAREHOUSE = <warehouse_name> ]

ALTER ONLINE FEATURE TABLE [ IF EXISTS ] <name> <tagAction>
```

## Parameters

`name`
:   Specifies the identifier for the online feature table to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`RENAME TO new_name`
:   Changes the name of the online feature table to `new_name`. The new identifier must be unique for the schema.

    For more details about identifiers, see [Identifier requirements](../identifiers-syntax.md).

    When an object is renamed, other objects that reference it must be updated with the new name.

`SUSPEND | RESUME`
:   Specifies whether the periodic background refreshes of the data in the table are suspended or resumed.

    `SUSPEND`
    :   Suspends the periodic background refreshes of the online feature table.

    `RESUME`
    :   Resumes the periodic background refreshes of the online feature table.

`REFRESH`
:   Specifies that the online feature table must be manually refreshed.

`SET ...`
:   Sets one or more specified properties or parameters for the online feature table:

    `TARGET_LAG = 'num { seconds | minutes | hours | days }'`
    :   Specifies the new target lag to use to define the schedule of the background refreshes.

        Must be a value between 10 seconds and 8 days, inclusive.

    `WAREHOUSE = warehouse_name`
    :   Specifies the name of the new warehouse that provides the compute resources for refreshing the online feature table.

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the online feature table.

`tagAction`
:   Sets or unsets the tag on the online feature table:

    ```sqlsyntax
    tagAction ::=
      {
          SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]
        | UNSET TAG <tag_name> [ , <tag_name> ... ]
      }
    ```

    `SET TAG`
    :   Sets the specified tag and tag value on the online feature table.

    `UNSET TAG`
    :   Unsets the specified tag on the online feature table.

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Online feature table | Role that has the OWNERSHIP privilege on the online feature table. |
| USAGE | Warehouse | Required when changing the warehouse |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example suspends the periodic background refreshes for the online feature table named `my_online_feature_table`:

```sqlexample
ALTER ONLINE FEATURE TABLE my_online_feature_table SUSPEND;
```

The following example manually refreshes the online feature table named `my_online_feature_table`:

```sqlexample
ALTER ONLINE FEATURE TABLE my_online_feature_table REFRESH;
```

The following example changes the target lag for the online feature table named `my_online_feature_table`:

```sqlexample
ALTER ONLINE FEATURE TABLE my_online_feature_table SET TARGET_LAG = '1 minute';
```

The following example changes the name of the online feature table `my_online_feature_table` to `my_new_online_feature_table`:

```sqlexample
ALTER ONLINE FEATURE TABLE my_online_feature_table RENAME TO my_new_online_feature_table;
```
