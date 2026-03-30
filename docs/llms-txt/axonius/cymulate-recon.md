# Source: https://docs.axonius.com/docs/cymulate-recon.md

# Cymulate

Cymulate is a breach and attack simulation (BAS) platform that helps companies optimize security posture by testing internal and external defenses.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cymulate server. The default value is api.app.cymulate.com

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. Refer to Cumulate support for your key.

3. **Verify SSL** *(required, default: False)* - Choose whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CymulateADapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CymulateADapter.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Limit fetched data to last x days** *(required, default: 365)* - Select from how far back data will be fetched.
* **Fetch history from all past assessments** - Enable this to select from how far back ASM history will be fetched, and enter a value for **Date Range in Days**. This will fetch ASM history from the last specified number of days instead of the latest ASM endpoint.
* **Rate Limit Settings** Use the settings below to customize rate limit settings. Enter values to set the number of requests allowed per second.
  * **Number of requests allowed** *(Default: 15)* - Set the number of requests.
  * **Time window (seconds)** *(Default 10)* - Define the time window in seconds for this number of request.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Cymulate API](https://api.app.cymulate.com/docs/#/).

## Supported From Version

Supported from Axonius version 4.5