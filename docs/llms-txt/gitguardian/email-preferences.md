# Source: https://docs.gitguardian.com/platform/user-account/email-preferences.md

# Configure email preferences

> Manage your personal email notification preferences for GitGuardian incident alerts and workspace updates.

You can configure the email notifications you want to receive from GitGuardian in [your personal settings](https://dashboard.gitguardian.com/settings/personal/notifications).

By default, GitGuardian notifies you by email for any important events that occur on your dashboard. You can customize the email notifications for each workspace you are a member of. The available notifications are grouped into different categories:

- **Workspace notifications**
  - **Team notifications**: Receive email notifications about your teams.
  - **Health Checks**: Receive email notifications about the health of your integrations.

- **Internal Monitoring**
  - **Incident alerting**: Receive email notifications upon new internal incidents from your teams.:warning: Turning off these notifications will require confirmation, as you may miss future important security-related notifications. This setting may be automatically disabled by default at the [workspace level](../enterprise-administration/workspace-settings#by-default-users-are-notified-by-email-when-a-new-incident-is-detected)).
  You have two options for receiving notifications:
    - All internal incidents (default)
    - Only internal incident involving yourself (based on git commit email)
  - **Historical scan notifications**: Receive email notifications upon completion of historical scans.
  - **Feedback submission notifications**: Receive email notifications upon feedback submission on an internal incident.
  - **Access granting notifications**: Receive email notifications when granted access to an internal incident.
  - **Weekly recap**: Receive a weekly email to keep track of the evolution of your internal incidents.
  - **Incident ignored with a valid secret**: Receive email notification when an internal incident is ignored with a valid secret based on the teams(s) you manage. _This option is available in the business plan_

- **Honeytokens**
  - **Trigger notifications**: Receive email notifications when an active token is triggered. Find more information about those alerts [here](../../honeytoken/configure-alerts).

- **Public Monitoring** (if your workspace and team have access to Public Monitoring)
  - **Incident alerting**: Receive email notifications upon new public incidents
  - **Historical scan notifications**: Receive email notifications upon completion of historical scans of your public perimeter.
  - **Feedback submission notifications**: Receive email notifications upon feedback submission on a public incident.
  - **Access granting notifications**: Receive email notifications when granted access to a public incident.

![email preferences](/img/platform/user-account/email_preferences.png)

> If you are a member of multiple workspaces, you can tailor your email notifications for each separate workspace.
