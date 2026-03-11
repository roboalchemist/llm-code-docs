# Source: https://docs.axonius.com/docs/ibm-tivoli-tsm.md

# IBM Storage Protect

IBM Storage Protect is an enterprise-level data protection tool that solutions for data backup and recovery.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the IBM Storage Protect server.

2. **Port** *(optional)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![IBM Storage Protect](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IBM%20Storage%20Protect.png)

## APIs

Axonius uses the [IBM Tivoli Storage Manager Client Management Services REST API](https://www.ibm.com/support/pages/sites/default/files/inline-files/$FILE/TSM%20Client%20Management%20Service%20API%20Guide.pdf).

## Supported From Version

Supported from Axonius version 6.1.31.0