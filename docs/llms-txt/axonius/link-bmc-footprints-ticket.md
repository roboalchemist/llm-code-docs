# Source: https://docs.axonius.com/docs/link-bmc-footprints-ticket.md

# Link BMC FootPrints Ticket

**Link BMC FootPrints Ticket** links tickets in BMC Footprints for:

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

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the BMC Footprints adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      Note

      To use this option, you must successfully configure a [BMC FootPrints](https://docs.axonius.com/axonius-help-docs/docs/bmc-footprints) adapter connection.
    </Callout>

* **first\_ticket\_id** - The unique numerical identifier (Record ID) of the first ticket in the relationship.

* **first\_ticket\_definition\_id** - The unique internal identifier (Record Definition ID) specifying the type of the first ticket.

* **second\_ticket\_id** - The unique numerical identifier (Record ID) of the second ticket in the relationship.

* **second\_ticket\_definition\_id** - The unique internal identifier (Record Definition ID) specifying the type of the second ticket.

* **link\_type\_name** - The descriptive name of the relationship type that defines the connection between the two tickets.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Ticket Main Settings

These fields are optional.

* **Submitter** - The user who created and submitted the ticket into the FootPrints system.

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the BMC FootPrints server.
  * **User Name** and **Password**  - The credentials for a user account that has the  Required Permissions to fetch assets.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses BMC FootPrints Service Core Web Services.

## Required Ports

Axonius must be able to communicate via the following ports:

* TCP port 80/443

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).