# Source: https://docs.gitguardian.com/self-hosting/saas-vs-self-hosted.md

# SaaS vs Self-Hosted

> Compares GitGuardian SaaS and self-hosted deployment models, including feature availability, upgrade process, and support differences.

## Core concepts

### SaaS vs Self-Hosted

- **SaaS (Software-as-a-Service)** means the application is hosted and maintained by the vendor.
  Example: GitGuardian SaaS is hosted on GitGuardian's servers, [start for free](../platform/getting-started/account-creation)!
- **Self-Hosted or On-Premise** means the application is hosted on the customer's servers.
  Example: GitGuardian Self-Hosted is deployed on the customer's servers, [choose your installation method](./installation/choose-embedded-existing.md).

### Deployment

- **SaaS:** GitGuardian manages and controls the servers, databases, and infrastructure.
- **Self-Hosted:** GitGuardian ensures compatibility with the customerâs environment.

For more details about self-hosted, refer to the [System Requirements](./system-requirements.md) page.

### Versions and Upgrades

- **SaaS:** GitGuardian controls version releases and can quickly address issues with hotfixes or rollbacks. ([SaaS Release Notes](/releases/saas))
- **Self-Hosted:** The customer decides when to deploy new versions. GitGuardian provides support when needed and sends newsletters with each new release. ([Self-Hosted Release Notes](/releases/self-hosted))

For more details about self-hosted, refer to the [Upgrade](./management/infrastructure-management/upgrade-helm) page.

### Maintenance

- **SaaS:** GitGuardian monitors the platform and handles alerts.
- **Self-Hosted:** GitGuardian has no direct visibility and includes self-monitoring capabilities within the platform, managed by the customer.

For more details about self-hosted, refer to the [Health Checks](./troubleshoot/health-check.md) page.

### Support and Debugging

- **SaaS:** GitGuardian has full access to data and logs, enabling quick bug identification and fixes.
- **Self-Hosted:** GitGuardian relies on customer-provided data ("support bundle") to investigate issues, potentially lengthening the resolution process.

For more details about self-hosted, refer to the [Support](./troubleshoot/support.md) page.

## Feature matrix

The software running in our SaaS and Self-Hosted solutions is essentially the same. However, some features are not available in Self-Hosted versions due to significant differences in environments, requiring more effort for them to work in a self-hosted setup. The tables below highlight some of the differences between our SaaS and Self-Hosted offerings.

- â available
- â coming soon
- â not available

### Secrets scanning sources 

For more details, refer to the [Secrets Scanning Integrations Overview](../internal-monitoring/integrate-sources/overview.md) page.

| Scan source name                         | GitGuardian SaaS | GitGuardian Self-Hosted | Additional Details |
| ---------------------------------------- | ---------------- | ----------------------- | ------------------ |
| GitHub.com                               | â               | â                      |                    |
| GitHub Enterprise Server                 | â               | â                      |                    |
| GitLab.com                               | â               | â                      |                    |
| GitLab Self-Hosted Community Edition     | â               | â                      |                    |
| GitLab Self-Hosted Premium/Ultimate Plan | â               | â                      |                    |
| Bitbucket Cloud                          | â               | â (2025.2.0)           |                    |
| Bitbucket Server/Data Center             | â               | â                      |                    |
| Slack                                    | â               | â (2024.3.0)           |                    |
| Microsoft Teams                          | â               | â (2024.3.0)           |                    |
| Jira Cloud                               | â               | â (2024.4.0)           |                    |
| Jira Data Center                         | â               | â (2024.12.0)          |                    |
| ServiceNow                               | â               | â (2025.5.0)           | No historical scan |
| Confluence Cloud                         | â               | â (2024.7.0)           |                    |
| Confluence Data Center                   | â               | â (2024.11.0)          |                    |
| Azure Container Registry                 | â               | â (2025.6.0)           |                    |
| Google Artifact Registry                 | â               | â (2025.6.0)           |                    |
| JFrog Container Registry                 | â               | â (2025.6.0)           |                    |
| DockerHub                                | â               | â (2025.6.0)           |                    |
| AWS Container Registry (ECR)             | â               | â (2025.8.0)           |                    |
| Microsoft SharePoint Online              | â               | â (2025.9.0)           |                    |
| Microsoft OneDrive                       | â               | â (2025.9.0)           |                    |
| Bring Your Own Sources                   | â               | â (2025.9.0)           |                    |

### Alerting and Notifications

For more details, refer to the [Alerting and Notifications](../platform/configure-alerting/alerting-and-notifications.md) page.

| Notifier name    | GitGuardian SaaS | GitGuardian Self-Hosted |
| ---------------- | ---------------- | ----------------------- |
| Slack            | â               | â                      |
| PagerDuty        | â               | â                      |
| Splunk           | â               | â                      |
| Discord          | â               | â                      |
| Jira Cloud       | â               | â (2024.5.0)           |
| Jira Data Center | â               | â (2024.12.0)          |
| Microsoft Teams  | â               | â (2025.1.0)           |

### Honeytoken

For more details, refer to the [Honeytoken](../honeytoken/home.mdx) page.

| Feature Name                                                                  | GitGuardian SaaS | GitGuardian Self-Hosted | Additional Details                                                                                       |
| ----------------------------------------------------------------------------- | ---------------- | ----------------------- | -------------------------------------------------------------------------------------------------------- |
| Honeytoken                                                                    | â                | â                       |                                                                                                          |
| Honeytoken Deployment Jobs                                                    | â                | â (2024.4.0)            |                                                                                                          |
| [Honeytoken "Publicly Exposed" Detailed Location](../honeytoken/code-leakage) | â                | â                       | The âPublicly Exposedâ tag exists for both, but exact location on GitHub.com is available only for SaaS. |

### Other features

| Feature Name | GitGuardian SaaS | GitGuardian Self-Hosted | Additional Details |
| ------------ | ---------------- | ----------------------- | ------------------ |
| [AI Filters](../platform/collaboration-and-sharing/saved-views#ai-filters) | â | â (2025.9.0) | |
| [Remediation Tracking](../internal-monitoring/remediate/prioritize-incidents.md#2-explore-with-the-incident-page) | â | â (2025.1.0) | |
| [False Positive Remover (Machine Learning)](../secrets-detection/secrets-detection-engine/machine_learning#false-positive-remover) | â | â (2025.1.0) | |
| [Secret Enricher (Machine Learning)](../secrets-detection/secrets-detection-engine/machine_learning#secret-enricher) | â | â (2025.3.0) | |
| [Similar Incident Grouping (Machine Learning)](../internal-monitoring/remediate/investigate-incidents#ml-powered-similar-incident-grouping) | â | â | Not supported on self-hosted yet but will be added in a future release. |
| [Incident Prioritization Risk Score (Machine Learning)](../internal-monitoring/remediate/prioritize-incidents#risk-score-ml-powered-prioritization) | â | â | Not supported on self-hosted yet but will be added in a future release. |
| [Secret "Publicly Leaked" Tag](../internal-monitoring/remediate/investigate-incidents#public-exposure-information) | â | Partial | Self-hosted: Only "Source publicly visible" exposure type is available. SaaS: All three exposure types are visible; "Public incident linked" and "Outside perimeter" details require [Public Monitoring](https://www.gitguardian.com/monitor-public-github-for-secrets) subscription. |
| [Secrets Analyzer](../secrets-detection/secrets-detection-engine/secrets_analyzer) | â | â (2025.4.0) | |
| [Advanced Analytics](../platform/analytics/internal-monitoring) | â | â (2025.12.0) |  |
| [Analytics Overview](../platform/analytics/overview) | â | â | Coming soon...  |
| [Secrets Manager integration](../ggscout-docs/integrations.md) | â | â (2025.3.0) | ggscout is deployed on the GitGuardian Self-Hosted cluster |
| [IP allowlist](../platform/enterprise-administration/ip-allowlist.md) | â | â | This feature is not available on self-hosted environments, as there are alternative methods to restrict access. |
| [GG Bridge](../platform/deployment-model/ggbridge.md) | â | â | Not supported for self-hosted deployments. |
| [GitGuardian Agent](../platform/agent/overview.md) | â | â | |
