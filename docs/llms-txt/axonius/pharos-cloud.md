# Source: https://docs.axonius.com/docs/pharos-cloud.md

# Pharos Cloud

Pharos Cloud is a cloud print management tool that provides centralized control of organizational print operations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.beacon.pharos.com`)* - The hostname or IP address of the Pharos Cloud server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Scopes** *(optional)* - The authorization scopes for the configured Client ID.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Pharos Beacon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Pharos%20Beacon.png)

## APIs

Axonius uses the [Pharos Cloud API](https://doc.pharos.com/cloud/C_Topics/Analysis/Connecting-API-ExtractData.htm).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

Only Admin users and system users have access to the API screen.

## Supported From Version

Supported from Axonius version 6.1.38.2