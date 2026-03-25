# Source: https://docs.axonius.com/docs/palo-alto-networks-panorama.md

# Palo Alto Networks Panorama

The Palo Alto Panorama management server provides centralized monitoring and management of multiple next-generation firewalls and appliance clusters.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Networks, Network/Firewall Rules

## About Palo Alto Networks Panorama

**Use cases the adapter solves**

Connecting Panorama to Axonius will allow you to quickly identify which assets are accessing the network over VPN. Specifically, Axonius can identify which private IP address is being used on the organization's internal network and identify which public IP address was used to access the VPN.

**Data retrieved by Panorama**

Network interface data about how the client connected to the VPN.

**Additional note**

Because it leverages the PanOS API, the Palo Alto Panorama adapter can be used to connect directly to Palo Alto firewalls if a Panorama endpoint is not available.

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password
* API Key

### APIs

Axonius uses the [Palo Alto Networks XML API](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-panorama-api/get-started-with-the-pan-os-xml-api/enable-api-access#ide6063ba8-2b0b-42eb-98c2-eb4914061722) and [REST API](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-panorama-api/get-started-with-the-pan-os-rest-api/access-the-rest-api).

### Permissions

<Callout icon="📘" theme="info">
  Note

  As a best practice, ensure that you create a separate, dedicated account for API access to Palo Alto Panorama.
</Callout>

* If you have supplied a [User Name](#required-parameters) - The username must be provided the [’Superuser (read-only)](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/firewall-administration/manage-firewall-administrators/administrative-role-types)' role.
  Instructions for associating this role with an  account can be found [here](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/firewall-administration/manage-firewall-administrators/configure-administrative-accounts-and-authentication#idab70b74d-1aaf-4701-a05c-a561251223f8).

* If you have supplied an [API Key](#required-parameters) - You can obtain an API key by following the instructions [here](https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-panorama-api/get-started-with-the-pan-os-xml-api/get-your-api-key.html#) as an alternative to using a username/password as described above (once the API has been enabled as described [here](https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-panorama-api/get-started-with-the-pan-os-xml-api/enable-api-access.html)).

* The following API permissions are required for basic Panorama configuration:
  * XML API (Configuration) - Required for fetching Firewalls, Firewall Rules, ARPs, and VPN Users.
  * XML API (Operational Requests) "Full Access" - Required to run SHOW command on firewalls. For more details, see:[https://support.axonius.com/hc/en-us/articles/360057994593](https://support.axonius.com/hc/en-us/articles/360057994593)
  * REST API (Panorama) - Required for fetching Device Groups.
  * REST API (Objects) - Fetch Address Groups.
  * REST API (Networks) - Fetch Networks associated with Device Groups to correlate with Firewall Rules.

* Optional API Permission:
  * XML API (Log permission) - Fetch users' login logs

### Palo Alto Networks Panorama Adapter Endpoints

Palo Alto Networks Panorama uses the REST and XML API, using different endpoints to retrieve the needed assets for the adapter to work properly:

For the XML API the adapter only uses one endpoint (api/) but it provides different paths in the URL parameters to retrieve different assets:

* Firewalls `(<show><devices><all /></devices></show>)`
* Panorama boxes `(<show><system><info></info></system></show>)`
* ARP table `(<show><arp><entry name=\'all\'/></arp></show>)`
* VPN `(<show><global-protect-gateway><{user_state}/></global-protect-gateway></show>)`
* Device Group Policies `(/config/devices/entry[@name="localhost.localdomain"]/device-group)`
* VSYS Policies `(/config/devices/entry/vsys/entry/rulebase/{rule_type})`
* Shared Policies `(/config/shared/{rule_base_type}/{rule_type})`
* VSYS Addresses `(/config/devices/entry/vsys/entry/address)`

For the REST API (restapi/v10.1), the adapter uses the following endpoints:

* Device Groups `(Panorama/DeviceGroups)`
* Device Group Addresses `(Objects/Addresses?location=device-group&device-group={device_group}&vsys=vsys1)`
* Shared Addresses `(Objects/Addresses?location=shared&vsys=vsys1)`
* Device Group Address Groups `(Objects/AddressGroups?location=device-group&device-group={device_group}&vsys=vsys1)`
* Shared Address Groups `(Objects/AddressGroups?location=shared&vsys=vsys1)`
* Zones `(Network/Zones?location=template&template={template}&vsys=vsys1)`
* Ethernet Interfaces `(Network/EthernetInterfaces?location=template&template={template}&vsys=vsys1)`

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Panorama Domain** - The hostname or IP address of the Palo Alto Panorama server or PA Firewall server.
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Key** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Key** is required.
</Callout>

<br />

<Image alt="PaloAltoNetworksPanorama.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PaloAltoNetworksPanorama.png" />

### Optional Parameters

* **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Panorama Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch ARP data** *(required, default: true)* - By default this adapter fetches ARP data from the Palo Alto Networks Panorama server. Clear this option to not fetch ARP data from the Palo Alto Networks Panorama server.
2. **Force logout of the user** -  Select this option to force logout of the account used to query the Palo alto Panorama data.
3. **Fetch Firewall Policies** - Select this option to fetch firewall security and NAT policies.
4. **Fetch Network Entities (Addresses, Interfaces)** - Select this option to fetch Addresses as an asset and to fetch Ethernet interfaces as a new device type.
5. **Enrich network interfaces with comments** - Select this option to enrich network interfaces with comments.
6. **Set the firewall last seen to the “connected-at” date if it is within the last X days** - Enter the amount of days necessary in order to set the firewall last seen to the “connected-at” date.
7. **Extend NAT Rules as connected devices** - Select this option to connect NAT firewall rules (public to private IPs only) with Network assets.
8. **Extend Access Rules as connected devices** - Select this option to connect Access firewall rules (from untrust sources) with Network assets.
9. **Fetch Users From Login Logs** - Select this option to fetch the one-day-old VPN login logs to parse users of type `LOGIN LOG`.
10. **Fetch Rules Hit Count** - Select this option to count the number of firewall rules.
11. **Internet Facing Zones** *(optional, default: any, untrust, outside)* - Enter a list of zones that are exposed to the Internet. This field will allow Axonius systems to tag devices that receive public traffic.
12. **CIDRs to be considered as internal/private** - Enter a list of CIDRs to be considered internal/private (IPs can be inserted with the suffix /32). Assets within the range of these CIDRs will be treated as belonging to internal systems.
13. **Addresses to be considered as internal/private** - Enter a list of Panorama addresses to be considered internal/private. Assets within the range of these addresses will be treated as belonging to internal systems.

<Callout icon="📘" theme="info">
  Note

  Both the above settings are used by the adapter to identify which firewall rules are exposing public traffic to internal systems.
  You should only use these fields in very specific cases. Normally using the Internet-facing zones is enough.
</Callout>

14. **Fetch HIP Match Logs** - Enable this option to fetch HIP match logs. If enabled, the following setting may be configured.
    * **Fetch HIP Match Logs From Date** *(default: Last 24 Hours)* - Select the dates from which you want the data to be retrieved.
15. **Exclude generic host devices** - Select this option to ignore all generic host devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />