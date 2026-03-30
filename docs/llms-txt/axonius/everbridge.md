# Source: https://docs.axonius.com/docs/everbridge.md

# Everbridge

Everbridge is an emergency notification and critical event management platform for communicating during incidents or crises.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Roles

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Everbridge server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets. For information on authentication, see [Authentication Types](https://developers.everbridge.net/home/docs/ebs-gs-guide-authentication-types).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Everbridge](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Everbridge.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch SecurityRoles from Role Details** - Toggle on this option to fetch SM SecurityRole objects from role details.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [EB Suite REST API](https://developers.everbridge.net/home/reference/ebs-get-user).

## Supported From Version

Supported from Axonius version 6.1