# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/issues/security-issues-in-devops-platform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/issues/security-issues-in-devops-platform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/issues/security-issues-in-devops-platform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/issues/security-issues-in-devops-platform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/issues/security-issues-in-devops-platform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/security-issues-in-devops-platform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/issues/security-issues-in-devops-platform.md

# Issues reported in DevOps platform

### Managing security issues in GitHub <a href="#github" id="github"></a>

When you analyze a project in SonarQube, the detected security issues are displayed on the GitHub interface as code scanning alerts, if set up in your system. See [report-security-alerts](https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts "mention") for more information. When you change the status of a security issue in the SonarQube interface that status change is immediately reflected in the GitHub interface. Similarly, if you change the status of a code scanning alert in GitHub, that change is reflected in SonarQube.

To view and manage your code scanning alerts:

1. In GitHub, go to your repository’s **Security** > **Code scanning alerts** tab.
2. Select **View alerts** to see the full list.

<figure><img src="https://512221655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyDv2XwTC1xoOKBYeCK45%2Fuploads%2Fgit-blob-8c8b17d188092d27734ec71043cbba94aeee73d9%2Fsonar-github-code-scanning-alerts.png?alt=media" alt="Managing your code scanning alerts in GitHub"><figcaption></figcaption></figure>

### Viewing the security issues in GitLab <a href="#gitlab" id="gitlab"></a>

When you analyze a project in SonarQube Server, the detected security issues are displayed on the GitLab interface as security vulnerabilities if set up in GitLab CI/CD. See [setting-up-at-project-level](https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/gitlab-integration/setting-up-at-project-level "mention") for more information. When you change the status of a security issue in the SonarQube Server interface that status change is immediately reflected in the GitLab interface. If you change the status of a security vulnerability in GitLab, that change is reflected in SonarQube Server during the next analysis.

To view the security vulnerabilities:

* Go to the **GitLab** > **Vulnerability** report page.

{% hint style="info" %}
If your issues appear duplicated (it may be the case after the modification of a file), we recommend using the **Activity** > **Still detected** filter.
{% endhint %}

### Viewing the issues detected on a pull request in Azure DevOps <a href="#azure-devops" id="azure-devops"></a>

When you run a SonarQube Server analysis for a pull request, each SonarQube issue is displayed as a comment on the Azure DevOps pull request. If the Azure DevOps instance is configured correctly and you change the status of an issue in SonarQube Server, that status change is immediately reflected in the Azure DevOps interface.

If you want to decorate your pull request with a quality gate status and are not interested to have SonarQube Server annotations in your PR, see the [#disable-pull-request-annotations](https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/setting-up-project-integration#disable-pull-request-annotations "mention") article.
