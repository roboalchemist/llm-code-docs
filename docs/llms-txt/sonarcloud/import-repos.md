# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/import-repos.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/import-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/import-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/bitbucket-integration/data-center/import-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/import-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/import-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/import-repos.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/import-repos.md

# Importing your Bitbucket Data Center repositories

Once the integration of your SonarQube instance with Bitbucket Data Center has been properly set up, you can import a Bitbucket repository to create the corresponding project in SonarQube. To do so, you need the Create Project permission in SonarQube.

The so-created SonarQube project is "bound" to its Bitbucket repository. With a bound project:

* The project’s main branch name will be automatically set up from Bitbucket.
* The quality gate status report to the pull requests will be automatically set up.

{% hint style="info" %}
Starting in[ Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can import a Bitbucket monorepo. See [monorepos](https://docs.sonarsource.com/sonarqube-server/project-administration/monorepos "mention").
{% endhint %}

### Step 1: Create a Personal Access Token

You must provide a Bitbucket Data Center [Personal Access Token](https://confluence.atlassian.com/bitbucketserver0717/personal-access-tokens-1087535496.html) with `Read` permissions for both projects and repositories. This token will be stored in SonarQube and can be revoked at any time in bitbucket. SonarQube will use this token to access and list your Bitbucket projects and repositories. Copy it (you will have to paste it during Step 2). You may ask your administrator to encrypt this token.

### Step 2: Import one or several Bitbucket repositories

1. In the top navigation bar of SonarQube, select the **Projects** tab.
2. In the top right corner, select **Create Project > From Bitbucket Server**. The Bitbucket project onboarding page opens.
3. In **Personal Access Token**, enter the PAT you created in Step 1 and select **Save**. The projects and repositories to which the PAT has access are listed on the page.
4. Select one or several repositories to be imported and follow the instructions.

### Related pages

[global](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/global "mention")\
[project](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/project "mention")\
[encrypting-settings](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings "mention")
