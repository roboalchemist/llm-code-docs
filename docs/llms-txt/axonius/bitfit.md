# Source: https://docs.axonius.com/docs/bitfit.md

# bitFit

bitFit is a business development and information technology company that collects all of your IT operations data and combines it into a unified cloud system.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the bitFit server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Client ID** *(required)* - A Key obtained from bitFit support.

4. **Client Secret** *(required)* - A Secret Key obtained from bitFit support.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![bitFit.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/bitFit.png)

## APIs

Axonius uses the bitFit API v2.