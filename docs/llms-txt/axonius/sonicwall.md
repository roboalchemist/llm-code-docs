# Source: https://docs.axonius.com/docs/sonicwall.md

# SonicWall

SonicWall next-generation firewalls (NGFW) provide security, control, and visibility to maintain an effective cybersecurity posture.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SonicWall server.
2. **Port** *(required, default: 443)* - The port Axonius will use to communicate with the SonicWall server.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
4. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../global-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
5. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
6. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="SonicWall.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SonicWall.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

**Do not fetch devices with no IP** *(required, default: False)* - Select whether to fetch devices which do not have an IP address.

<Image alt="SonicWallADv.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SonicWallADv.png" />

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [SonicWall SonicOS API 6.5.1](https://www.sonicwall.com/techdocs/pdf/sonicos-6-5-1-api-reference.pdf).

## Required Permissions

The value supplied in [User Name](#parameters) must have full admin privileges are allowed to access SonicOS API.

To enable SonicOS API through the management interface:

1. Navigate to **MANAGE | Network > Appliance | Base Settings**.
2. Scroll to the **SonicOS API** section.
3. Select **Enable SonicOS API**.
4. Click **Accept**.