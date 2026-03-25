# Source: https://docs.axonius.com/docs/n-sight-rmm.md

# N-able N-sight RMM

N-sight RMM provides remote monitoring and access, ticketing, and management for Windows, Linux, and Mac devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the N-sight RMM server. To determine this value, see [Generate the API Key](https://documentation.n-able.com/remote-management/userguide/Content/commitcrm_apikey.htm).

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To generate an API Key, see [Generate the API Key](https://documentation.n-able.com/remote-management/userguide/Content/commitcrm_apikey.htm).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![N-Able N-Sight RMM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/N-Able%20N-Sight%20RMM.png)

## APIs

Axonius uses the [Data Extraction API](https://documentation.n-able.com/remote-management/userguide/Content/data_extraction_api.htm).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

The following permissions are required to fetch the Asset Status.

* [MSP Manager's API](https://documentation.n-able.com/MSPM/userguide/en/Content/MSP-Configure-API-permissions.htm)
* [Asset Endpoint permissions](https://documentation.n-able.com/MSPM/userguide/en/Content/MSP-API-endpoint-permissions.htm)

## Supported From Version

Supported from Axonius version 4.7