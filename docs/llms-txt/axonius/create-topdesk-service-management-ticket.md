# Source: https://docs.axonius.com/docs/create-topdesk-service-management-ticket.md

# TOPdesk Enterprise Service Management - Create Ticket

**TOPdesk Enterprise Service Management - Create Ticket**  creates a ticket in TOPdesk and attaches a .csv file of:

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

* **Use stored credentials from TOPdesk Enterprise Service Management adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [TOPdesk Enterprise Service Management](/docs/en/topdesk) adapter connection.
</Callout>

* **Incident Type** - Select the TOPdesk Incident Type.
* **Caller Email** - Specify the caller's email address.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="📘" theme="info">
  Note

  In order for TOPdesk tickets to be created correctly, you have to make sure you fill in the parameters **with existing options** exactly as they appear in TOPdesk.
</Callout>

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** – The hostname of the TOPdesk server. Required when there is more than one connection.

  * **User Name or Application Name** – Specify the User Name or Application Name. Required when there is more than one connection.

  * **Password** - Enter the password for the account used to access TOPdesk.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Brief Description** - Enter a brief description to add to the ticket.
* **Request Details** - Enter the request details. This field fills the large text box in the TOPdesk ticket creation page.
* **Add results to request details** - Select this option to add the results of the action to the Details field in the TOPdesk incident.
* **Entry** - The method of entry. The parameter must exactly match an existing option in TOPdesk.
* **Call Type** - Enter the call type exactly as it appears in TOPdesk.
* **Category** - Enter an incident category exactly as it appears in TOPdesk.
* **Subcategory** - Enter an incident subcategory exactly as it appears in TOPdesk.
* **Object ID** - Enter an object ID. The parameter must exactly match an existing option in TOPdesk.
* **Impact** - The impact level of the problem that is the basis of the ticket. The parameter must exactly match an existing option in TOPdesk.
* **Urgency** - The urgency level of the ticket. The parameter must exactly match an existing option in TOPdesk.
* **Priority** - The priority of the ticket. The parameter must exactly match an existing option in TOPdesk.
* **Operator Group** - Enter an operator group exactly as it appears in TOPdesk.
* **Operator** - Enter an operator name exactly as it appears in TOPdesk.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version                   | Supported | Notes |
| ------------------------- | --------- | ----- |
| Topdesk API v3 and higher | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).