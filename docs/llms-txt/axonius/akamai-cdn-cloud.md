# Source: https://docs.axonius.com/docs/akamai-cdn-cloud.md

# Akamai CDN Cloud

Akamai CDN Cloud is a content delivery network that accelerates web and video content delivery globally.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(optional)* - The hostname or IP address of the Akamai CDN Cloud server.

2. **Client Token** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets. For information about how to create these credentials, see [Create authentication credentials](https://techdocs.akamai.com/developer/docs/set-up-authentication-credentials).

3. **Access Token** *(required)* - An Access Token associated with a user account that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Akamai CDN Cloud](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Akamai%20CDN%20Cloud.png)

## APIs

Axonius uses the [Akamai Identity and Access Management API v3](https://techdocs.akamai.com/iam-api/reference/api).

## Supported From Version

Supported from Axonius version 6.1