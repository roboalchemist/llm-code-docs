# Source: https://docs.axonius.com/docs/normalization-reasons-complex-field.md

# Normalization Reasons Complex Field

The **Normalization Reasons** table displays indicators that use the holistic data available in Axonius to hint why a record didn't correlate with others. The details displayed include:

* **Normalization Reason** - The normalizer's name
* **Field name** - The name of the field that is being correlated
* **Field Value** - The value of the field
* **Calculated time** - The time in the discovery cycle at which this was found

![NormalizationReasonsTable](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-RYINB8J8.png)

Below is a list of the reasons that can be displayed for different asset types.

## Devices

* **Bad Hostnames By Cloud ID** - Used to indicate that this hostname might be overlapping between multiple cloud assets. A Cloud ID should represent a single asset; a hostname seen with multiple Cloud IDs is suspected to be overlapping.
* **Bad Names By Cloud ID** - Used to indicate that this asset name might be overlapping between multiple cloud assets. A Cloud ID should represent a single asset; an asset name seen with multiple Cloud IDs is suspected to be overlapping.
* **Bad Hostnames By Cloud Provider** - Used to indicate that this hostname might be overlapping between multiple cloud providers. A hostname seen with multiple Cloud providers is suspected to be overlapping.
* **Bad Hostname By Serial** - Used to indicate that this hostname might be overlapping between different devices. A Device Serial is normally a hardware identifier representing the BIOS serial, and as such, it should be unique. A Hostname that is related to multiple serial numbers is suspected to be overlapping.
* **Bad Hostnames By OS types** - Used to indicate that this hostname might be overlapping between multiple OS types. A hostname seen with multiple OS types is suspected to be overlapping.
* **Bad Asset Names By OS types** - Used to indicate that this asset name might be overlapping between multiple OS types. An asset name seen with multiple OS types is suspected to be overlapping.
* **Bad Serials By Hostnames** - Used to indicate that this serial might be considered as not unique since it is related to multiple hostnames. A Device Serial is normally a hardware identifier representing the BIOS serial and as such, it should be unique.
* **Bad Serials By Asset Names** - Used to indicate that this serial might be considered as not unique since it is related to multiple asset names. A Device Serial is normally a hardware identifier representing the BIOS serial and as such, it should be unique.
* **Bad Hostname By MachineID** - Used to indicate that this Microsoft Defender hostname might be overlapping between multiple machine ids. A Machine ID should represent a single machine; a hostname seen with multiple Machine IDs is suspected to be overlapping.
* **Bad Name By Entra Object ID** - Used to indicate that this device name might be overlapping between multiple Entra Object IDs. An Object ID should represent a single device within a tenant; a name seen with multiple Object IDs within the same tenant is suspected to be overlapping.
* **Bad Private IP By Domains** - Used to indicate that this private IP might be overlapping across different domains. A private IP seen across multiple domains is suspected to be overlapping and should be ignored.
* **Bad VMware-ServiceNow Fields By AX-Unique-ID** - Used to indicate that this unique ID might be overlapping between multiple VMware and ServiceNow adapter devices. Identifiers such as MAC addresses, hostnames, asset names, and serial numbers are used to detect overlaps.
* **Bad ServiceNow Hostnames By Agents** - Used to indicate that this hostname or asset name might be overlapping between multiple serial numbers. A Device Serial is normally a hardware identifier representing the BIOS serial; a hostname or an asset name seen with multiple serial numbers is suspected to be overlapping.
* **Bad Infoblox Hostname By FQDN** - Used to indicate that this Infoblox hostname might be invalid as its Fully Qualified Domain Name (FQDN) does not match. The hostname is ignored if there is a mismatch.
* **Bad IPs By Stacked Switch** - Used to indicate that this IP address might belong to a stacked switch device and should be ignored.
* **Bad Phone Numbers By IMEI** - Used to indicate that this phone number might be overlapping between multiple mobile devices based on their IMEIs. An IMEI is a unique identifier for a device; a phone number associated with multiple IMEIs is suspected to be non-unique within their environment.
* **Bad IMEI By Serial** - Used to indicate that this IMEI might be overlapping between multiple devices based on their serial numbers. A serial number should uniquely identify a device; an IMEI associated with multiple serial numbers is suspected to be non-unique within their environment.
* **Bad Hostnames By HP NNMI Long Names** - Used to indicate that this hostname might be overlapping between multiple devices based on long names provided by the HP NNMI adapter. A long name should be unique to a device; a hostname associated with multiple long names is suspected to be overlapping.
* **Bad Serials By ESX UUID** - Used to indicate that this serial number might be overlapping between multiple devices based on their ESX UUIDs. A UUID should uniquely identify an ESX device; a serial number associated with multiple UUIDs is suspected to be non-unique within their environment.
* **Bad Bios Serials By Hostnames** - Used to indicate that this BIOS serial might be overlapping between multiple devices based on their hostnames. A hostname should uniquely identify a device; a BIOS serial associated with multiple hostnames is suspected to be non-unique within their environment.
* **Bad Hostnames By Rumble Sites** - Used to indicate that this hostname might be overlapping between multiple devices based on Rumble site names. A site name should uniquely identify a group of devices; a hostname associated with multiple site names is suspected to be overlapping.
* **Bad Short Hostnames By FQDN** - Used to indicate that this short hostname might be overlapping between multiple devices based on their Fully Qualified Domain Names (FQDNs). A short hostname should uniquely identify a device; a short hostname associated with multiple FQDNs is suspected to be non-unique within their environment.
* **Bad Short Asset Names By FQDN** - Used to indicate that this short asset name might be overlapping between multiple devices based on their Fully Qualified Domain Names
* **Bad Azure Name By Azure Device ID** - Used to indicate that this Azure display name might be overlapping between multiple assets with different Azure Device IDs. A display name shared by multiple Azure Device IDs is suspected to be overlapping.
* **Bad AD Name By AD Guid** - Used to indicate that this AD display name might be overlapping between multiple assets with different AD GUIDs. A display name shared by multiple AD GUIDs is suspected to be overlapping.
* **Bad FQDN By Cloud ID** - Used to indicate that this FQDN might be overlapping between multiple assets with different Cloud IDs. An FQDN shared by multiple Cloud IDs is suspected to be overlapping.
* **Bad Hostnames By IMEI** - Used to indicate that this hostname might be overlapping between multiple devices with different IMEIs. A hostname shared by multiple IMEIs is suspected to be overlapping.
* **Bad Asset Names By IMEI** - Used to indicate that this asset name might be overlapping between multiple devices with different IMEIs. An asset name shared by multiple IMEIs is suspected to be overlapping.
* **Bad Hostnames By VMware UUID** - Used to indicate that this hostname might be overlapping between multiple virtual machines with different VMware UUIDs. A hostname shared by multiple VMware UUIDs is suspected to be overlapping.
* **Bad Hostnames By Serial Many Adapters** - Used to indicate that this hostname might be overlapping between multiple devices with different serial numbers across multiple adapters. A hostname shared by multiple serial numbers is suspected to be overlapping.
* **Bad Hostnames By Azure Subscription ID** - Used to indicate that this hostname might be overlapping between multiple assets with different Azure Subscription IDs. A hostname shared by multiple Subscription IDs is suspected to be overlapping.
* **Bad Hostnames By ESX Duplicate Names** - Used to indicate that this hostname might be overlapping between multiple machines identified in ESX. A hostname shared by multiple ESX machines is suspected to be overlapping.
* **Bad Names By ESX Duplicate Names** - Used to indicate that this asset name might be overlapping between multiple machines identified in ESX. An asset name shared by multiple ESX machines is suspected to be overlapping.
* **Bad Hostnames By ServiceNow Duplicate Hostnames** - Used to indicate that this hostname might be overlapping between multiple assets with different sys\_ids in ServiceNow. A hostname shared by multiple sys\_ids is suspected to be overlapping.
* **Bad Asset Names By ServiceNow Duplicate Asset Names** - Used to indicate that this asset name might be overlapping between multiple assets with different sys\_ids in ServiceNow. An asset name shared by multiple sys\_ids is suspected to be overlapping.
* **Bad Hostnames By Jamf Duplicate Hostnames** - Used to indicate that this hostname might be overlapping between multiple devices identified in Jamf. A hostname shared by multiple devices is suspected to be overlapping.
* **Bad Hostnames By Cherwell Printers** - Used to indicate that this hostname might be overlapping between multiple printers identified in Cherwell. A hostname shared by multiple printers is suspected to be overlapping.
* **By MAC Normalizer** – Used to indicate that a MAC address may be shared among multiple devices. A MAC address should uniquely identify a device; A MAC address associated with multiple devices is considered non-unique within the environment and is therefore excluded from correlation based solely on MAC addresses.

## Users

* **Bad Usernames By Last Name** - Used to indicate that this username might be overlapping between multiple users. A user has only one last name; a username seen with multiple last names is suspected to be overlapping.
* **Bad Mails By Employee ID** - Used to indicate that this mail might be overlapping between multiple employee IDs. A unique mail address is associated with a single employee (user); a mail seen with multiple employee IDs is suspected to be overlapping.
* **Bad Mails By Username** - Used to indicate that this mail might be overlapping between multiple users. A username should represent a single user; a mail seen with multiple usernames is suspected to be overlapping.
* **Bad Mails by Service Account** - Used to indicate that this mail belongs to a service account and won’t be used for correlation.