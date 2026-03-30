# Source: https://docs.axonius.com/docs/cradlepoint-adapter.md

# Cradlepoint

Cradlepoint develops cloud-managed wireless edge networking equipment.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cradlepoint server.

2. **User Name** and **Password** *(optional)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. **X-CP-API-ID** and **X-CP-API-KEY**, **X-ECM-API-ID** and **X-ECM-API-KEY** - Two pairs of access keys used to authenticate to the NetCloud Manager (NCM) API. Refer to [NetCloud Manager API](https://customer.cradlepoint.com/articles/Knowledge/NCM-APIv2-Overview#Obtaining-API-Keys) on how to generate and access these key pairs.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cradlepoint](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cradlepoint.png)

## APIs

Axonius uses the [Cradlepoint NetCloud Webhooks API](https://developer.cradlepoint.com/documentation/webhooks#!/Net_Device_Metrics) and [Cradlepoint Connect API](https://customer.cradlepoint.com/s/article/NCOS-SDK-Router-API-for-Applications#Python-Example).

## Supported From Version

Supported from Axonius version 6.0