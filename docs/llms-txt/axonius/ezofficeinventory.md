# Source: https://docs.axonius.com/docs/ezofficeinventory.md

# EZOfficeInventory

EZOfficeInventory is a cloud-based asset tracking platform used for tracking physical and digital assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Subdomain** *(required)* - The subdomain of the EZOfficeInventory server. For instance in the following example, only input the subdomain,  `https://\<SUBDOMAIN>.ezofficeinventory.com/assets.api`.

2. **Company  Token** *(required)* - An API Token associated with a user account that has the permissions to fetch assets. To generate the API Token,  go to Settings, and enable API for the company (disabled by default) and generate an access token. The Access token is used to authenticate each request.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="EZofficeInventory.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EZofficeInventory.png" />

## APIs

Axonius uses the [EZOfficeInventory API](https://www.ezofficeinventory.com/developers).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [Company Token](#parameters) must be associated with credentials that have permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5