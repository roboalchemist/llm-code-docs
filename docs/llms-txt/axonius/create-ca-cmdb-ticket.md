# Source: https://docs.axonius.com/docs/create-ca-cmdb-ticket.md

# CA Service Management - Create Ticket

**CA Service Management - Create Ticket** creates a ticket in CA Service Management for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

* **Use stored credentials from CA Service Management Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [CA Service Management](/docs/ca-service-management) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="default">
  ### Connection Parameters

  When **Use stored credentials from the CA Service Management adapter** is toggled **Off**, these fields are required:

  * **CA CMDB Domain** - The hostname or IP address of the CA Service Management server.

  * **Username** and **Password** - The credentials for a user account that has the permissions to perform this action.
</Callout>

* **Incident description** - Enter a free text description of the incident.

* **Add default incident description** *(default: False)* - Select this option to include the default incident description at the end of the ticket body.
  The incident description message includes the Enforcement Set name and triggered query, the Dynamic Value statement that is applied when executing the Enforcement, if such exists, and the number of current and previous results.

<Callout icon="📘" theme="info">
  Message example

  Alert - "test" for the following query has been triggered: Missing Sophos

  Alert Details
  The alert was triggered because: The number of entities is above 0
  The number of devices returned by the query: 4
  The previous number of devices was: 4

  You can view the query and its results here: [https://demo-latest.axonius.com/devices?view=Missing](https://demo-latest.axonius.com/devices?view=Missing) Sophos
</Callout>

* **Problem type** - Enter a full description of the issue. Required by the CA CMDB API.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [createTicket Method](https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/ca-service-management/17-2/reference/ca-service-desk-manager-reference-commands/technical-reference/createticket-method.html) API.

For more details about other enforcement actions available, see [Action Library](/docs/action-library).