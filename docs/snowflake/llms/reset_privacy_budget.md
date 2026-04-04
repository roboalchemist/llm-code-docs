# Source: https://docs.snowflake.com/en/sql-reference/stored-procedures/reset_privacy_budget.md

# RESET_PRIVACY_BUDGET

Resets the cumulative privacy loss of a [privacy budget](../../user-guide/diff-privacy/differential-privacy-overview.md) to 0.

## Syntax

```sqlsyntax
SNOWFLAKE.DATA_PRIVACY.RESET_PRIVACY_BUDGET(
  '<privacy_policy_name>',
  '<budget_name>',
  '<organization_name>',
  '<account_name>')
```

## Arguments

`'privacy_policy_name'`
:   Name of the [privacy policy](../../user-guide/diff-privacy/differential-privacy-admin-privacy-policies.md) that specifies the privacy
    budget. Must be a fully qualified name that includes the database and schema.

`'budget_name'`
:   Name of a privacy budget.

`'organization_name'`
:   Name of the organization that contains the account in which the analyst is incurring privacy loss.

`'account_name'`
:   Name of the account in which the analyst is incurring privacy loss, specified using the [account name format](../../user-guide/admin-account-identifier.md)
    of the account identifier.

## Usage notes

* Globally defined stored procedures utilize caller’s rights. For more details, see
  [Understanding caller’s rights and owner’s rights stored procedures](../../developer-guide/stored-procedure/stored-procedures-rights.md).
* Cumulative privacy loss is reset the next time a query incurs privacy loss. If you view the privacy budget after calling
  RESET_PRIVACY_BUDGET but before the first query incurs privacy loss, the cumulative privacy loss will not be 0.

## Examples

Suppose the `my_policy` privacy policy includes the `analyst_budget` privacy budget. To reset the cumulative privacy loss incurred by
users associated with the `analysts_budget` privacy budget who are executing their queries in the `companyorg.account_123` account:

```sqlexample
CALL SNOWFLAKE.DATA_PRIVACY.RESET_PRIVACY_BUDGET(
  'my_policy_db.my_policy_schema.my_policy',
  'analyst_budget',
  'companyorg',
  'account_123');
```
