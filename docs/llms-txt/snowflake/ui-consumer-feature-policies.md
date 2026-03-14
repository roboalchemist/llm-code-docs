# Source: https://docs.snowflake.com/en/developer-guide/native-apps/ui-consumer-feature-policies.md

# Use feature policies to limit the objects an app can create

This topic describes how to use feature policies to limit the objects that a Snowflake Native App
can create.

## About feature policies

If an app is configured to use
[automated granting of privileges](requesting-auto-privs.md), the app can request to use
the following privileges:

* EXECUTE TASK
* EXECUTE MANAGED TASK
* CREATE WAREHOUSE
* CREATE COMPUTE POOL
* BIND SERVICE ENDPOINT
* CREATE DATABASE
* CREATE EXTERNAL ACCESS INTEGRATION

If the app is configured to use these privileges, a consumer cannot directly revoke these privileges
after the app is installed. However, consumer administrators can use feature policies
to limit the objects an app can create in the consumer account.

For example, if a consumer does not want an app to create warehouses or compute pools, a consumer account
administrator can create a feature policy that prohibits a particular app or all apps from
creating warehouses or compute pools.

Feature policies allow consumers to restrict an app from creating or using the following
objects:

* COMPUTE POOLS
* DATABASES
* TASKS
* WAREHOUSES

> **Note:**
>
> External access integrations can’t be blocked using feature policies. Instead, consumers
> can choose to approve or decline the endpoints for an app using app specifications.

## Workflow

The general workflow for using feature policies to limit the objects an app can create is:

1. View the listing for the app to determine the privileges the app is
   requesting.
2. If there are any objects you want to restrict, create a feature policy to block these objects.

   For more information, see Create a new feature policy.
3. Apply the feature policy to the account or to a specific object.

   For more information, see Assign a feature policy at the account level and
   Apply a feature policy to an app.

## Replication considerations when using feature policies

Feature policy references at the account-level are replicated when specifying the database containing policy, for example, by setting `ALLOWED_DATABASES = policy_db` in a replication group or failover
group.

If the account has already been replicated to a target account, a consumer account administrator must
do the following:

1. Update the replication or failover group in the source account to include the databases and object types
   required to successfully replicate the feature policy.
2. Execute a refresh operation to update the target account.

> **Note:**
>
> The feature policy must be in the same account as the account-level policy assignment.

If you have a feature policy set on the account and you do not update the replication or failover group to include the policy_db containing the policy, this creates a dangling reference in the target account. This means that Snowflake cannot locate the policy in the target account because the fully-qualified name of the policy points to the database in the source account. The result is that the target account or users in the
target account are not required to comply with the feature policy.

To successfully replicate a feature policy, verify that the replication or failover group includes the object types and databases required to prevent a dangling reference.

For more information, see [Replication considerations](../../user-guide/account-replication-considerations.md).

## Feature policy precedence

Consumers can apply a feature policy to all applications in an account or a specified application.
If there are feature policies applied to more than one of these, the most specific feature policy
overrides more general feature policies. The following summarizes the order of precedence:

Account:
:   Feature policies applied to an account are the most general feature policies. They are overridden
    by feature policies applied to a specific object, for example, an application

Object:
:   Feature policies applied to a specific object override feature policies applied to the account.

Consumers can use this precedence to fine-tune the objects an app can create in their account.
For example, a consumer can apply an account-level feature policy that prohibits all apps in the account from creating a
database. If an app tries to create a database during installation, the installation fails.

However, consumers can also create a feature policy with no restrictions and apply tha feature policy
to a specific app. That app would be allowed to create a database.

For more information, see Create a new feature policy.

## Privileges required to use feature policies

The following table describes the privileges require to create and use feature policies:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE FEATURE POLICY | SCHEMA | Required to create a feature policy. This privilege must be granted on the schema containing the feature policy. |
| APPLY FEATURE POLICY | ACCOUNT |  |
| APPLY or OWNERSHIP | FEATURE POLICY |  |

## Working with feature policies

Consumers can use Snowsight or SQL to manage the lifecycle of a feature policy.

### Create a new feature policy

Consumers can create feature policies to prohibit an app from creating certain
types of objects. The following example shows how to create a feature policy to
prohibit an app from creating a database:

```sqlexample
CREATE DATABASE feature_policy_db;
CREATE SCHEMA sch;
CREATE FEATURE POLICY block_create_db_policy
  BLOCKED_OBJECT_TYPES_FOR_CREATION = (DATABASE);
```

> **Note:**
>
> Feature policies must be created within a schema.

Consumers can also create a feature policy that doesn’t restrict creating objects,
as shown in the following example:

```sqlexample
CREATE FEATURE POLICY block_nothing_policy
  BLOCKED_OBJECT_TYPES_FOR_CREATION = ();
```

### Assign a feature policy at the account level

Consumers can apply a feature policy at the account level by using the
[ALTER ACCOUNT](../../sql-reference/sql/alter-account.md) command, as shown in the following example:

```sqlexample
ALTER ACCOUNT
  SET FEATURE POLICY feature_policy_db.sch.block_create_db_policy
  FOR ALL APPLICATIONS;
```

This command applies the `block_create_db_policy` policy for any app that is installed
in the account. After applying this policy, apps can no longer create databases.

### Apply a feature policy to an app

To apply a feature policy when creating an app manually, use the WITH FEATURE POLICY clauase of the
[CREATE APPLICATION](../../sql-reference/sql/create-application.md) command,
as shown in the following example:

```sqlexample
CREATE APPLICATION hello_snowflake_app
  WITH FEATURE POLICY = feature_policy_db.block_create_db_policy;
```

To app a feature policy to an app, use the
[ALTER APPLICATION](../../sql-reference/sql/alter-application.md) command,
as shown in the following example:

```sqlexample
ALTER APPLICATION hello_snowflake_app
  SET FEATURE POLICY feature_policy_db.block_create_db_policy;
```

### Unapply a feature policy

To unapply a feature policy at the account level, use the
[ALTER ACCOUNT](../../sql-reference/sql/alter-account.md) command,
as shown in the following example:

```sqlexample
ALTER ACCOUNT UNSET FEATURE POLICY FOR ALL APPLICATIONS;
```

To unapply a feature policy for a specific app, use the
[ALTER APPLICATION](../../sql-reference/sql/alter-application.md) command,
as shown in the following example:

```sqlexample
ALTER APPLICATION FEATURE_POLICY_TEST_APP UNSET FEATURE POLICY;
```

### Delete a feature policy

To delete a feature policy, use the [DROP FEATURE POLICY](../../sql-reference/sql/drop-feature-policy.md)
command, as shown in the following example:

```sqlexample
DROP FEATURE POLICY block_create_db_policy;
```

## View information about feature policies

To view the feature policies in an account for which you have access privileges, use the
[SHOW FEATURE POLICIES](../../sql-reference/sql/show-feature-policies.md)
command:

```sqlexample
SHOW FEATURE POLICIES ON ACCOUNT;
```

To view the feature policies applied to an app, use the following command:

```sqlexample
SHOW FEATURE POLICIES ON APPLICATION hello_snowflake_app;
```

To see information about a specific feature policy, use the
[DESCRIBE FEATURE POLICY](../../sql-reference/sql/desc-feature-policy.md),
as shown in the following example:

```sqlexample
DESCRIBE FEATURE POLICY feature_policy_db.block_create_db_policy;
```
