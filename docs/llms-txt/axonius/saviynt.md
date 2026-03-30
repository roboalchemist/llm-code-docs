# Source: https://docs.axonius.com/docs/saviynt.md

# Saviynt Security Manager

Saviynt Enterprise Identity Cloud is a cloud identity and access governance platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Saviynt Security Manager server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. **API version** *(required, default: api/v5)*
   * Select **api/v5** for SSM 5.2 or newer versions.
   * Select **api** for older versions of SSM.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Saviynt Security Manager](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Saviynt%20Security%20Manager.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fields to skip** - From the dropdown select fields to ignore for user data.
2. **Fetch attestations and entitlements** - Select this option to fetch attestation and entitlement data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Saviynt Security Manager API](https://documenter.getpostman.com/view/1797923/RWaLwo21?version=latest).

## Supported From Version

Supported from Axonius version 4.5