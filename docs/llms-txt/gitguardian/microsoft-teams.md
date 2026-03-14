# Source: https://docs.gitguardian.com/platform/configure-alerting/notifiers-integrations/microsoft-teams.md

# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/messaging-integrations/microsoft-teams.md

# Integrate Microsoft Teams

> Guide to integrating Microsoft Teams with GitGuardian to monitor channel messages and file attachments for exposed secrets.

Monitor Microsoft Teams workspaces for exposed secrets in channel messages, conversations, and file attachments.

## Why Monitor Microsoft Teams?

Microsoft Teams serves as the central communication hub for enterprise collaboration where employees share technical information, troubleshooting details, and project updates in real-time. During daily conversations and file sharing, team members frequently paste configuration snippets, error logs, and debugging information containing API keys, database credentials, and service account tokens directly into channels and private messages.

## Capabilities

| Feature | Support | Details |
|---------|---------|---------|
| **Historical Scanning** | â (Manual Trigger) | Analyze existing messages and chat history |
| **Incremental Scanning** | â (Supported) | Regular scheduled scanning for new content |
| **Monitored Perimeter** | â³ (Coming Soon) | All channels monitored by default |
| **Team Perimeter** | â³ (Coming Soon) | Users must be in the "All-incidents" team to access incidents |
| **Presence Check** | â (Not Supported) | All occurrences considered present |
| **Source Visibility** | â (Supported) | Private channels show as `private`, public/shared as `public` |
| **Group Chats** | â (Not Supported) | Group chats are not scanned |
| **File Attachments** | â (Beta) | File attachment scanning in beta |

**What we scan:**
- Standard, private, and shared channel messages
- Direct messages and conversations
- File attachments and shared documents
- Thread discussions and replies

:::info
**Plan requirements:** Available for GitGuardian **Business** and **Enterprise** plans. Try it for free with a 30-day trial - any detected incidents remain accessible after the trial ends. 
**Detector coverage:** To minimize false positives, [Generic High Entropy Secret](/secrets-detection/secrets-detection-engine/detectors/generics/generic_high_entropy_secret) and [Generic Password](/secrets-detection/secrets-detection-engine/detectors/generics/generic_password) are disabled. All other detectors are enabled.
:::

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **Microsoft Teams administrator** permissions for the tenants you want to monitor

GitGuardian integrates with Microsoft Teams via an **Entra ID Enterprise application** with **read-only access** to your channels.

<!--
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/B4rkhIuiH8I" title="Add GitGuardian Secrets Detection To Microsoft Teams" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
--> 
## Setup your Microsoft Teams integration

You can install GitGuardian on multiple Microsoft Teams tenants to monitor your standard, private and shared channels.

1. Make sure you're logged as administrator in the Microsoft Teams tenant you want to install
2. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
3. Click **Install** next to **Microsoft Teams** in the **Messaging** section
   ![Microsoft Teams install](/img/internal-monitoring/integrate-sources/messaging-integrations/microsoft-teams/microsoft-teams-install.png)
4. Click **Install** on the [Microsoft Teams integration](https://dashboard.gitguardian.com/settings/integrations/microsoft_teams) page
5. Select your Microsoft Teams administrator account
6. Click **Accept** to grant the permissions requested by GitGuardian
   ![Microsoft Teams permissions](/img/internal-monitoring/integrate-sources/messaging-integrations/microsoft-teams/microsoft-teams-permissions.png)

That's it! Our GitGuardian Entra app is now automatically installed on your Microsoft Teams tenant. It will now start monitoring all posts shared on your standard, private and shared channels for secrets.

## Understanding scanning capabilities

### Historical scanning
**Uncover your secret debt:** When you first integrate this source, GitGuardian performs a comprehensive scan of your entire content history, based on your customized perimeter. This reveals secrets that may have been exposed weeks, months, or even years ago - helping you address your existing security debt.

### Incremental scanning
**Stay protected with regular monitoring:** Once integrated, GitGuardian provides ongoing protection through scheduled automated scans of your content. New and modified content is systematically monitored at regular intervals, ensuring comprehensive coverage and timely detection of any secret exposures. Your source remains under GitGuardian's protection, giving you confidence that secrets won't go unnoticed.

## Setup Microsoft Teams for self-hosted GitGuardian

:::info
We recommend using dedicated workers for Microsoft Teams. For more detailed information on scaling and configuration, please visit our [scaling](../../../self-hosting/management/infrastructure-management/scaling#configure-scaling-settings) page.
:::

If you are using a self-hosted GitGuardian instance, you must first configure a dedicated Azure Entra ID Application.

### Create the Azure Entra ID Application for GitGuardian

:::info
You must be logged as a Microsoft Entra ID administrator to complete this process
:::

1. In your Microsoft Azure Tenant, browse to your Entra ID applications and create a new application, and click the "Create your own application" button

   

2. Choose a name for your application and register it to integrate with Microsoft Entra ID

   

3. Set a Redirect URI matching your GitGuardian Self-Hosted Instance:

`https://<your instance url>/api/v1/microsoft-teams/app/install_callback/`

  ![Create your own application](/img/internal-monitoring/integrate-sources/messaging-integrations/microsoft-teams/entra-id-create-application-3.png)

4. Set permissions for your application

Browse to Manage / API Permissions to set the needed permissions.Choose **Application permissions** if you are asked :

  ![Entra ID app permissions](/img/internal-monitoring/integrate-sources/file-storage-integrations/sharepoint-online/entra-id-application-permissions.png)

Your application must be allowed the following Graph API permissions:

- Application.ReadWrite.OwnedBy
- Channel.ReadBasic.All
- ChannelMessage.Read.All
- ChatMember.Read.All
- ChatMessage.Read.All
- Files.Read.All
- Group.Read.All
- Organization.Read.All
- Policy.Read.All
- Policy.ReadWrite.ApplicationConfiguration
- Team.ReadBasic.All
- TeamMember.Read.All
- User.Read

You must also "Grant admin consent" for all these permissions.

  ![Create your own application](/img/internal-monitoring/integrate-sources/messaging-integrations/microsoft-teams/entra-id-create-application-4.png)

5. Generate a Secret for your application

Browse to Manage / Certificates & secrets to create a Client Secret, create a secret and copy it while it is displayed.

:::tip
Store the Application ID and the Client Secret in a secure location like a vault or a secret manager
:::

### Reference your newly created application in GitGuardian Self-Hosted

1. Navigate to the Microsoft Teams integration page
2. Click **Configure Microsoft Teams app**
   ![Configure Microsoft Teams app](/img/internal-monitoring/integrate-sources/messaging-integrations/microsoft-teams/self-hosted-configure-app.png)

3. Set the Application ID and Secret you just created in Microsoft Azure Entra Id

### Attachment Scanning
**No blindspot:** GitGuardian scans any attachments uploaded by end-users, except files previously uploaded to SharePoint and shared through the SharePoint link.

Please consider using the **[Microsoft SharePoint Online integration](../documentation-integrations/microsoft-sharepoint-online)** to scan any file from SharePoint Online, shared through Microsoft Teams. 

### Comprehensive file support
GitGuardian integration supports a wide range of file types:

1. **Text and code files:**
- Source code (.py, .js, .java, .cpp, .cs, .rb, .go, .php, etc.)
- Configuration files (.yaml, .json, .xml, .ini, .conf, .properties, etc.)
- Documentation (.txt, .md, .rst, .log, etc.)

2. **Office documents:**
- Microsoft Office (.docx, .xlsx, .pptx, .doc, .xls, .ppt)
- OpenOffice/LibreOffice (.odt, .ods, .odp)
- Rich text formats (.rtf)
- Others (.epub)

3. **Archive and compressed files (experimental):**
- Archive formats (.zip, .7z, .rar, .tar, .gz, .tgz or .tar.gz, .bz2, .tbz2 or .tar.bz2, .xz, .txz or .tar.xz, .ar, .cpio, .pack)
- Container images (through .tar extensions)

4. **Other document formats:**
- PDF documents (.pdf)
- Email formats (.eml, .msg)
- Web files (.html, .css)

**File size considerations:** Large files are skipped to maintain optimal performance. Size thresholds are as follows: 
- 100 MB for any text file type.
- 500 MB for PDFs.
- 1 GB for any other file type listed.

## Uninstall your Microsoft Teams tenant

To uninstall a Microsoft Teams tenant:
1. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
2. Click **Edit** next to **Microsoft Teams** in the **Messaging** section
3. Click the bin icon next to the Microsoft Teams tenant to uninstall
4. Confirm by clicking **Yes, uninstall** in the confirmation modal
![Microsoft Teams uninstall](/img/internal-monitoring/integrate-sources/messaging-integrations/microsoft-teams/microsoft-teams-uninstall.png)

That's it! Your Microsoft Teams tenant is now uninstalled.

## Additional Self-Hosted considerations

For GitGuardian Self-Hosted instances, scan frequency can be configured in the [Admin Area](../../../self-hosting/management/application-management/admin-area):
- Time interval unit: **seconds**
- Default value: **21600** (6 hours)  
- Minimum value: **1800** (30 minutes)

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
Country-specific laws and regulations may require you to inform your Microsoft Teams users that your channels are being scanned for secrets. Here is a suggestion for a message you may want to use:
> As part of our internal information security process, the company scans the Microsoft Teams channels for potential secrets leaks using [GitGuardian](https://www.gitguardian.com/monitor-internal-repositories-for-secrets). All data collected will be processed for the purpose of detecting potential secret leaks. To find out more about how we manage your personal data and to exercise your rights, please refer to our employee/partner privacy notice.
> 
> *Please note that only channels relating to the company's activity and business may be monitored and that users shall refrain from sharing personal or sensitive data not relevant to the channel's purpose.*

## Managing your integration

### Monitoring health and Maintenance
If you need to modify your integration settings or troubleshoot connectivity issues, access the management interface through [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning).

### Uninstalling the integration

While our goal is to help you maintain comprehensive security coverage, you may uninstall the integration whenever necessary:

1. Navigate to [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning)
2. Click **Edit** next to the integration name
3. Click **Configure**
3. Click the delete icon next to your resource
4. Confirm the removal

**Note:** Removing the integration preserves your incident history, but stops future scanning and presence checks for the integrations that support it.
