# Source: https://docs.axonius.com/docs/xen-server.md

# XenServer

XenServer is a virtualization platform that enables the creation and management of virtualized server infrastructures.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the XenServer server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![XenServer.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/XenServer.png)

## APIs

Axonius uses the following APIs through XenServer SDK:

* [https://docs.xenserver.com/en-us/xenserver/developer/sdk-guide/python](https://docs.xenserver.com/en-us/xenserver/developer/sdk-guide/python)
* [https://github.com/xenserver/xenserver-samples/tree/master/python](https://github.com/xenserver/xenserver-samples/tree/master/python)

## Supported From Version

Supported from Axonius version 6.1.64