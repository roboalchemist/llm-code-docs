# Source: https://docs.axonius.com/docs/aternity.md

# Aternity

Aternity is a device performance monitoring solution that provides insights into performance and health of laptops, desktops, VDI, and mobile devices, along with self-healing capabilities to automatically resolve issues.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Aternity server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1637\).png)

## APIs

Axonius uses the following APIs:

* [Device Inventory - REST API (version 2.0)](https://help.aternity.com/bundle/console_user_guide_12y_console_saas/page/console/topics/console_api_odata_device_inventory.html)
* [Deployed Applications on All Devices - REST API (Installed Software) (version 2.0)](https://help.aternity.com/bundle/console_user_guide_12y_console_saas/page/console/topics/console_api_odata_installed_software.html)

## Required Permissions

The value supplied in [User Name](#parameters) must have the OData REST API role.
For details, see [Aternity - Add Users or Edit a User](https://help.aternity.com/bundle/console_admin_guide_x_console_saas/page/console/topics/console_admin_users_add.html).

<Callout icon="📘" theme="info">
  NOTE

  If the supplied user is an SSO user, you must generate a password for them, as Aternity's REST API does not authenticate with your enterprise's identity provider.
</Callout>

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version              | Supported | Notes |
| -------------------- | --------- | ----- |
| Aternity REST API V2 | Yes       |       |