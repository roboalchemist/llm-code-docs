# Source: https://docs.axonius.com/docs/sure-mdm.md

# SureMDM

42Gears SureMDM is a Unified Endpoint Management (UEM) solution for company-owned and BYOD devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default [https://suremdm.42gears.com](https://suremdm.42gears.com))* - The hostname or IP address of the SureMDM server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **API Key** *(required)* - Specify the API Key provided by SureMDM. To locate your API Key, see [APIs](/docs/Sure-Mdm#APIs).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="SureMDM(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SureMDM(1).png" />

## APIs

Axonius uses the [SureMDM API](https://developer.42gears.com/suremdm/api/v2/).

Every REST request made to your SureMDM account through an API needs an API key for authentication. To locate the API key for your SureMDM account, follow these steps:

1. Log into the **SureMDM** console.
2. Navigate to **Settings** > **Account Settings** > **Account Management**.
   You will find the API key under the **API Key** section.

## Supported From Version

Supported from Axonius version 6.0