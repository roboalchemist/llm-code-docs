# Source: https://docs.axonius.com/docs/teamviewer.md

# TeamViewer

TeamViewer is remote access and remote control computer software, allowing maintenance of computers and other devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the TeamViewer server.  To work with the TeamViewer Cloud Hosted Application use webapi.teamviewer.com as the Host Name.

2. **Token** *(required)* - An access token associated with a TeamViewer script that has the [Required Permissions](/docs/teamviewer#required-permissions) to fetch assets.
   To create a token, see [TeamViewer API Documentation](https://www.teamviewer.com/en/for-developers/#api-documentation-section).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="TeamViewer" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TeamViewer.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch managed groups' devices** - Select this option to fetch devices assigned to all groups.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the:

* [TeamViewer Web API](https://webapi.teamviewer.com/api/v1/docs/index)
* [TeamViewer API](https://community.teamviewer.com/English/kb/articles/3682-teamviewer-api)

The adapter should reach the following endpoints:

* [https://webapi.teamviewer.com/api/v1/account](https://webapi.teamviewer.com/api/v1/account)
* [https://webapi.teamviewer.com/api/v1/devices](https://webapi.teamviewer.com/api/v1/devices)

## Required Permissions

The value supplied in [Token](#parameters) must be associated with one of the following product plans that have permissions to read user information:

* Business
* Premium
* Corporate
* Tensor

The following permissions are required:

* **Account Management `>` View Account Data**
* **User Management `>` View Users**
* **Computer & Contacts `>` View Entries**

## Supported From Version

Supported from Axonius version 4.5