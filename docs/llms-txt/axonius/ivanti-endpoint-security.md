# Source: https://docs.axonius.com/docs/ivanti-endpoint-security.md

# Ivanti Endpoint Security

Ivanti Endpoint Security, powered by Heat, provides application control, antivirus, patch management, and device control to protect endpoints.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Ivanti Endpoint Security server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Port** *(required, default: 43470)* - Use the default value.

3. **API Token for API v1** *(optional)* - An API Token associated with a user account that has permissions to fetch assets. For details on creating an API Token from the Ivanti Service Manager configuration console, see [Ivanti Service Manager - Using the REST API Key](https://help.ivanti.com/ht/help/en_US/ISM/2019.2/admin/Content/Configure/API/Using-REST-API-Key.htm#CreatingRESTAPIKey).

4. **Username for API v2** and **Password for API v2** *(optional)* - The credentials for the API associated with a user account that has permission to fetch assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. **API Version** - Select an API version (v1 or v2).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Ivanti Endpoint Security](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Ivanti%20Endpoint%20Security.png)

## APIs

Axonius uses the EMSS REST API v1.0.1.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* Port 43470

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                                 | Supported | Notes |
| --------------------------------------- | --------- | ----- |
| Ivanti Endpoint Security v8.5 or higher | Yes       |       |