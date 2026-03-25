# Source: https://docs.axonius.com/docs/dell-unisphere.md

# Dell Unisphere For Unity

Dell Unisphere for Unity enables Dell EMC Unity customers to manage storage systems.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Dell Unisphere For Unity server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![DellUnisphereAdapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DellUnisphereAdapter.png)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## APIs

Axonius uses the [Unisphere Management REST API](https://www.dell.com/support/manuals/en-il/unity-400f/unity_p_restapi_prog_guide/the-unisphere-management-rest-api?guid=guid-a2e37655-3818-489f-8305-27e73d93fdf5\&lang=en-us).

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0