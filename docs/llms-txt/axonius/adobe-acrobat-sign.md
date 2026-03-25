# Source: https://docs.axonius.com/docs/adobe-acrobat-sign.md

# Adobe Acrobat Sign

Adobe Sign allows users to create, edit, collaborate, e-sign, and share PDFs, on any device.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Adobe Acrobat Sign server.

2. **Integration  Key** *(required)* - An Integration Key associated with a user account that has permissions to fetch assets. Refer to [How to create an integration key](https://helpx.adobe.com/sign/kb/how-to-create-an-integration-key.html) for instructions for more information.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![AdobeAcrobatSign](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdobeAcrobatSign.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch full data per user** - Select this option to fetch full data per user.
2. **Fetch user groups** *(required, default: false)*  - Select whether to fetch user groups.
3. **Fetch user last login date**  *required, default: false)* - Select whether to fetch the user's last login date.
4. **Filter users with the following User Status** - Enter a comma-separated list of users to filter with specified user statuses.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Acrobat Sign REST API Version 6](https://secure.na4.adobesign.com/public/docs/restapi/v6)

## Required Ports

Axonius must be able to communicate with the value supplied in [Integration Key](#parameters) via the following ports:

* **TCP port 80, 443**

## Required Permissions

The value supplied in [Integration Key](#parameters) must have user\_read permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                          | Supported | Notes |
| -------------------------------- | --------- | ----- |
| Acrobat Sign REST API Version 6) | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7