# Source: https://docs.axonius.com/docs/sciencelogic.md

# ScienceLogic

ScienceLogic is an IT operations management (ITOM) and AIOps platform for monitoring and managing hybrid cloud infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ScienceLogic server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ScienceLogic](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ScienceLogic.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Ingest All Custom Fields** - Select this option to ingest all ScienceLogic custom fields.
2. **Parse Device Additional Fields From Raw** - Enter a list of additional fields to parse from the raw data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses [Introduction to the ScienceLogic API](https://docs.sciencelogic.com/latest/Content/Web_Content_Dev_and_Integration/ScienceLogic_API/api_intro.htm).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following port:

* **TCP port 443**

## Required Permissions

* EM7 System Administration: Basic User Privileges
* Dashboards: Dashboard - View
* Asset Management: Asset - View
* Organizations: Org/User/Vendor/Contact - View
* Devices: Devices - Information View
* IT Services: IT Services - View

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version           | Supported | Notes |
| ----------------- | --------- | ----- |
| ScienceLogic 11.3 | Yes       |       |

## Supported From Version

Supported from Axonius version 5.0