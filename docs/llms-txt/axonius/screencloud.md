# Source: https://docs.axonius.com/docs/screencloud.md

# ScreenCloud Studio

ScreenCloud Studio is a digital signage platform that allows businesses to create, manage, and display content across variety of screen types and locations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ScreenCloud Studio server.

2. **API Key** *(required)* - The API Token associated with a user account that has permissions to fetch assets. For information on how to obtain an API Token, see [Get an API Token](https://screencloud.github.io/signage-next-graphql-docs/get-an-api-token).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ScreenCloud Studio](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ScreenCloud%20Studio.png)

## APIs

Axonius uses the [ScreenCloud API](https://screencloud.github.io/signage-next-graphql-docs/overview).

## Supported From Version

Supported from Axonius version 6.1.32.1