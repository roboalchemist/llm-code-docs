# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-procedure.md

# ALTER PROCEDURE

Modifies the properties for an existing stored procedure. If you need to make any changes not supported here, use [DROP PROCEDURE](drop-procedure.md)
instead and then recreate the stored procedure.

See also:
:   [CREATE PROCEDURE](create-procedure.md) , [DROP PROCEDURE](drop-procedure.md) , [SHOW PROCEDURES](show-procedures.md) , [DESCRIBE PROCEDURE](desc-procedure.md), [SHOW USER PROCEDURES](show-user-procedures.md)

## Syntax

The syntax for ALTER PROCEDURE varies depending on which language you’re using as the UDF handler.

### Java handler

```sqlsyntax
ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) RENAME TO <new_name>

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET
  [ LOG_LEVEL = '<log_level>' ]
  [ TRACE_LEVEL = '<trace_level>' ]
  [ EXTERNAL_ACCESS_INTEGRATIONS = '<integration_name>' [ , '<integration_name>' ... ] ]
  [ SECRETS = '<secret_variable_name>' = <secret_name> [ , '<secret_variable_name>' = <secret_name> ... ] ]
  [ COMMENT = '<string_literal>' ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET COMMENT

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) EXECUTE AS { OWNER | CALLER | RESTRICTED CALLER }
```

### JavaScript handler

```sqlsyntax
ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) RENAME TO <new_name>

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET
  [ LOG_LEVEL = '<log_level>' ]
  [ TRACE_LEVEL = '<trace_level>' ]
  [ COMMENT = '<string_literal>' ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET COMMENT

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) EXECUTE AS { OWNER | CALLER | RESTRICTED CALLER }
```

### Python handler

```sqlsyntax
ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) RENAME TO <new_name>

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET
  [ LOG_LEVEL = '<log_level>' ]
  [ TRACE_LEVEL = '<trace_level>' ]
  [ EXTERNAL_ACCESS_INTEGRATIONS = '<integration_name>' [ , '<integration_name>' ... ] ]
  [ SECRETS = '<secret_variable_name>' = <secret_name> [ , '<secret_variable_name>' = <secret_name> ... ] ]
  [ COMMENT = '<string_literal>' ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET COMMENT

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) EXECUTE AS { OWNER | CALLER | RESTRICTED CALLER }
```

### Scala handler

```sqlsyntax
ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) RENAME TO <new_name>

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET
  [ LOG_LEVEL = '<log_level>' ]
  [ TRACE_LEVEL = '<trace_level>' ]
  [ EXTERNAL_ACCESS_INTEGRATIONS = '<integration_name>' [ , '<integration_name>' ... ] ]
  [ SECRETS = '<secret_variable_name>' = <secret_name> [ , '<secret_variable_name>' = <secret_name> ... ] ]
  [ COMMENT = '<string_literal>' ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET COMMENT

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) EXECUTE AS { OWNER | CALLER | RESTRICTED CALLER }
```

### Snowflake Scripting handler

```sqlsyntax
ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) RENAME TO <new_name>

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET
  [ AUTO_EVENT_LOGGING = '<option>' ]
  [ LOG_LEVEL = '<log_level>' ]
  [ TRACE_LEVEL = '<trace_level>' ]
  [ COMMENT = '<string_literal>' ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET COMMENT

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER PROCEDURE [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] ) EXECUTE AS { OWNER | CALLER | RESTRICTED CALLER }
```

## Parameters

`name`
:   Specifies the identifier for the stored procedure to alter. If the identifier contains spaces or special characters, the entire string must be
    enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`arg_data_type [ , ... ]`
:   Specifies the data type of the argument(s) for the stored procedure, if it has arguments. The argument types are required because stored
    procedures support name overloading (i.e. two stored procedures in the same schema can have the same name) and the argument types are used to
    identify the procedure you wish to alter.

`RENAME TO new_name`
:   Specifies the new identifier for the stored procedure; the combination of the identifier and existing argument data types must be unique for
    the schema.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

    You can move the object to a different database and/or schema while optionally renaming the object. To do so, specify
    a qualified `new_name` value that includes the new database and/or schema name in the form
    `db_name.schema_name.object_name` or `schema_name.object_name`, respectively.

    > **Note:**
    >
    > * The destination database and/or schema must already exist. In addition, an object with the same name cannot already
    >   exist in the new location; otherwise, the statement returns an error.
    > * Moving an object to a managed access schema is prohibited unless the object owner (that is, the role that has
    >   the OWNERSHIP privilege on the object) also owns the target schema.

    When an object is renamed, other objects that reference it must be updated with the new name.

`SET ...`
:   Specifies the properties to set for the stored procedure.

    `AUTO_EVENT_LOGGING = 'option'`
    :   (For Snowflake Scripting stored procedures only) Controls whether additional Snowflake Scripting log messages and trace events are
        ingested automatically into the [event table](../../developer-guide/logging-tracing/event-table-setting-up.md).

        For information about the options, see [AUTO_EVENT_LOGGING](../parameters.md).

    `LOG_LEVEL = 'log_level'`
    :   Specifies the severity level of messages that should be ingested and made available in the active event table. Messages at
        the specified level (and at more severe levels) are ingested.

        For more information about levels, see [LOG_LEVEL](../parameters.md). For information about setting log level, see
        [Setting levels for logging, metrics, and tracing](../../developer-guide/logging-tracing/telemetry-levels.md).

    `TRACE_LEVEL = 'trace_level'`
    :   Controls how trace events are ingested into the event table.

        For information about levels, see [TRACE_LEVEL](../parameters.md). For information about setting trace level, see
        [Setting levels for logging, metrics, and tracing](../../developer-guide/logging-tracing/telemetry-levels.md).

    `EXTERNAL_ACCESS_INTEGRATIONS = ( integration_name [ , ... ] )`
    :   The names of [external access integrations](create-external-access-integration.md) needed in order for this
        procedure’s handler code to access external networks.

        An external access integration contains [network rules](create-network-rule.md) and
        [secrets](create-secret.md) that specify the external locations and credentials (if any) needed for handler code
        to make requests of an external network, such as an external REST API.

        For more information, refer to [External network access overview](../../developer-guide/external-network-access/external-network-access-overview.md).

    `SECRETS = ( 'secret_variable_name' = secret_name [ , ...  ] )`
    :   Assigns the names of secrets to variables so that you can use the variables to reference the secrets when retrieving information from
        secrets in handler code.

        This parameter’s value is a list of assignment expressions with the following parts:

        * `secret_name` as the name of a secret specified in an
          [external access integration’s](create-external-access-integration.md) ALLOWED_AUTHENTICATION_SECRETS parameter
          value. That external access integration’s name must, in turn, be specified as a value of this CREATE PROCEDURE call’s
          EXTERNAL_ACCESS_INTEGRATIONS parameter.

          You will receive an error if you specify a SECRETS value whose secret isn’t also included in an integration specified by the
          EXTERNAL_ACCESS_INTEGRATIONS parameter.
        * `'secret_variable_name'` as the variable that will be used in handler code when retrieving information from the secret.

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites the existing comment for the stored procedure. The value you specify is displayed in the `DESCRIPTION`
        column in the output for [SHOW PROCEDURES](show-procedures.md).

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`UNSET ...`
:   Specifies the properties to unset for the stored procedure, which resets them to the defaults.

    Currently, the only properties you can unset are:

    * `COMMENT`, which removes the comment, if any, for the procedure.
    * `TAG tag_name [ , tag_name ... ]`

`EXECUTE AS { OWNER | CALLER | RESTRICTED CALLER }`
:   [Preview Feature](../../release-notes/preview-features.md) — Open

    Restricted caller’s rights (`EXECUTE AS RESTRICTED CALLER`) is a preview feature available to all accounts.

    Specifies whether the stored procedure executes with the privileges of the owner (an “owner’s rights” stored procedure) or with
    the privileges of the caller (a “caller’s rights” stored procedure):

    * If you execute ALTER PROCEDURE … EXECUTE AS OWNER, then in the future the procedure will execute as an owner’s rights procedure.
    * If you execute the statement ALTER PROCEDURE … EXECUTE AS CALLER, then in the future the procedure will execute as a
      caller’s rights procedure.
    * If you execute the statement ALTER PROCEDURE … EXECUTE AS RESTRICTED CALLER, then in the future the procedure will execute as a
      caller’s rights procedure, but might not be able to run with all of the caller’s privileges. For more information, see
      [Restricted caller’s rights](../../developer-guide/restricted-callers-rights.md).

    If `EXECUTE AS ...` isn’t specified, the procedure runs as an owner’s rights stored procedure. Owner’s rights stored
    procedures have less access to the caller’s environment (for example, the caller’s session variables), and Snowflake defaults to this
    higher level of privacy and security.

    For more information, see [Understanding caller’s rights and owner’s rights stored procedures](../../developer-guide/stored-procedure/stored-procedures-rights.md).

    Default: `EXECUTE AS OWNER`

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Rename stored procedure `procedure1` to `procedure2`:

> ```sqlexample
> ALTER PROCEDURE IF EXISTS procedure1(FLOAT) RENAME TO procedure2;
> ```
