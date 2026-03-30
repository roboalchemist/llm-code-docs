# Source: https://docs.axonius.com/docs/mulesoft.md

# MuleSoft

MuleSoft is an integration platform that helps businesses connect data, applications and devices across on-premises and cloud computing environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the MuleSoft server.

2. **Authentication Domain** *(optional)* - The domain of the service used for authentication.

3. **Client Name** - Enter the name of the client.

4. **Client ID** and **Client Secret** *(optional)* - The credentials for a user account that has the permissions to fetch assets.
   To generate a Client ID and Client Secret, see [Creating Connected Apps](https://docs.mulesoft.com/access-management/creating-connected-apps-dev).

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Mulesoft](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Mulesoft.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Past Configured Days** *(required, default: 1)* - Enter the number of past days to start fetching data from.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **HTTPS port 443**

## Supported From Version

Supported from Axonius version 4.6