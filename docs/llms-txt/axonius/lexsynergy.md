# Source: https://docs.axonius.com/docs/lexsynergy.md

# Lexsynergy

Lexsynergy is a domain management platform that helps organizations manage and protect their domain assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Lexsynergy server.

2. **API Key** and **API Secret** *(required)* - The credentials for a user account that has permissions to fetch assets.

3. **Realm** *(optional, default: api)* - Your organization realm ID.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Lexsynergy](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Lexsynergy.png)

## APIs

Axonius uses the Lexsynergy API.

## Supported From Version

Supported from Axonius version 6.1.28.0