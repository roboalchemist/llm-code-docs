# Source: https://docs.axonius.com/docs/nucleussec.md

# Nucleus Security

Nucleus Security provides unified vulnerability management via integrations with third-party tools including threat intelligence, penetration testing, appsec, network scanners, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Nucleus Security server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="NucleusSecurity.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NucleusSecurity.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Issues severity to fetch** - Select the severity of issues to fetch. Only issues with the severity chosen are fetched. If no issues are selected, none are fetched.
2. **Project IDs** - Enter a list of project IDs to specify which projects you want to fetch from.
3. **Fetch project risk score** - Select this option to fetch the project risk score.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Nucleus API](https://api-docs.nucleussec.com/nucleus/docs/).

## Supported From Version

Supported from Axonius version 4.5