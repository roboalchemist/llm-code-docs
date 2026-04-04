# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/gitlab-integration/importing-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/importing-repos.md

# Importing your GitLab repositories

Once the integration of your SonarQube instance with GitLab has been properly set up, you can import a GitLab repository to create the corresponding project in SonarQube. To do so, you need the Create Project permission in SonarQube Server.

The so-created SonarQube project is "bound" to its GitLab repository. With a bound project:

* The project’s main branch name will be automatically set up from GitLab.
* The quality gate status report to the merge requests will be automatically set up.

{% hint style="info" %}
Starting in [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can import a GitLab monorepo. See [monorepos](https://docs.sonarsource.com/sonarqube-server/project-administration/monorepos "mention").
{% endhint %}

### Step 1: Create a Personal Access Token <a href="#one-or-several" id="one-or-several"></a>

You must provide a[ GitLab Personal Access Token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with `read_api` scope. This token will be stored in SonarQube and can be revoked at any time in GitLab. SonarQube will use this token to access and list your GitLab repositories. Copy it (you will have to paste it during Step 2). You may ask your administrator to encrypt this token.

### Step 2: Import one or several GitLab repositories <a href="#one-or-several" id="one-or-several"></a>

1. In the top navigation bar of SonarQube Server, select the **Projects** tab.
2. In the top right corner, select **Create Project** > **From GitLab**.The **GitLab project onboarding** page opens.
3. In **Personal Access Token**, enter the PAT you created in Step 1 and select **Save**. The repositories to which the PAT has access are listed on the page.
4. Select one or several repositories to be imported and follow the instructions.

### Related pages

[global-setup](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/global-setup "mention")\
[setting-up-at-project-level](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/setting-up-at-project-level "mention")
