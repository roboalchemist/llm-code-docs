# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-sequence-number.md

# ALTER APPLICATION … { APPROVE | DECLINE} SPECIFICATION

Approves or declines an [app specification](../../developer-guide/native-apps/requesting-app-specs.md)
using the specified sequence number.

See also:
:   [ALTER APPLICATION SET SPECIFICATION](alter-application-set-app-spec.md), [ALTER APPLICATION DROP SPECIFICATION](alter-application-drop-app-spec.md)

## Syntax

```sqlsyntax
ALTER APPLICATION <app_name>
  { APPROVE | DECLINE } SPECIFICATION <spec_name>
  SEQUENCE_NUMBER = <sequence_num>;
```

## Parameters

`app_name`
:   Specifies the identifier for the app being altered. If the identifier contains spaces, special characters, or
    mixed-case characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double
    quotes are also case-sensitive.

`APPROVE | DECLINE SPECIFICATION spec_name`
:   Approves or declines the specified app specification.

`SEQUENCE_NUMBER = sequence_num`
:   Specifies the sequence number of the app specification to approve. The sequence number represents a
    version id of the app specification. The sequence number starts at 1 when the specification is created.
    The value is incremented each time the provider updates the app specification. Use
    [SHOW SPECIFICATIONS](show-specifications.md) or
    [DESCRIBE SPECIFICATION](desc-specification.md) commands to determine the current sequence number of
    the app.

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| MANAGE APPLICATION SPECIFICATIONS | Account | Allows a role to approve or decline app specifications for any app in their account. Only the SECURITYADMIN and ACCOUNTADMIN system roles have the MANAGE APPLICATION SPECIFICATIONS privilege; however, the privilege can be granted to custom roles. |
