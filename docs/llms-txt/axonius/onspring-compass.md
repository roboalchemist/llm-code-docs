# Source: https://docs.axonius.com/docs/onspring-compass.md

# Onspring-Compass

Onspring is cloud-based automated GRC software for business process management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Onspring server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. Refer to [Generating an API Key in the API documentation.](https://software.onspring.com/hubfs/Training/Admin%20Guide%20-%20v2%20API.pdf)

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![OnSpringCompass](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OnSpringCompass.png)

## APIs

Axonius uses the [Onspring v2 API](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://software.onspring.com/hubfs/Training/Admin%20Guide%20-%20v2%20API.pdf)

## Required Permissions

The value supplied in [API Key](#parameters) must  be associated with credentials that have read-only permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.7