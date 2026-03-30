# Source: https://docs.axonius.com/docs/update-tickets-jira.md

# Jira Service Management - Update Tickets

<Callout icon="💡" theme="warn">
  Note

  This Enforcement Action requires the Jira Service Management (JSM) Standard, Premium, or Enterprise license.
</Callout>

**Jira Service Management - Update Tickets** updates the relevant tickets for:

* Assets matching the Enforcement Set query or assets selected on the relevant asset page. For example, if the action is triggered on asset type=Users, the action updates tickets linked to each user.
  * When triggered on any asset type except Tickets (for example, Users, Devices), this action updates related ServiceNow tickets based on your selection in the **Select Which Related Tickets To Update** dropdown (see below).
  * When triggered on asset type=Tickets, this action runs on all tickets resulting from the selected query. The **Select Which Related Tickets To Update** dropdown is not applicable in this scenario.

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

* **Use stored credentials from  Jira Service Management (Service Desk) adapter** - Select this option to use the [Jira Service Management](/docs/atlassian-jira-service-desk) connected adapter credentials.

  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Jira Service Management (Service Desk)](/docs/atlassian-jira-service-desk) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Ticket Main Settings

These fields are optional.

* **Ticket Status** - Select a value for ticket status. You must configure the Jira Service Desk adapter in order to fetch the Ticket Status field values. If an adapter connection is not configured, you must provide the transition/status ID. This must be a number, not a string like ‘Done' or 'In Progress’.

* **Ticket Assignee** - Enter to whom the ticket is assigned.

* **Ticket Comments** - Enter comments related to the ticket.

* **Select Which Related Tickets To Update** - Relevant when this enforcement action runs on an asset category other than Tickets. Select which tickets to update.

## Ticket Additional Settings

These fields are optional.

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

## Connection and Credentials

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** -The hostname or IP address of the Jira Service Management server.

  * **Jira Service Management API version** - The Jira Service Management API number.

  * **User Name and API Token** - The credentials for a user account that has the permissions to read and write.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Use Cloud API** - Select this option to explicitly specify that the enforcement should use the Cloud API instead of Jira Server API. When the user is using the cloud API the default host name or IP address should be [https://api.atlassian.com](https://api.atlassian.com). Even when left unselected, the action will attempt to use the cloud API if the domain specified is “api.atlassian.com”.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Additional Fields

* **Additional fields (json format)** - Specify additional fields to be added as part of the incident as key/value pairs in a JSON format.
  * For example:

    ```
    {"field1": "value1", "field2": "value2"}
    ```
* **Allow update tickets using JIRA Fetch Tickets Adapter only** - When selected, tickets are updated using only the [Jira Service Management (Service Desk) Fetch Tickets](https://docs.axonius.com/axonius-help-docs/docs/jira-fetch-tickets) adapter.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Action privileges

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).