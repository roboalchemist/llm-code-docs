# Source: https://docs.axonius.com/docs/desktop-central-create-software-action.md

# ManageEngine Endpoint (Desktop) Central and Patch Manager Plus - Create Software Action

**ManageEngine Endpoint (Desktop) Central and Patch Manager Plus - Create Software Action** performs an install or uninstall of a software on:

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

* **Use stored credentials from the ManageEngine Endpoint (Desktop) Central and Patch Manager Plus adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [ManageEngine Endpoint (Desktop) Central and Patch Manager Plus adapter](/docs/manageengine-desktop-central) connection.
</Callout>

* **OS Type** - Select between Windows, Mac, and Linux.
* **Package IDs** - Enter the unique IDs of the software packages you want to use in the action.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Domain** - The hostname or IP address of the ManageEngine Endpoint Central or Patch Manager server.
    For cloud Endpoint/Desktop Central use: `desktopcentral.manageengine.com`
    For cloud Patch Manager Plus use: `patch.manageengine.com`
  * **Port** *(default: 8020)* - The port Axonius will use to communicate with the server (for cloud use 443).
  * **User Name** and **Password** - The credentials for a user account that has permissions to fetch assets. For details, see [Authentication and Authorization for On-Prem Instances](#Authentication-and-Authorization-for-On-Prem-Instances).

  <Callout icon="📘" theme="info">
    Note

    When **OAuth Client ID**,  **OAuth Client Secret**  and  **OAuth Refresh Token** are not supplied, **User Name** and **Password** are required.
  </Callout>

  * **User Name Domain** *(optional)* - The AD domain. Use this option if you are using the AD authentication method.
  * **OAuth Client ID**,  **OAuth Client Secret**,  and  **OAuth Refresh Token** - The parameters for OAuth authentication, used in the cloud version of ManageEngine Endpoint Central and Patch Manager Plus. Refer to [APIs](#apis) for information on how to generate them.
  * **OAuth Zoho Accounts URL** *(default: `https://accounts.zoho.com`)* - The account URL for your Zoho account. Refer to [Refresh Access Tokens](https://www.zoho.com/crm/developer/docs/api/v2/refresh.html) for information on how to obtain the account URL.

  <Callout icon="📘" theme="info">
    Note

    When **User Name** and **Password** are not supplied, **OAuth Client ID**,  **OAuth Client Secret**,  and  **OAuth Refresh Token** are required.
  </Callout>

  * **Domain Authorization Token** - Token to access the AD domain.
  * **Fetch Desktop Central Data** *(default: enabled)* - Select this parameter to fetch desktop central data. If you do not select this option, only patch data is fetched (patch data is available from both products).
  * **MFA QR Code** *(optional)* - If MFA is enabled using Google Authenticator, save the QR code received as a PNG file and upload it.
    * If supplied, the connection for this adapter will use the uploaded file to authenticate the specified **User Name** and **Password**.
    * If not supplied, the connection for this adapter will not add any additional authentication to the specified **User Name** and **Password**.
  * **MSP Customer ID** - Customer ID to fetch information for, when connecting to Endpoint Central MSP.  Only use this when connecting to Endpoint Central MSP, otherwise leave empty.
  * **API Version** - Select the API version, either 1.3 or 1.4 (Beta).
  * **DC Instance** - The ID used to add to the headers for the API calls, if specified.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Configuration Name** - Enter a name for this configuration.

* **Operation Type** - Select between *install* and *uninstall*.

* **Install As** - Select between *system* and *run as user*.

* **Template ID** - Enter the Deployment Policy ID.

* **Custom Resource Domain** - Enter the custom resource domain.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [ManageEngine Endpoint Central API - SoM Summary API](https://www.manageengine.com/patch-management/api/apd-patch-management.html).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).