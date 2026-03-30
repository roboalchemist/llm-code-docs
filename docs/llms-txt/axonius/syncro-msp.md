# Source: https://docs.axonius.com/docs/syncro-msp.md

# Syncro MSP

Syncro MSP is a combined remote monitoring and management (RMM) and professional services automation (PSA) platform that manages invoicing, credit card payments, help desk, customer relationship tracking, remote access and support, and more managed IT services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Syncro MSP server.

2. **API Key/Token** *(required)* - An API token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To generate an API token, see [Syncro API Tokens](https://community.syncromsp.com/t/api-tokens/2297).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="SyncroMSP" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyncroMSP.png" />

## APIs

Axonius uses the [Syncro API v1](https://api-docs.syncromsp.com/).

## Required Permissions

The value supplied in [API Key/Token](#parameters) must be associated with credentials that have Read permissions for listing assets and asset details.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V1      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.6