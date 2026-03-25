# Source: https://docs.axonius.com/docs/crestron-xio-cloud.md

# Crestron XiO Cloud

Crestron XiO Cloud is a technology operations management platform that allows users to configure and manage all Crestron device from one central location.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Crestron XIO  server.

2. **Account ID** *(required)* - The Crestron XIO account ID. Contact [Technical Support](https://sdkcon78221.crestron.com/sdk/Crestron_XiO_Cloud_SDK/Content/Topics/Customer-Guidelines.htm) to have public API access enabled for the customer XiO Cloud account. A subscription key and an account ID will be provided once public API access has been enabled.

3. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. Refer to [Crestron Documentation](https://sdkcon78221.crestron.com/sdk/Crestron_XiO_Cloud_SDK/Content/Topics/Customer-Guidelines.htm) for information on how to get the API key.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CrestronXIO](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CrestronXIO.png)

## APIs

Axonius uses the [CRESTRON Xio Cloud API](https://sdkcon78221.crestron.com/sdk/Crestron_XiO_Cloud_SDK/Content/Topics/Customer-Guidelines.htm)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [Account ID](#parameters) must be associated with credentials that have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0