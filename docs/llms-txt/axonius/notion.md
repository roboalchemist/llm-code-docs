# Source: https://docs.axonius.com/docs/notion.md

# Notion

Notion offers a workplace productivity suite that includes solutions for collaboration and communication, task management, project tracking, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Notion server.

2. **API Token** *(required)* - An API Token associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Notion](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Notion.png)

## APIs

Axonius uses the [Notion API](https://developers.notion.com/reference/get-users)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read permissions in order to fetch assets.

### Integration Permissions

In order for an integration can interact with your Notion workspace page(s), the page must be manually shared with the integration.
To share a page with an integration

1. Visit the page in your Notion workspace
2. Click the ••• menu at the top right of a page
3. Scroll down to **Add Connections**, and use the search bar to find and select the integration from the dropdown list.

Once the integration is shared, you can start making API requests. If the page is not shared, any API requests made will respond with an error. Refer to [Notion Authorization.](https://developers.notion.com/docs/authorization)

## Supported From Version

Supported from Axonius version 5.0