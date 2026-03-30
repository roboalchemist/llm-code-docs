# Source: https://docs.axonius.com/docs/tenable-asm.md

# Tenable.asm

Tenable Attack Surface Management (formerly Tenable.asm) continuously maps the internet and discovers connections to internet-facing assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Tenable.asm server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Tenablasm" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Tenablasm.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **List of tags to filter**  - Enter a list of tags to filter.
* **Include only assets with ports** - Check to fetch only assets that have ports.
* **List of ports to include (equal to)** - Provide a list of specific ports, only assets with these ports will be fetched.
* **List of record types to include (equal to)** - Provide a list of specific record types, only assets with these record types will be fetched.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Tenable ASM Bit Discovery API](https://bitdiscovery.com/api/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Supported From Version

Supported from Axonius version 6.0

## Related Enforcement Actions

* [Tenable.asm - Add Subdomains](https://docs.axonius.com/axonius-help-docs/docs/tenableasm-add-subdomains)