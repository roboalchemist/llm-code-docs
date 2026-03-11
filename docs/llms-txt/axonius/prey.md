# Source: https://docs.axonius.com/docs/prey.md

# Prey

Prey is a cross-platform, open source tool that allows you to track and recover your devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - This should be [https://api.preyproject.com/v1](https://api.preyproject.com/v1)

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. To get the API Key, log into your Control Panel in the Prey website, from the Settings menu find the key generator in the Developer API tab.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![prey](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/prey.png)

## APIs

Axonius uses the [Prey API](https://api.preyproject.com/)

## Supported From Version

Supported from Axonius version 6.0