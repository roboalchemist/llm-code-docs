# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/setting-up-at-global-level/setting-parameters-for-github-actions.md

# Setting parameters for GitHub Actions

You can define at the global level the parameters used in GitHub Actions workflows to connect to the SonarQube Server (Server URL and token).

### Storing the authentication token in GitHub at the global level <a href="#token" id="token"></a>

To store sensitive data, use GitHub secrets: see GitHub’s documentation on [Encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets) for more information.

{% hint style="warning" %}
A token defined at the global level gives permissions on all projects in the SonarQube Server instance.
{% endhint %}

Proceed as follows to store the authentication token at the global level:

1. In the SonarQube Server UI, generate a SonarQube Server token at the global level.
2. Create an organization secret in GitHub with:
   * Name: SONAR\_TOKEN
   * Value: the token you generated in the previous step.

### Storing the SonarQube Server URL in GitHub at the global level <a href="#server-url" id="server-url"></a>

Create an [organization variable](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables) in GitHub with:

* Name: SONAR\_HOST\_URL
* Value: SonarQube Server URL.
