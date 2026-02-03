# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app.md

# Setting up a GitHub App

You need to use a GitHub App to connect SonarQube Server with a GitHub instance in order to be able to use the following features:

* Importing your GitHub repositories into SonarQube Server.
* Delegating the SonarQube Server user authentication to GitHub.
* [autodetect-ai-code](https://docs.sonarsource.com/sonarqube-server/ai-capabilities/autodetect-ai-code "mention") in projects using GitHub and GitHub Copilot.

You need the global Administer System permission in SonarQube Server to perform this setup.

### Setup overview <a href="#overview" id="overview"></a>

To set up a GitHub App to integrate SonarQube Server with GitHub:

1. Before starting, see [#related-pages](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/introduction#related-pages "mention").
2. Register a GitHub App for SonarQube Server.
3. Install the App on the organizations SonarQube Server needs to access.
4. Add the App to SonarQube Server’s global setup through a "GitHub Configuration" record. You must:
   * Create one GitHub Configuration for the GitHub repository import.
   * Create one GitHub Configuration for the user authentication delegation.

### Step 1: Register a GitHub App for SonarQube Server <a href="#register-a-github-app-for-sonarqube-server" id="register-a-github-app-for-sonarqube-server"></a>

See GitHub’s documentation on [registering a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) for general information on GitHub Apps.

In the procedure below, we recommend registering a public App. You can register a private App if you have only one GitHub organization. In that case, you must register the App under that organization.

Specify the following settings in your app:

* **GitHub App Name**: Your app’s name. Example: sonarqubeserver.
* **Homepage URL**: Your SonarQube Server instance’s base URL (for information purposes only).
* **Callback URL**: Your SonarQube Server instance’s base URL (the URL used to redirect to the SonarQube Server).
* **Webhook URL**: To improve security, webhooks, by default, are not allowed to point to the SonarQube Server. Therefore, we recommend that you disable the feature unless you want to enable alerts for security issues in GitHub. See [report-security-alerts](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts "mention") for more information. To disable the feature, clear the Webhook Active checkbox to silence a forthcoming deprecation warning, and clear the Webhook URL and Webhook secret fields.
* **Under Permissions & events**, set up the permissions and events as explained below. Some permissions or events are only necessary depending on the purpose of the integration.

<details>

<summary>Permissions &#x26; events</summary>

**Repository permissions**

| Permission                                                                                                        | Access       | Note                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checks                                                                                                            | Read & Write | <p><br></p>                                                                                                                                                                                                                                                             |
| Administration                                                                                                    | Read-only    | Required only for user provisioning.                                                                                                                                                                                                                                    |
| <p><strong>GitHub Enterprise Server:</strong> Repository metadata</p><p><strong>GitHub.com</strong>: Metadata</p> | Read-only    | <p><br></p>                                                                                                                                                                                                                                                             |
| Pull Requests                                                                                                     | Read & Write | <p><br></p>                                                                                                                                                                                                                                                             |
| **Private repositories:** Contents                                                                                | Read-only    | <p><br></p>                                                                                                                                                                                                                                                             |
| Code scanning alerts                                                                                              | Read & Write | Required only if you want to report security alerts raised in SonarQube Server to GitHub. When you update this permission, GitHub sends an email to the GitHub organization’s administrator, asking them to validate the changes on the installation of the GitHub App. |

**Organization permissions**

| Permission              | Access    | Note                                                                          |
| ----------------------- | --------- | ----------------------------------------------------------------------------- |
| Administration          | Read-only | Required only for user provisioning.                                          |
| GitHub Copilot Business | Read-only | Required only to use SonarQube Server’s Autodetect AI-Generated Code feature. |
| Members                 | Read-only | <p><br></p>                                                                   |
| Projects                | Read-only | <p><br></p>                                                                   |

**Account permissions**

| Permission      | Access    | Note                                                    |
| --------------- | --------- | ------------------------------------------------------- |
| Email addresses | Read-only | Required only for user authentication and provisioning. |

**Subscribe to events**

Only if you want to report security alerts raised in SonarQube Server to GitHub:

Select **Code scanning alert**.

</details>

* Under **Where can this GitHub App be installed?** select **Any account** to make the App public in order to allow you in step 2 to install the App on any organization.

### Step 2: Install the GitHub App for SonarQube Server in your organizations <a href="#install-github-app-on-organization" id="install-github-app-on-organization"></a>

You need to install the GitHub App for SonarQube Server on the GitHub organizations that SonarQube Server will need to access. See GitHub’s documentation on [installing GitHub Apps](https://docs.github.com/en/free-pro-team@latest/developers/apps/installing-github-apps) for more information.

### Step 3: Add the GitHub App to SonarQube Server’s global setup <a href="#add-github-app-to-sonarqube-setup" id="add-github-app-to-sonarqube-setup"></a>

You need to create a GitHub Configuration record in SonarQube Server and add the GitHub App to it. The setup is different depending on your integration purpose:

<details>

<summary>If you want to support the GitHub repository import</summary>

To add the GitHub App to SonarQube Server’s global setup for repository import:

1. In the SonarQube UI, go to **Administration** > **Configuration** > **General Settings** > **DevOps Platform Integrations**.
2. Select the **GitHub** tab and click **Create configuration**. The **New GitHub configuration** dialog opens.
3. Specify the settings: see **Configuration settings** below.

</details>

<details>

<summary>If you want to delegate the user authentication to GitHub</summary>

To add the GitHub App to SonarQube Server’s global setup for user delegation, go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitHub**. See Connecting your GitHub App to SonarQube Server in [github](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/github "mention") authentication.

</details>

<details>

<summary>Configuration settings</summary>

| **Field**          | **Description**                                                                                                                                                                                                               | **Note**                                                                                                                                                                      |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuration name | <p>The name used to identify your GitHub Configuration. Use something succinct and easily recognizable.</p><p><br></p>                                                                                                        | Only available in editions authorizing the integration with multiple GitHub instances: Enterprise Edition and Data Center Edition.                                            |
| GitHub API URL     | <p>The API URL of the GitHub instance. For example, <https://github.company.com/api/v3> for GitHub Enterprise or <https://api.github.com/> for GitHub.com.</p><p><br></p>                                                     | <p><br></p>                                                                                                                                                                   |
| GitHub App ID      | The App ID of your GitHub App (on GitHub, go to **Settings** > **Developer Settings** > **GitHub Apps** to view your App).                                                                                                    | <p><br></p>                                                                                                                                                                   |
| Client ID          | The Client ID of your GitHub App’s page.                                                                                                                                                                                      | <p><br></p>                                                                                                                                                                   |
| Client Secret      | The Client secret of your GitHub App’s page. Administrators can encrypt this secret. See [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings "mention"). | <p><br></p>                                                                                                                                                                   |
| Private Key        | Your GitHub App’s private key in PEM format. You can generate a .pem file from your GitHub App’s page under Private keys. Copy and paste the whole contents of the file here.                                                 | Administrators can encrypt this key. See [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings "mention"). |
| Webhook Secret     | Webhook secret defined in your GitHub App to enable the report of code scanning alerts..                                                                                                                                      | Required only if you want to enable code scanning alerts for security issues in GitHub.                                                                                       |

</details>

{% hint style="info" %}
Standard GitHub procedures require confirmation when access levels are changed. Typically, this is done by confirming via an email sent to administrators.
{% endhint %}
