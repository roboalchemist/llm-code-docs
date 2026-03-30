# Source: https://docs.axonius.com/docs/ondmarc.md

# OnDMARC

OnDMARC provides automated management for DMARC, DKIM and SPF records.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the OnDMARC server.

2. **API Key** *(required)* - An API Key associated with a user account that has [required permissions](/docs/OnDMARC#required-permissions) to fetch assets.
   To obtain an API Key, navigate to OnDMARC and select your user's profile.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="OnDMARC" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OnDMARC.png" />

## APIs

Axonius uses the [OnDMARC 1.1.1 API](https://app.swaggerhub.com/apis/ondmarc/ondmarc/1.1.1).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have super-user permissions to request and view API keys.

## Supported From Version

Supported from Axonius version 4.5