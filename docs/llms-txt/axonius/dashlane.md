# Source: https://docs.axonius.com/docs/dashlane.md

# Dashlane

Dashlane is a password management tool that offers secure storage and autofill capabilities for credentials.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.dashlane.com/public`)* - The hostname or IP address of the Dashlane server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For more information about how to generate an API Key, see [Getting Started](https://github.com/Dashlane/public-api-documentation?tab=readme-ov-file#getting-started).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Dashlane.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dashlane.png)

## APIs

Axonius uses the [Dashlane Public API](https://dashlane.github.io/public-api-documentation/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.57.0