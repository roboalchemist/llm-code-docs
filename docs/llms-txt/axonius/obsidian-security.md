# Source: https://docs.axonius.com/docs/obsidian-security.md

# Obsidian Security

Obsidian delivers a security solution for SaaS applications built around unified visibility, continuous monitoring, and security analytics.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

* **Host Name or IP Address** *(required)* - The hostname or IP address of the Obsidian Security server: `https://api.obsec.io`.
* **Token** *(required)* - A Token associated with a user account that has permissions to fetch assets. Refer to Obsidian documentation for information on how to create the Token,
* **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
  * When enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** is verified against the CA database inside of Axonius. When the SSL certificate can not be validated against the CA database inside  Axonius, the connection fails with an error.
  * When disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** is not verified against the CA database inside Axonius.
* **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
  * When supplied, Axonius uses the proxy when connecting to the value supplied in **Host Name or IP Address**.
  * When not supplied, Axonius connects directly to the value supplied in **Host Name or IP Address**.
* **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
  * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
  * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
  * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
  * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="obsidian security.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/obsidian%20security.png" />

## APIs

Axonius uses the <Anchor label="Obsidian Security API" target="_blank" href="https://www.obsidiansecurity.com/resource-center">Obsidian Security API</Anchor>.

## Permissions

Admin permission is needed to create the API token.

## Supported From Version

Supported from Axonius version 4.5.