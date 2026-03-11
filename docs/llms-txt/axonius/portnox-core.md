# Source: https://docs.axonius.com/docs/portnox-core.md

# Portnox CORE

Portnox CORE is a software-based solution that runs on Windows Servers (physical and virtual) to continually communicate with all existing networking infrastructure, gaining complete visibility into all assets currently connected to the network.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Portnox CORE server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PortnoxCOre](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PortnoxCOre.png)

## APIs

Axonius uses the [Portnox CORE 4.0 API](https://portnox.app.box.com/v/ngxuserguide).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [User Name](#parameters) must have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0