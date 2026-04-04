# Source: https://docs.gitguardian.com/platform/getting-started/integrate.md

# Integrate your first repositories

> Guide to integrating your first VCS source with GitGuardian to start monitoring repositories for secrets.

To get started with Internal Monitoring for secrets, you need to add an integration with a source like a Version Control System (VCS).

![Get started page - connect a source](/img/platform/getting-started/connect-source.png)
![Sources integrations](/img/platform/getting-started/sources-integrations.png)

:::tip

If you want to try GitGuardian Internal Monitoring out on a test repository, go ahead and clone our [**sample_secrets repo**](https://github.com/GitGuardian/sample_secrets). It contains 8 unique secrets our detection engine will find during the scans.

:::

## Integrate with GitHub

1. From the VCS integrations page, select GitHub

![GitHub integration](/img/platform/getting-started/vcs_integrations-github-1.png)

2. Confirm access to your GitHub account

![GitHub integration](/img/platform/getting-started/vcs_integrations-github-2.png)

3. Choose whether you want GitGuardian to monitor all your repositories or a selection of repositories. This can be changed later from your GitHub account.

![GitHub integration](/img/platform/getting-started/vcs_integrations-github-3.png)
![GitHub integration](/img/platform/getting-started/vcs_integrations-github-4.png)

4. Go back to your GitGuardian dashboard to see your added user or organization and its repositories.

![GitHub integration](/img/platform/getting-started/vcs_integrations-github-5.png)

Once installed, GitGuardian will also give you the option to add or remove repositories from the monitored perimeter directly from your workspace.

## Integrate with other VCS platforms

### Integrate with GitLab

When integrating GitGuardian with GitLab, you can choose to monitor an entire instance or certain groups only. In both cases, you will need to generate a personal access token with admin permissions for the chosen perimeter.

Once installed, GitGuardian will also give you the option to add or remove repositories from the monitored perimeter directly from your workspace.

#### Step 1. Create a personal access token

1. Go to your **User Settings** on GitLab
2. View the **Access Tokens** section
3. Choose a name (for example âgitguardian-secrets-scanningâ)
4. IMPORTANT: Select the **API** scope

If you need to, visit the [GitLab documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) for more details on how to create personal access tokens.

#### Step 2. Configure your GitLab integration via a system hook or a group hook

There are two ways to configure your GitLab integration, using system hooks or group hooks. Now that you have your personal access token ready, follow one of these guides depending on your preference:

- [setup a system hooks type integration](../../internal-monitoring/integrate-sources/vcs-integrations/gitlab.md#integrate-your-gitlab-instance-with-system-hooks),
- [setup a group hooks type integration](../../internal-monitoring/integrate-sources/vcs-integrations/gitlab.md#integrate-your-gitlab-groups-with-group-hooks).

### Integrate with Bitbucket server/data center

:::warning

This integration does not support projects and repositories hosted on Bitbucket Cloud (bitbucket.org). Check out our Bitbucket Pipelines integration to keep your Bitbucket Cloud workspace secure.

:::

#### Step 1. Create a personal access token

1. In your Bitbucket workspace, navigate to your Bitbucket user settings (typically on your upper right hand corner, under Manage Account)
2. Go to the Personal access tokens section
3. Create a personal access token with a simple name such as "GitGuardian" and Read permissions on projects and Admin permissions on repositories. Set the "Automatic Expiry" option to "No".

#### Step 2. Configure your Bitbucket integration via a system hook or a group hook

There are two ways to configure your Bitbucket integration, at the instance-level or at the project-level. Follow one of these guides depending on your preference:

- [setup an instance-level integration](../../internal-monitoring/integrate-sources/vcs-integrations/bitbucket.md#instance-level-integration),
- [setup a project-level integration](../../internal-monitoring/integrate-sources/vcs-integrations/bitbucket.md#project-level-integration).

<!-- TODO -->
<!-- ### Integrate with Azure Repos -->
