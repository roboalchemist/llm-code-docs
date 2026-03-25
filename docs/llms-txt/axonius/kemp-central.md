# Source: https://docs.axonius.com/docs/kemp-central.md

# Kemp 360 Central

Kemp 360 Central is an application delivery and management platform for infrastructure monitoring of all data centers, private clouds, IaaS, PaaS, and public cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Kemp 360 Central server.

2. **User Name** *(required)* - The username for which the API key was generated.

3. **API Key** *(required)* - The API key that was generated for the specific host/username pair. For more information, see [Creating an API Key](/docs/kemp-central#creating-an-api-key) below.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="KempCentral_Adapter" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/KempCentral_Adapter.png" />

## APIs

Axonius uses the [Kemp 360 Central API](https://support.kemptechnologies.com/hc/en-us/articles/360001683652-Interface-Description-Kemp-360-Central-API#MadCap_TOC_4_1).

## Creating an API Key

To create an API Key in Kemp 360 Central:

Run the authenticate command, for example:

curl -k -X POST -d '`{"username":"USERNAME","password":"PASSWORD"}`' '`https://KEMP360CENTRALIPADDRESS/api/v1/user/authenticate/`'

Replace USERNAME, PASSWORD, and KEMP360CENTRALIPADDRESS with their respective values.

## Supported From Version

Supported from Axonius version 5.0.