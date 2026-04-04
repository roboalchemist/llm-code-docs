# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/creating-project/importing-repo.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/creating-your-project/importing-repo.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/creating-your-project/importing-repo.md

# Importing your DevOps platform repository

Once the global-level integration with your DevOps platform is complete, you can create your SonarQube Server project by importing your DevOps platform repository. The so-created SonarQube Server project is "bound" to its Azure DevOps repository. With a bound project, you benefit from integration features, such as pull request decoration, code scanning alerts, permission synchronization, etc.

To import your repository, you need the Create Projects permission in SonarQube Server and the corresponding access rights on the repository.

To import a DevOps platform repository into SonarQube Server:

1. In the top navigation bar of SonarQube Server, select the **Projects** tab.
2. In the top right corner, select the **Create Project > From \<DevOps Platform>** button.
3. If your instance has multiple DevOps platform Integrations, select the configuration from which you want to import your project.
4. Select the repository to be imported.

For more information, see the section corresponding to your DevOps platform:

* [importing-github-repositories](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/importing-github-repositories "mention")
* [import-repos](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/import-repos "mention")
* [import-repos](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/import-repos "mention")
* [importing-repos](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/importing-repos "mention")
* [creating-your-project](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/creating-your-project "mention")

{% hint style="info" %}
Starting in [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can import a monorepo. See [monorepos](https://docs.sonarsource.com/sonarqube-server/project-administration/monorepos "mention").
{% endhint %}
