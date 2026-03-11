# Source: https://docs.axonius.com/docs/manage-engine-key-manager-plus.md

# ManageEngine Key Manager Plus

ManageEngine Key Manager Plus is a platform for managing the entire lifecycle of SSH keys and SSL certificates, including consolidation, control, monitoring, and auditing.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Certificates

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ManageEngine Key Manager Plus server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For information on how to generate the API Key, see the [ManageEngine Key Manager Plus RESTful API](https://www.manageengine.com/key-manager/help/restapi.html).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ManageEngine Key Manager Plus](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngine%20Key%20Manager%20Plus.png)

## APIs

Axonius uses the [ManageEngine Key Manager Plus RESTful API](https://www.manageengine.com/key-manager/help/restapi.html).

## Supported From Version

Supported from Axonius version 6.1.31.0