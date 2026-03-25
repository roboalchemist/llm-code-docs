# Source: https://docs.axonius.com/docs/solarwinds-network-performance-monitor.md

# SolarWinds Network Performance Monitor

SolarWinds Network Performance Monitor is a unified IT systems management system that tracks the performance of networks, applications, systems, and databases on-premises, in a hybrid environment, or in the cloud.

## Assets Types Fetched

This adapter fetches the following types of assets:

* Devices, Software, SaaS Applications, Networks

## About SolarWinds Network Performance Monitor

**Use cases the adapter solves**
Keeping Axonius data correlation capabilities in mind, you will be able to quickly identify any assets that are not being monitored by SolarWinds. The data SolarWinds provides allows better correlation in Axonius, which allows you to gain better insight into the performance of your infrastructure.

**Data retrieved by SolarWinds Network Performance Monitor**
Performance data, i.e.,  Power consumption, RAM usage, and CPU load. Network-level data, IP address, MAC addresses, and interface settings. OS data, build, distribution, serial number.

## Before You Begin

### Ports

Port 17774 for SWIS REST is default for SolarWinds.

### APIs

Axonius uses the [SolarWinds Orion SDK](https://thwack.solarwinds.com/community/it-resources/orion-sdk).

Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

**IP Address** – The hostname or IP Address of the SolarWinds management server.

1. **Authentication Method** - Select **Username and Password**, **API Key**, or **Bearer Token** as your method for authentication.
   * **User Name and Password** - The user name and password for an account that has admin access to the management server API. Note that the account might have to be a local account with admin access and not an AD integrated account.
   * **API Key** - Enter the API Key in the **User Name or API Key** field and the private key in the **Password or API Token** field. The API key is a long string included in either the request URL or request header (for example, Authorization: API\_KEY PRIVATE\_KEY). Some APIs require both a public and private key -- the public key is usually included in the request, and the private key is treated like a password.
   * **Bearer Token** - Enter the API token in the **Password or API Token** field. Refer to [API Tokens](https://documentation.solarwinds.com/en/success_center/observability/content/settings/api-tokens.htm) for information about the API Tokens

2. **Port** *(required, default: 17774)* - The port used for the connection. Port 17774 for SWIS REST is now default for SolarWinds. Note that from SolarWinds Release 2023.1 SWIS REST Endpoint on port 17778 is deprecated and has been replaced with port 17774. SolarWinds recommends you migrate SWIS REST Endpoint to port 17774.

<Image alt="SolarWindsNWPErfMon" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SolarWindsNWPErfMon.png" />

## Optional Parameters

1. **Custom Properties List** *(optional)* - Specify a comma-separated list of SolarWinds properties.
   * If supplied, the adapter connection will add a device field for each of the comma-separated list properties that have been defined in this field.
   * If not supplied, the adapter connection will not fetch any additional SolarWinds properties.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **Certificate File** *(optional)* - It is possible to  encrypt the SolarWinds DB connection and connect to it by using a Certification file. Upload the certificate file.

4. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. Fetch Types: Select the data to fetch from the drop down.
   1. **IPAM** - Select this option to fetch data from SolarWinds IP Address Manager (IPAM).  You must select this option to use the  **Fetch IPAM only if MAC address exists** or **Fetch IPAM only if status is "Used"** options.
   2. **UDT Endpoint Information** *(default: true)* - Select this option to fetch User Device Tracker endpoint information.
   3. **Wi-Fi information** *(default: true)* - Select this option to fetch Wi-Fi details. The Wi-Fi devices will then be presented as separate devices in the system.
   4. **Stack Members** - Select this option to fetch stack members.
   5. **Dependencies information** - Select this option to fetch dependencies information.
   6. **IPAM subnet by node IP** - Select this option to fetch subnet info from IPAM by the node IP. If enabled, this setting also parses the subnet info as networks.
   7. **Node custom properties** - Select this option to fetch the node custom properties.

2. **Fetch IPAM only if MAC address exists** - You must select **IPAM**  in Fetch Types to use this option. Select this option to fetch data from SolarWinds IP Address Manager (IPAM), but only for entities with a MAC address.

3. **Avoid Virtualization** - By default, SolarWinds marks all devices to be set as virtual devices. Select this option to avoid classification.

4. **CIDR exclude list** *(optional)* - Specify a comma-separated list CIDR blocks (for example: 192.168.20.0/24,192.168.30.0/24). so that the adapter will not collect devices with an IP address that is in the range of any of the comma-separated list of CIDR blocks that have been defined in this field.

5. **Use Lease Expiration as Last Seen** - Select whether to map SolarWinds' Lease Expiration field as the device's Last Seen field.

6. **Fetch IPAM only if status is "Used"** *(default: true)* - Select whether to only fetch IPAM devices with a status of "Used". Otherwise, all IPAM devices will be fetched, regardless of their status.  You must enable **Fetch IPAM** to use this option.

7. **Fetch IPAM with the status** *(optional)* - From the dropdown, select the IPAM devices to fetch according to their status. Supported statuses: **Used**, **Available**, **Reserved**, **Transient**. If nothing is selected, then all IPAM devices are fetched regardless of their status.

8. **Enable DNS as the Value for the FQDN Field** *(optional)* - Select to use the value in the DNS field for the FQDN field.

9. **Exclude devices which reside on the following VLANs** - Enter a comma separated list of VLANs not to fetch devices from.

10. **Round RAM Memory to the closest power of 2** - Select this option to round the RAM memory to the closest power of 2.

11. **Parse OS from VM host data (if available)** - Select this option to parse the operating system data from the `vim.host` Solarwinds Orion table (this is only used if data is available in the asset).

12. **Custom Fields List** - Specify a comma-separated list of additional SolarWinds custom fields to fetch.

13. **Parse Wifi Devices name as Host Name** - Select this option to parse the WiFi name as the Host Name.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Related Enforcement Actions

* [SolarWinds Network Performance Monitor - IPAM Information Enrichment](/docs/solarwinds-orion-ipam-enrichment)

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                                           | Supported | Notes                                                                                                                                                                              |
| ------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SolarWind Orion Platform version 2018.4 and later | Yes       | Axonius uses the [SolarWinds Orion SDK](https://thwack.solarwinds.com/community/it-resources/orion-sdk), which is supported for SolarWind Orion Platform version 2018.4 and later. |