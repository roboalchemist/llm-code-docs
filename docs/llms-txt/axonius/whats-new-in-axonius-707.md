# Source: https://docs.axonius.com/docs/whats-new-in-axonius-707.md

# What's New in Axonius Asset Cloud 7.0.7

#### Release Date: August 31st 2025

These Release Notes contain new features and enhancements added in version 7.0.7.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

### Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

#### Adapters Fetch History

**Ignored Reasons**

When you hover over a row for any ignored asset column that shows the number of ignored assets, a tooltip now appears with the different reasons why those assets were ignored.

<Image alt="Adapters Fetch History Ignore Reasons.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapters%20Fetch%20History%20Ignore%20Reasons(3).png" />

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**6clicks**](/docs/six-clicks)
  * 6clicks is a governance, risk, and compliance platform that offers automated risk assessment and management solutions. (Fetches: Business Applications)
* [**InfoSec IQ Phishing Simulator Platform**](/docs/infosec-iq-phishing-simulator)
  * Infosec IQ is a security awareness platform that offers training and phishing simulations. (Fetches: Users, Tickets)
* [**OpenText Service Management (SMAX)**](/docs/opentext-service-management)
  * OpenText Service Management (SMAX) is a solution that provides AI‑powered automation for IT service management, asset lifecycle tracking, and enterprise service workflows. (Fetches: Tickets)
* [**Push Security**](/docs/push-security)
  * Push Security is a cybersecurity platform that helps organizations secure their SaaS environments by monitoring user behavior, detecting misconfigurations, and guiding employees to fix security issues directly through browser-based prompts.  (Fetches: Users, SaaS Applications, Alerts/Incidents)
* [**Scalefusion**](/docs/scalefusion)
  * Scalefusion is a tool that offers mobile device management solutions for securing and managing endpoints.  (Fetches: Devices, Users, Software, SaaS Applications)
* [**Security Journey**](/docs/security-journey)
  * Security Journey is a secure coding training platform that offers hands‑on lessons, assessments, and a reporting API for capturing developer learning metrics. (Fetches: Users)

### Adapter Updates

The following adapters were updated:

* [**Bently Nevada**](/docs/bently-nevada) - This adapter can now read text files.

* [**DNSFilter**](/docs/dnsfilter) - This adapter now supports authentication using an API Key.

* [**Duo Beyond**](/docs/duo-beyond) - Added the option that if a device has only one user, to set that user as the owner.

* [**FlexNet Manager Suite Cloud**](/docs/flexnet-manager-suite-cloud) - This adapter now supports Layer 7 API Gateway authentication.

* [**Huawei iMaster MAE**](/docs/huawei-imaster-mae)
  * Added more options for file sources to select from.
  * Added the capability to select XML files from a pre-defined list.

* [**IONIX (formerly Cyberpion)**](/docs/ionix)
  * Added the option to enrich domains with the Tests endpoint.
  * Added the option to fetch application services from the Cloud Assets endpoint.
  * Added the option to enrich cloud assets with the Tests endpoint.

* **Ivanti Security Controls** - Previously, the "OS Installed Security Patches" field showed all installed and available patches. Now, only patches with both the 'FoundPatch' and 'InstalledPatch' states are added to the "OS Installed Security Patches" field. All other patches are added to the new "OS Available Security Patches" field.

* [**Ivanti Unified Endpoint Manager (Landesk)**](/docs/ivanti-unified-endpoint-manager) - Added the capability to define a list of canonical software names to use for software normalization, to remove unnecessary information from the software name.

* [**Microsoft Defender for Endpoint (Microsoft Defender ATP)**](/docs/microsoft-defender-atp) - Added the option to fetch remediation information for vulnerabilities.

* [**Orca Cloud Visibility Platform**](/docs/orca-cloud-visibility-platform) - Added the option to fetch CVEs.

* [**Palo Alto Networks Cortex XDR**](/docs/palo-alto-networks-cortex-xdr) - Added the option to fetch incidents and alerts.

* **Prima Access Insights** - Connection Configuration updated to use Client ID, Client Secret and TSG ID.

* [**PrivX**](/docs/privx) - Advanced configuration added to fetch device connection details from the last specified number of days.

* [**Qualys Cloud Platform** ](/docs/qualys-cloud-platform) - This adapter now fetches Roles.

* [**Rapid7 InsightVM**](/docs/rapid7-insightvm) - Added the option to swap the Tag Key and Tag Value fields.

* [**SQL Server**](/docs/sql-server) - Added the option to aggregate devices by key.

* [**Snyk**  ](/docs/snyk)
  * Added the option to enrich projects (Application Resources) with issues.
  * Added the capability to use an alternate API URL in the connection configuration

* [**Trellix ePolicy Orchestrator (ePO)**](/docs/mcafee-epolicy-orchestrator-epo) - The name of the `McAfee ePolicy Orchestrator (ePO)` adapter was changed to **Trellix ePolicy Orchestrator (ePO)**. The names of the related [Enforcement Actions](/docs/whats-new-in-axonius-asset-cloud-707#updated-enforcement-actions) were changed accordingly.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**6clicks - Report Test Result**](/docs/six-clicks-report-test-result) - Creates a test result on an existing test in 6clicks.
* [**CrowdStrike Falcon - Create User**](/docs/create-crowd-strike-user) - Creates a CrowdStrike Falcon user.
* [**CrowdStrike Falcon - Delete User**](/docs/delete-crowd-strike-user) - Deletes a CrowdStrike Falcon user.
* [**CrowdStrike Falcon - Update User**](/docs/update-crowd-strike-user) - Updates a CrowdStrike Falcon user.
* [**CrowdStrike Falcon - Assign Role to User**](/docs/assign-role-to-crowd-strike-user) - Assigns a role to a CrowdStrike Falcon user.
* [**Push Security - Add/Remove Group to User**](/docs/push-security-alter-group-for-user) -
* [**Qualys - Launch Vulnerability Scan**](/docs/launch-vulnerability-scan) - Scans assets to detect vulnerabilities.
* [**Qualys - Update User**](/docs/qualys-update-user) - Updates a Qualys User.
* [**Qualys - Activate User**](/docs/qualys-activate-user) - Activates a Qualys User.
* [**Qualys - Suspend User**](/docs/qualys-suspend-user) - Suspends a Qualys User.
* [**Qualys - User Password Change** ](/docs/qualys-user-password-change) - Resets the password for a Qualys user.
* [**Qualys - Create User**](/docs/qualys-create-user) - Creates a new Qualys user.
* [**Snyk - Create Jira Issue**](/docs/snyk-create-jira-issue) - Create a Jira issue via Snyk
* [**Salesbuzz - Create User**](/docs/salesbuzz-create-user) - This action creates a user on Salesbuzz
* [**Salesbuzz - Manage Users**](/docs/salesbuzz-manage-users) - This action assigns a specified role to a Salesbuzz user, removes role assignment from a Salesbuzz user, or sets a Salesbuzz user to an active or inactive state.
* [**Tenable.sc (SecurityCenter) - Launch Scan**](/docs/tenable-sc-launch-scan) - Launches a scan on assets with a Tenable.sc UUID.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* The following actions were renamed:
  * **McAfee ePolicy Orchestrator (ePO) - Add or Remove Tag to/from Assets** was renamed as [**Trellix ePolicy Orchestrator (ePO) - Add or Remove Tag to/from Assets**](/docs/tag-in-mcafee-epolicy-orchestrator-epo).
  * **McAfee ePolicy Orchestrator (ePO) - Add Assets** was renamed as [**Trellix ePolicy Orchestrator (ePO) - Add Assets**](/docs/epo-add-asset).
* [**AWS - Send JSON to S3**](/docs/send-json-to-amazon-s3) - This enforcement action now supports assets created from System Queries.
* [**Tenable.sc (SecurityCenter) - Add or Remove IP Addresses to/from Assets**](/docs/add-ips-to-tenablesc-asset) and [**Tenable Vulnerability Management - Add IP Addresses to Scan**](/docs/add-ips-to-tenableio-scan) - Added the option to prevent these Enforcement Actions from failing when there is no data to update.