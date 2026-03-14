# Source: https://docs.gitguardian.com/platform/configure-alerting/issue-tracking-integrations/servicenow.md

# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/ticketing-integrations/servicenow.md

# Integrate ServiceNow

> Integrate ServiceNow with GitGuardian to monitor tickets, knowledge articles, and service management workflows for exposed secrets.

Monitor ServiceNow for exposed secrets in tickets, knowledge articles, and service management workflows.

## Why Monitor ServiceNow?

ServiceNow serves as the central IT service management platform where IT teams document incidents, manage changes, and maintain knowledge bases. During incident response and troubleshooting, IT staff frequently embed system credentials, configuration details, and service account information in tickets, change requests, and knowledge articles, creating persistent security vulnerabilities within critical IT documentation.

## Capabilities

| Feature | Support | Details |
|---------|---------|---------|
| **Historical Scanning** | â (Supported) | Analyze existing tables and records histories  |
| **Incremental Scanning** | â (Supported) | Regular scheduled scanning for new content |
| **Monitored Perimeter** | â³ (Coming Soon) | All tables and record monitored by default |
| **Team Perimeter** | â³ (Coming Soon) | Users must be in the "All-incidents" team to access incidents |
| **Presence Check** | â (Not Supported) | All occurrences considered present |
| **Source Visibility** | â (Not Supported) | All tables show as `private` |
| **File Attachments** | â (Not Supported) | File attachments are not scanned |

**What we scan:**
- Incident and service request descriptions
- Change request documentation
- Knowledge base articles and procedures
- Workflow configurations and scripts

:::info
**Plan requirements:** Available for GitGuardian **Business** and **Enterprise** plans. Try it for free with a 30-day trial - any detected incidents remain accessible after the trial ends. 
**Detector coverage:** To minimize false positives, [Generic High Entropy Secret](/secrets-detection/secrets-detection-engine/detectors/generics/generic_high_entropy_secret) and [Generic Password](/secrets-detection/secrets-detection-engine/detectors/generics/generic_password) are disabled. All other detectors are enabled.
:::

<!--
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ER27aHgtfzQ" title="Add GitGuardian Secrets Detection To ServiceNow" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
--> 

## Setup your ServiceNow integration

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **ServiceNow admin** permissions to create user accounts with API access
- **Network connectivity** between GitGuardian and your self-hosted services. Check out [**GitGuardian Bridge**](/platform/deployment-model/ggbridge#supported-integrations) to enable secure connections between GitGuardian SaaS and your self-hosted services in private networks.

GitGuardian integrates with ServiceNow via a dedicated **User** with **read-only access** to your tables.
You can install GitGuardian on multiple ServiceNow instances to monitor your tables.

### 1. Create a new user

1. Login to your ServiceNow instance
2. Go to **Organization > Users** and click **New** to create the new user required for authentication
   ![ServiceNow Create New User](/img/internal-monitoring/integrate-sources/ticketing-integrations/servicenow/servicenow-create-new-user.png)
3. Set a **User ID** (e.g.: `GitGuardian`) and click **Submit** to create it
   ![ServiceNow GitGuardian User](/img/internal-monitoring/integrate-sources/ticketing-integrations/servicenow/servicenow-gitguardian-user.png)

### 2. Give the required roles to the user

1. Click on the **User ID** (e.g.: `GitGuardian`) to edit it and add the required roles
2. Go to the **Roles** tab and click **Edit...**
   ![ServiceNow Edit User](/img/internal-monitoring/integrate-sources/ticketing-integrations/servicenow/servicenow-edit-user.png)
3. Add the following roles and click **Save**:
   - `admin`
   - `snc_read_only`
   The `admin` role will give the user access to all tables, while the `snc_read_only` role will restrict access to read-only.
   ![ServiceNow Edit User](/img/internal-monitoring/integrate-sources/ticketing-integrations/servicenow/servicenow-user-roles.png)
4. Click **Update** to validate the roles added to the user
   ![ServiceNow Validate User Edition](/img/internal-monitoring/integrate-sources/ticketing-integrations/servicenow/servicenow-validate-user-edition.png)

### 3. Set a password to the user

1. Click on the **User ID** (e.g.: `GitGuardian`) to edit it and set a password
2. Click **Set Password**
3. Click **Generate** and copy the password
4. Save by clicking **Save Password** and **Close**
5. Uncheck **Password needs reset** option and click **Update**
   ![ServiceNow Set Password User](/img/internal-monitoring/integrate-sources/ticketing-integrations/servicenow/servicenow-set-password-user.png)

### 4. Finalize the configuration in GitGuardian

1. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
2. Click **Install** next to **ServiceNow** in the **Ticketing** section
   ![ServiceNow install](/img/internal-monitoring/integrate-sources/ticketing-integrations/servicenow/servicenow-install.png)
3. Click **Install** on the [ServiceNow integration](https://dashboard.gitguardian.com/settings/integrations/servicenow_data_source) page
4. Paste your ServiceNow instance URL in the **API endpoint URL** field (e.g.: `https://acme.service-now.com/`)
5. Paste the newly created **Username** (e.g.: `GitGuardian`), its associated **Password**, and click **Add**
   ![ServiceNow integration](/img/internal-monitoring/integrate-sources/ticketing-integrations/servicenow/servicenow-integration.png)

That's it! Your ServiceNow instance is now installed, and GitGuardian is monitoring all records of your tables for secrets.

## Uninstall your ServiceNow instance

To uninstall a ServiceNow instance:
1. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
2. Click **Edit** next to **ServiceNow** in the **Ticketing** section
3. Click the bin icon next to the ServiceNow instance to uninstall
4. Confirm by clicking **Yes, uninstall** in the confirmation modal
![ServiceNow uninstall](/img/internal-monitoring/integrate-sources/ticketing-integrations/servicenow/servicenow-uninstall.png)

That's it! Your ServiceNow instance is now uninstalled.

## Additional Self-Hosted considerations

For GitGuardian Self-Hosted instances, scan frequency can be configured in the [Admin Area](../../../self-hosting/management/application-management/admin-area):
- Time interval unit: **seconds**
- Default value: **3600** (1 hour)
- Minimum value: **1800** (30 minutes)

## Privacy

Country-specific laws and regulations may require you to inform your users that your tables are being scanned for secrets. Here is a suggestion for a message you may want to use:
> As part of our internal information security process, the company scans its tables for potential secrets leaks using [GitGuardian](https://www.gitguardian.com/monitor-internal-repositories-for-secrets). All data collected will be processed for the purpose of detecting potential leaks. To find out more about how we manage your personal data and to exercise your rights, please refer to our employee/partner privacy notice.
> *Please note that only tables relating to the companyâs activity and business may be monitored and that users shall refrain from sharing personal or sensitive data not relevant to the tableâs purpose.*
