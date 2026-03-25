# Source: https://docs.axonius.com/docs/opal.md

# Opal

Opal is an access management platform that helps enterprise companies scale least privilege.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Groups

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Opal server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **ApiKey** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![opal](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/opal.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Endpoints Config** - Click on `>` to open the following settings for configurable endpoints:
  * **Enrich Groups with Apps** - By default the adapter enriches Opal groups with Opal apps. Toggle off if you want to clear this option.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Opal API](https://docs.opal.dev/reference/getapps).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| Opal V1 | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.0