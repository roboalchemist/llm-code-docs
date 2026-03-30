# Source: https://docs.axonius.com/docs/sap-s4hana-cloud.md

# SAP S/4HANA Cloud

SAP S/4HANA Cloud is a modular enterprise resource planning (ERP) software that streamlines various business functions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SAP S/4HANA Cloud server.

2. **Port** *(required)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SAP%20S4HANA%20Cloud(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAP%20S4HANA%20Cloud\(1\).png)

## APIs

Axonius uses the [SAP S/4HANA Cloud APIs](https://help.sap.com/docs/SAP_S4HANA_CLOUD/f1531d40f450474dbf95f0404cb62007/d2fb90305084421e883978b4bf9da775.html).

## Supported From Version

Supported from Axonius version 6.0