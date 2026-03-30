# Source: https://docs.axonius.com/changelog/release-notes-8017.md

# Axonius Release Notes 8.0.17

#### Release Date: March 1st 2026

These Release Notes contain new features and enhancements added in version 8.0.17.

# Axonius Platform New Features and Enhancements

## Dashboard

### Chart Enhancements

#### New Median Calculation Available on the Pivot Chart

Numerical fields can now be calculated to show the median value. For large volume data sets, an approximate median is used rather than an exact one, and there may be a deviation of up to 2% from the true median.

## New Adapters

* **[BACnet Scanner](https://docs.axonius.com/axonius-help-docs/docs/bacnet-scanner)** - Axonius-provided BACnet scanner, discovers BACnet devices on a network using the BACnet/IP protocol (Who-Is/I-Am). (Fetches: Devices)
* **[LivePerson](https://docs.axonius.com/axonius-help-docs/docs/liveperson)** - LivePerson is a conversational AI platform that enables businesses to engage with customers through messaging, chatbots, and agent tools. (Fetches: Users)
* **[Tenable Cloud Security](https://docs.axonius.com/axonius-help-docs/docs/Tenable-Cloud-Security)** - Tenable Cloud Security (formerly Ermetic) provides cloud-native application protection platform (CNAPP) capabilities for vulnerability management, compliance, and security posture management across multi-cloud environments. (Fetches: Devices, Aggregated Security Findings, SaaS Applications)
* **[Upwind](https://docs.axonius.com/axonius-help-docs/docs/Upwind)** - Upwind is a unified cloud-native application protection platform that provides runtime‑powered insights for detecting risks and mitigating misconfigurations across infrastructure and applications. (Fetches: Devices, Compute Services, Serverless Functions, Databases, Load Balancers, Network Services, Networks, Disks, File Systems, Object Storages, Secrets, SaaS Applications, Aggregated Security Findings)

## Updated Adapters

* **[Akamai Kona WAF](https://docs.axonius.com/axonius-help-docs/docs/akamai-kona-waf)** - Added an advanced configuration option to parse hostname as the URL's name.

* **[Box Platform](https://docs.axonius.com/axonius-help-docs/docs/box)** - Added the option to configure fetch of Application Settings in the advanced configuration.

* **[Censys ASM](https://docs.axonius.com/axonius-help-docs/docs/Censys-Asm)**
  * Added support for fetching Domain & URL assets.
  * Made several endpoints configurable (certificate, device, domain, and logbook endpoints are enabled by default).
  * Added an advanced configuration option to fetch URLs from the domain endpoint.

* **Cisco Catalyst Center (formerly Cisco DNA Center)**- Added an option to fetch Device Running Configuration and fetch various configuration settings.

* **[Cisco Identity Services Engine (ISE)](https://docs.axonius.com/axonius-help-docs/docs/cisco-identity-services-engine-ise)**
  * Added support for fetching Admin Users from the Cisco ISE ERS API.

* **[CrowdStrike Falcon](https://docs.axonius.com/axonius-help-docs/docs/crowdstrike-falcon)**
  * Added a new advanced configuration option to fetch CrowdStrike Alerts as Incident assets in Axonius.

* **[CyberArk Privilege Cloud](https://docs.axonius.com/axonius-help-docs/docs/Cyberark-Privilege-Cloud)** - Added a new parsing configuration option that allows you to choose the domain source for parsing account domains.

* **[Cymulate](https://docs.axonius.com/axonius-help-docs/docs/cymulate-recon)** - Improved rate limit management with configurable timers.

* **[Foreman](https://docs.axonius.com/axonius-help-docs/docs/foreman)** - Added an option to  fetch errata information.

* **[HCL Appscan](https://docs.axonius.com/axonius-help-docs/docs/Appscan-Enterprise)** - This adapter now supports authenticating with an API Key.

* **[i-doit](https://docs.axonius.com/axonius-help-docs/docs/I-Doit)**
  * Added name parsing functionality.
  * Added a configuration option for users.

* **[Infoblox BloxOne](https://docs.axonius.com/axonius-help-docs/docs/BloxOne)**
  * Added parsing of tags as individual fields.

* **[Ivanti Service Manager](https://docs.axonius.com/axonius-help-docs/docs/ivanti-service-manager)**
  * Added an advanced configuration option to enrich devices with network adapter component information.

* **[Juniper Junos](https://docs.axonius.com/axonius-help-docs/docs/juniper-junos)** - Added a "Disable RPC" configuration option in the adapter's connection parameters. When this option is enabled, the adapter uses SNMP only without RPC.

* **[ManageEngine Endpoint (Desktop) Central and Patch Manager Plus](https://docs.axonius.com/axonius-help-docs/docs/manageengine-desktop-central)** - Added an option to fetch high-risk software information including End-of-Life data.

* **[Palo Alto Networks Cortex XDR](https://docs.axonius.com/axonius-help-docs/docs/palo-alto-networks-cortex-xdr)** - Added a new advanced configuration option "XQL filter for daemon records" that allows you to insert a custom XQL filter on the Daemon query.

* **[Twistlock](https://docs.axonius.com/axonius-help-docs/docs/twistlock)** - Added support for newer API versions.

* **[Vectra AI](https://docs.axonius.com/axonius-help-docs/docs/vectra-ai)** - Added support for fetching Users.

* **[VMware Carbon Black App Control (Carbon Black CB Protection)](https://docs.axonius.com/axonius-help-docs/docs/carbon-black-cb-protection)** - Added a new advanced configuration option "Fetch Users" (disabled by default). When enabled, the adapter fetches console users from Carbon Black App Control and enriches them with their associated user group data.

## New Enforcement Actions

* **Trend Micro Vision One - Isolate Device** - Isolates a device in Trend Micro Vision One to prevent potential threats from spreading.
* **Hyland OnBase - Assign Group to User** - Assigns a group to a user in Hyland OnBase.

## Updated Enforcement Actions

* **[CSV - Send to Share](https://docs.axonius.com/axonius-help-docs/docs/send-csv-to-share)** - Added support for SMB v2 and v3 protocols when sending files to network shares.