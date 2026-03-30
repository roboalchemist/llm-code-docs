# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/vcs-integrations/gitlab.md

# Integrate GitLab

> Integrate GitLab with GitGuardian using system hooks or group hooks to monitor repositories for exposed secrets.

Protect your source code by monitoring GitLab repositories for exposed secrets in commits, merge requests, and project files.

## Why Monitor GitLab?

GitLab repositories serve as the backbone of modern DevOps workflows, making them prime targets for secret exposure. When developers commit credentials, API tokens, or configuration secrets, they create permanent vulnerabilities in git history that can be exploited by anyone gaining repository access, potentially compromising entire development and production environments.

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
- **GitLab admin** permissions (for system hooks) or **group owner** permissions (for group hooks)
- **Personal access token** with appropriate scopes
- **Network connectivity** between GitGuardian and your self-hosted services. Check out [**GitGuardian Bridge**](/platform/deployment-model/ggbridge#supported-integrations) to enable secure connections between GitGuardian SaaS and your self-hosted services in private networks.

GitGuardian integrates with GitLab in two ways: **instance-level with system hooks** or **group-level with group hooks**. Please refer to the GitLab documentation for more information on [system hooks](https://docs.gitlab.com/ee/administration/system_hooks.html) and [group hooks](https://docs.gitlab.com/ee/api/groups.html#hooks).

### Create a Personal Access Token

We highly recommend that you use a bot user in order to generate personal access tokens.

:::warning
As mentioned above, only personal access tokens are currently supported. Other types of tokens (like group access tokens) are not supported.
:::

1. Navigate to your GitLab user settings
2. Go to **Access Tokens** section
3. Create a personal access token with a simple name such as "GitGuardian" and **`api` scope**.
   The personal token enables GitGuardian to create webhooks through your GitLab permissions.
   ![GitLab personal access token](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_personal_access_token.png)

Please refer to the [GitLab documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#creating-a-personal-access-token)
for more information about personal access tokens.

It's also possible to use a personal access token with the **`read_api`** scope. In this case, a hook URL and a secret token will be displayed once you submit the form. Use this hook URL and secret token to [add a new system hook on your GitLab instance](https://docs.gitlab.com/ee/api/system_hooks.html#add-new-system-hook). Once this is done, your GitLab integration will be functional.

If "*Admin mode*" is enabled on your GitLab instance, you'll need the `admin_mode` scope in addition to the `api` or `read_api` scope.

### Integrate your GitLab instance with system hooks

**System hooks** can only be created **by an Administrator of the instance**, they provide access to projects belonging to all users and groups. The system hook integration is only available for the on-premise version of GitLab (such an integration is not possible on GitLab.com).

:::tip
We recommend that you leverage a bot user when integrating with GitGuardian.
:::

#### Requirements

- Self-managed GitLab: GitLab Community Edition or any plan of GitLab Enterprise Edition. v11.0+
- GitLab.com (SaaS): **IMPORTANT** GitGuardian cannot integrate with GitLab.com (SaaS) via System hooks.

#### Guidelines

1. Navigate to Settings > Integrations > [Sources](https://dashboard.gitguardian.com/settings/integrations/sources).
2. Click on **Configure** for GitLab.
3. Click on **Start** for the system hook option: "Monitor the entire GitLab instance"
4. Submit your GitLab instance url and the personal access token created.
   ![GitLab system hook form](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_system_hook_form.png)
   :::caution
   _GitLab instance URL_ must be prefixed with `https://`, instances without a secure connection won't be monitored.
   :::
5. GitGuardian will instantly start monitoring your GitLab instance. You can see the projects and groups monitored in
   your [GitLab settings page](https://dashboard.gitguardian.com/settings/integrations/gitlab) by clicking on **See my GitLab perimeter**:
   ![GitLab system hook perimeter](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_perimeter.png)

#### Events subscription details

Our system hook will subscribe to the following events:

- `Repository update events`
- `Push events`
- `Merge request events`

and SSL verification will be enabled.

Other events our system hooks will subscribe to but won't process:

- `Tag push events`
- `Issues events`
- `Confidential issues events`
- `Comments`
- `Confidential comments`
- `Job events`
- `Pipeline events`
- `Wiki page events`
- `Deployments events`
- `Releases events`
- `Member events`
- `Subgroup events`
- `Feature flag events`

#### Troubleshooting

- GitGuardian automatically detects if the system hook is deleted from GitLab side or if the Personal access token becomes invalid (by expiring or being revoked). We will send an email to notify you. All of your existing data will remain accessible.
- If your GitLab instance is marked as ânot monitored" but the personal access token associated is still active, you can reactivate it by clicking on the **synchronize** button. It will recreate a system hook programmatically.
  ![GitLab system hook instances table](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_system_hook_instances.png)
- If the token is invalid you can set a new personal access token by editing it:
  ![GitLab system hook edit](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_system_hook_edit.png)
- If the admin token is revoked, GitGuardian will detect it and automatically deactivate your GitLab integration if no other
  active token is present. If another token suitable for monitoring exists, the GitLab integration will use that token. All your existing data will remain accessible.

:::caution
**IMPORTANT**: Do not change the URL or the Personal access token of the system hook from the GitLab admin interface or this will break the integration.
:::

### Integrate your GitLab groups with group hooks

**Group hooks** require the user to have **Owner permissions on the GitLab groups to be monitored**. Group hooks do not support the monitoring of GitLab users personal projects. The group hook integration works for both GitLab on-premise and Gitlab.com. Note that you can only monitor up to 50,000 projects per group for a group hook integration.

:::tip
We recommend that you leverage a bot user when integrating with GitGuardian.
:::

Note that you can't have a system hook integration and a group hook integration at the same time.

#### Requirements

- Self-managed GitLab: Starter plan and higher tiers. v13.5+
- GitLab.com (SaaS): Premium plan

#### Guidelines

1. Navigate to Settings > Integrations > [Sources](https://dashboard.gitguardian.com/settings/integrations/sources).
2. Click on **Configure** for GitLab.
3. Click on **Start** for the group hook option: "Monitor only certain GitLab groups"
4. Submit your GitLab instance url and the personal access token, and make sure to name this personal access token as you might use several
   of them in the future to integrate more GitLab groups.
   ![GitLab group hook form](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_group_hook_form.png)
   :::caution
   _GitLab instance URL_ must be prefixed with `https://`, instances without a secure connection won't be monitored.
   :::
5. You are then brought to the configuration page of your GitLab integration where you can see the list of all the GitLab
   groups and subgroups that your personal access token gives access to.
   Click **Install** for the GitLab groups and subgroups you want GitGuardian to monitor.
   ![GitLab group hook configuration](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_group_hook_configuration_page.png)
6. You can see the projects and groups monitored in your [GitLab settings page](https://dashboard.gitguardian.com/settings/integrations/gitlab)
   ![GitLab group hook perimeter](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_perimeter.png)

#### Installation remarks

- When you choose to install a GitLab group, all its sub-groups will also be installed automatically.
  In doing so, the "parent" group and "children" subgroups are linked together and if you only want to uninstall one subgroup,
  you will need to uninstall the "parent" group first.
- A GitLab group cannot belong to two personal access tokens. Therefore, when you want to install a "parent" group that
  has an already-installed subgroup you must first uninstall the "child" subgroup.

#### Events subscription details

Our group hooks will subscribe to the following events:

- `Repository update events`
- `Push events`
- `Merge request events`

and SSL verification will be enabled.

Other events our group hooks will subscribe to but won't process:

- `Tag push events`
- `Issues events`
- `Confidential issues events`
- `Comments`
- `Confidential comments`
- `Job events`
- `Pipeline events`
- `Wiki page events`
- `Deployments events`
- `Releases events`
- `Member events`
- `Subgroup events`
- `Feature flag events`

#### Troubleshooting

- You can **submit new personal access tokens if you want to monitor more GitLab groups**. Multiple tokens can be added for group hooks integration.
  If several tokens are associated with the same GitLab group, you have to choose which token will be monitoring it.
  ![GitLab group hook new personal access token](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_group_hook_new_personal_access_token.png)
- If the token is revoked, the group will no longer be monitored (you can install it again with another token, but GitGuardian will not arbitrarily choose another token for you). In this scenario you'll receive an email informing of the unmonitored status of the integration.

## Automatic historical scan

By default, GitGuardian performs a historical scan for each newly created GitLab project added to your perimeter.

You can deactivate this behavior in your [GitLab settings](https://dashboard.gitguardian.com/settings/integrations/gitlab) if you are a Manager of the workspace.

![Autoscan settings](/img/internal-monitoring/integrate-sources/vcs-integrations/gitlab/gitlab_auto_scan_setting.png)

## Automatic repository monitoring

By default, GitGuardian automatically monitors repositories added to your perimeter.

You can deactivate this behavior in your [GitLab settings](https://dashboard.gitguardian.com/settings/integrations/gitlab) if you are a Manager of the workspace.

## Understanding scanning capabilities

### Historical scanning
**Uncover your secret debt:** When you first integrate this source, GitGuardian performs a comprehensive scan of your entire content history, based on your customized perimeter. This reveals secrets that may have been exposed weeks, months, or even years ago - helping you address your existing security debt.

### Real-time scanning
**Catch new exposures instantly:** Once integrated, GitGuardian continuously monitors your content through event-based detection. Any new or modified content containing secrets are detected immediately, allowing you to respond quickly to new exposures.

## Customize your monitored perimeter

Once you have set up your GitLab integration, you have the possibility to configure which projects to monitor in the
[GitLab settings section](https://dashboard.gitguardian.com/settings/integrations/gitlab) of your workspace.

If you deselect a project from your monitored perimeter:

- GitGuardian will no longer fetch the content of its commits, therefore you won't receive any alerts related to this project.
- The webhook installed on this project will still exist, therefore you can easily turn the monitoring back on at any moment.
