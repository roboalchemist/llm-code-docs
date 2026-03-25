# Source: https://docs.axonius.com/docs/expensify.md

# Expensify

Expensify is a software company that develops an expense management system for personal and business use.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* SaaS data

## Parameters

1. **Partner User ID** and  **Partner Secret ID** *(required)* - Credentials to access Expensify. Refer to [Authentication](https://integrations.expensify.com/Integration-Server/doc/#introduction) for details of how to create these credentials.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Expensify](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Expensify.png)

## Supported From Version

Supported from Axonius version 5.0