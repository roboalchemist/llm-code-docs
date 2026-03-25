# Source: https://docs.axonius.com/docs/one-trust.md

# OneTrust

OneTrust is a privacy, security, and data governance platform that helps organizations manage compliance, risk, and data privacy.

The OneTrust adapter provides Axonius with visibility into your publicly accessible assets, including device, user, and group data

## Asset Types Fetched

* Devices
* Users
* Groups

## Before You Begin

### Required Ports

* TCP port 80/443

### Authentication Methods

* Client ID / Client Secret

### Required Permissions

The adapter connection requires a user account with the following permissions and access scopes configured within the OneTrust portal:

* `INVENTORY_READ` scope - This scope must be passed in the token request to allow the adapter to retrieve asset and inventory data.
* View Users and Groups - The credentials must be associated with a role (Viewer or higher) that has access to the User Management module to fetch identities and organizational structures.
* API access - The account must have permissions to generate and use OAuth 2.0 Client Credentials (Client ID and Client Secret) for external system integrations.

### APIs

Axonius uses the <Anchor label="OneTrust API" target="_blank" href="https://developer.onetrust.com/onetrust/reference/getlistofinventoriesbyfiltercriteriausingpost">OneTrust API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 6.1.64.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the OneTrust server.
2. **Client ID** and **Client Secret** - The credentials of a user account that has the [required permissions](/docs/one-trust#required-permissions) to fetch assets. For information on how to generate client credentials, see <Anchor label="Generate Access Token" target="_blank" href="https://developer.onetrust.com/onetrust/reference/getoauthtoken-1">Generate Access Token</Anchor>.

![onetrust](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-RM38T7CM.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

5. **API Gateway Connection** - Enable this option to use API gateway parameters for authentication. After enabling this option, under **API Gateway Type**, choose **Layer7** and fill in the displayed parameters (in addition to **Host Name or IP Address**). Read about [Layer7 API Gateway Parameters](/docs/adding-a-new-adapter-connection#layer7-api-gateway-parameters).

   <Callout icon="📘" theme="info">
     Note

     When you use an API gateway connection, the other authentication parameters are not required. However, to add the connection successfully, you need to enter placeholder values in these fields.
   </Callout>

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **Enable Custom Parsing** - Enable this option to define how to parse specific fields from the raw data fetched. You can choose to parse the data into an already existing field, or create a new one. This adapter supports **Device Custom Parsing**. See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.