# Source: https://docs.axonius.com/docs/intel-dcmc.md

# Intel DCMC

Intel® Data Center Manager is a software solution that collects and analyzes the real-time health, power, and thermals of a variety of devices in data centers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Intel DCMC server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has at least Read Only permissions to fetch assets.

3. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Intel_DCMC" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Intel_DCMC.png" />

## APIs

Axonius uses the DCM RESTful API.

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5