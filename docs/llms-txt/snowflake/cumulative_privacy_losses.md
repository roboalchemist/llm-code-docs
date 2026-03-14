# Source: https://docs.snowflake.com/en/sql-reference/functions/cumulative_privacy_losses.md

Categories:
:   [Table functions](../functions-table.md)

# CUMULATIVE_PRIVACY_LOSSES

Returns the privacy budgets associated with a specific [privacy policy](../../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md).

For more information about viewing privacy budgets, see [View a privacy budget](../../user-guide/diff-privacy/differential-privacy-admin-privacy-budgets.md).

## Syntax

```sqlsyntax
SNOWFLAKE.DATA_PRIVACY.CUMULATIVE_PRIVACY_LOSSES( '<privacy_policy>' )
```

## Arguments

`'privacy_policy'`
:   Specifies the fully-qualified name of the privacy policy. A privacy policy is a schema-level object.

## Output

| Column | Data type | Description |
| --- | --- | --- |
| `database_name` | VARCHAR | Database that contains the privacy policy. |
| `schema_name` | VARCHAR | Schema that contains the privacy policy. |
| `policy_name` | VARCHAR | Name of the privacy policy. |
| `budget_name` | VARCHAR | Name of the privacy budget in the privacy policy. |
| `consumer_id` | VARCHAR | Organization and account where users executed queries that incurred privacy loss. |
| `budget_spent` | FLOAT | Cumulative privacy loss since the last time the [privacy budget was refreshed](../../user-guide/diff-privacy/differential-privacy-admin-privacy-budgets.md). |

## Usage notes

A privacy budget only appears if analysts associated with the privacy budget have incurred privacy loss or if an administrator has
[reset the privacy budget](../../user-guide/diff-privacy/differential-privacy-admin-privacy-budgets.md).

## Examples

View the privacy budgets that are associated with the `my_policy_privacy` policy:

```sqlexample
SELECT *
  FROM TABLE(SNOWFLAKE.DATA_PRIVACY.CUMULATIVE_PRIVACY_LOSSES(
    'my_policy_db.my_policy_schema.my_policy_privacy'));
```
