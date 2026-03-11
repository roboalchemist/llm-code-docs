# Source: https://docs.axonius.com/docs/glpi.md

# GLPI

GLPI is an open-source service management software tool to manage Helpdesk and IT assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Software, SaaS Applications

## Parameters

1. **Authentication Type** *(optional, default: Login Credentials)* - Select whether to authenticate by **Login Credentials** or **API Token**.
   * If **Login Credentials** is selected, enter your **User Name** and **Password**.
   * If **API Token** is selected, enter the API Token.

2. **User Name** and **Password** *(required if selected **Login Credentials** is **User Name**)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **API Token** *(required if selected **Authentication Type** is **API Token**)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To obtain an API Token for GLPI, select **Administration `>` Users >**  \<*User*> **> User `>` Remote access keys `>` API Token**.

4. **Host Name or IP Address** *(required)* - The hostname or IP address of the GLPI server.

5. **Application Token** *(optional)* - Enter the Authorization string provided by the GLPI API configuration.

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![GLPI](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GLPI.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Device types to fetch** *(required, default: Computer, Peripheral, Phone)* - From the dropdown select one or more types of devices to fetch.
2. **Enrich computer plugin fields** - Select this option to enrich Computers with additional plugin fields.
3. **Enrich computer installed software** - Select this option to enrich Computers with installed software.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [GLPI Developer API](https://glpi-developer-documentation.readthedocs.io/en/master/devapi/index.html).
Download an instance locally to test and access the documentation.

## Required Permissions

The value supplied in [User Name](#parameters) or [API Token](#parameters) must have permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                               | Supported | Notes |
| ------------------------------------- | --------- | ----- |
| Developed and tested with GLPI 10.0.3 | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7