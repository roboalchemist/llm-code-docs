# Source: https://docs.gitguardian.com/platform/deployment-model/ggbridge.md

# GitGuardian Bridge

> Describes ggbridge, a secure relay that enables GitGuardian SaaS to scan self-hosted VCS repositories without exposing them to the internet.

GitGuardian Bridge extends GitGuardian SaaS with secure access to your private infrastructure through encrypted tunnels. This approach allows you to leverage the full benefits of GitGuardian's cloud platform while maintaining secure access to your internal resources.

Built with security at its core, GitGuardian Bridge uses outbound-only connections, mutual TLS authentication, end-to-end encryption, minimal attack surface with distroless container images, and provides complete audit logging for full compliance.

:::info
GG Bridge is only available for:
- Workspaces under Enterprise plan
- US and EU SaaS customers
:::

## What is GitGuardian Bridge?

GitGuardian Bridge creates an encrypted, outbound-only tunnel from your private network to GitGuardian SaaS, allowing you to:

- **Scan private repositories** without exposing them to the internet
- **Monitor self-hosted services** while maintaining network isolation  
- **Meet compliance requirements** by keeping sensitive infrastructure private
- **Support multiple networks** with separate bridge configurations

## Cost considerations

GitGuardian Bridge has the same egress cost implications as direct GitGuardian SaaS access. Consider data volume when scanning large datasets, and deploy your bridge close to data sources to minimize network transfer costs.

## Supported integrations

GitGuardian Bridge works with:

| Service | Type |
|---------|------|
| [GitHub Enterprise Server](../../internal-monitoring/integrate-sources/vcs-integrations/github-enterprise) | Version Control |
| [GitLab Enterprise Edition](../../internal-monitoring/integrate-sources/vcs-integrations/gitlab) | Version Control |
| [Bitbucket Data Center](../../internal-monitoring/integrate-sources/vcs-integrations/bitbucket) | Version Control |
| [Azure DevOps Server](../../internal-monitoring/integrate-sources/vcs-integrations/azure-repos) | Version Control |
| [JFrog Artifactory](../../internal-monitoring/integrate-sources/container-registries-integrations/jfrog-container-registry) | Container Registry |
| [Azure Container Registry](../../internal-monitoring/integrate-sources/container-registries-integrations/azure-container-registry) | Container Registry |
| [Confluence Data Center](../../internal-monitoring/integrate-sources/documentation-integrations/confluence-data-center) | Documentation |
| [Microsoft OneDrive](../../internal-monitoring/integrate-sources/documentation-integrations/microsoft-onedrive) | Documentation |
| [Microsoft SharePoint Online](../../internal-monitoring/integrate-sources/documentation-integrations/microsoft-sharepoint-online) | Documentation |
| [Jira Data Center](../../internal-monitoring/integrate-sources/ticketing-integrations/jira-data-center) | Ticketing |
| [ServiceNow (on-premise)](../../internal-monitoring/integrate-sources/ticketing-integrations/servicenow) | Ticketing |
| [Bring Your Own Sources](../../internal-monitoring/integrate-sources/bring-your-own-sources) | Custom Sources |
| [Custom webhooks](../configure-alerting/notifiers-integrations/custom-webhook) | Notifications |
| [Splunk Enterprise](../configure-alerting/notifiers-integrations/splunk) | Notifications |
| [Custom validity endpoints](../../secrets-detection/customize-detection/validity-checks#customize-validity-checks) | Secret Validation |
| [Secrets Analyzers](../../secrets-detection/secrets-detection-engine/secrets_analyzer) | Secret Analyzers |

:::info Validity Checks Support
GitGuardian Bridge currently supports validity checks for detectors that allow you to configure custom hosts (such as GitLab instances). However, validity checks are not yet supported for detectors where GitGuardian automatically extracts the host information from the location where the secret is discovered (such as PostgreSQL connection strings).

Reach out to [support@gitguardian.com](mailto:support@gitguardian.com) if you have any questions.
:::

## How to set up GitGuardian Bridge

### Step 1: Request bridge access
Contact [support@gitguardian.com](mailto:support@gitguardian.com) to request bridge functionality for your account. Specify how many bridges you need (typically one per isolated network segment).

### Step 2: Create your bridge
1. Log into GitGuardian Dashboard and navigate to **Settings > Security > [GitGuardian Bridge](https://dashboard.gitguardian.com/settings/workspace/security#gg_bridge)**
2. Click **"Create Bridge"**
    ![Create GG Bridge](/img/platform/enterprise-administration/ggbridge/create_ggbridge.png)
3. **Configure your bridge**: Name your bridge (e.g., "Production Network", "Dev Environment"), optionally add a Custom CA if your internal services use custom certificates, and add domain names of internal services (you can also do this later). Then download the certificate bundle and copy the bridge URL.
    ![Configure GG Bridge](/img/platform/enterprise-administration/ggbridge/configure_ggbridge.png)

    :::warning Custom CA Configuration
    The Custom CA field is **required** when your target services use certificates signed by a custom Certificate Authority (CA). You must provide the complete certificate chain in PEM format, including:
    - The Root CA certificate
    - All intermediate CA certificates (if any)

    **To export the certificate chain from your service:**
    ```bash
    openssl s_client -showcerts -connect your-internal-service.com:443 -servername your-internal-service.com </dev/null 2>/dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > bundle.pem
    ```

    **Example PEM format:**
    ```
    -----BEGIN CERTIFICATE-----
    MIIDXTCCAkWgAwIBAgIJAKoK/OvD... (Root CA)
    ...certificate content...
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    MIIDbTCCAlWgAwIBAgIJAKoK/OvD... (Intermediate CA)
    ...certificate content...
    -----END CERTIFICATE-----
    ```

    Alternatively, you can export the Root CA and Intermediate CA certificates from your browser and concatenate them into a single file:
    ![Export CA from browser](/img/platform/enterprise-administration/ggbridge/export-custom-ca.png)

    Without proper Custom CA configuration, GitGuardian Bridge will be unable to establish secure connections to your internal services and will fail with SSL verification errors.
    :::

### Step 3: Configure bridge client
Deploy the bridge client in your private network using the certificate bundle and bridge URL from Step 2.

ð **Follow the detailed installation guide**: [github.com/GitGuardian/ggbridge](https://github.com/GitGuardian/ggbridge)

The repository provides complete instructions for:
- VM deployment (via k3s)
- Kubernetes/Helm deployment  
- OpenShift configurations
- Troubleshooting guides

:::tip Important
Make sure to whitelist the bridge URL in your network security settings to allow outbound connections from your private network to GitGuardian SaaS.
:::

### Step 4: Configure URL mapping (if not done during creation)
If you didn't add domain names during bridge creation, go to your [bridge settings](https://dashboard.gitguardian.com/settings/workspace/security#gg_bridge) and add the domain names of internal services that should route through the bridge:

- `gitlab.internal.company.com`
- `bitbucket.team.local` 
- `artifactory.dev.internal`

![Configure URL Mapping](/img/platform/enterprise-administration/ggbridge/configure_url_mapping.png)

GitGuardian will automatically route traffic to these URLs through your bridge.

### Step 5: Configure your integrations
Set up your self-hosted services in GitGuardian Dashboard:

1. **Sources**: Navigate to **Settings > Integrations > [Sources](https://dashboard.gitguardian.com/settings/integrations/sources)**
2. **Destinations**: Navigate to **Settings > Integrations > [Destinations](https://dashboard.gitguardian.com/settings/integrations/destinations)**
3. **Custom Hosts**: Navigate to **Settings > Secrets > [Detectors](https://dashboard.gitguardian.com/settings/secrets/detectors?sd_validity_check=y%2Cc_set%2Cc_none%2Boperator__in)**.

Example with GitHub Enterprise:

![Example Sources Integration Settings](/img/platform/enterprise-administration/ggbridge/example_sources_integration_settings.png)

When you enter URLs that match your bridge configuration, GitGuardian automatically uses the bridge connection.

## Verify everything works

- **Bridge Status**: Check **Settings > Security > [GitGuardian Bridge](https://dashboard.gitguardian.com/settings/workspace/security#gg_bridge)** for connection status
- **Integration Health**: Monitor your source/destination health checks  
- **Test Scans**: Run a test scan on a private repository

:::tip Start Small
**Before launching full-scale scans**, we recommend starting with a small batch of repositories/sources to confirm the bridge is working correctly. This approach helps:
- Verify connectivity and authentication  
- Validate certificate configurations
- Test integration health without overwhelming your network
- Identify and resolve any configuration issues early

Once you've confirmed everything works smoothly with the small batch, you can proceed with larger-scale scanning operations.
:::

For assistance, contact **[support](mailto:support@gitguardian.com)**.
