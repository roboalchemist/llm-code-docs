# Source: https://docs.axonius.com/docs/nutanix-cloud-cost-governance.md

# Nutanix Cloud Manager (NCM) Cost Governance

Nutanix Cloud Manager (NCM) Cost Governance (formerly Beam) provides visibility into cloud spend across multiple cloud environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Nutanix Cloud Manager (NCM) Cost Governance server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to generate an API Key, see [Setting up API key](https://dev.beam.nutanix.com/reference/setting-up-api-key).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Nutanix%20Cloud%20Manager%20(NCM)%20Cost%20Governance](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nutanix%20Cloud%20Manager%20\(NCM\)%20Cost%20Governance.png)

## APIs

Axonius uses the [Nutanix Cost Governance platform API](https://dev.beam.nutanix.com/reference/accounts-list).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have admin permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0