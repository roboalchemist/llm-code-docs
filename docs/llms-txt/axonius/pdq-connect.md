# Source: https://docs.axonius.com/docs/pdq-connect.md

# PDQ Connect

PDQ Connect is a remote desktop and server management tool that allows IT administrators to remotely access and manage Windows computers and servers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the PDQ Connect server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For information on how to obtain an API Key, see the [PDQ Connect API](https://connect.pdq.com/hc/en-us/articles/22929727991451-PDQ-Connect-API).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PDQ Connect](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PDQ%20Connect.png)

## APIs

Axonius uses the [PDQ Connect API](https://connect.pdq.com/hc/en-us/articles/22929727991451-PDQ-Connect-API).

## Supported From Version

Supported from Axonius version 6.1