# Source: https://docs.axonius.com/docs/halo-create-ticket.md

# Halo - Create Ticket

**Halo - Create Ticket** creates a HaloITSM ticket for:

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

These fields are required to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Split Tickets By** - When enabled, group assets into different tickets based on a shared attribute. Click the adapter icon to select an adapter (or Aggregated), and then click the **Select Adapter Field** box to select the asset field used to generate a separate ticket for each unique value.

  <Callout icon="📘" theme="info">
    Note

    * The **Split Tickets By** option appears only in ticket creation actions, and does not appear in ticket-per-asset creation or ticket update actions.
    * For assets containing multiple values, the system uses only the first value to perform the split.
  </Callout>

<br />

* **Use stored credentials from HaloITSM Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.
  <br />

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [HaloITSM](/docs/haloitsm) adapter connection.
</Callout>

* **Summary** *(default: New Ticket)* - A concise description of the ticket.
* **Details** *(default: This is a ticket created by Axonius.)* - A complete description of the ticket.
* **Ticket Type ID** *(default: 0)* - The specific ID for the ticket's type.
* **Ticket Category** *(default: Category 1)* - The category the ticket falls under.
* **Impact** *(default: 0)* - The impact level of the ticket (string or number). 0 is the lowest.
* **Urgency** *(default: 0)* - The urgency level of the ticket (string or number). 0 is the lowest.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional  Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Map Axonius fields to Halo fields** - Use the Field Mapping Wizard to transfer data from Axonius assets directly into standard Halo ticket fields. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily. For details, see [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping).

  * **Map Axonius fields to Halo custom fields** - Use the Field Mapping Wizard to transfer data from Axonius assets directly into Halo custom fields. Similar to the above field, but for custom fields you've created within your HaloITSM system.

  * **Host Name or IP Address** - The hostname or IP address of the HaloITSM server.

  * **Client ID** and **Client Secret**   - The credentials for a user account that has permissions to perform this Enforcement Action.

  * **Tenant** - Specifies the tenant in the URL. Used only with hosted solutions of Halo.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Halo REST API](https://halo.haloservicedesk.com/apidoc/info).

## Required Ports

Axonius must be able to communicate via the following port:

* 443

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).