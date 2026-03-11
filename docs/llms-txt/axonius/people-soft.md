# Source: https://docs.axonius.com/docs/people-soft.md

# PeopleSoft

Oracle PeopleSoft is a suite of applications that provides solutions for human resources, finance, business operations, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the PeopleSoft server.

2. **User Name** and **Password** *(required)* - The credentials for a web service account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PeopleSoft](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PeopleSoft.png)

## APIs

Axonius uses the [PeopleSoft Employee Directory (employeedirectory) API](https://docs.oracle.com/cd/F82121_01/fscm92pbr48/eng/fscm/eccf/UnderstandingRESTAPIEndpointsForPeoplesoftEmployeeDirectoryemployeedirectory.html#topic_d0ec0561-901f-4aa0-a1c0-056247f5f915) to retrieve employees.

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch employees from the PeopleSoft Employee Directory (employeedirectory) API.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 6.0     | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.0