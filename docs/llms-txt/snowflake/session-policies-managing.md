# Source: https://docs.snowflake.com/en/user-guide/session-policies-managing.md

# Managing session policies

This topic describes Snowflake sessions and session policies and provides instructions for configuring session policies at the account or
user level.

## Session policy privileges

Snowflake supports the following session policy privileges to determine whether users can create, set, and own session policies.

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

| Privilege | Usage |
| --- | --- |
| CREATE SESSION POLICY | Enables creating a new session policy in a schema. |
| APPLY SESSION POLICY | Enables applying any session policy at the account or user level. |
| OWNERSHIP | Grants full control over the session policy. Required to alter most properties of a session policy. |

## Summary of commands, operations, and privileges

The following table summarizes the relationship between the session policy DDL operations and their necessary privileges.

| Operation | Privilege required |
| --- | --- |
| Create session policy | A role with the CREATE SESSION POLICY privilege on the schema. |
| Alter session policy | A role with the OWNERSHIP privilege on the session policy. |
| Drop session policy | A role with the OWNERSHIP privilege on the session policy. |
| Describe session policy | A role with the OWNERSHIP privilege on the session policy or . the APPLY SESSION POLICY privilege on the account. |
| Show session policies | A role with the OWNERSHIP privilege on the session policy or . the APPLY SESSION POLICY privilege on the account. |
| Set & unset session policy | For accounts, a role with the APPLY SESSION POLICY privilege on the account and the OWNERSHIP privilege on the session policy, or a role with the APPLY SESSION POLICY privilege on the account and the APPLY privilege on a specific session policy.  For users, a role with the APPLY SESSION POLICY privilege on the user. |

## Session Policy DDL Reference

Snowflake provides the following DDL commands to manage session policy objects:

* [CREATE SESSION POLICY](../sql-reference/sql/create-session-policy.md)
* [ALTER SESSION POLICY](../sql-reference/sql/alter-session-policy.md)
* [DROP SESSION POLICY](../sql-reference/sql/drop-session-policy.md)
* [SHOW SESSION POLICIES](../sql-reference/sql/show-session-policies.md)
* [DESCRIBE SESSION POLICY](../sql-reference/sql/desc-session-policy.md)

To set or unset a session policy on the account, execute the [ALTER ACCOUNT](../sql-reference/sql/alter-account.md) command as shown below.

> ```sqlexample
> ALTER ACCOUNT SET SESSION POLICY mydb.policies.session_policy_prod_1;
> ```
>
> ```sqlexample
> ALTER ACCOUNT UNSET SESSION POLICY;
> ```

To set or unset a user-level session policy, execute the [ALTER USER](../sql-reference/sql/alter-user.md) command as shown below.

> ```sqlexample
> ALTER USER jsmith SET SESSION POLICY mydb.policies.session_policy_prod_1_jsmith;
> ```
>
> ```sqlexample
> ALTER USER jsmith UNSET SESSION POLICY;
> ```

## Auditing session policies

* You can query the [SESSION_POLICIES view](../sql-reference/account-usage/session_policies.md) view to return a row for each session policy and its metadata in
  your Snowflake account.
* You can call the [POLICY_REFERENCES](../sql-reference/functions/policy_references.md) function to return a row for each user that is assigned to the
  specified session policy and a row for the session policy assigned to the Snowflake account.

  Currently, only the following syntax is supported for session policies:

  > ```sqlsyntax
  > POLICY_REFERENCES( POLICY_NAME => '<session_policy_name>' )
  > ```

  Where `session_policy_name` is the fully qualified name of the session policy.

  For example, execute the following query to return a row for each user that is assigned the session policy named
  `session_policy_prod_1`, which is stored in the database named `my_db` and the schema named `my_schema`:

  > ```sqlexample
  > SELECT *
  > FROM TABLE(
  >   my_db.INFORMATION_SCHEMA.POLICY_REFERENCES(
  >     POLICY_NAME => 'my_db.my_schema.session_policy_prod_1'
  >   ));
  > ```

## Troubleshooting session policies

* If a session policy is assigned to an account or a user and the database or schema that contains the session policy is dropped, and then
  a new session policy is assigned to the account or user, the user will not be held to the idle session timeout value(s) in the new
  session policy.

  The workaround is to unset the original session policy from the account using an ALTER ACCOUNT command or from the user using an ALTER
  USER command as shown in this topic.
* The following table summarizes some error messages that can occur with session policies.

  | Behavior | Error Message | Troubleshooting Action |
  | --- | --- | --- |
  | Cannot create a session policy. | Cannot perform CREATE SESSION POLICY. This session does not have a current database. Call ‘USE DATABASE’, or use a qualified name. | Specify a database prior to executing CREATE SESSION POLICY or use the fully qualified object name in the CREATE SESSION POLICY statement. |
  | Cannot create a session policy. | SQL access control error: Insufficient privileges to operate on schema ‘<schema_name>’ | Verify that the role executing the CREATE SESSION POLICY statement has the CREATE SESSION POLICY on SCHEMA privilege. |
  | Cannot create a session policy. | SQL compilation error: Database ‘<database_name>’ does not exist or not authorized. | Verify that the database exists and that the role executing the CREATE SESSION POLICY statement has the USAGE privilege on the schema in which the session policy should exist. |
  | Cannot execute a describe statement. | SQL compilation error: Schema ‘<schema_name>’ does not exist or not authorized. | Verify that the role executing the DESC SESSION POLICY statement has the OWNERSHIP privilege on the session policy or the APPLY privilege on the session policy. |
  | Cannot drop a session policy. | SQL compilation error: Session policy ‘<policy_name>’ does not exist or not authorized. | Verify that the role executing the DROP SESSION POLICY statement has the OWNERSHIP privilege on the session policy. |
  | Cannot drop a session policy. | Session policy <policy_name> cannot be dropped because it is attached to an account. | Unset the session policy from the account with an [ALTER ACCOUNT](../sql-reference/sql/alter-account.md) statement and try the drop statement again. |
  | Cannot set a session policy on an account. | Session policy ‘<policy_name> is already attached to account <account_name>. | An account can only have one active session policy. Determine which session policy should be set for the account. . If necessary, unset the current session policy from the account with a [ALTER ACCOUNT](../sql-reference/sql/alter-account.md) command; then set the other session policy on the account with another ALTER ACCOUNT command. |
  | Cannot set a timeout value. | SQL compilation error: invalid value ‘<integer>’ for property ‘session_idle_timeout_mins’ | The session timeout value, in minutes, must be an integer between `5` and `240`, inclusive. . Choose a valid integer for the session timeout and execute the CREATE or ALTER SESSION POLICY statement again. |
  | Cannot update an existing session policy. | SQL compilation error: Session policy ‘<policy_name>’ does not exist or not authorized. | Verify the name of the session policy, the syntax of the ALTER SESSION POLICY command, and the privileges to operate on the session policy, database, and schema. |
