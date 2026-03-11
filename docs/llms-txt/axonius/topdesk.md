# Source: https://docs.axonius.com/docs/topdesk.md

# TOPdesk Enterprise Service Management

TOPdesk Enterprise Service Management (ESM) lets service teams process requests from a single platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the TOPdesk Enterprise Service Management server.

2. **User Name** or **Application Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets. You can either use  **User Name** or **Application Name**. **Application Name** is recomended. Refer to [TOPdesk API tutorial ](https://developers.topdesk.com/tutorial.html) to learn how to create an application and password.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![TOPdesk Enterprise Service Management](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TOPdesk%20Enterprise%20Service%20Management.png)

## APIs

Axonius uses the following APIs:

* [TOPdesk API](https://developers.topdesk.com/)
* [TOPdesk Asset Management REST API](https://developers.topdesk.com/explorer/?page=assets#/Assets/getAssets)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                   | Supported | Notes |
| ------------------------- | --------- | ----- |
| TOPdesk 7.11.005 or later | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5