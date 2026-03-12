# Source: https://docs.snowflake.com/en/sql-reference/classes/budget.md

# BUDGET (SNOWFLAKE.CORE)

Budget commands enable you to manage [budgets](../../user-guide/budgets.md) in your account.

## Budget commands

* [ALTER BUDGET](budget/commands/alter-budget.md)
* [CREATE BUDGET](budget/commands/create-budget.md)
* [DROP BUDGET](budget/commands/drop-budget.md)
* [SHOW BUDGET](budget/commands/show-budget.md)

## Budget functions

* [SYSTEM$SHOW_BUDGETS_IN_ACCOUNT](../functions/system_show_budgets_in_account.md)

## Budget methods

* [account_root_budget!ACTIVATE](budget/methods/activate.md)
* [<budget_name>!ADD_CUSTOM_ACTION](budget/methods/add_custom_action.md)
* [<budget_name>!ADD_NOTIFICATION_INTEGRATION](budget/methods/add_notification_integration.md)
* [<budget_name>!ADD_RESOURCE](budget/methods/add_resource.md)
* [<budget_name>!ADD_RESOURCE_TAG](budget/methods/add_resource_tag.md) (Deprecated)
* [<budget_name>!ADD_TAG](budget/methods/add_tag.md) (Deprecated)
* [<budget_name>!CONFIRM_CUSTOM_ACTIONS_ACCESS](budget/methods/confirm_custom_actions_access.md)
* [account_root_budget!DEACTIVATE](budget/methods/deactivate.md)
* [<budget_name>!GET_BUDGET_SCOPE](budget/methods/get_budget_scope.md)
* [<budget_name>!GET_CONFIG](budget/methods/get_config.md)
* [<budget_name>!GET_CUSTOM_ACTIONS](budget/methods/get_custom_actions.md)
* [<budget_name>!GET_CYCLE_START_ACTION](budget/methods/get_cycle_start_action.md)
* [<budget_name>!GET_LINKED_RESOURCES](budget/methods/get_linked_resources.md)
* [<budget_name>!GET_LINKED_TAGS](budget/methods/get_linked_tags.md) (Deprecated)
* [<budget_name>!GET_MEASUREMENT_TABLE](budget/methods/get_measurement_table.md)
* [<budget_name>!GET_NOTIFICATION_EMAIL](budget/methods/get_notification_email.md)
* [<budget_name>!GET_NOTIFICATION_INTEGRATION_NAME](budget/methods/get_notification_integration_name.md)
* [<budget_name>!GET_NOTIFICATION_INTEGRATIONS](budget/methods/get_notification_integrations.md)
* [<budget_name>!GET_NOTIFICATION_MUTE_FLAG](budget/methods/get_notification_mute_flag.md)
* [<budget_name>!GET_NOTIFICATION_THRESHOLD](budget/methods/get_notification_threshold.md)
* [<budget_name>!GET_REFRESH_TIER](budget/methods/get_refresh_tier.md)
* [<budget_name>!GET_RESOURCE_TAGS](budget/methods/get_resource_tags.md) (Deprecated)
* [<budget_name>!GET_SERVICE_TYPE_USAGE](budget/methods/get_service_type_usage.md) (Deprecated)
* [<budget_name>!GET_SERVICE_TYPE_USAGE_V2](budget/methods/get_service_type_usage_v2.md)
* [<budget_name>!GET_SPENDING_HISTORY](budget/methods/get_spending_history.md)
* [<budget_name>!GET_SPENDING_LIMIT](budget/methods/get_spending_limit.md)
* [<budget_name>!REFRESH_USAGE](budget/methods/refresh_usage.md)
* [<budget_name>!REMOVE_CUSTOM_ACTIONS](budget/methods/remove_custom_actions.md)
* [<budget_name>!REMOVE_CYCLE_START_ACTION](budget/methods/remove_cycle_start_action.md)
* [<budget_name>!REMOVE_NOTIFICATION_INTEGRATION](budget/methods/remove_notification_integration.md)
* [<budget_name>!REMOVE_RESOURCE](budget/methods/remove_resource.md)
* [<budget_name>!REMOVE_RESOURCE_TAG](budget/methods/remove_resource_tag.md) (Deprecated)
* [<budget_name>!REMOVE_TAG](budget/methods/remove_tag.md) (Deprecated)
* [<budget_name>!SET_CYCLE_START_ACTION](budget/methods/set_cycle_start_action.md)
* [<budget_name>!SET_EMAIL_NOTIFICATIONS](budget/methods/set_email_notifications.md)
* [<budget_name>!SET_NOTIFICATION_MUTE_FLAG](budget/methods/set_notification_mute_flag.md)
* [<budget_name>!SET_NOTIFICATION_THRESHOLD](budget/methods/set_notification_threshold.md)
* [<budget_name>!SET_REFRESH_TIER](budget/methods/set_refresh_tier.md)
* [<budget_name>!SET_RESOURCE_TAGS](budget/methods/set_resource_tags.md)
* [<budget_name>!SET_SPENDING_LIMIT](budget/methods/set_spending_limit.md)
