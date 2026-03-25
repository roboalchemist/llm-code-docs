# Source: https://docs.axonius.com/docs/contabo.md

# Contabo

Contabo is a hosting provider that offers a range of solutions, including virtual private servers, dedicated servers, and colocation services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Client ID** and **Client Secret** *(required)* - Specify the Client ID and Client Secret to be used to authenticate the request.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Contabo](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Contabo.png)

## APIs

Axonius uses the [Contabo API](https://api.contabo.com/#section/Introduction/Product-documentation) as well as the following APIs:

* [Get Users](https://api.contabo.com/#tag/Users)
* [Get Devices](https://api.contabo.com/#tag/Instances/operation/retrieveInstancesList)

## Supported From Version

Supported from Axonius version 6.1.32.1