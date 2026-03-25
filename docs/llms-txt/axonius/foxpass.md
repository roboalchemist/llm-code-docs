# Source: https://docs.axonius.com/docs/foxpass.md

# Foxpass

Foxpass is an Identity and Access Management (IAM) solution that centralizes and automates access control for servers and applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For information about how to generate the API Key, see [Integrate with Foxpass's API](https://docs.foxpass.com/docs/integrate-with-foxpasss-api).

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Foxpass](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Foxpass.png)

## APIs

Axonius uses the [Foxpass API](https://docs.foxpass.com/reference/api-overview).

## Supported From Version

Supported from Axonius version 6.1