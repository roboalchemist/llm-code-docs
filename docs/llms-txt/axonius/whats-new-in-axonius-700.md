# Source: https://docs.axonius.com/docs/whats-new-in-axonius-700.md

# What's New in Axonius Asset Cloud 7.0

#### Release Date: July 13th 2025

These Release Notes contain new features and enhancements added in version 7.0

Axonius Version 7.0 introduces major new features:

* [Workflows](/docs/whats-new-in-axonius-700#workflows) are now part of the Enforcement Center
* [Case Sets](/docs/whats-new-in-axonius-700#case-sets)
* [New Axonius Experience](/docs/whats-new-in-axonius-700#new-axonius-experience)
* [API V2](/docs/whats-new-in-axonius-700#axonius-api-v2)

In addition, as with every Axonius Release, this version contains additional new product and platform features, new and updated adapters, and new and updated enforcement actions.

## Ongoing Updates

Check out ongoing updates to Version 7.0:

* [What's New in Axonius Asset Cloud 7.0.13](https://docs.axonius.com/changelog/release-notes-7013#/)
* [What's New in Axonius Asset Cloud 7.0.12](https://docs.axonius.com/changelog/release-notes-7012#/)
* [What's New in Axonius Asset Cloud 7.0.11](/docs/whats-new-in-axonius-7011)
* [What's New in Axonius Asset Cloud 7.0.10](/docs/whats-new-in-axonius-7010)
* [What's New in Axonius Asset Cloud 7.0.9](/docs/whats-new-in-axonius-709)
* [What's New in Axonius Asset Cloud 7.0.8](/docs/whats-new-in-axonius-708)
* [What's New in Axonius Asset Cloud 7.0.7](/docs/whats-new-in-axonius-707)
* [What's New in Axonius Asset Cloud 7.0.6](/docs/whats-new-in-axonius-706)
* [What's New in Axonius Asset Cloud 7.0.5](/docs/whats-new-in-axonius-705)
* [What's New in Axonius Asset Cloud 7.0.4](/docs/whats-new-in-axonius-704)
* [What's New in Axonius Asset Cloud 7.0.3](/docs/whats-new-in-axonius-703)
* [What's New in Axonius Asset Cloud 7.0.2](/docs/whats-new-in-axonius-702)
* [What's New in Axonius Asset Cloud 7.0.1](/docs/whats-new-in-axonius-701)

## Workflows

[Axonius Workflows](/docs/workflows-overview) is the continuous orchestration engine of the Axonius Asset Cloud. It is a visual automation engine built across the Axonius platform, adding value to every Axonius product. Workflows allows teams to orchestrate Security, IT, and Identity processes using logic-based flows triggered by real-time asset data, adapter events, external systems, and actions.
Workflows supports a wide range of use cases, from access lifecycle management and patch mobilization to compliance enforcement and alert triage – all in one place.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WorkflowForRN.png)

### How it Works

Workflows is a visual no-code builder for users to design multi-step logic flows that trigger based on events or actions. Users can apply conditions, loops, and variable handling to orchestrate the right actions, and then determine how and when to execute those actions.

### Trigger Mechanisms

* Query-based - Axonius saved or new queries.
* Adapter events - For example,[Workday New Termination](/docs/workday-new-termination),[Zendesk Ticket Created](/docs/zendesk-ticket-created).
* Scheduled actions - Discovery or time-based.
* External webhook events - For example,[Panther SIEM alert](/docs/panther-siem-alert).
* On-demand actions - Manual trigger.

### Logical Components

* Conditional branches - if, else if, else.
* Looping structures - Repeat for each (with *while* and *group by* on roadmap).
* Dynamic variables & memory bank - To store and pass data between steps.
* Time-based delays.
* Wait for Event - Allows the workflow to pause and wait for a specific response (e.g., from Slack or Teams), enabling "human-in-the-loop" approvals or declines for the next action. This is crucial for user trust and controlled automation.

### Action Nodes

* 500+ Enforcement Center actions.
* Create/update/delete tickets.
* Run remote commands or remediation tasks.
* Modify users, groups, assignments.
* Tag assets, assign owners.
* Send Slack, Teams, or email notifications.
* And more…

### Controls

* Execution history with per-step visibility

* Notifications and status outputs

* Data exports

### How Workflows Help You

Workflows is a foundational pillar in Axonius’ shift from visibility to actionability, expanding the capabilities of the Enforcement Center by unlocking more complex, distributed automation use cases that previously required external tools or manual effort.
Workflows gives users continuous, universal orchestration capabilities built directly into the Axonius platform, powered by the Adapter Network, and grounded in real-time asset intelligence.

### Common Use Cases

* **Automated Patch Orchestration** - Workflows automates the full patch lifecycle by connecting asset, vulnerability, ticketing, and software tools. It triggers remediation based on severity, updates tickets, validates fixes, and tracks compliance, reducing delays and minimizing exposure.

* **Alert Enrichment & Automated Triage** - Workflows pulls context from HR, identity, endpoint, and CMDB systems to enrich alerts in real time. This enables faster, more accurate triage, cutting false positives and analyst fatigue.

* **Identity Lifecycle Automation (in Identities)** - Workflows coordinates access provisioning and revocation across HR, ITSM, and IAM during joiner, mover, and leaver events. It enforces policy-aligned access automatically, boosting compliance and reducing risk from overprovisioning.

* **Asset Compliance Flows** - Workflows monitors asset posture and triggers remediation when systems drift out of compliance. From missing EDR to OS version gaps, it opens tickets, notifies owners, and initiates fixes, ensuring continuous policy enforcement.

## Case Sets

[Case Sets](/docs/case-sets-overview) is an enhancement to [Case Management](/docs/case-management-overview) that can link internal Axonius Cases to external tickets in systems like ServiceNow and Jira, closing the loop between issue detection, remediation tracking, and reporting. It allows users to create, track, and update both internal and external tickets as a unified object, ensuring coordination between Axonius users and downstream stakeholders who operate outside the platform.

<Image alt="CaseSets.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CaseSets.png" />

### How it Works

With Case Sets, users can:

* Create a one-time or recurring Case from a query.
* Schedule recurring Cases that act as automated policy adherence baselines.
* Link a new external ticket (i.e., Jira, ServiceNow) to the Case at creation time or retroactively.
* Automatically sync key fields such as ticket status and owner.

The Case Set wizard walks the user through:

* Selecting trigger logic (i.e., when X assets match a query).
* Defining Case metadata (title, priority, due date, assignee).
* Mapping and linking to external tickets.
* Setting automation behaviors (i.e., update status if resolved externally).
* Setting up follow-up actions to occur after Case and ticket creation.
* Setting additional conditions for triggering the Case Set.

This allows bidirectional status visibility between platforms, ensuring Axonius reflects the current state of remediation, even when work happens outside the platform.

### How This Helps You

Case Sets:

* Unifies internal and external remediation efforts, ensuring Axonius has complete visibility, even when action occurs elsewhere.
* Syncs status, ownership, and progress between platforms.
* Supports cross-functional coordination, especially for teams without direct Axonius access (i.e., finance, HR, legal).

### Common Use Cases

* **Vulnerability Remediation** - Create recurring Cases for critical CVEs, link them to Jira tickets for patching, and automatically close Cases when tickets are resolved and assets are remediated.

* **Privileged Access Cleanup** - Identify overprovisioned or dormant privileged accounts and coordinate cleanup efforts across security and IT operations teams.

* **Asset Hygiene & Compliance** - Generate Cases for noncompliant assets (e.g., those without EDR installed), link them to external queues, and ensure issues are addressed and auditable.

## New Axonius Experience

We’re excited to introduce a fresh new look for the Axonius platform with the launch of our redesigned platform frame. The updated design delivers a clean, elegant visual experience that reflects our brand identity, offering a modern and streamlined interface that enhances both aesthetics and usability.

**Refreshed Look and Feel** - Experience a more streamlined interface with a clean top header and left main navigation.
**Enhanced Left Main Navigation** - The icons in the left navigation for each module were updated and the module name is displayed directly beneath the icon.
**Improved Secondary Navigation** - The newly restructured secondary navigation helps users orient themselves more effectively within the platform.\
**Enhanced Drawers** - Drawers were redesigned and action buttons were made more prominents. In various system drawers, the position of some buttons was rearranged.
**Clearer User Identification** - The user avatar now prominently displays the user's first name first, making it quicker and easier to identify the account you are currently working with.
**Explanatory Descriptions** - Descriptions have been added to every page in the system to provide better context for each page's purpose.

## Axonius API v2

Axonius API v2 is now generally available for all users.
API v2 is designed to enhance your REST API experience. This new version features a more intuitive interface with cleaner and more intuitive endpoints and simplified parameter names.

### Key Features of API v2:

**Streamlined Endpoints** - This release includes over 40 endpoints, each focused on the most vital parameters needed to achieve your goals. More endpoints will be added over time.
**Standardized and Developer-Friendly** - The new API adheres to industry standards, making it easier to use and developer-friendly, which in turn speeds up development for Axonius developers.
**Comprehensive Documentation** - Our detailed and cohesive documentation helps users quickly understand which endpoints to use and how to write the necessary code to achieve their objectives.
**Clear Error Messages** - Clear and simple error messages, making it easier to understand and resolve issues.

### Access API v2

To start using API v2, open a [Zendesk ticket](http://support.axonius.com) and select the API v2 option to request access to the documentation.

**API v2 Access for Axonius Federal Users**
Open a ticket via the Federal Support Portal or email your request to [Support@AxoniusFed.com](mailto:Support@AxoniusFed.com) with the subject "Access to API v2 documentation".

## Exposures New Features and Enhancements

The following new features and enhancements were added to Exposures:

### Importing Device Fields to the Vulnerability Instances Table

From the **System Data** Settings page, users can now configure up to 10 fields that will be parsed from the Devices table to the Vulnerability Instances table. This allows users to access additional device data previously not accessible from the **Vulnerability Instances** page, which maintains data consistency and integrity between both modules, and improves overall vulnerability management and streamlining workflows. The imported fields are also accessible from the **All Fields** section of each Vulnerability Instance's Asset Profile page.

<Image align="center" alt="VIDataSettings" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-VPELC3KY.png" />

Note that only Preferred or Custom Device fields are available for import.

### Asset Tags Available in the Vulnerability Instances Table

Users can now add the **Associated Asset Tags** field to the **Vulnerability Instances** Table, and see the tags assigned to each asset type.

## Axonius Platform New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

Timeline charts now display partial data during the calculation process, starting with the most recent data.
Data is calculated in batches—each batch may include one or several days—and added to the chart incrementally as it's processed.
This process occurs when creating a new chart, editing an existing chart, manually refreshing a chart or dashboard, or applying filters in the dashboard space.
A visual indicator shows that data is still loading.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image%20\(16\).png)

### Assets New Features and Enhancements

### New Assets

Cases and Alerts/Findings are now shown as Axonius  **Assets**. They can now be used in the system like any other asset in Charts, Enforcement actions, other queries, and more.

* [**Cases**](/docs/cases-1) - Located under the **Tickets** menu item.
* [**Alerts/Findings**](/docs/findings-alerts) - Located under the **Alerts & Incidents** menu item.

### Copy to Clipboard

Users can now copy a value from the asset table so it can easily be pasted into the Query Wizard or anywhere else. Note that fields that contain only images (without text) do not support copying.

### Query Wizard Enhancements

### Including/Excluding Values From Assets to the Query Wizard

Users can now include or exclude a specific value from the asset table directly to the Query Wizard. Users can select a value on an Asset table to open a menu. They can then click **Include in Query** or **Exclude from Query**  (except **Adapter Connections**)  to automatically add that value to the Query Wizard and run the query.

<Image alt="Include_Exclude Query.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Include_Exclude%20Query.png" />

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**ColorTokens XShield**](/docs/colortokens-xshield-v3)
  * ColorTokens XShield is a cybersecurity platform that offers zero trust security and micro-segmentation solutions. (Fetches: Devices, Vulnerabilities, SaaS Applications)
* [**Hunters**](/docs/hunters-security)
  * Hunters is a security platform that offers threat detection and response capabilities. (Fetches: Alerts/Incidents)
* [**Oracle Identity Cloud Service (IDCS)**](/docs/oracle-idcs)
  * Oracle IDCS is an identity and access management service that provides user provisioning, SSO, and authentication across hybrid IT environments. (Fetches: Users, Roles, Groups, Permissions)

### Adapter Updates

The following adapters were updated:

* [**BigID**](/docs/bigid) - Added the option to fetch datasources classifiers count.

* [**Checkmarx One**](/docs/checkmarx-one)
  * Added the option to download a Vulnerability Status Report from the API.
  * Added the option to filter fetched scans by status.
  * Added the option to filter fetched scans by date.

* [**Cherwell IT Service Management**](/docs/cherwell) - Added to the Advanced Configuration the option to extract the device name and hostname from the friendly name.

* [**Cynerio**](/docs/cynerio)
  * Added the capability to fetch risks/vulnerabilities from a specified number of days.
  * Added the capability to fetch non-NDR events from a specified number of days.
  * Added the capability to fetch NDR events from a specified number of days.
  * Added the capability to fetch incidents created in a specified number of days.

* [**Dell iDRAC**](/docs/idrac) - Added the option to fetch storage devices from Dell iDRAC.

* [**Dell OpenManage Enterprise**](/docs/dell-openmanage-enterprise) - Added the option to use the DNS name as the device hostname.

* [**IBM Guardium Data Protection**](/docs/ibm-guardium-vulnerability-assessment) - The name of the advanced setting "Create Online Report" was changed to "Fetch Devices from the online report endpoint".

* [**Oracle Identity and Access Management (IAM)**](/docs/oracle-identity-management) - Added the option to custom-parse asset fields.

* [**Symantec DLP**](/docs/symantec-dlp) - Added the option to fetch subnets as Networks.

* [**Zscaler Web Security**](/docs/zscaler-web-security) - Added the option to select the source from which to fetch SaaS Applications.

### New Enforcement Actions

With this release Axonius now supports over 500 Enforcement Actions. These actions span IT, security, identity, cloud, and collaboration systems, enabling customers to not only detect issues but also take action from a single platform.

The following Enforcement Actions were added:

* [**Microsoft Entra ID (formerly Azure AD) - Delegate User's Mailbox**](/docs/azure-ad-delegate-users-mailbox) - Adds mailbox delegations to a specified list of users.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Microsoft Defender ATP - Add or Remove Tag to/from Assets**](/docs/defender-atp-tag-assets) -  The Tag Name field is now called Tag Name**s** and supports multiple tag values, separated by comma.
* [**SQL - Send Assets to Table**](/docs/send-to-sql-table) - This action now supports export of complex objects.