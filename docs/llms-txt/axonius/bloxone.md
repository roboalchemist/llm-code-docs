# Source: https://docs.axonius.com/docs/bloxone.md

# Infoblox BloxOne

BloxOne DDI delivers central control and automation of DNS, DHCP, and IP address management for hybrid and multi-cloud networks.

### Asset Types Fetched

* Devices, Networks

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the following APIs:

* [BloxOne Rest API](https://blogs.infoblox.com/community/bloxone-rest-api/)
* [InfoBlox On-Prem Authentication Service API](https://csp.infoblox.com/apidoc?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FAuthnapi)
* [InfoBlox Infrastructure Management API](https://csp.infoblox.com/apidoc?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FInfrastructure#/Hosts/HostsList)

Create the API Key from the User Preferences Window. Follow the procedure on the video on their site.

### Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have read permissions to fetch assets.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Infoblox BloxOne  server.

2. **API Key** - An API Key associated with a user account that has permissions to fetch assets.

![Infoblox BloxOne connection screen](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/InfobloxBloxOne.png)

### Optional Parameters

1. **Verify SSL** - Choose whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Roaming Devices** *(default: true)* - By default, this adapter fetches roaming devices. Clear this option to not fetch roaming devices.
2. **Fetch Infra Appliances As Devices** - Select this option to fetch Infra Appliances as devices.
3. **Fetch IP Spaces** - Select this option to fetch data from the 'IP Spaces' endpoint.
4. **Fetch Address Blocks**- Select this option to fetch data from both the 'Address Block' endpoint and the 'Subnet' endpoint.
5. **Parse Network Tags As Fields** - Select this option to parse all tags dynamically as individual fields.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version             | Supported | Notes |
| ------------------- | --------- | ----- |
| BloxOne Rest API V1 | Yes       |       |