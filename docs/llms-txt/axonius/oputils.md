# Source: https://docs.axonius.com/docs/oputils.md

# ManageEngine OpUtils

ManageEngine OpUtils is an IP address and switch port management software geared toward helping engineers efficiently monitor, diagnose, and troubleshoot IT resources.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ManageEngine OpUtils server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   **To generate an API Key**

   1. From the OpUtils Web console, select **Admin** `>` **User Management**. The details of all OpUtils users are displayed.
   2. Click the **Generate API Key** icon  available under the **Actions** column that corresponds to a user. The **Generate API Key** dialog opens, where you can either specify an expiry date for this key or choose never to expire.
   3. Click **Generate API Key**. The API Key is generated and displayed in the same dialog.
   4. Copy the API Key and store it in a secure location.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="ManageEngine_OpUtils" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngine_OpUtils.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Assets Asynchronously** - Select this option to fetch assets asynchronously.
2. **Ignore devices without IP to DNS values** - Select this option to ignore devices without IP to DNS values.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ManageEngine OpUtils API (v1)](https://www.manageengine.com/products/oputils/help/oputils-api.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **7080**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes                    |
| ------- | --------- | ------------------------ |
| v12.5   | Yes       | Product                  |
| API v1  | Yes       | ManageEngine OpUtils API |

## Supported From Version

Supported from Axonius version 4.5