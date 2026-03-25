# Source: https://docs.snowflake.com/en/sql-reference/functions/is_granted_to_invoker_role.md

Categories:
:   [Context functions](../functions-context.md) (Session Object)

# IS_GRANTED_TO_INVOKER_ROLE

Returns TRUE if the role returned by the INVOKER_ROLE function inherits the privileges of the specified role in the argument based on the
context in which the function is called.

The INVOKER_ROLE function only identifies and returns the account role of the object executing a SQL statement. Database roles are not
supported.

## Syntax

```sqlsyntax
IS_GRANTED_TO_INVOKER_ROLE( '<string_literal>' )
```

## Arguments

`'string_literal'`
:   The name of the role.

## Usage notes

* If using the IS_GRANTED_TO_INVOKER_ROLE function with [masking policy](../../user-guide/security-column-intro.md) or a
  [row access policy](../../user-guide/security-row-intro.md), verify that your Snowflake account is Enterprise Edition or higher.
* Only one role name can be passed as an argument.
* The following table summarizes the context in which you can call the function and the role hierarchy Snowflake evaluates.

  | Context | Evaluated role |
  | --- | --- |
  | User | [CURRENT_ROLE](current_role.md) |
  | Table | CURRENT_ROLE. |
  | View | View owner role. |
  | UDF | UDF owner role. |
  | Stored procedure with caller’s right | CURRENT_ROLE. |
  | Stored procedure with owner’s right | Stored procedure owner role. |
  | Task | Task owner role. |
  | Stream | The role that queries a given [stream](../../user-guide/streams-intro.md). |

* If prefer to evaluate the role hierarchy for the current session, call [IS_ROLE_IN_SESSION](is_role_in_session.md) instead.

## Example

Call the function directly:

> ```sqlexample
> IS_GRANTED_TO_INVOKER_ROLE('ANALYST')
>
> --------------------------------------+
> IS_GRANTED_TO_INVOKER_ROLE('ANALYST') |
> --------------------------------------+
>                 TRUE                  |
> --------------------------------------+
> ```

Specify the function in the masking policy body:

```sqlexample
CREATE OR REPLACE MASKING POLICY mask_string AS
(val string) RETURNS string ->
CASE
  WHEN IS_GRANTED_TO_INVOKER_ROLE('ANALYST') then val
  ELSE '*******'
END;
```
