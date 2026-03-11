# Source: https://docs.axonius.com/docs/pingdom.md

# SolarWinds Pingdom

SolarWinds Pingdom is a website and server monitoring tool that helps organizations track the uptime, performance, and availability of their web-based applications and services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SolarWinds Pingdom server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For information about how to create the API Key, see [Authentication](https://docs.pingdom.com/api/).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SolarWinds Pingdom](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SolarWinds%20Pingdom.png)

## APIs

Axonius uses the [Pingdom API](https://docs.pingdom.com/api/#section/Welcome-to-the-Pingdom-API!).

## Supported From Version

Supported from Axonius version 6.1