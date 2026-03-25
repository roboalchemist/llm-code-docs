# Source: https://docs.axonius.com/docs/cisco-dna-center.md

# Cisco Catalyst Center (formerly Cisco DNA Center)

Cisco Catalyst Center is a software-based network automation and assurance solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cisco Catalyst Center server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cisco DNA Center](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cisco%20DNA%20Center.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Get devices from the following "Client Detail" reports** *(optional)* - Enter names of "Client Detail" reports required in order to fetch additional devices from  configured “Client Detail” reports. Note that the reports must be in CSV format. If suitable reports are not found, additional details can be found in the fetch event logs.
2. **Report ID for Cisco AI Endpoint Analytics** *(optional)* - Enter the Report ID necessary in order to download the report file and then parse network devices from it.
3. **Get devices per site location** - Select this option to fetch devices via a method that includes the device site information.
4. **Fetch advisories per device** - Select this option to fetch Cisco Catalyst advisories. These advisories contain information about vulnerabilities, and the data can be found under the vulnerable software for relevant devices.
5. **Fetch Network Maps for Network Devices** - Select this option to enrich Device data with Network Maps, marking the locations of Network Devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Cisco Catalyst Center 2.3.7 API](https://developer.cisco.com/docs/dna-center/#!get-device-list).

## Required Permissions

The value supplied in [User Name](#parameters) must have the role of Network Administrator.