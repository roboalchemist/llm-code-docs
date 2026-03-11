# Source: https://docs.axonius.com/docs/remediant-secureone.md

# Remediant SecureONE (JITA)

Remediant SecureONE is a Just-In-Time Privileged Access Management (JITA) solution that enables control and insight over the distribution, usage, and protection of privileged access across enterprise environments.

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Remediant SecureONE server.

2. **User ID** and **API Token** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![Remediant\_SecureOne](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Remediant_SecureOne.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Number of requests to perform in parallel** *(required, default: 50)* - Specify the maximum parallel request all connections for this adapter will create when connecting the SecureONE server.
2. **Fetch full devices data**
   * If enabled, all connections for this adapter will fetch full devices data including the local admins from Remediant SecureONE.
   * If disabled, all connections for this adapter won't fetch full devices data from Remediant SecureONE.
3. **Ignore device without last seen** - Select to ignore devices that have no **Last Seen** information.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [SecureONE API](https://api-docs.remediant.com/?version=latest).

## Required Permissions

The value supplied in [User ID and API Token](#parameters) must have Read access to devices.
User ID refers to the internal ID of a SecureONE user the application wants to assume. The API key must be created with that User ID.