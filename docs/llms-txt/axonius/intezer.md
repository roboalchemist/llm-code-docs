# Source: https://docs.axonius.com/docs/intezer.md

# Intezer Protect

Intezer Protect offers runtime cloud workload protection.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
  , Aggregated Security Findings
  , Software, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Intezer Protect server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   To obtain an API key, click **Generate API Key**, located in your Intezer profile icon.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Intezer" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Intezer.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch installed packages** *(optional)* - Select whether to fetch installed packages.
2. **Fetch device alerts** *(optional)* - Select whether to fetch device alerts.
3. **Fetch Device Packages Concurrently** *(optional)* - Select whether to fetch installed packages concurrently.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Intezer Protect API](https://protect.intezer.com/api/doc#/Hosts/get_hosts).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V1      | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5