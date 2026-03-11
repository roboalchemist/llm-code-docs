# Source: https://docs.axonius.com/docs/create-and-update-manage-engine-device.md

# ManageEngine ServiceDesk Plus   - Create and Update Assets

**ManageEngine ServiceDesk Plus  - Create and Update Assets** creates a ManageEngine ServiceDesk Plus Asset, or updates ManageEngine ServiceDesk Plus Assets for:

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

* **Use stored credentials from ManageEngine ServiceDesk Plus adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [ManageEngine ServiceDesk Plus](/docs/manageengine-service-desk-plus) adapter connection.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Host Name or IP Address** - The hostname or IP address of the ManageEngine ServiceDesk Plus server that Axonius can communicate with.
* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

### Authentication Methods

Select Authentication method either **oAuth 2.0** or **Basic Authentication**.

* **Basic Authentication**:

  * **Technician key token** *(required)* - Use for on-prem deployment of ManageEngine ServiceDesk Plus (SDP). An API Key associated with a user account that has the  Required Permissions  to  perform this action.
    To obtain a technician key token, see [Generate a Technician Key Token](/docs/manageengine-service-desk-plus#generate-a-technician-key-token).

* **oAuth 2.0**
  Use for cloud deployment of ManageEngine ServiceDesk Plus (SDP).

  * **OAuth Client ID**, **OAuth Client Secret** and **OAuth Refresh Token** - Parameters for OAuth authentication used in the cloud version of ManageEngine ServiceDesk Plus. Refer to [Configuring OAuth Authentication](/docs/create-and-update-manage-engine-device#configuring-oauth-authentication) for information on how to generate them.
  * **OAuth Zoho Accounts URL** - Select the account URL, or add your own. Refer to [Refresh Access Tokens](https://www.manageengine.com/products/service-desk/sdpod-v3-api/getting-started/data-centers.html) for information on how to obtain the account URL.

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

* **Asset Product Name** *(only for new assets)* - Enter a name for the product.

* **Asset Product ID** *(only for new assets)* - Enter an ID for the product.

* **Use first IP address only** - When selected, adds only the first IP address to the ServiceNow asset. When not selected, all IP addresses are added.

* **Use first MAC address only** - When selected, only the first MAC address is added to the ServiceNow asset. When not selected, all MAC addresses are added.

* **Action Choice** - Select the Action you want to run: *Create*, *Create and Update*, or *Update*.

* **Exclude connections** - Select the adapter connections to exclude.

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses these APIs:

## Configuring OAuth Authentication

This adapter supports OAuth Authentication.

### Generating the **OAuth Client ID**,  **OAuth Client Secret**  and  **OAuth Refresh Token**

To use OAuth Authentication you need to generate the **OAuth Client ID**,  **OAuth Client Secret**  and  **OAuth Refresh Token**. To generate them:

1. Go to the Zoho API Console: [https://api-console.zoho.com/](https://api-console.zoho.com/)

2. Click 'Add client', choose 'Self Client' and click 'Create' (if a popup asks you to confirm, click “OK“).

3. On the API Console main page, click on the 'Self Client' application

4. In the tab 'Generate Code', enter the following details, and click 'Create':
   * Scope:
     * “SDPOnDemand.assets.CREATE,SDPOnDemand.assets.READ,SDPOnDemand.assets.UPDATE”
     * Time Duration: “10 minutes”
     * Scope Description: free text (could be anything)

5. A popup “Generated Code“  opens, click copy, and paste the code in a temporary file.

6. In the tab “Client Secret“, copy “Client ID“ and “Client Secret“ to a temporary file

7. Enter the values you’ve copied to the following command on a linux machine (or Windows with curl):

   ```TEXT
   curl -X POST "https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code&code=&client_id=&client_secret="
   ```

8. From the response of the command, copy the value of “refresh\_token“, and save it to a temporary file.

9. Copy the OAuth Client ID, OAuth Client Secret, OAuth Refresh Token to the appropriate places in the Configuration dialog.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).