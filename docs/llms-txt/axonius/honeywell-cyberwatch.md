# Source: https://docs.axonius.com/docs/honeywell-cyberwatch.md

# Honeywell Cyber Watch

Honeywell Cyber Watch is a cybersecurity software that identifies and manages OT cyber threats, providing insights into vulnerabilities, configuration issues, and compliance gaps.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
  , Aggregated Security Findings
  , SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Honeywell server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** and **API Secret** *(required)* - The credentials associated with a user account that has permissions to fetch assets. Note: Refer to the SCADAfence Multi-Site API reference guide for information on how to generate the API Key and API Secret.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Honeywell Cyber Watch" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Honeywell%20Cyber%20Watch.png" />

## APIs

Axonius uses the SCADAfence Multi-Site API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich Assets with Vulnerabilities** - Enable this to enrich assets with vulnerability data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 6.1.30.0