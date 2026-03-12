# Source: https://docs.gitguardian.com/platform/configure-alerting/issue-tracking-integrations/jira-data-center.md

# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/ticketing-integrations/jira-data-center.md

# Integrate Jira Data Center

> Integrate Jira Data Center with GitGuardian to monitor issue descriptions, comments, and project documentation for exposed secrets.

Monitor Jira Data Center projects for exposed secrets in issue descriptions, comments, and project documentation.

## Why Monitor Jira Data Center?

Jira Data Center houses your organization's enterprise project management and issue tracking in a self-hosted environment. Enterprise development teams regularly document technical issues, share debugging information, and collaborate on complex problems, often embedding production credentials, internal API keys, and infrastructure secrets directly in issue descriptions, comments, and custom field configurations.

## Capabilities

| Feature | Support | Details |
|---------|---------|---------|
| **Historical Scanning** | â (Manual Trigger) | Analyze existing issues and their histories |
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
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vZohw2bNzSA" title="Add GitGuardian Secrets Detection To Jira Data Center" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowFullScreen></iframe>
--> 

## Setup your Jira Data Center integration

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **Jira Data Center administrator** permissions to create Personal Access Tokens
- **Network connectivity** between GitGuardian and your self-hosted services. Check out [**GitGuardian Bridge**](/platform/deployment-model/ggbridge#supported-integrations) to enable secure connections between GitGuardian SaaS and your self-hosted services in private networks.

GitGuardian integrates with Jira Data Center via an **administrator Personal Access Token** with **read-only access** to your projects.

You can install GitGuardian on multiple Jira Data Center sites to monitor your projects.

1. Make sure you're logged as an administrator in the Jira Data Center site you want to install
2. Go to the **Profile** page
   ![Jira Data Center profile](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-data-center/jira-data-center-profile.png)
3. Go to the **Personal Access Tokens** section and click **Create token** to create a new PAT
   ![Jira Data Center PAT](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-data-center/jira-data-center-pat.png)
4. Provide a **Token Name**, an optional **Expiry date** and click **Create**
   ![Jira Data Center PAT form](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-data-center/jira-data-center-pat-form.png)
5. Copy your new PAT and click **Close**
   ![Jira Data Center PAT copy](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-data-center/jira-data-center-pat-copy.png)
6. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
7. Click **Install** next to **Jira Data Center** in the **Ticketing** section
   ![Jira Data Center install](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-data-center/jira-data-center-install.png)
8. Click **Install** on the [Jira Data Center integration](https://dashboard.gitguardian.com/settings/integrations/jira_data_center) page
9. Paste your **Jira Data Center site URL**, your **Administrator Personal Access Token** and click **Add**
   ![Jira Data Center integration](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-data-center/jira-data-center-integration.png)

That's it! Your Jira Data Center site is now installed, and GitGuardian is monitoring all issues and comments of your projects for secrets.

:::info
Jira allows the creation of up to 10 PATs. GitGuardian automatically renews PATs before they expire. To do this, you must have at least 2 PAT slots free. Otherwise, an error message will warn you that the integration is no longer functional.
:::

## Understanding scanning capabilities

### Historical scanning
**Uncover your secret debt:** When you first integrate this source, GitGuardian performs a comprehensive scan of your entire content history, based on your customized perimeter. This reveals secrets that may have been exposed weeks, months, or even years ago - helping you address your existing security debt.

### Real-time scanning
**Catch new exposures instantly:** Once integrated, GitGuardian continuously monitors your content through event-based detection. Any new or modified content containing secrets are detected immediately, allowing you to respond quickly to new exposures.

## Scanning your Jira Data Center history (beta)

GitGuardian enables you and encourages you to **scan the entire history of your perimeter**. By executing historical scanning, all secrets present in your Jira sources prior to installing GitGuardian will be detected.

Unlike Version Control Systems, historical scanning has to be manually executed from your [perimeter page](https://dashboard.gitguardian.com/workspace/perimeter), by:
- Selecting your Jira Data Center sources
- Clicking **scan** from the top action bar

## Uninstall your Jira Data Center site

To uninstall a Jira Data Center site:

1. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
2. Click **Edit** next to **Jira Data Center** in the **Ticketing** section
3. Click the bin icon next to the Jira Data Center site to uninstall
4. Confirm by clicking **Yes, uninstall** in the confirmation modal
![Jira Data Center uninstall](/img/internal-monitoring/integrate-sources/ticketing-integrations/jira-data-center/jira-data-center-uninstall.png)

That's it! Your Jira Data Center site is now uninstalled.

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
Country-specific laws and regulations may require you to inform your Jira Data Center users that your projects are being scanned for secrets. Here is a suggestion for a message you may want to use:

> As part of our internal information security process, the company scans the Jira Data Center projects for potential secrets leaks using [GitGuardian](https://www.gitguardian.com/monitor-internal-repositories-for-secrets). All data collected will be processed for the purpose of detecting potential leaks. To find out more about how we manage your personal data and to exercise your rights, please refer to our employee/partner privacy notice.
> 
> *Please note that only projects relating to the company's activity and business may be monitored and that users shall refrain from sharing personal or sensitive data not relevant to the project's purpose.*
