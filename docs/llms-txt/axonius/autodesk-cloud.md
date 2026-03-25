# Source: https://docs.axonius.com/docs/autodesk-cloud.md

# Autodesk Cloud Platform

Autodesk Cloud Platform is comprised of the Forma, Fusion and, Flow industry clouds.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Autodesk Cloud Platform server.

2. **Client ID** and **Client Secret** *(required)* - The username and password associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to obtain the Client ID and Client Secret, see [Create an App](https://aps.autodesk.com/en/docs/oauth/v2/tutorials/create-app/).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Autodesk%20Cloud](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Autodesk%20Cloud.png)

## APIs

Axonius uses the [APS API](https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/overview/).

## Required Permissions

In order to fetch assets, you must have access to the [Autodesk Developer Portal](https://aps.autodesk.com/) and permissions to create a new app.

## Supported From Version

Supported from Axonius version 6.0