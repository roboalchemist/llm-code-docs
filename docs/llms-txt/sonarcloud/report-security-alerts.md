# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts.md

# Setting up the report of security alerts

SonarQube Server can provide feedback about security issues inside the GitHub interface itself as code scanning alerts under the **Security** tab. This feature is supported for bound projects only.

This page explains the feature and how to set it up. To view and manage the security issues reported in GitHub see [in-devops-platform](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/in-devops-platform "mention").

### Security alerts report overview <a href="#overview" id="overview"></a>

The report of security alerts in GitHub is part of the [GitHub Advanced Security package](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) and is currently free for public projects. It is available as a paid option for private projects and GitHub Enterprise. This option is entirely on the GitHub side. Sonar does not charge anything extra to enable the code scanning alerts feature.

#### Issue status synchronization <a href="#issue-status-synchronization" id="issue-status-synchronization"></a>

When users change the status of a security issue in the SonarQube Server interface, that status change is immediately reflected in the GitHub interface. Similarly, if users change an alert status in GitHub, that change is reflected in SonarQube Server.

Initially, all issues marked Open on SonarQube Server are marked Open on GitHub. Because the available statuses on the two systems are not exactly the same, the following logic is used to manage the transitions.

| **In SonarQube Server, a transition to:** | **Results in this On GitHub:** |
| ----------------------------------------- | ------------------------------ |
| Confirm (deprecated)                      | Open                           |
| Fixed                                     | Open                           |
| Accept                                    | Dismiss: Won’t Fix             |
| False Positive                            | Dismiss: False positive        |
| Open                                      | Open                           |

| **On Github, a transition to:** | **Results in this in SonarQube Server:** |
| ------------------------------- | ---------------------------------------- |
| Dismiss: False positive         | False Positive                           |
| Dismiss: Used in tests          | Accept                                   |
| Dismiss: Won’t fix              | Accept                                   |

#### Issue report and synchronization from SonarQube Server to GitHub <a href="#issue-report-and-synchronization-from-sonarqube-server-to-github" id="issue-report-and-synchronization-from-sonarqube-server-to-github"></a>

SonarQube Server reports security issues to GitHub’s Code scanning alerts by accessing GitHub through the GitHub App configured in [setting-up-github-app](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/setting-up-at-global-level/setting-up-github-app "mention").

#### Synchronization process from GitHub to SonarQube Server <a href="#synchronization-process-from-github-to-sonarqubeserver" id="synchronization-process-from-github-to-sonarqubeserver"></a>

The update in SonarQube Server of a security alert status change performed by a GitHub user is performed through a webhook mechanism as illustrated below. The procedure is as follows:

1. When a user changes a security alert status in GitHub, a webhook event is generated.
2. GitHub sends a webhook request to SonarQube Server to inform it about the event. To do so, it retrieves the webhook URL and the webhook secret from the GitHub App for SonarQube Server.
3. SonarQube Server checks the received webhook secret against the secret stored in the GitHub Configuration for security import.
4. If the check is successful, SonarQube Server updates the status of the respective security issue.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/YLLES7JLKq2t671LdTrz/sonarqube-github-security-alerts.png" alt="Synchronization process from GitHub to SonarQube Server"><figcaption></figcaption></figure>

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

The feature is only available to projects bound to their respective GitHub repository. It means that the integration of SonarQube Server with GitHub for repository import must have been set up.

In addition, GitHub must reach SonarQube to send the webhook request. This means that either SonarQube server base URL is a public URL, or you can use a reverse proxy to forward webhooks from GitHub to SonarQube’s private URL. for more information, see GitHub documentation on [Delivering webhooks to private systems](https://docs.github.com/en/webhooks/using-webhooks/delivering-webhooks-to-private-systems).

### Setting up the report in SonarQube Server <a href="#settting-up" id="settting-up"></a>

#### Enabling the feature in the GitHub App for SonarQube Server <a href="#enabling-the-feature-in-the-github-app-for-sonarqube-server" id="enabling-the-feature-in-the-github-app-for-sonarqube-server"></a>

If not already done, edit your GitHub App for SonarQube Server to enable and set up the report of security alerts to GitHub:

1. In GitHub, go to **Settings** > **Developer settings** > **GitHub Apps** and select your GitHub App.
2. Go to the **General** > **Webhook** section and make sure to select the active checkbox.
3. Add the following Webhook URL: https\://\<yourinstance>.sonarqube.com/api/alm\_integrations/webhook\_github. Replace \<yourinstance>.sonarqube.com with your SonarQube Server instance.
4. Set a Webhook secret, see [GitHub’s webhook security recommendations](https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks).
5. Under **Permissions & events** > **Repository permissions** > **Code scanning alerts**, set the access level to Read and write. When you update this permission, GitHub sends an email to the GitHub organization’s administrator, asking them to validate the changes on the installation of the GitHub App.
6. Under **Permissions & events > Subscribe to events**, select **Code scanning alert**.

#### Managing the user access to security alerts in GitHub <a href="#managing-the-user-access-to-security-alerts-in-github" id="managing-the-user-access-to-security-alerts-in-github"></a>

In GitHub, you can [configure access to security alerts](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository) for a repository to enable and disable security and analysis features.
