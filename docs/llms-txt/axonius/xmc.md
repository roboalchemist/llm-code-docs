# Source: https://docs.axonius.com/docs/xmc.md

# XMC Extreme Management Center

XMC Extreme Management Center is a wired and wireless network management and automation software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the XMC Extreme Management Center server.

2. **Port** *(optional, default: 8443)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="XMC_Extreme_Management_Center" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/XMC_Extreme_Management_Center.png" />

## APIs

Axonius uses the Northbound API.

## Required Permissions

The value supplied in [User Name](#parameters) must have Read-only permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                 | Supported | Notes |
| --------------------------------------- | --------- | ----- |
| Extreme Management Center Version 8.4.3 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5