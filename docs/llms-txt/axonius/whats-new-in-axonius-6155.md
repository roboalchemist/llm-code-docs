# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6155.md

# What's New in Axonius 6.1.55

#### Release Date: February 23rd 2025

These Release Notes contain new features and enhancements added in version 6.1.55.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Assets Pages

## Devices  Page  New Features and Enhancements

The following new features and enhancements were added to the **Devices**  page.

#### EOL/EOS and Latest Version Support for Additional Operating Systems

[Devices](/docs/devices-page#os-end-of-life-end-of-support-and-latest-os-version) in Axonius now support End of Life, End of Support, Latest Version, and Is Latest Version for the openSUSE and SLES operating systems.

## SaaS Management New Features and Enhancements

**New SaaS Applications Field 'SSO Provider'**
A new ['SSO Provider'](/docs/saas-applications#static-fields) field has been added to SaaS Applications. This field displays the logo of the application configured as the Single Sign-On (SSO) provider for accessing the SaaS application.

## System Settings New Features and Enhancements

The following updates were made to System settings:

**Remove trailing spaces from preferred values**\
Axonius now provides the [option](/docs/configuring-data-aggregation-settings) to retain trailing spaces (spaces before and after values) in preferred fields. By default, Axonius removes these spaces.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**ConductorOne**](/docs/conductor-one)
  * ConductorOne is an Identity Governance and Administration (IGA) platform that provides comprehensive visibility, automation, and fine-grained access controls for modern environments. (Fetches: Users)
* [**ControlUp**](/docs/control-up)
  * ControlUp is a digital workspace management platform that provides real-time monitoring and troubleshooting for virtual desktop infrastructure (VDI) environments. (Fetches: Devices, Users, Vulnerabilities, SaaS Applications)
* [**eloomi**](/docs/eloomi)
  * eloomi is a learning management system that offers employee training and performance management solutions. (Fetches: Users)
* [**Forcepoint Security Manager Data Loss Prevention (DLP)**](/docs/forcepoint-dlp)
  * Forcepoint DLP is a data loss prevention solution that offers protection against data breaches and unauthorized access. (Fetches: Devices)
* [**HackNotice**](/docs/hacknotice)
  * HackNotice is a threat intelligence platform that provides alerts and insights on data breaches and security incidents. (Fetches: Users)
* [**Verve Security Center**](/docs/verve-security-center)
  * Verve Security Center is a cybersecurity platform that offers comprehensive protection for industrial control systems. (Fetches: Devices, Vulnerabilities, SaaS Applications)

### Adapter Updates

The following adapters were updated:

* [**Cherwell IT Service Management**](/docs/cherwell) - Added the capability to enter a string to fetch application data related to the device according to the specified relationship ID.
* **[Entra ID](/docs/microsoft-azure-active-directory-ad#general1)** - Added the option to designate specific user groups as "admin" groups.  Users belonging to these groups will have their 'Is Admin User' field set to 'True'.
* [**NetBox**](/docs/netbox) - Custom NetBox Domain Path Prefix was added to connection parameters.
* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - Added the option to use the latest API version when fetching Posture information.
* **[SentinelOne](/docs/sentinelone#setting-up-multifactor-authentication)** - It is now possible to use the new Axonius built-in authenticator to set up Multi-Factor Authentication when configuring the SentinelOne adapter connection.
* [**SQL Server**](/docs/sql-server) - Added support for Athena DB.
* [**STIG**](/docs/stig) - Added support for CKLB format.
* [**Trellix Endpoint Security (HX)**](/docs/fireeye-endpoint-security-formerly-hx) - The name of the `FireEye Endpoint Security (formerly HX)` adapter was changed to **Trellix Endpoint Security (HX)**.
* [**Zafran**](/docs/zafran)
  * Added the option to cancel running exports.

  * Added the capability to enter a valid ZQL query.

  * Added the option to enrich devices with vulnerabilities findings.

  * Added the option to specify the number of retries.

  * Added the option to specify the number of sleep seconds between retries.

  * Added the option to enrich findings with vulnerabilities.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Tenable.io - Launch WAS Scan**](/docs/tenable-io-launch-was-scan) - Launches a web application scan.