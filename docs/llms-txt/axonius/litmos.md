# Source: https://docs.axonius.com/docs/litmos.md

# Litmos

Litmos is a learning management system that provides pre-built courses and eLearning solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: 'api.litmos.com')* - The hostname or IP address of the Litmos server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **App Name** -  Specify the domain value from the Litmos account.

4. **Verify SSL**  - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Litmos" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Litmos.png" />

## APIs

Axonius uses the [SAP SuccessFactors Litmos API](https://api.sap.com/api/LitmosAPIdetails/resource).

## Supported From Version

Supported from Axonius version 4.5