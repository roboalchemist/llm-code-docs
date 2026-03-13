# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/vcs-integrations/azure-repos.md

# Integrate Azure DevOps

> Integrate Azure DevOps Repos with GitGuardian at the instance or organization level to monitor repositories for exposed secrets.

Monitor Azure DevOps repositories for exposed secrets in source files, configuration files, and commit histories.

## Why Monitor Azure DevOps?

Azure DevOps repositories are deeply integrated with Azure services, Microsoft 365, and enterprise Active Directory systems. When developers commit credentials or service connection secrets, they risk exposing not just individual applications but entire cloud infrastructures, potentially granting attackers access to production Azure resources and sensitive corporate data.

## Capabilities

| Feature | Support | Details |
|---------|---------|---------|
| **Historical Scanning** | â (Supported) | Complete repository history analysis |
| **Real-time Detection** | â (Supported) | Instant detection via webhooks |
| **Monitored Perimeter** | â (Supported) | Granular monitoring of your Orgs and repos |
| **Team Perimeter** | â (Supported) | Team-based access control |
| **Presence Check** | â (Supported) | Verify if secrets are still accessible |
| **File Attachments** | â (Not Supported) | Not applicable for code repositories |

**What we scan:**
- Source code files, configuration files, and raw text files
- All repository branches and commit history

## Setup

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **Azure DevOps admin** or **project admin** permissions for the organizations you want to monitor
- **Network connectivity** between GitGuardian and your self-hosted services. Check out [**GitGuardian Bridge**](/platform/deployment-model/ggbridge#supported-integrations) to enable secure connections between GitGuardian SaaS and your self-hosted services in private networks.

GitGuardian can integrate with Azure Repos in two different ways: **at the instance level or at the organization/collection level**.

:::note
In Azure Repos the wordings `Organization` and `Collection` refer to the same concept depending on the version of your Azure DevOps. In GitGuardian's dashboard, we use the wording `Organization` as it is the most common, but don't be embarrassed if you have `Collection` in your Azure Repos instance.
:::

The Azure DevOps Repos integration requires **a personal access token** for GitGuardian to be able to access your Azure Repos organizations/collections for analysis.

:::caution
To enable functional real-time scanning of your projects and repository, the personal access token owner must either be an `Organization admin` or a `Project administrator` for all projects within your organization. This can be accomplished by being added to the `Project Collection Administrators` group of the organization.
:::

### Create a Personal Access Token

:::tip
We highly recommend that you use a bot user in order to generate personal access tokens.
:::

1. Go to your âUser settingâ section on Azure DevOps.
2. For Azure Repos Service, Dive into âPersonal access tokensâ section and create a new token.
   For Azure Repos Server, you first need to dive into "Security", and then select the Personal access tokens page on the left side bar.
3. Set a name (ex: âgitguardianâ).
4. Select if you want to provide access for the current organization or for the entire instance.
5. IMPORTANT: You must check the `Read` scope for **Code** and **Graph** (click on the 'Show all scopes' link to display this scope).
The `Graph:Read` scope is used for billing purposes as it allows us to look at users, groups and their memberships.
6. We recommend you set the expiration date to 1 year, this is the maximum allowed.

:::caution
Azure DevOps has a limit of 1 year maximum for the validity of a token. It means you'll have to renew the token if you want to keep the integration up and running.
:::

The personal token enables GitGuardian to access your repos through your Azure DevOps permissions.

![Azure Repos personal access token Code](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_PAT.png)

Click on the 'Show all scopes' link to display the scope for Graph.

![Azure Repos personal access token show all scopes](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_PAT_show_all.png)

![Azure Repos personal access token Graph](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_PAT_graph.png)

:::caution
This integration doesn't monitor disabled repositories. If you include disabled repositories in your perimeter, they won't be checked and they will appear with the status `Unknown`.
:::

![Azure Repos disabled repo](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_Disable_repo.png)

Please refer to the [Azure DevOps documentation](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate)
for more information about personal access tokens.

### Instance-level integration

This integration mode will automatically monitor **all projects and repositories on the instance**.
When a new project or a new repository is created on any organization, it will be automatically included in the perimeter by GitGuardian.

#### Requirements

- Azure DevOps Service or self-managed Azure DevOps Server: minimum assured compatible version 2019
- A personal access token with **Read scope for "Code" and "Graph"**.

#### Guidelines

1. Navigate to Settings > Integrations > [Sources](https://dashboard.gitguardian.com/settings/integrations/sources).
2. Click on **Configure** for Azure Repos.
3. Click on **Start** for the instance-level option: "Monitor the entire Azure Repos instance"
   ![Azure Repos installation selection](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_Instancelvl.png)
4. Submit your Azure Repos instance url, and the personal access token created.
   ![Azure Repos token form](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_tokenform.png)
   :::caution
   Azure instance URL must be prefixed with `https://`, instances without a secure connection won't be monitored.
   The URL used should be of type scheme+basename (eg: `https://azuredevops.gitguardian.example`).
   :::
5. GitGuardian will start scanning your Azure Repos instance. You can view the projects and repositories monitored in your [Azure Repos settings page](https://dashboard.gitguardian.com/settings/integrations/azure_devops) by clicking on **See my Azure Repos perimeter**.

#### Troubleshooting

- You can **submit new personal access tokens if you want to monitor more Azure Repos instances**.
- GitGuardian automatically detects if the Personal access token becomes invalid (by expiring or being revoked) and will send an email to notify you. All of your existing data will remain accessible.
- In case you have a lot of repositories, they may take some time to show up on your perimeter.

### Organization-level integration

This integration will **only monitor organizations you select**.
When a new project is added to a monitored organization, it will be automatically added to the perimeter. However,
new organizations added to the Azure Repos instance will not be automatically included to the GitGuardian perimeter.

Note that you can't have an instance-level integration and an organization-level integration at the same time.

#### Requirements

- Azure DevOps Service or self-managed Azure DevOps Server/Data Center: minimum assured compatible version 2019
- A personal access token with **Read scope for "Code".**

#### Guidelines

1. Navigate to Settings > Integrations > [Sources](https://dashboard.gitguardian.com/settings/integrations/sources).
2. Click on **Configure** for Azure Repos.
3. Click on **Start** for the instance level option: "Monitor certain Azure Repos organizations only"
   ![Azure Repos installation selection](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_InstallOrglvl.png)
4. Submit your Azure DevOps instance url and the personal access token created. If you're willing to install only one organization, submit also the name of this organization.
   ![Azure Repos token form](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_tokenform2.png)
   :::caution
   Azure instance URL must be prefixed with `https://`, instances without a secure connection won't be monitored.
   The URL used should be of type scheme+basename (eg: `https://azuredevops.gitguardian.example`).
   :::
5. GitGuardian will display the organization available for monitoring.
   Clicking `Install`, GitGuardian will access the organization and scan the content of the repositories.
   ![ADO install form](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_InstallOrg.png)
6. You can view the projects and repositories monitored in
   your [Azure Repos settings page](https://dashboard.gitguardian.com/settings/integrations/azurerepos) by clicking on **See my Azure Repos perimeter**:

#### Troubleshooting

- You can **submit new personal access tokens if you want to monitor more Azure Repos instances or organizations**.
- GitGuardian automatically detects if the Personal access token becomes invalid (by expiring or being revoked) and will send an email to notify you. All of your existing data will remain accessible.
- In case you have a lot of repositories, they may take a short time to show up on your perimeter
- If the Azure DevOps user associated with the personal access token used for integration lacks sufficient permissions for real-time project monitoring, a visual icon will be displayed next to the project. This icon indicates that the project is still part of your scope and can be scanned manually, but it cannot be monitored in real time.

![No real-time](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_no-real-time.png)

### Rotate/Replace a Personal Access Token

In Azure Repos, the maximum lifetime of a Personal Access Token is 365 days, and there is no option to extend this duration. Additionally, updating the scopes of a Personal Access Token requires creating a new one; it cannot be modified directly. Consequently, it is necessary to replace your Personal Access Token at least once a year to continue scanning your repositories with GitGuardian.

To minimize disruption, we recommend:
1. Generate a new Personal Access Token in Azure DevOps before the expiration of the current one.
2. Add this newly created Personal Access Token to the list of tokens in GitGuardian.
3. Only after completing steps 1 and 2, remove the old Personal Access Token.

This ensures a seamless transition, allowing the new Personal Access Token to take over in case the current token expires or is deleted, thereby maintaining the functionality of your integration.

:::caution
For Organization-level installations, the new Personal Access Token should have the same permissions. Failure to do so may result in incomplete access to certain Organizations. GitGuardian will continue monitoring accessible ones and uninstall Organization(s) that are no longer reachable.
:::

## Automatic historical scan

By default, GitGuardian performs a historical scan for each newly created Azure Repos repository added to your perimeter.

You can deactivate this behavior in your [Azure Repos settings](https://dashboard.gitguardian.com/settings/integrations/azure_devops/instance) if you are a Manager of the workspace.

![Autoscan settings](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_Autoscan.png)

## Automatic repository monitoring

By default, GitGuardian automatically monitors repositories added to your perimeter.

You can deactivate this behavior in your [Azure Repos settings](https://dashboard.gitguardian.com/settings/integrations/azure_devops/instance) if you are a Manager of the workspace.

## Understanding scanning capabilities

### Historical scanning
**Uncover your secret debt:** When you first integrate this source, GitGuardian performs a comprehensive scan of your entire content history, based on your customized perimeter. This reveals secrets that may have been exposed weeks, months, or even years ago - helping you address your existing security debt.

### Real-time scanning
**Catch new exposures instantly:** Once integrated, GitGuardian continuously monitors your content through event-based detection. Any new or modified content containing secrets are detected immediately, allowing you to respond quickly to new exposures.

## Customize your monitored perimeter

Once you have set up your Azure Repos integration, you have the possibility to configure which projects and repositories to monitor in the
[Azure Repos settings section](https://dashboard.gitguardian.com/settings/integrations/azure_devops) of your workspace.

![ADO perimeter](/img/internal-monitoring/integrate-sources/vcs-integrations/azure-repos/ADO_Perimeter.png)

If you deselect a repository from your monitored perimeter, GitGuardian will not receive any commit for your future scans.
