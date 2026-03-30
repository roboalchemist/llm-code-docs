# Source: https://docs.axonius.com/docs/conductor-one.md

# ConductorOne

ConductorOne is an Identity Governance and Administration (IGA) platform that provides comprehensive visibility, automation, and fine-grained access controls for modern environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ConductorOne server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ConductorOne.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ConductorOne.png)

## APIs

Axonius uses the [ConductorOne API](https://api.conductorone.com/docs/conductorone-api/a76uioi122862-how-to-authenticate-requests).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| API v1  | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1.55.0