# Source: https://docs.snowflake.com/en/user-guide/storage-management/storage-lifecycle-policies-monitoring.md

# Monitor storage lifecycle policies

Identify which tables have storage lifecycle policies
attached, and monitor storage lifecycle policy runs by using Snowflake’s built-in functions.

> **Note:**
>
> For information about monitoring storage lifecycle policy costs,
> see [Billing for storage lifecycle policies](storage-lifecycle-policies-billing.md).

## Monitor policy assignments

To view storage lifecycle policy metadata, use the following views:

* [ACCOUNT_USAGE.STORAGE_LIFECYCLE_POLICIES](../../sql-reference/account-usage/storage_lifecycle_policies.md)
* [ORGANIZATION_USAGE.STORAGE_LIFECYCLE_POLICIES](../../sql-reference/organization-usage/storage_lifecycle_policies.md)
* [ACCOUNT_USAGE.STORAGE_LIFECYCLE_POLICY_HISTORY](../../sql-reference/account-usage/storage_lifecycle_policy_history.md)
* [ORGANIZATION_USAGE.STORAGE_LIFECYCLE_POLICY_HISTORY](../../sql-reference/organization-usage/storage_lifecycle_policy_history.md)

## See lifecycle policy attachments

To see which tables a particular lifecycle policy is attached to, call the [POLICY_REFERENCES](../../sql-reference/functions/policy_references.md) table function in
the [Snowflake Information Schema](../../sql-reference/info-schema.md). The function displays only the tables that you have the OWNERSHIP privilege on.

The function returns a row for each table in a database that has the specified policy attached to it.

### Example: List all tables associated with a policy

The following query retrieves a list of tables with a specified storage lifecycle policy attached:

```sqlexample
SELECT *
  FROM TABLE(
    my_db.INFORMATION_SCHEMA.POLICY_REFERENCES(
    POLICY_NAME => 'my_storage_lifecycle_policy'
  )
);
```

### Example: Find the policy assigned to a table

Retrieve the policy assigned to a specified table:

```sqlexample
SELECT *
  FROM TABLE(
    my_db.INFORMATION_SCHEMA.POLICY_REFERENCES(
      REF_ENTITY_NAME => 'my_db.my_schema.my_table',
      REF_ENTITY_DOMAIN => 'table'))
  WHERE POLICY_KIND = 'STORAGE_LIFECYCLE_POLICY';
```

## Monitor storage lifecycle policy runs

To monitor storage lifecycle policy executions over the last 14 days, use the [STORAGE_LIFECYCLE_POLICY_HISTORY](../../sql-reference/functions/storage_lifecycle_policy_history.md) table function. For information about the function output, see the [STORAGE_LIFECYCLE_POLICY_HISTORY](../../sql-reference/functions/storage_lifecycle_policy_history.md) page.

The following example retrieves the 100 most recent executions for a policy attached to a specified table,
scheduled within the last day:

```sqlexample
SELECT * FROM
  TABLE(
    INFORMATION_SCHEMA.STORAGE_LIFECYCLE_POLICY_HISTORY(
      REF_ENTITY_NAME => 'my_db.my_schema.my_source_table',
      REF_ENTITY_DOMAIN => 'table',
      TIME_RANGE_START => DATEADD('DAY', -1, CURRENT_TIMESTAMP()),
      RESULT_LIMIT => 100
    )
  );
```

Alternatively, to retrieve historical data for storage lifecycle policy runs, use the following views:

* [ACCOUNT_USAGE.STORAGE_LIFECYCLE_POLICY_HISTORY](../../sql-reference/account-usage/storage_lifecycle_policy_history.md)
* [ORGANIZATION_USAGE.STORAGE_LIFECYCLE_POLICY_HISTORY](../../sql-reference/organization-usage/storage_lifecycle_policy_history.md)
