# Source: https://docs.gitguardian.com/platform/configure-alerting/issue-tracking-integrations/jira-cloud.md

# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud.md

# Integrate Jira Cloud

> Integrate Jira Cloud with GitGuardian via a Jira Cloud app to monitor issue descriptions and comments for exposed secrets.

Monitor Jira Cloud projects for exposed secrets in issue descriptions, comments, and project documentation.

## Why Monitor Jira Cloud?

Jira Cloud serves as the central repository for project management and issue tracking where teams document technical problems, share debugging information, and collaborate on solutions. During troubleshooting and issue resolution, developers frequently paste configuration details, error logs, and code snippets containing API keys, database credentials, and environment secrets directly into issue descriptions and comments.

## Capabilities

| Feature | Support | Details |
|---------|---------|---------|
| **Historical Scanning** | â (Manual Trigger) | Analyze existing projects issues and their histories |
| **Real-time Detection** | â (Supported) | Instant detection via Jira webhooks |
| **Monitored Perimeter** | â³ (Coming Soon) | All projects monitored by default |
| **Team Perimeter** | â³ (Coming Soon) | Users must be in the "All-incidents" team to access incidents |
| **Presence Check** | â (Not Supported) | Not applicable for project management content |
| **Source Visibility** | â (Not Supported) | All projects show as `private` |
| **File Attachments** | â³ (Coming Soon) | File attachments are not scanned |

**What we scan:**
- Issue descriptions and summaries
- Comments and discussion threads
- Custom fields and project documentation

:::info
**Plan requirements:** Available for GitGuardian **Business** and **Enterprise** plans. Try it for free with a 30-day trial - any detected incidents remain accessible after the trial ends. 
**Detector coverage:** To minimize false positives, [Generic High Entropy Secret](/secrets-detection/secrets-detection-engine/detectors/generics/generic_high_entropy_secret) and [Generic Password](/secrets-detection/secrets-detection-engine/detectors/generics/generic_password) are disabled. All other detectors are enabled.
:::

<!--
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zhHWlYGCEFs" title="Add GitGuardian Secrets Detection To Jira Cloud" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
--> 
## Setup your Jira Cloud integration

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **Jira Cloud admin** permissions for the sites you want to monitor

GitGuardian integrates with Jira Cloud via a **Jira Cloud app** with **read-only access** to your projects.

You can install GitGuardian on multiple Jira Cloud sites to monitor your projects.

1. Make sure you're logged in the Jira Cloud site you want to install
2. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
3. Click **Install** next to **Jira Cloud** in the **Ticketing** section
   ![Jira Cloud install](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-install.png)
4. Click **Install** on the [Jira Cloud integration](https://dashboard.gitguardian.com/settings/integrations/jira_cloud) page
5. Select the Jira Cloud site you want to add
6. Click **Accept** to grant the permissions requested by GitGuardian
   ![Jira Cloud permissions](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-permissions.png)

That's it! Our GitGuardian app is now automatically invited on all your projects. It will now start monitoring all issues of your projects for secrets.

## Integration with GitGuardian Self-Hosted

:::info
We recommend using dedicated workers for this integration. For more detailed information on scaling and configuration, please visit our [scaling](../../../self-hosting/management/infrastructure-management/scaling#configure-scaling-settings) page.
:::

If you are using a self-hosted GitGuardian instance, you must first configure a dedicated Jira Cloud App so that you own the entire data stream. This will ensure that your Jira Cloud App is created with all the appropriate rights.

### 1. Create a Jira Cloud app

1. Navigate to the [Jira Cloud integration](https://dashboard.gitguardian.com/settings/integrations/jira_cloud) page
2. Click **Configure Jira Cloud app**
   ![Jira Cloud app configure](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-configure.png)

#### As a Jira Cloud administrator

1. Click **Create Jira Cloud app** (Alternatively, if you're not a GitGuardian Manager, you can access the [Atlassian developer console](https://developer.atlassian.com/console/myapps/create-3lo-app) directly)
2. Type the name of your new Jira Cloud app: `GitGuardian`
3. Agree to Atlassian's developer terms by checking: **I agree to be bound by Atlassian's developer terms.**
4. Click **Create**
   ![Jira Cloud app create](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-create.png)
5. Go to the **Permissions** page
6. Click **Add** next to the **Jira API** line
   ![Permissions - Jira API add](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-permissions-jira-api-add.png)
7. Click **Configure** next to the **Jira API** line
8. In the **Classic scopes** tab, click **Edit Scopes** in the **Jira platform REST API** section
   ![Jira Cloud - Classic scopes edit](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-classic-scopes-edit.png)
9. Select the following **classic scopes**:
   - `read:jira-work`
   - `manage:jira-configuration`
   - `read:jira-user`
   - `write:jira-work`
   - `manage:jira-webhook`
10. Click **Save**
   ![Jira Cloud - Classic scopes](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-classic-scopes.png)
11. In the **Granular scopes** tab, click **Edit Scopes**
   ![Jira Cloud - Granular scopes edit](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-granular-scopes-edit.png)
12. Select the following **granular scopes**:
    - `read:application-role:jira`
    - `read:avatar:jira`
    - `read:project.avatar:jira`
    - `read:group:jira`
    - `read:issue:jira`
    - `read:issue-meta:jira`
    - `read:attachment:jira`
    - `read:comment:jira`
    - `read:comment.property:jira`
    - `read:field:jira`
    - `read:field.default-value:jira`
    - `read:field.option:jira`
    - `read:field-configuration:jira`
    - `read:issue.property:jira`
    - `read:issue-details:jira`
    - `read:issue-type:jira`
    - `read:issue-field-values:jira`
    - `read:issue-security-level:jira`
    - `read:issue-type-hierarchy:jira`
    - `read:issue.changelog:jira`
    - `read:issue.vote:jira`
    - `read:issue-event:jira`
    - `read:user:jira`
    - `read:project:jira`
    - `read:project-category:jira`
    - `read:project.component:jira`
    - `read:project.property:jira`
    - `read:project-role:jira`
    - `read:project-version:jira`
    - `read:project.feature:jira`
    - `read:webhook:jira`
    - `write:webhook:jira`
    - `delete:webhook:jira`
    - `read:status:jira`
    - `read:jql:jira`
    - `read:project-type:jira`
    - `read:project.email:jira`
    - `read:epic:jira-software`
13. Click **Save**
   ![Jira Cloud - Granular scopes](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-granular-scopes.png)
14. Go to the **Authorization** page
15. Click **Add** next to the **OAuth 2.0 (3LO)** line
   ![Authorization - OAuth 2.0 add](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-authorization-oauth-2.0-add.png)
16. Enter the callback URL based on your GitGuardian self-hosted instance URL:
   `https://<gitguardian.acme.com>/api/v1/jira-cloud/app/install_callback/`
17. Click **Save changes**
   ![Jira Cloud - Callback URL](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-callback-url.png)
18. Go to the **Overview** page
19. Get your App details (`App ID`) (alternatively, you can find and copy it more easily from the URL)
   ![Jira Cloud - Overview credentials](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-overview-credentials.png)
20. Go to the **Settings** page
21. Get your Authentication details (`Client ID`, `Secret`)
   ![Jira Cloud - Settings credentials](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-settings-credentials.png)

That's it! Your Jira Cloud app has been created and you can now [declare your Jira Cloud app in the GitGuardian Platform](jira-cloud#2-declare-your-jira-cloud-app-in-the-gitguardian-platform).
Alternatively, if you are not a GitGuardian Manager, you can now return the Jira Cloud app credentials to your requester in the secure way of your choice (`App ID`, `Client ID`, `Secret`).

:::info
All these permissions are defined for the creation of your Jira Cloud app. This Jira Cloud app can be used for any type of Jira Cloud integration (secret detection, issue tracking).
When installing a Jira Cloud site for a specific integration, only a subset of your Jira Cloud app's permissions will be requested. GitGuardian requires only the minimum number of permissions per integration.
:::

#### As a non Jira Cloud administrator

If you don't have the right to create a Jira Cloud app, please ask your Jira Cloud administrator to do it for you.
You can easily forward a request with this procedure:
1. Click the **Send a request to a Jira administrator** link to easily forward your request
2. They should in turn provide you with the Jira Cloud app credentials to proceed with the [rest of the configuration](jira-cloud#2-declare-your-jira-cloud-app-in-the-gitguardian-platform).

### 2. Declare your Jira Cloud app in the GitGuardian Platform

1. Paste your Jira Cloud app credentials (`App ID`, `Client ID`, `Secret`)
2. Click **Save and close**
   ![Jira Cloud app credentials](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-credentials.png)

That's it! Your Jira Cloud configuration is ready and you can now [setup your Jira Cloud integration](#setup-your-jira-cloud-integration).

## Understanding scanning capabilities

### Historical scanning
**Uncover your secret debt:** When you first integrate this source, GitGuardian performs a comprehensive scan of your entire content history, based on your customized perimeter. This reveals secrets that may have been exposed weeks, months, or even years ago - helping you address your existing security debt.

### Real-time scanning
**Catch new exposures instantly:** Once integrated, GitGuardian continuously monitors your content through event-based detection. Any new or modified content containing secrets are detected immediately, allowing you to respond quickly to new exposures.

## Scanning your JIRA Cloud history (beta)

GitGuardian enables you and encourages you to **scan the entire history of your perimeter**. By executing historical scanning, all secrets present in your JIRA sources prior to installing GitGuardian will be detected.

Unlike Version Control Systems, historical scanning has to be manually executed from your [perimeter page](https://dashboard.gitguardian.com/workspace/perimeter), by:
- Selecting your JIRA sources
- Click scan from the top action bar

:::warning **Previous installations!**
If you previously integrated your sources for real-time scanning, you will need to uninstall and reinstall the GitGuardian app from the Settings > Sources. This step is required as the GitGuardian application requires additional access rights: 
- read:field.default-value:jira 
- read:field.option:jira

Fresh installations do not require this step.
:::

## Edit your Jira Cloud app configuration

In case you need to edit your Jira Cloud app configuration, due to an error when declaring your Jira Cloud app credentials or due to a secret rotation, you can do so as follows:
1. Click **Edit Jira Cloud app**
2. Update your Jira Cloud app credentials
3. Click **Save and close**
   ![Jira Cloud app configuration edit](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-app-configuration-edit.png)

## Delete your Jira Cloud app configuration

In case you need to delete your Jira Cloud app configuration, you can do so as follows:
1. Click **Edit Jira Cloud app**
2. Click **Delete configuration**
3. Confirm by clicking **Delete configuration** in the confirmation modal

:::info
Deleting your Jira Cloud app configuration will uninstall all your Jira Cloud integrations.
However, all your existing incidents detected on Jira Cloud will remain available on your dashboard.
Note that deleting the Jira Cloud app configuration will only delete the configuration, not the Jira Cloud app.
If you want to delete your Jira Cloud app, you must do so from your Jira Cloud site.
:::

## Uninstall your Jira Cloud site

To uninstall a Jira Cloud site:
1. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
2. Click **Edit** next to **Jira Cloud** in the **Ticketing** section
3. Click the bin icon next to the Jira Cloud site to uninstall
4. Confirm by clicking **Yes, uninstall** in the confirmation modal
![Jira Cloud uninstall](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-uninstall.gif)

That's it! Your Jira Cloud site is now uninstalled.

## Remove the GitGuardian app from your Jira Cloud site

Uninstalling a Jira Cloud site from the GitGuardian platform does not remove the GitGuardian app from your Jira Cloud site. This is not a mandatory step, but you can remove it manually after uninstalling your Jira Cloud site from the GitGuardian platform.

:::caution Warning
The GitGuardian app is shared with the [Jira Cloud issue tracking integration](/platform/configure-alerting/issue-tracking-integrations/jira-cloud). Removing the app from your Jira Cloud site will break any existing integration in the GitGuardian platform. Make sure your Jira Cloud site is no longer installed on the GitGuardian platform before removing the GitGuardian app manually.
:::

To remove the GitGuardian app from your Jira Cloud site:
1. Go to your Jira Cloud site
2. Select **Settings > Atlassian account settings**
   ![Jira Cloud Atlassian account settings](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-atlassian-account-settings.png)
3. Go to the **Connected apps** tab
4. Click **Remove access** next to the GitGuardian app
   ![Jira Cloud - Remove app](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-cloud/jira-cloud-remove-app.png)
5. Click **Remove** in the confirmation modal

That's it! The GitGuardian app is now removed from your Jira Cloud site.

## Privacy and compliance

### Data handling

GitGuardian processes your data solely to detect exposed secrets:
- **Read-only access:** We never require write access unless scoped to creating webhooks to receive and process real-time events
- **Minimal data retention:** We store only data and metadata necessary for incident management
- **Encryption:** All data in transit and at rest is encrypted
- **Compliance:** We follow the same data protection standards as our other integrations

### Regional considerations

GitGuardian hosts its services in two AWS regions: eu-central-1 (Frankfurt) and us-west-2 (Oregon). Ensure your GitGuardian deployment region aligns with your data residency requirements. Contact support if you need guidance on compliance with local regulations.

### User notification
Country-specific laws and regulations may require you to inform your Jira Cloud users that your projects are being scanned for secrets. Here is a suggestion for a message you may want to use:
> As part of our internal information security process, the company scans the Jira Cloud projects for potential secrets leaks using [GitGuardian](https://www.gitguardian.com/monitor-internal-repositories-for-secrets). All data collected will be processed for the purpose of detecting potential leaks. To find out more about how we manage your personal data and to exercise your rights, please refer to our employee/partner privacy notice.
> 
> *Please note that only projects relating to the company's activity and business may be monitored and that users shall refrain from sharing personal or sensitive data not relevant to the project's purpose.*
