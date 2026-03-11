# Source: https://docs.axonius.com/docs/wrike-create-update-task.md

# Wrike - Create or Update Task

**Wrike - Create or Update Task** creates a new task from the results retrieved from a saved query. This EC searches Wrike tasks by title, and if the task already exists or has a task ID submitted, the EC updates the task instead of creating a new one.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Split Tickets By** - When enabled, group assets into different tickets based on a shared attribute. Click the adapter icon to select an adapter (or Aggregated), and then click the **Select Adapter Field** box to select the asset field used to generate a separate ticket for each unique value.

  <Callout icon="📘" theme="info">
    Note

    * The **Split Tickets By** option appears only in ticket creation actions, and does not appear in ticket-per-asset creation or ticket update actions.
    * For assets containing multiple values, the system uses only the first value to perform the split.
  </Callout>

<br />

* **Use stored credentials from Wrike adapter** - Select this option to use the [Wrike](/docs/wrike) connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Wrike](/docs/wrike) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Ticket Main Settings

These fields are optional, unless noted otherwise.

* **Folder ID** *(required if creating a task)* - The ID of the folder to create the task in.
* **Task ID** *(required if updating a task)* - The task ID to update.
* **Task Title** - The title of the task. A default value is added by Axonius. You can change the title according to your needs.
* **Task Description** - Enter a description of the task. It is recommended to describe what the task does.
* **Task Status** -  Select the task status: Active, Completed, Deferred, or Cancelled.
* **Task Importance** - Select the task importance: Low or Normal.
* **Remove Task Responsibles** - Remove the listed users from the task.
* **Add Task Responsibles** - Add the listed users to the task.
* **Due Date** - Select the date the task is due.
* **Work On Weekends** - When selected, allows work on Saturday and Sunday.

## Ticket Additional Settings

These fields are optional.

* **Create task even if no new assets are found in the query** - Enable this to try and create/update a task even if no new assets were retrieved from the last query run.
* **Add default report description** - Enable this to add a default report to the task description. The report will be in the following format:

```
Alert - "{EC Name}" for the following query has been triggered: {Query Name}
Alert Details
The alert was triggered because: {Trigger Reason}
The number of results returned by the query: {Results Number}
The previous number of results was: {Previous Results Numbers}
You can view the query and its results here: {Query Link}
Affected devices:
{Devices Names}
```

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the Wrike server.

  * **Permanent Access Token** - A permanent access token never expires, so you can obtain it once and then use it without the need to refresh or re-authenticate. For information on how to obtain a permanent access token, see [OAuth 2.0 Authorization under Permanent Access Token](https://developers.wrike.com/oauth-20-authorization/).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).