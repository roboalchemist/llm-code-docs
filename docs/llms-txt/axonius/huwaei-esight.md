# Source: https://docs.axonius.com/docs/huwaei-esight.md

# Huawei eSight

Huawei eSight is an enterprise operation and maintenance (O\&M) platform that provides cross-vendor and cross-product converged management, visualized monitoring, and intelligent analysis for enterprise ICT devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Huawei eSight server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API port** (required, default: 32102) - The port selected by the customer for REST API requests.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Huawei%20eSight](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Huawei%20eSight.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Populate Hostname with Serial Number when Hostname and Asset Name are empty** - Select this option to populate hostname with serial number when the hostname and asset name are missing.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the **Third-Party Terminal Resource Report Interface** API endpoint. Info about this API can be found in the ESight Self-Service Integration Guide help file.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0