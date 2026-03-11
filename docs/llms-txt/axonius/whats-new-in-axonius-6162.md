# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6162.md

# What's New in Axonius Asset Cloud 6.1.62

#### Release Date: April 14th 2025

These Release Notes contain new features and enhancements added in version 6.1.62.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Cyber Assets New Features and Enhancements

The following new features and enhancements were added to Axonius Cyber Assets:

### Updated Name for Firewall Rule Assets

The 'Firewall Rules' Asset has been renamed 'Network/Firewall Rules.'

### Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter API Gateway Connection

Some adapters have the option to add a connection using API gateway parameters for authentication instead of the other authentication parameters. Currently, Axonius supports Layer 7 API Gateway authentication for the Netshot adapter.

### Activity Log New Features and Enhancements

**Additional Filters**
It is now possible to filter Activity Logs by data scope and by role.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**HCL AppScan**](/docs/appscan-enterprise)
  * HCL AppScan is an application security tool that provides vulnerability assessment and management. (Fetches: Business Applications)
* [**Let's Encrypt**](/docs/lets-encrypt)
  * Let's Encrypt is a non-profit certificate authority run by Internet Security Research Group that provides X.509 certificates for Transport Layer Security encryption at no charge. (Fetches: Certificates)
* [**Motus**](/docs/motus)
  * Motus is a platform that provides vehicle management and reimbursement solutions for mobile-enabled workforces. (Fetches: Users)

### Adapter Updates

The following adapters were updated:

* [**Akamai Kona WAF**](/docs/akamai-kona-waf) - Added the option to fetch dynamic IP firewall and network lists.

* [**Backstage**](/docs/backstage) - 'Generate a JWT Token Using the API Key' was added to connection parameters.

* **[NetBox](/docs/netbox#advanced-settings)** - Added the option to exclude device roles.

* [**Netshot**](/docs/netshot) - Added support of the Layer7 API Gateway for authentication for this adapter.

* [**PKWARE**](/docs/pkware)
  * Added the option to not enrich devices with assignments.
  * Added the option to not enrich devices with lockers.
  * Added the option to not enrich devices with locker status.
  * Added the option to allow locker duplications.
  * Added the option to avoid hostname duplications.

* [**Saviynt Security Manager**](/docs/saviynt) - Added the option to fetch attestation and entitlement data.

* [**Site24x7**](/docs/site24x7)
  * This adapter now fetches domains and URLs as assets.
  * Added the capability to select which asset types to fetch.
  * Added the option to parse URLs as devices, in addition to being parsed as URLs.

* [**Tenable.io**](/docs/tenableio) - Added the option to not fetch RECASTED vulnerabilities.

* [**Tenable Nessus**](/docs/tenable-nessus) - Added the option to use the asset's Netbios name as the asset name.

### New Enforcement Actions

The following Enforcement Actions were added:

* **[Illumio - Unpair VEN from Workload](/docs/illumio-unpair-vens)** - Stops the monitoring, enforcement, and security control that the VEN has over the workload, without completely deleting the workload or uninstalling the agent from the system.
* **[Illumio Delete Workload](/docs/illumio-delete-workload)** - Removes the workload from the Illumio policy enforcement framework.
* [**DigiCert - Renew Certificate**](https://docs.axonius.com/axonius-help-docs/docs/digicert-renew-cert) - Renews certificates with the DigiCert server.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Send JSON to S3**](/docs/send-json-to-amazon-s3) - Added the option to compress the file using GZip.