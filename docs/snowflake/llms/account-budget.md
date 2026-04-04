# Source: https://docs.snowflake.com/en/user-guide/budgets/account-budget.md

# Work with the account budget

The account budget monitors spending for all credit usage in the account.

## Activating the account budget

To start using budgets to monitor credit usage for your account, activate the account budget. After you activate the account
budget, you can set the spending limit for the account and configure how notifications are sent when credit usage is
expected to exceed the spending limit. Notifications begin when projected spending is more than 10% above the spending limit.

You can activate the account budget by using Snowsight or by executing SQL statements.

The next sections explain how to activate the account budget:

* Create a custom role to manage the account budget
* Use Snowsight to activate the account budget
* Use SQL commands to activate the account budget

### Create a custom role to manage the account budget

You can create a custom role to activate and modify the account budget. A user who is granted this role can administer the budget by taking
the following actions on the account budget:

* Activate and deactivate the account budget.
* Set the spending limit.
* Edit notification settings.
* Monitor credit usage for the account.

For a full list of roles and privileges required for the budget administrator role, see [Budgets roles and privileges](../budgets.md).

The following example creates a role named `account_budget_admin` and grants the role the ability to monitor and manage the
account budget:

```sqlexample
USE ROLE ACCOUNTADMIN;

CREATE ROLE account_budget_admin;

GRANT APPLICATION ROLE SNOWFLAKE.BUDGET_ADMIN TO ROLE account_budget_admin;

GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE account_budget_admin;
```

### Use Snowsight to activate the account budget

> **Note:**
>
> Only a user with the ACCOUNTADMIN role or a role
> granted account budget admin privileges can activate and set up the account budget for a regular
> account.
>
> If you are activating the account budget for the [organization account](../organization-accounts.md), use the GLOBALORGADMIN
> role instead of the ACCOUNTADMIN role.

1. Sign in to [Snowsight](../ui-snowsight-gs.md).
2. In the navigation menu, select Admin » Cost management.
3. Select Budgets.
4. If prompted, select a warehouse.
5. In the dashboard, select Set up Account Budget.
6. Enter the target spending limit for the account.
7. Enter the email addresses to receive notification emails.

   > **Note:**
   >
   > Each email address added for budget notifications must be [verified](../notifications/email-notifications.md). The
   > notification email setup fails if any email address in the list is *not* verified.
8. Select Finish Setup.

### Use SQL commands to activate the account budget

> **Note:**
>
> Only a user with the ACCOUNTADMIN role or a role
> granted account budget admin privileges can activate and set up the account budget in a regular
> account.
>
> If you are activating the account budget for the [organization account](../organization-accounts.md), use the GLOBALORGADMIN
> role instead of the ACCOUNTADMIN role.

1. Activate the account budget by calling the [account_root_budget!ACTIVATE](../../sql-reference/classes/budget/methods/activate.md) method on the
   SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET object:

   ```sqlexample
   CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!ACTIVATE();
   ```

2. Set the spending limit calling the [<budget_name>!SET_SPENDING_LIMIT](../../sql-reference/classes/budget/methods/set_spending_limit.md) method:

   ```sqlexample
   CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!SET_SPENDING_LIMIT(1000);
   ```

3. Set up notifications for the budget so that you receive notifications when your credit usage is expected to exceed your
   spending limits.

   See [Notifications for budgets](notifications.md).

## Deactivating the account budget

You can deactivate the account budget using Snowsight or SQL.

Deactivating the account budget resets the account budget to its state before activation:

* All historical account budget data is deleted.
* The background measurement task for the account budget is suspended.
* The account budget settings for spending limit and email notifications are reset.

Account budget deactivation does not affect custom budgets. To remove a custom budget from your account, use
the [DROP BUDGET](../../sql-reference/classes/budget/commands/drop-budget.md) command.

> **Note:**
>
> If the account budget is deactivated, you can’t create new custom budgets using Snowsight.
> However, you can continue to [create custom budgets using SQL](custom-budget.md).

### Use Snowsight to deactivate the account budget

You can deactivate the account budget using the Budgets page:

1. Sign in to [Snowsight](../ui-snowsight-gs.md).
2. In the navigation menu, select Admin » Cost management.
3. Select Budgets.
4. Select the  more menu.
5. Select Deactivate account budget.

### Use SQL commands to deactivate the account budget

You can use the [account_root_budget!DEACTIVATE](../../sql-reference/classes/budget/methods/deactivate.md) method to deactivate the account budget:

```sqlexample
CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!DEACTIVATE();
```
