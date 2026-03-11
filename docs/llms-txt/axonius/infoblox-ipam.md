# Source: https://docs.axonius.com/docs/infoblox-ipam.md

# Infoblox IPAM and DHCP

Infoblox IPAM and DHCP is a platform that provides automated IP address management and Dynamic Host Configuration Protocol services.

<Callout icon="💡">
  For on-prem Infoblox NIOS use the [Infoblox DDI](https://docs.axonius.com/axonius-help-docs/docs/infoblox)  adapter.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Infoblox IPAM and DHCP server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Infoblox IPAM" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Infoblox%20IPAM.png" />

## APIs

Axonius uses the [Infoblox IP Address Management API](https://csp.infoblox.com/apidoc/?url=https://csp.infoblox.com/apidoc/docs/Ipamsvc#/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with a user account that has access to the assets the adapter needs to fetch.

## Supported From Version

Supported from Axonius version 6.1.45.0