# Source: https://docs.axonius.com/docs/dell-powerprotect-dd-management-center.md

# Dell PowerProtect DD Management Center

Dell PowerProtect Data Domain Management Center is a centralized storage management solution that provides aggregate capacity, replication and performance management, and reporting.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Dell PowerProtect Data Domain Management Center server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
   To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![DellPowerProtectDDManagementCenter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DellPowerProtectDDManagementCenter.png)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## APIs

Axonius uses the [PowerProtect DD Management Center API Version 7.7](https://developer.dell.com/apis/4208/versions/7.7/docs/Introduction.md).

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0.