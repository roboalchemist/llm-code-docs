# Source: https://docs.axonius.com/docs/samsung-knox.md

# Samsung Knox

Samsung Knox is a built-in solution used to secure, deploy, and manage Samsung and Galaxy devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Samsung Knox server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has  permissions to fetch assets.
   To generate a Client ID and Client Secret, see [APIs](/docs/samsung-knox#apis).

3. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Samsung_Knox" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Samsung_Knox.png" />

## APIs

Axonius uses:

* [Knox Manage Open API](https://docs.samsungknox.com/dev/knox-manage/api/#section/Authentication/OAuth-2.0) to get the domain.

* [Manage API Clients](https://docs.samsungknox.com/admin/knox-manage/manage-api-clients.htm) to manage API clients.

* [Get Device List](https://docs.samsungknox.com/dev/knox-manage/api/#tag/Device/operation/selectDeviceList) to get devices.

## Supported From Version

Supported from Axonius version 4.5