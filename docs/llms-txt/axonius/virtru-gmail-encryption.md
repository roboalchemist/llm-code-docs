# Source: https://docs.axonius.com/docs/virtru-gmail-encryption.md

# Virtru Gmail Encryption

Virtru Gmail Encryption protects Gmail messages and attachments with end-to-end encryption while maintaining user ownership and control.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Virtru Gmail Encryption server.

2. **Token ID** and **Token Secret** *(required)* - The credentials for a user account that has the permissions to fetch assets. To obtain the Token ID and Token Secret, contact Virtru Support.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Virtru_Gmail" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Virtru_Gmail.png" />

## APIs

Axonius uses the following APIs:

* [Audit Export - Authentication](https://support.virtru.com/hc/en-us/articles/360006454274-Audit-Export-Authentication)
* [API Data Dictionary for Audit Export](https://support.virtru.com/hc/en-us/articles/360006454734-API-Data-Dictionary-for-Audit-Export)

## Supported From Version

Supported from Axonius version 4.7