# Source: https://docs.axonius.com/docs/extreme-networks-extremecontrol.md

# Extreme Networks ExtremeControl

Extreme Networks ExtremeControl is a Network Access Control (NAC) solution that provides role-based access controls and reporting on user activity across all devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Extreme Networks ExtremeControl server.

2. **User ID** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Extreme Networks ExtremeControl.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Extreme%20Networks%20ExtremeControl.png)

## APIs

Axonius uses the [ExtremeCloud REST API](https://api.extremenetworks.com/extremecloud/rest_api/index.html?_ga=2.203460948.539865667.1594032983-1920910494.1594032983).

## Required Permissions

The value supplied in [User ID](#parameters) must have read access to devices.

You must have administrator credentials to log in to this server. Administrators with read-only privileges can make GET calls using a REST-API consuming program, but only fully privileged accounts can be used to make configuration changes through the REST API.