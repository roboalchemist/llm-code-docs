# Source: https://docs.axonius.com/docs/mosyle-manager.md

# Mosyle Manager

Mosyle Manager is a MDM solution designed to manage, configure, and secure Apple devices in educational and enterprise environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://managerapi.mosyle.com`)* - The hostname or IP address of the Mosyle Manager server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Access Token** *(required)* - An Access Token associated with a user account that has permissions to fetch assets. To use the Mosyle API you need to enable this feature in the API profile page (My School `>` API Integration `>` enable the profile). Once enabled, you will see your access token and make requests to the endpoint "`https://managerapi.mosyle.com/v2`”.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Mosyle Manager" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Mosyle%20Manager.png" />

## APIs

Axonius uses the Mosyle API.

## Supported From Version

Supported from Axonius version 6.1