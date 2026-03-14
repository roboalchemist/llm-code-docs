# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/documentation-integrations/confluence-data-center.md

# Integrate Confluence Data Center

> Integrate Confluence Data Center with GitGuardian to scan pages, blog posts, and comments for exposed secrets.

Monitor Confluence Data Center spaces for exposed secrets in pages, documentation, and collaborative content.

## Why Monitor Confluence Data Center?

Confluence Data Center houses your organization's most critical technical documentation and knowledge base content in a self-hosted environment. Enterprise teams regularly embed production credentials, internal API keys, and infrastructure secrets in technical documentation, deployment guides, and troubleshooting pages, creating persistent security vulnerabilities within your most trusted knowledge repositories.

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

## Setup your Confluence Data Center integration

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **Confluence Data Center administrator** permissions to create Personal Access Tokens
- **confluence-administrators** group membership to access all pages and spaces
- **Network connectivity** between GitGuardian and your self-hosted services. Check out [**GitGuardian Bridge**](/platform/deployment-model/ggbridge#supported-integrations) to enable secure connections between GitGuardian SaaS and your self-hosted services in private networks.

GitGuardian integrates with Confluence Data Center via an **administrator Personal Access Token** with **read-only access** to your spaces.

You can install GitGuardian on multiple Confluence Data Center sites to monitor your spaces.

1. Make sure you're logged as an administrator in the Confluence Data Center site you want to install
2. Go to the **Settings** page
   ![Confluence Data Center settings](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-data-center/confluence-data-center-settings.png)
3. Go to the **Personal Access Tokens** section and click **Create token** to create a new PAT
   ![Confluence Data Center PAT](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-data-center/confluence-data-center-pat.png)
4. Provide a **Token Name**, an optional **Expiry date** and click **Create**
   ![Confluence Data Center PAT form](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-data-center/confluence-data-center-pat-form.png)
5. Copy your new PAT and click **Close**
   ![Confluence Data Center PAT copy](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-data-center/confluence-data-center-pat-copy.png)
6. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
7. Click **Install** next to **Confluence Data Center** in the **Documentation** section
   ![Confluence Data Center install](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-data-center/confluence-data-center-install.png)
8. Click **Install** on the [Confluence Data Center integration](https://dashboard.gitguardian.com/settings/integrations/confluence_data_center) page
9. Paste your **Confluence Data Center site URL**, your **administrator Personal Access Token** and click **Add**
   ![Confluence Data Center integration](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-data-center/confluence-data-center-integration.png)

That's it! Your Confluence Data Center site is now installed, and GitGuardian is monitoring all pages, blogs and comments of your spaces for secrets.

:::info
Confluence allows the creation of up to 10 PATs. GitGuardian automatically renews PATs before they expire. To do this, you must have at least 2 PAT slots free. Otherwise, an error message will warn you that the integration is no longer functional.
:::

## Understanding scanning capabilities

### Historical scanning
**Uncover your secret debt:** When you first integrate this source, GitGuardian performs a comprehensive scan of your entire content history, based on your customized perimeter. This reveals secrets that may have been exposed weeks, months, or even years ago - helping you address your existing security debt.

### Incremental scanning
**Stay protected with regular monitoring:** Once integrated, GitGuardian provides ongoing protection through scheduled automated scans of your content. New and modified content is systematically monitored at regular intervals, ensuring comprehensive coverage and timely detection of any secret exposures. Your source remains under GitGuardian's protection, giving you confidence that secrets won't go unnoticed.

## Scanning your Confluence Data Center history

GitGuardian enables you and encourages you to **scan the entire history of your perimeter**. By executing historical scanning, all secrets present in your Confluence sources prior to installing GitGuardian will be detected.

Unlike Version Control Systems, historical scanning has to be manually executed from your [perimeter page](https://dashboard.gitguardian.com/workspace/perimeter), by:
- Selecting your Confluence Data Center sources
- Clicking **scan** from the top action bar

## Uninstall your Confluence Data Center site

To uninstall a Confluence Data Center site:
1. In the GitGuardian platform, navigate to the [Sources integration](https://dashboard.gitguardian.com/settings/integrations/sources#secrets-scanning) page
2. Click **Edit** next to **Confluence Data Center** in the **Documentation** section
3. Click the bin icon next to the Confluence Data Center site to uninstall
4. Confirm by clicking **Yes, uninstall** in the confirmation modal
![Confluence Data Center uninstall](/img/internal-monitoring/integrate-sources/documentation-integrations/confluence-data-center/confluence-data-center-uninstall.png)

That's it! Your Confluence Data Center site is now uninstalled.

## Additional considerations

**Occurrence metadata:** Author's email is not determined

## Privacy

### Data handling

GitGuardian processes your data solely to detect exposed secrets:
- **Read-only access:** We never require write access unless scoped to creating webhooks to receive and process real-time events
- **Minimal data retention:** We store only data and metadata necessary for incident management
- **Encryption:** All data in transit and at rest is encrypted
- **Compliance:** We follow the same data protection standards as our other integrations

### Regional considerations

GitGuardian hosts its services in two AWS regions: eu-central-1 (Frankfurt) and us-west-2 (Oregon). Ensure your GitGuardian deployment region aligns with your data residency requirements. Contact support if you need guidance on compliance with local regulations.

Country-specific laws and regulations may require you to inform your Confluence Data Center users that your spaces are being scanned for secrets. Here is a suggestion for a message you may want to use:
> As part of our internal information security process, the company scans the Confluence Data Center spaces for potential secrets leaks using [GitGuardian](https://www.gitguardian.com/monitor-internal-repositories-for-secrets). All data collected will be processed for the purpose of detecting potential leaks. To find out more about how we manage your personal data and to exercise your rights, please refer to our employee/partner privacy notice.
> *Please note that only spaces relating to the companyâs activity and business may be monitored and that users shall refrain from sharing personal or sensitive data not relevant to the spaceâs purpose.*
