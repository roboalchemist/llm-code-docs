# Source: https://docs.axonius.com/docs/dell-unisphere-powermax.md

# Dell Unisphere for PowerMax

Dell Unisphere for PowerMax is a management tool for administering and monitoring PowerMax storage arrays.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Dell Unisphere for PowerMax server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information about authorization, see [Setting up user authentication](https://developer.dell.com/apis/4458/versions/9.2/docs/Tasks/setting_up_user_authentication.md).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Dell Unisphere for PowerMax](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dell%20Unisphere%20for%20PowerMax.png)

## APIs

Axonius uses the SLOProvisioning endpoint in the [Dell Unisphere for PowerMax 9.2 REST API](https://developer.dell.com/apis/4458/versions/9.2/openapi.json).

## Required Permissions

You must have a user who has GET access to the arrays as listed in [Storage array access](https://developer.dell.com/apis/4458/versions/9.2/docs/Tasks/setting_up_user_authentication.md).

## Supported From Version

Supported from Axonius version 6.1