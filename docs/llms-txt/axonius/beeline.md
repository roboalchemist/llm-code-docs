# Source: https://docs.axonius.com/docs/beeline.md

# Beeline

Beeline is a cloud-based system for managing and procuring employees and services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Beeline server.

2. **Client ID** and **Client Secret** *(required)* - The credentials (supplied by Beeline) for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Client Site ID** *(required)* - Enter the Client Site ID supplied by Beeline.

4. **API Version** *(required)* - Enter the version of the Beeline Client Gateway API.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Beeline" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Beeline.png" />

## APIs

Axonius uses the [Beeline Client APIs](https://developers.beeline.com/client-apis).

## Required Permissions

The value supplied in [Client ID and Client Secret](#parameters) must have the following permissions in order to fetch assets:

1. **read:user**
2. **write:user**

## Supported From Version

Supported from Axonius version 6.1