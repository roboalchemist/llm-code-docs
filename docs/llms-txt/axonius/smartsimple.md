# Source: https://docs.axonius.com/docs/smartsimple.md

# SmartSimple

SmartSimple is a grant management and business process solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SmartSimple server.

2. **API Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information about how to generate API Tokens, see [SmartConnect - API User Access Tokens](https://wiki.smartsimple.com/wiki/SmartConnect_-_RESTful_API#API_User_Access_Tokens).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SmartSimple](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SmartSimple.png)

## APIs

Axonius uses the [SmartConnect API](https://api.smartsimple.com/devtools/api.html).

## Required Permissions

The value supplied in [API Token](#parameters) must be associated with credentials that have manager permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0