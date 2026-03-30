# Source: https://docs.axonius.com/docs/risk-recon.md

# RiskRecon

RiskRecon is a cloud-based third-party risk management solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Vulnerabilities
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the RiskRecon server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![RiskRecon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RiskRecon.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Endpoints Config** - By default the adapter enriches users via various endpoints. Click on `>` to open the following settings for configurable endpoints:
  * **Fetch Devices from Hosts** - Toggle on to fetch devices from hosts.
    * **TOE ID** *(optional)* - If enabled, enter the TOE ID.
  * **Enrich Hosts with Findings** - Toggle on to enrich hosts with findings.
    * **TOE ID** *(optional)* - If enabled, enter the TOE ID.
  * **Enrich Hosts with Action Plan Findings** - Toggle on to enrich hosts with action plan findings.
    * **TOE ID** *(optional)* - If enabled, enter the TOE ID.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [RiskRecon API](https://api.riskrecon.com/v1/swagger/index.html#/Users/getUserData).

## Supported From Version

Supported from Axonius version 6.0