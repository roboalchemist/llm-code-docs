# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6173.md

# What's New in Axonius Asset Cloud 6.1.73

#### Release Date: June 29th 2025

These Release Notes contain new features and enhancements added in version 6.1.73.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

### System Settings New Features and Enhancements

The following updates were made to various System settings:

#### New Enrichment Setting

On the [**Enrichment** settings page](/docs/configuring-enrichment-settings)(accessible from **System Settings `>` Enrichment**), it is now possible to enable the new **Prefix Common Enrichment field as "CE"** option to shorten Common Enrichment field prefixes to **CE:** instead of **Common Enrichment:**

### Customizing Fields for Global Search

For the **Global Search** module, users can now configure up to 10 fields to search assets by, per asset type.
Under the new **Global Search Fields** page under **Settings**, users can change the default search settings that are set by Axonius, for each asset type, by selecting up to 10 searchable fields. By editing the list of searchable fields, it becomes manually managed, so that any changes made to the list by Axonius (such as adding or removing default fields to search) will not apply.

<Image alt="GlobalSearchFields" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-4G59VSTI.png" />

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**LightMesh**](/docs/lightmesh)
  * LightMesh is a network management tool that offers comprehensive visibility and control over network infrastructure. (Fetches: Devices)
* [**Metasys**](/docs/metasys)
  * Metasys is a building management system that provides integrated control and monitoring of facility operations. (Fetches: Devices)
* [**Palo Alto Networks Strata Cloud Manager**](/docs/palo-alto-networks-strata-cloud-manager)
  * Strata Cloud Manager is a platform that offers cloud infrastructure management and optimization solutions. (Fetches: Devices)
* [**Symantec Endpoint Protection Mobile**](/docs/symantec-endpoint-protection-mobile)
  * Symantec Endpoint Protection Mobile is a security solution that offers mobile device protection and management. (Fetches: Devices, Users, Organizational Units)

### Adapter Updates

The following adapters were updated:

* [**Amazon Web Services (AWS)**](/docs/amazon-web-services-aws) - Added multiple options to filter Security Hub findings by different criteria.

* [**BitSight Security Ratings**](/docs/bitsight-security-ratings) - Added an option to fetch company security ratings.

* [**Brinqa**](/docs/brinqa) - This adapter now fetches Vulnerabilities.

* [**CSV**](/docs/csv) - This adapter now fetches Business Applications.

* [**Delinea Secret Server**](/docs/thycotic-secret-server) - Added the option to fetch devices.

* [**Egress Defend**](/docs/egress-defend) - Organization Domains list was added to connection parameters.

* [**GitHub**](/docs/github) - Added the option to fetch repository runners.

* [**HashiCorp Vault**](/docs/hashicorpvault)
  * Added the option to fetch users from the Entities endpoint and to enrich the Entities endpoint with the Certificates endpoint.
  * Added the option to fetch application resources of the subtype 'mount' from the Mounts endpoint.
  * Added the option to fetch application resources of the subtype 'certificate' from the Certificates endpoint.

* [**KnowBe4**](/docs/knowbe4) - Added the option to parse the employee number as the employee ID.

* [**McAfee ePolicy Orchestrator (ePO)**](/docs/mcafee-epolicy-orchestrator-epo) - Added the capability to set the timeout in seconds for reading data from the ePO connection.

* [**Microsoft SCOM**](/docs/scom) - Added an option to determine the table name from which the adapter will fetch devices.

* [**Opsgenie**](/docs/opsgenie) - Added the following advanced options:
  * **Fetch Teams** - Can be enabled to fetch teams as Group assets. Each group has a link to its roles and members.
  * **Fetch Teams Roles** - Enable this option to fetch the roles of each team as Role assets.

* [**Splunk**](/docs/splunk) - Added the option to perform **Device Custom Parsing** and **User Custom Parsing**. This enables users to define how to parse specific fields from the raw data fetched for Device and User assets.

* [**SQL Server**](/docs/sql-server) - Added support for SSL verified connections for the MySQL and PostgresSQL database types.

* [**TeamViewer**](/docs/teamviewer) - Added the option to fetch devices assigned to all groups.

* [**Veeam**](/docs/veeam) - Added support for API 1.2-rev0 (Veeam Backup and Replication 12).

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Ivanti Unified Endpoint Manager (Landesk) - Create or Update Asset**](/docs/landesk-create-or-update-asset) - Creates or updates an asset in Ivanti Unified Endpoint Manager (Landesk).
* [**Microsoft Entra ID (formerly Azure AD) - Enrich User with Microsoft Defender Attack data**](/docs/enrich-azure-ad-users-with-microsoft-defender-attack) - Enriches users with the Microsoft Defender Attack report data.
* [**Add MimecastV2 Group Members**](/docs/add-mimecast-v2-group-members) - Adds members to a Mimecast group.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Microsoft AD - Disable Assets**](/docs/disable-users-devices-in-ms-ad) - Added an option to re-fetch assets if the action is successful.
* [**Microsoft Entra ID (formerly Azure AD) - Assign Group to Users**](/docs/assign-azure-ad-group-to-user?highlight=assign%20group) and [**Microsoft Entra ID (formerly Azure AD) - Add or Remove Assets in Group**](/docs/add-users-or-devices-to-azure-ad-group?highlight=add%20%2F%20remove%20users) - Added support for email-enabled security groups in these two Enforcement Actions. Creating a service account with the relevant credentials is required to use this option.
* [**ServiceNow - Create Assets**](/docs/create-servicenow-computer) - ServiceNow IRE fields have been relocated to the new **IRE Configuration** tab. These fields are now automatically populated with the relevant field names.