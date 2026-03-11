# Source: https://docs.axonius.com/docs/configuring-activity-logs-settings.md

# Configuring Activity Logs Settings

Use the **Activity Logs Settings** to control the logging of two distinct types of activities for enhanced visibility and audit capabilities:

* **Access (read) activities** - Logs read actions (such as viewing assets or reports) to the relevant activity logs, viewable on the Axonius [Activity Logs page](/docs/activity-logs-page).

* **API GET activities** - Logs all API GET requests to the Syslog external system.

**To configure Activity Logs settings**

1. From the top right corner of any page, click the **System Settings** ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png) icon.
2. In the Categories/Subcategories pane of the **System Settings** page that opens, expand **System**, and select **Activity Logs**.
3. Toggle on the desired logging options (by default both False):
   * **Add activity logs for access (read) activity** - Records **View** activities in the Activity Log, such as View Alerts/Findings, View Enforcement, View Assets (for various asset types), and View Activity Log itself.
   * **Add API GET activities to Syslog** - Logs all API GET requests to your configured external Syslog system.

![ActivityLogsSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActivityLogsSettings.png)

<Callout icon="📘" theme="info">
  Note

  * You can see the list of supported **View** activity logs (logged when the setting is enabled) in the **Action** dropdown on the [**Activity Logs** page](/docs/activity-logs-page).
  * When you disable the logging of access (read) activities, new read actions stop being recorded. However, all previously logged activities (while the setting was enabled) remain viewable on the **Activity Logs** page.
  * API GET activities are never written to the internal Axonius **Activity Logs** page; they are only forwarded to Syslog when the setting is enabled.
</Callout>