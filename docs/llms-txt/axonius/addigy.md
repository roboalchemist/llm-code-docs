# Source: https://docs.axonius.com/docs/addigy.md

# Addigy

Addigy is a real-time Apple mobile device management platform (MDM) that is combined with live agent capabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Addigy server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Addigy](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Addigy.png)

## APIs

Axonius uses the [Addigy API](https://documenter.getpostman.com/view/6033495/S17tPnJf#2f612c77-5c51-4953-bde0-21cf00b47026).

## Required Permissions

The value supplied in [Client ID](#parameters) must have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.7