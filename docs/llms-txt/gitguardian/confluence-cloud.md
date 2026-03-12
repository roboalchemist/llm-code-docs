# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud.md

# Integrate Confluence Cloud

> Integrate Confluence Cloud with GitGuardian via OAuth2 to scan pages, blog posts, and comments for exposed secrets.

Monitor Confluence Cloud spaces for exposed secrets in pages, documentation, and collaborative content.

## Why Monitor Confluence Cloud?

Confluence Cloud serves as the central repository for your organization's technical knowledge and documentation. Teams frequently embed API keys, database credentials, and configuration secrets in wiki pages, setup guides, and troubleshooting documentation, creating long-lasting security vulnerabilities that can be accessed by anyone with space permissions and are often overlooked during security reviews.

## Capabilities

| Feature | Support | Details |
|---------|---------|---------|
| **Historical Scanning** | â (Manual Trigger) | Analyze existing spaces and their histories |
| **Incremental Scanning** | â (Supported) | Regular scheduled scanning for new content |
| **Monitored Perimeter** | â³ (Coming Soon) | All spaces monitored by default |
| **Team Perimeter** | â³ (Coming Soon) | Users must be in the "All-incidents" team to access incidents |
| **Presence Check** | â (Not Supported) | Not applicable for Space content |
| **Source Visibility** | â (Not Supported) | All spaces show as `private` |
| **File Attachments** | â³ (Coming Soon) | File attachments are not scanned |

**What we scan:**
- Confluence pages and blog posts
- Comments and page histories
- Space documentation and wikis

:::info
**Plan requirements:** Available for GitGuardian **Business** and **Enterprise** plans. Try it for free with a 30-day trial - any detected incidents remain accessible after the trial ends. 
**Detector coverage:** To minimize false positives, [Generic High Entropy Secret](/secrets-detection/secrets-detection-engine/detectors/generics/generic_high_entropy_secret) and [Generic Password](/secrets-detection/secrets-detection-engine/detectors/generics/generic_password) are disabled. All other detectors are enabled.
:::
<!--
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/bHOSzOlPs18" title="Add GitGuardian Secrets Detection To Confluence Cloud" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
--> 

## Setup your Confluence Cloud integration

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **Confluence Cloud administrator** permissions for the sites you want to monitor

GitGuardian integrates with Confluence Cloud via an **OAuth2 app** with **read-only access** to your spaces.

You can install GitGuardian on multiple Confluence Cloud sites to monitor your spaces.

1. Make sure you're logged in the Confluence Cloud site you want to install
2. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
3. Click **Install** next to **Confluence Cloud** in the **Documentation** section
   ![Confluence Cloud install](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-install.png)
4. Click **Install** on the [Confluence Cloud integration](https://dashboard.gitguardian.com/settings/integrations/confluence_cloud) page
5. Click **Connect with Confluence Cloud** in the installation modal
   ![Confluence Cloud install - Step 1](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-install-1.png)
6. Make sure you are connected to the right Confluence Cloud site
7. Click **Accept** to grant the permissions requested by GitGuardian
   ![Confluence Cloud permissions](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-permissions.png)
That's it! Our OAuth2 app is now authorized on your Confluence Cloud site and will start monitoring pages, blogs, and comments in your spaces for secrets.

## Setup Confluence Cloud for self-hosted GitGuardian

:::info
We recommend using dedicated workers for Confluence Cloud. For more detailed information on scaling and configuration, please visit our [scaling](../../../self-hosting/management/infrastructure-management/scaling#configure-scaling-settings) page.
:::

If you are using a self-hosted GitGuardian instance, you must first configure a dedicated Confluence Cloud App so that you own the entire data stream. This will ensure that your Confluence Cloud App is created with all the appropriate rights.

### 1. Create a Confluence Cloud app

1. Navigate to the [Confluence Cloud integration](https://dashboard.gitguardian.com/settings/integrations/confluence_cloud) page
2. Click **Configure Confluence Cloud app**
   ![Confluence Cloud app configure](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-configure.png)

#### As a Confluence Cloud administrator

1. Click **Create Confluence Cloud app** (Alternatively, if you're not a GitGuardian Manager, you can access the [Atlassian developer console](https://developer.atlassian.com/console/myapps/create-3lo-app) directly)
2. Type the name of your new Confluence Cloud app: `GitGuardian`
3. Agree to Atlassian's developer terms by checking: **I agree to be bound by Atlassian's developer terms.**
4. Click **Create**
   ![Confluence Cloud app create](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-create.png)
5. Go to the **Permissions** page
6. Click **Add** next to the **Confluence API** line
   ![Permissions - Confluence API add](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-permissions-confluence-api-add.png)
7. Click **Configure** next to the **Confluence API** line
8. In the **Classic scopes** tab, click **Edit Scopes** in the **Confluence platform REST API** section
   ![Confluence Cloud - Classic scopes edit](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-classic-scopes-edit.png)
9. Select the following **classic scopes**:
   - `read:confluence-content.all`
   - `read:confluence-content.permission`
   - `read:confluence-content.summary`
   - `read:confluence-groups`
   - `read:confluence-props`
   - `read:confluence-space.summary`
   - `read:confluence-user`
   - `readonly:content.attachment:confluence`
   - `search:confluence`
10. Click **Save**
   ![Confluence Cloud - Classic scopes](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-classic-scopes.png)
11. In the **Granular scopes** tab, click **Edit Scopes**
   ![Confluence Cloud - Granular scopes edit](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-granular-scopes-edit.png)
12. Select the following **granular scopes**:
   - `read:blogpost:confluence`
   - `read:comment:confluence`
   - `read:page:confluence`
   - `read:space:confluence`
13. Click **Save**
   ![Confluence Cloud - Granular scopes](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-granular-scopes.png)
14. Go to the **Authorization** page
15. Click **Add** next to the **OAuth 2.0 (3LO)** line
   ![Authorization - OAuth 2.0 add](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-authorization-oauth-2.0-add.png)
16. Enter the callback URL based on your GitGuardian self-hosted instance URL:
   `https://<gitguardian.acme.com>/api/v1/confluence-cloud/app/install_callback/`
17. Click **Save changes**
   ![Confluence Cloud - Callback URL](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-callback-url.png)
18. Go to the **Overview** page
19. Get your App details (`App ID`) (alternatively, you can find and copy it more easily from the URL)
   ![Confluence Cloud - Overview credentials](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-overview-credentials.png)
20. Go to the **Settings** page
21. Get your Authentication details (`Client ID`, `Secret`)
   ![Confluence Cloud - Settings credentials](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-settings-credentials.png)

That's it! Your Confluence Cloud app has been created and you can now [declare your Confluence Cloud app in the GitGuardian Platform](confluence-cloud#2-declare-your-confluence-cloud-app-in-the-gitguardian-platform).
Alternatively, if you are not a GitGuardian Manager, you can now return the Confluence Cloud app credentials to your requester in the secure way of your choice (`App ID`, `Client ID`, `Secret`).

#### As a non Confluence Cloud administrator

If you don't have the right to create a Confluence Cloud app, please ask your Confluence Cloud administrator to do it for you.
You can easily forward a request with this procedure:
1. Click the **Send a request to a Confluence administrator** link to easily forward your request
2. They should in turn provide you with the Confluence Cloud app credentials to proceed with the [rest of the configuration](confluence-cloud#2-declare-your-confluence-cloud-app-in-the-gitguardian-platform).

### 2. Declare your Confluence Cloud app in the GitGuardian Platform
1. Paste your Confluence Cloud app credentials (`App ID`, `Client ID`, `Secret`)
2. Click **Save and close**
   ![Confluence Cloud app credentials](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-credentials.png)

That's it! Your Confluence Cloud configuration is ready and you can now [setup your Confluence Cloud integration](#setup-your-confluence-cloud-integration).

## Understanding scanning capabilities

### Historical scanning
**Uncover your secret debt:** When you first integrate this source, GitGuardian performs a comprehensive scan of your entire content history, based on your customized perimeter. This reveals secrets that may have been exposed weeks, months, or even years ago - helping you address your existing security debt.

### Incremental scanning
**Stay protected with regular monitoring:** Once integrated, GitGuardian provides ongoing protection through scheduled automated scans of your content. New and modified content is systematically monitored at regular intervals, ensuring comprehensive coverage and timely detection of any secret exposures. Your source remains under GitGuardian's protection, giving you confidence that secrets won't go unnoticed.

## Scanning your Confluence Cloud history (beta)

GitGuardian enables you and encourages you to **scan the entire history of your perimeter**. By executing historical scanning, all secrets present in your Confluence sources prior to installing GitGuardian will be detected.

Unlike Version Control Systems, historical scanning has to be manually executed from your [perimeter page](https://dashboard.gitguardian.com/workspace/perimeter), by:
- Selecting your Confluence sources
- Clicking scan from the top action bar

## Edit your Confluence Cloud app configuration

In case you need to edit your Confluence Cloud app configuration, due to an error when declaring your Confluence Cloud app credentials or due to a secret rotation, you can do so as follows:
1. Click **Edit Confluence Cloud app**
2. Update your Confluence Cloud app credentials
3. Click **Save and close**
   ![Confluence Cloud app configuration edit](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-app-configuration-edit.png)

## Delete your Confluence Cloud app configuration

In case you need to delete your Confluence Cloud app configuration, you can do so as follows:
1. Click **Edit Confluence Cloud app**
2. Click **Delete configuration**
3. Confirm by clicking **Delete configuration** in the confirmation modal

:::info
Deleting your Confluence Cloud app configuration will uninstall all your Confluence Cloud integrations.
However, all your existing incidents detected on Confluence Cloud will remain available on your dashboard.
Note that deleting the Confluence Cloud app configuration will only delete the configuration, not the Confluence Cloud app.
If you want to delete your Confluence Cloud app, you must do so from your Confluence Cloud site.
:::

## Uninstall your Confluence Cloud site

To uninstall a Confluence Cloud site:
1. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
2. Click **Edit** next to **Confluence Cloud** in the **Documentation** section
3. Click the bin icon next to the Confluence Cloud site to uninstall
4. Confirm by clicking **Yes, uninstall** in the confirmation modal
![Confluence Cloud uninstall](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-uninstall.png)

That's it! Your Confluence Cloud site is now uninstalled.

## Remove the GitGuardian OAuth2 app from your Confluence Cloud site

Uninstalling a Confluence Cloud site from the GitGuardian platform does not remove the GitGuardian OAuth2 app from your Confluence Cloud site. This is not a mandatory step, but you can remove it manually after uninstalling your Confluence Cloud site from the GitGuardian platform.

To remove the GitGuardian OAuth2 app from your Confluence Cloud site:
1. Go to the **[Connected apps](https://id.atlassian.com/manage-profile/apps)** page of your Confluence Cloud site
2. Click **Remove access** next to the **GitGuardian Confluence** app
3. Confirm by clicking **Remove** in the confirmation modal
   ![Confluence Cloud - Remove app](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-remove-app.png)

That's it! The GitGuardian OAuth2 app is now removed from your Confluence Cloud site.

## Installing the GitGuardian Connect App (for self-hosted version earlier than 2025.9.0)

For GitGuardian Self-Hosted versions earlier than 2025.9.0, installing a Confluence Connect App on each Confluence Cloud site is required in addition to authorizing the OAuth2 app.

1. In your Confluence Cloud site, go to **Settings** â **Manage apps**
2. Click **Settings** (top-right of the Manage apps page)
3. Check **Enable development mode** and click **Apply**
   ![Confluence Cloud Development Mode](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-development-mode.png)
4. Back on the **Manage apps** page, click **Upload app**
5. Paste your GitGuardian Connect App descriptor URL and click **Upload**:
   - For GitGuardian Self-Hosted:
   `https://<gitguardian.acme.com>/api/v1/confluence-cloud/connect-app/app-descriptor/`
   Replace `https://<gitguardian.acme.com>` with your GitGuardian Self-Hosted base URL
   ![Confluence Cloud Upload app](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-cloud/confluence-cloud-upload-app.png)
6. Verify the app appears under installed apps. The Connect App will now stream page, blog, and comment events to your GitGuardian instance.

Notes:
- Repeat these steps on every Confluence Cloud site you want to monitor.
- When you upgrade GitGuardian Self-Hosted to version 2025.9.0 or later, the Connect App is no longer required. You can safely uninstall it from Confluence (**Manage apps** â select the app â **Uninstall**).

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
Country-specific laws and regulations may require you to inform your Confluence Cloud users that your spaces are being scanned for secrets. Here is a suggestion for a message you may want to use:
> As part of our internal information security process, the company scans the Confluence Cloud spaces for potential secrets leaks using [GitGuardian](https://www.gitguardian.com/monitor-internal-repositories-for-secrets). All data collected will be processed for the purpose of detecting potential leaks. To find out more about how we manage your personal data and to exercise your rights, please refer to our employee/partner privacy notice.
> 
> *Please note that only spaces relating to the company's activity and business may be monitored and that users shall refrain from sharing personal or sensitive data not relevant to the space's purpose.*
