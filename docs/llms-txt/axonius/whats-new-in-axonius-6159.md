# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6159.md

# What's New in Axonius 6.1.59

#### Release Date: March 23rd 2025

These Release Notes contain new features and enhancements added in version 6.1.59.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Axonius Identities

Axonius [Identities](/docs/getting-started-with-identities) transforms fragmented identity data into actionable insights – bringing core discovery, lifecycle, governance, and posture management efforts together in one place to strengthen your IAM program resilience. It equips teams with the tools to optimize identity operations, unifying data from every downstream system and application with high granularity. **Identities** enables users to gain complete visibility into their identity fabric by continuously discovering all human and machine/non-human identities across their cloud, on-prem, and hybrid environments. Axonius bi-directionally integrates with systems and applications to sync accounts, roles, policies, entitlements, permission sets, and resources – ensuring users never miss a single identity in their environment.

Identities offers:

* Streamlined Identity Lifecycle Management
* Simplified Identity Governance
* Optimized Identity Security Posture Management
* Smart Identity Hygiene
* Rules to control identity lifecycle management
* Role mining to right-size identities access
* Conduct access reviews with Campaigns
* Identify excessive access with peer group analysis

Identities provides the following:

**Role Mining**

* Role mining delves deep into the organization's access landscape, analyzing user access patterns to identify common combinations of entitlements. The [**Role Mining Simulator**](/docs/using-the-role-mining-simulator) helps visualize the distribution of entitlements assigned to roles. Customers can also use the simulator to investigate entitlement drift.

<Image align="center" alt="RoleMiningSimExample.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleMiningSimExample.png" />

**Rules Simulator**

* Use the [**Rules Simulator**](/docs/rules-simulator) to build a Query Intersection Venn diagram to compare between rules that grant access and permissions. This helps you learn about the rules in your organization and determine when multiple rules can be condensed, making your rules easier to manage.

<Image align="center" alt="RulesSimulator.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RulesSimulator(1).png" />

**Peer Group Analysis**

* Peer group analysis compares an individual's performance, behavior, or characteristics against a group of similar individuals/peers. Use the [**Peer Group Simulator**](/docs/peer-group-simulator) to visually compare the entitlements of a specific identity with those of the whole team. This helps to reveal extra or unnecessary permissions.

<Image align="center" alt="Peer Group Simulator" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PeerGroupSimulator.png" />

**Access Reviews**

* Use Axonius [**Access Reviews**](/docs/campaigns-page) to set up and carry out periodic assessments to the continued necessity of users' previously granted access to software, applications, and permissions in your organization. After initiating a campaign, you can monitor its progress, and determine whether to approve or revoke user access.

<Image align="center" alt="CampaignsPage" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CampaignsPage.png" />

**Pre-built Dashboards**

* Pre-built [Identities dashboards](/docs/identities-dashboards) provide immediate value by offering readily available insights into your identity landscape. They serve as a starting point for exploring the platform's capabilities, demonstrating the potential for data analysis and informed decision-making.

<Image align="center" alt="IdentityRiskOverviewDashboard.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IdentityRiskOverviewDashboard.png" />

**Compare Permission Chart**

* Use the  Compare Permission chart  on any dashboard. It is a small version of the Peer Group Simulator chart. Adding this to a frequently used dashboard can enhance awareness of permission drift.

<Image align="center" alt="ComparePermissionChart.png" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ComparePermissionChart.png" />

**Justifications**

* **Justifications** provide a clear and auditable record of why a user has access to specific resources or data. They support informed decision-making, risk mitigation, compliance adherence, and collaboration among stakeholders. Justifications enhance transparency and accountability in access management, ensuring that access decisions are well-documented and aligned with organizational policies.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JustificationsExample.png)

## Assets Pages

The following features were added to all assets pages:

### Asset Investigation Support for Custom Fields

Custom fields can now be tracked in [Asset Investigation](/docs/advanced-asset-investigation#asset-investigation-fields), allowing for more flexibility in how users monitor changes in their assets.

### Query Wizard Enhancements

### Tool-Tip Descriptions Added to the Query Wizard

Users can hover over any operator in the Query Wizard to view their descriptions and quickly understand the various options for creating a query.

<Image align="center" alt="image \(47\).png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image%20(47).png" />

### Adapters Displayed in Field Description

The [Field Description window](/docs/field-descriptions) in the Query Wizard now shows the adapters that provide data for each field.

<Image align="center" alt="image \(48\).png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image%20(48).png" />

## Vulnerability Management Module New Features and Enhancements

The following new features and enhancements were added to the Vulnerability Management Module:

### EPSS Field Name Change

When enriching software vulnerabilities with details from EPSS DB, the Creation Date field is now renamed as Last Calculation Date.

## SaaS Applications New Features and Enhancements

### New User Extension Asset Types for SaaS Applications

The following new User Extension Asset Types were added for SaaS Applications. They can help users manage their application integrations more effectively. These new asset types provide users with a more granular and organized view of how applications are connected and accessed within their SaaS environments:

* **[Admin Managed Extensions](/docs/admin-managed-extensions)** - Integrations configured by administrators, including SSO, Bookmark, IDP, and Admin Consent types.
* **[User Initiated Extensions](/docs/user-initiated-extensions)** - Integrations initiated by users, specifically those using User Consent, where users grant permissions for their own account and data.
* **[Application Keys](/docs/application-keys)** - API keys used for programmatic or machine-level access to applications. These keys are typically generated by administrators and used for automation or integration purposes.
* **[Application Add-Ons](/docs/application-add-ons)** - Extensions or plugins installed by users within another application to enhance its functionality. These add-ons are typically user-specific and managed within the context of the main application.

### New Automatic Account Creation Logic

Account assets are now automatically created for all [administrator-managed extensions](/docs/admin-managed-extensions) in Axonius except for 'Admin consent' extensions. These extensions include SSO, IDP, and Bookmark extensions.

### Improved Behavior for 'User Count' Extensions Field

The 'User Count' field in [Application Extensions](/docs/application-extensions#counter-fields) now shows the number of users associated with an extension. Clicking the number opens the Users page filtered for that extension.
The 'User Extension Count' field shows the number of extensions that are associated with specific users.

## System Settings New Features and Enhancements

The following updates were made to various System Settings:

### SSL Cipher Field Added to LDAP Settings

In the **LDAP & SAML** settings page (under **Settings** `>` **Access Management**), an "SSL cipher" optional field was added. Users can provide an SSL cipher to use for the TLS object of the connection.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Cisco Secure Access**](/docs/cisco-secure-access)
  * Cisco Secure Access is a tool that provides secure access to your network and devices. It allows you to manage and control access to your network and devices, ensuring that only authorized users can access them. (Fetches: Devices, Users)
* [**Freshservice Fetch Tickets**](/docs/freshservice-fetch-tickets)
  * Freshservice is a cloud-based IT help desk and service management solution that enables organizations to simplify their IT operations. (Fetches: Tickets)
* [**SecuriThings**](/docs/securithings)
  * SecuriThings is a platform that enables organizations to proactively manage, automate, and secure their entire physical security infrastructure. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**1Password**](/docs/one-password)
  * This adapter now fetches application resources as assets.
  * Added the option to fetch vault items.
* [**BIND**](/docs/bind-dns-adapter) - Added the capability to upload remote files.
* [**Ceridian Dayforce**](/docs/ceridian-dayforce) - This adapter now fetches managed identities as assets.
* [**Checkmarx One**](/docs/checkmarx-one)
  * Authentication Method and Tenant Name were added to connection parameters.
  * A dropdown based on user's region was added to the Host Name or IP Address connection parameter.
* [**CSV**](/docs/csv) - Added the option to remove the CSV prefix from dynamic fields.
* [**Fortinet FortiGate**](/docs/fortinet-fortigate) - Added the option to use the fetch time instead of the last\_checked value for the “Last Seen” field on FortiManager devices.
* **[Github](/docs/github#general1)** - Added the following advanced settings:
  * Enable fetching of default branches.
  * Enrich the default branches with protection rules
* [**Ivanti Neurons**](/docs/ivanti-neurons) - RapidAPI Key was removed from connection parameters.
* [**Ivanti Security Controls**](/docs/ivanti-security-controls) - Added the option to fetch CVEs related to the machine security patches.
* [**ManageEngine ServiceDesk Plus**](/docs/manageengine-service-desk-plus) - Added the option to not enrich devices with workstation data.
* **[Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad#general)** - Added the option to filter which applications are included in the fetch by their preferred SSO mode.
* [**N-able**](/docs/n-able)
  * JWT Token was added to connection parameters.
  * Added the option to fetch device custom properties.
* [**Okta**](/docs/okta#permissions) - The adapter can now fetch many of the Application Settings with just an API token/OAuth credentials.
* [**Oracle Cloud**](/docs/oracle-cloud) - This adapter now fetches Firewalls and Load Balancers as assets.
* [**Orca Cloud Visibility Platform**](/docs/orca-cloud-visibility-platform) - Added the option to avoid keeping asset data from custom fetch rules on the device.
* **[Sailpoint IdentityIQ](/docs/sailpoint-iq#advanced-settings)** - Added the capability for customers to specify a comma separated list of which fields to fetch.
* [**Snowflake Data Warehouse**](/docs/snowflake) - Added the option to parse additional device columns.
* [**SQL Server**](/docs/sql-server)
  * SQL Query was added to connection parameters.
  * "Fetch only databases" was added to connection parameters.
* [**watchTowr**](/docs/watchtowr)
  * Added the capability to specify the number of days back to fetch Cloud Storage.

  * Added the option to not fetch devices of the subtype 'ip\_address' from the IP Addresses endpoint.

  * Added the option to not fetch devices of the subtype 'domain' from the Domains endpoint.

  * Added the option to not fetch devices of the subtype 'subdomain' from the Subdomains endpoint.

  * Added the option to fetch ObjectStorage from the Cloud Storage endpoint.

  * Added the option to fetch Containers from the Containers endpoint.

  * Added the option to fetch ApplicationResources from the Repositories endpoint.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Make LeanIX Factsheets**](/docs/make-leanix-factsheets) - Takes data from the device's Instaled Software aggretated field and creates a factsheet in LeanIX based on that data.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Rapid7 InsightVM - Add Assets to Scan**](/docs/rapid7-insightvm-add-assets-to-scan) - Added an optional Engine IDs field, to provide the engines used in the scan.
* [**SNIPE-IT - Create Asset**](https://docs.axonius.com/axonius-help-docs/docs/create-snipeit-asset) - Added the ability to use Additional Fields.