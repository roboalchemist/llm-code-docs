# Source: https://docs.axonius.com/docs/whats-new-in-axonius-706.md

# What's New in Axonius Asset Cloud 7.0.6

#### Release Date: August 24th 2025

These Release Notes contain new features and enhancements added in version 7.0.6.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

## Axonius Platform New Features and Enhancements

### System Settings New Features and Enhancements

The following updates were made to various System settings:

### AWS Secrets Manager Now Supports ARN Roles

When using the [AWS Secrets Manager](/docs/managing-external-passwords#aws-secrets-manager) for access, users can now upload an ARN role that points to a specific IAM role in AWS, which has its own set of permissions defined in its IAM policy. For example, the following role can be uploaded: `arn:aws:iam::123456789012:role/MyCrossAccountRole`.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Avanan**](/docs/avanan)
  * Avanan is an API‑based inline protection platform that offers multi‑layer threat detection and security event management across SaaS applications. (Fetches: Users, Network/Firewall Rules)
* [**Bluewater Control**](/docs/bluewater-control)
  * Bluewater is a network management tool that monitors and optimizes network performance. (Fetches: Devices, Users, Networks)
* [**Drata**](/docs/drata)
  * Drata is a compliance automation platform that offers continuous monitoring and evidence collection. (Fetches: Devices, Users, SaaS Applications)
* [**Elisity**](/docs/elisity)
  * Elisity is a security platform that provides identity-based microsegmentation and zero trust access control for managing network access to critical assets. (Fetches: Devices, Users, Network/Firewall Rules)
* [**Oracle Fusion Cloud Applications**](/docs/oracle-fusion-cloud-applications)
  * Oracle Fusion Cloud Applications is a suite that provides integrated cloud services for enterprise resource planning. (Fetches: Users, Roles)
* [**Pronto**](/docs/pronto)
  * Pronto enables organizations to accelerate collaboration and efficiency by seamlessly integrating data and workflows across departments and enterprise systems. (Fetches: Users)
* [**SonarQube Server**](/docs/sonar-qube-server)
  * SonarQube Server is a tool that provides automated code review and static analysis to detect coding issues and enforce quality rules. (Fetches: Vulnerabilities, Users, SaaS Applications, Application Resources)
* [**Vtiger CRM**](/docs/vtiger)
  * Vtiger CRM is a customer relationship management tool that provides unified sales, marketing, support, automation, analytics and contact management. (Fetches: Devices, Users)
* [**Workday VNDLY**](/docs/workday-vndly)
  * Workday VNDLY is a workforce management platform that provides contingent labor procurement, onboarding workflows, and vendor management functionality. (Fetches: Users, Application Resources)

### Adapter Updates

The following adapters were updated:

* [**Anomali Threatstream**](/docs/anomali-threatstream) - This adapter no longer fetches Vulnerabilities.

* [**CrowdStrike Falcon Discover**](/docs/crowd-strike-falcon-discover) - Added the option to avoid device duplications based on hostname.

* [**Duo Beyond**](/docs/duo-beyond) - Added the capability to specify the amount of days back to look for user activity logs.

* [**HAProxy**](/docs/haproxy) - Added support for API Version 3.

* **[IAVM Enrichment](/docs/iavm-enrichment)** - Added the option to upload a Client Key File when connecting the adapter.

* [**Microsoft Endpoint Configuration Manager (MECM) (formerly SCCM)**](/docs/microsoft-sccm) - Added two new authentication methods to connect the adapter: Kerberos with Password or Kerberos with Keytab.

* [**Microsoft Teams**](/docs/microsoft-teams) - Added the option to fetch Teams User Activity Report, including information such as the number of meetings organized by each user.

* [**Palo Alto Networks Cortex XDR**](/docs/palo-alto-networks-cortex-xdr) - Added the option to fetch incidents and alerts.

* [**PingIDM (formerly ForgeRock)**](/docs/forgerock) - Added an option to authenticate using Rest connection. When using this authentication method, the adapter fetches additional user information: internal and external users, roles, and managed users.

* [**PrivX**](/docs/privx) - Added the option to have the adapter try and resolve FQDN addresses to IP addresses.

* [**SecurityScorecard**](/docs/securityscorecard) - Added the option to fetch SaaS Applications, fetching all followed companies and their risk scores.

* [**SentinelOne**](/docs/sentinelone) - Added the option to deduplicate devices based on agent version.

* [**Slack**](/docs/slack) - Added the option to fetch Application Add-Ons.

* [**Venminder**](/docs/venminder) - This adapter now fetches Tickets and Organizational Units as assets.

* [**Windows Server Update Services (WSUS)**](/docs/windows-server-update-services-wsus) - Added the option to fetch downstream servers and the client computers attached to them.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Halo - Create Ticket**](/docs/halo-create-ticket) - Creates a Halo ticket for assets returned by the query or for selected assets.
* [**PANW Cortex XDR - Run Script**](/docs/paloalto-xdr-run-script) - Runs a script on assets returned by the query or on selected assets.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Qualys - Add IP Addresses to Asset Group**](/docs/add-ips-to-qualys-asset-group) - Added the options to send all preferred IP addresses without filters, or to send only public IP addresses.
* [**Tenable Vulnerability Management - Add IP Addresses to Target Group**](/docs/add-ips-to-tenableio-target-group) - Added the option to take IPs from the Public IPs field.
* [**ServiceNow - Create Assets**](/docs/create-servicenow-computer) - Added the option to create multiple relationships for one asset.