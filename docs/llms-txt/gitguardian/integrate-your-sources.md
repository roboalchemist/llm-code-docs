# Source: https://docs.gitguardian.com/nhi-governance/integrate-your-sources.md

# Integrate your NHI sources

> Lists the supported NHI Governance integrations including secrets managers, CI/infrastructure sources, cloud IAM systems, and identity providers.

## Monitor your perimeter

NHI Governance supports a range of integrations that connect to your existing systems where NHIs are created, stored, or used. These integrations enable the platform to automatically inventory NHIs, capture key metadata (such as context, usage, and scope), and provide continuous visibility into their lifecycle and security posture.

## Supported integrations

NHI Governance offers native support for widely-used secrets managers and infrastructure components where NHIs typically reside or operate.

GitGuardian integrates with a set of sources across your infrastructure through **[ggscout](/ggscout-docs/home)** a lightweight, auditable application that safely collects secrets and their metadata from your configured secret managers, without exposing secret values. It hashes the data locally before securely sending it to your GitGuardian workspace.

![Scout Flow](/img/ggscout/scout-flow.png)

### Secrets Managers

GitGuardian integrates with Secrets Managers as a primary source of truth for secrets and tied NHIs.
Supported Secrets Managers:
- HashiCorp Vault
- CyberArk Secrets Manager SaaS
- CyberArk Secrets Manager Self-Hosted
- Akeyless Secrets Management Platform
- AWS Secrets Manager
- Google Cloud Secret Manager
- Azure Key Vault
- Delinea Secret Server

Learn more on [Secrets managers integrations](/ggscout-docs/integrations/secret-managers).

### CI and Infrastructure sources

GitGuardian also integrates with CI and Infrastructure sources to collect additional NHIs and provide additional insights to those already collected, such as understanding where NHIs are used and consumed.
Supported sources:
- [GitHub Actions](/ggscout-docs/integrations/github-actions)
- [GitLab CI](/ggscout-docs/integrations/gitlab-ci)
- [Kubernetes clusters](/ggscout-docs/integrations/infrastructure/kubernetes)

### Cloud IAM integrations

GitGuardian also integrates with Cloud Identity and Access Management systems to provide comprehensive context about NHI permissions and potential impact. These integrations analyze the permissions and policies associated with discovered credentials, offering deeper insight into the sensitivity and blast radius of exposed secrets.

Supported Cloud IAM systems:
- [AWS IAM](./aws-iam-integration) - Comprehensive AWS Identity and Access Management integration
- [Azure Entra ID](./azure-entra-integration) - Comprehensive Microsoft Entra ID integration

### Other identity providers

- Auth0
- Okta

### SaaS providers

GitGuardian can also integrate with popular SaaS platforms to provide visibility on NHI usage and potential exposure.

Supported providers:
- Airbyte
- Anthropic
- Datadog
- N8n
- OpenAI
- Slack
- Snowflake

## Contextualize your NHI sources

When configuring your integrations, you can manually assign an environment category to each data source (e.g., a specific vault or Kubernetes cluster) directly in the ggscout configuration file. This helps you contextualize NHIs based on their operational scopeâsuch as distinguishing between production and development identities.

Supported categories:
- ```prod``` - Production
- ```preprod``` - Pre-production
- ```staging``` - Staging
- ```testing``` - Testing
- ```dev``` - Development
