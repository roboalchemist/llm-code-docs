# Source: https://docs.axonius.com/docs/digicert-certcentral.md

# DigiCert CertCentral

DigiCert CertCentral consolidates tasks for issuing, installing, inspecting, remediating, and renewing certificates.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications
* Certificates

## Parameters

1. **API Key** *(required)* - An API key that has the [Required Permissions](#required-permissions) to fetch assets.
2. **Division IDs** *(optional)* - Set the Division IDs to connect to the specified divisions.

   * Multiple comma-separated values are accepted.
   * If supplied, Axonius will fetch only from the specified divisions.
   * If not supplied, Axonius will fetch all account data.
3. **Verify SSL** - Select to verify the SSL certificate offered by the hostname (used to connect to the API). For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-certificate).
4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the hostname (used to connect to the API).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="DigiCertCentral" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DigiCertCentral.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch only "Issued" orders**- Select whether to fetch only 'issued' orders.

   * If enabled, all connections for this adapter will only fetch 'issued' orders, without 'expired' orders.
   * If disabled, all connections for this adapter will fetch all orders.
2. **Do not populate hostname when domain name is NO\_DOMAINNAME\_SPECIFIED** - Select to not populate the hostname when the domain name isn't specified.
3. **Parse as certificate asset or device asset** - Select one of the options from the drop-down list to create either certificate assets, device assets, or both assets.
4. **Fetch order certificate notes** - Select this option to fetch order certificate notes.
5. **Fetch order certificate additional info** - Select this option to fetch order certificate additional information.
6. **Certificate Status Exclusions List** *(optional)* - Enter one or more comma-separated certificate statuses to exclude from the fetch.

## APIs

Axonius uses the following DigiCert APIS:

* Services API (`https://www.digicert.com/services/v2`)
* Discovery API (`https://daas.digicert.com/apicontroller/v1`)

## Required Permissions

The value supplied in [API Key](#parameters) must have Read access to devices.

To generate a new API Key, see [DigiCert Documentation - Generate an API key](https://dev.digicert.com/authentication/#generate-an-api-key).

To restrict the API keys permissions to read access to devices, in the **API key restrictions** dropdown, select **View Only**.

## Related Enforcement Actions

* [DigiCert - Renew Certificate](https://docs.axonius.com/axonius-help-docs/docs/digicert-renew-cert)