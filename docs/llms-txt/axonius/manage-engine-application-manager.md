# Source: https://docs.axonius.com/docs/manage-engine-application-manager.md

# ManageEngine Applications Manager

ManageEngine Applications Manager offers full-stack visibility across cloud and on-premise apps, optimizing performance and simplifying IT and DevOps processes.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Business Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ManageEngine Applications Manager server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to generate the API Key, see [Generate API Key](https://www.manageengine.com/products/applications_manager/help/rest-apis.html#:~:text=API%20request%20made.-,Generate%20API%20Key,-The%20User%20can).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ManageEngine Applications Manager](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngine%20Applications%20Manager.png)

## APIs

Axonius uses the [ManageEngine Applications Manager V1 REST APIs](https://www.manageengine.com/products/applications_manager/help/v1-rest-apis.html).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Administrator, Operator, and User permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1.45.0