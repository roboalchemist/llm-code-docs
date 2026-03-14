# Source: https://docs.gitguardian.com/ggscout-docs/integrations.md

# Integrations

> Overview of all ggscout integration types including secrets managers, CI/CD systems, and infrastructure sources, with their read/write capabilities.

# ggscout Integrations

ggscout can integrate with various types of sources in your infrastructure to discover, monitor, and manage secrets. Each integration type serves different purposes and has specific capabilities.

See [Configure integrations](./configure-integrations) for general information on how integration configuration is handled.

## Integration Types

### Secrets Managers

Secrets managers are dedicated services for storing and managing sensitive information like passwords, API keys, and certificates. ggscout can both read from and write to most secrets managers, making them ideal for secret discovery and remediation workflows.

**Supported Secrets Managers:**

- **[HashiCorp Vault](./integrations/secret-managers/hashicorp-vault)** - Enterprise-grade secret management with multiple authentication methods
- **[AWS Secrets Manager](./integrations/secret-managers/aws-secrets-manager)** - AWS native secret management service
- **[Azure Key Vault](./integrations/secret-managers/azure-key-vault)** - Microsoft Azure's secret management solution
- **[Google Secret Manager](./integrations/secret-managers/google-secret-manager)** - Google Cloud's secret management service
- **[CyberArk Secrets Manager SaaS](./integrations/secret-managers/cyberark-secrets-manager-saas)** - Enterprise security platform for secrets management (cloud)
- **[CyberArk Secrets Manager Self-Hosted](./integrations/secret-managers/cyberark-secrets-manager-self-hosted)** - Enterprise security platform for secrets management (on-premises)
- **[Akeyless](./integrations/secret-managers/akeyless)** - Cloud-native secrets management platform
- **[Delinea Secret Server](./integrations/secret-managers/delinea-secret-server)** - Privileged access management and secrets vault

[**Learn more about Secrets Managers integrations â**](./integrations/secret-managers)

### CI/CD Systems

Continuous Integration and Continuous Deployment platforms often contain secrets in environment variables, pipeline configurations, and deployment scripts. ggscout can monitor these systems to identify exposed secrets.

**Supported CI/CD Systems:**

- **[GitLab CI](./integrations/gitlab-ci)** - GitLab's integrated CI/CD platform with comprehensive secret scanning

*More CI/CD integrations coming soon!*

### Infrastructure Sources

ggscout can also integrate with infrastructure components where secrets might be stored or configured.

**Supported Infrastructure Sources:**

- **[Kubernetes](./integrations/infrastructure/kubernetes)** - Native Kubernetes resources including Secrets, ConfigMaps, Deployments, and Service Accounts

*More infrastructure integrations coming soon!*

## Integration Capabilities

| Integration Type | Read Support | Write Support | Primary Use Case |
|------------------|--------------|---------------|------------------|
| **Secrets Managers** | â Yes | â Most | Secret discovery and remediation |
| **CI/CD Systems** | â Yes | â No | Secret discovery and monitoring |
| **Infrastructure** | â Yes | â No | Secret discovery and monitoring |

## Getting Started

1. **Choose your integrations**: Select the sources where your secrets might be stored
2. **Configure authentication**: Set up proper credentials and permissions
3. **Deploy ggscout**: Use our [configuration guide](./configure-ggscout) to deploy ggscout
4. **Monitor and remediate**: Use the GitGuardian platform to review discovered secrets

## Need Help?

- **Configuration guidance**: Check our [integration configuration guide](./configure-integrations)
- **Secret remediation**: Learn about [secret synchronization](./sync-secrets)
- **Best practices**: Review our [deployment recommendations](./configure-ggscout#deployment)

Each integration has specific setup requirements and capabilities. Click on the links above to access detailed configuration instructions for your chosen integrations.
