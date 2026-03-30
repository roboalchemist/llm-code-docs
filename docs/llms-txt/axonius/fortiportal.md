# Source: https://docs.axonius.com/docs/fortiportal.md

# FortiPortal

FortiPortal is a cloud-based security policy, wireless management, and analytics for MSSPs, enterprises, education and government customers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the FortiPortal server that Axonius can communicate with via TCP port 8080.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** *(required, default: False)* - Choose whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="fortiportal_fields" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/fortiportal_fields.png" />

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [FortiPortal REST API](https://fortinetweb.s3.amazonaws.com/docs.fortinet.com/v2/attachments/349c970c-eae7-11e9-8977-00505692583a/FortiPortal-v5.3.0-rest-api-guide.pdf)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 8080**: REST API

## Required Permissions

The value supplied in [User Name](#parameters) must have read permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version           | Supported | Notes |
| ----------------- | --------- | ----- |
| FortiPortal 5.3.0 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5