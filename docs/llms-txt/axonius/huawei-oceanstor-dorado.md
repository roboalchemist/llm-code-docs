# Source: https://docs.axonius.com/docs/huawei-oceanstor-dorado.md

# Huawei OceanStor Dorado V3

Huawei OceanStor Dorado V3 is an all-flash storage solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **IP Address** *(required)* - The IP address of the Huawei OceanStor Dorado V3 server.

2. **Port** *(required)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

4. **Scope** - Select either Local User or LDAP User for the scope.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
![Huawei%20OceanStor%20Dorado%20V3](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Huawei%20OceanStor%20Dorado%20V3.png)

## APIs

Axonius uses the [Huawei OceanStor DeviceManager RESTful API](https://support.huawei.com/enterprise/en/doc/EDOC1100144155/f5087536/restful-apis).

## Supported From Version

Supported from Axonius version 6.0