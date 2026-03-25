# Source: https://docs.axonius.com/docs/mosyle.md

# Mosyle

Mosyle is an Apple Endpoint Management & Security platform with solutions for education providers and enterprises.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://businessapi.mosyle.com`)* - The hostname or IP address of the Mosyle server.
2. **User Name** and **Password** *(optional)* - The credentials for a user account that has Permissions to fetch assets. The user name should be in the format of an Email address of the Mosyle user.
3. **Access Token** *(required)* - A Java Web Token with permission to fetch assets. To generate this new token refer to [configuring settings](https://community.incidentiq.com/asset-management-65/mosyle-asset-mdm-configuring-settings-170).

<Callout icon="📘" theme="info">
  Note

  Starting February 8 2024, all Mosyle API authentication must be performed using a JWT token. Authentication via JWT token is supported from Axonius 6.1.4.3. After upgrading to this version or higher you need to generate a new JWT token in Mosyle and update the adapter to use this new token.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Mosyle.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/mosyle.png" />

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**: HTTPS

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch device groups** - Select this option to fetch device groups.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Use the Mosyle Business API and enable API integration in Mosyle under 'Organization `>` API Integration `>` enable the profile'.

## Supported From Version

Supported from Axonius version 4.4