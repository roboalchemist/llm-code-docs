# Source: https://docs.axonius.com/docs/qualys-cloud-platform.md

# Qualys Cloud Platform

Qualys Cloud Platform monitors customers' global security and compliance posture using sensors.  This adapter connects to the Qualys Cloud Platform service to import information about devices and vulnerabilities.

## Asset Types Fetched

![DevicesIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![AggregatedSecurityFindingsIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Findings.svg) Aggregated Security Findings | ![UsersIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![SoftwareIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![RolesIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![SaaSApplicationsIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![TicketsIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/tickets.svg) Tickets | ![CertificatesIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Certificates.svg) Certificates

### About Qualys Cloud Platform

**Use cases the adapter solves**
Discovery and asset enrichment are secondary to the collection of vulnerability (missing patch and configuration) elements. The case of unmanaged devices can partially be solved using Qualys for automation of enforcing scanning regimes. Qualys uses the Scanning Appliance to discover assets that are unknown through any other source.

**Data retrieved by Qualys Cloud Platform adapter**
Qualys Cloud Platform brings device and service data from systems, including:

* OS, Distribution
* Interfaces
* Network details
* Last Users
* Installed Software
* Security Finding Instances
* CVE details

## Before You Begin

### Authentication Methods

You can connect this adapter using either User Name and Password **or** OpenID Token. See [Connecting the Adapter in Axonius](/docs/qualys-cloud-platform#connecting-the-adapter-in-axonius) for details.

### APIs

Axonius uses the following APIs for integration with Qualys:

* [Qualys API](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf)
* [Global IT Asset Inventory API](https://www.qualys.com/docs/qualys-global-ai-api-user-guide.pdf)

Axonius fetches data from the following Qualys endpoints:

* `api/3.0/fo/asset/ip` - List IP addresses in the user account.
* `api/5.0/fo/asset/host/` - Download a list of scanned hosts in the user’s account.
* `api/3.0/fo/report` - View a list of reports in the user’s account when Report Share feature is enabled.
* `msp/ticket_list.php` - View a list of selected tickets which the API user has permission to access.
* `msp/user_list.php`  - List user accounts in the subscription that are visible to the API user.
* `api/2.0/fo/appliance` - List scanner appliances in your account with their configurations.
* `qps/rest/3.0/search/was/webapp` - Returns a list of web applications that are in the user’s scope.
* `qps/rest/3.0/search/was/finding` - Returns a list of findings (vulnerabilities, sensitive contents, information gathered) found in web applications that are in the user’s scope.
* `api/3.0/fo/asset/group` - List asset groups in the user’s account.
* `api/3.0/fo/scan` - List vulnerability scans in the user’s account.
* `api/3.0/fo/scan/compliance` - List of compliance scans in your account.
* `api/4.0/fo/knowledge_base/vuln` - Download a list of vulnerabilities from Qualys’ KnowledgeBase.
* `api/2.0/fo/compliance/control` - View a list of compliance controls that are visible to the user.
* `api/3.0/fo/compliance/policy` - View a list of compliance policies visible to the user.
* `api/3.0/fo/compliance/posture/info/` - The Policy Compliance APIs help you gain essential insight into the compliance posture of the hosts within your account.
* `api/5.0/fo/asset/host/vm/detection/` - Download a list of hosts with the hosts' latest vulnerability data, based on the host-based scan data available in the user’s account.
* `/certview/v1/certificates` - List CertView certificates based on an input filter query and list.
* `qps/rest/2.0/search/am/tag` - Returns a list of tags that match the provided criteria.
* `/rest/2.0/count/am/asset` - Returns the number of assets that match the provided criteria.
* `/rest/2.0/search/am/asset` - Returns a list of assets matching the provided criteria.

### Required Permissions

The User Name supplied in the connection parameters must be associated with one of the following user roles and permissions:

* Manager role with full scope
  **OR**
* Reader role and AssetView Reader role with full scope
  **OR**
* Non-manager role with the following permissions:
  * Access Permission "API Access"
  * Asset Management Permission "Read Asset"
  * Requested asset in their scope

It is highly recommended to provide the user permissions and access to all objects in the subscription. To do so:

1. From the Qualys Administration utility, select **Users** `>` **User Management**.
2. Click the user account and select **Actions** `>` **Edit**.

![ActionsEdit](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Qualys1.png)

3. Navigate to **Roles and Scopes** and select the **Allow user full permissions and scope** option.

<Image align="center" alt="RolesAndScopes" width="475px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Qualys2.png" />

**To enable user access to the API:**

1. From the Qualys Administration utility, click **User** next to **Logout** -> **User Profile**. The **Edit User** page is displayed.

   ![EditUser](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(758\).png)

2. From the left sidebar, click **User Role**. Then select the **API** option to enable API Access.

   <Image align="center" alt="UserRoleAPI" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(759).png" />

3. Click **Save**.

<Callout icon="📘" theme="info">
  Notes

  * Some Qualys [advanced settings](/docs/qualys-cloud-platform-advanced-settings) might require additional permissions. Refer to the appropriate setting for information.

  * Some Qualys [Enforcement Actions](/docs/qualys-cloud-platform#related-enforcement-actions) might require additional permissions. Refer to appropriate action for information.
</Callout>

### Configuring Incremental Fetch (Optional)

Use Incremental Fetch to fetch big Qualys inventories, which can take a long time to fetch. To use Incremental Fetch you need to configure two Qualys connections.

#### Configuring Full Fetch for the First Connection (Not Delta)

1. Configure the first connection to run at a low frequency. Axonius' best practice for fetching big inventories is once a month, usually over the weekend. For more information, see [Adapter Custom Schedule](/docs/adapter-discovery-configuration#adapter-custom-cycle).
2. In the Qualys Configuration dialog, leave the **Incremental fetch from last successful** option unselected.

#### Configuring Incremental Fetch for the Second Connection

1. Configure a second Qualys connection that will perform the Incremental fetch.

2. Configure this connection to run more frequently than the first. Axonius' best practice is once a day or each discovery cycle.

3. In the Qualys Configuration dialog, select **Incremental fetch from last successful**.

#### General Configuration for Incremental Fetch

* In the adapter's [Advanced Settings](/docs/advanced-settings) section, the values of the following parameters must be greater than the frequency set for the full fetch connection:
  * Ignore devices that have not been seen by the source in the last X hours
  * Ignore users that have not been seen by the source in the last X hours
  * Delete devices and other assets that have not been returned from the source in the last X hours
  * Delete users that were not been returned from the source in the last X hours

![qualys settings incremental fetch](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/qualys%20settings%20incremental%20fetch.png)

## Connecting the Adapter in Axonius

### Required Parameters

* **Qualys Cloud Platform Domain** - The hostname of the Qualys API (for example, `qualysapi.apps.qualys.com`). For more details on how to determine your Qualys API URL, see [Identify your Qualys platform](https://www.qualys.com/platform-identification/). **This is required for all authentication methods.**

#### Required Parameters per Authentication Method

* When authenticating with a **User Name** and **Password**, provide the credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
* When authenticating with an **OpenID Token**, see [Qualys Onboarding Process](https://docs.qualys.com/en/tc/api/get_started/get_started.htm) for details on how to obtain this token.

![QualysCloudPlatformAddConnection](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/qcp.png)

### Optional Parameters

* **Qualys Tags Include list** - Specify a comma-separated list of Qualys tags.
  * If supplied, the connection for this adapter will only fetch devices tagged in Qualys with the tags provided in this list.
  * If not supplied, the connection for this adapter will fetch all devices from Qualys Cloud Platform.
* **API Rate Limit (Requests per Hour)** - Specify a rate limit for the number of requests per hour to be sent to Qualys.
  * If supplied, the number of requests initiated per hour by the connection for this adapter will be limited to the specified value. During data fetch from this connection, if the API rate limit is reached, the connection will be paused for an hour, and then will resume the data fetch.
  * If not supplied, the number of requests initiated by the connection for this adapter will not be limited.

<Callout icon="📘" theme="info">
  Note

  This setting is applicable only for the **Global IT Asset Inventory API**.
</Callout>

* **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Hostname or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Qualys Cloud Platform Domain**.

* **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Qualys Cloud Platform Domain** via the value supplied in **HTTPS Proxy**.

* **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Qualys Cloud Platform Domain** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
 

### Related Enforcement Actions

* [Qualys - Add IP Addresses to Asset Group](/docs/add-ips-to-qualys-asset-group)
* [Qualys - Add IP Addresses to User Subscription](/docs/add-ips-to-qualys-asset-group)
* [Qualys - Add Tags to Host Asset](/docs/add-tag-to-host-asset-in-qualys-cloud-platform)
* [Qualys - Remove IPs from Asset Group](/docs/qualys-remove-ips-from-asset-group)
* [Qualys - Remove Tags from Host Asset](/docs/remove-tag-from-host-asset-in-qualys-cloud-platform)
* [Qualys - Update Asset Names to Host Names](/docs/qualys-update-asset-name)
* [Qualys - Execute Script](/docs/qualys-execute-script)
* [Qualys - Launch Vulnerability Scan](/docs/launch-vulnerability-scan)
* [Qualys - Create User](/docs/qualys-create-user)
* [Qualys - Update Use](/docs/qualys-update-user)
* [Qualys - Activate User](/docs/qualys-activate-user)
* [Qualys - Suspend User](/docs/qualys-suspend-user)
* [Qualys - User Password Change](/docs/qualys-user-password-change)
* [Qualys - Assign Role to User](/docs/qualys-assign-role-to-user)
* [Qualys - Add Tags to User](/docs/qualys-add-tag-to-user)