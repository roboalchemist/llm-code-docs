# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/setting-up-at-project-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/setting-up-at-project-level.md

# Setting up GitHub integration for your project

### Setting up pull request integration <a href="#pull-request-integration" id="pull-request-integration"></a>

For bound projects (projects created by importing the GitHub repository), pull request decoration is supported in GitHub provided the pull request analysis has been properly set up in your project. See [setting-up-the-pull-request-analysis](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis "mention").

You can bind an existing and manually created project to its GitHub repository provided the global integration of SonarQube Server with GitHub has been properly set up. To do so, see [changing-project-binding](https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/changing-project-binding "mention").

### Disabling the analysis summary in GitHub Conversation tab <a href="#disable-summary-in-conversation-tab" id="disable-summary-in-conversation-tab"></a>

By default, SonarQube Server shows the analysis summary in the Conversation and Checks tab of your GitHub pull requests.&#x20;

To disable the summary in the Conversation tab:

* In your SonarQube Server project page, navigate to **Project Settings** > **General Settings** > **DevOps Platform Integration** and unselect **Enable analysis summary under the GitHub Conversation tab**.

### Preventing pull request merges when the quality gate fails <a href="#preventing-pull-request-merges" id="preventing-pull-request-merges"></a>

In GitHub, you can block pull requests from being merged if it is failing the quality gate. To do this:

1. In GitHub, go to your repository **Settings** > **Branches** > **Branch protection rules** and select either the **Add rule** or **Edit** button if you already have a rule on the branch you wish to protect.
2. Complete the **Branch protection rule** form:
   * Define the **Branch name pattern** (the name of the branch you wish to protect)
   * Select **Require status checks to pass before merging** to open supplementary form fields.
   * In the **Search for status checks in the last week** for this repository field, select **Require branches to be up to date before merging**, then find `SonarQube Code Analysis` and add it to the list of required checks.

### Related pages

* [github](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/in-devops-platform/github "mention")
