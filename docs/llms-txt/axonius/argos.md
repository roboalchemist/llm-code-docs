# Source: https://docs.axonius.com/docs/argos.md

# Cyberint Argos Edge

Cyberint Argos Edge is an attack surface management solution providing findings into the external attack surface, phishing threats, brand impersonation, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Argos Edge server, such as `https://environment.cyberint.io/`

2. **Access Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Argos" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Argos.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Alerts Modified In Last X Days** - Specify the number of days back to fetch modified alerts. By default th,e API sets a filter of one day.
* **Enable fetch from Assets API** - Enable this option to have the adapter fetch Devices, Organizational Units, Users, Domains and URLs, and File Systems from the Assets API, according to the filter you configure. When you enable this, the following fields become available:
  * **Customer ID** *(required)* - Enter your customer ID.
  * **Filter assets by type** and **Filter assets by monitoring status** - Select the filters you want to apply to the fetch from each category's dropdown. For example, under **Filter assets by type**, you can choose to fetch only AWS accounts.
  * The following fields provide additional filtering options with numeric values. Enter the required number for the selected filter. For Example, if you want to **Fetch only technologies with the specified top CVE score or higher**, specify a CVE score.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Cyberint Alerts (1.0) API.

## Supported From Version

Supported from Axonius version 4.5