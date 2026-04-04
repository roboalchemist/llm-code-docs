# Aikido Security Documentation

Source: https://help.aikido.dev/llms-full.txt

---

# Aikido Docs Overview

### Getting Started <a href="#getting-started" id="getting-started"></a>

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="https://help.aikido.dev/getting-started/overview"><strong>Account Creation &#x26; User Management</strong></a></td><td>Set up your account, user, team and application management</td><td></td><td><a href="getting-started">getting-started</a></td></tr><tr><td><a href="getting-started/core-functionalities"><strong>Manage Findings</strong></a></td><td>Manage and triage your security findings</td><td></td><td><a href="getting-started/core-functionalities">core-functionalities</a></td></tr><tr><td><a href="getting-started/task-management-systems"><strong>Task Management Tools</strong></a></td><td>Learn how to integrate your task management tool</td><td></td><td><a href="getting-started/task-management-systems">task-management-systems</a></td></tr><tr><td><a href="getting-started/chat-and-alerts"><strong>Chat &#x26; Alerts</strong></a></td><td>Connect your Slack or MS Teams for instant alerts</td><td></td><td><a href="getting-started/chat-and-alerts">chat-and-alerts</a></td></tr></tbody></table>

### Scanning Capabilities <a href="#getting-started" id="getting-started"></a>

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="code-scanning"><strong>Code Scanning</strong></a></td><td>Learn how to connect your source code &#x26;  scanning best practices.</td><td></td><td><a href="code-scanning">code-scanning</a></td></tr><tr><td><a href="cloud-scanning"><strong>Cloud Scanning</strong></a></td><td>Connect your cloud to scan for misconfigurations and security risks.</td><td></td><td><a href="cloud-scanning">cloud-scanning</a></td></tr><tr><td><a href="container-image-scanning"><strong>Container Image Scanning</strong></a></td><td>Learn how to connect &#x26; configure your Container Registries.</td><td></td><td><a href="container-image-scanning">container-image-scanning</a></td></tr><tr><td><a href="virtual-machine-scanning"><strong>Virtual Machine Scanning</strong></a></td><td>Learn how to connect your Virtual Machines for scanning.</td><td></td><td><a href="virtual-machine-scanning">virtual-machine-scanning</a></td></tr><tr><td><a href="dast-surface-monitoring"><strong>Surface Monitoring</strong></a></td><td>Learn how to connect your Domain, API &#x26; Web App for scanning</td><td></td><td><a href="dast-surface-monitoring">dast-surface-monitoring</a></td></tr><tr><td><a href="pentests/aikido-pentest"><strong>Pentests</strong></a></td><td>Learn how to setup continuous, automated penetration testing</td><td></td><td></td></tr></tbody></table>

### Developer Integrations <a href="#getting-started" id="getting-started"></a>

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="pr-and-release-gating"><strong>PR &#x26; Release Gating</strong></a></td><td>Learn how to set up pull request &#x26; feature branch scanning.</td><td></td><td><a href="pr-and-release-gating">pr-and-release-gating</a></td></tr><tr><td><a href="aikido-autofix"><strong>Aikido AutoFix</strong></a></td><td>Learn how to create PRs that fix vulnerabilities with one click.</td><td></td><td><a href="aikido-autofix">aikido-autofix</a></td></tr><tr><td><a href="ide-plugins"><strong>IDE Plugins</strong></a></td><td>Use our IDE plugins to scan and auto-remediate vulnerabilities while coding.</td><td></td><td><a href="ide-plugins">ide-plugins</a></td></tr><tr><td><a href="code-quality"><strong>Code Quality</strong></a></td><td>Learn how to maintain high standards across your codebase</td><td></td><td></td></tr></tbody></table>

### Zen Firewall

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="zen-firewall"><strong>Zen Firewall</strong></a></td><td>Your in-app firewall for peace of mind–at runtime</td><td></td><td><a href="zen-firewall">zen-firewall</a></td></tr></tbody></table>

### Compliance & Governance

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="compliance-and-reporting"><strong>ISO 27001 &#x26; SOC 2 Compliance</strong></a></td><td>Learn how to connect Aikido Security with your compliance software.</td><td></td><td><a href="compliance-and-reporting">compliance-and-reporting</a></td></tr></tbody></table>

# Getting Started Overview

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="setting-up-your-account"><strong>Setting Up Your Account</strong></a></td><td>Learn how to create an account and connect your Git</td><td><a href="setting-up-your-account">setting-up-your-account</a></td></tr><tr><td><a href="automated-user-management"><strong>User Management</strong></a></td><td>Easily control who has access with automated user management, roles, and SSO setup.</td><td><a href="automated-user-management">automated-user-management</a></td></tr><tr><td><a href="manage-teams-and-applications"><strong>Manage Teams &#x26; Applications</strong></a></td><td>Organize teams, assign responsibilities, and manage your apps and projects in Aikido.</td><td><a href="manage-teams-and-applications">manage-teams-and-applications</a></td></tr><tr><td><a href="core-functionalities"><strong>Manage Findings</strong></a></td><td>Review, triage, and manage security findings in Aikido</td><td><a href="core-functionalities">core-functionalities</a></td></tr><tr><td><a href="task-management-systems"><strong>Task Management Tools</strong></a></td><td>Learn how to integrate your task management tool</td><td><a href="task-management-systems">task-management-systems</a></td></tr><tr><td><a href="chat-and-alerts"><strong>Chat &#x26; Alerts</strong></a></td><td>Connect your Slack or MS Teams to receive instant alerts</td><td><a href="chat-and-alerts">chat-and-alerts</a></td></tr></tbody></table>

# Setting Up Your Account

# Connect Your Repositories

## Introduction <a href="#introduction" id="introduction"></a>

Welcome to Aikido, where we prioritize the security of your software without compromising on your data's privacy. At Aikido, we stand firm on our commitment: **we never store your code**.

As soon as you have done account setup and connected repositories, Aikido will instantly start a scan. Results will start coming in **within 1 minute. By connecting your repositories, you will already be benefiting from six different security scans** (SCA, SAST, Secrets, Licenses, IaC, Malware)**.**

You can setup an account in Aikido through your version control system —be it GitHub, GitLab, Bitbucket, Azure Devops, or on-premise solutions.

## Detailed Integration Guides <a href="#detailed-integration-guides" id="detailed-integration-guides"></a>

For more specific instructions for account setup, please check out the dedicated articles below:

* [Connect your GitHub Account to Aikido](https://help.aikido.dev/docs/code-scanning/connect-your-source-code/connect-github-account-to-aikido)
* [Connect your Bitbucket Account to Aikido](https://help.aikido.dev/docs/code-scanning/connect-your-source-code/connect-bitbucket-account-to-aikido)
* [Connect your GitLab Account to Aikido](https://help.aikido.dev/docs/code-scanning/connect-your-source-code/connect-gitlab-account-to-aikido)
* [Connect your Azure Devops Account to Aikido](https://help.aikido.dev/docs/code-scanning/connect-your-source-code/connect-azure-devops-projects-to-aikido)
* [Connect your GitLab Self-Managed Server to Aikido](https://help.aikido.dev/docs/code-scanning/connect-your-source-code/connect-gitlab-self-managed-server-to-aikido)
* [Setup Local Scanner Account if you don't want code to leave your premise](https://help.aikido.dev/docs/code-scanning/local-code-scanning/account-creation-for-local-scanning-on-aikido)

These guides provide detailed steps and considerations for a smooth and secure integration process tailored to your needs.

# Account Setup with Multiple Gits

If you have repositories with multiple Git Providers (such as GitHub and GitLab) and you want to quickly access them, this is possible by setting up multiple workspaces that are connected to those specific Gits.

## Step-by-Step Guide <a href="#step-by-step-guide" id="step-by-step-guide"></a>

**Step 1:** Add a new workspace by clicking your profile icon in the top right corner.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9e8383f7e131fbf7800ee5466bc7341f327a810b%2Faccount-setup-with-multiple-gits_93857e5c-5593-4dd8-a34a-e2ea48456e36.png?alt=media)

**Step 2:** Click "Logout" on the top right if you need to connect to a different Git provider. If it is the same Git provider, continue by selecting "Add a New Workspace."

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4b562977262ec5c2325165f5866d7d5917724830%2Faccount-setup-with-multiple-gits_dcb7ca88-5e79-4d63-8a9b-34f2dff195ca.png?alt=media)

> This screen can look slightly different when you are connected via Azure, GitLab Self Managed or Local Scanner.

**Step 3:** Choose the preferred Git Provider on the login screen.

![Login options for GitHub, Bitbucket, and GitLab displayed as prominent buttons.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a1d23e83ed2631f57ff3cfaf49ed93bb43f544ef%2Faccount-setup-with-multiple-gits_7c0e3c26-7568-4949-a10c-dfb60ca25817.png?alt=media)

**Step 4:** After setting up the new account, merge both accounts. [Click here for more information](https://help.aikido.dev/docs/getting-started/setting-up-your-account/link-and-merge-multiple-login-types-github-gitlab-etc) on how to set this up.

**Step 5:** Switch between different Git accounts using the workspace switcher located in the top left corner.

![GitHub dashboard showing repository selection and vulnerability summary chart.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9d0c46ff88832f76efae093d92e2fbc1ead03f3d%2Faccount-setup-with-multiple-gits_4ee894b7-873c-4531-87c3-f0c9bf8d9190.png?alt=media)

# Merge Multiple Login Types

### Introduction <a href="#introduction" id="introduction"></a>

If you have multiple organizations across different source code managers (e.g. GitHub and GitLab), you can link these different login types which allows for easily swapping between organizations using the org-switcher at the **top left of the screen**. This allows you to not always having to go through the login hassle when you are changing login types.

{% hint style="info" %}
**Note.** this will not result in having all issues in 1 feed. All issues across workspaces is currently not supported
{% endhint %}

## How to Link Accounts <a href="#how-to-link-accounts" id="how-to-link-accounts"></a>

**Prerequisite:**

* Functionality needs to be enabled. ​**To enable, please contact our support over chat or via** [**support@aikido.dev**](mailto:support@aikido.dev)**.**
* Email needs to be the same across accounts

**Steps to link**

1. Open your [personal profile](https://app.aikido.dev/my-profile)via the top right corner and select 'Link A Secondary User' in the Personal Profile Section.
2. Select your accounts to link (add links for account 1 and account 2). Make sure these accounts use the same email address. If you are using Azure DevOps, select Microsoft or Google Login (depending on the account you have used).

   ![Link two accounts for seamless integration and easy switching between platforms.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c358940f2740f8727aa5a77fc5ee0aebe5f02b73%2Flink-and-merge-multiple-login-types-github-gitlab-etc_e527424d-3d62-4cb2-8ff3-2ff70811e41d.png?alt=media)
3. Click 'Link Accounts'.\
   ​

   ![Link GitHub and GitLab accounts for seamless integration and easy switching.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-340c13a935649351b5a6bcff3bed8acb34c210d8%2Flink-and-merge-multiple-login-types-github-gitlab-etc_ab79e54e-04bb-4a8e-b641-c0afdf6b9663.png?alt=media)
4. Log in with any of the linked accounts and you'll find the organizations of both users in the organization dropdown.\
   ​

   ![Workspace menu for Aikido Security with options to manage team and settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7206c7f183a651c2fc6a9430a606319f6385b456%2Flink-and-merge-multiple-login-types-github-gitlab-etc_27bda9fe-764b-48a3-b08e-f6ae34b2b0f1.png?alt=media)

### How to link 3 or more accounts <a href="#how-to-link-3-or-more-accounts" id="how-to-link-3-or-more-accounts"></a>

It is possible to link more than 2 accounts, which is a bit more complex to set up. All workspaces will need to be linked to each other, in order to have all workspaces in the sidebar visible at all times.

**Example.**

If you have already linked a GitLab and a Bitbucket workspace, and you want to add a third GitHub workspace you will need to

* Link the GitLab and GitHub workspaces
* Link the Bitbucket and GitHub workspaces

In order to link these, visit the merge logins screen directly via [this link](https://app.aikido.dev/merge-logins).

# Change Email for Notifications

## Introduction <a href="#introduction" id="introduction"></a>

You can change your email address for receiving notifications (e.g., new issues and weekly digest). This change does not impact your authentication method.

## How To Change Your Email <a href="#how-to-change-your-email" id="how-to-change-your-email"></a>

**Step 1:** Navigate to [**Your Profile**](https://app.aikido.dev/my-profile) via the top right corner of the Aikido interface.

![User profile dropdown menu with options to view profile, add workspace, or log out.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-be41d929fe8236461b3b618b56a3344eb863f2dd%2Fchange-email-for-receiving-notifications_73882820-d86d-4804-9e9f-35837a813d6f.png?alt=media)

**Step 2:** In the **email notification settings**, click the **edit icon** (next to the email).

![Notification email settings displaying the registered email address for alerts.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8e7b8181bf3407189e7d452261520a23ebe3a1cc%2Fchange-email-for-receiving-notifications_f2090201-6e48-4b48-b934-a283aa631686.png?alt=media)

**Step 3:** **Enter your new email address** in the provided field within the modal.

![Edit notification email address for receiving Aikido security alerts.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-db49212528107d6606e98e05d0a791838003111a%2Fchange-email-for-receiving-notifications_11a8c09d-81df-480d-829d-c070bc3af3e0.png?alt=media)

**Step 4:** After entering your new email, **a verification email will be sent** to the new address. Follow the instructions within this email to confirm the change.

![Email verification prompt for notification updates on the Aikido platform.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fd6ae6993feaadda9f97958d210f77cd7d399fcf%2Fchange-email-for-receiving-notifications_59e0bb34-3943-4fe0-97e6-e9def128a581.png?alt=media)

# User Management

# Inviting Users to Aikido

Aikido offers two primary methods for inviting users to your workspace: inviting users who are part of your Github organization/ Gitlab group/ Bitbucket workspace and inviting users who do not have access to an organizational Git account.

![Login option menu: Only organizational GitHub login is currently selected.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ee749b60b7f4c45822fe2f189a6380a3572f9f19%2Finviting-users-to-aikido_dc9e92e7-5586-4876-80de-6d3564125852.png?alt=media)

### Option 1. Inviting Users That Are Part of Your Organization / Group <a href="#inviting-users-that-are-part-of-your-organization" id="inviting-users-that-are-part-of-your-organization"></a>

{% hint style="success" %}
This functionality is recommended as this allows for hassle-free automatic on- and offboarding of all your users.
{% endhint %}

By connecting to your organization’s Git provider (GitHub, GitLab, Bitbucket), Aikido ensures a streamlined on- and off-boarding process. This integration simplifies the management of user access and roles, ensuring that as users join or leave your Git organization, their access to Aikido is automatically adjusted.

{% hint style="info" %}
**Note.** For GitHub these are members part of the **organisation**. For Gitlab these are members of a **group**. For Bitbucket, these are members of a **workspace**.
{% endhint %}

**Choose the below login method in Aikido 👇**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-db345a62c52d75dc3a18fb0fd601a14f674075a1%2Finviting-users-to-aikido_200a3413-312d-4613-a3fc-1286345ef84b.png?alt=media)

***

### Option 2. Inviting Users That Do Not Have Access to an Organization Git Account <a href="#inviting-users-that-do-not-have-access-to-an-organization-git-account" id="inviting-users-that-do-not-have-access-to-an-organization-git-account"></a>

{% hint style="info" %}
Automated off-boarding is **not available** for this option. You need to manually manage your users and deactivate them once access should be revoked.
{% endhint %}

This is especially useful for adding billing personnel, users with personal GitHub accounts, freelancers, and auditors requiring temporary access. Read the full article on how to [Invite Users to Aikido Without a Git Account](https://help.aikido.dev/docs/getting-started/automated-user-management/invite-users-to-aikido-without-a-git-account).

**Choose the below login method in Aikido 👇**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cb8e3fdf92fefefc67834fb53ab3bf39ed9fa905%2Finviting-users-to-aikido_4aa29acf-2342-428f-940d-67b1b580c116.png?alt=media)

***

### More info on authentication & automated user management <a href="#more-info-on-authentication--automated-user-management" id="more-info-on-authentication--automated-user-management"></a>

* [GitHub Integration](https://help.aikido.dev/docs/getting-started/automated-user-management/automated-user-management/github-integration-for-authentication-and-user-management)
* [GitLab Cloud Integration](https://help.aikido.dev/docs/getting-started/automated-user-management/automated-user-management/gitlab-integration-for-authentication-and-user-management)
* [GitLab Self-Managed Integration](https://help.aikido.dev/docs/getting-started/automated-user-management/automated-user-management/gitlab-self-managed-integration-for-authentication-and-user-management)
* [BitBucket Cloud Integration](https://help.aikido.dev/docs/getting-started/automated-user-management/automated-user-management/bitbucket-cloud-integration-for-authentication-and-user-management)

# Invite Users to Aikido Without a Git Account

Aikido provides flexible options for inviting users who do not have a GitHub/BitBucket/GitLab account or prefer using alternative login methods such as Google, Microsoft, or a personal GitHub/BitBucket/GitLab account.

## Use Cases <a href="#use-cases" id="use-cases"></a>

* **Billing Personnel**: Users responsible for billing who do not have a Git account.
* **Personal GitHub Account Users**: Users with a personal GitHub account not affiliated with the organization.
* **Freelancers**: Contractors needing partial or temporary access.
* **Auditors**: External auditors requiring temporary access.
* **BitBucket users with limited-access to repos:** Users that only have limited access to a certain repos in BitBucket.
* **Multiple Git systems:** when users need to be invited to multiple workspaces of different Git systems (combo Github and Gitlab).&#x20;

## Steps to Invite Users <a href="#steps-to-invite-users" id="steps-to-invite-users"></a>

**Step 1**: Navigate to the [Users Section](https://app.aikido.dev/settings/users) in Settings. Click **'Add'** to open the user invite dialogue

**Step 2**: Enter one or multiple **email address**. The email needs to be a company email.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fefc53a1e1b0bb49b00d17d30bec75da3f2da3f5%2Finvite-users-to-aikido-without-a-git-account_dcbbcf0d-b654-4c4d-ad97-ed877b60f8f1.png?alt=media)

**Step 3.** Choose the **second Login Method** - Users can log in via GitHub/Bitbucket/GitLab, Google or Microsoft.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-dbf1fd0c4f7dc8b2a1b5178a6052432fbde5b8c1%2Finvite-users-to-aikido-without-a-git-account_9682a418-4581-46c3-bb07-370ba01aa4ee.png?alt=media)

**Step 4.** Ensure that the invited user clicks the button in the email redirecting to Aikido and then using its email that was used during invite for Google/Microsoft.

### Important Notes <a href="#important-notes" id="important-notes"></a>

* **Manual Offboarding**: Users invited via these methods **will not** be automatically offboarded. It is important to manually remove users who no longer require access to the Aikido platform to maintain security and manage access appropriately.

# Setting Roles and Permissions

## Roles and Permissions Logic <a href="#roles-and-permissions-logic" id="roles-and-permissions-logic"></a>

Aikido offers three distinct user roles (**admins**, **default** and **team-only** users) to manage access and permissions effectively. Default and team-only users can have **standard editing rights** or can be **read-only**.

| Role                | Access Level                                                 |
| ------------------- | ------------------------------------------------------------ |
| **Admins**          | Full access                                                  |
| **Default Users**   | <p>Global / All Teams</p><p>Standard rights or read-only</p> |
| **Team-Only Users** | <p>Team-specific</p><p>Standard rights or read-only</p>      |

### Default Users vs Team-Only Users <a href="#default-users-vs-team-only-users" id="default-users-vs-team-only-users"></a>

The main difference between the two is that team-only users only have access to those issues for the teams they belong to. They still are able to mostly manage issues.

| Permission                                                                           | Default Users | Team-Only Users                                       |
| ------------------------------------------------------------------------------------ | ------------- | ----------------------------------------------------- |
| <p><strong>Issue Actions</strong></p><p>Snooze, ignore, severity change, autofix</p> | ✅             | ✅                                                     |
| **Create Tasks**                                                                     | ✅             | ✅                                                     |
| **Add Repos**                                                                        | ✅             | ❌                                                     |
| **Add Container Registries**                                                         | ✅             | ❌                                                     |
| **Add Domains**                                                                      | ✅             | Connected to repos only. No standalone.               |
| **Export Issues**                                                                    | ✅             | ❌                                                     |
| **Pentests**                                                                         | ✅             | ❌                                                     |
| **Code Quality**                                                                     | ✅             | ❌                                                     |
| **Zen Firewall**                                                                     | ✅             | ❌                                                     |
| **Acces to Settings**                                                                | All settings  | General Settings **Only**                             |
| **Acces to Reports**                                                                 | All Reports   | Trends Over Time, Licenses & SBOM and Malware Monitor |

### Advanced Rights for Users with Standard Rights <a href="#advanced-rights-for-users-with-standard-rights" id="advanced-rights-for-users-with-standard-rights"></a>

Aikido has an extra layer of permissions that can be enabled or disabled (both for default and team-only users). This is helpful in case you still want users to be able to execute certain actions. **Read-only rights block all possible actions.**

**Configurable for Default and Team-Only**

* **Snooze/Ignore Issues**: Ability to temporarily or permanently dismiss issues.
* **Change Issue Severity**: Ability to modify the severity level of issues.
* **Can export data:** Ability to export csv reports of vulnerability issues.

**Limited to Default Users**

* **Manage Teams**: Ability to manage team settings and membership.
* **Manage Repositories:** Ability to change branch, set multi-branch scanning and manage custom SAST rules.
* **Manage Clouds:** Ability to add and configure clouds
* **Manage Containers:** Ability to add and configure containers
* **Manage Domains:** Ability to add and configure domains
* **Manage Pentests:** Ability to run and configure pentests
* **Manage Code Quality Rules:** Ability to add and configure Code Quality Rules & manage code context

## How to change roles and permissions <a href="#how-to-change-roles-and-permissions" id="how-to-change-roles-and-permissions"></a>

**Step 1.** Go to the user overview in your settings

**Step 2.** Click the triple dots to open up the role and permissions modal for a specific user

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cf4b7f2e0972adf8d7be8edaf5ef9bdf997710d3%2Fsetting-roles-and-permissions_3666ec2a-c91c-473f-9352-6c191c51c09b.png?alt=media" alt="" width="563"></div>

**Step 3.** Set the preferred user role and permissions

<div data-full-width="false" data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FzO5WoAYz5yzDF85TIZ0c%2FScreenshot%202025-11-17%20at%2021.47.17.png?alt=media&#x26;token=452bae16-f9a7-43ed-a7f7-152ae3f884e7" alt=""><figcaption></figcaption></figure></div>

# Automated User Management

# GitHub Integration: Authentication and User Management

## Introduction <a href="#introduction" id="introduction"></a>

Aikido ensures a one-to-one mapping with your GitHub organizations, including repositories, and teams. This streamlines the onboarding and offboarding processes within Aikido.

## Understanding Aikido's GitHub Integration <a href="#understanding-aikidos-github-integration" id="understanding-aikidos-github-integration"></a>

* **Automatic Onboarding**: Thanks to the one-to-one mapping with GitHub organizations, all GitHub org members can easily onboard themselves to Aikido workspaces. This eliminates the need for manual email invitations. As soon as a user is part of the GitHub org, they will be able to access the workspace directly.
* **Effortless Offboarding**: When a member is removed from your GitHub organization, they automatically lose access to the Aikido workspace.
* **Synchronization of Teams and Repositories**: Aikido replicates your GitHub team structure and repository access controls. If your GitHub setup involves managing repository access through team memberships, Aikido will automatically and instantly mirror this structure, ensuring access levels remain consistent across both platforms.
* **Instant Syncing**: Instant syncing for adding & removing members, changing teams, changing repos on a team. All changes done in GitHub will instantly be reflected in Aikido.
* **Limitations for Outside Collaborators**: It's important to note that only full members of your GitHub organization can join the Aikido workspace. This means outside collaborators, even though they may have access to your GitHub repositories, will not be granted access to Aikido, ensuring workspace access is limited to your core team. If you want to add these users, you can also invite them via Google/Microsoft (see below).

### Inviting users to Aikido without an organisational GitHub account <a href="#inviting-users-to-aikido-without-an-organisational-github-account" id="inviting-users-to-aikido-without-an-organisational-github-account"></a>

You can invite users via Gmail, Microsoft or using a personal GitHub Account. More information can be [found here.](https://help.aikido.dev/docs/getting-started/automated-user-management/invite-users-to-aikido-without-a-git-account)

# Azure DevOps: Authentication and User Management

If your organization uses Azure DevOps, users can login with Google and Microsoft accounts. To allow auto-onboarding of users in your workspace: configure **Trusted Domains (see below for instructions)**

### Understanding Aikido's Azure DevOps Integration <a href="#understanding-aikidos-azure-devops-integration" id="understanding-aikidos-azure-devops-integration"></a>

* **Manual Onboarding:** invite users manually via email
* **Auto-onboard via Trusted Domains**: Users can automatically join the Azure DevOps workspace if their login email is part of a trusted domain that you can specify on workspace level. Aikido will verify this user has access to your Azure Devops organization. **Note:** the user needs to be a member on the organisation level in Azure, otherwise they will not be recognised during team sync.
* **Synchronization of Teams and Repositories:** Aikido replicates your Azure DevOps team and project structure. All users will have access to their repos, in line with the permissions set in Azure DevOps. By default, all users will have the **Team Only** role.

### Onboarding of Users with Trusted Domains <a href="#onboarding-of-users-with-trusted-domains" id="onboarding-of-users-with-trusted-domains"></a>

{% hint style="info" %}
If you have multiple workspaces, you need to setup Trusted Domains in each workspace.
{% endhint %}

1. Go to [General Settings](https://app.aikido.dev/settings/account) in your workspace
2. In workspace info, click 'Add Trusted Domain'

   ![Azure DevOps Server: Update token and add trusted domains for security.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0122fba6f18348ef9a8b008b25b48f883a5885b2%2Fazure-devops-integration-for-authentication-and-user-management_57ed94d1-4c3f-434b-8db6-b92ef76238e1.png?alt=media)
3. Fill in the trusted domain in the modal

   ![Add a trusted domain for Azure DevOps user auto-enrollment and verification.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a71a6382939034e9f54a9928c311d46d23b94711%2Fazure-devops-integration-for-authentication-and-user-management_36b654cd-1d63-4245-b543-c1a62828fc6c.png?alt=media)

{% hint style="info" %}
For security reasons, Aikido only allows you to add trusted domains that are the same as the current logged in user. This means that <user@aikido.dev> can only add [aikido.dev](http://aikido.dev) as trusted domain.
{% endhint %}

### Manually Inviting Users <a href="#manually-inviting-users" id="manually-inviting-users"></a>

**Manually invite via email**: You can invite users via the Aikido platform on the specified email, and the user will be able to access Aikido directly.

# Bitbucket Cloud Integration: Authentication and User Management

### Introduction <a href="#introduction" id="introduction"></a>

Aikido ensures a one-to-one mapping with this Bitbucket Workspace, including repositories and teams. This streamlines the onboarding and offboarding processes within Aikido.

If you have multiple Bitbucket workspaces, you can connect these by setting up multiple Aikido workspaces.

{% hint style="warning" %}
For automatic onboarding to work, developers need to have **access to all repos**. If you want to give access to a developer with limited access to repos in Bitbucket, we suggest inviting them [via Google/Microsoft](https://help.aikido.dev/docs/getting-started/automated-user-management/invite-users-to-aikido-without-a-git-account).
{% endhint %}

### Benefits <a href="#benefits" id="benefits"></a>

* **Automatic Onboarding:** After initial connection with Bitbucket, all Bitbucket members of this group will be able to onboard Aikido automatically, on the condition they have access to **all repositories** in this Bitbucket workspace.
* **Effortless Offboarding:** Aikido will sync access every night and auto-offboard members that are no longer active in your Bitbucket Workspace. This means that when a member is removed from the Bitbucket Workspace, they automatically lose access to the Aikido Workspace too.
* **Synchronization of Teams:** Aikido replicates your Bitbucket team structure (i.e. User Groups in Bitbucket). Groups need to have access to repositories in order to connect responsibilities of repositories to the teams in Aikido.
* **Daily Syncing**: Currently, Aikido updates the team structures, repositories and access permissions on a daily basis.

### Inviting users to Aikido without an organisational Bitbucket account <a href="#inviting-users-to-aikido-without-an-organisational-bitbucket-account" id="inviting-users-to-aikido-without-an-organisational-bitbucket-account"></a>

You can invite users via Gmail, Microsoft or using a personal Bitbucket Account. This can be helpful when a developer only has limited access in Bitbucket. More information can be [found here.](https://help.aikido.dev/docs/getting-started/automated-user-management/invite-users-to-aikido-without-a-git-account)

# GitLab Integration: Authentication and User Management

### Introduction <a href="#introduction" id="introduction"></a>

When you create an Aikido workspace based on GitLab Cloud version, you select a GitLab Group. The Aikido workspace will consist of the main group and all its subgroups and underlying repositories.

### Benefits <a href="#benefits" id="benefits"></a>

* **Automatic Onboarding:** From that point on, other GitLab members of this group will be able to onboard Aikido automatically. Note: this only on the condition that they have at the least 'reporter', 'developer', 'maintainer' or 'owner' level of access to this group. 'Guests' will not be able to get in.
* **Effortless Offboarding:** When a member is removed from your GitLab Instance, they automatically lose access to the Aikido workspace. Aikido will sync access every night and auto-offboard members that are no longer active in your GitLab instance.

### Adding multiple GitLab Groups in a single Aikido Workspace <a href="#adding-multiple-gitlab-groups-in-a-single-aikido-workspace" id="adding-multiple-gitlab-groups-in-a-single-aikido-workspace"></a>

By default, a new workspace will be created for every GitLab group. If you want to have multiple GitLab groups inside 1 Aikido workspace, you need to create a root-level group in GitLab that contains all the subgroups.

### Inviting users to Aikido without an organisational GitLab account <a href="#inviting-users-to-aikido-without-an-organisational-gitlab-account" id="inviting-users-to-aikido-without-an-organisational-gitlab-account"></a>

You can invite users via Google, Microsoft or using a personal GitLab Account. More information can be [found here.](https://help.aikido.dev/docs/getting-started/automated-user-management/invite-users-to-aikido-without-a-git-account)

# GitLab Self-Managed Integration: Authentication and User Management

### Introduction <a href="#introduction" id="introduction"></a>

If your organization uses GitLab self-managed, it's not possible to authenticate via the Git provider. In those cases, we allow Gmail and Office365 logins.

### Onboarding of Users <a href="#onboarding-of-users" id="onboarding-of-users"></a>

**Manually invite via email (default)**: You can invite users via the Aikido platform on the specified email, and the user will be able to access Aikido directly.

***

**Auto-onboarding**: Aikido can check whether the email that is being used for login is available in the GitLab instance. This is based on adding trusted domains. **Contact us** to help in setting this up or go to your Workspace settings and click 'Add Trusted Domain'.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d95229ed077388c110be7b44fe4ec2efbd616f41%2Fgitlab-self-managed-integration-for-authentication-and-user-management_d7cc579b-0475-45a3-9120-f05797054408.png?alt=media)

{% hint style="info" %}
**​Important notes on auto-onboarding**

* All users will need to have their 'public email' field exposed. Currently, GitLab does not allow yet to force this upon all users ([more info](https://gitlab.com/gitlab-org/gitlab/-/issues/9828)).
* The email used for login and the email in the 'public email' field need to be exactly the same. Aliases are currently not supported.
  {% endhint %}

# SAML Login

# SAML User Rights: Access Profiles (Recommended)

SAML Access Profiles allow you to define user access rights based on SAML attributes. You can manage these profiles in the app under:

**Settings > General > SAML Setup > Add SAML Profile**<https://app.aikido.dev/settings/account>

## Configuring SAML Access Profiles <a href="#configuring-saml-access-profiles" id="configuring-saml-access-profiles"></a>

When adding a new SAML Profile, you can define the following settings:

### 1. Profile Name <a href="#id-1-profile-name" id="id-1-profile-name"></a>

* The name that should be passed as the `aikido_access_profile` SAML claim.

### 2. Role <a href="#id-2-role" id="id-2-role"></a>

* Defines the user's role:
  * **Admin**
  * **Default**
  * **Team Only**

### 3. Edit Rights <a href="#id-3-edit-rights" id="id-3-edit-rights"></a>

* Determines the user's edit capabilities:
  * **Standard**
  * **Read Only**

### 4. Can Ignore <a href="#id-4-can-ignore" id="id-4-can-ignore"></a>

* Specifies whether the user can ignore issues:
  * **Yes**
  * **No**

### 5. Can Snooze <a href="#id-5-can-snooze" id="id-5-can-snooze"></a>

* Specifies whether the user can snooze issues:
  * **Yes**
  * **No**

### 6. Can Change Severity <a href="#id-6-can-change-severity" id="id-6-can-change-severity"></a>

* Defines if the user can change the severity of issues:
  * **Yes**
  * **No**

### 7. Can Export Data <a href="#id-7-can-manage-teams" id="id-7-can-manage-teams"></a>

* Defines if the user can export data:
  * **Yes**
  * **No**

### 8. Can Manage Teams <a href="#id-7-can-manage-teams" id="id-7-can-manage-teams"></a>

* Defines if the user can manage teams:
  * **Yes**
  * **No**

### 9. Can Manage Clouds <a href="#id-7-can-manage-teams" id="id-7-can-manage-teams"></a>

* Defines if the user can manage clouds:
  * **Yes**
  * **No**

### 9. Can Manage Containers <a href="#id-7-can-manage-teams" id="id-7-can-manage-teams"></a>

* Defines if the user can manage containers:
  * **Yes**
  * **No**

### 10. Can Manage Domains <a href="#id-7-can-manage-teams" id="id-7-can-manage-teams"></a>

* Defines if the user can manage domains:
  * **Yes**
  * **No**

### 11. Can Manage Pentests <a href="#id-7-can-manage-teams" id="id-7-can-manage-teams"></a>

* Defines if the user can manage pentests:
  * **Yes**
  * **No**

### 12. Can Manage Code Quality Rules <a href="#id-7-can-manage-teams" id="id-7-can-manage-teams"></a>

* Defines if the user can manage code quality rules:
  * **Yes**
  * **No**

### 13. Member of Teams <a href="#id-8-member-of-teams" id="id-8-member-of-teams"></a>

* A comma-separated list of team names the user belongs to.
* Matches the existing `aikido_teams` [SAML claim](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-using-custom-attributes-advanced).

### 14. Workspace IDs <a href="#id-9-workspace-ids" id="id-9-workspace-ids"></a>

* A comma-separated list of workspace IDs where the user has access.
* Matches the existing `aikido_workspace_ids` [SAML claim](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-using-custom-attributes-advanced).
* If left empty, the profile grants access to all workspaces linked to the SAML client.

## Using SAML Access Profiles <a href="#using-saml-access-profiles" id="using-saml-access-profiles"></a>

Once a profile is created, you can set up a custom SAML claim `aikido_access_profile` with the profile name as value. **If set**, users who authenticate via SAML will receive access based on the profile associated with this claim. Ensure that the correct claims are configured in your Identity Provider (IdP) to match the assigned profiles.

> **Note**
>
> When using the `aikido_access_profile` in combination with other [custom SAML claims](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-using-custom-attributes-advanced), those other claims will take precedence.

# SAML User Rights: Custom Attributes (Advanced)

> These are the advanced way of setting up user rights. We recommend using [SAML Access Profiles](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)
>
> [https://help.aikido.dev/doc/saml-user-rights-access-profiles-recommended/docVaVb0VPy1](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)

This guide provides detailed instructions on how to configure and manage user rights within Aikido using SAML custom attributes. By leveraging attributes such as `aikido_role`, `aikido_data_edit_rights`, `aikido_can_ignore`, `aikido_can_snooze`, `aikido_can_change_severity`, `aikido_can_manage_teams`, and `aikido_teams`, you can control user permissions and roles from within your identity provider. This approach ensures that users have the same access in Aikido as set up in your identity provider.

* **aikido\_access\_profile:** [**More info**](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)\
  When setting up SAML Access Profiles, this is the claim to use.

  ```xml
  <saml:Attribute Name="aikido_access_profile">
      <saml:AttributeValue xsi:type="xs:anyType">My Access Profile</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_username:** You can define the name of the user in Aikido

  ```xml
  <saml:Attribute Name="aikido_username">
      <saml:AttributeValue xsi:type="xs:anyType">John Doe</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_role:** `admin`, `default`, `team_only`

  ```xml
  <saml:Attribute Name="aikido_role">
      <saml:AttributeValue xsi:type="xs:anyType">default</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_data\_edit\_rights:** `standard`, `read_only`

  ```xml
  <saml:Attribute Name="aikido_data_edit_rights">
      <saml:AttributeValue xsi:type="xs:anyType">standard</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_ignore:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_ignore">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_snooze:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_snooze">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_change\_severity:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_change_severity">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_manage\_teams:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_manage_teams">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_export\_data:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_export_data">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_manage\_clouds:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_manage_clouds">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_manage\_containers:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_manage_containers">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_manage\_domains:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_manage_domains">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_manage\_pentests:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_manage_pentests">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_can\_manage\_code\_quality:** `true`, `false`

  <pre class="language-xml"><code class="lang-xml">&#x3C;saml:Attribute Name="aikido_can_manage_code_quality">
  <strong>    &#x3C;saml:AttributeValue xsi:type="xs:anyType">true&#x3C;/saml:AttributeValue>
  </strong>&#x3C;/saml:Attribute>
  </code></pre>
* **aikido\_teams:** You can define the different teams where the user is a part of here. If the team(s) do not exist in Aikido, it will be created. The user will auto-join these given teams. The user will be removed from all other teams if this is set up.

  ```xml
  <saml:Attribute Name="aikido_teams">
      <saml:AttributeValue xsi:type="xs:anyType">team1</saml:AttributeValue>
      <saml:AttributeValue xsi:type="xs:anyType">team2</saml:AttributeValue>
  </saml:Attribute>
  ```

* **aikido\_workspace\_ids:** You can define the different Aikido workspaces where the user is a part of here. The user will auto-join these given workspaces. The user will be removed from all other workspaces if this field is set up.

  ```xml
  <saml:Attribute Name="aikido_workspace_ids">
      <saml:AttributeValue xsi:type="xs:anyType">1233</saml:AttributeValue>
      <saml:AttributeValue xsi:type="xs:anyType">2511</saml:AttributeValue>
  </saml:Attribute>
  ```

* **github\_user\_id:** You can define the ID of the user in GitHub or GitHub Enterprise Server. This field will ensure that the user is linked to the appropriate imported team from GitHub.

  ```xml
  <saml:Attribute Name="github_user_id">
      <saml:AttributeValue xsi:type="xs:anyType">1233</saml:AttributeValue>
  </saml:Attribute>
  ```

# Okta: Login with SAML

{% hint style="info" %}
This feature is only available on a **paying** plan and is not enabled by default. If you’d like to enable this feature, please reach out via the chat in the bottom right corner within Aikido.
{% endhint %}

> If you switch to SAML Login instead of auto-onboarding via your Git provider, team import from GitHub, Bitbucket, or Azure DevOps will no longer work. You will need to manage your teams manually moving forward, either through the Aikido UI or [Access Profiles.](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)

## Setting up SAML in your account <a href="#setting-up-saml-in-your-account" id="setting-up-saml-in-your-account"></a>

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Workspace info page showing option to enable SAML authentication for a GitHub account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-52bef8060e16dc93c85e5a6c3a75db646ff32e9a%2Fokta-login-with-saml_cd9146ff-36d4-4839-a879-0092907a7019.png?alt=media)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![SAML Authentication setup screen with required URLs and Name ID format for configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6a282e9f1b96450fcddfcafe2bb9f1476210c99c%2Fokta-login-with-saml_01f94720-00dc-4d8f-95a3-887c7546433b.png?alt=media)

### Continue in Okta <a href="#continue-in-okta" id="continue-in-okta"></a>

**Step 1.** Go to **Applications** > **Applications** in the Admin Console.

**Step 2.** Click **Create App Integration**, select **SAML 2.0** and click **Next**.

**Step 3.** Choose an **App name** and click **Next**.

**Step 4.** Fill the fields **Single sign-on URL**, **Audience URI** and **Name ID format** with the fields visible in Aikido (see above) and click **Next**.

**Step 5.** Now you should be on the tab **Sign On** and you should see **Metadata details**. Click **More details**.

### Go back to Aikido <a href="#go-back-to-aikido" id="go-back-to-aikido"></a>

* Fill in the **Entity ID / Issuer**, **Single Sign-On URL** and **X.509 Certificate** as shown in Okta.
* Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![Form for entering SAML authentication details for secure single sign-on setup.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-851c3a7f92d35b9f083ce8fc28190e0b53544b85%2Fokta-login-with-saml_bf648fe2-3f42-4490-9067-3840392e84f9.png?alt=media)

> Success! People having access to your Okta SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client <a href="#id-2-options-for-users-to-login-using-your-saml-client" id="id-2-options-for-users-to-login-using-your-saml-client"></a>

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![SAML Authentication settings with options to manage or copy the login link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c359002b6002f1c6d80bd9683f7eaf4f8808d1c3%2Fokta-login-with-saml_b6d1fe83-fa12-410c-b6de-77ac12f0f41b.png?alt=media)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![One-click free login and sign-up with Google, Microsoft, or SSO—no card required.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2bfbc01b8c5f3ac8d7bc3a12a695819f8f89a2c7%2Fokta-login-with-saml_c233b6e3-7de6-40fe-b58c-8e6414a89556.png?alt=media)

![Login screen with Google, Microsoft, and email authentication options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-911aa517b4f1102384e77de360b476ca88642232%2Fokta-login-with-saml_4e595972-8a51-4473-956b-7da0b4fd41fa.png?alt=media)

# JumpCloud: Login with SAML

{% hint style="info" %}
This feature is only available on a **Pro** or **Advanced** plan and is not enabled by default. If you’d like to enable this feature, please reach out via the chat in the bottom right corner within Aikido.
{% endhint %}

> If you switch to SAML Login instead of auto-onboarding via your Git provider, team import from GitHub, Bitbucket, or Azure DevOps will no longer work. You will need to manage your teams manually moving forward, either through the Aikido UI or [Access Profiles.](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)

## Setting up SAML in your account <a href="#setting-up-saml-in-your-account" id="setting-up-saml-in-your-account"></a>

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Workspace info page with option to enable SAML authentication.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-52bef8060e16dc93c85e5a6c3a75db646ff32e9a%2Fjumpcloud-login-with-saml_e1fd0c18-f548-4071-919d-67e1fac297ec.png?alt=media)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![SAML authentication setup screen with required URLs and Name ID format.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d0f87c55a3ce6f0dca79d576308678a1d33cf8d3%2Fjumpcloud-login-with-saml_09a7d874-2d07-4f24-b41c-83eb4ae62a50.png?alt=media)

### Continue in JumpCloud <a href="#continue-in-jumpcloud" id="continue-in-jumpcloud"></a>

**Step 1.** Go to **User Authentication** > **SSO Applications** in the JumpCloud Admin Portal navigation.

**Step 2.** Click the **Add New Application** and search for **SAML 2.0**. Click **Next**.

**Step 3.** Choose a **Display Label** and click **Save Application**.

**Step 4.** Click **Configure Application**.

**Step 5.** Click on the **SSO** tab and fill following fields:

* **Idp Entity ID:** `https://console.jumpcloud.com/<appname>`
* **SP Entity ID:** `https://app.aikido.dev/saml`
* **ACS URLs** - **Default URL:** `https://app.aikido.dev/api/saml/saml_auth?samlClientId=...` (As shown in Aikido)
* **SAMLSubject NameID:** `email`
* **SAMLSubject NameID Format:** `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`
* **Signature Algorithm:** `RSA-SHA256`
* **Default RelayState:** You can leave this empty

![SAML 2.0 single sign-on configuration settings for secure identity management integration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-eff061b095b5f561245505a012f6875e2e63d38a%2Fjumpcloud-login-with-saml_05b8da4a-cc77-4099-856c-70e00b369a45.png?alt=media)

**Step 6.** We'll continue in Aikido, but you might as well click **Save** and come back to this screen.

### Go back to Aikido <a href="#go-back-to-aikido" id="go-back-to-aikido"></a>

* Fill in the:
  * **Entity ID / Issuer:** `https://console.jumpcloud.com/<appname>` (Make sure this matches what you've entered as **Idp Entity ID** in JumpCloud. If you're having issues with this, see the Troubleshooting section at the bottom)
  * **Single Sign-On URL:** as shown in JumpCloud under **IDP URL**. (looks like `https://sso.jumpcloud.com/saml2/<appname>`)
  * **X.509 Certificate**: This can be fetched in different ways. One way is to click **Export Metadata** in JumpCloud the config and open the downloaded xml. You'll find your certificate between the `ds:X509Certificate` tags.
* Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![SAML Authentication setup form for configuring identity provider details.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-851c3a7f92d35b9f083ce8fc28190e0b53544b85%2Fjumpcloud-login-with-saml_282cde57-79ed-4aab-bddb-bd4073327ee6.png?alt=media)

> Success! People having access to your JumpCloud SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client <a href="#id-2-options-for-users-to-login-using-your-saml-client" id="id-2-options-for-users-to-login-using-your-saml-client"></a>

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![SAML Authentication settings with options to manage or copy the login link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c359002b6002f1c6d80bd9683f7eaf4f8808d1c3%2Fjumpcloud-login-with-saml_13d717d7-9d5e-4dd1-ab34-4d5b6455f475.png?alt=media)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![One-click login and sign-up with Google, Microsoft, or SSO—no credit card needed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2bfbc01b8c5f3ac8d7bc3a12a695819f8f89a2c7%2Fjumpcloud-login-with-saml_ca4791cb-4534-471c-8757-b2dc3ca7e569.png?alt=media)

![Login screen with Google, Microsoft, and email login options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-911aa517b4f1102384e77de360b476ca88642232%2Fjumpcloud-login-with-saml_ff9dd4af-ca57-484d-aacb-ed9cbe5aad7d.png?alt=media)

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

**Error**

![SAML client already exists error; prompts user to contact support for linking organization.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fde2154e1f44785ccbde15520e03afb67162f2c8%2Fjumpcloud-login-with-saml_5f7761f9-08db-4072-8559-0567d1bfc719.png?alt=media)

**Solution**

Make sure the **Idp Entity ID** is unique. Perhaps you could change it to `https://console.jumpcloud.com/<samlClientId>`. Note that you'll also need to change it in Aikido in **Entity ID / Issuer** as these should match.

# Google Workspaces: Login with SAML

{% hint style="info" %}
This feature is only available on a **Pro** or **Advanced** plan and is not enabled by default. If you’d like to enable this feature, please reach out via the chat in the bottom right corner within Aikido.
{% endhint %}

> If you switch to SAML Login instead of auto-onboarding via your Git provider, team import from GitHub, Bitbucket, or Azure DevOps will no longer work. You will need to manage your teams manually moving forward, either through the Aikido UI or [Access Profiles.](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)

### Setting up SAML in your account <a href="#setting-up-saml-in-your-account" id="setting-up-saml-in-your-account"></a>

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Workspace info page showing option to enable SAML authentication.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-52bef8060e16dc93c85e5a6c3a75db646ff32e9a%2Fgoogle-workspaces-login-with-saml_6bb8581e-5aab-49a3-8ce8-4b5f13a49749.png?alt=media)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![SAML Authentication setup screen with required URLs and Name ID format fields.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d0f87c55a3ce6f0dca79d576308678a1d33cf8d3%2Fgoogle-workspaces-login-with-saml_131b2923-631f-42e8-af65-87faa35c50e0.png?alt=media)

### Continue in Google <a href="#continue-in-google" id="continue-in-google"></a>

**Step 1.** Go to **Apps** > **Web and mobile apps** in the Google Admin Console.

**Step 2.** Click the **Add app** dropdown and select **Add custom SAML app**.

**Step 3.** Choose an **App name** and click **Continue**.

**Step 4.** Ignore the metadata page for now, we'll get this information later on. Click **Continue**.

**Step 5.** Fill the fields **ACS URL**, **Entity ID** and **Name ID format** with the fields visible in Aikido (see above) and click **Continue** and click **Finish**.

**Step 6.** Now you should be on the detail page of your newly created app. Click **Download Metadata**.

### Go back to Aikido <a href="#go-back-to-aikido" id="go-back-to-aikido"></a>

* Fill in the **Entity ID / Issuer**, **Single Sign-On URL** and **X.509 Certificate** as shown in the modal in Google.
* Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![SAML authentication setup form requiring identity provider and company domain details.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-851c3a7f92d35b9f083ce8fc28190e0b53544b85%2Fgoogle-workspaces-login-with-saml_33ba5a40-204e-4c76-8a85-971b8115c30b.png?alt=media)

> Success! People having access to your Google SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client <a href="#id-2-options-for-users-to-login-using-your-saml-client" id="id-2-options-for-users-to-login-using-your-saml-client"></a>

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![SAML Authentication settings with options to manage or copy the login link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c359002b6002f1c6d80bd9683f7eaf4f8808d1c3%2Fgoogle-workspaces-login-with-saml_d44ce4f2-726b-4108-b8d5-bb83c49b1490.png?alt=media)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![One-click login and sign-up with Google, Microsoft, or SSO—no credit card needed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2bfbc01b8c5f3ac8d7bc3a12a695819f8f89a2c7%2Fgoogle-workspaces-login-with-saml_fa842428-89f5-4aa8-91a4-56cc2a7533eb.png?alt=media)

![Login options: Google, Microsoft, or email for account access.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-911aa517b4f1102384e77de360b476ca88642232%2Fgoogle-workspaces-login-with-saml_2ec57086-151e-48f9-ab55-0c1ac60cafb1.png?alt=media)

# Microsoft Azure: Login with SAML/ Entra ID

{% hint style="info" %}
This feature is only available on a **Pro** or **Advanced** plan and is not enabled by default. If you’d like to enable this feature, please reach out via the chat in the bottom right corner within Aikido.
{% endhint %}

> If you switch to SAML Login instead of auto-onboarding via your Git provider, team import from GitHub, Bitbucket, or Azure DevOps will no longer work. You will need to manage your teams manually moving forward, either through the Aikido UI or [Access Profiles.](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)

## Setting up SAML in your account <a href="#setting-up-saml-in-your-account" id="setting-up-saml-in-your-account"></a>

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Workspace info screen with option to enable SAML authentication for GitHub account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-52bef8060e16dc93c85e5a6c3a75db646ff32e9a%2Fmicrosoft-azure-login-with-saml-entra-id_226233e4-b7ed-4614-a3c7-2316aa00830e.png?alt=media)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![SAML Authentication setup screen showing required URLs and Name ID format for configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d0f87c55a3ce6f0dca79d576308678a1d33cf8d3%2Fmicrosoft-azure-login-with-saml-entra-id_af05c8a1-f44f-499c-85a3-40090e79ede6.png?alt=media)

### Continue in Azure <a href="#continue-in-azure" id="continue-in-azure"></a>

**Step 1.** Go to **Microsoft Entra ID**.

**Step 2.** Click the **Add** dropdown and select **Enterprise application**.

![Adding a new enterprise application in Microsoft Azure Active Directory.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-be0bbc97894a04cf73d8b8813002f0a18089e255%2Fmicrosoft-azure-login-with-saml-entra-id_e2b0c97b-cd57-473d-a88b-ae86bae5f17e.jpg?alt=media)

**Step 3.** Click **Create your own application**, choose a name for your app and select 'Non-gallery'.

![Creating a custom non-gallery application named "Aikido-SSO" for integration purposes.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a593f1ffb0e6d737d0e15ce4ee98ab5cf9ef961%2Fmicrosoft-azure-login-with-saml-entra-id_34300cbc-6836-46d3-bcda-326d3726eaac.jpg?alt=media)

**Step 4.** Select **Set up single sign on**.

![Aikido-SSO application setup: Assign users and configure single sign-on in Microsoft Entra.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-071fa54e26d712a8a8ec61ff1ff343618ac94105%2Fmicrosoft-azure-login-with-saml-entra-id_041ab86f-83f5-4f7d-b318-3a5e4b8a4fdb.jpg?alt=media)

**Step 5.** Click the **SAML** option.

![Enable SAML single sign-on for secure application authentication in Aikido-SSO.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-adb03664c9535a4fbc72aff1305439f6e3de55d4%2Fmicrosoft-azure-login-with-saml-entra-id_1659ec2c-7283-426d-894c-48ef502505ec.jpg?alt=media)

**Step 6.** On **step 1**, click **Edit.**

![Basic SAML Configuration: Edit required Identifier and Reply URL fields.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e19ceee608639777d51f0504d6bd8cd3489dfadf%2Fmicrosoft-azure-login-with-saml-entra-id_62185eb3-6a97-427b-b914-3a1ec840b54c.jpg?alt=media)

**Step 7.** Fill in the **Entity ID** and **ACS URL** as shown in Aikido.

![Configuration screen for SAML SSO with Entity ID and Reply URL fields specified.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-61508f5f6273b02030c7226c9cd8e74525d7a8f6%2Fmicrosoft-azure-login-with-saml-entra-id_b29695e0-9d2a-4f64-9a88-e30172e85348.jpg?alt=media)

**Step 8.** At **step 2**, click **Edit.**

![User attributes and claims mapping with editable options highlighted.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5dcf9aa3540b381c1af5bf5383478aa4ac7d0836%2Fmicrosoft-azure-login-with-saml-entra-id_0cc0859a-2fbd-4ca9-9442-c8114c034d3b.jpg?alt=media)

**Step 9.** Click the **Unique User Identifier (Name ID)**.\
Optional: clicking 'Add new claim' at the top of this page allows you to add [custom attributes](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/saml-user-rights-using-custom-attributes-advanced) to SAML. More info [here](https://help.aikido.dev/doc/microsoft-azure-custom-attributes-with-saml--entra-id/docFaysVwVZy).

![Highlighted SAML claim: Unique User Identifier (Name ID) for user identification.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9bb311d72ded942631541250588a40360249a636%2Fmicrosoft-azure-login-with-saml-entra-id_c58d21d6-7556-43db-96eb-3f2b81663b8d.jpg?alt=media)

**Step 10.** Make sure to set **Source attribute** to `user.mail` here.

![Configuring a SAML claim for user email as the name identifier in Azure AD.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5a86243ee8598d6afe63a05a23b910836aed9038%2Fmicrosoft-azure-login-with-saml-entra-id_7359629d-6b9b-4c7a-822a-46ddb14ae30e.jpg?alt=media)

**Step 11.** At step 3 you can download the **Certificate (Base64)** & at step 4 you'll see the **Login URL** and **Mircosoft Entra Identifier**. These should be copy and pasted to Aikido.

### Go back to Aikido <a href="#go-back-to-aikido" id="go-back-to-aikido"></a>

* Fill in the **Entity ID / Issuer**, **Single Sign-On URL** and **X.509 Certificate** as shown in Azure.
* Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![SAML Authentication setup form for configuring Single Sign-On (SSO) credentials.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-851c3a7f92d35b9f083ce8fc28190e0b53544b85%2Fmicrosoft-azure-login-with-saml-entra-id_ecd63576-b9c5-464a-ae53-3bbb1494f534.png?alt=media)

> Success! People having access to your Azure SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client <a href="#id-2-options-for-users-to-login-using-your-saml-client" id="id-2-options-for-users-to-login-using-your-saml-client"></a>

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![SAML Authentication settings with options to manage or copy the login link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c359002b6002f1c6d80bd9683f7eaf4f8808d1c3%2Fmicrosoft-azure-login-with-saml-entra-id_bf7e0490-bc80-42f3-8517-805537105a8d.png?alt=media)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![One-click login and sign-up with Google, Microsoft, or SSO; no credit card needed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2bfbc01b8c5f3ac8d7bc3a12a695819f8f89a2c7%2Fmicrosoft-azure-login-with-saml-entra-id_a72d4e17-3465-4a72-bd1b-5b15115eb4da.png?alt=media)

![Login screen offering Google, Microsoft, or email sign-in options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-911aa517b4f1102384e77de360b476ca88642232%2Fmicrosoft-azure-login-with-saml-entra-id_9ad5fafb-e1f7-4ac8-b3b7-37d4639c046d.png?alt=media)

# Microsoft Azure: Custom Attributes with SAML /Entra ID

First, make sure you have SAML login working using following guide:

[https://help.aikido.dev/doc/microsoft-azure-login-with-saml--entra-id/doc74BfKR60Z](https://help.aikido.dev/docs/getting-started/automated-user-management/saml-login/microsoft-azure-login-with-saml-entra-id)

### Setting up Azure Group based SAML custom attributes <a href="#setting-up-azure-group-based-saml-custom-attributes" id="setting-up-azure-group-based-saml-custom-attributes"></a>

1. Go to the application registration

   ![Azure portal view for managing Aikido-SSO enterprise application properties and settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8ae302f9235687b459c2ba2701289c48f38f2aa0%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_62b626cc-9385-45bc-9fff-35344531e015.jpg?alt=media)
2. Create an app role.**value** here should be the value of the claim. In this example, we're setting up for `aikido_role`, so valid values for this are `admin`, `default`, `team_only`.

   ![Creating a new app role "Aikido Admin" in Microsoft Azure for Aikido-SSO.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-78e993105cc638717163210b2b3a28878554aa15%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_88ff497f-e551-4c8e-8abb-445c5d69bf5a.jpg?alt=media)
3. After saving, go back to the app settings, and add a group to 'Users and Groups'

   ![Azure portal: Assign users or groups to the Aikido-SSO enterprise application.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0faef4fdf1540f2b60462f4241e99cf71d8e5ffb%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_1e4e94af-0c14-4f6f-81a9-30c75166cf58.png?alt=media)
4. Add the Entra group you'd like to give admin access (in this case) and add the role we created in step 2.

   ![Azure Add Assignment: Select users, groups, and roles for directory permissions.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a11449ba5258733300a9c54341186ed6376fb916%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_8e32309f-84be-45d0-87d6-972bb1857a3a.png?alt=media)
5. Back in the Single Sign-on settings of the app, go to the Attributes & Claims -> Edit

   ![Azure portal SAML-based single sign-on configuration for Aikido-SSO application.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a05c51da649be812679cfc6144889782075725d9%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_ffa0ee52-da46-4747-8542-2cddee420427.png?alt=media)
6. Click 'Add new claim'

   ![Azure portal Attributes & Claims page for adding and managing SAML claims.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7cd3122ee7a99d6a9941025423a70b7812407d34%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_e7012a33-19d0-4a01-9a12-f17231dff1e4.png?alt=media)
7. Fill in the attribute name & user.assignedroles as source attribute. (this is the `admin` value we set up in step 2)

   ![Azure claim setup: mapping "aikido\_role" to "user.assignedroles" attribute.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e9f3c593cdd24ba6b70e09564291cedf58661d9d%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_02e6788a-d5d8-4bc8-b2c8-7f3371441391.png?alt=media)
8. All done. On SAML login, these changes will take effect.

# Manage Teams & Applications

# Managing User Access with Teams

## Introduction <a href="#introduction" id="introduction"></a>

Aikido lets you create teams, connect multiple repositories and clouds, and manage access using RBAC (Role-Based Access Control) for better security. This article focuses on Managing of User Access. If you are looking to use Teams to group your resources into Projects or Apps, please [**click here**](https://help.aikido.dev/docs/getting-started/manage-teams-and-applications/manage-and-view-your-apps-and-projects-via-our-teams-feature).

## Use Cases <a href="#use-cases" id="use-cases"></a>

* **Selective Access Control:** Assign repository access exclusively to designated team members.
* **Filter Repositories Quickly:** In companies with multiple teams, each team may have access to the entire codebase, but their primary responsibilities are often limited to specific repositories or projects. By creating teams in Aikido, team members **can have a focused overview** of only the repositories relevant to their tasks.\
  ​

  ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4bb2f109bd2129819846da01466f592e79b2c0e0%2Fmanaging-user-access-with-teams_e47c7d0e-a0e8-40db-9c28-dd5ab925c8c5.png?alt=media)
* **Better overview when using a monorepo split.** You can assign team members to specific directories of your monorepo, improving their overview. More information on splitting monorepositories can be found [here](https://help.aikido.dev/en/articles/9026666-splitting-up-your-monorepo-per-directory).

## How To Create Teams <a href="#how-to-create-teams" id="how-to-create-teams"></a>

**Step 1:** Navigate to **Settings -> Teams**\
​

![Team dashboard showing user "mdschuym" with 4 active repositories and 1 member.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0b18ccf8b33376a81bcb2be0b155c8ea75bf054a%2Fmanaging-user-access-with-teams_eb9c5cc9-fe18-4fda-8040-d68dc275f186.png?alt=media)

**Step 2:** Click **Create Team** and give your team a name

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2df987cb28febd5270a9e0f37b72b13d15f2eaee%2Fmanaging-user-access-with-teams_2713e19f-5433-435b-b10b-9f1aa409950e.png?alt=media)

**Step 3:** **Add team members** to the newly created team.

![User management interface showing available users and team assignment options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-360a0c5347426b99a212daa1a65be6b91a03be63%2Fmanaging-user-access-with-teams_59d4a227-bdc5-4880-a1de-4fcb3da51294.png?alt=media)

**Step 4:** Define the **team's responsibilities** by adding **resources via the responsibility tab.** You can add different resources such as clouds, repositories, containers, domains and zen apps.

> If you want to link specific domains to a team, you can set this up by linking your domains to a repo or container. It will automatically inherit access permissions.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FuyEJzLnw6eQHoLdBUAiw%2FScreenshot%202025-12-15%20at%2016.21.52.png?alt=media\&token=ce29fb76-f6bc-4401-a7e3-e81bd279ef20)

**Step 5.** Go back to your feed and filter on a specific team. You should only see issues that are related to those repositories and clouds that were attached to the team.

## Syncing with GitHub, Bitbucket or Azure DevOps <a href="#syncing-with-github-bitbucket-or-azure-devops" id="syncing-with-github-bitbucket-or-azure-devops"></a>

If you have **existing teams** set up in GitHub, Bitbucket or Azure DevOps, Aikido will import them and maintain synchronization on a nightly basis. This ensures that any changes in team structures or access rights managed in GitHub/Bitbucket are accurately reflected in Aikido. Any new teams that are created in GitHub will appear in Aikido. The same applies to when you remove a team in GitHub: Aikido will pick this up and remove the team too. Any repos that are part of the team, will be synced too.

{% hint style="info" %}
It's important to note that in this scenario, GitHub/Bitbucket/Azure DevOps acts as the source of truth for access rights, and all management should be conducted within those platforms. This also means that **no extra users can be added to scm-linked teams** inside Aikid&#x6F;**.**
{% endhint %}

Aikido makes it clear which teams have been imported from your SCM.

![Team roles and users overview with DevOps group imported from GitHub.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7f3ddad0a51238cf01f2b9d4ccf619c5ac7995bf%2Fmanaging-user-access-with-teams_0ab4ee09-6b7d-48ee-a435-b20c98ff18d6.png?alt=media)

## Syncing with Backstage.io <a href="#syncing-with-backstageio" id="syncing-with-backstageio"></a>

Aikido integrates seamlessly with repositories containing `catalog-info.yaml` files for [Backstage.io](https://backstage.io). This allows for the automatic importing of teams, taking into account the path of where the file is located.

{% hint style="info" %}
Please note: This feature needs to be enabled by Aikido manually. Please reach out to support to enable this.
{% endhint %}

#### How It Works <a href="#how-it-works" id="how-it-works"></a>

1. Aikido scans repositories for `catalog-info.yaml` files.
2. Aikido looks for the `spec->owner` field in the file and imports this as team.
3. Aikido records the exact path of each `catalog-info.yaml` file, ensuring the team is responsible for those specific paths (and repositories).

## Syncing with Port.io <a href="#syncing-with-backstageio" id="syncing-with-backstageio"></a>

Aikido integrates seamlessly with repositories containing `port.yaml` files for [Port.io](https://port.io). This allows for the automatic importing of teams, taking into account the path of where the file is located.

#### How It Works <a href="#how-it-works" id="how-it-works"></a>

1. Aikido scans repositories for `port.yaml` files.
2. Aikido looks for the `team` field in the file and imports this as team.
3. Aikido records the exact path of each `port.yaml` file, ensuring the team is responsible for those specific paths (and repositories).

## How to select your team in UI <a href="#how-to-select-your-team-in-ui" id="how-to-select-your-team-in-ui"></a>

**Aikido's Feed** features a **team filter** at the top of the page. This filter allows users to tailor the feed to display only the issues relevant to selected teams. This filter can be used on basically every page in Aikido (feed, reports, settings etc).

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-61296e08665b9c3e6e29330ab62bf16a1916b53d%2Fmanaging-user-access-with-teams_1c6dccbd-d42b-46d0-afb8-741ac1a85163.png?alt=media)

# Assigning Resources to Teams

Assigning resources to teams defines ownership inside Aikido. It ensures that findings are routed to the right people, dashboards stay relevant, and teams only see what they are responsible for.

This page explains all available ways to assign resources, including individual and bulk options.

### Assign from the Team Page

1. Go to [Settings → Teams](https://app.aikido.dev/settings/teams)
2. Select a team
3. Open the Responsibility tab

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FZu4AiAtPf48AR1Rwf1LA%2FScreenshot%202026-02-23%20at%2011.45.39.png?alt=media&#x26;token=255dde11-a62d-4e75-9028-2ece67f08e5a" alt=""><figcaption></figcaption></figure>
4. Click "Link Resource"
5. Select resource type, and search and add resources<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F6lBS6KejQUT885j598Jm%2FScreenshot%202026-03-10%20at%2011.38.31.png?alt=media&#x26;token=4fd2e7c3-c13d-4475-ba7f-49493d856939" alt="" width="563"><figcaption></figcaption></figure>

### Assign from the Resource Page

You can also assign a team while viewing the resource itself.

#### Repositories

Open a Repository → Configure → Teams responsible

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FIBphGT7Vm07ANtO9GsAJ%2FLanguageTool_Overlay.png?alt=media&#x26;token=65470eba-cd61-4fdc-aa0d-a4900aa73f97" alt=""><figcaption></figcaption></figure>

#### Cloud Accounts

Open a Cloud Connection → Configure → Teams responsible

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F5bW7TDTZNYNeWS31ZkKS%2FLanguageTool_Overlay.png?alt=media&#x26;token=7251d5fd-e33a-496e-a809-5c06b5854607" alt=""><figcaption></figcaption></figure>

### Domains & API's

Open the Front-end, REST, or GraphQL scan configuration from the Settings page (or the action menu in the list view) and link the domain to an asset.

You can link it to either a repository or a container. Once linked, the scan inherits the team permissions from that asset.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FLUDN9XokEfkVrdqOJOIe%2FScreenshot%202026-02-25%20at%2019.05.11.png?alt=media&#x26;token=5a95e5c3-45f3-4a0f-90c2-a9300bda6bc3" alt=""><figcaption></figcaption></figure>

### Bulk Assignment

Bulk actions are available on resource list pages in [settings](https://app.aikido.dev/settings/account).

{% hint style="info" %}
If bulk actions are not visible, assignment must be done individually.
{% endhint %}

**Repositories**

[Settings → Repositories](https://app.aikido.dev/settings/integrations/repositories) → Select multiple → Bulk Actions → Assign to team

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FI5Rav0nqk14UtdB1Qz5K%2FLanguageTool_Overlay.png?alt=media&#x26;token=db3bd019-72cd-432f-846a-408c0be4d8b5" alt=""><figcaption></figcaption></figure>

**Containers**

[Settings → Containers](https://app.aikido.dev/settings/container-image-registry) → Select multiple → Bulk Actions → Assign to team

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F1jltOtRF87i8totb0kgy%2FScreenshot_23_02_2026__11_57.png?alt=media&#x26;token=6cebb8f3-ab14-43cc-b39c-0eabd7bc1ed7" alt=""><figcaption></figcaption></figure>

# Manage and View Your Apps and Projects via Our Teams Feature

## Introduction <a href="#introduction" id="introduction"></a>

Aikido lets you create teams, connect multiple repositories and clouds to have a clear overview of your apps and projects. This project/app view is available throughout the entire Aikido app, going from feed, alerting and reporting. This article focuses on using Teams in order to group resources into Project and Apps. Managing of User Access. If you are looking to manage User Access with teams, please [**click here**](https://help.aikido.dev/docs/getting-started/manage-teams-and-applications/managing-user-access-with-teams).

## Use Cases <a href="#use-cases" id="use-cases"></a>

* **Agency Project Management:** Agencies frequently handle multiple clients, necessitating a structured approach to manage each client's repositories separately. Aikido facilitates this by allowing the creation of teams for each client, making it straightforward to organize and access client-specific repositories. Additionally, this allows for easy generation of client-specific reports.

  ![Dropdown menu for selecting "All teams" or individual client teams.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fc75651468dd17ae319af297704658fc64a26e34%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_a746b534-b6eb-4c21-bbdc-1265ab24b74f.png?alt=media)
* **Specify resources connect to an app:** you can use the team functionality to combine resources that are part of the same app (combination of repos, containers and clouds). This also allows you to view all reports
* **Better overview when using a monorepo split.** You can assign team members to specific directories of your monorepo, improving their overview. More information on splitting monorepositories can be found [here](https://help.aikido.dev/en/articles/9026666-splitting-up-your-monorepo-per-directory).

{% hint style="info" %}
Repo linking is only available for manually created teams (not imported from SCM). Other resources like containers, clouds & Zen apps can be linked to both manually created and SCM-imported teams.
{% endhint %}

## How To Create Teams <a href="#how-to-create-teams" id="how-to-create-teams"></a>

**Step 1:** Navigate to **Settings -> Teams**\
​

![Team dashboard for “mdschuym” showing 4 active repositories and management options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0b18ccf8b33376a81bcb2be0b155c8ea75bf054a%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_5986952f-2c5a-4fc5-bbab-78742b2d10d0.png?alt=media)

**Step 2:** Click **Create Team** and give your team a name\
​

![Form to create a new team by entering a team name for vulnerability tracking.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2df987cb28febd5270a9e0f37b72b13d15f2eaee%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_86bb94a8-6266-4192-945a-873e275bfc36.png?alt=media)

**Step 3 (optional):** **Add team members** to the newly created team.

![User management interface for assigning people to the "Architects" team.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-360a0c5347426b99a212daa1a65be6b91a03be63%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_56480ec4-3c43-4324-a974-31492495dd76.png?alt=media)

**Step 4:** **Link different resources** via the **responsibility tab.** You can add different resources such as repositories, clouds, containers, domains and zen apps. You can add repositories and containers **in bulk** via the [repository](https://app.aikido.dev/settings/integrations/repositories) and [container settings](https://app.aikido.dev/settings/container-image-registry) screen.

> If you want to link specific domains to a team, you can set this up by linking your domains to a repo or container. It will automatically inherit access permissions.

![Interface for linking repositories, cloud, or container resources to the Backend team.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FuyEJzLnw6eQHoLdBUAiw%2FScreenshot%202025-12-15%20at%2016.21.52.png?alt=media\&token=ce29fb76-f6bc-4401-a7e3-e81bd279ef20)

**Step 5.** Go back to your feed and filter on a specific team. You should only see issues that are related to those repositories and clouds that were attached to the team.

## How to select your team in UI <a href="#how-to-select-your-team-in-ui" id="how-to-select-your-team-in-ui"></a>

**Aikido's Feed** features a **team filter** at the top of the page. This filter allows users to tailor the feed to display only the issues relevant to selected teams. This filter can be used on basically every page in Aikido (feed, reports, settings etc).

![Team filter dropdown with stats for solved and newly detected issues this week.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-61296e08665b9c3e6e29330ab62bf16a1916b53d%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_4709269e-976a-487e-af63-80160fbc3907.png?alt=media)

# Assign Team Responsibilities by Specific Path in Repo

Assigning **specific repo paths** to teams in Aikido can help to streamline issue management in **large monorepos** and enabling **more granular reporting**.

### Use Cases <a href="#use-cases" id="use-cases"></a>

* **Monorepo management:** Assign specific paths to teams instead of the full monorepo. This allows you to filter your feed in a more granular way.
* **Specific reporting:** Allows reports to be generated based on service-level/path-level rather than at the repo level.

### Assigning Specific Paths <a href="#assigning-specific-paths" id="assigning-specific-paths"></a>

**Step 1:** Create a Team and Link Repositories (see [article](https://help.aikido.dev/docs/getting-started/manage-teams-and-applications/managing-user-access-with-teams))

* Create a new team or select an existing one, then link the relevant repositories to this team.

**Step 2:** Click Limit Access By Path in the dropdown menu

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-3a01b2dcc3f32601d77662d9d9d9371cc37f2c40%2Fassign-team-responsibilities-by-specific-path-in-repo_e373539b-fc2c-4566-bd1a-49ea280c5386.png?alt=media)

**Step 3:** Enter the paths within the repo that you want the team to have access to.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-df71db5c6ffd56f721b37087d38991706c629630%2Fassign-team-responsibilities-by-specific-path-in-repo_fe715668-3cdc-4ff9-8dee-953f92ad64f8.png?alt=media)

**Wildcard support**

`**` means anything in any subdirectory\
`*` means anything in the current directory\
`?` means any single char

**Step 4:** Filter Issues in Feed/Reports

Go to the **Feed** or **Reports** section. Apply a filter based on the team, and you will see only the issues related to the paths assigned to that team.

![Dashboard showing security findings, severity levels, and issue statuses for the "devs" team workspace.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6aa40746080049d93c39e7df6a862098639abd72%2Fassign-team-responsibilities-by-specific-path-in-repo_12583652-fb59-4830-a140-36996db6ff3d.png?alt=media)

# Assign Team Responsibilities with Gitlab Topics

Aikido allows you to use **Gitlab Project Topics** to automatically manage team assignments in Aikido. This streamlines issue management in large organizations and enables more granular reporting without manual setup.

### Use Cases <a href="#use-cases" id="use-cases"></a>

* **Clear ownership across many repos**: In large orgs, each repo has a defined owning team, making it easier to track who is responsible.
* **Automatic onboarding**: When new repos are created with the right topic, they’re instantly assigned to the correct team in Aikido.

### Configuration <a href="#assigning-specific-paths" id="assigning-specific-paths"></a>

{% hint style="warning" %}
This feature is **not enabled by default** and needs to be activated for your account. Please contact **Aikido support** for assistance.&#x20;
{% endhint %}

For each repository you want managed by Aikido:

1. In GitLab, [go to your repository’s Settings → General → Topics](https://docs.gitlab.com/user/project/project_topics/).
2. Add a topic like: `owner:Internal Tooling Team`.
3. Aikido will automatically create (or update) the team and assign the repo.
4. If the topic is removed or changed later, Aikido will unassign or reassign the repo automatically.

# Assign Team Responsibilities with Code Owners

Aikido allows you to use **Code Owners** to automatically manage team assignments in Aikido. This streamlines issue management in large organizations and enables more granular reporting without manual setup.

{% hint style="info" %}
Code Owners is independent from source code manager. It can easily be used with GitHub, Gitlab, Bitbucket and even our Local Scanning workspaces.
{% endhint %}

### Use Cases <a href="#use-cases" id="use-cases"></a>

* **Clear ownership across many repos**: In large orgs, each repo has a defined owning team, making it easier to track who is responsible.
* **Path-level ownership:** For codebases where multiple teams own different directories or paths (e.g. monorepos), Aikido maps CODEOWNERS paths directly to teams, no manual assignment needed.
* **Automatic onboarding**: When new repos are created with the right topic, they’re instantly assigned to the correct team in Aikido.

### Configuration <a href="#assigning-specific-paths" id="assigning-specific-paths"></a>

{% hint style="warning" %}
This feature is **not enabled by default** and needs to be activated for your account. Please contact **Aikido support** for assistance.&#x20;
{% endhint %}

1. In Github/Gitlab/Bitbucket, create a new file called `CODEOWNERS.` See [GitHub docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [Gitlab docs](https://docs.gitlab.com/user/project/codeowners/) and [Bitbucket docs](https://support.atlassian.com/bitbucket-cloud/docs/set-up-and-use-code-owners/). Aikido assumes there is only 1 codeowner file and will use the first one it finds.
2. Aikido will automatically create (or update) the team and assign the repo.
3. If the Codeowners file is changed later, Aikido will unassign or reassign the repo automatically.

# Manage Findings

# Main Feed

## Main Feed

### Introduction <a href="#introduction" id="introduction"></a>

Aikido's Feed is meticulously designed to streamline security management: it groups similar issues for clarity, allows for customizable views to highlight what's currently important. The main feed focusses on open issues only. Snoozed and ignored issues are accessible on a separate page for a clean giving a focused and clean overview.

### Aikido's Main Feed <a href="#aikidos-main-feed" id="aikidos-main-feed"></a>

The **Feed** is the central hub for monitoring and managing security issues. A similar view can be found all over Aikido when going into details of repositories, clouds and domains.

By default, Aikido enables the **Focus** view, containing all issues that are important to follow-up. By toggling to **All** we will also show issues that have been auto-triaged and ignored.

*Status Column*

Shows the status of the particular issue.

* *New*: issues that have been around for less than 7 days
* *To Do:* all other issues that are still unresolved
* *Task Open:* only when a task manager is linked
* *PR Open:* clicking will take you to PR / branch scan overview.

![Security dashboard showing vulnerability status, severity, fix times, and task assignments for issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5cb555f73d17f6d317932191188f13d4677b5de0%2Fmain-feed_e134c1d8-5218-4f06-96d2-2cb099968f41.png?alt=media)

### Sidebar <a href="#sidebar" id="sidebar"></a>

Aikido's Feed is equipped with a detailed sidebar, designed to provide users with comprehensive information and actionable options for each security issue. The image below shows the main important actions one can take.

**#1 Group Actions:** these are actions that can be taken on group level of an issue.

**#2 Subissue Actions:** you can also take actions on a subissue separately. This can be important when certain subissues want to be snoozed or ignored, but the overal issue group should remain in the main feed.

**#3 Reachability Analysis:** visualizes accessible code paths for that specific issue.

**#4 Detail Screen**: Separate detail screen with even more information (e.g., CVE information).

![Security dashboard showing a critical vulnerability in the 'bson' package with actionable steps.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1f6fb449f589e649ad898af25e94711cbc0fffaf%2Fmain-feed_7d0dadc8-a23e-4f23-b207-c1710b0ce1df.png?alt=media)

**Reachability Analysis**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1251e9ff34ebcce7f172efe396d5a5f537a061bb%2Fmain-feed_1aabe4cf-b6b9-44e5-b953-41f35c7ef824.png?alt=media)

### Filter Issues <a href="#filter-issues" id="filter-issues"></a>

You can easily adjust the view in order to filter on those issues that are most important to you in the moment. These filters can be found above the issue table in every feed view. You can filter on

* **Issue Type**
* **Predefined filtered views**
  * If you are using the [**SLA functionality**](https://help.aikido.dev/en/articles/8926339-enabling-slas-in-aikido), you will be able to see all upcoming and out of SLA issues

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8c544a031cfaa1e383902af5efee62f1a0c14dc7%2Fmain-feed_ac998c65-834e-4bad-b76b-550ca0c2db6b.png?alt=media)

### Export Issues to CSV or PDF <a href="#export-issues-to-csv-or-pdf" id="export-issues-to-csv-or-pdf"></a>

You can export a CSV or PDF of issues. You can configure which issues to export exactly. This can be triggered from the Actions menu in the top right.

![Export issues: Filter by status, type, team, and format for CSV or PDF download.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-10981ff893e46976c3e8e0f2e87817e9308b46a7%2Fmain-feed_fc64121c-f6e4-4e98-87b9-e2c0cedcdf20.png?alt=media)

### Show issues per team or project <a href="#show-issues-per-team-or-project" id="show-issues-per-team-or-project"></a>

**Aikido's Feed** features a **team filter** at the top of the page. This filter allows users to tailor the feed to display only the issues relevant to selected teams ([📖 Set Up Teams](https://help.aikido.dev/en/articles/9005606-using-teams-for-repository-and-user-management)).

![Team selector dropdown with search and statistics on solved and new issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-61296e08665b9c3e6e29330ab62bf16a1916b53d%2Fmain-feed_7d1a69e7-7618-4eae-b374-ee6322f9fd43.png?alt=media)

# Manually Adjust Issue Severity

### Introduction <a href="#introduction" id="introduction"></a>

When Aikido finds vulnerabilities in your code repos, cloud environments or public facing domains, our scoring engine gives the vulnerability a severity from 'low' to 'critical'. Our scoring engine takes into account a whole set of rules to assign this severity, but the most important one would be the urgency to fix.

If for some reason, you believe a vulnerability has been given a wrong severity, either to low or to high, Aikido gives you the opportunity to adjust the severity manually so it ends up higher or lower on your list of things to fix.

You can either adjust a **single issue's severity**, or the **severity of a whole group** of issues, in which case they will all get the same severity, regardless of their previous severity.

### Adjust severity of a single issue <a href="#adjust-severity-of-a-single-issue" id="adjust-severity-of-a-single-issue"></a>

A single issue's severity can be adjusted via the issue's action menu found in the sidebar, as shown in the image below.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7e2b264662f921b06dc4c7333df7c96b6c50886e%2Fmanually-adjust-issue-severity_62363e1c-cd80-42eb-86c9-4a9010f3c05f.png?alt=media)

### Adjust severity of a whole issue group <a href="#adjust-severity-of-a-whole-issue-group" id="adjust-severity-of-a-whole-issue-group"></a>

To adjust the severity of a whole issue group, you can click on "Adjust severity" on the issue group's action menu in a row in any table.

![Security vulnerabilities dashboard showing critical issues, severity, affected systems, and assigned team members.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b0d10f287a6aa546c93ddac35933c143b29b26b4%2Fmanually-adjust-issue-severity_7917f621-24d7-4468-a987-7fbb42ae99a2.png?alt=media)

When adjusting the severity, you need to provide the new severity the vulnerability as well as a reason why you think the severity should be adjusted.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-df9e0f591bef57b950c9ed8fb8a53ead5d6eb1fa%2Fmanually-adjust-issue-severity_ec76e6e3-7826-47d6-8afb-aac88c2b4f15.png?alt=media)

If you decide to lower or increase the severity of an issue group, Aikido's scoring engine will not apply that adjusted severity to any newly discovered issue in that group. This is because we believe that you should at that moment evaluate this new finding after which you can again adjust the severity.

# Ignore Issues to Remove Issues From Main Feed

#### Use Cases <a href="#introduction" id="introduction"></a>

While Aikido boasts advanced detection capabilities with auto-ignore (see the [ignore criteria](https://app.aikido.dev/issues/ignored/criteria)), the occasional false positive may slip through, or an issue may be irrelevant to your specific context. The ignore functionality is designed to address this, ensuring your security overview remains accurate.

#### How to ignore an issue group or subissue <a href="#how-to-ignore-an-issue-group-or-subissue" id="how-to-ignore-an-issue-group-or-subissue"></a>

**Step 1:** Navigate to the **issue group**, or **subissue** in Aikido you wish to ignore and select the "Ignore" option in the actions menu (triple dots).

![Action menu options for task management and issue handling in a software interface.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-93bd099dbbcc470aa389965348238da29f9bcc94%2Fignore-issues-to-remove-issues-from-main-feed_ff7d2590-2d08-42c5-b7a1-464dac520f01.png?alt=media)

**Step 2:** For subissues, you will be asked about how Aikido should treat this subissue and potential similar detections in the future.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-732f6fbd318fabb89d98493e94a1b9e8b73e89f2%2Fignore-issues-to-remove-issues-from-main-feed_b8de9c2c-c625-4a45-9c92-09c72c786b24.png?alt=media)

You have a few options available to ignore the current and future issues. The options available depend on the context in which you are ignoring an issue (single issue or issue group), but also on the issue type (e.g., Surface Monitoring and Cloud Issues show different options).

Below are all the ignore options listed that you might see

* **Only this issue/only this issue group**\
  This option will only ignore this subissue, or this issue group and all its sub issues, depending on the context. *Note. If you ignore an issue group, new future subissues will not be auto-ignored and will re-open the group containing this specific subissue.*\
  ​
* **Ignore by path**\
  When choosing this option, you create an issue rule which will ignore all current and future file based issues (open source, SAST, IAC and exposed secrets) under a certain path. You can edit the path there for convenience to make the rule as specific as you'd like.\
  ​\
  This can be helpful when there are testing frameworks in a specific path that you do not want Aikido to scan.

  ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ff9610e35481d2f79cb0c8dd1c330a3baf916e53%2Fignore-issues-to-remove-issues-from-main-feed_fe887c2a-204b-412b-9854-dbe96beff936.png?alt=media)

  ​
* **Ignore all findings related to CVE**\
  This option creates an issue rule which ignores all current and future open source dependencies linked to that CVE. This ignore rule is global and is applied to all repositories.\
  ​
* **Ignore all findings related to rule**\
  Most issues in Aikido are related to a specific rule code such as SAST, IAC and Cloud issues. When selecting this option, you create an issue rule which ignores all current and future issues related to that specific rule. This ignore rule is global and is applied to all repositories.

**Step 3:** Confirm your choice to ignore the issue, effectively removing it from your main feed in Aikido.

#### View all (auto-) ignored issues <a href="#check-out-all-auto--ignored-issues" id="check-out-all-auto--ignored-issues"></a>

The [ignore view](https://app.aikido.dev/issues/ignored) consolidates all issues ignored by Aikido's triaging algorithm, as well as those manually ignored by users. Here, you can review the rationale behind each automatically ignored issue (see the [ignore criteria](https://app.aikido.dev/issues/ignored/criteria)). Your manually ignored issues will also be displayed here, providing a comprehensive overview of all exclusions made within Aikido.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c00fc346f2e8dca328bd63a6b61bf1c63ef3d7b6%2Fignore-issues-to-remove-issues-from-main-feed_65ba19ef-aa73-4a9f-aa79-50f391560e04.png?alt=media)

# Snooze Issues for Later

### Use Case <a href="#introduction" id="introduction"></a>

Aikido introduces a flexible snooze feature that allows the snoozing of issue groups or subissues separately. This functionality clears the main feed of non-urgent items, providing a cleaner workspace to focus on immediate priorities.

### How to snooze issues <a href="#how-to-snooze-issues" id="how-to-snooze-issues"></a>

**Step 1.** Navigate to the **issue group**, or **subissue** in Aikido you wish to snooze and select the "Snooze" option in the actions menu (triple dots).

![Context menu displays task management actions like create, snooze, ignore, and adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5ecce4f4f5b4f9c50ffa9697fab20b72c42fd039%2Fsnooze-issues-for-later_cf410044-9793-44be-b6a7-f630c1b06093.png?alt=media)

**Step 2.** Choose the duration for snoozing: 1 day, 1 week, 1 month, 1 year, or specify a custom period.\
​

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4c7f34adc095d00b4b7386f46d27f2f19b0d3c83%2Fsnooze-issues-for-later_1a4d86fe-2bfc-4e85-9ff5-eafad017c960.png?alt=media)

**Step 3.** Optionally, add a reason for snoozing to keep track of the decision-making process.\
​

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9fa6e40d1a0b7f61895ce780591031feb29a0075%2Fsnooze-issues-for-later_01078916-5014-4514-9643-e0656d67dfba.png?alt=media)

​After snoozing, these items will disappear from the main feed, simplifying your view to focus on what's urgent.

### Viewing Snoozed Items: <a href="#viewing-snoozed-items" id="viewing-snoozed-items"></a>

* Access the [Snooze View](https://app.aikido.dev/issues/snoozed) in Aikido to see all snoozed issue groups and and subissues. You can extend or unsnooze any issue from this view.\
  ​

  ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4c64427b1e337dac60f50ab65f6a677c1ebbdfd4%2Fsnooze-issues-for-later_dd6f4c38-5d68-4143-a463-0f5970ff8729.png?alt=media)

# Display License Issues in Feed

In addition to the license report, Aikido allows you to display licenses directly in the feed. These issues are grouped by license type and show all locations where a specific license is used. This feature helps you stay informed and take immediate action on license-related issues.

### Benefits <a href="#benefits" id="benefits"></a>

* Directly act licenses: snooze, ignore, or create tasks.
* Receive alerts for new critical and high severity license issues.

### How to enable Licenses in feed <a href="#how-to-enable-licenses-in-feed" id="how-to-enable-licenses-in-feed"></a>

**Step 1:** Navigate to the [License & SBOM Reports page](https://app.aikido.dev/licenses)

**Step 2:** Click the Action dropdown menu and select 'Display Licenses in Feed'

![Dropdown menu with option to display licenses in the feed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e3ac3de12c552677333bf419ff9adcf64762ab42%2Fdisplay-license-issues-in-feed_1b911e0a-9234-471b-8012-fb2db9f5bf3e.png?alt=media)

**Step 3:** Select one of the three options. You have the option to show only the critical licenses issues, or also including the high severity ones.

> **Note:** all issues in the feed are reflected in the trends over time report. This means that by enabling this functionality, there might be a bump in the number of open issues.

![License issue feed settings with options for filtering severity and reporting.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d6f5457beeb8749ba50c310ef61c7a29bcabbce0%2Fdisplay-license-issues-in-feed_ec0a687f-41f4-4660-ba8d-66423429f333.png?alt=media)

**Step 4:** Go back to Feed and select License Issues in the filter. All open critical and/or high severity license issues will be displayed. **Aikido will run a scan in the background to start showing licenses - this can take a minute.**

![Security dashboard menu highlighting resolved License Issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e1c4819f8388c079fe38ed3324e82e68817fb52d%2Fdisplay-license-issues-in-feed_d4b4064c-882a-40b5-b9c4-3b61ef5780ea.png?alt=media)

# Enable SLAs in Aikido

## Enable SLAs in Aikido

You can enable SLA settings in Aikido to automatically assign due dates to tickets. This facilitates a structured and timely approach to issue resolution based on their reported time and severity.

#### Detection and SLA Reset Logic <a href="#how-to-enable-slas-in-aikido" id="how-to-enable-slas-in-aikido"></a>

* SLA countdown starts the moment Aikido first detects the issue and are measured in calendar days, not business days
* When the severity of an issue is manually changed, the SLA date resets.
* When an issue is unsnoozed, the SLA date resets.
* When an issue is unignored, the SLA date resets.

#### How to enable SLAs in Aikido <a href="#how-to-enable-slas-in-aikido" id="how-to-enable-slas-in-aikido"></a>

1. Navigate to the Settings -> [SLA settings](https://app.aikido.dev/settings/sla)
2. Ensure the 'Enable SLAs' option is turned on to implement SLA rules.\
   ​

   ![Set and enable SLAs per severity to manage vulnerabilities and notify stakeholders via Slack.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f93ecd6cd8d715bea613c848c784fda38a7260e2%2Fenable-slas-in-aikido_1ff28d9b-3344-4de1-bcfd-f50e669ab680.png?alt=media)
3. Input the **number of days** for resolution in the fields for Critical, High, Medium, and Low priority issues to establish SLA time frames.\
   ​

   ![Issue resolution deadlines by priority: critical (5 days), high (20), medium (60), low (100).](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8cd7d0b03d924c45304bbf39e83cd6592d71ad71%2Fenable-slas-in-aikido_c1e31d14-d808-4f55-a853-117c72d67aba.png?alt=media)

   ​
4. Set up the '**Due Soon' notification threshold** by specifying the number of days before the SLA deadline, which will highlight impending due dates on the [SLA Due Soon](https://app.aikido.dev/queue?filter=due_soon) view.\
   ​

   ![Set the 'Due Soon' issue status by days before the SLA deadline.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8df4724d3cbe60f6148b02c611be9fdc39ec56a5%2Fenable-slas-in-aikido_e8abe17c-281e-4a5f-9947-3caf00ca1536.png?alt=media)
5. Click **'Save'** to apply these configurations.

#### SLA Information in Aikido UI <a href="#sla-information-in-aikido-ui" id="sla-information-in-aikido-ui"></a>

After setting up your SLA parameters, here's how you can monitor your SLA due dates.

* **Sidebar Information**: Next to each subissue in the sidebar, you will see the SLA information, providing a quick reference to gauge urgency. Hover over the label in order to view the date.\
  ​

  ![NodeGoat subissues list with priorities, due dates, authors, and commit links.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f8dfd18aeef9f2f73ab8ed912d1c03846cefe425%2Fenable-slas-in-aikido_9b8a2056-6d6a-4314-a7cc-3efff950ad43.png?alt=media)
* **SLA Due Soon Filter**: The [**SLA Due Soon**](https://app.aikido.dev/queue?filter=due_soon) view view displays issues that are close to breaching the SLA, based on the threshold set. **Enable this filtered view** by clicking the Filter Icon on your Feed and select SLA Due Soon.\
  ​

  ![Security vulnerabilities dashboard showing severity, status, and assignment for identified software issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-08454e035e1cfc5cc11a90a388476bddd7d5fb78%2Fenable-slas-in-aikido_b8bdc36a-51a0-4742-9ec8-ce0d1dc6cc90.png?alt=media)
* **Out of SLA View**: The [**Out of SLA**](https://app.aikido.dev/queue?filter=out_of_sla) view lists all issues and subissues that have exceeded their SLA limits. **Enable this filtered view** by clicking the Filter Icon on your Feed and select Out of SLA.\
  ​

  ![Critical vulnerabilities dashboard showing unassigned open tasks and their fix times.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-efacf0999b36f0f471bf1cc0265efff45b4597c7%2Fenable-slas-in-aikido_ba292c16-3b12-456a-b0a4-5e118b7638c8.png?alt=media)

***

# How is Severity Score Calculated

Aikido provides a contextual, risk-based severity score from 0 to 100, offering 10× more granularity than traditional CVSS scoring (which is on a 0–10 scale). This allows for better prioritization and filtering.

<table><thead><tr><th width="143.943603515625">Severity</th><th width="155.927001953125">Score</th></tr></thead><tbody><tr><td>Critical</td><td>90 - 100</td></tr><tr><td>High</td><td>70 - 89</td></tr><tr><td>Medium</td><td>40 - 69</td></tr><tr><td>Low</td><td>1 - 39</td></tr></tbody></table>

### 1. Multiple Vulnerability Data Sources

We continuously monitor a variety of vulnerability feeds and databases, that  provide baseline severity information and help establish initial severity scores. Databases include:

* Public vulnerability databases (e.g., NVD, GHSA,... | [See full list](https://help.aikido.dev/code-scanning/scanning-practices/external-vulnerability-databases-used-in-our-sca-engine))
* Operating system and vendor-specific advisories
* Our own Aikido Intel: <https://intel.aikido.dev/>

### 2. Contextual Severity Adjustments

To reflect actual risk more accurately, Aikido layers in additional context such as exploitability, environment, threat intelligence, and custom rules.<br>

**Exploitability & Threat Intelligence:**

Severity can increase when there’s evidence of real-world risk:

* The vulnerability is actively exploited or appears on the CISA KEV list
* A public PoC exploit is available (e.g., on GitHub)

#### Business Context

Severity is adjusted based on the importance of the affected asset. Some example are:

* Production vs test environments
* Backend vs frontend code
* Whether the vulnerable code is reachable or executed

#### Customer Rules

You can further refine issue scoring by adding contextual information to your project

* Learn how you can improve the risk score for repositories and containers [here](https://help.aikido.dev/docs/getting-started/general-information/improve-risk-scoring-for-repositories-and-containers)

#### Exploit Prediction (EPSS)

Aikido also supports EPSS-based prioritization to automatically downgrade or ignore vulnerabilities that are unlikely to be exploited in the next 30 days. This is optional and turned off by default, more info here: [use-epss-values-to-further-reduce-noise](https://help.aikido.dev/docs/code-scanning/miscellaneous/use-epss-values-to-further-reduce-noise "mention")

{% hint style="success" %}
You can click the score to view a detailed breakdown of why this issue received this severity rating
{% endhint %}

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F0zrwbgJB3u5IR8WgbPmJ%2FScreenshot%202025-07-09%20at%2014.21.12.png?alt=media&#x26;token=4d20add5-436b-432d-b65c-def34196a984" alt="" width="375"><figcaption></figcaption></figure>

# Why Was an Issue Marked as Solved

In Aikido, issues automatically move from **Open** to **Solved** when they are no longer detected in the latest scan.

There are several common reasons why this might happen:

***

### ✅ The Issue Was Fixed <a href="#the-issue-was-fixed" id="the-issue-was-fixed"></a>

Someone in your team resolved the problem — it's no longer showing up in the scan because it has been **completely removed or fixed in code**.

***

### 🌿 Branch Change <a href="#branch-change" id="branch-change"></a>

If you're scanning a **different branch**, Aikido will:

* Close issues tied to the old branch
* Open any issues found on the new one
* 💡You can verify which branch is being scanned via the tag on the [repository page](https://app.aikido.dev/repositories)

  ![Highlighted "master" branch in the about-github repository navigation menu.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7afc1c0377036c01140081a5d19bb14c6f7e23b9%2Fwhy-was-an-issue-marked-as-solved_3f340eda-9a59-4886-b42c-af90f0c51a24.png?alt=media)

***

### 📁 File Relocation <a href="#file-relocation" id="file-relocation"></a>

If the affected file was **moved or renamed**, Aikido will:

* Mark the original issue as solved (since the file path changed)
* Potentially open a new issue under the new file location

***

### 🔐 CVE Database Update <a href="#cve-database-update" id="cve-database-update"></a>

Sometimes CVEs get updated to narrow down the versions affected.

**Example**:

* Aikido flagged a vulnerability in log4j:2.17.1 based on CVE-2021-44832.
* Later, the CVE was updated to say only versions ≤2.17.0 are affected.
* Aikido picked up the change and automatically removed the issue for 2.17.1.

***

### 📦 Dependency Moved to Dev-Dependency <a href="#dependency-moved-to-dev-dependency" id="dependency-moved-to-dev-dependency"></a>

If a vulnerable package is moved from a production dependency to a dev-dependency, Aikido will:

* Mark the original issue as solved (since the dependency type changed)
* Not longer report the issue as dev-dependencies are **by default** not scanned.
* 💡 You can enable scanning of dev-dependencies on a **per-repository** basis. [More information in this doc](https://help.aikido.dev/docs/code-scanning/scanning-practices/scanning-dev-dependencies-for-cves)

***

### 🧠 SAST Rule Improvements <a href="#sast-rule-improvements" id="sast-rule-improvements"></a>

Static analysis rules are continuously improved to reduce false positives. As these rules become more accurate, Aikido may:

* **Mark previously flagged issues as solved**
* Prevent future false alarms for similar patterns

***

### 🗂️ Local Scanning – Scan Location Changed <a href="#local-scanning-scan-location-changed" id="local-scanning-scan-location-changed"></a>

When scanning locally, changing the **target directory** will influence what gets scanned.

* Issues in unscanned paths will be marked as solved
* New issues may show up in the new location

***

### Still Not Sure? <a href="#still-not-sure" id="still-not-sure"></a>

This list covers the most frequent causes, but there may be other edge cases.

👉 If you're unsure why something was marked as solved, just reach out through the in-app chat — we're happy to help.

# How Is Fix Time Calculated

### What Is Fix Time?

Fix time is a rough estimate of how long it may take to remediate a security issue. It’s not exact—it’s meant to help you prioritize and plan based on the relative effort required.

### How It’s Calculated

Aikido uses a custom algorithm per issue type. Here’s how it works:

#### 🧬 Dependency (SCA) Issues

Fix time depends on the type of version upgrade:

* Minor upgrade (e.g. 4.5.1 → 4.5.2) → 5–15 minutes
* Major upgrade (e.g. 1.0 → 3.0, or across EOL boundaries) → at least 1 hour

#### 🔍 SAST (Code Issues)

Calculated as: Issue count × static time per issue type

Examples:

* SQL Injection ≈ 30 min/issue
* Secrets ≈ 10 min/issue

#### ☁️ Cloud Issues

Similar logic as SAST: static values per issue type, multiplied by count.

#### 🔑 Secrets

One fixed estimate per issue (e.g., rotate a key = 5–10 minutes).

{% hint style="success" %}
When there's an [Aikido AutoFix](https://help.aikido.dev/docs/aikido-autofix)available, the actual fix time will be lower
{% endhint %}

# Task Management Tools

### Jira

{% content-ref url="task-management-systems/all-supported-task-trackers/jira-cloud" %}
[jira-cloud](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/jira-cloud)
{% endcontent-ref %}

{% content-ref url="task-management-systems/troubleshoot-jira-task-creation-set-up-default-issue-types" %}
[troubleshoot-jira-task-creation-set-up-default-issue-types](https://help.aikido.dev/docs/getting-started/task-management-systems/troubleshoot-jira-task-creation-set-up-default-issue-types)
{% endcontent-ref %}

{% content-ref url="task-management-systems/all-supported-task-trackers/jira-data-center" %}
[jira-data-center](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/jira-data-center)
{% endcontent-ref %}

{% content-ref url="task-management-systems/advanced-functionalities/auto-close-jira-tasks-when-aikido-issues-are-resolved" %}
[auto-close-jira-tasks-when-aikido-issues-are-resolved](https://help.aikido.dev/docs/getting-started/task-management-systems/advanced-functionalities/auto-close-jira-tasks-when-aikido-issues-are-resolved)
{% endcontent-ref %}

### Linear

{% content-ref url="task-management-systems/all-supported-task-trackers/linear" %}
[linear](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/linear)
{% endcontent-ref %}

{% content-ref url="task-management-systems/advanced-functionalities/auto-close-linear-tasks-when-aikido-issues-are-resolved" %}
[auto-close-linear-tasks-when-aikido-issues-are-resolved](https://help.aikido.dev/docs/getting-started/task-management-systems/advanced-functionalities/auto-close-linear-tasks-when-aikido-issues-are-resolved)
{% endcontent-ref %}

### Others

{% content-ref url="task-management-systems/all-supported-task-trackers/asana" %}
[asana](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/asana)
{% endcontent-ref %}

{% content-ref url="task-management-systems/all-supported-task-trackers/azure-devops-boards" %}
[azure-devops-boards](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/azure-devops-boards)
{% endcontent-ref %}

{% content-ref url="task-management-systems/all-supported-task-trackers/clickup" %}
[clickup](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/clickup)
{% endcontent-ref %}

{% content-ref url="task-management-systems/all-supported-task-trackers/github-issues" %}
[github-issues](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/github-issues)
{% endcontent-ref %}

{% content-ref url="task-management-systems/all-supported-task-trackers/gitlab-issues" %}
[gitlab-issues](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/gitlab-issues)
{% endcontent-ref %}

{% content-ref url="task-management-systems/all-supported-task-trackers/gitlab-issues-self-managed" %}
[gitlab-issues-self-managed](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/gitlab-issues-self-managed)
{% endcontent-ref %}

{% content-ref url="task-management-systems/all-supported-task-trackers/jetbrains-youtrack" %}
[jetbrains-youtrack](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/jetbrains-youtrack)
{% endcontent-ref %}

{% content-ref url="task-management-systems/all-supported-task-trackers/mondaycom" %}
[mondaycom](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/mondaycom)
{% endcontent-ref %}

{% content-ref url="task-management-systems/all-supported-task-trackers/shortcut" %}
[shortcut](https://help.aikido.dev/docs/getting-started/task-management-systems/all-supported-task-trackers/shortcut)
{% endcontent-ref %}

# All Supported Task Trackers

# Jira Cloud

*📋 Setting up automated task creation in Jira Cloud*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Jira Cloud.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Jira projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Jira, ensuring targeted attention for critical vulnerabilities.

{% hint style="warning" %}
Note: the ticket creation is linked to the user who has set up the integration. We recommend creating an extra 'Aikido' user inside Jira with write access to all projects.
{% endhint %}

## Connecting the Aikido App to Jira <a href="#connecting-the-aikido-app-to-jira" id="connecting-the-aikido-app-to-jira"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Jira Issues'
3. A prompt will request authorization for Jira.\
   ​

   ![Jira access unauthorized; prompt to authorize account for issue-tracking integration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-556af441921a4c0ed9e37f27386a63fca7b3e117%2Fjira-cloud_7f02a7ff-2d6a-4fd2-859a-690ec2503847.png?alt=media)
4. Login into your Jira account
5. Grant Aikido permission to access your Jira workspace

   ![Aikido Security requests permission to access and manage your Atlassian Jira account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7d2ac9ab0fe4929ed1615e3358c1956f680100f4%2Fjira-cloud_a052e293-4386-42ea-a4ae-4fa3661b2fad.png?alt=media)
6. Once authorized, Aikido is successfully connected to Jira, enhancing your task management capabilities 🚀<br>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FIIJTv7IwxLagom4d9B03%2Fimage.png?alt=media&#x26;token=7e64c1e3-bbc4-47a2-b543-6a6100e8a96b" alt="" width="563"><figcaption></figcaption></figure>

## ​Options for Task Creation in Jira via Aikido <a href="#options-for-task-creation-in-jira-via-aikido" id="options-for-task-creation-in-jira-via-aikido"></a>

There are two different options to create new tasks from Aikido into Jira.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assign column.**

   ![Task management table with “Assignee” column and options to add or edit entries.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fjira-cloud_0001b592-6b4b-4bbf-b3a8-ff8ddff44c51.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.

   ![Menu of task management actions: create, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d48713cff103c764405a9fcbcfccdbde6e7c7ee3%2Fjira-cloud_38576e60-ea82-4442-88d3-db09a3bbd539.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Jira task creation form detailing a critical security vulnerability.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8e0c4229e5124fa8d1d8f8e4cd261a3e56169e01%2Fjira-cloud_61e7326b-5183-4741-aaac-891ec98663fc.png?alt=media)
3. The newly created task in Jira will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Critical security task: var\_dump() may expose sensitive user information; action required.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5c8af49ae0f80e42d1ed19999fe754dacbd5f5cf%2Fjira-cloud_294591ba-6d3d-4cfc-9cee-0fc1b6c880cd.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Jira Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.

   ![Autocreation settings for automatic task generation based on issue severity and daily limit.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fjira-cloud_a2cf62ba-d5ce-4053-a032-2f6f5f0b43ad.png?alt=media)

   ​
4. Aikido will then autonomously generate Jira tickets based on these settings 🚀

### Jira Sync Information <a href="#jira-sync-information" id="jira-sync-information"></a>

Aikido automatically syncs a couple of fields to Jira

* Severity is mapped to the 'Priority field' in Jira (one way)
* Assignees are synced both ways (so updates in Jira will be reflected in Aikido too

***

# Jira Data Center

**Table of contents:**

* [Introduction](#introduction-)
* [Prerequisites](#prerequisites)
* [Connecting the Aikido App to Jira](#connecting-the-aikido-app-to-jira)
* [Options for Task Creation in Jira via Aikido](#options-for-task-creation-in-jira-via-aikido)
* [1. Manual Task Creation](#1-manual-task-creation)
* [2. Automated Task Creation](#2-automated-task-creation)
  * [Setup Jira Integration Now→](#setup-jira-integration-now-)
  * [Discover Integration Details →](#discover-integration-details--)

## Jira Data Center

***📋 Setting up automated task creation in Jira Data Center***

### Introduction <a href="#introduction" id="introduction"></a>

This article focuses on those companies that have Jira Data Center running (i.e., Jira on premise, different from [Jira Cloud](https://help.aikido.dev/en/articles/8680218-setting-up-automated-task-creation-in-jira-cloud)). The following one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Jira On Prem.

Following use cases are supported :

* Automated Ticket Creation: Automatically create and push tickets to specified Jira projects for seamless tracking of security issues.
* Manual Ticket Addition: Manually add security issue tickets to Jira, ensuring targeted attention for critical vulnerabilities.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

In order to make the connection to JIRA Data Center, you'll need to create a personal access token. This token will then be used to carry out all requests to your instance.\
​\
Please note that the level of access the integration has will be equal to the person who created the personal access token (PAT). It's therefore advised to let a person with sufficient access rights in the environment to create the PAT.

To create a PAT, you can follow the steps below:

1. Navigate to your JIRA Data Center environment
2. Click on your avatar in the navigation bar on top and navigate to "Profile"
3. Click on "Personal Access Tokens", you should end up on a screen similar to the one below**​**

   ![Jira Software personal access tokens page prompting user to create their first token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-792134445b90e7c6d1bf8e568dcbbc3840ea981c%2Fjira-data-center_bd8df7ef-3798-4bdb-acac-65a30ef15823.png?alt=media)
4. Click on "Create token" and give it an appropriate name
5. We advise to not set an expiry date, but if you do, you'll have to remind yourself to update the token in Aikido periodically
6. Once the token is created, you'll get to copy it momentarily, copy the token and keep it for the next step

### Connecting the Aikido App to Jira <a href="#connecting-the-aikido-app-to-jira" id="connecting-the-aikido-app-to-jira"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Jira Data Center'
3. Enter the url of your environment
4. Enter the PAT from the previous step and hit "Save"**​**

   ![Jira Data Center integration setup: enter server URL and personal access token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ea7bcbd99334f1ec8279aea3d333f6fd0bdf2e58%2Fjira-data-center_f6f0b160-29a8-4940-8cd2-0a53e76f1741.png?alt=media)
5. Once authorized, Aikido is successfully connected to Jira, enhancing your task management capabilities 🚀

   ![Jira Data Center integration settings for repo mapping, task autocreation, and default labels.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2ee2f66f0404ba302a1b0a237ddf9da89ebc570f%2Fjira-data-center_3d9b5e8e-600d-467a-9683-1c80aa0e556f.png?alt=media)

### Options for Task Creation in Jira via Aikido <a href="#options-for-task-creation-in-jira-via-aikido" id="options-for-task-creation-in-jira-via-aikido"></a>

There are two different options to create new tasks from Aikido into Jira.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

### 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the *+* in the assign column.**​**

   ![Task assignment table with add and options buttons under "Assignee" column.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fjira-data-center_41b48dfa-4002-4038-85ac-35e0f21a5378.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Action menu with options to manage, share, or adjust task settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d48713cff103c764405a9fcbcfccdbde6e7c7ee3%2Fjira-data-center_8e0eca2d-bd15-4a1a-917e-c22a19b36547.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Jira task creation form with project, assignee, scope, summary, and description fields.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8e0c4229e5124fa8d1d8f8e4cd261a3e56169e01%2Fjira-data-center_2601869d-3437-4823-b410-264c9eb9f8fb.png?alt=media)
3. The newly created task in Jira will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Critical task: var\_dump() exposes sensitive info, needs attention and assignment.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5c8af49ae0f80e42d1ed19999fe754dacbd5f5cf%2Fjira-data-center_6fd5b53d-a667-4294-b410-5caecbb3552d.png?alt=media)

### 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Jira Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable 'Autocreation' by clicking the toggle to On.
3. Define the criteria for automatic task creation.\
   ​

   ![Autocreation settings: Automatically create one task daily for critical issues or higher.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fjira-data-center_003436a4-f840-40c3-a362-f9f37b377cc1.png?alt=media)

   **​**
4. Aikido will then autonomously generate Jira tickets based on these settings 🚀

***

# Linear

*📋 Setting up automated task creation in Linear*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Linear.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Linear projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Linear, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Linear <a href="#connecting-the-aikido-app-to-linear" id="connecting-the-aikido-app-to-linear"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Linear Issues'
3. A prompt will request authorization for Linear.\
   ​

   ![Authorization prompt for Linear issue-tracking; user currently unauthorized.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-850e27321b08e82d6e5f5ba1a65ae23ae4d9483f%2Flinear_3620920b-3f02-43c8-a768-08cd22401356.png?alt=media)
4. Login into your Linear account
5. Grant Aikido permission to access your Linear workspace

   ![Aikido Security requests access to manage and comment on issues in your Linear workspace.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9adced6265021a0ff866af89265b71201fd349b9%2Flinear_5b96e403-1657-482b-b760-19f73d2bd463.png?alt=media)
6. Once authorized, Aikido is successfully connected to Linear, enhancing your task management capabilities 🚀

## ​Options for Task Creation in Linear via Aikido <a href="#options-for-task-creation-in-linear-via-aikido" id="options-for-task-creation-in-linear-via-aikido"></a>

There are two different options to create new tasks from Aikido into Linear.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

### 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assign column.**\
   ​

   ![Task management interface showing the "Assignee" column with add and options buttons.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Flinear_68a7926c-ffdc-4813-b3e0-5e25252173f7.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Dropdown menu offering task creation and additional action options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-50c4fc60bc662b3821f743b2f5d7ee7d1a3a2ab8%2Flinear_cedd6e79-044b-42d9-a646-bd611ee50265.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Task creation form for reporting a critical Content Security Policy issue in Aikido.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5a5936aaded7a55d81b8ff689a708bc6d8f8e85f%2Flinear_10e057ec-646a-497c-bef2-24c7353c91ba.png?alt=media)
3. The newly created task in Linear will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Critical task: CSP header missing, issue unassigned and currently open for resolution.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f42269839d66ff6c54219e84ac5f559aa00b31dc%2Flinear_dae76f1e-7db0-4ff3-b011-52631c0175d5.png?alt=media)

### 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Linear Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Select '**Change auto creation**'
3. Define the criteria for automatic task creation.\
   ​

   ![Autocreation settings for automatic task creation based on severity and daily limit.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Flinear_2a504784-5a18-4dac-a575-fd4f2ea7bab2.png?alt=media)

   ​
4. Aikido will then autonomously generate Linear tickets based on these settings 🚀

***

# ClickUp

*📋 Setting up automated task creation in ClickUp*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in ClickUp.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified ClickUp projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to ClickUp, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to ClickUp <a href="#connecting-the-aikido-app-to-clickup" id="connecting-the-aikido-app-to-clickup"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'ClickUp'
3. A prompt will request authorization for ClickUp.\
   ​

   ![ClickUp authorization prompt for issue-tracking; user currently unauthorized.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f596a8b23097cb626a88b2928dcbd43d3bec46f9%2Fclickup_795b1392-e60d-4492-8853-d2b4251f9fef.png?alt=media)
4. Login into your ClickUp account
5. Grant Aikido permission to access your ClickUp workspace

   ![ClickUp workspace selection screen for connecting with Aikido Security integration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c26585189847f4d665ab63ed941f0b89d184da59%2Fclickup_72bc2856-bacd-4204-a446-7984aa1e9f38.png?alt=media)
6. Once authorized, Aikido is successfully connected to ClickUp, enhancing your task management capabilities 🚀

![Map repositories to ClickUp projects and enable automatic task creation with Aikido.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8090b05b2126ec3028cb19cab5078db1f6c66c3c%2Fclickup_e419f1df-e108-4d00-ba4d-3057129c8133.png?alt=media)

## ​Options for Task Creation in ClickUp via Aikido <a href="#options-for-task-creation-in-clickup-via-aikido" id="options-for-task-creation-in-clickup-via-aikido"></a>

There are two different options to create new tasks from Aikido into ClickUp.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Assignee section with options to add or manage task assignments.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fclickup_63fe9e3c-4d1a-4724-b36c-e206e5043543.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Action menu with options: create task, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-021540fd57c14956dfe908955e17785a65e98352%2Fclickup_b05ddc73-2393-4d76-97b5-29f663068d65.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![ClickUp task creation form for reporting high-severity XSS vulnerability findings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e816c82b292bf2f77092029f21e6a0591efc3d2f%2Fclickup_368fbd17-a295-490a-b7c2-a3adecaff6df.png?alt=media)
3. The newly created task in ClickUp will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Task warning about high-risk XSS attacks from unescaped input, labeled as open.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f93a1dd3b7fcb002297069e96fbaa9278ac6cc8d%2Fclickup_7292e563-fdc4-46d8-b2d7-48bbd8567288.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [ClickUp Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.\
   ​

   ![Autocreation settings for task severity and daily task limit are enabled.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fclickup_68aa1690-fb9a-4eb9-a9ad-72c970001cc4.png?alt=media)

   ​
4. Aikido will then autonomously generate ClickUp tickets based on these settings 🚀

***

# Azure DevOps Boards

*📋 Setting up automated task creation in Azure DevOps Boards*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Azure DevOps Boards.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Boards projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Boards, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Boards <a href="#connecting-the-aikido-app-to-boards" id="connecting-the-aikido-app-to-boards"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Azure DevOps Boards'\
   A modal will request some more information to authenticate:

   * **UserID**​: this is your **email**
   * **Access Token**: Can be found inside Azure DevOps. As scope, under '**Work Items**', you can select '**Read & write**'.
   * **Organisation** ***Name*****:** name of the organisation, can be found in the URL <mark style="color:red;">Make sure to include the organisation name ONLY, without the prefix of the url https\://...</mark>\ <br>

   ![Azure DevOps integration setup screen prompting for user ID, token, and organization.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-576a9243c01363aca2a13c3d8fa8ab27964c51cd%2Fazure-devops-boards_d8185da7-4270-4757-983c-2f49135d8433.png?alt=media)
3. After filling in the credentials correctly, press save and Close the modal.\
   ​
4. Open the Azure DevOps Boards Integration page to manage the auto creation settings.\
   ​

   ![Azure DevOps Boards integration setup: map repos, enable autocreation, set default task type.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c34d515eb718263b78f7eaacb54cb95452508680%2Fazure-devops-boards_6ca66041-0504-4364-9a0c-281eee90ffa3.png?alt=media)

## Options for Task Creation in Azure DevOps Boards via Aikido <a href="#options-for-task-creation-in-azure-devops-boards-via-aikido" id="options-for-task-creation-in-azure-devops-boards-via-aikido"></a>

There are two different options to create new tasks from Aikido into Boards

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task assignment table section with add and options buttons.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fazure-devops-boards_ae1f257e-0299-4349-b6df-4992273bef04.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Actions dropdown menu with options for task management and severity adjustment.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a4e79410a509c6922b4448a3458827a1a1093e51%2Fazure-devops-boards_a9b48cf3-8614-447c-b1dd-252ae08967c8.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Azure DevOps Boards task creation form with fields for project, assignee, scope, summary, and description.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6f8e295ef602f38de07d5e15463bda8e487943ae%2Fazure-devops-boards_636e8271-d106-4556-9e2f-fb9c1cc51345.png?alt=media)

   ​
3. The newly created task in Boards will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![High-priority task: Minor upgrade for @babel/traverse, assigned to aaron aikidodev.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-41ed8008ed2475cc2914de266aa4b0757dfcf747%2Fazure-devops-boards_803ed3f1-1548-49b0-ba58-64e153b91f1a.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Azure DevOps Boards Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Select '**Change auto creation**'
3. Define the criteria for automatic task creation.\
   ​

   ![Autocreation settings for generating daily tasks on critical issues or higher.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fazure-devops-boards_b847c651-3f59-4660-8350-960a783810d7.png?alt=media)

   ​
4. Aikido will then autonomously generate Boards tickets based on these settings 🚀

***

# GitHub Issues

**Table of contents:**

* [Introduction](#introduction-)
* [Prerequisites](#prerequisites)
* [Connecting the Aikido App to GitHub Issues](#connecting-the-aikido-app-to-github-issues)
  * [Options for Task Creation in GitHub Issues via Aikido](#options-for-task-creation-in-github-issues-via-aikido)
* [Manual Task Creation](#manual-task-creation)
* [Automated Task Creation](#automated-task-creation)
  * [Setup GitHub Issues Integration Now →](#setup-github-issues-integration-now-)
  * [Discover Integration Details →](#discover-integration-details-)

## GitHub Issues

*📋 Setting up automated task creation in GitHub Issues*

### Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in GitHub Issues

Following use cases are supported :

* **Manual Ticket Addition**: Manually sync security issue tickets to GitHub Issues.
* **Automated Ticket Creation**: Automatically create and push tickets to specified GitHub Issue projects/repos.&#x20;

{% hint style="warning" %}
All issues will be automatically created in the respective repo. If you wish to disable this functionality, contact us.
{% endhint %}

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* GitHub account needs to be an organisation account
* Issues need to be enabled inside GitHub

### Connecting the Aikido App to GitHub Issues <a href="#connecting-the-aikido-app-to-github-issues" id="connecting-the-aikido-app-to-github-issues"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'GitHub Issues'
3. **Install the Issues App inside your organisation** ([Install Link](https://github.com/apps/aikido-issues/installations/new)). This is needed in order to select your organisation.\
   ​

   ![GitHub issue-tracking integration setup requires authorization and organization configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-892b2ffe71a1d5666c1a7af5d4fe637aff06ee14%2Fgithub-issues_bb36cac9-b2e2-49f3-9efc-eccad640cb18.png?alt=media)
4. Select your organisation and repos\
   ​

   ![Aikido Issues installation prompt with user selection interface.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6fa85fd0bd5abbe8ba03e1997cd54e19087bf827%2Fgithub-issues_4563a93d-56a5-4793-9297-dd32eadc05b5.png?alt=media)
5. When installed succesfully, you will get a notification on top of the page in GitHub. **Return to Aikido.**\
   ​

   ![Notification confirming "Aikido Issues" was updated for the specified user account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e4f484c8a536b4452eb9cf1659d72b0a27fead19%2Fgithub-issues_6f174321-dada-40f3-938e-635ce3e1a691.png?alt=media)
6. **Select your organisation** in the modal.\
   ​

   ![Dropdown menu for selecting an organization in settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-de468ded024a4bdb9355a8c7eb5ab4802c72489f%2Fgithub-issues_869211a2-7d05-499d-95b1-76188d6f4518.png?alt=media)
7. **Click Save.** The status will now change to **Connected.**

   ![GitHub issue-tracking integration successfully connected and ready for use.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-233f10dbcea1796acd0cfe9c4bd41a502cd4fecd%2Fgithub-issues_1816d0df-29de-4d8e-9d64-da3851964f10.png?alt=media)
8. Close the modal & open the GitHub Issues Integration page. By default all issues will be synced to the 'Default Repo'. **Contact us** if you'd like to have autosyncing issues to the respective repo.

![
](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ac22813bab7365f8b245c5a497a2fe5311a226bd%2Fgithub-issues_62e79607-05a8-4f84-b7f3-77a7009eeb62.png?alt=media)

1. You can set a Default Label that will be send for all Aikido Issues. These will be synced and appear in GitHub.​\
   ​

   ![Open GitHub issue for minor aws/aws-sdk-php upgrade, labeled low priority security fix.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-51369fd5fe250500b37224369a3b95646410b073%2Fgithub-issues_39e93b13-3513-4384-b079-1b9cba20563e.png?alt=media)

#### Options for Task Creation in GitHub Issues via Aikido <a href="#options-for-task-creation-in-github-issues-via-aikido" id="options-for-task-creation-in-github-issues-via-aikido"></a>

There are two different options to create new tasks from Aikido into GitHub Issues

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

### Manual Task Creation <a href="#manual-task-creation" id="manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task management interface showing "Assignee" column with add and options buttons.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fgithub-issues_a7a0ade6-e58d-4930-8b44-564db5251eed.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Dropdown menu with task management actions: create, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1b55c4f9f3975d4d09d36f4c8ff9b1aa21818e3b%2Fgithub-issues_7e71f2c8-d4a3-4214-9fc0-26341486d030.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Form for creating a new GitHub issue task with project, assignee, and description fields.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d4780357247803a6f09ddeb87b3883a3205c34b3%2Fgithub-issues_c876d6f9-e42b-4d14-9e16-6d8f0474d73d.png?alt=media)

   ​
3. The newly created task in GitHub Issues will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Task management dashboard showing a low-priority AWS SDK PHP upgrade task.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-bf4076136ced939ad1e21d5e45582d6280156952%2Fgithub-issues_8160a9aa-cc40-4bab-9d96-e0f9f7b3f4c6.png?alt=media)

### Automated Task Creation <a href="#automated-task-creation" id="automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [GitHub Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.\
   ​

   ![Task autocreation settings: enable automatic creation for critical issues, limited to one task per day.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fgithub-issues_9ec09e96-b743-4daf-8fcc-f333d2bcaba2.png?alt=media)

   ​
4. Aikido will then autonomously generate GitHub Issues based on these settings 🚀

***

# GitLab Issues

*📋 Setting up automated task creation in GitLab Issues*

Aikido can connect to GitLab so that you can create issues for security findings found through Aikido. For each of the findings in the 'Feed' of Aikido, a GitLab issue can be created, and linked.

You will be able to follow along in the Feed, to whom the ticket is assigned.

### 1. Set up integration <a href="#id-1-set-up-integration" id="id-1-set-up-integration"></a>

Go to <https://app.aikido.dev/settings/integrations> and scroll down to the 'Task trackers' section.

![GitLab integration for tracking and managing security issues; connect to create GitLab issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-54d911143299bee5c0b06583d2ee2b2b74fe8b81%2Fgitlab-issues_315ed60c-bb33-46de-8437-b67458cb6851.png?alt=media)

Click on 'Connect'

![GitLab authorization prompt for issue-tracking, awaiting user permission to proceed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-418cc61c9ab0094dbbe886cbb7f229bb39fa69b7%2Fgitlab-issues_bd90ccd9-fdd9-46b8-b552-d28145c3f0d7.png?alt=media)

Click on 'Authorize GitLab'

![Authorization prompt for Aikido Issues to access GitLab user's API and account data.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ff8dfbbb15b3bae70630a8967baed6cc944511ab%2Fgitlab-issues_febb5b75-7e73-4a47-8d71-e576826a89d8.png?alt=media)

And select a 'Group' for which you want to activate the integration.

Click 'Save' and you're connected.

![GitLab issue-tracking integration status: Connected.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1c60ea2ab03a0fa5921b27c964033ea10d136dcc%2Fgitlab-issues_902c3217-4139-4079-9490-3f2059fbbdab.png?alt=media)

### 2. Create a GitLab issue for a finding, inside Aikido <a href="#id-2-create-a-gitlab-issue-for-a-finding-inside-aikido" id="id-2-create-a-gitlab-issue-for-a-finding-inside-aikido"></a>

Go to the [Feed](https://app.aikido.dev/queue), and go to the security finding of choice. In the column 'Assignee', you will find the ability to assign a GitLab Issue to someone.

![Assign a new task owner by clicking the plus icon.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1c4a80c473662a23eb9f82a9c9f060066c532a94%2Fgitlab-issues_cd3756a0-ebf2-4903-9d80-6f172e7d880d.png?alt=media)

When you click on it, a popup will open.

![Task creation form for assigning and summarizing a security fix in GitLab.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c7540129cf2ae91a67956a6ec43d8047bcac2d9f%2Fgitlab-issues_2d25f8b3-11d3-4b4a-b25f-100095e4966a.png?alt=media)

When creating the Issue Task, this will be made clear in the UI of Aikido

![Open task assigned to user "roelanddel" displayed in a project management dashboard.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1ac15a6f39e427c476b18d446bdf0d794c4fe96e%2Fgitlab-issues_a34498f0-206a-444d-ae0b-2a8992cb8ab7.png?alt=media)

You're done!

### &#x20;<a href="#set-up-gitlab-issues-integration" id="set-up-gitlab-issues-integration"></a>

***

# GitLab Issues Self-Managed

*📋 Setting up automated task creation in GitLab Issues*

Aikido can connect to GitLab Self-Managed (On-prem) so that you can create issues for security findings found through Aikido. For each of the findings in the 'Feed' of Aikido, a GitLab issue can be created, and linked.

You will be able to follow along in the Feed, to whom the ticket is assigned.

### 1. Set up integration <a href="#id-1-set-up-integration" id="id-1-set-up-integration"></a>

**Step 1.** Go to <https://app.aikido.dev/settings/integrations> and scroll down to the 'Task trackers' section.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FnuPGgMepHUcoOrR89krm%2Fimage.png?alt=media&#x26;token=8fcfb609-c48d-40ba-9755-fdefa96993d7" alt="" width="375"><figcaption></figcaption></figure>

**Step 2.** Click on 'Connect' and fill in the serve base URL, the PAT and Group ID

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fw3ii38ZrQSJ5McEb2QrC%2Fimage.png?alt=media&#x26;token=f1aa66e5-d118-4b60-9fe0-bcc995fa3ff7" alt="" width="373"><figcaption></figcaption></figure>

**Step 3.** Click 'Save' and you're connected. Close the modal and you will redirected to the settings page.

### 2. Create a GitLab issue for a finding, inside Aikido <a href="#id-2-create-a-gitlab-issue-for-a-finding-inside-aikido" id="id-2-create-a-gitlab-issue-for-a-finding-inside-aikido"></a>

Go to the [Feed](https://app.aikido.dev/queue), and go to the security finding of choice. In the column 'Assignee', you will find the ability to assign a GitLab Issue to someone.

![Assign a new task owner by clicking the plus icon.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1c4a80c473662a23eb9f82a9c9f060066c532a94%2Fgitlab-issues_cd3756a0-ebf2-4903-9d80-6f172e7d880d.png?alt=media)

When you click on it, a popup will open.

![Task creation form for assigning and summarizing a security fix in GitLab.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c7540129cf2ae91a67956a6ec43d8047bcac2d9f%2Fgitlab-issues_2d25f8b3-11d3-4b4a-b25f-100095e4966a.png?alt=media)

When creating the Issue Task, this will be made clear in the UI of Aikido

![Open task assigned to user "roelanddel" displayed in a project management dashboard.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1ac15a6f39e427c476b18d446bdf0d794c4fe96e%2Fgitlab-issues_a34498f0-206a-444d-ae0b-2a8992cb8ab7.png?alt=media)

You're done!

### &#x20;<a href="#set-up-gitlab-issues-integration" id="set-up-gitlab-issues-integration"></a>

***

# JetBrains YouTrack

*📋 Setting up automated task creation in JetBrains YouTrack*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in YouTrack.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified YouTrack projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to YouTrack, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to YouTrack <a href="#connecting-the-aikido-app-to-youtrack" id="connecting-the-aikido-app-to-youtrack"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'YouTrack'\
   A modal will request the **Service URL** (of your YouTrack space) and the **Permanent Token**. The permanent token can be generated inside Profile -> Account Security in YouTrack.\
   ​

   ![JetBrains YouTrack integration setup screen requiring configuration for Service URL and token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-324f79ae66f62e7764d3fd76916e71265a0c4746%2Fjetbrains-youtrack_4b2cd46d-fffe-4903-8c91-3b2f596a08d0.png?alt=media)
3. When you have filled in the credentials correctly, the 'Connected' status will appear.\
   ​

   ![JetBrains YouTrack issue-tracking integration is successfully connected.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9cdf5b48fda4eed06398705329713d8807ac77de%2Fjetbrains-youtrack_6e0c61d5-f127-47e0-b0ba-79421e6a7dc6.png?alt=media)
4. Close the modal & open the YouTrack Integration page.\
   ​

![Map Git repositories to YouTrack projects and enable automatic task creation.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9041bf2c74162134ef849833df0df3384211ba6c%2Fjetbrains-youtrack_32e98656-e17b-4e42-9d5e-ad2611ed3541.png?alt=media)

## Options for Task Creation in YouTrack via Aikido <a href="#options-for-task-creation-in-youtrack-via-aikido" id="options-for-task-creation-in-youtrack-via-aikido"></a>

There are two different options to create new tasks from Aikido into YouTrack.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

### 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task assignment table section with options to add or manage assignees.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fjetbrains-youtrack_fd1bad1c-19b7-41d9-ba08-683817d37328.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Action menu with options: create task, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cd9fbadb30b244291b649bcf5dc8dd1b0d7978db%2Fjetbrains-youtrack_8642287d-0d10-46bf-9d0d-d25cf159d51d.png?alt=media)

   ​
2. Fill in the required details in the popup modal.\
   ​

   ![Form for creating a security task in JetBrains YouTrack with summary and details.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b1da99a1c36e0b4fe0770088171be43c8b5b7eda%2Fjetbrains-youtrack_98ce3ad1-5aca-4912-b986-17f2e2dc385c.png?alt=media)
3. The newly created task in YouTrack will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).\
   ​

   ![Security alert: HSTS header missing, high severity, reported by admin.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1fb87a2e240a65757508c64913a3e68b48a86579%2Fjetbrains-youtrack_df00a756-237c-4b53-949c-a66b981c5a56.png?alt=media)

### 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [YouTrack Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.\
   ​

   ![Automatic task creation for critical issues, limited to one task per day.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fjetbrains-youtrack_664f2728-c619-4a8c-8cde-32b8a1abaf16.png?alt=media)

   ​
4. Aikido will then autonomously generate YouTrack tickets based on these settings 🚀\
   ​

# Asana

*📋 Setting up automated task creation in Asana*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Asana.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Asana projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Asana, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Asana <a href="#connecting-the-aikido-app-to-asana" id="connecting-the-aikido-app-to-asana"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Asana'
3. A prompt will request authorization for Asana.

   ![Asana integration unauthorized; prompt to authorize access for issue-tracking.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e2dc5abffa04d6945840f96e6c202c1b8f271982%2Fasana_98d9b2b9-76e9-4a91-8726-6468e0239bf0.png?alt=media)

   ​
4. Login into your Asana account
5. Grant Aikido permission to access your Asana workspace

   ![Asana permission request for Aikido Security to access and modify your account data.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-26c32d4ac81fdb742c4ea13cbbac95667f097bf6%2Fasana_c08d4b3c-4754-43f3-b511-a0cb2dc3865d.png?alt=media)
6. Once authorized, Aikido is successfully connected to Asana, enhancing your task management capabilities 🚀

![Configure Asana integration to map repositories and enable automatic task creation.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-58c449bb7f87877e4ce10cd8c2301b97eea432fb%2Fasana_bbbaa91c-c6ce-4001-9052-308b490bc384.png?alt=media)

## ​Options for Task Creation in Asana via Aikido <a href="#options-for-task-creation-in-asana-via-aikido" id="options-for-task-creation-in-asana-via-aikido"></a>

There are two different options to create new tasks from Aikido into Asana.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task assignee section with add and options buttons visible.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fasana_a6b1ac3d-ef37-454a-a531-b366d190f292.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.

   ![Action menu with options to manage, snooze, ignore, share, or adjust task severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-de6fef3756564ef12a31b460350c1d0b23228a8f%2Fasana_487046b9-543c-4f1f-bcfc-f00f9b9edf71.png?alt=media)

   ​
2. Fill in the required details in the popup modal.\
   ​

   ![Create a ClickUp task reporting a high-severity XSS vulnerability with details and link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e816c82b292bf2f77092029f21e6a0591efc3d2f%2Fasana_22b79ff6-7c72-4889-9897-766cbe39516b.png?alt=media)
3. The newly created task in Asana will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![High-priority task warning: Unescaped input may cause XSS attacks.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f93a1dd3b7fcb002297069e96fbaa9278ac6cc8d%2Fasana_eca9cd6d-11f2-495c-88c4-db292078ec4c.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Asana Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.\
   ​

   ![Task autocreation settings for critical issues, limited to one task per day.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fasana_91aebcb9-d648-4193-ac60-f44d9aa5f37a.png?alt=media)

   ​
4. Aikido will then autonomously generate Asana tickets based on these settings 🚀

# Monday.com

*📋 Setting up automated task creation in Monday.com*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in the Monday app.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Monday.com projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Monday.com, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Monday.com <a href="#connecting-the-aikido-app-to-mondaycom" id="connecting-the-aikido-app-to-mondaycom"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Monday.com'\
   A modal will request an **API Key** (of your Monday workspace). This API key can be found in Administration -> Connections -> API.\
   ​

   ![Monday.com integration setup screen requesting API key for issue tracking configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-875f3c3e098d4dee0aa02aa1181e59d898c84d69%2Fmondaycom_4398b70e-28ca-4e9b-9b40-bf3788b6b1d9.png?alt=media)
3. When you have filled in the credentials correctly, the 'Connected' status will appear.\
   ​

   ![Monday.com issue-tracking integration successfully connected.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9a78c058627a830a2264f88b08fbec57b21ccd34%2Fmondaycom_4661f824-7819-4aff-b74b-b7dd04a0c42c.png?alt=media)

Close the modal & open the Monday.com Integration page.

![Map repositories to monday.com projects and enable automated task creation with Aikido.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5e7e807248251fc05aca0994ba37aefb1dcd1fd2%2Fmondaycom_dc426a4a-3d15-46dc-aad4-998e028ffa9f.png?alt=media)

## Options for Task Creation in Monday.com via Aikido <a href="#options-for-task-creation-in-mondaycom-via-aikido" id="options-for-task-creation-in-mondaycom-via-aikido"></a>

There are two different options to create new tasks from Aikido into Monday.com.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task assignment interface with options to add or manage an assignee.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fmondaycom_504a5b08-ce92-4bd3-b464-fa7388ff2b18.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Action menu with options to create task, snooze, ignore, copy link, or adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f5536a3335e1cc523ce45b3d7377bb96634f0dfc%2Fmondaycom_466636e8-15d6-4a23-abb5-27f748884ebe.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Task creation form for project management in monday.com, detailing a critical upgrade issue.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2520f14235e8aae5d2c2bb86930fa33f6fc02a3b%2Fmondaycom_7ed10212-15ca-4d68-afd4-6510ac747e14.png?alt=media)

   ​
3. The newly created task in Monday.com will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Critical Log4j upgrade task assigned to Maarten De Schuymer.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-45f83feaef6ed9d301bd489d96d791b93d6f4a51%2Fmondaycom_e8b64e9e-3feb-471c-9ac9-a1c89c5fba00.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Monday.com Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Select '**Change auto creation**'
3. Define the criteria for automatic task creation.\
   ​

   ![Task tracker settings for automatic task creation based on issue severity and daily limit.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-99fc126ce92c0f7fb334ea553c56470c86832fbd%2Fmondaycom_843bd00e-b2b0-4106-be92-cc720f2f6419.png?alt=media)
4. Aikido will then autonomously generate Monday.com tickets based on these settings 🚀

***

***

# Shortcut

*📋 Setting up automated task creation in Shortcut*

### Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Shortcut.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Shortcut projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Shortcut, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Shortcut <a href="#connecting-the-aikido-app-to-shortcut" id="connecting-the-aikido-app-to-shortcut"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Shortcut'
3. A prompt will request authorization for Shortcut.\
   ​

   ![Shortcut issue-tracking setup screen prompting for API key configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0d2f97cdcd985979c860e6836a652bca58bdf510%2Fshortcut_47c4c8f3-3a8c-4029-ade4-7aae235f0cf1.png?alt=media)

   ​
4. Login into your Shortcut account
5. Grant Aikido permission to access your Shortcut workspace
6. Once authorized, Aikido is successfully connected to Shortcut, enhancing your task management capabilities 🚀

![Map repositories to Shortcut teams and enable or disable task autocreation.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8d9393c5053c40cded6d209149c751ed03fc75b9%2Fshortcut_509f1035-d5ae-49e2-9213-912ca5ffda52.png?alt=media)

## Options for Task Creation in Shortcut via Aikido <a href="#options-for-task-creation-in-shortcut-via-aikido" id="options-for-task-creation-in-shortcut-via-aikido"></a>

There are two different options to create new tasks from Aikido into Shortcut.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task table section showing "Assignee" field with add and options buttons.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fshortcut_35248b32-c81f-4581-b101-909ea251588e.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Dropdown menu with task management actions: create, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4067fb2cc4f1003160a84d70590cd024877befb2%2Fshortcut_357ca834-144e-425d-80c3-e125c3b7ccd7.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​
3. The newly created task in ClickUp will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![High-priority tzinfo upgrade task, currently unassigned and open for action.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6fe8c245bf5c7526bd1514118b5f0cde09441e11%2Fshortcut_ad2fc758-eca3-4e95-94e4-7fb186aca52b.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Shortcut Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Select '**Change auto creation**'
3. Define the criteria for automatic task creation.\
   ​

   ![Task autocreation settings interface for handling critical issues, with daily task limit.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fshortcut_0db998f8-a063-4a93-a616-c08d38411906.png?alt=media)

   ​
4. Aikido will then autonomously generate Shortcut tickets based on these settings 🚀

***

# Advanced Functionalities

# Link Existing Tasks

### Introduction <a href="#introduction" id="introduction"></a>

Aikido supports the linking of existing Task Tracker (e.g. Jira, Clickup) tickets to Aikido issues, crucial for integrating already flagged security concerns in Jira that are not yet connected to Aikido.

> Note: This functionality is only available for **Jira Cloud & Data Center, Linear, ClickUp** and **AzureDevops Boards integrations**. Contact us if you are using another integration and would love to see this functionality available too!

### How to Link an Existing Task <a href="#how-to-link-an-existing-task" id="how-to-link-an-existing-task"></a>

*Following example is for Jira. Functionality is similar for other task trackers.*

**Step 1:** Click on '**Add Task**'. For issue groups: located at the top of the sidebar or in the action menu. For subissues: triple dots menu on subissue level.\
​

![Task management interfaces showing action menus for workflow and issue handling.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b64c78d9de2a5071a2385e17b182914961b76565%2Flink-existing-tasks_6f3c3573-9254-4bf5-8868-538950b88336.png?alt=media)

**Step 2:** Select 'Link to Existing Jira Ticket' at the top of the modal.

**Step 3**.Select your project and search for the name of the existing Jira ticket. You can also just paste the URL into the search bar.\
​\
​

![Interface for linking an existing Jira task by selecting project and task details.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1bc85aad3270a96326f5188d77fc9f39e997e502%2Flink-existing-tasks_b8f9f259-9a92-4fd3-9bb1-3f5501d45193.png?alt=media)

​**Step 4:** Click 'Link Jira Task' to finalize the linking process.\
​

**Step 5:** Once linked, Aikido will automatically sync any updates in assignee and status from Jira, ensuring both platforms are up to date.

***

# Smart Issue Routing: Map Teams or Repositories to Projects in Your Task Manager

## Introduction <a href="#introduction" id="introduction"></a>

Mapping your Aikido teams or repositories to projects within your Task Manager ensures that automated tasks are correctly routed to the appropriate project.

## Use Case <a href="#main-use-case" id="main-use-case"></a>

Often, you have different projects in your task tracker that map to different Aikido teams. This is helpful when you have certain teams that combine certain repos, cloud, containers and need those issues directed to a certain task tracker project.

### Step-by-Step Guide <a href="#step-by-step-guide" id="step-by-step-guide"></a>

**Step 1**: Navigate to the [**Task Manager Settings**](https://app.aikido.dev/settings/integrations/tasktracker)

**Step 2**: Select **Jira Project Mapping**.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FAAwa4DOWur6el4XacWvh%2Fimage.png?alt=media&#x26;token=dd87cf4a-af63-43b8-864c-e34802143953" alt=""><figcaption></figcaption></figure>

**Step 3: Map** your Task Tracker Projects to your Aikido Teams or Repositories

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FlbgAaHR4hjOP68i2HFsq%2Fimage.png?alt=media&#x26;token=e55449c0-e3ef-4e35-b87b-3c3a0672332e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important**: Don't forget to set a **default project**. This project acts as a fallback for any teams or repositories not explicitly mapped, ensuring no task goes unassigned.
{% endhint %}

**Extra notes**

* This option is not included in GitHub Issues / GitLab Issues.
* For Linear, we do not map the projects, but the Teams

***

# Auto-Close Linear Tasks When Aikido Issues Are Resolved / Ignored

### Use Case

When Aikido marks issues as **resolved** or **ignored**, you can sync this status with Linear to keep tasks automatically updated.

{% hint style="info" %}
Aikido checks every **8 hours** to detect and update resolved issues. Updates are **not instantaneous**, so some delay is expected between resolution and task closure.
{% endhint %}

### **Setup**

**Step 1.** Go to your [**Task Tracker Integration Settings**](https://app.aikido.dev/settings/integrations/tasktracker) in the Aikido dashboard.

**Step 2.** In the **Advanced** section, enable **Autoclose Tasks**.<br>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F6GihPWkrzcLQA0cJummE%2Fimage.png?alt=media&#x26;token=cefde62b-590f-43e4-bfee-327c8f143dd5" alt=""><figcaption></figcaption></figure>

**Step 3.** Set the corresponding **completion status** that you are using in Linear (e.g., “Done”).

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FKicmVqVs90BPsRWcQ4yM%2Fimage.png?alt=media&#x26;token=54736314-987a-431e-aadf-d400b4c18b5c" alt=""><figcaption></figcaption></figure>

**Step 4**. Hit Save in the top right

### **Troubleshoot**

* For **Linear**: if tasks don't move to “Done”, you may need to reauthorise the integration.

  * Go to **Manage Integration**
  * Click the **three dots**
  * Select **Re-authorize**

  <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F0XgLKpuvrpVM37Fi6KQu%2Fimage.png?alt=media&#x26;token=4abe09c8-dae3-4185-98ac-36aef13d47e4" alt="" width="375"><figcaption></figcaption></figure>

# Auto-Close Jira Tasks When Aikido Issues Are Resolved / Ignored

### Use Case

When Aikido marks issues as **resolved** or **ignored**, you can sync this status with Jira to keep tasks automatically updated.

{% hint style="info" %}
Aikido checks every **8 hours** to detect and update resolved issues. Updates are **not instantaneous**, so some delay is expected between resolution and task closure.
{% endhint %}

### **Setup**

**Step 1.** Go to your [**Task Tracker Integration Settings**](https://app.aikido.dev/settings/integrations/tasktracker) in the Aikido dashboard.

**Step 2.** In the **Advanced** section, enable **Autoclose Tasks**.<br>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FZghryJHTDXnSI6jBjvgD%2Fimage.png?alt=media&#x26;token=4c126c7c-1ce0-47ea-99fa-c8bd58e081ad" alt=""><figcaption></figcaption></figure>

**Step 3.** Set the corresponding **completion status** that you are using in Jira (e.g., “Done”).

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FPXjzHAKJ8BOi96GX7OLn%2Fimage.png?alt=media&#x26;token=fa30e75d-c868-4022-a87a-950a38a1e1d2" alt=""><figcaption></figcaption></figure>

**Step 4**. Hit Save Settings in the top right

# Troubleshoot Jira Task Creation: Set Up Default Issue Types

Task creation inside Aikido can fail, **particularly when the issue types that have been setup in Jira include required fields that are not available in Aikido**. The fix is to create a new issue type in Jira without any required fields, and inform Aikido about this new name.

### 1. Create a new Issue Type in JIRA <a href="#id-1-create-a-new-issue-type-in-jira" id="id-1-create-a-new-issue-type-in-jira"></a>

**Step 1:** Log in to JIRA and go to Settings > Issues > **Issue Types**

**Step 2: Add a New Issue Type**

Click *Add Issue Type*. Name it something indicative like **Security Fix**, and ensure it does not mandate any field that previously hindered Aikido task creation. This issue type must not include any required fields that Aikido cannot sync.

### 2. Configuring Aikido to Use the New Issue Type <a href="#id-2-configuring-aikido-to-use-the-new-issue-type" id="id-2-configuring-aikido-to-use-the-new-issue-type"></a>

**Step 1:** Go to [**JIRA Integration Settings**](https://app.aikido.dev/settings/integrations/tasktracker) in Aikido

**Step 2: Input the New Issue Type Name** in the default task type entry.

Enter the name of the issue type you created in JIRA (e.g., Security Fix). This links Aikido's ticket creation process with the new JIRA issue type.

![Set a default task type to "Task 2" for automatic task creation.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-31b4d143ca03b8dc4429bfc4d6ecea3c56157305%2Ftroubleshoot-jira-task-creation-set-up-default-issue-types_4d62afc3-3daa-409f-8c86-127036359b66.png?alt=media)

***

# Map Aikido Data to Jira Custom Fields

#### **Why use custom field mapping:**

* **Required fields** — If your Jira issue types have required custom fields, Aikido cannot create tickets without mapping values to them
* **Richer ticket data** — Send Aikido data like severity, SLA dates, and teams directly into Jira fields
* **Jira automations** — Use mapped field values to trigger workflows, route tickets, or set priorities automatically

#### **Simple setup**

* Just enter your Jira field names exactly as they appear in Jira
* No field IDs, API lookups, or special formatting required
* Use plain text for fixed values — just the readable name

#### **Supported Jira field types:**

* Free text: `short text` `paragraph`
* Links: `URL Field`
* Selection fields: `select list (single choice)`&#x20;
* Multi-selection fields:  `select list (multiple choice)`&#x20;
* Numbers: `Number field`
* Dates: `Date Picker`
* Datetimes: `Datetime Picker`

#### Configure Field Mappings

1. Go to [**Integrations** > **Jira** > **Jira Field Mapping**](https://app.aikido.dev/settings/integrations/tasktracker/fields/custom) and click **Add Field**<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F5Q61tL1tVo2tXEyd33ge%2Fimage.png?alt=media&#x26;token=bc92d764-32b1-41f2-b516-de3f300ef0a0" alt=""><figcaption></figcaption></figure>

2. Enter the Jira custom field name in the **Custom Field** input — just the name as it appears in Jira

3. Enter an Aikido shortcode (e.g., `$SEVERITY`) or a fixed text value in the **Aikido Value** input<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeUKSnTq0LnrumxkV4LSP%2Fimage.png?alt=media&#x26;token=545a6aef-abe4-4a81-a385-287909485ce1" alt=""><figcaption></figcaption></figure>

4. Click **Save Changes**

The **Preview** column shows what value will be sent to Jira. These can be values based on shortcodes or fixed values / free text.

#### Aikido Value: Fixed Text vs Shortcodes

**Option 1: Send Fixed Values to Jira via free text**

Enter plain text instead of a shortcode to set a constant value. Just use the readable name — no Jira IDs or special formatting needed.

For example, entering `Security` populates that Jira field with "Security" for every ticket created from Aikido.

**Option 2: Send Aikido Values to Jira via Shortcodes**

Shortcodes are placeholders that pull data from your Aikido issues. When a Jira ticket is created, the shortcode is replaced with the actual value. You can also combine shortcodes with fixed text — for example, `Issue: $TLDR` or `Detected on $FIRST_DETECTED_DATE`. Need a shortcode that's not listed? Reach out to us.

| Shortcode              | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| `$SEVERITY`            | Severity level (Critical, High, Medium, Low)                |
| `$ASSIGNEE`            | User assigned to handle the issue in Aikido                 |
| `$TLDR`                | Summary of the issue group                                  |
| `$TEAMS`               | Teams responsible for the related issues                    |
| `$SCOPES`              | Scopes/locations related to the task (repo, container, etc) |
| `$SLA_DATE`            | SLA due date                                                |
| `$SLA_TIME`            | SLA due date as a Unix timestamp                            |
| `$FIRST_DETECTED_DATE` | Date when the issue was first detected                      |
| `$FIRST_DETECTED_TIME` | First detected date as a Unix timestamp                     |
| `$AIKIDO_LINK`         | Link to the issue group in Aikido                           |

####

#### Date and Datetime Fields

For Jira **date** fields, use the `YYYY-MM-DD` format (e.g., `2024-03-15`) or the `_DATE` shortcodes.

For Jira **datetime** fields, use the `_TIME` shortcodes (e.g., `$SLA_TIME`, `$FIRST_DETECTED_TIME`). These output Unix timestamps, which Aikido automatically converts to Jira's required datetime format.

# Allowing IP Addresses for Issue/Task Tracker Integrations

If you only allows specific IP addresses to access your Issue/Task Management Systems (eg Jira, Linear,..), you will have to allowlist Aikido's IP addresses so tasks can be created and managed.

Add the following IPs:

* **18.197.244.247**
* **18.156.9.3**
* **3.65.139.215**

The ports required to be opened are at least port **443** for HTTPS.

## Third party provider instructions <a href="#third-party-provider-instructions" id="third-party-provider-instructions"></a>

For instructions on whitelisting IP addresses with third-party providers, refer to the following resources:

* [Cloudflare WAF](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/)
  * Cloudflare Turnstile does not support allowlisting specific client IP addresses. If you need to [bypass Turnstile for Aikido scanning traffic, you must do it in your application code.](https://developers.cloudflare.com/turnstile/tutorials/conditionally-enforcing-turnstile/) We recommend bypassing only when both conditions are true:
    1. The request originates from an Aikido IP range
    2. The request includes the `aikido` User Agent in headers as described above
* [Azure WAF](https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/custom-waf-rules-overview)
* [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-ipset-match.html).
  * For WAFs behind Application Load Balancers or CloudFront, your [WAF should check the last IP address in the `X-Forwarded-For` header](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-forwarded-ip-address.html).
* [Vercel WAF](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules)
  * Use the ["bypass" action](https://vercel.com/docs/vercel-firewall/firewall-concepts#bypass) for trusted IPs

{% hint style="info" %}
[The IP address lists are also available as JSON arrays](https://aikido.help/ips/)
{% endhint %}

# Chat & Alerts

# Slack Notifications

## Connecting the Aikido Slack app to Slack <a href="#connecting-the-aikido-slack-app-to-slack" id="connecting-the-aikido-slack-app-to-slack"></a>

Go to [the Slack integrations settings](https://app.aikido.dev/settings/integrations/notifications/slack) inside of the Aikido app.

1. Click **"Add integration"**
2. Select **the Slack workspace** you'd like to use on the top right dropdown
3. Select **the channel** you'd like to post to from the dropdown menu
4. Click "**Allow**"

Repeat this process by clicking **"Add Channel"** in case you'd like to use different channels for different notification types.

## Adding the Aikido Slackbot to a private channel <a href="#adding-the-aikido-slackbot-to-a-private-channel" id="adding-the-aikido-slackbot-to-a-private-channel"></a>

To add the Aikido Slackbot to a private channel, you first need to invite the bot to that channel. Otherwise you're not able to select that channel. (This is so for all Slackbots)

1. **Type "@Aikido Security"** in the channel & send the message
2. You'll get a popup asking if you'd like to add Aikido to the channel
3. **Click "Add to Channel"**

![Slack prompt suggesting to add a user to a channel before messaging the whole group.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c1f09419e912e94bfa72100946d0ccfb4432193d%2Fslack-notifications_41bc0618-352e-4cb8-a9d3-feb62fd3ea02.png?alt=media)

Now you should be able to find your private channel in the app.

Next, go [to Slack integration settings](https://app.aikido.dev/settings/integrations/notifications/slack) in the Aikido app.

1. **Enable the toggles** for the types of notifications you'd like to get
2. **Select the channels** you'd like the notifications to arrive in.
3. Hit "**Save**"

### Alternative method <a href="#alternative-method" id="alternative-method"></a>

Alternatively you can add the bot in the following steps:

1. Navigate to the channel you'd like to add the Slackbot to
2. Click the dropdown arrow
3. Navigate to the "Integrations" tab
4. Click "Add an App"
5. Search for "Aikido Security" and click "Add"

Now you should be able to find your private channel in the app.

![Slack channel integrations tab showing options to add workflows or apps, with buttons highlighted.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ce84233ec26f9541d38e5a3f7f4136a8fa097ba3%2Fslack-notifications_0d1b4b61-2ef7-4bb9-895e-d4366f1ae233.png?alt=media)

***

# Send Alerts to Multiple Slack Channels

## Introduction <a href="#introduction" id="introduction"></a>

Streamline your security response with Aikido by setting up tailored alerts to be sent to designated Slack channels. This guide will help you ensure that your team receives timely and relevant security notifications.

## Setting Up Slack Alerts <a href="#setting-up-slack-alerts" id="setting-up-slack-alerts"></a>

*Prerequisites: Ensure your Slack integration is active. You can find how to set up the Slack Integration* [*here*](https://help.aikido.dev/en/articles/8153269-how-to-set-up-slack-notifications)*.*

#### Step 1: Create an Alert <a href="#step-1-create-an-alert" id="step-1-create-an-alert"></a>

* Navigate to the [Slack integration page](https://app.aikido.dev/settings/integrations/notifications/slack) and click ‘Create Alert’ to bring up the configuration modal.

#### Step 2: Opt for Team-Based Notifications <a href="#step-2-opt-for-team-based-notifications" id="step-2-opt-for-team-based-notifications"></a>

* Choose 'Team-based' to route alerts to specific channels. Preconfigure your Teams with the right repositories and containers access.

![Configure Slack alerts for all users or specific teams with custom options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0676edac65b43e18714d4578cdee12129094671c%2Fsend-alerts-to-multiple-slack-channels_d97b50e1-80b2-44fa-918e-6ac469f5c347.png?alt=media)

#### Step 3: Map Channels to Teams <a href="#step-3-map-channels-to-teams" id="step-3-map-channels-to-teams"></a>

* For **Weekly Digests**, link a channel for summaries of weekly security issues.
* For **Critical Issues**, link a channel for real-time alerts on urgent vulnerabilities.

![Notification channels selection for weekly digest and critical issues alerts.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6c8fa38da63622e2309db7389eab9f8398167106%2Fsend-alerts-to-multiple-slack-channels_dc27e6fd-2e3e-4d96-ab27-52f038d1ced8.png?alt=media)

> Note: you can decide to only pick one of the two options to create alerts.

#### Step 4: Save Your Configuration <a href="#step-4-save-your-configuration" id="step-4-save-your-configuration"></a>

* Confirm your choices and click 'Save Alert' to activate the alerting system.

## Implementation Tips <a href="#implementation-tips" id="implementation-tips"></a>

* Regularly review and correct team settings in Aikido to maintain alert accuracy.
* Confirm that the Slack channels correspond to the correct teams to ensure proper communication

***

# Microsoft Teams Notifications

## Connecting Aikido to Microsoft Teams <a href="#connecting-aikido-to-ms-teams" id="connecting-aikido-to-ms-teams"></a>

{% hint style="warning" %}
Please note that only **Aikido admin users** can link a new Microsoft Team to your Aikido workspace.

If you are using the **OLD version** of the Microsoft Teams Integration, **please delete all alerts** before setting up the new version. You can setup the new version by removing the integration and then following the steps below.\
\
App requires application-level permissions; access is limited to the Microsoft it's installed in, not the whole org.
{% endhint %}

Follow these steps to connect Aikido to Microsoft Teams:

#### Step 0. Uninstall the MS Teams Integration v1  <a href="#id-1-click-add-integration" id="id-1-click-add-integration"></a>

In case you are still running the old MS Teams integration, first **uninstall** this one from the Aikido UI!

#### Step 1. Install the Aikido app in Microsoft Teams <a href="#id-1-click-add-integration" id="id-1-click-add-integration"></a>

* Open the [Aikido app](https://teams.microsoft.com/l/app/c2baec07-db8a-49de-b066-c0ddc19cc9c0?source=store-copy-link) in the Microsoft Teams app store and click "Add to a Team". &#x20;
* Select a channel for initial installation. You can configure alerts for all public channels of the selected Team later.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FOklwJhIen3C1ZFhAFTLG%2FScreenshot%202025-07-23%20at%2009.59.32.png?alt=media&#x26;token=a2634453-f7bd-44b3-b09d-546d4212c5a2" alt="" width="563"><figcaption><p>Select the team to which the messages should be sent.</p></figcaption></figure>

You can find more information on how to install an app on Microsoft Teams in [this Microsoft support article](https://support.microsoft.com/en-us/office/add-an-app-to-microsoft-teams-b2217706-f7ed-4e64-8e96-c413afd02f77).

#### Step 2. Link the Microsoft Team to an Aikido workspace <a href="#id-2-select-which-ms-teams-team-youd-like-to-connect" id="id-2-select-which-ms-teams-team-youd-like-to-connect"></a>

* The Aikido bot will send a message to the selected Microsoft Team channel. Click "Open Aikido" and log in.&#x20;
* Complete the app setup by confirming the installation in the modal.&#x20;

![Select a Microsoft Teams group to connect with Aikido integration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fx6GXiBlZRtF4Kbuiwu45%2FScreenshot%202025-07-23%20at%2010.07.48.png?alt=media\&token=ff5bb126-5f46-4aa1-b170-896d553ec03e)

#### Step 3. Configure the alerts you'd like to receive <a href="#id-3-configure-the-alerts-youd-like-to-receive" id="id-3-configure-the-alerts-youd-like-to-receive"></a>

{% hint style="warning" %}
Due to limitation on Microsoft side, some public channels may not be discovered automatically. You can add them manually by selecting "Public channel missing..." in the channel selection options.
{% endhint %}

Once the connection to Microsoft Teams was successful, you can start adding alerts.

* Choose whether you want to send global or team-based notifications
* Choose for which severity types
* Choose for which issue types

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FtMjPMGmY1m7rsB4J5xMn%2Fimage.png?alt=media&#x26;token=5834d2d4-bec8-4e1a-86a5-b7a463f129f1" alt="" width="375"><figcaption></figcaption></figure>

***

## Unlinking Aikido and Microsoft Teams

1. Open the Microsoft Teams app and right click on the team where the Aikido bot is installed.&#x20;
2. Click **Manage team** and select the **Apps** tab.&#x20;
3. Search for the Aikido app in the list of installed apps, click on the three dots next to it, and select **Remove**.&#x20;
4. Confirm the removal in the pop-up dialog. All settings for this team will be deleted automatically.

***

## FAQ

<details>

<summary>Can I link multiple Teams to one Aikido Workspace?</summary>

Yes, this is possible. Just follow the same steps again.

</details>

<details>

<summary>Is it possible to link multiple Aikido Workspaces to one Microsoft Team?</summary>

To link additional workspaces to the same Microsoft Team, click the button "Link another workspace" in the confirmation message sent by Aikido to your selected Teams channel. You will find theses message inside the Microsoft channel where you first installed the Aikido App. Please **do not** try to install the app multiple times.

</details>

<details>

<summary>How can I receive alerts in a private channel?</summary>

This is not easily possible due to restrictions imposed by Microsoft. We recommend creating a private Team with a public channel instead. But we describe a [workaround on this page](https://help.aikido.dev/docs/getting-started/chat-and-alerts/send-alerts-to-private-microsoft-teams-channels).

</details>

<details>

<summary>I don't receive the "Connect to Aikido" chat message</summary>

Please ensure that no moderation settings are configured for the selected channel that prevent bots from sending messages. Uninstall the app and try the process again using a different channel. If this does not help, please contact the Aikido support team.

</details>

<details>

<summary>Can I use the app in the Government Community Cloud (GCC)?</summary>

This is currently not possible. Please contact us to let us know that you would like to use our Teams app in a GCC environment.

</details>

***

# Send Alerts to Private Microsoft Teams Channels

Because Microsoft Teams apps can't be member of a private Teams channel, additional setup is required to send alerts to a private channel. The reason for this is a technical limitation in Microsoft Teams that exists since several years and was not solved until now. In some cases it might be easier to create a new MS Team instead, and only allow authorized people access to this team. Please note that alerts in private channels will be send as the user who has performed the setup steps and not as Aikido.

***

Follow these steps to send alerts to a private Microsoft Teams channel:

{% stepper %}
{% step %}

### Install the Aikido app

If not already done, follow the steps described on this page: [ms-teams-notifications](https://help.aikido.dev/docs/getting-started/chat-and-alerts/ms-teams-notifications "mention")
{% endstep %}

{% step %}

### Create the Workflow

Select the private channel that should receive the alerts, click on "More Options" (the three dots) and select "Workflows".

Select **"Send webhook alerts to a channel"**. After that enter a name for the workflow and click on "Next".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FBJrk33HQ5uvMY3fwVHeb%2Fevents%2C%20alerts%2C%20or%20custom%20triggers--%20withous.png?alt=media&#x26;token=3341bb54-da0f-489b-80b5-39e649beb6cd" alt="" width="563"><figcaption><p>Create a new Workflow</p></figcaption></figure>

Select the Microsoft Team and the private channel where the alerts should be sent. Finish the creation by clicking on "Add workflow".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FXsY4czeXgYXVAhr2CTuu%2Fevents%2C%20alerts%20or%20custom%20triggers--%20withous.png?alt=media&#x26;token=c51b40be-65cc-4e65-9f45-3d731cecd4fa" alt="" width="563"><figcaption><p>Select Microsoft Team and private channel</p></figcaption></figure>

Copy and save the workflow URL using the copy button. You need this URL later. Do **not** click on "Done".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FflYY0yMq7e8eERyWu3LX%2FPasted%20Graphic%203.png?alt=media&#x26;token=b0c52521-f23b-4964-9094-776141d703f4" alt="" width="563"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Edit the Workflow

The workflow is configured to send messages as the Power Automate bot, but this bot cannot send messages to private channels either.

Click on "Manage your workflow" in the left bottom corner of the dialog and then on "Edit" on the top left. Expand the "Attachment is null" section by clicking on it. Modify the "Post card in a chat or channel" action and select "User" for the "Post as" setting as shown in the following screenshot. Make sure to save your changes after that.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FSYRMkpBhYBPaN3zTDjCe%2FScreenshot%202026-01-28%20at%2013.18.23.png?alt=media&#x26;token=5fac63fc-886e-445f-ba85-bf482d79dfe8" alt=""><figcaption><p>Modify Workflow</p></figcaption></figure>
{% endstep %}

{% step %}

### Finish setup

Open the Microsoft Teams integration page and click on "New alert". Inside the channel select input, click on "Link a different private channel". After that the following dialog is opened. Select the Microsoft Team and enter the channel name and  the workflow URL. Click on "Add Channel" to finish the setup.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Ff2amCF4FsfMQbEMwArHz%2Fimage.png?alt=media&#x26;token=1c575c72-e9d2-4868-935f-be4f2db58269" alt="" width="563"><figcaption><p>Finish the connection</p></figcaption></figure>
{% endstep %}

{% step %}

### Confirm successful setup

After clicking on "Add Channel", you should receive the message "This channel has been successfully added to Aikido." in your private Microsoft Teams channel.
{% endstep %}
{% endstepper %}

# Reachability Analysis

# Introduction to Reachability Analysis

Learn how Aikido helps you identify which vulnerabilities are exploitable.

Aikido’s reachability analysis is focused on identifying whether a vulnerability is actually exploitable in the context of your application. Instead of flagging every vulnerable dependency or risky pattern as equally critical, Aikido builds a graph of modules, functions, and data flows within your codebase. It then asks a key question: ***Is there an execution path from real application behavior to the vulnerable code?*** Only when such a path exists is the finding considered truly security-relevant.

### Conceptual Overview

At a high level, Aikido constructs an abstract program graph in which:

* **Nodes** represent functions, methods, modules, files, and sometimes higher-level components.
* **Edges** represent relations such as function calls, imports, dependency inclusion, and data-flow between variables and parameters.

Vulnerabilities are anchored at specific nodes in this graph (for example, a known vulnerable function in a third-party library, or a sink such as a SQL execution point). Aikido then computes whether there exists a path from **entry points** (HTTP handlers, CLI commands, background jobs, etc.) to these vulnerable nodes. If no such path exists under the current code and configuration, the vulnerability is treated as non-reachable for that project revision.

In this way, reachability transforms a flat list of alerts into a structured subset of issues that are provably connected to real program behavior.

### Types of Reachability

Aikido uses several complementary notions of reachability. They share the same foundation, but operate at different levels of abstraction:

| Type                     | Scope                       | Main Question                                            | Typical Signals                                    |
| ------------------------ | --------------------------- | -------------------------------------------------------- | -------------------------------------------------- |
| **Dependency-level**     | SCA / package dependencies  | “Does the project ever call into the vulnerable symbol?” | Imports, symbol references, dependency manifests   |
| **Function-level**       | SAST / taint analysis       | “Can untrusted input flow into a dangerous sink?”        | Sources, sanitizers, sinks, inter-procedural flows |
| **Contextual (runtime)** | Build & runtime environment | “Does this code execute in the actual runtime context?”  | Prod vs dev deps, dead code, build-only tooling    |

These categories are not mutually exclusive. A typical Aikido finding may be filtered first by dependency-level reachability, then refined by function-level reachability, and finally reinterpreted in the context of how the project is built and deployed.

### How Reachability Works

#### 1. Graph construction

For each project, Aikido constructs a lightweight, language- and framework-aware graph:

* **Structural relations**: imports, requires, module references, inheritance, and other static relationships.
* **Call relations**: function calls, method invocations, event handlers.
* **Data-flow relations**: propagation of potentially tainted data through variables, parameters, and return values.

This graph is intentionally approximate but designed to preserve the properties needed to answer “is there a path?” questions efficiently.

#### 2. Anchoring vulnerabilities

The scanners then map each raw finding to one or more *anchor points* in the graph:

* For **SCA**, the anchor is usually a vulnerable symbol (a specific function, class, method, or module) associated with a CVE or advisory.
* For **SAST**, the anchor is a code location of interest, often a security sink such as `exec`, SQL queries, file system access, or deserialization.
* For **infrastructure scans**, anchor points may correspond to images, packages, or configuration elements that participate in the runtime execution environment.

#### 3. Reachability queries

Given a set of entry points and anchor nodes, Aikido asks reachability questions of the form:

> “Is there at least one valid execution path from any entry point to this anchor, under the current build and configuration?”

Algorithmically, this reduces to graph reachability (forward or backward traversal) constrained by language semantics and configuration knowledge. For data-flow analysis, the reachability relation is enriched with t**aint information**: a path is only considered security-relevant if untrusted data is able to traverse it without being fully neutralized by sanitization.

#### 4. Integration with triage and prioritization

Reachability is applied *before* higher-level triage:

* Findings with **no reachable path** are removed or heavily downgraded.
* Findings with a **clear, explainable path** are retained and passed to later stages (e.g., risk scoring, business impact analysis).
* Developers can inspect the concrete path (call stack and data-flow) to understand how the issue becomes exploitable.

This pipeline ensures that most “cry-wolf” findings are filtered out at the structural level rather than simply hidden behind severity tuning.

### Effects on Findings and Workflow

Reachability analysis has several practical consequences for how teams experience Aikido:

1. **Noise reduction**

   Many alerts produced by traditional tools stem from dependencies that are present but never invoked, or from code paths that are effectively dead. By eliminating issues without a demonstrable execution path, Aikido substantially reduces false positives and redundant tickets.
2. **More meaningful severity**

   Severity is no longer just a property of the CVE or rule; it is a property of the CVE *plus* the project’s usage. A medium-severity library issue that is deeply embedded on a hot path may be more urgent than a high-severity issue in a dev-only tool that is never executed in production.
3. **Developer-aligned explanations**

   Showing the concrete path (“request handler → service → library function → vulnerable symbol”) reframes security findings as recognizable program behavior. This lowers the cognitive overhead for developers and makes remediation efforts more targeted and efficient.
4. **Stable signal over time**

   Because reachability is recomputed as code and dependencies change, the issue backlog tracks actual architectural evolution. As dead dependencies are removed or code is refactored, previously reachable findings may transition to non-reachable, and vice versa, providing a dynamic, architecture-aware view of risk.

### Limitations and Design Choices

Aikido’s reachability engine is built as a ‘conservative **under-approximation**’—it only marks code as unreachable when it can be determined with high confidence. Dynamic language features like reflection, dynamic imports, metaprogramming, or complex build steps can make parts of the call graph unclear or invisible. In these ambiguous cases, Aikido errs on the side of caution: instead of suppressing a potentially relevant issue, it will either keep it as-is or lower its severity.

This trade-off strikes a balance between two goals:

* Reducing noise by filtering out issues that are definitely not reachable at runtime.
* Preventing a false sense of security when reachability can’t be determined with certainty.

### Summary

Reachability analysis in Aikido maps how different parts of your application are connected—tracing function calls, data flows, and interactions between components across source code, dependencies, and infrastructure. A vulnerability is only treated as a real risk if there’s a clear, executable path from an application entry point to the vulnerable behavior. By embedding this reasoning into every scanner and integrating it tightly with triage, Aikido transforms a large, noisy stream of raw alerts into a smaller, high-confidence set of findings that more accurately reflect how attackers could exploit the system in practice.

# Reachability Analysis Examples in Aikido

Aikido combines 100+ custom rules to reduce false positives and irrelevant alerts. Most of those ground rules are powered by our own reachability analysis engine.

When Aikido detects a known vulnerability in your dependencies or first-party code, it checks whether your application can actually call into the vulnerable code path. In practice, we build a lightweight call/dependency graph and trace references from your code to the functions/classes known to be affected. If the vulnerable code isn’t reachable (or is only used in non-production contexts like tests or tooling), the alert is downgraded or suppressed.

This results in significant noise reduction compared to legacy scanners that report every vulnerable package regardless of usage.

{% hint style="info" %}
Note: We continuously extend this mechanism across languages and ecosystems to further improve noise suppression.
{% endhint %}

#### **Example 1:** **You're not using the affected function**

Aikido’s internal knowledge base indicates that **CVE-2020-7774** only affects the `setLocale` function. If our analysis sees that your codebase never references `setLocale`, you’re not affected. Aikido will downgrade the issue and continue to monitor future changes in case the function starts being used.

![Security analysis found no usage of CVE-2020-7774 vulnerability in repository.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-08c143960fd7b7eb4055bd4942556f0d419e69b1%2Freachability-engine-to-remove-false-positives_2ab4f164-e024-42a0-8bf2-d050225cdf03.png?alt=media)

#### **Example 2:** **Vulnerable package used only in tooling**

The JS package `minimatch` is vulnerable, but we detect it’s only pulled in by `eslint` and `mochajs`. Because these are linting/testing dependencies and are not shipped to production, your end-users are not exposed. Aikido downgrades the issue accordingly.

#### **Example 3:** Dead dependency path

A package (`path-parse`) is known to have a CVE and is required by `pug`. Our trace shows `pug` is no longer used by your application (no imports/references, or it’s excluded from your build). In this case, the CVE can be safely discarded.

![Dependency reachability analysis for CVE-2021-23343 showing vulnerable package path in repository.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-04dc8499ce0f042d9e139978b0990ffdae5b4049%2Freachability-engine-to-remove-false-positives_fda1c7f6-1cba-439e-af75-38faf58cca3e.png?alt=media)

***

### How Aikido makes the call

* **Call/dependency graphing:** We map how your code imports and calls into packages, and then follow edges toward functions tied to a CVE.
* **Context awareness:** We distinguish production runtime code from dev and test tools (such as linting, test, or build code), so tooling-only usage won’t trigger production-impacting alerts
* **Guarded downgrades:** Findings are downgraded or suppressed only when the vulnerable symbol is provably unreachable. If evidence changes (such as with a new import), the severity is automatically reevaluted.

### Additional things to keep in mind

* **Heuristics and build setups:** Highly dynamic patterns, custom loaders, or unusual build steps can obscure call graphs. Some issues may be kept at a higher severity if usage is unclear.
* **Transitive changes:** Updating indirect dependencies can make previously unreachable code reachable. Aikido continually rechecks after dependency updates and code changes

# Scanning Configurations

# Aikido Security Checks

### Introduction <a href="#introduction" id="introduction"></a>

Aikido uses a robust array of security checks. We categorize these checks within specific overviews—Repository, Cloud, Container, and Domain—making it straightforward for you to access and understand the kind of security measures in place.

### Checks <a href="#checks" id="checks"></a>

* [**Repository Scanning checks**](https://app.aikido.dev/repositories/checks): Get insights into the checks for OSS, Secrets, Licences, SAST, IaC, Malware Detection and Mobile Issues
* [**Cloud Configuration Checks**](https://app.aikido.dev/clouds/checks)**:** You can filter on the type of cloud(s) you use for an easy overview.
* [**Container Scanning Checks**](https://app.aikido.dev/containers/checks): Open source dependency monitoring and end-of-life runtimes
* [**Domain Scanning Checks**](https://app.aikido.dev/domains/checks)**:** Checks for your domains and API's

### Other recommended views <a href="#other-recommended-views" id="other-recommended-views"></a>

* [**Overview of licenses and license groups**](https://app.aikido.dev/licenses)
* [**Malware Scanning**](https://app.aikido.dev/reports/malware/software-supply-chain-attacks)
* [**Runtimes and Frameworks**](https://app.aikido.dev/reports/runtimes)

# SAST/IaC: Supported Languages and Security Focus

### How Aikido SAST currently works <a href="#how-aikido-sast-currently-works" id="how-aikido-sast-currently-works"></a>

Aikido’s SAST engine is built to find and prioritize security issues in your code. No noise, just the vulnerabilities you need to fix.

Aikido SAST engine is based on our **custom risk categorisation model**. Some of these categorisation: -

* Aikido removes findings that are not related to security (eg opinionated code styling rules).
* Findings that reside in repositories that a user categorized as sensitive will get upgraded.
* Findings inside of files that are not intended for production (eg unit tests or functions that aren't used in production) might get downgraded and so on.

Our SAST engine also leverage some of the best open-source engines out there, which we have significantly customized and fine-tuned to provide you sharper, relevant results over the years.

To view all individual rules that are active per language, check out our [SAST Checks](https://app.aikido.dev/repositories/sast) or [Infrastructure as Code](https://app.aikido.dev/repositories/iac) checks to view the rules per language.

### Language support <a href="#language-support" id="language-support"></a>

Aikido is not sensitive to the versions of languages. By default, we support all versions.\
Aikido supports tracking tainted user input from top-level controllers to other files where dangerous functions are used for a growing set of languages.

| **Language**                                                                 | **Base engine**                                    | **Taint analysis**    |
| ---------------------------------------------------------------------------- | -------------------------------------------------- | --------------------- |
| JavaScript                                                                   | Aikido Engine + Opengrep                           | Across multiple files |
| Typescript                                                                   | Aikido Engine + Opengrep                           | Across multiple files |
| PHP                                                                          | Aikido Engine + Opengrep                           | Across multiple files |
| .NET/C#                                                                      | Aikido Engine + Opengrep                           | Across multiple files |
| Java                                                                         | Aikido Engine + Opengrep                           | Across multiple files |
| Rust                                                                         | Aikido Engine + Opengrep                           | Across multiple files |
| Go                                                                           | Aikido Engine + Opengrep                           | Across multiple files |
| Ruby                                                                         | Aikido Engine + Opengrep                           | Across multiple files |
| Python                                                                       | Aikido Engine + Opengrep                           | Across multiple files |
| Scala                                                                        | Aikido Engine + Opengrep                           | Within files          |
| C/C++                                                                        | Aikido Engine + Opengrep                           | Within files          |
| Swift                                                                        | Aikido Engine + Opengrep                           | Within files          |
| Android                                                                      | Aikido Engine + Opengrep                           | Within files          |
| Kotlin                                                                       | Aikido Engine + Opengrep                           | Within files          |
| Dart                                                                         | Aikido Engine + Opengrep                           | Within files          |
| Elixir                                                                       | Aikido Engine + Opengrep                           | Within files          |
| Apex                                                                         | Aikido Engine + Opengrep                           | Within files          |
| Clojure                                                                      | Aikido Engine + Opengrep                           | Within files          |
| Visual Basic                                                                 | Aikido Engine + Opengrep                           | Within files          |
| Infrastructure-as-code files (Terraform, Cloudformation, Docker, Pulumi,...) | Aikido Engine + Checkov                            | Not applicable        |
| Exposed secret discovery in all files inside of Git history                  | Aikido Base Engine with Liveness Checks + Gitleaks | Not applicable        |

# Scanning Frequencies

Aikido provides default scanning frequencies for various components to ensure security and performance. Here, you'll learn about these defaults and how to change them.

### Scanning Frequencies <a href="#scanning-frequencies" id="scanning-frequencies"></a>

* By default, for all paid plans, Aikido does **daily** scans for open-source dependencies, SAST, IaC, secrets, cloud, containers, and Front-End Domains.
* Domains scanned with Hosted Domains and APIs are by default done **twice a week** as this has a higher load on your system.
* In case you quickly want to verify whether a fix was implemented correctly, you can trigger a **manual scan** by clicking 'Start Scan' in the UI.

  ![Repositories page showing 9 active repos and a prominent "Start Scan" button.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fcbe998577438b0fd3fe84c23bd2b5f0e13db781%2Fscanning-frequencies_e678ed08-9cb8-4f4f-a651-7ca041202b17.png?alt=media)

> Workspaces on a free plan are scanned every 3 days, and users cannot trigger scans manually. Hosted domains are scanned once a week.

### Changing Scanning Frequency <a href="#changing-scanning-frequency" id="changing-scanning-frequency"></a>

In case you want to change your scanning frequency, you can do this by going to [Advanced Settings](https://app.aikido.dev/settings/advanced) (admins only) and click **Change Scanning Frequency**.

![Set automated scan frequency: daily, every 3 days, weekly, or monthly.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ef470ef8e18ca1021a301bc3c79060a7829f1eec%2Fscanning-frequencies_e91e1100-9205-4824-af06-f00bf304e481.png?alt=media)

# Improve Risk Scoring for Repositories and Containers

**Setting repo and container sensitivity to reduce noise**

Aikido allows you to add contextual info to all your repositories and containers to improve noise reduction. This info can help Aikido uncover more security risks and improves issue scoring. For example

* Adding info about the data sensitivity of each repo improves prioritisation and reduces noise. An issue found in a code repo that is responsible for handling personal information will be scored higher than a repo that never touches any sensitive data.
* Adding a domain name can allow Aikido to scan for issues including SSL, cookie misconfiguration, XSS attacks,..

### Configure Repository and Container Sensitivity <a href="#configure-repository-and-container-sensitivity" id="configure-repository-and-container-sensitivity"></a>

**Step 1.** Navigate to [Repositories](https://app.aikido.dev/repositories) overview or [Container](https://app.aikido.dev/containers) overview

**Step 2.** Click on the triple dots to open the action menu and select **Configure**

![Repository dashboard with critical alert; "Configure" option highlighted in actions menu.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4beefb6cd09d80212fa2459502fd1933d54243d4%2Fimprove-risk-scoring-for-repositories-and-containers_832117bd-88d8-403a-abf1-9745f3379814.png?alt=media)

**Step 3.** A modal pops up with different settings.

![Configuring security settings and domain details for the demo-app-1 repository.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6a995711044554d1dd4423657e96b7c0ae3c025a%2Fimprove-risk-scoring-for-repositories-and-containers_7e404a94-3fa2-4f4e-8b21-cac89328170f.png?alt=media)

* **Connection to the internet**: For each repository, you can specify whether the service/repository is connected to the internet via HTTP(S). There are three options:
  * Yes: Select this option if the repository is accessible over the internet using HTTP(S).
  * No: Choose this option if the repository is not connected to the internet.
  * Unknown: If you're unsure about the repository's internet connection status, select this option.
* **Specify the Domain** (if applicable): If the repository is connected to the internet, you can provide the domain of the service (e.g., <https://example.com>). This will activate Aikido's dynamic testing for surface monitoring (DAST).
* **Setting Sensitivity Levels**
  * Choose Sensitivity Level: Aikido allows you to define the sensitivity level of the data managed by each service/repository. This helps tailor the scanning process to the importance of the data. Sensitivity levels range from "Not Sensitive at All" to "Extremely Sensitive."
  * For each repository, choose the sensitivity level that best represents the data it manages. Consider the nature of the data, its confidentiality, and potential impact if compromised.
  * Updating the sensitivity level will influence the scoring mechanism of Aikido

    ![Data sensitivity setting impacts issue severity score by -5 for non-sensitive data.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-187df50f1f43bd9325a22136a8d485b837e2d3de%2Fimprove-risk-scoring-for-repositories-and-containers_041e2f1e-c2ad-4d23-bc10-5d2f59d4e45f.png?alt=media)

***

# Generate SBOM Based on Open-Source Packages

Aikido allows you to export both **SBOMs (Software Bill of Materials)** and **VEX (Vulnerability Exploitability eXchange)** files—giving you visibility into your software components and helping you prioritize what actually needs fixing.

**Use Cases:**

* **SBOM Export** (CycloneDX 1.6 , SPDX-2.3 or CSV)
  * Share with customers for compliance (e.g., ISO 27001, SOC2).
  * Feed into third-party risk or procurement tools.
* **VEX Export** (CycloneDX only)

  * Clearly flag which vulnerabilities are **exploitable** and which are **not applicable**.

## Where to find the SBOM <a href="#where-to-find-the-sbom" id="where-to-find-the-sbom"></a>

**Step 1.** Go to Reports > [Licenses & SBOM](https://app.aikido.dev/licenses)

**Step 2.** Download SPDX, CycloneDX or CSV SBOM via the top right action

![Python package license risks overview with filters and SBOM download option.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-46f4f8c55314ffff07437cd1b2ca77ea4c832a79%2Fgenerate-sbom-based-on-open-source-packages_74772dd0-d436-4829-9063-800bb19bb697.png?alt=media)

**Optional.** Filter licenses on different parameters and export the SBOM after. The export takes into account the chosen filter values.

![Filter menu for searching repositories by license, language, risk, and container options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6f6b8a2c274b7b7996cb1cd7814b34a3aa1062f8%2Fgenerate-sbom-based-on-open-source-packages_f7c910f2-edc1-4859-a464-b0155cc6d093.png?alt=media)

If you want to filter on team, you can do this via changing the Team Filter on the top of the page.

![Team selection dropdown for viewing Licenses & SBOM reports.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-644f5ae98897b1517a5dcf159e59369384237810%2Fgenerate-sbom-based-on-open-source-packages_156d14a3-4155-4ba9-bc53-1f4dff0152b5.png?alt=media)

> If you have multi-branch scanning enabled, you can get different SBOMs per legacy branch by selecting the specific legacy branch repo in the dropdown. Contact us via in-app chat for more info.

### Generate and Export via API <a href="#generate-and-export-via-api" id="generate-and-export-via-api"></a>

Aikido also supports generation and download of SBOM via API. More information can be found in our [Apidocs.](https://apidocs.aikido.dev/reference/exportcoderepolicenses)

# Add Custom SAST & IaC Rules

## Introduction <a href="#introduction" id="introduction"></a>

With these custom rules you can make Aikido scan for specific risks in your codebase, especially those risks that are particularly relevant for your environment. This way you can detect vulnerabilities that broader SAST or IaC rules might overlook.

## Step-by-Step Guide <a href="#step-by-step-guide" id="step-by-step-guide"></a>

{% hint style="info" %}
This functionality is not by default enabled in your workspace. Contact Aikido to enable.
{% endhint %}

**Step 1:** Go to the [repositories checks](https://app.aikido.dev/repositories/checks) page.

**Step 2:** Click on "[Create Custom Rule](https://app.aikido.dev/repositories/sast/custom/add)" in the SAST section\
​

![Repository checks dashboard with options for creating custom security and compliance rules.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-48c4139fb938cf10216e2f20d712aaff4de42017%2Fadd-custom-sast-iac-rules_bdfc2dff-94ec-4dce-b75d-371457b06f62.png?alt=media)

​**Step 3:** Enter the following details for your rule:

* **Opengrep rule:** Define the rule Aikido will search for. **Tip:** Use the [Opengrep playground](https://github.com/opengrep/opengrep-playground?tab=readme-ov-file#installation)[](https://semgrep.dev/playground)to test your rule's effectiveness before saving.
* **Title:** Name your rule for easy identification.
* **TL;DR:** Provide a concise description of the issue. This will show up in the sidebar.
* **How to fix it:** Let your team know the best way to fix this issue.
* **Language:** Specify the programming language.
* **Aikido Score:** Set the priority level for issue reporting in the main Feed.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FV9HMLR6D4QPuKW4yIBSh%2Fimage.png?alt=media&#x26;token=cee1e1d7-7eca-4c0c-ac07-1d4b41fe72f0" alt=""><figcaption></figcaption></figure>

**Step 4:** Once you're satisfied with the rule's configuration, click "Save" to add it to your Aikido SAST checks. Your custom rule is now active and will be automatically applied in future scans.

### Extra Info <a href="#extra-info" id="extra-info"></a>

* Overall, the language attribute in the Opengrep rule will always prevail. This can be helpful when you are looking to implement a custom rule that needs to be applied to all languages and files at once.
* If you want to create IaC rules, you can do this by setting the language to yaml/terraform/...

## Examples <a href="#examples" id="examples"></a>

* **SAST Rule:** Looking for use of the weak MD5 hashing algorithm in javascript.

  ```
  rules:
    - id: md5-used
      message: It looks like MD5 is used 
      languages:
        - javascript
      paths: 
        include
          - "*.js"
      severity: WARNING
      pattern-either:
        - pattern: $CRYPTO.createHash("md5")
        - pattern: CryptoJS.MD5(...)
  ```

* **IaC Rule:** A custom rule for detecting lambda functions that might be dangerous.

  ```
  rules:
     - id: CUSTOM-RULE-530
       languages:
         - hcl
       severity: WARNING
       message: >
         A Lambda function was found with the "type:monitored" tag, but without a "service" tag.
       patterns:
         - pattern: |-
             resource "aws_lambda_function" $ANYTHING {
               ...
               tags = {..., type = "monitored", ...}
             }
         - pattern-not: |-
             resource "aws_lambda_function" $ANYTHING {
               ...
               tags = {..., service= "...", ...}
             }
  ```

# Access Control Checks

Aikido's checks on Access Controls offers robust security by informing about critical access control practices. This way, you can ensure that only authorized and verified changes are made to your codebase. Some examples of checks are multi-factor authentication, restricting default access rights, and requiring mandatory code reviews.

> All Access Controls checks [can be found here](https://app.aikido.dev/repositories/access_control).

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

* Only available for GitHub & GitLab connected workspaces.

### Access Control Setup for GitHub <a href="#access-control-setup-for-github" id="access-control-setup-for-github"></a>

> For GitLab, no extra authorisation steps need to be taken.

**Step 1.** In the Main Feed, filter on **Access Controls.** Click **Authorise on GitHub** in order to allow Aikido scan for configurations related the access controls.

![Access controls filter active; Aikido requests extra GitHub permissions for analysis.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2f1deb6c6f469d2084befeb5497820727f0152a3%2Fenhancing-security-with-access-control-checks_a13fd024-3a98-4ee5-9e3f-9f4c50f66760.png?alt=media)

**Step 2.** In GitHub, grant permissions to **install** the Aikido GitHub Config Scanner. It is recommended to select **All Repositories**.

![Installing Aikido GitHub Config Scanner with repository and organization read access.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b735d8126097d001d8e70d1870b922357baee7fd%2Fenhancing-security-with-access-control-checks_f8ad227e-3483-4118-9dcd-a32af3acf7ca.png?alt=media)

**Step 3.** After connecting, Aikido will do a scan for [checks mentioned here.](https://app.aikido.dev/repositories/access_control)After a couple of minutes, you will be able to view them in the Aikido feed. The sidebar will give more information about which repos need configuration adjustments.

![Access control security issues listed by severity and estimated fix time.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f154d3154b9be3c3e7b263b2d75062e97284a749%2Fenhancing-security-with-access-control-checks_6b6bed8d-ee13-4d87-b0bb-47e2ac5dfe74.png?alt=media)

# Running a Successful Pilot with Aikido

At Aikido, we know that picking your next application security vendor is a critical business decision so we want to support you in making the best decision possible.

## Getting setup <a href="#getting-setup" id="getting-setup"></a>

We run Pilots with any organization of more than 5+ end users, typically over 1-2 weeks depending on need, and suggest the following key steps:

1. **Intro & Kick Off.** Get to know us, what we do, how we do it, and why we do it this way. If you haven’t already spoken to us, [book in a call here](https://www.aikido.dev/book-a-demo). If you require a signed NDA, we can provide one to you (or review your own to sign).
2. **Set up your account**
   1. To initiate your Pilot, you’ll need to [create your workspace](https://app.aikido.dev/login), using your git provider to sign up. If you’ve already created a workspace, then great!
3. **Pilot period**
   1. Upon completing step 2, your trial will be extended for an additional 1-2 weeks, as per our agreement.
   2. Sometimes you need more time before getting started - no worries. Your account will revert to a “Free” plan until you’re ready to run your Pilot - none of your details will be lost and you won’t be locked out.
4. **Support.** You and your team can access the Aikido team in 1 of 3 ways:
   1. **In-app support** via chat (bottom right of screen) - we usually respond in <3 minutes during European business hours (our tech team often man these!)
   2. **Slack/Teams -** we’re happy to set up a direct channel with you and your team in Slack or MS Teams (speak to your Aikido point of contact)
   3. **Dev Docs -** our comprehensive help center covers all you need to know to get started, set up, and troubleshoot: <https://docs.aikido.dev/>
5. **Evaluation.** Throughout your Pilot, consider the following suggested evaluation criteria commonly used by customers. Feel free to incorporate your own criteria as well.

## Scan your resources <a href="#evaluation-criteria-typical" id="evaluation-criteria-typical"></a>

1. Get your **code scanning** up and running. [More information](https://help.aikido.dev/en/collections/3821227-setting-up-code-scanning)
2. Connect your [**Cloud**](https://help.aikido.dev/docs/cloud-scanning)&#x20;
3. Connect your [**Containers**](https://app.aikido.dev/containers) and/or [**Virtual Machines**](https://help.aikido.dev/docs/virtual-machine-scanning)
4. Secure your App & APIs with our **DAST scanner.** [More information](https://help.aikido.dev/docs/dast-surface-monitoring/dast-surface-monitoring-overview)
5. Integrate your **Task Tracker**. Set-up guides are available [here](https://help.aikido.dev/docs/getting-started/task-management-systems)
6. **Invite your colleagues**. [More information](https://help.aikido.dev/docs/getting-started/automated-user-management)

## Evaluation Criteria (Typical) <a href="#evaluation-criteria-typical" id="evaluation-criteria-typical"></a>

1. **Ease of use & setup**
   1. Was Aikido easy and fun to set up? Did it make sense?
   2. Did our team onboard easily onto Aikido?
   3. Was it clear, concise, and compelling?
2. **Capabilities**
   1. Is Aikido broad and deep enough for our needs?
   2. Does it meet our requirements?
   3. Did Aikido's noise-cancelling algorithm improve focus and prioritisation compared to others you've seen?
   4. Do the integrations support our workflows and real estate (Slack, Jira, etc.)?
   5. Are the reporting and compliance features sufficient?
3. **Comparisons**
   1. How does Aikido compare to our existing stack / provider? And to others we’ve seen?
   2. How does Aikido’s pricing and terms compare? Are they fair and reasonable?
   3. How does Aikido’s security issues reporting compare to others - does it “noise cancel” effectively versus others?
4. **Support**
   1. Is there sufficient and good quality support for me and my team?
   2. Are the response times and quality of responses reasonable and good?
   3. Does my team feel comfortable and trust the work of Aikido’s support teams?
5. **Costs & ROI**
   1. Is it a reasonably priced and good value-for-money product?
   2. Can I demonstrate ROI to my stakeholders and teams? Eg through increased security posture, reduced dev time on security issues, and better training?
   3. How does the ROI of Aikido compare to our existing stack / other vendors?

# Aikido Never Stores Your Code

{% hint style="success" %}
In short: Aikido does not store your code after analysis has taken place. Some of the analysis jobs such as SAST or Secrets Detection require a git clone operation. Below we talk about the technical measures we take to ensure your code is protected:
{% endhint %}

* We perform different actions such as git clones in a fresh docker container for each repository. After analysis, the data is wiped and the docker container is terminated.
* For GitHub, no refresh or access tokens are ever stored in our database. We use the new GitHub Apps which do not require this. Even a database breach of Aikido itself would not result in your GitHub code being downloadable.
* By default, our integrations require a very minimal read-only scope. Only if you enable special features such as Autofix Pull Requests, Aikido will request write accesses.
* If you want to keep your code completely on-premise, without ever leaving your environment, you can use our [Local Scanner](https://help.aikido.dev/category/aikido-local-scan-setup/sg4xF4OsJciW). The results will seamlessly populate on the Aikido platform.
* Aikido has SOC2 Type 2 & ISO27001:2022 certification. A report is available [upon request](http://trustcenter.aikido.dev/). That means we adhere to several organizational and technical policies by default.
* Aikido runs AWS, with data residency in the EU and US region.That means all processing and storage will stay in that location.

The process we use to ensure code security:

![Secure repository scanning workflow: select, clone, scan, encrypt findings, destroy containers.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0acaf4018cdcba7833afcf08271e7f8c9ceeda00%2Faikido-never-stores-your-code_411acc55-32e2-4db5-88e5-c26b0896eb7a.png?alt=media)

**Disclaimer.**

Aikido has some features where certain parts of your code are stored. This is in the case for the following functionalities:

* AutoFix: Aikido stores the diffs (original and AutoFixed code) - only files that are part of the AutoFix
* Aikido stores the calltree for each AutoTriaged SAST finding for up to 2 weeks

All code that is stored is ran through Gitleaks. If there are any obvious secrets in the code, we make sure to definitely not store these.

# Limit Aikido Access to Specific IPs

IP allowlisting is a critical security measure that allows you to restrict access to Aikido so only users from specific, trusted IP addresses (e.g., your company’s network) can log in.

> This feature is currently only available upon request. Contact us via chat.

# Custom Rules

You can define your own rules in Aikido across code security, cloud security, and code quality, so checks align with your your environment and standards.

### **Where you can add custom rules**

* [**Custom SAST & IaC Rules**](https://help.aikido.dev/general-information/add-custom-sast-iac-rules)

  Define rules to detect application or infrastructure patterns that are specific to your stack, such as enforcing internal security APIs or common misconfigurations specific to your organization.
* [**Custom CSPM Rules**](https://help.aikido.dev/cloud-scanning/custom-cspm-rules)

  Add your own cloud misconfiguration checks on top of Aikido’s managed rules. Custom CSPM rules can be mapped to compliance benchmarks via tags, and they show up in compliance reports like any other cloud rule (for example, mapping a backup rule to ISO 27001 sections).
* [**Custom Code Quality Rules**](https://help.aikido.dev/code-quality/add-custom-code-rules)

  Describe code patterns or conventions you want to enforce in natural language. Aikido turns these into AI-powered checks that run on pull requests and help you enforce team-specific coding guidelines.

### Typical use cases

* Encode internal security guidelines, such required wrappers or safe helpers
* Flag cloud configurations that are risky in your particular architecture and tying them to your compliance framework
* Enforce local coding standards and architectural rules

# Code Scanning Overview

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="connect-your-source-code"><strong>Connect Your Source Code</strong></a></td><td>Learn how to connect your git and scan your source code for dependencies, SAST, IaC, secrets, malware, and more.</td><td><a href="connect-your-source-code">connect-your-source-code</a></td></tr><tr><td><a href="local-code-scanning"><strong>Local Code Scanning</strong></a></td><td>Set up Aikido’s Local Scanner to run scans as part of your CI/CD pipelines and development processes.</td><td><a href="local-code-scanning">local-code-scanning</a></td></tr><tr><td><a href="scanning-practices"><strong>Scanning Best Practices</strong></a></td><td>Configure and optimize scanning for dependencies, secrets, and malware </td><td><a href="scanning-practices">scanning-practices</a></td></tr><tr><td><a href="miscellaneous"><strong>Repository Configuration</strong></a></td><td>Set up repositories, branches, and scan settings</td><td><a href="miscellaneous">miscellaneous</a></td></tr></tbody></table>

# Connect Your Source Code

# Connect GitHub Organization

**Table of contents:**

* [1. Logging in using GitHub](#1-logging-in-using-github)
* [2. Authorizing access to an organization](#2-authorizing-access-to-an-organization)
* [3. Checking results](#3-checking-results)

## Connect GitHub Account to Aikido

Aikido requests read-only access to your GitHub organization to analyze your repositories. We use the new GitHub App system, so we don't have to store any tokens in our database at all. After analysis, your code is always wiped from the system.

#### 1. Logging in using GitHub <a href="#id-1-logging-in-using-github" id="id-1-logging-in-using-github"></a>

To get started, navigate to <https://app.aikido.dev/> and log in with GitHub. This will look like the screenshot below. Here, Aikido only requests access to your identity on GitHub and the associated email address.

![Aikido Security requests GitHub authorization to access user identity and email addresses.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-def027deaa2ea84ba3f765c6e45e72e6e8d4338d%2Fconnect-github-account-to-aikido_86f8bf78-e871-4801-b0ec-5da21d111456.png?alt=media)

#### 2. Authorizing access to an organization <a href="#id-2-authorizing-access-to-an-organization" id="id-2-authorizing-access-to-an-organization"></a>

On the next screen, you can choose to connect a real organization or a sample workspace. If you choose a real organization you will be redirected back to GitHub. Once there, pick the organization you would like to authorize. You can optionally grant access to 1 or 2 repositories instead of all repositories as seen below:

![Authorize Aikido Security to access all repositories and read email addresses on GitHub.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-70b99cde218b1a974e192c31ddcdc77a30025d27%2Fconnect-github-account-to-aikido_c8faa94c-a2c8-4173-8dc3-d938951f8aae.png?alt=media)

#### 3. Checking results <a href="#id-3-checking-results" id="id-3-checking-results"></a>

After granting access and validating the repositories you want to scan, Aikido will automatically start scanning. After about 1 minute, you should see the first results come in!

# Connect Azure DevOps Projects

**Table of contents:**

* [Select Microsoft / Office 365 or Google to authenticate](#select-microsoft--office-365-or-google-to-authenticate)
* [Insert your organization's name](#insert-your-organizations-name)
* [Create a Personal Access Token](#create-a-personal-access-token)
* [Select the project and repos you'd like to secure](#select-the-project-and-repos-youd-like-to-secure)

## Connect Azure DevOps Projects to Aikido

Aikido allows you to connect your Azure DevOps projects to secure your code. To connect your Azure DevOps projects to Aikido, you will need to follow the steps below.

Note that each Azure Project with one or more repos will map to one Aikido workspace.

### Select Microsoft / Office 365 or Google to authenticate <a href="#select-microsoft--office-365-or-google-to-authenticate" id="select-microsoft--office-365-or-google-to-authenticate"></a>

**Step 1.** To connect your Azure DevOps project, you first need to authenticate via Microsoft / Office 365 or Google to create a user in Aikido. On the [signup screen](https://app.aikido.dev/login), click on 'Microsoft / Google' to continue.

> Depending on your organization's Microsoft Entra settings, you may need IT admin approval to authorize the Aikido application. [For more information about the approval process, check Azure docs.](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal)

**Step 2.** Once you are authenticated via Google/Microsoft, you can go ahead and select 'Connect Azure' on the page like below.

![Repository integration options: Connect with GitHub, Azure DevOps, GitLab, or Bitbucket.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0538cafa47734c6ab1098288262536d38e0f83be%2Fconnect-azure-devops-projects-to-aikido_8fece096-ffc3-4775-bd8d-52b44b022ee8.png?alt=media)

**Step 3.** Enter the details to connect the Azure Devops project of your choosing. We'll explain how to obtain the required information right below.

![Aikido onboarding: Enter Azure DevOps details to authenticate and connect your projects.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b90f85e72e89d499f3d58e420dd508b56c9156f7%2Fconnect-azure-devops-projects-to-aikido_3b1a2af6-64ef-4b33-b436-5e61e388e8dc.png?alt=media)

### Insert your organization's name <a href="#insert-your-organizations-name" id="insert-your-organizations-name"></a>

Enter the name of the Azure DevOps organization you'd like to connect. You can find this name by going to [https://dev.azure.com](https://dev.azure.com/) and copying it from the left-side navigation.

### Create a Personal Access Token <a href="#create-a-personal-access-token" id="create-a-personal-access-token"></a>

Next up, you need to create a Personal Access Token to give us access to the resources you want.

* Log in to your Azure DevOps account
* In the upper-right corner, click the user settings icon next to your avatar. It looks like this:

  ![User profile icon with a settings gear for account management options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1a7d3d50a15bc9f2a63c718d2fdb779dc55b3eca%2Fconnect-azure-devops-projects-to-aikido_8ac6922c-38e0-481b-a9e7-0be293fa315a.png?alt=media)
* Select **Personal Access Token** in the dropdown.
* Click on the **+New Token** button in the top left corner
* Enter a name for the token, eg: 'Aikido Security Access Token'
* Make sure to select the same organization as the one you entered in the previous step
* Make sure to select an expiration date in the future, the max should be 1 year.
* Next, we need the following scopes to be selected (click 'show all scopes'):
  * **Code: Read**
  * **Member Entitlement Management: Read**
  * **Project and Team: Read**
  * **User Profile: Read**
* Click the **Create** button at the bottom.

![Editing Azure DevOps personal access token with custom-defined code read permissions.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8f592ae4b0c29f78271e25fdd8fb18470239fb07%2Fconnect-azure-devops-projects-to-aikido_06457a8f-e8dd-47b3-a629-8cb8cff94338.png?alt=media)

* Copy the token being shown on the following screen and enter it in the input field .

**Important**: You will no longer be able to view the value of the token once you hit continue. Make sure you copied it first.

Aikido will now check the connection to your Azure DevOps organization. If the connection was not successful, make sure to double-check the organization name and personal access token you provided.

### Select the project and repos you'd like to secure <a href="#select-the-project-and-repos-youd-like-to-secure" id="select-the-project-and-repos-youd-like-to-secure"></a>

On the next screen, you can select which project you'd like to start with. You'll always be able to connect more of your projects to Aikido.

In the final step you can select all the repos you would like us to monitor.

#### Specific notes on TFVC Repos

Aikido supports the integration of both Git and Team Foundation Version Control (TFVC) repositories.&#x20;

* For TFVC repositories, Aikido **does not** perform secret scanning.
* By default, Aikido tries to scan 'All Branches' for TFVC repos. This might result in slow scanning speed. **It is recommended to select the actual branch to scan.** This can be changed by clicking the branch label on the repo detail page.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FP3dD3aHfu20Em6CrMhJi%2Fimage.png?alt=media&#x26;token=caf72359-e3c2-4e6e-9e1f-17314252f773" alt=""><figcaption></figcaption></figure>

# Connect Bitbucket Account

**Table of contents:**

* [1. Logging in using Bitbucket](#1-logging-in-using-bitbucket)
* [2. Authorizing access to an organization](#2-authorizing-access-to-an-organization)
* [3. Select your repos](#3-select-your-repos)
* [4. Checking results](#4-checking-results)

## Connect Bitbucket Account to Aikido

Aikido requests read-only access to your Bitbucket organization to analyze your repositories. After analysis, your code is always wiped from the system.

### 1. Logging in using Bitbucket <a href="#id-1-logging-in-using-bitbucket" id="id-1-logging-in-using-bitbucket"></a>

To get started, navigate to <https://app.aikido.dev/> and log in with Bitbucket. This will look like the screenshot below. Here, Aikido only requests access to your identity on Bitbucket and the associated email address.

![Access request screen for account information by Aikido User Authentication, with grant or cancel options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cfe1712ebee2f37ac0b729bdee750fc636d826d3%2Fconnect-bitbucket-account-to-aikido_10401885-4c52-4133-894a-48f9d2736781.png?alt=media)

### 2. Authorizing access to an organization <a href="#id-2-authorizing-access-to-an-organization" id="id-2-authorizing-access-to-an-organization"></a>

On the next screen, you can choose to connect a real organization or a sample workspace. If you choose a real organization you will be redirected back to Bitbucket. Once there, pick the organization you would like to authorize.

![Aikido requests account and repository access; user must approve or deny.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4564ac5f4c41b0bcc1c126c072afcbf1670be22c%2Fconnect-bitbucket-account-to-aikido_76533a25-f878-4c97-a437-e35e38c780ea.png?alt=media)

### 3. Select your repos <a href="#id-3-select-your-repos" id="id-3-select-your-repos"></a>

You can optionally grant access to 1 or 2 repositories instead of all repositories as seen below:

![Select repositories to monitor for security with Aikido’s free or upgraded plan.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9a584a4da4b5097c54d0e77e10ad7fefa40fe257%2Fconnect-bitbucket-account-to-aikido_89ce9a97-d113-4d2d-bb6c-8526fb67646c.png?alt=media)

### 4. Checking results <a href="#id-4-checking-results" id="id-4-checking-results"></a>

After granting access and validating the repositories you want to scan, Aikido will automatically start scanning. After about 1 minute, you should see the first results come in!

# Code Scanning with a Workspace Access Token

{% hint style="warning" %}
Bitbucket only supports the creation of Workspace Access Tokens for their premium plan.
{% endhint %}

### Introduction <a href="#introduction" id="introduction"></a>

You can easily configure Bitbucket Code Scanning via the Aikido interface via the account settings page, or by navigating directly to [this link](https://app.aikido.dev/onboarding/bitbucket/update-workspace-access-token).&#x20;

### Creating a Workspace Access Token <a href="#creating-a-personal-access-token" id="creating-a-personal-access-token"></a>

{% stepper %}
{% step %}

### Navigate to the workspace settings

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FO0UPQ4AE27X0DjlzyEGl%2F11.jpg?alt=media&#x26;token=6874f843-b8ae-4f0c-a74b-a08b8e92ebe9" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Create access token

Click on the "Create access token" button to start creating a workspace access token.
{% endstep %}

{% step %}

### Select the required scopes

Choose a descriptive name for the token like "**Aikido Security Code Scanning**", and select the following scopes: **Account:Read** & **Repsitories:Read**
{% endstep %}

{% step %}

### Copy the token

After clicking "**Create**", you can copy the token and enter it in the input field on [this page](https://app.aikido.dev/onboarding/bitbucket/update-workspace-access-token)
{% endstep %}
{% endstepper %}

# Connect GitLab Account

**Table of contents:**

* [Step 1. Logging in using GitLab](#step-1-logging-in-using-gitlab)
* [Step 2. Creating a workspace, join an existing workspace or create a demo](#step-2-creating-a-workspace-join-an-existing-workspace-or-create-a-demo)
* [Step 3. Connect a GitLab group to Aikido](#step-3-connect-a-gitlab-group-to-aikido)
* [Step 4. Selecting groups & selecting repos](#step-4-selecting-groups--selecting-repos)
* [5. Checking results](#5-checking-results)

## Connect GitLab account to Aikido

Aikido requests read-only access to your GitLab group to analyze your projects. After analysis, your code is always wiped from the system.

***Important before you start***

* If your GitLab is behind a firewall, we have a [list of Static IPs](https://help.aikido.dev/en/articles/8731261-allowing-ip-addresses-for-code-scanning) you can allowlist.
* The person who sets up the account needs to have access rights both to the GitLab instance **and** GitLab group\*.

{% hint style="warning" %}
\*An Aikido workspace always maps to a single GitLab group. We recommend to connect Aikido to a top-level GitLab group (i.e. root group) that contains all subgroups. If no top-level group exists, you can create a separate workspace for each GitLab group. This option is available after creating the first workspace via the top-left dropdown “Add another workspace”.
{% endhint %}

{% hint style="success" %}
**Repositories not linked to a group**, but linked to just your user can currently not be scanned. If you do have personal repositories which you'd like to have scanned, we recommend to create a personal group, or transfer them to a group you own.
{% endhint %}

#### Step 1. Logging in using GitLab <a href="#step-1-logging-in-using-gitlab" id="step-1-logging-in-using-gitlab"></a>

To get started, navigate to <https://app.aikido.dev> and log in with GitLab. This will look like the screenshot below. Here, Aikido only requests access to your identity on GitLab and the associated email address.

![Aikido Security requests access to read personal information from a GitLab account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-55ac731f87c11d27462aee1d900212bfddef8b65%2Fconnect-gitlab-account-to-aikido_dd58925f-aa33-4b89-9e02-bd75cc1009ad.png?alt=media)

#### Step 2. Creating a workspace, join an existing workspace or create a demo <a href="#step-2-creating-a-workspace-join-an-existing-workspace-or-create-a-demo" id="step-2-creating-a-workspace-join-an-existing-workspace-or-create-a-demo"></a>

After authorizing Aikido to read your personal GitLab information you get the following screen.

![gitlab\_signup](https://ucarecdn.com/143adfc1-c0c6-4c71-8a3d-1bed03e7ca6a/)

On this page you can do one of 3 things:

* **Create a new workspace:** select this option if you want to connect a GitLab group to Aikido and start scanning your code repositories and clouds.
* **Join your team:** select this option if someone in your organization already connected a GitLab group to Aikido, and you'd like to get access to it
* **Use sample repo:** want to have a sneak peak of what Aikido looks like and what it can do? Create a demo account to get a taste of Aikido. You can always connect your GitLab group at a later moment

#### Step 3. Connect a GitLab group to Aikido <a href="#step-3-connect-a-gitlab-group-to-aikido" id="step-3-connect-a-gitlab-group-to-aikido"></a>

If you would like to create a new workspace, Aikido will need **read-only access** to your projects and groups. We will therefore redirect you back to GitLab so you can authorize Aikido.

**Note.** This does *not* give access to the actual repos yet. Selecting which ones you want to have scanned is in the step after this one.

![Aikido Security requests GitLab read access and user information authorization.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-99cd8b807b1832f7b8eff5bf78e3e751cd24869b%2Fconnect-gitlab-account-to-aikido_b461947a-bf2e-4a4e-936a-84efb59a1f48.png?alt=media)

#### Step 4. Selecting groups & selecting repos <a href="#step-4-selecting-groups--selecting-repos" id="step-4-selecting-groups--selecting-repos"></a>

After authorizing Aikido to read your groups and projects, you can select which group you'd like to connect to Aikido.

**Note:** Aikido will include any subgroups of the GitLab group you selected in the workspace

![Select a group to connect to Aikido as a workspace.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f10225612eaf70ef96669b6069de25acf121f121%2Fconnect-gitlab-account-to-aikido_f0dad506-48d9-4216-a102-80051d6019b3.png?alt=media)

​After selecting the groups of choice, you can choose which repositories you want to give access to.

![Select repositories for monitoring security with Aikido's cloud and repo management tool.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6caceaad1872fc4aac3d6652b2d7c61245144bf5%2Fconnect-gitlab-account-to-aikido_b7b4ee31-ffac-48a6-8c1e-282fe833ca81.png?alt=media)

#### 5. Checking results <a href="#id-5-checking-results" id="id-5-checking-results"></a>

After granting access and validating the repositories you want to scan, Aikido will automatically start scanning. After about 1 minute, you should see the first results come in!

# Code Scanning with a Service Account Access Token

### ⚠️ Disclaimer

This guide is only available for **Gitlab Premium &** **Gitlab Ultimate** users. Check out our the setup with [personal access tokens](https://help.aikido.dev/docs/code-scanning/connect-your-source-code/connect-gitlab-account-to-aikido/code-scanning-with-a-personal-access-token) for **Gitlab Free** users

### Introduction

You can use service account tokens which Aikido uses to perform the code scanning. You can update this token on the [update workspace access token](https://app.aikido.dev/onboarding/gitlab/update-workspace-access-token) page.

### Creating a Service Account and Access Token <a href="#creating-a-personal-access-token" id="creating-a-personal-access-token"></a>

1. Navigate to the "Service Accounts" settings page. Group > Settings > Service accounts

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FexZlH0U1ZIwXGlPdeewY%2Fimage.png?alt=media&#x26;token=185d5cc8-de72-486c-b753-e0d6adfadde3" alt="Gitlab group sidebar: highlighting &#x22;Service accounts&#x22; under the &#x22;Settings&#x22; option"><figcaption></figcaption></figure>

2. Click on "**Add service account**"

3. Give a **Name** and **Username** to the Service Account and click **Create**

4. Click the options of the newly created service account and select **Manage access tokens**

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FYKpNvN0JgtysQMCxsPbo%2Fimage.png?alt=media&#x26;token=0affb51b-44f0-4aa7-9f37-232f692a20a2" alt="Gitlab Service Accounts overview"><figcaption></figcaption></figure>

5. Click on "**Add new token**"

6. Enter a name for the token, remove the expiration date or set it to the max value and select the **api** scope

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fk7E9OtnoLgQOFdze1iMq%2FScherm%C2%ADafbeelding%202025-12-11%20om%2012.11.34.png?alt=media&#x26;token=8833dde6-ed95-4225-aa43-4eddea5f3a40" alt=""><figcaption></figcaption></figure>

7. Click on "**Create token**"

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FUrQEqurtCGh5y4ZdSQFB%2FScherm%C2%ADafbeelding%202025-12-11%20om%2012.15.09.png?alt=media&#x26;token=69832055-017e-4d4e-8989-00e3061e206a" alt=""><figcaption></figcaption></figure>

8. Copy the token and keep it for the "[update workspace access token](https://app.aikido.dev/onboarding/gitlab/update-workspace-access-token)" page

9. Go to the members page: **Group** > **Manage** > **Members**

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FJT588D1d6YCZREQyboZ3%2Fimage.png?alt=media&#x26;token=f455025a-ba12-46e1-85e0-b2781a2f9ec8" alt="Gitlab Group sidebar; showing members under the manage option"><figcaption></figcaption></figure>

10. Click "**Invite Members**"

11. Search for your new Service account created earlier and set role to "**Maintainer**"

    <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F8mKYveigtRhAs6s9H6cL%2Fimage.png?alt=media&#x26;token=835e40f5-43c2-4782-8edd-c3bdf2ced2bd" alt=""><figcaption></figcaption></figure>

# Code Scanning With a Personal Access Token

### ⚠️ Disclaimer

For **Gitlab Premium & Gitlab Ultimate** users we recommend using [Gitlab Service Accounts](https://help.aikido.dev/docs/pr-and-release-gating/gitlab-mr-gating/gitlab-server-ci-mr-gating-via-aikido-dashboard-with-a-service-account-token). In case you would use this approach, make sure to setup an integration user that is called AikidoSec.

### Introduction

You can use personal access tokens which Aikido uses to perform the code scanning. You can update this token on [this page](https://app.aikido.dev/onboarding/gitlab/update-workspace-access-token).

### Creating a Personal Access Token <a href="#creating-a-personal-access-token" id="creating-a-personal-access-token"></a>

Gitlab cloud supports several different personal access tokens, which all work the same way. We usually recommend to create a group PAT, but for Gitlab cloud this is only possible for premium customers.

1. Navigate to the "Personal Access Token" settings page
   1. For a group access token: Go to you group page > Settings > Access Tokens
   2. For a personal access token: Go to your profile page > User settings > Access Tokens

      ![Group Access Tokens page with no active tokens and an option to add new token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4c2148c4eecfd757dcd7b52f5f1d69ccfc08a14b%2Fgitlab-server-ci-mr-gating-via-aikido-dashboard-with-a-personal-access-token-pat_9e58d61d-ee8e-4c49-8f0d-e3e081aff7d0.png?alt=media)
2. Click on "**Add new token**"
3. Enter a name for the token, remove the expiration date and select the **read\_api, read\_user and read\_repository** scope<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FdjJx3d6Rn5VxNydgX3jf%2FScherm%C2%ADafbeelding%202025-12-11%20om%2012.11.34.png?alt=media&#x26;token=a73926ff-63d5-4390-a79d-882659b5ac34" alt=""><figcaption></figcaption></figure>
4. Click on "**Create token**"
5. Copy the token and enter it into the input field on the update access token page of Aikido<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FUrQEqurtCGh5y4ZdSQFB%2FScherm%C2%ADafbeelding%202025-12-11%20om%2012.15.09.png?alt=media&#x26;token=69832055-017e-4d4e-8989-00e3061e206a" alt=""><figcaption></figcaption></figure>

# Connect GitLab Self-Managed Server

Aikido lets you connect a self-managed GitLab instance to scan and secure your code. Follow the steps below to connect your GitLab server to Aikido.

### Before you start

* If your GitLab is behind a firewall, [allowlist the Aikido IP addresses](https://help.aikido.dev/docs/code-scanning/miscellaneous/allowing-ip-addresses-for-code-container-scanning) so Aikido can reach it.
* The person setting this up needs access to both the GitLab instance **and** the GitLab group you want to connect.

{% hint style="warning" %}
An Aikido workspace always maps to a single GitLab group.

We recommend connecting Aikido to a top-level (root) group that contains all subgroups. If you don’t have a root group, create one workspace per GitLab group. You can do this after creating your first workspace via the top-left dropdown: “Add another workspace”.
{% endhint %}

## Configuration

{% stepper %}
{% step %}

### Create an Aikido account

To connect your GitLab server, first sign up or log in to Aikido using Google or Microsoft. On the [signup screen](https://app.aikido.dev/login), click **Google / Microsoft**.
{% endstep %}

{% step %}

### Start the GitLab setup

Once you’re authenticated, create a new workspace by clicking **Self-Managed** in the GitLab section.

![Select a source control provider to connect: GitHub, Azure DevOps, GitLab, or Bitbucket.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4be1bf4a3d0bcc9641482ed36641a7c4d97ed5d9%2Fconnect-gitlab-self-managed-server-to-aikido_38929d5c-805a-4ee2-9881-67b5a316190d.png?alt=media)
{% endstep %}

{% step %}

### Provide GitLab details

To create the workspace, provide a few details about your self-managed GitLab instance so Aikido can connect to it.

{% hint style="info" %}
If your GitLab runs behind a firewall, [allowlist the Aikido IP addresses](https://help.aikido.dev/docs/code-scanning/miscellaneous/allowing-ip-addresses-for-code-container-scanning) so we can access it. If that’s not possible, use the [Broker setup guide](https://help.aikido.dev/docs/code-scanning/connect-your-source-code/connect-gitlab-self-managed-server-to-aikido/connect-gitlab-self-managed-server-broker-set-up).
{% endhint %}

Enter the URL to your GitLab server in the first input field.

![Aikido onboarding: Enter GitLab Self-Managed URL and access token to authenticate.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FY14PPZwrIReXD70FUMfc%2FScreenshot%202025-12-22%20at%2010.16.41.png?alt=media\&token=2a30dbe4-ddce-4ccd-bda7-aaa260b165bb)
{% endstep %}

{% step %}

### Create a GitLab personal access token (PAT)

Next, create a personal access token (PAT). We recommend using a dedicated service account.

* Log in to your GitLab server
* Go to the admin area (`/admin`)
* Go to **Settings** → **Service accounts**
* Click **Add service account**, enter a name, then save

{% hint style="warning" %}
Add the service account to the GitLab group you want to connect, like any other user. See GitLab’s docs on [group members](https://docs.gitlab.com/ee/user/group/members/).
{% endhint %}

Now that the service account is created, you can create a PAT for it by clicking the three dots and select "**Manage access tokens**"

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FFT7nRO99qhMkOcxnWAP5%2FScherm%C2%ADafbeelding%202025-08-11%20om%2014.57.42.png?alt=media&#x26;token=f9ba8fbb-e70c-44ec-8b79-dd6cb09214aa" alt=""><figcaption></figcaption></figure>

* Click on "**Add new token**"
* Enter a name for the token, for example: `Aikido Security Access Token`
* Set an expiration date that matches your internal policy. Rotate the token before it expires.
* We need the following scopes to be selected:
  * **read\_user**
  * **read\_api**
  * **read\_repository**
* Click the **Create token** button at the bottom of the form.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FnVQ5yJX7Y287k8x4KoCQ%2FScherm%C2%ADafbeelding%202025-08-11%20om%2015.00.51.png?alt=media&#x26;token=d49e8025-7601-46af-93bb-bd48f797f421" alt=""><figcaption></figcaption></figure>

* Copy the token being shown on the screen and enter it in the input field.

**Important:** You won’t be able to see the token again after you leave this screen. Copy it before you continue.

Aikido will now check the connection to your GitLab server. If it fails, double-check the server URL and the token.
{% endstep %}

{% step %}

### Complete the installation

After you click **Next, Connect Group**, select the group you want to start with. You can always connect more groups later.

In the final step, select the repositories you want Aikido to monitor.
{% endstep %}
{% endstepper %}

# Connect GitLab Self-Managed Server (Broker Set-Up)

Aikido lets you connect a self-managed GitLab instance to scan and secure your code. Follow the steps below to connect your GitLab server to Aikido.

### Before you start

* The person setting this up needs access to both the GitLab instance **and** the GitLab group you want to connect.

{% hint style="warning" %}
An Aikido workspace always maps to a single GitLab group.

We recommend connecting Aikido to a top-level (root) group that contains all subgroups. If you don’t have a root group, create one workspace per GitLab group. You can do this after creating your first workspace via the top-left dropdown: “Add another workspace”.
{% endhint %}

## Configuration

{% stepper %}
{% step %}

### Create an Aikido account

To connect your GitLab server, first sign up or log in to Aikido using Google or Microsoft. On the [signup screen](https://app.aikido.dev/login), click **Google / Microsoft**.
{% endstep %}

{% step %}

### Start the GitLab setup

Once you’re authenticated, create a new workspace by clicking **Self-Managed** in the GitLab section.

![Select a source control provider to connect: GitHub, Azure DevOps, GitLab, or Bitbucket.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4be1bf4a3d0bcc9641482ed36641a7c4d97ed5d9%2Fconnect-gitlab-self-managed-server-to-aikido_38929d5c-805a-4ee2-9881-67b5a316190d.png?alt=media)
{% endstep %}

{% step %}

### Enable Broker access

Enable the **Aikido broker** by clicking the toggle in the "Advanced Connection Options" section.

Click **Create Group** to continue.

![Aikido onboarding: Enter GitLab Self-Managed URL and access token to authenticate.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FDMVpZt1bwxhnZElIoGu5%2FScherm%C2%ADafbeelding%202026-01-27%20om%2015.15.28.png?alt=media\&token=c26da44c-6d3f-4237-bdf1-bb2b8de833fd)
{% endstep %}

{% step %}

### Configure the Broker

Configure the Broker using the guide below. After you deploy it, return here to finish the GitLab setup.

{% content-ref url="../../../miscellaneous-info/aikido-broker-for-internal-applications" %}
[aikido-broker-for-internal-applications](https://help.aikido.dev/docs/miscellaneous-info/aikido-broker-for-internal-applications)
{% endcontent-ref %}

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F4TexnG7f9FVyi8mkOG9Q%2FScreenshot%202025-12-22%20at%2010.48.21.png?alt=media&#x26;token=e69fac71-7a6e-4efd-8ea6-25ca01b1692d" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Complete GitLab server setup

After you create the broker and deploy it in your environment, you can complete the GitLab setup.

First, copy the **Broker URL**. It looks similar to this:

```
https://55673-355dsfwea68cb.aikidobroker.com
```

Then click **Complete GitLab Server Setup**.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgrhts0YhFD1PjvtW3NvL%2FBroker_Clients_-_Gitlab_Server_EVAfKobo3u_-_Aikido_Security_%E2%80%94_Aikido.png?alt=media&#x26;token=c4a247df-8483-4ec4-80d9-2bfb494d40f8" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Enter the Broker URL

Paste the Broker resource URL from the previous step in the input field for the "server URL".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fo4hRI8ViDdYpreixIVos%2FScherm%C2%ADafbeelding%202026-01-27%20om%2015.16.49.png?alt=media&#x26;token=8cf2b417-b61c-43e5-b2e1-5334a93c0578" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Create a GitLab personal access token (PAT)

Next, create a personal access token (PAT). We recommend using a dedicated service account

* Log in to your GitLab server
* Go to the admin area (`/admin`)
* Go to **Settings** → **Service accounts**
* Click **Add service account**, enter a name, then save

{% hint style="warning" %}
Add the service account to the GitLab group you want to connect, like any other user. See GitLab’s docs on [group members](https://docs.gitlab.com/ee/user/group/members/).
{% endhint %}

Now that the service account is created, you can create a PAT for it by clicking the three dots and select "**Manage access tokens**"

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FFT7nRO99qhMkOcxnWAP5%2FScherm%C2%ADafbeelding%202025-08-11%20om%2014.57.42.png?alt=media&#x26;token=f9ba8fbb-e70c-44ec-8b79-dd6cb09214aa" alt=""><figcaption></figcaption></figure>

* Click on "**Add new token**"
* Enter a name for the token, for example: `Aikido Security Access Token`
* Set an expiration date that matches your internal policy. Rotate the token before it expires.
* We need the following scopes to be selected:
  * **read\_user**
  * **read\_api**
  * **read\_repository**
* Click the **Create token** button at the bottom of the form.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FnVQ5yJX7Y287k8x4KoCQ%2FScherm%C2%ADafbeelding%202025-08-11%20om%2015.00.51.png?alt=media&#x26;token=d49e8025-7601-46af-93bb-bd48f797f421" alt=""><figcaption></figcaption></figure>

* Copy the token being shown on the screen and enter it in the input field.

**Important:** You won’t be able to see the token again after you leave this screen. Copy it before you continue.

Aikido will now check the connection to your GitLab server. If it fails, double-check the server URL and the token.
{% endstep %}

{% step %}

### Complete the installation

After you click **Next, Connect Group**, select the group you want to start with. You can always connect more groups later.

In the final step, select the repositories you want Aikido to monitor.
{% endstep %}
{% endstepper %}

# How to Scan a Personal GitLab Project

**Table of contents:**

* [Step 1. Create a new group in GitLab](#step-1-create-a-new-group-in-gitlab)
* [Step 2. Transfer your personal projects to the newly created group](#step-2-transfer-your-personal-projects-to-the-newly-created-group)
* [Step 3. Connect the group to Aikido](#step-3-connect-the-group-to-aikido)

## How to scan a personal GitLab project

At this moment, Aikido only allows to scan projects which are linked to a group. Projects linked to your GitLab user are currently not supported.\
​\
If you'd like to enable code scanning on your personal GitLab projects, we recommend you create a personal group and transfer the projects there. To accomplish this, we recommend you follow the steps below.

#### Step 1. Create a new group in GitLab <a href="#step-1-create-a-new-group-in-gitlab" id="step-1-create-a-new-group-in-gitlab"></a>

Login to your GitLab account, navigate to "Groups" in the left-hand side navigation and click on "New group". Follow the steps to create a group.

![GitLab Groups dashboard with options to explore, create, and search for groups.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f4c4a2bdcdce6e2d188891de29bc58e0934b91ca%2Fhow-to-scan-a-personal-gitlab-project_6f7e4107-4a83-44b6-ae5c-f858a3b4ac78.png?alt=media)

#### Step 2. Transfer your personal projects to the newly created group <a href="#step-2-transfer-your-personal-projects-to-the-newly-created-group" id="step-2-transfer-your-personal-projects-to-the-newly-created-group"></a>

Now, you can transfer your personal projects to the newly created group. To do this, navigate to the project's detail page and go to it's "General settings", which you can see in the left-hand side navigation. At the bottom you can expand the "Advanced" settings section.

![GitLab project general settings page showing configuration options for visibility, badges, and advanced features.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-14b6a6ad756dfffbc60ca773e3ab093ab9ca330a%2Fhow-to-scan-a-personal-gitlab-project_12819150-cf77-456d-95fc-21fcad9de857.png?alt=media)

At the bottom of this section, you can transfer this project to a different namespace.\
​

![GitLab project settings for changing repository path and transferring project namespace.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-bef13254ff0392a1d9039e4ccd975bbcef6d2927%2Fhow-to-scan-a-personal-gitlab-project_968e99ba-c1be-4ccd-ac56-e243c658c35f.png?alt=media)

#### Step 3. Connect the group to Aikido <a href="#step-3-connect-the-group-to-aikido" id="step-3-connect-the-group-to-aikido"></a>

Now that you transferred your new project to the new namespace aka "group", you can connect Aikido to that group and allow read-only acces to start scanning for vulnerabilities.\
​\
In Aikido, select the Group dropdown picker in the left-hand side navigation, and click on "Add another workspace".

![Workspace menu showing "aikido-dev" on Pro plan with team and settings options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-36973a8dc3ab1cda5a314aebebf1c8f7b68a7a83%2Fhow-to-scan-a-personal-gitlab-project_75339182-b6b1-4078-a9d1-e7d549c7bdc2.png?alt=media)

You will now go through the flow of connecting your newly created GitLab group to Aikido to grant read-only access to your personal projects.

# Connect GitHub Enterprise (Cloud & Server)

Aikido integrates with [Github Enterprise Cloud](https://docs.github.com/en/get-started/onboarding/getting-started-with-github-enterprise-cloud) and [GitHub Enterprise Server](https://docs.github.com/en/enterprise-server@3.19/admin/overview/about-github-enterprise-server) through a secure, app-based connection. This allows Aikido to access the repositories you choose while keeping full control.

### Installation

Aikido connects to your GitHub Enterprise setup by creating a GitHub App on your server. The app includes the permissions and callbacks needed for Aikido to work. After it is created, you can install it in any organisation on your GitHub Server instance that you want to link to Aikido.\
\
To create the GitHub app on your instance, follow the steps below.

{% stepper %}
{% step %}

### Create your account

If you don’t have an Aikido account yet, create one through Google or Microsoft first. This is required before you can connect your GitHub Enterprise Server.

Open the [setup installation page](https://app.aikido.dev/onboarding/github-server/install-app), enter the URL of your GitHub Enterprise and click `Next, Install App`.

{% hint style="warning" %}
If your GitHub Enterprise Server is not reachable from the internet, enable the Broker setting.

For details about how the Aikido Broker works, [see the documentation.](https://help.aikido.dev/docs/miscellaneous-info/aikido-broker-for-internal-applications)
{% endhint %}

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FwIvfeXwO6TJAZNHOhhEW%2FScreenshot%202025-12-03%20at%2017.05.52.png?alt=media&#x26;token=fb4dffc0-b376-41e3-a820-621817dc3748" alt=""><figcaption></figcaption></figure>

{% endstep %}

{% step %}

### Install Aikido Github App on your Github Enterprise

A file named `install.html` is downloaded to your machine. It contains an HTML page with a form that sends a JSON payload to your GitHub Enterprise to create the GitHub App.

Open the file in your browser and select Install to continue the setup process.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fp9oazDrex1FjdANY139U%2FScreenshot%202025-11-25%20at%2017.41.41.png?alt=media&#x26;token=60c75430-4153-4b2e-85e4-e1e8544bc3cb" alt="" width="375"><figcaption></figcaption></figure>

After clicking "Install" you are redirected to a page on your GitHub Enterprise that prompts you to install the app. Choose `Create GitHub App for User` to create the app on your server.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F2d6VFuX7mrqjK01fHajy%2FScherm%C2%ADafbeelding%202025-11-25%20om%2016.12.59.png?alt=media&#x26;token=207335a2-4cb2-4ff2-a008-2e91913a716b" alt="" width="563"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Authorize Aikido Github app

Now you need to authorize the new GitHub App with your user account through OAuth. This step confirms that the app was created correctly and that you have permission to use it. The screen you see will be similar to the example below.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FJXheF9D7xoNYw13ikbfh%2Ftest.png?alt=media&#x26;token=c65e8924-be12-4fda-848e-0809a1900e4a" alt="" width="375"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Connect Github organization

Choose the GitHub organisation where you want to install the application and link it to Aikido. You can add more organisations later. After selecting the organisation, confirm the authorization for the GitHub App.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FpPKnUuZwjWSh8GPKBCWB%2Ftester.webp?alt=media&#x26;token=7465aa35-8984-4aed-ada7-678cf3708150" alt="" width="375"><figcaption></figcaption></figure>

You are now redirected back to Aikido where you can choose which repositories should be scanned. Select the repositories you want and continue. Aikido will start scanning the chosen applications.
{% endstep %}

{% step %}

### Explore Aikido

After granting access and validating the repositories you want to scan, Aikido will automatically start scanning. After about 1 minute, you should see the first results come in
{% endstep %}
{% endstepper %}

#### Managing the GitHub Enterprise App

{% content-ref url="connect-github-enterprise/connect-additional-organizations-to-aikido" %}
[connect-additional-organizations-to-aikido](https://help.aikido.dev/docs/code-scanning/connect-your-source-code/connect-github-enterprise/connect-additional-organizations-to-aikido)
{% endcontent-ref %}

{% content-ref url="connect-github-enterprise/transferring-ownership-of-the-aikido-app-in-github-enterprise" %}
[transferring-ownership-of-the-aikido-app-in-github-enterprise](https://help.aikido.dev/docs/code-scanning/connect-your-source-code/connect-github-enterprise/transferring-ownership-of-the-aikido-app-in-github-enterprise)
{% endcontent-ref %}

# Transferring Ownership of the Aikido App in Github Enterprise (Cloud & Server)

When you create the Aikido GitHub App inside your GitHub Enterprise environment, it is set up under the account of the user performing the installation. This follows the default GitHub flow when no prior ownership choice is known.

You can transfer the app to any other user or organization in your GitHub Enterprise Server environment at any time. This has no impact on how the app operates.

To transfer ownership, follow the steps below.

{% stepper %}
{% step %}

### Go to the Github App's developer Settings page

In your GitHub Server environment, navigate to Settings > Developer Settings > GitHub Apps.\
Click on "Edit".

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FRSQv666dC74rFZh5RkqE%2FScherm%C2%ADafbeelding%202025-12-02%20om%2010.15.04.png?alt=media&#x26;token=d4f5f6f6-d07e-4c19-83dc-435a7e1e1ccb" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Go to Advanced settings

In the left-hand navigation, go to the "Advanced" settings and scroll all the way down on the page until you see this section. \
\
Click on "Transfer ownership"<br>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F6GK1ce9BbATKp2X0woxG%2FScherm%C2%ADafbeelding%202025-12-02%20om%2010.17.15.png?alt=media&#x26;token=7ab9f996-e070-4894-a6eb-97a585c0d7e2" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Transfer ownership

Once you've clicked the button, you need to confirm the name of the App, and then you can select the organization or user to which you want to transfer the ownership.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FptOiNtbkk5MXLSo4EBEr%2FScherm%C2%ADafbeelding%202025-12-02%20om%2010.17.43.png?alt=media&#x26;token=1fad0324-3086-473c-a515-4cda2a9a1f64" alt=""><figcaption></figcaption></figure>

{% endstep %}

{% step %}

### Success

The App is now transferred to the new owner.
{% endstep %}
{% endstepper %}

# Connect additional organizations to Aikido

When the GitHub Enterprise instance has been connected to Aikido, you can start linking more GitHub orgs from your server instance to Aikido. Each org is linked to a single workspace in Aikido. To add more orgs, follow the steps below.

{% stepper %}
{% step %}

### Create a new workspace

From the left-hand navigation, open the workspace selector and click on "Add another workspace"

<p align="center"><br><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fp0GsjTVy40hp3c1ODPu0%2FScherm%C2%ADafbeelding%202025-12-15%20om%2010.06.45.png?alt=media&#x26;token=366785f3-85e9-4471-87e6-4b1a9cdda130" alt="" data-size="original"></p>
{% endstep %}

{% step %}

### Select "GitHub Enterprise Server"

On the next screen select the "GitHub Enterprise Server" option to start the setup flow.
{% endstep %}

{% step %}

### On the setup page, enter your GitHub server URL

On the setup page, just enter your GitHub Server URL to continue the setup. You will be redirected to GitHub straight away.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FDlFLiVdENPLZpSPLCVGe%2FScherm%C2%ADafbeelding%202025-12-15%20om%2010.23.31.png?alt=media&#x26;token=dde50b1d-df2c-4d12-aaa6-8d5dac842908" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Setup the organization in GitHub

On the GitHub installation page, select the organization and subsequently the repositories you would like to connect to Aikido.
{% endstep %}
{% endstepper %}

# Local Code Scanning

Local code scanning lets you analyze your source code directly on your own machines without sending any code to Aikido. It is useful when you want to test changes during development, work in isolated environments, or keep sensitive repositories fully local.

{% hint style="success" %}
For most workflows we still recommend using the [standard Aikido integrations](https://help.aikido.dev/docs/code-scanning/connect-your-source-code) as they give faster results and better coverage.
{% endhint %}

Before you start, make sure you have an Aikido account/workspace that supports local scanning. Follow [Account Creation for Local Scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/account-creation-for-local-scanning-on-aikido).

If you are looking to scan container images instead, check the [container image scanning docs](https://help.aikido.dev/docs/container-image-scanning/local-image-scanning).

## General

{% content-ref url="local-code-scanning/account-creation-for-local-scanning-on-aikido" %}
[account-creation-for-local-scanning-on-aikido](https://help.aikido.dev/docs/code-scanning/local-code-scanning/account-creation-for-local-scanning-on-aikido)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/pr-gating-for-code-using-local-scanner" %}
[pr-gating-for-code-using-local-scanner](https://help.aikido.dev/docs/code-scanning/local-code-scanning/pr-gating-for-code-using-local-scanner)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/release-gating-for-code-using-local-scanner" %}
[release-gating-for-code-using-local-scanner](https://help.aikido.dev/docs/code-scanning/local-code-scanning/release-gating-for-code-using-local-scanner)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/performing-nightly-scans-using-the-aikido-local-scanner" %}
[performing-nightly-scans-using-the-aikido-local-scanner](https://help.aikido.dev/docs/code-scanning/local-code-scanning/performing-nightly-scans-using-the-aikido-local-scanner)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/cli-options-for-local-scanner" %}
[cli-options-for-local-scanner](https://help.aikido.dev/docs/code-scanning/local-code-scanning/cli-options-for-local-scanner)
{% endcontent-ref %}

## CI/CD Integrations

{% content-ref url="local-code-scanning/azure-devops-server-setup-for-local-code-scanning" %}
[azure-devops-server-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/azure-devops-server-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/bitbucket-pipeline-setup-for-local-code-scanning" %}
[bitbucket-pipeline-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/bitbucket-pipeline-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/bamboo-setup-for-local-code-scanning" %}
[bamboo-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/bamboo-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/circleci-setup-for-local-code-scanning" %}
[circleci-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/circleci-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/github-action-setup-for-local-code-scanning" %}
[github-action-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/github-action-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/gitlab-self-managed-setup-for-local-code-scanning" %}
[gitlab-self-managed-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/gitlab-self-managed-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/jenkins-setup-for-local-code-scanning" %}
[jenkins-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/jenkins-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/teamcity-pipeline-setup-for-local-code-scanning" %}
[teamcity-pipeline-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/teamcity-pipeline-setup-for-local-code-scanning)
{% endcontent-ref %}

## Operating Systems

{% content-ref url="local-code-scanning/linux-setup-for-local-code-scanning" %}
[linux-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/linux-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/mac-setup-for-local-code-scanning" %}
[mac-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/mac-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/windows-setup-for-local-code-scanning" %}
[windows-setup-for-local-code-scanning](https://help.aikido.dev/docs/code-scanning/local-code-scanning/windows-setup-for-local-code-scanning)
{% endcontent-ref %}

## Other

{% content-ref url="local-code-scanning/local-scanning-in-existing-scm-integrated-workspaces" %}
[local-scanning-in-existing-scm-integrated-workspaces](https://help.aikido.dev/docs/code-scanning/local-code-scanning/local-scanning-in-existing-scm-integrated-workspaces)
{% endcontent-ref %}

---

[Next Page](/llms-full.txt/1)
