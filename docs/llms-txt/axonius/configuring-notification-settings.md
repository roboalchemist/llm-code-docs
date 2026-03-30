# Source: https://docs.axonius.com/docs/configuring-notification-settings.md

# Configuring Notification Settings

Use **Notifications** to have Axonius send a notification email to configured email addresses according to these settings.

**To configure Notification Settings:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **System**, and select **Notifications**.

<Image alt="NotificationsSettingsNew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NotificationsSettingsNew.png" />

<Callout icon="📘" theme="info">
  Note

  The **Enable notifications for low disk space (percentage %)** and **Enable notifications for low disk space (GB)** options in the above screen are visible for [customer-hosted (on-premises / private cloud)](/docs/on-premise-and-private-cloud-deployments) deployments only; not for [Axonius-hosted (SaaS)](/docs/saas-deployment) deployment.
</Callout>

* **Notifications email address** - Configure a comma-separated list of email addresses to receive an email:
  * When there is a connection issue with any of the adapter connections, the email contains a table of affected adapters with relevant details.
  * When a node has not communicated for over three hours.
  * When the available free disk space is below the limit defined (if configured).
* **Notifications webhook address** - Configure the webhook URL to receive a message. The message sent is the same as the message included in the email.
  * When there is a connection issue with any of the adapter connections.
  * When the available free disk space is below the limit defined (if configured).
* **Enable notifications for low disk space (percentage %)**
  * Visible for customer-hosted (on-premises / private cloud) deployments only.
  * When toggled on, the system monitors the available free disk space percentage for all nodes and creates critical or warning notifications based on the following settings:
    * **Critical notifications: notify when free disk space is below (percentage %)** *(optional, default: 5)* - Set the percentage of free disk space, below which the system creates a critical notification.
    * **Warning notifications: notify when free disk space is below (percentage %)** *(optional, default: 10)* - Set the percentage of free disk space, below which the system creates a warning notification.
    * **Minimum days between critical notifications** *(required, default: 1)* - Set the minimum number of days that need to pass since the last time a critical disk space notification based on percentage was created per node.
    * **Minimum days between warning notifications** *(required, default: 7)* - Set the minimum number of days that need to pass since the last time a warning disk space notification based on percentage was created per node.
* **Enable notifications for low disk space (GB)**
  * Visible for customer-hosted (on-premises / private cloud) deployments only.
  * When toggled on, the system monitors the available free disk space in GB for all nodes and creates critical or warning notifications based on the following settings:.
    * **Critical notifications: notify when free disk space is below (GB)** *(optional, default: 10)* - Set the amount of free disk space (GB), below which the system creates a critical notification.
    * **Warning notifications: notify when free disk space is below (GB)** *(optional, default: 15)* - Set the amount of free disk space (GB), below which the system creates a critical notification.
    * **Minimum days between critical notifications** *(required, default: 1)* - Set the minimum number of days that need to pass since the last time a critical disk space notification based on available space in GB was created per node.
    * **Minimum days between warning notifications** *(required, default: 7)* - Set the minimum number of days that need to pass since the last time a warning disk space notification based on available space in GB was created per node.
* **Send notification when a scheduled fetch failed to trigger** - Enable this option to send an email notification if a scheduled adapter fetch did not begin fetching within 24 hours from the time it was scheduled to fetch.

<Callout icon="📘" theme="info">
  Note

  * When an adapter fails to trigger, an adapter fetch fails, or an adapter connection fails, a Finding is automatically created and appears in the [Findings Center - **Alerts** table](/docs/viewing-finding-information#viewing-the-alerts-of-a-finding). However, enabling this option sends a notification email only when an adapter fails to trigger; not when an adapter fetch fails or an adapter connection fails.
  * You can create a notification email for adapter connection failure or adapter fetch failure by creating a Finding in the Findings Center and adding an External Notification.
</Callout>

<Callout icon="📘" theme="info">
  Note

  Axonius cloud customers are not required to configure an email server in order to receive notification emails.
</Callout>

* **Notify when at least one gateway is running an outdated agent version** - When selected, weekly notifications are sent when at least one gateway is running a version lower than the Axonius instance and can be upgraded. Additionally, a banner is displayed in both the Gateways page and in the details drawer of the outdated gateway. See [Upgrading a Gateway](https://docs.axonius.com/axonius-help-docs/docs/manage-gateways#upgrading-a-gateway).

  In order to send notifications via email, the email settings in External Integrations must be configured. See [Configuring Email Settings](https://docs.axonius.com/axonius-help-docs/docs/configuring-email-settings).

<br />