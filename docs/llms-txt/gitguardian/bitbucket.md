# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/vcs-integrations/bitbucket.md

# Integrate Bitbucket Data Center/Server

> Integrate Bitbucket Data Center/Server with GitGuardian at the instance or project level to monitor repositories for exposed secrets.

Monitor Bitbucket Data Center/Server repositories for exposed secrets in source files, configuration files, and commit histories.

## Why Monitor Bitbucket Data Center/Server?

Bitbucket Data Center/Server installations house your organization's most critical source code and intellectual property. When developers commit hardcoded secrets into these enterprise repositories, they create vulnerabilities that can expose sensitive production systems, databases, and internal infrastructure to malicious actors or accidental breaches.

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

:::info
Throughout this page, "Bitbucket Data Center" refers to both Bitbucket Data Center and Bitbucket Server. In the app, you'll see "Data Center" as the label, which also includes Server functionality. We use "Data Center" in our wording because Bitbucket Server is deprecated and Data Center is the latest supported version by Atlassian.
:::

## Integration Overview

**Prerequisites:**
- **Owner** or **Manager** account on your GitGuardian Dashboard
- **Bitbucket admin permissions** to create personal access tokens and configure webhooks
- **Network connectivity** between GitGuardian and your self-hosted services. Check out [**GitGuardian Bridge**](/platform/deployment-model/ggbridge#supported-integrations) to enable secure connections between GitGuardian SaaS and your self-hosted services in private networks.

GitGuardian can integrate with your Bitbucket Data Center through two mechanisms: **project-level and instance-level integrations**.

:::info
Both mechanisms require a personal access token with the following scopes: **Read permissions for projects and Admin permissions for repositories**. This allows GitGuardian to create webhooks for receiving information on repository updates.
:::

GitGuardian requires a 3-hour window before synchronizing Bitbucket instance information. This could translate, at worst, to a 3-hour delay before a newly created project is monitored.

In order to keep your integration safe, SSL verification is required for integrating Bitbucket instances.
All messages between GitGuardian and your Bitbucket instance will be authenticated by HMAC SHA-256.

## Setup

### Create a Personal Access Token

:::tip
We strongly recommend that you use **a bot user in order to generate personal access tokens**. This is because a personal access token is closely linked to the Bitbucket account that created it. If the Bitbucket account is deleted, the token it generated is also deleted.
:::

1. Navigate to your Bitbucket user settings
   (typically on your upper right hand corner, under **Manage Account**)
2. Go to **Personal access tokens** section
3. Create a personal access token with a simple name such as "GitGuardian"
   and **Read** permissions on projects and **Admin** permissions on repositories.
   Set the **"Automatic Expiry"** option to **"No"**.
   The personal token enables GitGuardian to create webhooks through your Bitbucket's API.
   ![Bitbucket personal access token creation form](/img/internal-monitoring/integrate-sources/vcs-integrations/bitbucket/bb-token.png)

Please refer to the [Bitbucket server documentation](https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html)
for more information about personal access tokens.

> We advise that you never revoke the token before removing your Bitbucket integration on [GitGuardian dashboard](https://dashboard.gitguardian.com/settings/integrations/bitbucket).

### Instance-level integration

This integration mode will automatically monitor **all projects and repositories on the instance**.

#### Requirements

- Self-managed Bitbucket Server/Data Center: minimum assured compatible version 7.6+
- An Administrator (`SYSADMIN` global permission) token with **Read permissions for projects and Admin permissions for repositories**

#### Guidelines

1. Navigate to Settings > Integrations > [Sources](https://dashboard.gitguardian.com/settings/integrations/sources).
2. Click on **Configure** for Bitbucket.
3. Click on **Start** for the instance level option: "Monitor the entire Bitbucket instance"
4. Submit your Bitbucket instance url and the personal access token created.
   ![Bitbucket token form](/img/internal-monitoring/integrate-sources/vcs-integrations/bitbucket/bb-token-form.png)
   :::caution
   Bitbucket instance URL must be prefixed with `https://`, instances without a secure connection won't be monitored.
   The URL used should be of type scheme+basename (eg: `https://bitbucket.gitguardian.example`).
   :::
5. GitGuardian will start monitoring your Bitbucket instance. You can view the projects and repositories monitored in
   your [Bitbucket settings page](https://dashboard.gitguardian.com/settings/integrations/bitbucket) by clicking on **See my Bitbucket perimeter**.

#### Events subscription details

Our integration will subscribe to the following events:

- `Repository update events`
- `Push events`

#### Troubleshooting

- You can **submit new personal access tokens if you want to monitor more Bitbucket instances**.
- GitGuardian automatically detects if the Personal access token becomes invalid (by expiring or being revoked) and will send an email to notify you. All of your existing data will remain accessible.
- In case you have a lot of repositories, they may take a short time to show up on your perimeter page while GitGuardian sets up the necessary webhooks on each of them.

### Project-level integration

This integration will **only monitor projects selected by the user**.
When a new repository is added to a monitored project, it will be automatically monitored.

Note that you can't have an instance-level integration and a project-level integration at the same time.

#### Requirements

- Self-managed Bitbucket Server/Data Center: minimum assured compatible version 7.6+
- A token with **Read permissions for projects and Admin permissions for repositories**. A **project-level** integration can be created by any user with Administrator permissions on a Bitbucket project. It does not require the user to be an Administrator of the instance.

#### Guidelines

1. Navigate to Settings > Integrations > [Sources](https://dashboard.gitguardian.com/settings/integrations/sources).
2. Click on **Configure** for Bitbucket.
3. Click on **Start** for the project level option: "Monitor only certain Bitbucket projects"
4. Submit your Bitbucket instance url and the personal access token created.
   ![Bitbucket token form](/img/internal-monitoring/integrate-sources/vcs-integrations/bitbucket/bb-token-form.png)
   :::caution
   Bitbucket instance URL\_ must be prefixed with `https://`, instances without a secure connection won't be monitored.
   :::
5. GitGuardian will display the projects available for monitoring.
   Clicking `Install`, GitGuardian will install hooks and allow all repositories of that project to be monitored.
   ![Bitbucket install form](/img/internal-monitoring/integrate-sources/vcs-integrations/bitbucket/bb-install-form.png)
6. You can view the projects and repositories monitored in
   your [Bitbucket settings page](https://dashboard.gitguardian.com/settings/integrations/bitbucket) by clicking on **See my Bitbucket perimeter**.

#### Events subscription details

Our integration will subscribe to the following events:

- `Repository update events`
- `Push events`

#### Troubleshooting

- You can **submit new personal access tokens if you want to monitor more Bitbucket instances or projects**.
- GitGuardian automatically detects if the Personal access token becomes invalid (by expiring or being revoked) and will send an email to notify you. All of your existing data will remain accessible.
- In case you have a lot of repositories, they may take a short time to show up on your perimeter page while GitGuardian sets up the necessary webhooks on each of them.

## Automatic historical scan

By default, GitGuardian performs a historical scan for each newly created Bitbucket repository added to your perimeter.

You can deactivate this behavior in your [Bitbucket settings](https://dashboard.gitguardian.com/settings/integrations/bitbucket) if you are a Manager of the workspace.

![Autoscan settings](/img/internal-monitoring/integrate-sources/vcs-integrations/bitbucket/bb-auto-scan-setting.png)

## Automatic repository monitoring

By default, GitGuardian automatically monitors repositories added to your perimeter.

You can deactivate this behavior in your [Bitbucket settings](https://dashboard.gitguardian.com/settings/integrations/bitbucket) if you are a Manager of the workspace.

![Autoscan settings](/img/internal-monitoring/integrate-sources/vcs-integrations/bitbucket/bb-auto-monitor-new-projects-setting.png)

## Customize your monitored perimeter

Once you have set up your Bitbucket integration, you have the possibility to configure which repositories to monitor in the
[Bitbucket settings section](https://dashboard.gitguardian.com/settings/integrations/bitbucket) of your workspace.

If you deselect a repository from your monitored perimeter:

- GitGuardian will no longer receive any content of its commits
- and therefore you won't receive any alerts related to this repository.

## Possible adjustments of Bitbucket Server settings

The [Bitbucket Server Config](https://confluence.atlassian.com/bitbucketserver076/bitbucket-server-config-properties-1026535505.html)
properties allow you to modify some default behaviors of Bitbucket Server so that it can handle
monitoring of a greater number of repositories.

Reduce the delay of webhooks (so that GitGuardian incidents do not appear late):

- `plugin.webhooks.io.threads` can be increased from the default `3` if the Bitbucket host has enough threads.
- `plugin.webhooks.http.connection.host.max` can be increased from the default `5`.
