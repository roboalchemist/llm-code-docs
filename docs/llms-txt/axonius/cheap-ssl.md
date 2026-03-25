# Source: https://docs.axonius.com/docs/cheap-ssl.md

# Cheap SSL Shop

Cheap SSL Shop is a provider of SSL/TLS certificates for websites and servers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Certficates

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cheap SSL Shop server.

2. **LoginEmail** *(required)* - The email used to log in to CheapSSLShop.

3. **APIKey** *(required)* -  An API Key associated with a user account that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CheapSSLShop](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CheapSSLShop.png)

## APIs

Axonius uses the [CheapSSL Get Order List API](https://www.cheapsslshop.com/api-docs/web-service-method-description/order-services/get-order-list/)

## Supported From Version

Supported from Axonius version 6.1.30.0