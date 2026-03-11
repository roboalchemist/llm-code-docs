# Source: https://docs.axonius.com/docs/seceon.md

# Seceon aiXDR

Seceon aiXDR is an extended detection and response platform that provides comprehensive threat detection, automated response, and continuous monitoring across endpoints, networks, and cloud environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Seceon server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Tenant ID** *(required)* - Specify the Seceon Tenant ID.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Seceon aiXDR](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Seceon%20aiXDR.png)

## APIs

Axonius uses the [Seceon OTM REST API](https://app.swaggerhub.com/apis/seceon/SeceonOpenAPI/10.1.2).

## Supported From Version

Supported from Axonius version 6.1.32.1