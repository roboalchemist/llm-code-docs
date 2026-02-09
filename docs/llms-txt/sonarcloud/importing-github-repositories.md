# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/github-integration/importing-github-repositories.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/importing-github-repositories.md

# Importing GitHub repositories

Once the integration of SonarQube Server with GitHub has been set up , you can import a GitHub repository to create the corresponding project in SonarQube Server. The so-created SonarQube Server project is "bound" to its GitHub repository. With a bound project:

* You can see in the SonarQube Server UI with which repository the project is associated.
* The quality gate status report to GitHub on pull requests is automatically set up.
* You can set up report of security alerts, see [report-security-alerts](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/setting-up-at-global-level/report-security-alerts "mention") for more details.

To import a GitHub repository into SonarQube Server, do one of the following:

* Import the GitHub repository from the SonarQube Server UI: see below.\
  You need access to the GitHub repository and you need the **Create Projects** permission in SonarQube Server.
* Analyze a repository from a GitHub action. SonarQube Server will create the corresponding project in SonarQube Server and will automatically bind it to the GitHub repository if it finds a matching GitHub integration configuration in its database. See [adding-analysis-to-github-actions-workflow](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow "mention") for more information.

### Importing GitHub repositories <a href="#repositories" id="repositories"></a>

To import GitHub repositories into SonarQube Server:

1. In the top navigation bar of SonarQube Server, select the **Projects** tab.
2. In the top right corner, select the **Create Project** > **Import from DevOps platforms** button.
3. In the **Import from GitHub** section, select **Setup**. The **GitHub project onboarding** page opens.
4. In the **GitHub project onboarding** page, select the GitHub organization and then the repository(ies) you want to import.
5. Select the **Import** button. The Clean as You Code setting page opens.
6. Select the new code definition option.
7. Select the **Create projects** button.

### Importing a GitHub monorepo <a href="#monorepo" id="monorepo"></a>

Starting in [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can import a GitHub monorepo. See [monorepos](https://docs.sonarsource.com/sonarqube-server/project-administration/monorepos "mention") for more information.
