# Source: https://docs.axonius.com/docs/serraview.md

# Serraview

Serraview is workplace management and space optimization software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Serraview server.

2. **Client ID** *(required)* - The credentials for a user account that has the permissions to fetch assets. Refer to [Access Serraview APIs](https://support.iofficecorp.com/Serraview/Workplace_Management/Integrations/Portfolio_Data_-_Extract/Serraview_Core_API/Access_Serraview_APIs) for information on how to create the Client ID.

3. **Private Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.[Access Serraview APIs](https://support.iofficecorp.com/Serraview/Workplace_Management/Integrations/Portfolio_Data_-_Extract/Serraview_Core_API/Access_Serraview_APIs) for information on how to create the Private Key (step 1).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Serraview](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Serraview.png)

## APIs

Axonius uses the:

* [Serraview Integrations API](https://support.iofficecorp.com/Serraview/Workplace_Management/Integrations)
* [Serraview Access Serraview APIs](https://support.iofficecorp.com/Serraview/Workplace_Management/Integrations/Portfolio_Data_-_Extract/Serraview_Core_API/Access_Serraview_APIs)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80, 443** or any other port configured by the user.

## Required Permissions

The service account for the API needs to be assigned the Service Account role in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.8