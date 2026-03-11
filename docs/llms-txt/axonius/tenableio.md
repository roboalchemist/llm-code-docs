# Source: https://docs.axonius.com/docs/tenableio.md

# Tenable Vulnerability Management

Tenable Vulnerability Management automatically discovers and assesses a customer's environment for vulnerabilities, misconfigurations, and other cybersecurity issues.

<Callout icon="📘" theme="info">
  Note

  This adapter was previously named **Tenable.io**.
</Callout>

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices, Users, Software, Groups, SaaS Applications, Containers, Network Services, Aggregated Security Findings (default: last seen in the last 30 days)

## About Tenable Vulnerability Management

Tenable provides tooling for Vulnerability Assessment, Management, and ultimately Risk-based Vulnerability management. Tenable Vulnerability Management is the cloud platform that provides a rich capability for discovery, assessment, reporting, and prioritization of vulnerabilities across systems and services.

Nessus is a standalone scanner used as a Vulnerability Assessment scanner. Tenable.sc is the on-premise manager of Nessus scanners for Vulnerability Management across large businesses. ​

**Use cases the adapter solves**

* Collection of vulnerability elements - missing patch and configuration.
* Discovery and asset enrichment (secondary vulnerability collection).
* Discovery of unmanaged devices - this use case can partially be solved using Tenable Vulnerability Management for automation of enforcing scanning regimes. ​

**Data retrieved by Tenable Vulnerability Management**

Data collected by each adapter varies slightly between each adapter, and the collective set includes ID (agent-based), OS Type & Distribution, Interfaces / MAC / IP info, CPU, Patches, Software installations, Services & Open Ports, Vulnerabilities, and configuration validation.

Note that the Source field shown in the Axonius Installed Software table for Tenable  shows either Direct or Agent Scanning:

* *Direct* - The information about this source is updated to the Axonius fetch time from Tenable.
* *Agent Scanning* - The information is updated only according to the information fetched by the Tenable Agent, and up to date according to the time that the Tenable agent ran.

## Before You Begin

### General Permissions

* The value supplied in [**Access API Key** and **Secret API Key**](/docs/tenableio#required-parameters) must have Read access to devices.
* The API Keys are created for a user account. This user account must have Administrator user permissions.

### Resources Required per Asset/Entity Type

The following table details the API endpoints used to fetch each asset/entity type, and the permissions, roles, and advanced settings required, if relevant.

<Callout icon="📘" theme="info">
  Note

  To see the relevant API endpoints and permissions for Tenable Vulnerability Management [Enforcement Actions](/docs/tenableio#related-enforcement-actions), see details in each Enforcement Action’s dedicated page.
</Callout>

| Asset / Entity Type              | API Endpoint(s)                                                                                                                       | Required Permissions/Roles                                                                                                                                                                                                                                                      | Required Advanced Settings                                                                                |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------- |
| Authentication                   | `POST /session`, `GET /session`                                                                                                       | -                                                                                                                                                                                                                                                                               | -                                                                                                         |
| Devices                          | `POST /assets/export`                                                                                                                 | Basic \[16] user role **and** Can View access control permission; **or** Administrator \[64] user role (only)                                                                                                                                                                   | Selecting **Fetch only agent data** disables fetch from this endpoint                                     |
| Vulnerabilities                  | `POST /vulns/export`                                                                                                                  | Basic \[16] user role **and** Can View access control permission; **or** Administrator \[64] user role (only)                                                                                                                                                                   | Selecting **Do not fetch vulnerabilities** or **Fetch only agent data** disables fetch from this endpoint |
| Compliance                       | `POST /compliance/export`                                                                                                             | Basic \[16] user role **and** Can View access control permission                                                                                                                                                                                                                | **Fetch compliance - will be fetched in background**                                                      |
| Users                            | `GET /users`                                                                                                                          | Basic \[16] user role (If the requesting user has the Administrator \[64] user role, Tenable Vulnerability Management fetches all attributes for an individual user’s details. Otherwise, it fetches only the following user details: UUID, ID, username, and email attributes) | -                                                                                                         |
| Groups                           | `GET /groups`                                                                                                                         | Basic \[16] user role                                                                                                                                                                                                                                                           | **Fetch groups**                                                                                          |
| Group members                    | `GET /groups/{group_id}/users`                                                                                                        | Administrator \[64] user role                                                                                                                                                                                                                                                   | **Fetch groups**                                                                                          |
| Server devices                   | `GET /server/properties`                                                                                                              | Basic \[16] user role                                                                                                                                                                                                                                                           | -                                                                                                         |
| Scan info                        | `GET /scans`                                                                                                                          | Basic \[16] user role **and** Can View \[16] scan permission                                                                                                                                                                                                                    | -                                                                                                         |
| Canceling old export jobs        | `POST /compliance/export/{export_uuid}/cancel`, `POST /assets/export/{export_uuid}/cancel`, `POST /vulns/export/{export_uuid}/cancel` | Basic \[16] user role                                                                                                                                                                                                                                                           | **Cancel old export jobs**                                                                                |
| Device exclusions                | `GET /exclusions`                                                                                                                     | Scan Manager \[40] user role                                                                                                                                                                                                                                                    | **Fetch scan exclusions**                                                                                 |
| Agents                           | `GET /scanners/null/agents`                                                                                                           | Scan Manager \[40] user role                                                                                                                                                                                                                                                    | **Fetch agent data** or **Merge agents and assets in the same tab**                                       |
| Network Services                 | `GET /networks`                                                                                                                       | Scan Manager \[40] user role                                                                                                                                                                                                                                                    | **Fetch scanners**; Also, selecting **Fetch only agent data** disables fetch from this endpoint           |
| Device network details           | `GET /scanners`                                                                                                                       | Administrator \[64] user role                                                                                                                                                                                                                                                   | **Fetch network details**                                                                                 |
| Vulnerability accept rules       | `GET /private/recast`                                                                                                                 | -                                                                                                                                                                                                                                                                               | **Fetch Accept rules**                                                                                    |
| Web applications                 | `POST /api/v3/assets/webapp/search`                                                                                                   | -                                                                                                                                                                                                                                                                               | **Fetch web applications**                                                                                |
| Web applications vulnerabilities | `POST /api/v3/findings/vulnerabilities/webapp/search` or `POST /was/v2/vulnerabilities/by-plugins/search`                             | -                                                                                                                                                                                                                                                                               | **Fetch web applications or Use V2 API for fetching web application vulnerabilities**                     |

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Tenable Vulnerability Management Domain**  - The hostname of the Tenable Vulnerability Management server. When fetching assets and vulnerabilities, a different hard-coded domain is used (currently [https://cloud.tenable.com](https://cloud.tenable.com)).
2. **Access API Key** and **Secret API Key** - An API Key associated with a user account that has the [Required Permissions](/docs/tenableio#general-permissions) to fetch assets. To generate an API key in the Tenable Vulnerability Management console, see [Generate Another User's API Keys](https://docs.tenable.com/vulnerability-management/Content/Settings/access-control/GenerateUserAPIKey.htm).

<Callout icon="📘" theme="info">
  Note

  To connect the adapter successfully, before you generate your API Key/Secret, you must disable **Username/Password Authentication** in the Tenable Vulnerability Management console.
</Callout>

![TVM\_parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-7KGIO16U.png)

### Optional Parameters

1. **Tenable Vulnerability Management Tags Include list** *(optional, case sensitive)* - Specify a comma-separated list of tag keys in Tenable Vulnerability Management.
   * If supplied, this adapter will only fetch devices from Tenable Vulnerability Management with any of the tag keys provided in this list.
   * If not supplied, this adapter will fetch all devices from Tenable Vulnerability Management.
2. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Tenable Vulnerability Management Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Tenable Vulnerability Management Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

For the full list of advanced settings for this adapter, see [Tenable Vulnerability Management - Advanced Settings](/docs/tenable-vulnerability-management-advanced-settings).

### Related Enforcement Actions

[Tenable Vulnerability Management - Add Agent to Agent Group](/docs/add-tenableio-agent-to-group)

[Tenable Vulnerability Management - Add IP Addresses to Scan](/docs/add-ips-to-tenableio-scan)

[Tenable Vulnerability Management - Add IP Addresses to Target Group](/docs/add-ips-to-tenableio-target-group)

[Tenable Vulnerability Management - Add or Remove Tags to/from Assets](/docs/tag-tenableio-assets)

[Tenable Vulnerability Management - Create Assets](/docs/create-tenableio-asset)

[Tenable Vulnerability Management - Launch WAS Scan](/docs/tenable-io-launch-was-scan)

[Tenable Vulnerability Management - Overwrite ACR](/docs/tenable-io-overwrite-acr)

[Tenable Vulnerability Management - Create User ](/docs/tenable-io-create-user)

[Tenable Vulnerability Management - Assign Role to User](/docs/tenable-io-change-user-role)

[Tenable Vulnerability Management - Assign Group to User](/docs/tenable-io-assign-group-to-user)

[Tenable Vulnerability Management - Unlink Tenable Agents](/docs/unlink-tenable-agents)

[Tenable Vulnerability Management - Delete Account](/docs/delete-tenable-io-account)

[Tenable Vulnerability Management - Restart Agent](https://docs.axonius.com/axonius-help-docs/docs/tenable-io-restart-agent)

[Tenable Vulnerability Management - Update Account Status](/docs/tenable-io-update-account-status)

[Tenable Vulnerability Management - Delete Asset](/docs/tenable-io-delete-asset)

[Tenable Vulnerability Management - Suspend User](/docs/suspend-tenableio-user)