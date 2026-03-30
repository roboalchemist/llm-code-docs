# Source: https://docs.axonius.com/docs/thycotic-pm.md

# Delinea Privilege Manager (Thycotic)

Delinea Privilege Manager (formerly Thycotic) mitigates malware and security threats from exploiting applications by removing local administrative rights and enforcing least privilege on endpoints.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Delinea Privilege Manager server.

2. **API Client** and **API Secret** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Search Object ID** *(required, default: 27c3943d-d46c-4801-bb06-b3fa416756f6)* - Enter the ID for the object of the search query. This option is available for legacy support and shouldn't be changed unless the object ID is changed in later versions.

4. **Verify SSL**  - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![DelineaPrivilegeManager](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DelineaPrivilegeManager.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced Settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch extra item information** *(optional)* - Select whether to fetch additional information regarding users and devices, such as IP addresses.
2. **Fetch device policies** *(optional)* - Select whether to fetch device security policies applied by Delinea.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Delinea Privilege Manager API](https://delinea.com/products/privilege-manager/).

## Supported From Version

Supported from Axonius version 4.5