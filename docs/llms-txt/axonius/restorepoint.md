# Source: https://docs.axonius.com/docs/restorepoint.md

# Restorepoint

Restorepoint is a platform that automates network configuration backup, recovery, change auditing, and compliance analysis for multiple vendors.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Restorepoint server.

2. **Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](/docs/restorepoint#required-permissions) to fetch assets. For instructions on how to generate the Token, see [here](https://docs.sciencelogic.com/restorepoint/api/5-6/api.html#section/Authentication/Token).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![restorepoint connection parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-HKYJA0UA.png)

## APIs

Axonius uses the [Restorepoint API](https://docs.sciencelogic.com/restorepoint/api/5-6/api.html#section/Authentication).

## Required Permissions

The user account used for connection must have the `ViewDevices` permission to fetch assets.
You can find the full list of Restorepoint permissions [here](https://docs.sciencelogic.com/restorepoint/api/5-6/api.html#section/Authentication/Permissions).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version   | Supported | Notes |
| --------- | --------- | ----- |
| Version 2 | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1