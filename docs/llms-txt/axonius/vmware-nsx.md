# Source: https://docs.axonius.com/docs/vmware-nsx.md

# VMware NSX

VMware NSX provides an agile software-defined infrastructure to build cloud-native application environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Load Balancers, Network/Firewall Rules

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the VMware NSX server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  To learn more, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="VMwareNSX" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VMwareNSX.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Device types to fetch** *(required, default: NSX Device)* - Select from dropdown the device types that will be fetched with this connection. Supported device types: **Cloud Device**, **NSX Device**.
2. **Fetch firewall rules** *(required, default: true)* - Select this option to enrich devices with firewall rules.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [NSX-T Data Center REST API](https://developer.broadcom.com/xapis/nsx-t-data-center-rest-api/latest/).

## Required Permissions

The value supplied in [User Name](#parameters) must have the following permissions in order to fetch assets:

1. **read:cloud\_resources**
2. **read:vm\_vm\_info**
3. **read:firewall\_general** *(optional, required for fetching firewall rules)*

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                      | Supported | Notes                          |
| ---------------------------- | --------- | ------------------------------ |
| VMware NSX device API V3.1.2 | Yes       | --                             |
| VMware NSX device API V2.4   | Partial   | Some endpoints do not exist.   |
| VMware NSX device API V4.0   | Partial   | Some endpoints are deprecated. |

## Supported From Version

Supported from Axonius version 4.8