# Source: https://docs.axonius.com/docs/global-sign-atlas.md

# GlobalSign Atlas

GlobalSign Atlas offers cloud certificate management and automation.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the GlobalSign Atlas server.

2. **API Key** and **API Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To generate a Key Pair, see [How to Obtain GlobalSign Account Credentials](https://support.globalsign.com/ssl/api-plugins/how-to-obtain-globalsign-atlas-account-credentials).

3. **Certificate File** *(optional)* - The GlobalSign issued certificate file (.CRT file).  For more detailed information, see [Get Certificates API](https://www.globalsign.com/en/resources/apis/api-documentation/globalsign_atlas_certificate_management_api.html#certificates__certificate__get).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="GlobalSign Atlas" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GlobalSign%20Atlas.png" />

## APIs

Axonius uses the:

* [GlobalSign Atlas Certificate Management API (PDF)](https://www.globalsign.com/en/repository/globalsign-atlas-certificate-management-api.pdf)
* [Get Certificates API](https://www.globalsign.com/en/resources/apis/api-documentation/globalsign_atlas_certificate_management_api.html#certificates__certificate__get)

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.7