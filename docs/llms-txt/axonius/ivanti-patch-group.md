# Source: https://docs.axonius.com/docs/ivanti-patch-group.md

# Ivanti Security Controls - Patch Group

**Ivanti Security Controls - Patch Group**  adds CVEs to the Patch Group or updates the Patch Group CVEs from:

* Aggregated Security Findings that match the results of the selected saved query, and match the Enforcement Action Dynamic Value statement, if defined; or assets selected on the Aggregated Security Findings page.
  The CVEs in the Patch Group determine what patches are applicable on the devices.

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

<Callout icon="📘" theme="info">
  Note

  This action runs on Aggregated Security Findings.
</Callout>

* **Use stored credentials from  Ivanti Security Controls adapter** - Select this option to use the Ivanti Security Controls connected adapter credentials.

  * When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.

  * When not enabled, see [Connection and Credentials](/docs/ivanti-patch-group#connection-and-credentials).

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [ Ivanti Security Controls](/docs/ivanti-security-controls) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Patch Group ID** - The ID of the Patch Group.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the **Ivanti Security Controls** server that  Axonius can communicate with via the [Required Ports](#required-ports).

  * **Port** *(default: 3121)* - The port on the on-prem server that is connected to the Ivanti Security Controls application.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to  perform this action.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Patch Deployments](https://help.ivanti.com/iv/help/en_US/isec/API/Topics/Patch%20Deployments.htm) API.

Learn more on [how to use the REST API](/docs/ivanti-security-controls#APIs).

## Required Ports

Axonius must be able to communicate with the value supplied in [Hostname or IP Address](#parameters) via the designated port (default: 3121).

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to vulnerabilities (Aggregated Security Findings in Axonius).

* The user must be a local or domain admin.

The values supplied in [Connection Settings](#parameters) above must have Read permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).