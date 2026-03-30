# Source: https://docs.axonius.com/docs/check-point-management.md

# Check Point Management

Check Point Management is a centralized solution for configuring, managing, and monitoring Check Point security policies and devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Networks

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Check Point Management server.

2. **Auth Method** - Select an Authentication method, either **User Name and Password** (default) or **API Key**.
   * **User Name** and **Password** - The credentials for a user account that has permission to fetch assets.
   * **API Key** - An API Key associated with a user account that has permissions to fetch assets.

3. **Port** *(optional, default: 443)* - The port used for the connection.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Check Point Management" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Check%20Point%20Management.png" />

## APIs

Axonius uses the [Check Point Management API](https://sc1.checkpoint.com/documents/latest/APIs/?#introduction~v2%20).

## Supported From Version

Supported from Axonius version 6.1.46.0