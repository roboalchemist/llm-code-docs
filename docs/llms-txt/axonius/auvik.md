# Source: https://docs.axonius.com/docs/auvik.md

# Auvik

Auvik is an IT asset and network monitoring solution for managing entire network infrastructures, including physical servers, data centers, workstations and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Auvik server.  Within the API URL, us1.my (`https://auvikapi.us1.my.auvik.com`) should be updated to match the region in which your account resides. To locate the region, log into your Auvik dashboard and look at the URL in your browser's address bar.
2. **User Name** and **API Key** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Tenant IDs** *(optional)* -Comma delimited list of tenant IDs from which to request information. When you list tenant IDs the system only fetches information from the Tenant IDs listed. Otherwise when this field is empty by default the system fetches for all tenant IDs visible to the user.
4. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
5. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Auvik.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Auvik.png" />

## APIs

Axonius uses the [Auvik API (v1)](https://auvikapi.us1.my.auvik.com/docs).

## Required Permissions

The values supplied in [User Name and API Key](#parameters) must have read access to devices.

* The user must be assigned to a role with API Access. For details on creating a role with API access only, see [Auvik Support - How to add API access only roles](https://support.auvik.com/hc/en-us/articles/115002815966#topic_addapi).
* To generate an API key, see [Auvik Support - How to generate an API key](https://support.auvik.com/hc/en-us/articles/204309114-#topic_generate).