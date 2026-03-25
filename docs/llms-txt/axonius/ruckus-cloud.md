# Source: https://docs.axonius.com/docs/ruckus-cloud.md

# RUCKUS Cloud

CommScope RUCKUS Cloud is a network management-as-a-service platform that enables IT to provision, manage, optimize, and troubleshoot wired and wireless networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the RUCKUS Cloud server.

2. **Tenant ID** and  **API Key** -  Tenant ID and an API Key  required to fetch assets. Both values are available through the [API client Authentication](https://docs.ruckuswireless.com/ruckus-cloud/platform-ns-220711.html#tag/API-Client-Authentication) endpoint on the RUCKUS Cloud Platform which can only be made with admin credentials (username and password).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![RuckusCloud](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RuckusCloud.png)

## APIs

Axonius uses the [RUCKUS Cloud API ](https://support.ruckuswireless.com/documents/4229-ruckus-cloud-api-documentation).

## Required Permissions

The value supplied in [User Name](#parameters) must have RUCKUS admin support for an OAuth2 token for read-only consumption in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                   | Supported | Notes |
| ------------------------- | --------- | ----- |
| RUCKUS Networks V22.07.11 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.8