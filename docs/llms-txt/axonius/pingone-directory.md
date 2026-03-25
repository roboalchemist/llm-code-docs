# Source: https://docs.axonius.com/docs/pingone-directory.md

# PingOne Directory

PingOne Directory provides a hosted directory service that developers can use to store user authentication and profile data.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the PingOne Directory server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PingOne Directory.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PingOne%20Directory.png)

## APIs

Axonius uses the [PingOne Directory API](https://www.pingidentity.com/developer/en/api/pingone-directory-api.html).