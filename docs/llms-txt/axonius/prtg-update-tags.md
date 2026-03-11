# Source: https://docs.axonius.com/docs/prtg-update-tags.md

# PRTG - Add/Remove Tags

**PRTG - Add/Remove Tags** manages tags in the PRTG Network Monitor for:

* Assets that match the parameters of the selected saved query, and match the Enforcement Action Conditions, if defined, or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  To use this Enforcement Action, you must successfully configure a [PRTG Network Monitor](/docs/prtg-network-monitor) adapter connection.
</Callout>

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Use stored credentials from the PRTG Network Monitor adapter** - Select this option to use credentials stored as an adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The host name or IP address of the PRTG Network Monitor server.

  * Fill in one of the following:

  * **User Name** and **Passhash** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this Enforcement Action.

  * **API Token** - Enter the API token related to the user name and passhash.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Tags To Add** - Enter the tags to add.
* **Tags To Remove** - Enter the tags to remove.
* **Should Overwrite Existing Tags** - When selected, all existing tags are removed and replaced with the new tags listed in **Tags to Add**.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Application Programming Interface (API) Definition | PRTG Manual ](https://www.paessler.com/manuals/prtg/application_programming_interface_api_definition) API.

## Required Ports

Axonius must be able to communicate with the values supplied in **Connection Parameters** via the PRTG Network Monitor server port.

## Required Permissions

The stored credentials, or those provided in Connection and Credentials, must have API permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).