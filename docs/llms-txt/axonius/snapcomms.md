# Source: https://docs.axonius.com/docs/snapcomms.md

# SnapComms

SnapComms is an internal communications software solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Snapcomms server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Tenant ID** *(required)* - The Tenant ID.

3. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Snapcomms](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Snapcomms.png)

## APIs

Axonius uses the [Everbridge SnapComms API](https://developers.everbridge.net/home/reference/token).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Data Privacy policy permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0