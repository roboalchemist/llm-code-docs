# Source: https://docs.axonius.com/docs/trellix-epo.md

# MVISION ePO

MVISION provides hardware, software, and services to investigate cybersecurity attacks, protect against malicious software, and analyze IT security risks.

### Related Enforcement Actions

[MVISION ePO - Add Asset](/docs/trellix-epo-add-asset)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, api.manage.trellix.com)* - The hostname or IP address of the MVISION ePO server.

2. **Client ID** *(required)* - Create a client type by accessing the self-service section of Developer Portal.

3. **Client Secret** *(required)* - Create a client type by accessing the self-service section of Developer Portal.

4. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![MVISION EPO](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MVISION%20EPO.png)

## APIs

Axonius uses the:

* [Trellix API](https://developer.manage.trellix.com/mvision/docs/uma).
* [Trellix ePO API - devices  1.0.0](https://developer.manage.trellix.com/mvision/apis/v2-devices)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version         | Supported | Notes |
| --------------- | --------- | ----- |
| Trellix ePO v1) | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7