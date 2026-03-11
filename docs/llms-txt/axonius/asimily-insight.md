# Source: https://docs.axonius.com/docs/asimily-insight.md

# Asimily Insight

Asimily provides a vulnerability management platform that scans for devices, vulnerabilities and attack paths, and helps organizations prioritize and manage risk for IoMT, IoT, and laboratory devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
  , Aggregated Security Findings
  , Software
  , SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Asimily Insight server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Asimily%20Insight.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch vulnerabilities** - Toggle on in order to fetch vulnerabilities.
2. **Fetch anomalies** - Toggle on in order to fetch anomalies.
3. **Fetch recalls** - Toggle on in order to fetch recalls.
4. **Fetch ports** - Toggle on in order to fetch ports.
5. **Fetch applications** - Toggle on in order to fetch applications.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Asimily Insight REST API.

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0