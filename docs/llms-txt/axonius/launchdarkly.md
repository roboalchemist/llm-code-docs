# Source: https://docs.axonius.com/docs/launchdarkly.md

# LaunchDarkly

LaunchDarkly is a continuous delivery platform and feature management platform that provides feature flags as a service.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: app.launchdarkly.com)* - The hostname or IP address of the LaunchDarkly server.

2. **API Token** *(required)* - An API REST token. Refer to [API Access Tokens](https://docs.launchdarkly.com/home/account-security/api-access-tokens) for information on creating the Access Token.  associated with a user account that has permissions to fetch assets.

3. **Verify SSL** *(required, default: False)* - Choose whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="LaunchDarkly" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LaunchDarkly.png" />

## APIs

Axonius uses the [LaunchDarkly REST API](https://apidocs.launchdarkly.com/).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with Read credentials.

## Supported From Version

Supported from Axonius version 4.5