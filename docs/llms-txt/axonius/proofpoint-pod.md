# Source: https://docs.axonius.com/docs/proofpoint-pod.md

# Proofpoint POD

Proofpoint on Demand (PoD) Email Security classifies types of email, while detecting and blocking threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Cluster  ID** *(required)* - A Cluster ID assigned by Proofpoint. Refer to PoD Logging API Key Management

2. **API Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to generate the API Token, see [http://admin.proofpoint.com/apiKeyManagement](http://admin.proofpoint.com/apiKeyManagement) and select **Create New**.

3. **Historical Data Limit (Hours)** *(required)* - Set a limit in hours to the historical data to fetch.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ProofpointPOD](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProofpointPOD.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Domains include list** *(optional, default: empty)* -  By default this adapter fetches all users. Enter a list of domains from which to fetch. Once you fill in values in this field, only users from the domains listed are fetched (separate domain names by commas, or click enter).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [API Token](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0