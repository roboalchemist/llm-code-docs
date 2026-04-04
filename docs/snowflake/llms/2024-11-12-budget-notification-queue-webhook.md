# Source: https://docs.snowflake.com/en/release-notes/2024/other/2024-11-12-budget-notification-queue-webhook.md

# November 12, 2024 — Budgets: Support for cloud provider queue and webhook notifications

You can now configure your account budget and custom budgets so that notifications are sent to the following:

* A queue provided by a cloud service (Amazon SNS, Azure Event Grid, or Google Cloud PubSub).
* A webhook for Slack, Microsoft Teams, or PagerDuty.

To do this, you create a [notification integration for a queue](../../../user-guide/notifications/queue-notifications.md) or a
[webhook](../../../user-guide/notifications/webhook-notifications.md), and you call a method to associate the integration with the
budget. The BUDGET class now supports the following new methods:

| Method | Description |
| --- | --- |
| [<budget_name>!ADD_NOTIFICATION_INTEGRATION](../../../sql-reference/classes/budget/methods/add_notification_integration.md) | Adds a queue or webhook notification integration to a custom budget or the account budget. |
| [<budget_name>!GET_NOTIFICATION_INTEGRATIONS](../../../sql-reference/classes/budget/methods/get_notification_integrations.md) | Returns information about the queue and webhook notification integrations associated with a custom budget or the account budget. |
| [<budget_name>!REMOVE_NOTIFICATION_INTEGRATION](../../../sql-reference/classes/budget/methods/remove_notification_integration.md) | Removes a queue or webhook notification integration from a custom budget or the account budget. |

For information, see [Notifications for budgets](../../../user-guide/budgets/notifications.md).
