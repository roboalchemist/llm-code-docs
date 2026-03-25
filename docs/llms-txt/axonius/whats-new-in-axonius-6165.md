# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6165.md

# What's New in Axonius Asset Cloud 6.1.65

#### Release Date: May 4th 2025

These Release Notes contain new features and enhancements added in version 6.1.65

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Axonius Exposures

**Axonius Exposures** provides a comprehensive approach to managing and mitigating risk across your entire IT ecosystem. Axonius Exposures aggregates data from various sources and continuously discovers security findings, helping you stay on top of your environment in real time.

Here's how you can benefit from Exposures:

* Receive a unified view of all the vulnerabilities in your organization and their hosts.
* Improve prioritization - with asset, vulnerability, and network context.
* Visualize connections between threats and assets.
* Track vulnerability resolution status, and time to resolution.
* Set and track SLA and compliance.
* Identify internet-exposed assets for comprehensive risk score calculation.

Exposures offers the following:

**Vulnerabilities**

The [Vulnerabilities](/docs/vulnerabilities) page offers a consolidated view of all the vulnerabilities in your organization from all sources.

![VulnerabilitesUP](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VulnerabilitesUP.png)

**Vulnerability Instances**

The [Vulnerability Instances](/docs/vulnerability-instances) page lists vulnerabilities in the context of specific hosts. The Vulnerability Instances view helps security, IT, and risk teams identify vulnerabilities in specific devices, enabling them to prioritize vulnerabilities by combining security, asset, and business context from a single place.

![VIPage](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-PSISNTWH.png)

**Risk Score Calculation**

[Axonius Risk Score Calculation](/docs/risk-score) offers a robust solution to assess threat levels and prioritize remediation efforts. Users can calculate the risk scores of different asset types by creating custom conditions and parameters, based on account risk, business impact, and exploitability considerations.

<Image alt="RiskScoreDevicesAction.png" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RiskScoreDevicesAction(1).png" />

[ **Vulnerability Enrichment**](/docs/vulnerability-enrichment)

Axonius uses a variety of sources to collect information on reported CVEs and enriches them with that information, including severities and details on the vulnerable software or vendor.
The enrichment sources used by Axonius are as follows:

| Source name                                                                                                                     | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NVD ![NVDIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NVDIcon.png)                        | Indicates Vulnerabilities enriched with data from the [NIST NVD](https://nvd.nist.gov/vuln) database.                                                                                                                                                                                                                                                                                                                                                            |
| EPSS ![EPSSIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EPSSIcon.png)                     | Indicates   software vulnerabilities enriched with details from the [Exploit Prediction Scoring System EPSS](https://www.first.org/epss/model) from connected adapters.                                                                                                                                                                                                                                                                                          |
| **CISA** ![CISA\_logo\_50x50](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CISA_logo_50x50.png) | Indicates Vulnerabilities enriched with  vulnerabilities information from your connected adapters with additional details from the [CISA Known Exploited Vulnerabilities (KEV) Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). When relevant, the CISA fields and information are available for viewing and querying in the Vulnerabilities module and Devices module. Only CVEs that are part of the CISA KEV Catalog will be enhanced. |

MSRC <Image alt="MSRCVulnLogo" width="50px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MSRCVulnLogo.png" /> |Indicates   software vulnerabilities enriched with details  from MSRC from connected adapters.  |

\| VulnCheck  ![Vulncheck](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/vulncheck.svg) | Indicates Vulnerabilities enriched with data from the VulnCheck enrichment enforcement action.
\| Intel 471 Enrichment  ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-17JEX16H.png) | Provides cyber threat intelligence to assess, identify, and manage potential risks.
\| Mandiant Enrichment  ![image](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Mandiant%20Logo.svg) | Offers threat intelligence, incident response, and security consulting services to detect and mitigate advanced cyber threats.

[**Static Analysis**](/docs/vulnerability-static-analysis)

Axonius Static Analysis  identifies CVEs within the installed software reported by adapters. To achieve this, Axonius leverages Common Platform Enumerations (CPEs) and the National Vulnerability Database (NVD). The process includes mapping every installed software on each device, normalizing the data, converting it into the calculated CPE of the installed software, and then - based on the information received from NVD - listing all CVEs associated with the software installed on each device.

[**Publicly Exposed by**](/docs/publicly-exposed-by)

The Publicly Exposed by table shows assets that are reachable by external attackers as network traffic changes IP through subnets, load balancers, and firewalls. Axonius compiles the Public Exposed By information by reading configuration from your network equipment, such as load balancers and firewalls.

## Software Assets   New Features and Enhancements

The following new features and enhancements were added to Software Assets:

The "Is Excluded" field was added to the Software page. This aggregated field exists only if certain adapters (for example: Jamf Pro) have the "Installed Software: Is Blacklisted" field in the Devices page.

## Axonius Platform New Features and Enhancements

### Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Compare Results to Previous Date on Adapter Segmentation Chart

The Adapter Segmentation chart now supports comparing query results to a previous date. This provides additional context for your data and highlights changes in the results.

#### Dashboard-Level Filters Are Applied in the Chart Wizard Preview

When a filter is applied to a dashboard, that same filter is displayed, but cannot be edited, in the Chart Wizard preview for each of the charts in that dashboard.

### Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

#### Adapter Fetch History Enhancements

* A Refresh button was added to the **[Adapter Fetch History](/docs/adapters-fetch-history)**  page that allows users to refresh the data on the page without losing the filters configured.

## Data Analytics New Features and Enhancements

The following updates were made to the Data Analytics module:

* All rows can be expanded or collapsed at the same time.
* The number of rows displayed automatically fits the size of the screen.
* View the total row at bottom of the table using **Scroll to Bottom** and return with **Scroll to Top**.
* Blank values are removed with the empty field not "blank".
* Export data analytics reports to the following formats: Print, HTML, CSV, Excel, Image, and PDF.
* Apply color scheme to the table.

![DataAnalyticsUpdates.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DataAnalyticsUpdates.png)

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Enhancements to Axonius Actions

#### Axonius  - Export Assets to Instance

Added the option to only export assets from the asset type that is queried.

#### Axonius - Send Email per Asset

Added the option for the Plain-text mail to include the custom message only.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Bently Nevada**](/docs/bently-nevada)
  * Bently Nevada is a condition monitoring system that provides asset protection and predictive maintenance solutions. (Fetches: Devices)
* [**Cisco Nexus Dashboard**](/docs/cisco-nexus-dashboard)
  * Cisco Nexus Dashboard is a platform that offers centralized management and monitoring for network operations. (Fetches: Devices)
* [**Mandiant Enrichment**](/docs/mandiant-enrichment)
  * Mandiant is a cybersecurity platform offering threat intelligence, incident response, and security consulting services to detect and mitigate advanced cyber threats.  (Fetches: Devices)
* [**ZipHQ**](/docs/ziphq)
  * ZipHQ License Management is a comprehensive software solution designed to streamline and automate the management of software licenses across an organization. (Fetches: Licenses, SaaS Applications)

### Adapter Updates

The following adapters were updated:

* [**Active Directory Certificate Services (AD CS)**](/docs/adcs)
  * Added the capability to enter a semicolon-separated list of templates to exclude from the fetch.
  * Added the capability to set a future expiration date to filter certificates by.

* [**Akamai Kona WAF**](/docs/akamai-kona-waf) - Added the option to fetch Rules tree and hostname list from Property Manager.

* [**Amazon Web Services (AWS)**](/docs/amazon-web-services-aws) - Added the option to enrich RDS assets with KMS information.

* [**BeyondTrust Remote Support**](/docs/beyondtrust-remote-support) - Added the option to not parse public IPs to Network Interfaces.

* [**Burp Suite**](/docs/burpsuite) - This adapter now fetches domains and URLs as assets.

* [**CyberArk Privileged Account Security**](/docs/cyberark-privileged-account-security) - Added the option to enrich Users and Groups with permitted safes.

* [**Forcepoint ONE**](/docs/forcepoint-one) - Added support for OAuth authentication.

* [**Google Cloud Platform (GCP)**](/docs/google-cloud-platform-gcp) - Added the option to fetch Google Instance Groups as Compute Services.

* [**HPE Switches**](/docs/hpe-switches) - SNMP Protocol was added to connection parameters.

* [**IBM Guardium Data Protection**](/docs/ibm-guardium-vulnerability-assessment)
  * The name of the 'IBM Guardium' adapter was changed to **IBM Guardium Data Protection**.
  * Added the option to fetch STAP configuration.

* [**Ivanti Service Manager**](/docs/ivanti-service-manager) - URL Base Prefix was added to connection parameters.

* [**LogicGate**](/docs/logicgate) - Added the option to enrich users with records.

* [**ManageEngine Network Configuration Manager**](/docs/manageengine-network-configuration-manager)
  * This adapter now fetches vulnerabilities and SaaS applications.
  * Added the option to enrich the device summary with device vulnerabilities.

* [**Microsoft Azure**](/docs/microsoft-azure) - This adapter now fetches Traffic Manager Profiles as Load Balancers.

* [**Nexthink Query Language (NQL)**](/docs/nexthink-infinity-nql)
  * Software Query ID was added to connection parameters.
  * This adapter now fetches software and SaaS applications. An optional advanced setting can be configured to do this.

* [**Nutanix AHV**](/docs/nutanix-ahv) - Added the option to parse the serial field from the 'block\_serial' raw data instead of 'serial'.

* [**Oracle Fusion HCM Cloud**](/docs/oracle-fusion-hcm-cloud) - Added the option to parse user assignments as Security Roles.

* [**Proofpoint Endpoint DLP**](/docs/proofpoint-endpoint-dlp) - Added an option to parse `Last Seen (Updater)` and 'Last Seen' fields with the same value.

* [**ServiceNow**](/docs/servicenow) - Added the new **Devices: Unset Downstream and Upstream fields if not populated in fetch results** option to automatically clear existing field values in the **Downstream** and **Upstream** complex object fields on devices when no new values are returned during a ServiceNow fetch. This is useful for optimizing 'delta fetches' (double fetching).

* [ **Tenable.io**](/docs/tenableio) - Added an option to prevent the adapter from duplicating plugins.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Google Workspace - Delete / Wipe Cloud Device**](/docs/google-mdm-delete-wipe-device) - Removes and wipes devices from Google.
* [**Azure DevOps -  Update Task**](/docs/update-azure-devops-task) - Changes the status of a DevOps work item to a status defined by a user.
* [**SysAid - Update Ticket**](/docs/sysaid-update-ticket) - Updates SysAid tickets.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Axonius - Export Assets to Instance**](/docs/export-assets-to-external-axonius) - Added the **Export only the queried asset type** field that when selected, only assets of the asset type selected when creating the Enforcement Action are exported.

* [**Microsoft Teams - Send message**](/docs/en/send-microsoft-teams-message) - Added the option to replace message body under **Additional text in message body** section.

* **ServiceNow - Create Asset**
  * Added IRE Configuration
  * Moved mapping of Axonius fields to ServiceNow IRE fields
  * Reorganized other configuration fields

* **Zendesk - Create Custom Object per Asset** - Added the option  to create a custom object key if it does not exist