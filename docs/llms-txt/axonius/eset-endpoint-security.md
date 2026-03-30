# Source: https://docs.axonius.com/docs/eset-endpoint-security.md

# ESET Endpoint Security

ESET Endpoint Security is an anti-malware suite for Windows including web filtering, firewall, USB drive and botnet protection.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name** *(required)* - The hostname or IP Address of the ESET Endpoint Security management server.
2. **Port** *(optional, default: 2223)* - The required port. If not supplied, port 2223 will be used.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
4. **Is Domain User** *(required)*
   * If enabled, a domain user credentials must be specified. The user name format should be "DOMAIN\USERNAME".
   * If disabled, an ESET Endpoint Security 'internal' user credentials should be specified.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1408).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Exclude no 'Last Seen' devices** *(required, default: true)* - Select whether to exclude devices that do not have 'last seen' indication.
   * If enabled, all connections for this adapter will not fetch devices that do not have 'last seen' indication.
   * If disabled, all connections for this adapter will fetch devices, even those do not have 'last seen' indication.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1409).png" />

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>