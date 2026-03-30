# Source: https://docs.axonius.com/docs/spycloud.md

# SpyCloud

SpyCloud is an account takeover prevention and fraud investigation tool that alerts companies when their users' data has been compromised in a third-party breach.

## Asset Types Fetched

* Devices

## Before You Begin

### APIs

Axonius uses the [SpyCloud API](https://spycloud-external.readme.io/sc-enterprise-api/docs).

### Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SpyCloud server. Use `https://api.spycloud.io`.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SpyCloudParams](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-4SJ722OL.png)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version     | Supported | Notes |
| ----------- | --------- | ----- |
| SpyCloud v2 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.8.6