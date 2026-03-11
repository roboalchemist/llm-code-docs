# Source: https://docs.axonius.com/docs/huawei-esight-21.md

# Huawei eSight 21.x

Huawei eSight is an enterprise operation and maintenance (O\&M) platform that provides cross-vendor and cross-product converged management, visualized monitoring, and intelligent analysis for enterprise ICT devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Huawei eSight server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Version** *(optional, default: For Version 21 Authentication)* - Select the version of Huawei eSight you want to connect to, either Version 21 or Version 10.

   * **For Version 21 Authentication**:
     * **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   * **For Version 10 Authentication**
     * **User ID** and **Password Value** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **API port** *(required, default: 443)* - The port used for the connection.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Huawei%20eSight%2021.x(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Huawei%20eSight%2021.x(1).png" />

## APIs

Click to see the APIs used by this adapter.

Axonius uses the following APIs:

* [eSight 20.1 Auth API](https://support.huawei.com/enterprise/br/doc/EDOC1100199653/ad9ec466/auth)
* [eSight 20.1 Network Management API](https://support.huawei.com/enterprise/br/doc/EDOC1100199653/67966e82/network-management#:~:text=basic%20information%20query.-,Querying%20Asset%20Information,-Functions)
* [eSight 20.1 Server Management API](https://support.huawei.com/enterprise/br/doc/EDOC1100199653/3c28ddf/server-management#:~:text=Server%20Device%20Ports-,Obtained%20Server%20List,-Functions)
* [eSight 20.1 Storage Device Management API](https://support.huawei.com/enterprise/br/doc/EDOC1100199653/d3dbe8c5/storage-device-management#:~:text=and%20Other%20Information-,Querying%20the%20Storage%20Device%20List,-Functions)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0