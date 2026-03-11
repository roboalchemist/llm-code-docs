# Source: https://docs.axonius.com/docs/extra-hop-360.md

# ExtraHop Reveal(x) 360

ExtraHop Reveal(x) 360 is a SaaS-based network detection and response (NDR) platform that provides unified security across on-premises and cloud environments.

The ExtraHop Reveal(x) 360 adapter enables Axonius to fetch and catalog network devices, providing visibility into their network behavior and security context.

## Asset Types Fetched

* Devices
* Networks

## Before You Begin

### Required Ports

* TCP Port 80/443

### Required Permissions

The value supplied in **API Key** must be associated with credentials that have **Read** permissions in order to fetch assets.

### APIs

Axonius uses the <Anchor label="Reveal(x) 360 REST API Guide | ExtraHop" target="_blank" href="http://docs.extrahop.com/current/rx360-rest-api/">Reveal(x) 360 REST API Guide | ExtraHop</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 4.8.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ExtraHop Reveal(x) 360 server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **ID** and **Secret** *(required)* - The ID and secret of the REST API credentials (see "Create REST API credentials" section in [Reveal(x) 360 REST API Guide | ExtraHop](http://docs.extrahop.com/current/rx360-rest-api/)).

<Image alt="ExtraHopRevealX360" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExtraHopRevealX360.png" />

### Optional Parameters

1. **Fetch devices from the last X days** *(optional)* - Fetch active devices last seen by the number of days specified.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **Parse dhcp\_name as hostname** - Select this option to use the DHCP name as the device hostname. When enabled, the adapter parses the `dhcp_name` field and populates it into the hostname field for the device.
* **Fetch VLANs as Networks** – Select this option to fetch VLAN information as networks. When enabled, the adapter retrieves VLAN data and parses VLAN as a network asset type.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1      | Yes       | --    |

<br />

<br />