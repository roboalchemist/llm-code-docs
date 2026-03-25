# Source: https://docs.axonius.com/docs/firemon-asset-manager.md

# FireMon Asset Manager

FireMon Asset Manager is a network visibility solution for cyber situational awareness and compliance monitoring.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the FireMon Asset Manager server.

2. **Auth Method** - Select an Authentication method, either **User Name and Password** (default) or **API Key**.
   * **User Name** and **Password** - The credentials for a user account that has permission to fetch assets.
   * **Client Secret** - The client credentials for a user account that has permission to fetch assets.

3. **Zone Name** *(required)* - The name of the zone from which to fetch data.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![FireMon Asset Manager](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FireMon%20Asset%20Manager.png)

## APIs

Axonius uses the Asset Manager API. See /api/rest/zonedata/devices.

## Supported From Version

Supported from Axonius version 6.1