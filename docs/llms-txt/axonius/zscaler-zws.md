# Source: https://docs.axonius.com/docs/zscaler-zws.md

# Zscaler Workload Segmentation

Zscaler Workload Segmentation is a SaaS solution for applying and managing network segmentation in cloud and on-prem environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `https://console.edgewise.services`)* - The hostname or IP address of the ZScale ZWS server.

2. **Site ID** *(required)* - Enter the ID of the site you want to fetch in Axonius.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **Certificate File (.pem)** *(optional)* - Select **Choose File** next to this parameter to upload an API Key associated with a user account that has permissions to fetch assets.

6. **Key File (.pem)** *(optional)* - Select **Choose File** next to this parameter to upload the Public key file and Private key file, used for authentication.

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

10. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Zscaler_WS" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Zscaler_WS.png" />

## APIs

Axonius uses the [EdgewiseNetworks API](https://github.com/EdgewiseNetworks/api-examples/tree/f6fb7b7335b0ceae0a997efeb9c17d3cc58cfb7e/v1/python) as a shared code example.

## Supported From Version

Supported from Axonius version 4.5