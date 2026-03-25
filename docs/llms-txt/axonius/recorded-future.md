# Source: https://docs.axonius.com/docs/recorded-future.md

# Recorded Future

Recorded Future threat intelligence helps identify the vulnerabilities that pose an actual risk to an organization, adding context and data to CVE scoring.

**Related Enforcement Actions**

* [Recorded Future - Add or Remove Assets To/From Watchlist](https://docs.axonius.com/axonius-help-docs/docs/add-or-remove-assets-from-watchlist)

<br />

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.recordedfuture.com`)* - The hostname or IP address of the Recorded Future server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **List of CIDRs** -  Specify a comma-separated list of CIDR blocks (for example: 192.168.20.0/24,192.168.30.0/24) to connect to.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="RecordedFuture" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RecordedFuture.png" />

## APIs

Axonius uses the [Recorded Future Connect API](https://api.recordedfuture.com/v2/#/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich assets with CVE data** - Enable this to enrich assets with CVE information.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 2.18.0  | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7