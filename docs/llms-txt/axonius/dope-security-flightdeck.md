# Source: https://docs.axonius.com/docs/dope-security-flightdeck.md

# Dope Security Flightdeck

Dope Security is an endpoint-based secure web gateway solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Dope Security server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets. For information on generating client credentials, see [API Client Credentials](https://inflight.dope.security/dope.console/settings/api-client-credentials).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Dope%20Security](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dope%20Security.png)

## APIs

Axonius uses the [Flightdeck API](https://inflight.dope.security/dope.apis/public-api-specification).

## Supported From Version

Supported from Axonius version 6.0