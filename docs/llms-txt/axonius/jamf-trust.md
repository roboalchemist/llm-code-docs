# Source: https://docs.axonius.com/docs/jamf-trust.md

# Jamf Trust

Jamf Trust provides enterprise-level security and remote access for mobile devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Jamf Trust server.

2. **Hash of Client ID and Client Secret** *(required)* - The basic auth header containing the base64 hash of the Client ID and Client Secret. Hash is calculated from the string pair "clientId:clientSecret".

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
![Jamf%20Trust%20Config%20Screen](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Jamf%20Trust%20Config%20Screen.png)

## APIs

Axonius uses the [Risk API](https://developer.jamf.com/jamf-security/docs).

## Supported From Version

Supported from Axonius version 6.0