# Source: https://docs.anyscale.com/administration/resource-management/custom-notifications.md

# Custom job and service notifications

[View Markdown](/administration/resource-management/custom-notifications.md)

# Custom job and service notifications

You can create resource notification rules to send alerts to custom channels, such as Slack or email, based on specific job and service statuses. You must be an organization owner to use this feature.

By default, resource owners receive notifications for all events through email. This document is for admins who want to configure additional notification channels, such as Slack or custom webhooks, or extend email notifications to additional recipients.

## Create a resource notification[​](#create "Direct link to Create a resource notification")

To create a new resource notification, complete the following steps:

1. [Log in to the Anyscale console](https://console.anyscale.com/).

2. Click your user icon.

3. Click **Organization settings**.

4. Click **Resource notifications**.

5. Click **Create**.

6. In the **Name** field, provide a unique name for your notification.

7. Use the following fields under the **Target clusters in** heading to set the resource scope.

   <!-- -->

   * (Required) Use the **Cloud** field to select an Anyscale cloud.
   * Use the **Projects** field to limit the scope to clusters in a single project.
   * Use the **Users** field to limit the scope to a single user.

8. Select one or more notification events in the **Events** field. For a description, see [Notification events](#events).

9. Configure one or more types of notifications:

   <!-- -->

   * Use the **Receivers** field to select email addresses of users in the Anyscale organization to receive email notifications.
   * Under **Trigger a Slack notification**, click **Add URL** and paste the URL for a Slack webhook. See [Slack webhook docs](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).
   * Under **Trigger a webhook**, click **Add URL** and paste the URL for any arbitrary webhook.

10. Click **Save**.

## Manage resource notification[​](#manage-resource-notification "Direct link to Manage resource notification")

To edit or delete a resource notification, do the following:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click your user icon.
3. Click **Organization settings**.
4. Click **Resource notifications**.
5. Click the name of your notification.
6. Click the ellipsis (`...`).
7. Click **Edit** or **Delete**.
   <!-- -->
   * You can't modify the cloud for a resource notification.

For further assistance, contact [Anyscale support](mailto:support@anyscale.com).

## Notification events[​](#events "Direct link to Notification events")

The following table describes available notification events:

| Event                  | Description                                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Job failure            | A job fails. Only triggers if no retries remain.                                                                 |
| Job succeeded          | The application code in a job finishes running.                                                                  |
| Job retrying           | A job retries due to job failure.                                                                                |
| Long-running job       | A job runs longer than a specified time limit.Specify threshold in minutes, hours, or days in the console.       |
| Long-running workspace | A workspace runs longer than a specified time limit.Specify threshold in minutes, hours, or days in the console. |
| Service unhealthy      | A service is unavailable or malfunctioning.                                                                      |
| Service running        | A service has deployed and is healthy.                                                                           |
| Service rolled out     | A new version of a service has deployed.                                                                         |
| Service rolling back   | A version roll out has failed and is reverting to the previous version.                                          |

## Unsubscribe from email notifications[​](#unsubscribe-from-email-notifications "Direct link to Unsubscribe from email notifications")

You can unsubscribe from all email notifications for an event type. Click the **Unsubscribe** link in a notification email manage your notification settings.

Anyscale manages email subscription preferences at the organization level for each user for each resource event type. If you unsubscribe from a notification, you no longer receive notifications for that resource event for all Anyscale clouds and projects.
