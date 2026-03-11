# Source: https://docs.axonius.com/docs/blackberry-unified-endpoint-management-uem.md

# BlackBerry Unified Endpoint Management (UEM)

BlackBerry Unified Endpoint Management (UEM) delivers endpoint management and policy control for devices and apps on-premise or in the cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Software, SaaS Applications

## Parameters

1. **Blackberry UEM Domain** *(required)* - The hostname of the Blackberry UEM server.

2. **Tenant ID** *(required)* - The organization’s tenant ID (previously known as SRPID), also referred to as 'tenantGuid' in web service routes.
   * Ask your organization’s UEM administrator for the tenant ID of the UEM domain. The administer would have specified the tenant ID during the UEM installation process.
   * The administrator can also scan the log file for the BlackBerry UEM Core component for the 'tenantID'.

3. **Port** *(required, default: 18084)* - Use the default value.

4. **User Name** and **Password** *(required)* - The user name and password for a UEM administrator account. The REST Web Services require the login information for an administrator account to enable remote administration of the UEM domain. This adapter support OAuth authentication. Enter your  OAuth creds the corresponding fields,  the Client ID into Username and the Client Secret into Password.

5. **User Name Domain** *(optional)* - The user name domain.
   * If supplied, Axonius will use the specified domain when connecting to the host defined for this connection.
   * If not supplied, Axonius will only user the user name and the password specified when connecting to the host defined for this connection.

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Blackberry\_UEM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Blackberry_UEM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch external data for devices** - Select whether to fetch external data for each device and simple user information for each device.
2. **Fetch IT policies** - Select whether to fetch user IT policies for each device.
3. **Fetch Users** - Select whether to fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [BlackBerry UEM Web Services API](https://developer.blackberry.com/files/bws/reference/blackberry_uem_12_10_rest/).