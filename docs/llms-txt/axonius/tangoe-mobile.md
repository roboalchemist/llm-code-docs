# Source: https://docs.axonius.com/docs/tangoe-mobile.md

# Tangoe Managed Mobility Services (MMS)

Tangoe Managed Mobility Services (MMS) provides end-to-end mobile lifecycle management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Tangoe Managed Mobility Services (MMS) server.

2. **API Token** *(required)* - An API Token associated with a user account that has permissions to fetch assets. For information on how to authenticate using the API Token, see [Authentication](https://anypoint.mulesoft.com/exchange/portals/tangoe/f5574299-614a-4d3f-885d-24958c10613f/tangoe-mobile-rest/minor/1.0/pages/Authentication/).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Tangoe Managed Mobility Services (MMS)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Tangoe%20Managed%20Mobility%20Services%20\(MMS\).png)

## APIs

Axonius uses the [Tangoe Mobile REST API](https://anypoint.mulesoft.com/exchange/portals/tangoe/f5574299-614a-4d3f-885d-24958c10613f/tangoe-mobile-rest/minor/1.0/pages/home/).

Axonius fetches from the following APIs:

* /devices
* /people

## Supported From Version

Supported from Axonius version 6.1