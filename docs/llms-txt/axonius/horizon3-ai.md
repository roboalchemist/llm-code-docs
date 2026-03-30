# Source: https://docs.axonius.com/docs/horizon3-ai.md

# NodeZero

NodeZero by Horizon3 provides continuous autonomous penetration testing via SaaS.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: api.horizon3ai.com)* - The hostname or IP address of the NodeZero server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select this option to verify the SSL certificate of the server against the CA database inside of Axonius.  To learn more, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
![NodeZero](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NodeZero.png)

## Advanced Settings

* **Fetch weaknesses** - Whether to fetch weaknesses

## APIs

Axonius uses the [Horizon3.ai GraphQL API reference](https://docs.horizon3ai.com/api/graphql/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following port:

* **TCP port 80/443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.8