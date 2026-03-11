# Source: https://docs.axonius.com/docs/qualys-execute-script.md

# Qualys - Execute Script

**Qualys - Execute Script** executes a script in Qualys on the assets that match the query parameters or the assets selected on an asset page.

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
* **Use stored credentials from the Qualys Cloud Platform adapter** - Select this option to use the the first connected adapter credentials.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure a [Qualys Cloud Platform](/docs/qualys-cloud-platform) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Script ID** - Qualys Script ID to be run.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Qualys Cloud Platform domain** - The domain on the Qualys Cloud Platform server.

  * **User Name** and **Password** - The user name and password for an account that has permissions to run scripts on machines.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## Required Ports

Axonius must be able to communicate with the values supplied in **Connection Parameters** via the following ports:

* 80
* 443

## Required Permissions

The credentials used to connect to Qualys must be able to execute scripts.

## APIs

Axonius uses the [Qualys API Doc - Search for Execute Scripts On Demand](https://cdn2.qualys.com/docs/qualys-car-api-user-guide.pdf) API.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).