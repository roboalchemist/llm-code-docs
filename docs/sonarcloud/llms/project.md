# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/bitbucket-integration/data-center/project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/project.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/project.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/project.md

# Setting up Bitbucket Data Center integration for your project

### Reporting your quality gate status to Bitbucket for unbound projects

On SonarQube Server projects bound to their Bitbucket repository, SonarQube Server automatically sets up the report of your quality gate status and analysis metrics directly to your pull requests. For unbound projects, you must set up the quality gate status report manually. The integration of your SonarQube Server instance with Bitbucket Data Center must be properly set up.

To report your quality gate status in Bitbucket for unbound projects:

1. In the SonarQube Server UI page of your project, select Project Settings > General Settings > DevOps Platform Integration.
2. Set:
   * **Configuration name**: The configuration name that corresponds to your DevOps Platform instance.
   * **Project Key**: the project key is part of your BitBucket repository URL (`.../projects/<key>/repos/<slug>/browse`).
   * **Repository SLUG**: The repository slug is part of your BitBucket repository URL (`.../projects/<key>/repos/<slug>/browse`).

### Preventing pull request merges when the quality gate fails

After setting up pull request analysis, you can block pull requests from being merged if it is failing the quality gate. To do this:

1. In Bitbucket Data Center, navigate to Repository settings > Code Insights.
2. Add a Required report called com.sonarsource.sonarqube
3. Select Must pass as the Required status.
4. Select Must not have any annotations as the Annotation requirements.

{% hint style="info" %}
Preventing pull request merges when the quality gate fails is not supported for monorepos.
{% endhint %}

### Related pages

[global](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/global "mention")\
[import-repos](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/import-repos "mention")
