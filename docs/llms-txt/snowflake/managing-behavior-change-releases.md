# Source: https://docs.snowflake.com/en/release-notes/bcr-bundles/managing-behavior-change-releases.md

# Behavior change management

This document explains how to check whether a particular
[behavior change bundle](../behavior-change-policy.md) is enabled in your account and how to enable or disable it.

## Overview

Snowflake implements behavior changes monthly in bundles included in regularly-scheduled
[releases](../../user-guide/intro-releases.md). During the testing period and opt-out period for each behavior change bundle,
you can enable or disable the bundle in your account. This document explains how to check whether a particular bundle is enabled
in your account and how to enable or disable it.

In this document, the name of the behavior change bundle is in the form `YYYY_NN`. For the names of the
currently available behavior change bundles, see [Behavior change announcements](../behavior-changes.md).

> **Note:**
>
> Behavior changes in bundles cannot be enabled/disabled individually. To enable/disable a behavior change, you must
> enable/disable the bundle containing the change.

## Checking the status of a behavior change bundle in your account

To check whether a specific behavior change bundle is enabled in your account, call the
[SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS](../../sql-reference/functions/system_behavior_change_bundle_status.md) function. For example, to check the status of the bundle
named `2024_02`:

```sqlexample
SELECT SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS('2024_02');
```

```output
+-------------------------------------------------+
| SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS('2024_02') |
|-------------------------------------------------|
| DISABLED                                        |
+-------------------------------------------------+
```

To check the status of all currently available behavior change bundles, call the
[SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES](../../sql-reference/functions/system_show_active_behavior_change_bundles.md) function:

```sqlexample
SELECT SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES();
```

```output
+--------------------------------------------------------------------------------------------------------------+
| SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES()                                                                 |
|--------------------------------------------------------------------------------------------------------------|
| [{"name":"2023_08","isDefault":true,"isEnabled":true},{"name":"2024_01","isDefault":false,"isEnabled":true}] |
+--------------------------------------------------------------------------------------------------------------+
```

## Enabling a behavior change bundle in your account

To enable a particular behavior change in your account, call the
[SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE](../../sql-reference/functions/system_enable_behavior_change_bundle.md) function. For example, to enable the bundle
named `2024_02`:

```sqlexample
SELECT SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE('2024_02');
```

```output
+-------------------------------------------------+
| SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE('2024_02') |
|-------------------------------------------------|
| ENABLED                                         |
+-------------------------------------------------+
```

## Disabling a behavior change bundle in your account

To disable a particular behavior change in your account, call the
[SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE](../../sql-reference/functions/system_disable_behavior_change_bundle.md). For example, to disable the bundle
named `2024_02`:

```sqlexample
SELECT SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE('2024_02');
```

```output
+-------------------------------------------------+
| SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE('2024_02')|
|-------------------------------------------------|
| DISABLED                                        |
+-------------------------------------------------+
```

## Determining the current version of your account

To check the current version of Snowflake that is in your account, call the
[CURRENT_VERSION](../../sql-reference/functions/current_version.md) function. For example:

> ```sqlexample
> SELECT CURRENT_VERSION();
> ```
>
> ```output
> +-------------------+
> | CURRENT_VERSION() |
> |-------------------|
> | 8.5.1             |
> +-------------------+
> ```

## Mitigating masking policy return value updates

In the `2024_04` [bundle](2024_04/bcr-1355.md), there are changes to the values for precision and
scale in masking policy conditions (collectively: “return value updates”). A query on a column protected by a masking policy fails when the
following are true:

* The bundle is enabled.
* The masking policy conditions return a value whose precision is greater than the precision of the column to which the masking
  policy is assigned.

If the scale of the return value is larger than the scale of the column, the value is truncated to match the scale of the column.

If you want to apply the new behavior to a pre-existing policy, create a new masking policy and replace the pre-existing policy using the
`FORCE` [keyword](../../user-guide/security-column-intro.md).

When the bundle is enabled, you can test the behavior as follows:

1. Create a policy:

   ```sqlexample
   CREATE MASKING POLICY MP AS (n NUMBER)
   RETURNS NUMBER -> 12345;
   ```

2. Assign the policy:

   ```sqlexample
   CREATE TABLE t(col1 NUMBER(2,0));

   ALTER TABLE t MODIFY COLUMN col1 SET MASKING POLICY mp;
   INSERT INTO t VALUES (10);
   ```

3. Query the column (fails):

   ```sqlexample
   SELECT * FROM t;
   ```

> **Note:**
>
> The changes to the values for precision and scale are not applicable to the string data type.

To determine the impact of this change and provide enough time to update the masking policy conditions to protect data, query the
SNOWFLAKE.BCR_ROLLOUT.BCR_2024_03_DDM_ROLLOUT view to understand how the future return value updates affect your account.

The BCR_2024_03_DDM_ROLLOUT view is temporary. Snowflake will remove the view when the return value updates are generally enabled
in a future behavior change bundle. At this point, you will not be able to query the view to determine affected columns and policies or
prevent column query or masking policy assignment operation failures due to return value updates.

The view records data starting from March 2024. If a query on the view takes a long time to complete, you can specify the start date and
end date session variables using a [SET](../../sql-reference/sql/set.md) command. These variables help to reduce the number of rows to evaluate when
you query the view. For example:

> ```sqlexample
> SET DDM_CASTING_BCR_START_DATE = '2024-03-01';
> SET DDM_CASTING_BCR_END_DATE = '2024-04-03';
> ```

### Identify masking policy & column associations

To query the view and mitigate the upcoming return value changes, do the following:

1. Query the SNOWFLAKE.BCR_ROLLOUT.BCR_2024_03_DDM_ROLLOUT view. For example:

   ```sqlexample
   USE ROLE ACCOUNTADMIN;
   SET DDM_CASTING_BCR_START_DATE = '2024-03-01';
   SET DDM_CASTING_BCR_END_DATE = '2024-04-03';
   SELECT * FROM SNOWFLAKE.BCR_ROLLOUT.BCR_2024_03_DDM_ROLLOUT;
   ```

2. Evaluate the REASON column in the BCR_2024_03_DDM_ROLLOUT View Reference section to determine what update needs to be made to the
   masking policy conditions.
3. Update the masking policy conditions with an [ALTER MASKING POLICY](../../sql-reference/sql/alter-masking-policy.md) statement to ensure the column data remains
   protected and that policy assignment operations or protected column queries do not fail.
4. Test the new policy conditions by querying the table columns to which the masking policies are assigned.

### BCR_2024_03_DDM_ROLLOUT view reference

The BCR_2024_03_DDM_ROLLOUT view (in the SNOWFLAKE.BCR_ROLLOUT schema) records information starting on July 15, 2022 and contains the
following columns:

| Column | Data type | Description |
| --- | --- | --- |
| `policy_name` | VARCHAR | The name of the policy. |
| `policy_id` | NUMBER | Internal/system-generated identifier for the policy. |
| `policy_schema` | VARCHAR | The parent schema of the policy. |
| `policy_database` | VARCHAR | The parent database of the policy. |
| `policy_body` | VARIANT | The conditions of the policy to mask or unmask the column data. |
| `column_name` | VARCHAR | The name of the column that has the policy. |
| COLUMN_TYPE | VARCHAR | The data type of the column. |
| COLUMN_LENGTH | NUMBER | The length of the column that has the policy or `[NULL]` if not set for the column. |
| COLUMN_PRECISION | NUMBER | The precision of the column that has the policy or `[NULL]` if not set for the column. |
| COLUMN_SCALE | NUMBER | The scale of the column that has the policy or `[NULL]` if not set for the column. |
| TABLE_NAME | VARCHAR | The name of the table. |
| `table_id` | NUMBER | Internal/system-generated identifier for the table. |
| `table_schema` | VARCHAR | The parent schema of the table. |
| `table_database` | VARCHAR | The parent database of the table. |
| `table_kind` | VARCHAR | The type of table. One of the following: `TABLE`, `LOCAL TEMPORARY`, `VIEW`, `MATERIALIZED VIEW`, `EXTERNAL TABLE`, or `DYNAMIC TABLE`. |
| `reason` | VARCHAR | Possible reason for the mismatch. One of the following: `precision` or `scale`. |
| LARGEST_MASKED_SIZE | NUMBER | The maximum length, scale, or precision a masked value can have based on the masking policy assigned to the column. |
