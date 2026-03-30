# Source: https://docs.axonius.com/docs/symantec-data-center-security-dcs-server-advanced.md

# Symantec Data Center Security (DCS) Server Advanced

Symantec Data Center Security Server Advanced delivers security detection, monitoring, and prevention capabilities for both physical and virtual server infrastructures.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **DCS Host Name or IP Address** *(required)* - The hostname or IP address of the Data Center Security (DCS) server.

2. **UMC Host Name or IP Address** *(required)* - The hostname or IP address of the Unified Management Console server.

3. **DCS Port** *(required)* - The port used in the connection to the DCS server.

4. **UMC Port** *(required)* - The port used in the connection to the UMC server.

5. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions). These credentials are used for getting the token from the UMC which will be later used for API call to the DCS server.

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Symantec Data Center Security (DCS) Server Advanced.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Symantec%20Data%20Center%20Security%20\(DCS\)%20Server%20Advanced.png)

## APIs

Axonius uses the [Symantec Data Center Security: Server Advanced REST APIs](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/data-center-security-%28dcs%29/6-9-3/rest-apis-v127998007-d3608e248183/getting-started-with-rest-apis-v127998009-d3608e248186.html).

## Required Permissions

The value supplied in [User Name](#parameters) must have permissions to connect to the UMC.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version       | Supported | Notes |
| ------------- | --------- | ----- |
| 6.6, 6.7, 6.8 | Yes       |       |