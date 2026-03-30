# Source: https://docs.axonius.com/docs/asset-sonar.md

# AssetSonar

AssetSonar maintains, tracks, and manages a single source of truth for the IT asset landscape.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Asset Sonar server. This is in the format of the  Company name used in signup, also visible in the URL when you are logged in,  e.g. `https://.assetsonar.com/`.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. This should be in the format of   .   It is an Access token generated from the  Asset Sonar Settings page.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![AssetSonar](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetSonar.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

* **Handle API Limit** - Enable this to limit the amount of API requests per minute. This can help prevent errors in the fetch process. The default value is 60.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [AssetSonar API](https://www.assetsonar.com/developers)

## Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version       | Supported | Notes |
| ------------- | --------- | ----- |
| AssetSonar v1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7

## Related Enforcement Actions

* [AssetSonar - Update Asset](https://docs.axonius.com/axonius-help-docs/docs/update-sonar-asset)
* [Asset Sonar - Delete or Retire Asset](https://docs.axonius.com/axonius-help-docs/docs/manage-sonar-asset)