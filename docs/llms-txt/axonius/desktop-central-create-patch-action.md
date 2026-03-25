# Source: https://docs.axonius.com/docs/desktop-central-create-patch-action.md

# ManageEngine Endpoint (Desktop) Central and Patch Manager Plus - Create Patch Action

**ManageEngine Endpoint (Desktop) Central and Patch Manager Plus - Create Patch Action** performs an install or uninstall of a software patch on:

* Assets returned by the selected query or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Notes

  * This Enforcement Action only works with assets from DesktopCentral that have a resource ID.

  * This Action requires the ManageEngine license for *Patch Manager Plus*.
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

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the ManageEngine Endpoint (Desktop) Central and Patch Manager Plus adapter** - Select this option to use **[ManageEngine Endpoint (Desktop) Central and Patch Manager Plus](/docs/manageengine-desktop-central)** connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [ManageEngine Endpoint (Desktop) Central and Patch Manager Plus](/docs/manageengine-desktop-central) adapter connection.
</Callout>

* **Patch IDs** - Enter the IDs of the patches to be applied.
* **Patch Configuration Name** - Enter the patch configuration name.
* **Patch Action** - Select the action to perform:
  * **install** - Install the patch.
  * **uninstall** - Uninstall the patch.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Fetch Desktop Central Data** - Fetch data from Desktop Central.
* **MFA QR Code** - Click **Upload File**, select the QR code file and click **Open**.
* **OAuth Client ID** - Enter the OAuth Client ID.
* **OAuth Client Secret** - Enter the OAuth Client Secret.
* **OAuth Refresh Token** - Enter the OAuth Refresh Token.
* **OAuth Zoho Accounts URL** *(default: `https://accounts.zoho.com`)* - Enter the OAuth Zoho accounts URL.
* **MSP Customer ID** -  Enter the MSP Customer ID.
* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **API Version** - Select the API version to use.
* **Patch Configuration Description** - Enter a description of the patch configuration.
* **Create patch per entity connection** - When selected, a patch is created for each connection.

<Callout icon="📘" theme="info">
  Notes

  * When **Create patch per entity connection** is selected, the credentials from **Use stored credentials from ManageEngine...** will be ignored as well as any other Enforcement Action credentials.

  * When **Use stored credentials from ManageEngine...** is toggled **on** and **Create patch per entity connection** is **not** selected, the Action will create one patch.

  * When **Use stored credentials from ManageEngine...** is toggled **off** and **Create patch per entity connection** is **not** selected, the Action will create patches for configured Action credentials.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Domain** - Enter the ManageEngine domain. For more details, see [ManageEngine Endpoint (Desktop) Central and Patch Manager Plus](/docs/manageengine-desktop-central).

  * **Port** *(default: 8020)* - Enter the port to use to apply the patch.

  * **User Name Domain** - Enter the user name domain for ManageEngine.

  * **User Name** - Enter the user name used to access ManageEngine.

  * **Password** - Enter the password used to access ManageEngine.

  * **Domain Authorization Token** - Enter the domain authorization token.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

## APIs

Axonius uses the [ManageEngine Endpoint Central API - SoM Summary](https://www.manageengine.com/patch-management/api/apd-patch-management.html) API.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).