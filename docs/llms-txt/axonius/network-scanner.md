# Source: https://docs.axonius.com/docs/network-scanner.md

# Axonius Network Discovery

Axonius-provided Axonius Network Discovery adapter, performing standardized network discovery.
The Axonius Network Discovery adapter scans your network and discovers the assets connected to the network. This is an active scan and could be flagged by security systems as a possible penetration. The Axonius Network Discovery adapter runs on every discovery cycle and at any other custom discovery cycle configured.  Information fetched by this adapter can include the following parameters, depending on the asset:

* IP address
* Host name
* OS
* Open ports and their common use
* MAC address

This adapter fetches the following types of assets:

* Devices
* Certificates

**Related Enforcement Actions**

[Axonius Network Discovery - Enrich Asset Data](/docs/network-scanner-enrichment)

[Axonius Network Discovery - Scan](/docs/network-scanner-scan)

## Parameters for Customer-hosted (on-premises / private cloud)

* **Use Auto-discover Subnet** - Select this option to use the auto-discover IP range for the network discovery. This is a subnet of the Axonius machine (based on the IP address of the Axonius machine).
* **Additional Network Subnets** - Set an IP range to use.  When working with customer-hosted machines this is an optional field. The IP range should be input in CIDR format of IPv4 or IPv6 style for example 10.0.0.0/24 or 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64. Multiple ranges are supported using a delimiter.
* **Exclude Network Subnets** - Set an IP range to exclude.  The IP range should be input in CIDR format of IPv4 or IPv6 style for example 10.0.0.0/24 or 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64. Multiple ranges are supported using a delimiter.
* **Ports to scan** *(default Top 100)* - Set the number of ports to scan, either 'Top 100', 'Top 1000' or `Full’ for all ports (1-65535); or `Custom only' - If you select 'Custom only', only the custom ports listed in the *Custom ports to scan* field are scanned.
* **Exclude Dangerous Ports From Scan (9100)***(default: true)*- By default the system does not scan the printer port 9100. Clear this setting to scan port 9100.
* **Custom ports to scan** *(use comma or hyphen)* - You can add custom ports to scan, either specific ports separated by commas, or a range of ports separated by hyphens. If you select Top 100 or Top 1000 in the ports to scan field, the system will scan those ports, and in addition it will scan any ports listed in this field. If you only want to scan the ports listed in this field, select *Custom only* in the *Ports to scan* drop down.
* **Hosts to exclude from scan** - Enter a comma separated list of hosts to exclude from the scan.
* **Ports to exclude from scan** - Enter a comma separated lists of ports to exclude from the scan.
* **Comma separated list of new DNS resolvers** - Add a comma separated list of DNS resolvers. The system will then use them to get the DNS name of the device from the IP address.

<Image alt="AxoniusNetworkDiscovery" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AxoniusNetworkDiscovery.png" />

## Parameters for Axonius-hosted (SaaS)

<Callout icon="📘" theme="info">
  Note

  If the source for an adapter connection is only accessible by an internal network, you must set the relevant Gateway Connection as part of the Adapter Connection settings.
</Callout>

1. **Network Subnets** - Set an IP range to use. For Axonius-hosted (SaaS) systems, this parameter is a required field.  The IP range should be input in CIDR format of IPv4 or IPv6 style for example 10.0.0.0/24 or 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64. Multiple ranges are supported using a delimiter.
2. **Ports to scan** - Set the number of ports to scan, either 'Top 100' ,  'Top 1000' or 'Full’ for all ports (1-65535).
3. **Gateway Name** - You have to select a gateway connection when running the Network Scanner adapter on Axonius-hosted (SaaS) systems.

<Callout icon="📘" theme="info">
  Note

  Any additional parameters are the same as above  under *Parameters for Customer-hosted (on-premises / private cloud)*.
</Callout>

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch certificate data from hosts** *(default: false)*   - Select how to fetch certificate data from hosts, either in Normal Fetch, Background Fetch or Disabled.
2. **Parse the operating system field** *(default: true)* - Enable to fetch and parse the Operating System field.
3. **Timeout for a single scan (seconds)** *(optional)* - Set a single scan timeout in seconds.
4. **Include detailed information in Fetch Event Logs** *(default: false)* - Enable to fetch the event log with the full details. Note that this might increase significantly the size of the fetch event.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Protocols Used

The following protocols are used in the scan:
ICMP, ARP, Banner Grabber

## Tools Used

The following open source tools are used by the scanner:

* [naabu](https://github.com/projectdiscovery/naabu)
* [sx](https://github.com/v-byte-cpu/sx)
* [zgrab2](https://github.com/zmap/zgrab2)
* [p0f](https://lcamtuf.coredump.cx/p0f3/)

## Supported From Version

Supported from Axonius version 4.6