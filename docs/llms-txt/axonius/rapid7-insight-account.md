# Source: https://docs.axonius.com/docs/rapid7-insight-account.md

# Rapid7 Insight Account Platform

Rapid7 Insight API: This API provides API access for the entire Rapid7 Insight platform and suite of products.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Rapid7 Insight Account server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. Refer to [Managing Platform API Keys](https://docs.rapid7.com/insight/api-overview) to get the endpoint URL and generate the API key.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Rapid7InsightAccount](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Rapid7InsightAccount.png)

## APIs

Axonius uses Get Users from the [InsightsVM API](https://help.rapid7.com/insightvm/en-us/api/index.html#operation/getUsers).

## Supported From Version

Supported from Axonius version 4.8