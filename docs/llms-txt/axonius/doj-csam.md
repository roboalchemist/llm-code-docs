# Source: https://docs.axonius.com/docs/doj-csam.md

# DOJ CSAM

DOJ’s proprietary Cyber Security Assessment and Management (CSAM) automates assessments and authorizations to provide a comprehensive assessment and continuous monitoring service.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the DOJ CSAM server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![DOJCASM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DOJCASM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **System Report Name** - Enter a meaningful name (string) for the System Report that is to contain CSAM report data  pulled from the DOJ CSAM adapter. When you enter this name:
  * The name (string) is automatically URL encoded (converted into valid URL format) and appended to /CSAM/API/v1/reports/`{description}`.
  * During a fetch, the DOJ CSAM adapter pulls CSAM report data into this URL. This report data contains more device information than the minimal device data that is pulled (when the report name is not filled in). This additional report data enriches the system assets.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80, 443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have ReadOnly permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| DOJ CSAM 1.0.0 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.8