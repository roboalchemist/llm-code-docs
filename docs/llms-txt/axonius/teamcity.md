# Source: https://docs.axonius.com/docs/teamcity.md

# TeamCity

TeamCity is a build management and continuous integration server

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the TeamCity server.

2. **API Key/Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![TeamCity](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TeamCity.png)

## APIs

Axonius uses the [TeamCity REST API](https://www.jetbrains.com/help/teamcity/rest/teamcity-rest-api-documentation.html)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [API Key/Token](#parameters) must be associated with credentials access to view the build agents in order  to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| TeamCity v8.0) | Yes       |       |

## Supported From Version

Supported from Axonius version 4.8