# Source: https://docs.snowflake.com/en/sql-reference/account-usage/privacy_budgets.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# PRIVACY_BUDGETS view

This Account Usage view lets you retrieve the privacy budgets associated with
[privacy policies](../../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md) in an account.

For more information about viewing privacy budgets, see [View a privacy budget](../../user-guide/diff-privacy/differential-privacy-admin-privacy-budgets.md).

## Columns

| Column | Data type | Description |
| --- | --- | --- |
| `database_name` | VARCHAR | Database that contains the privacy policy. |
| `schema_name` | VARCHAR | Schema that contains the privacy policy. |
| `policy_name` | VARCHAR | Name of the privacy policy. |
| `budget_name` | VARCHAR | Name of the privacy budget in the privacy policy. |
| `consumer_id` | VARCHAR | Organization and account where users executed queries that incurred privacy loss. |
| `budget_spent` | FLOAT | Cumulative privacy loss since the last time the [privacy budget was refreshed](../../user-guide/diff-privacy/differential-privacy-admin-privacy-budgets.md). |

## Usage notes

* Latency for the view may be up to 24 hours.
* A privacy budget only appears if analysts associated with the privacy budget have incurred privacy loss or if an administrator has
  [reset the privacy budget](../../user-guide/diff-privacy/differential-privacy-admin-privacy-budgets.md).
