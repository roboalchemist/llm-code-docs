# Source: https://docs.axonius.com/docs/netiq-im.md

# NetIQ Identity Manager

NetIQ Identity Manager by MicroFocus uses integrated identity information to create and manage identities and control access to enterprise resources.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the NetIQ Identity Manager server.
2. **Port** *(required)* - The port used for the connection.
3. **Client ID** and **Client Password** *(required)* - The Client ID and Client Password.
4. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  **Client ID**, **Client Password**, **User Name** and **Password** are all required to  configure the connection.
</Callout>

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

10. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![NetIQIDentityMaker](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetIQIDentityMaker.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch groups** - Select this option to fetch groups and associate users with them.
2. **Fetch assignments** - Select this option to fetch Roles and Permissions and associate users with them.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [NetIQ Identity Manager REST API](https://www.netiq.com/documentation/identity-manager-developer/rest-api-documentation/idmappsdoc/).

## Supported From Version

Supported from Axonius version 4.5