# Source: https://docs.axonius.com/docs/canary.md

# Thinkst Canary

Thinkst Canary is deception technology deployed as tokens to catch malicious activity.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Domain** *(required)* - The unique hash identifying your console.

2. **Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   To obtain the **Domain** and **Token**:

   * From the Canary Console, navigate to **/settings**. In the API section, the values of the Domain and Token are displayed.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Canary\_Thinkst(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Canary_Thinkst\(1\).png)

## APIs

Axonius uses the [Canary API](https://docs.canary.tools/console-settings/api.html).

## Supported From Version

Supported from Axonius version 4.5