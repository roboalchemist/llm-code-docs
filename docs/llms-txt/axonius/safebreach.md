# Source: https://docs.axonius.com/docs/safebreach.md

# SafeBreach

SafeBreach offers a breach and attack simulation platform that helps organizations locate and remediate security issues.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SafeBreach server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Account ID** *(required)* - SafeBreach account identifier.

3. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SafeBreach](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SafeBreach.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich Nodes with Simulation Steps** - Toggle on to enable the addition of Simulation Steps from the execution history to each Node. When enabled, the following setting can be configured:
  * **Simulations Query** *(optional, default: 7 days)* - Specify an execution history filter to limit the amount of simulations to include.  Note that this impacts fetch time and completion. The API allows up to 1M records.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the SafeBreach API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443/80**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0