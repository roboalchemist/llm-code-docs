# Source: https://docs.sonarsource.com/sonarqube-cloud/discovering-sonarcloud/integration-with-devops-platforms.md

# Integration with DevOps platforms

This integration allows you to import your DevOps platform organization and its repositories into SonarQube Cloud, automatically binding SonarQube Cloud projects to their corresponding DevOps platform repositories. The integration also enables features like automatically triggering analysis in your CI/CD pipeline, displaying quality gate status in your DevOps pipeline, and preventing merges when the quality gate fails.

By default, users can authenticate to SonarQube Cloud with their existing credentials on their DevOps platform service (no additional setup is required). With the DevOps platform service authentication, Just-in-Time user provisioning is used.

{% hint style="info" %}
With the Enterprise plan, you can use Single Sign On authentication. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more information.
{% endhint %}

### GitHub <a href="#github" id="github"></a>

SonarQube Cloud’s integration is supported with GitHub plans running on the [github.com](https://github.com/) domain.

With this integration, you’ll be able to:

* Authenticate with GitHub (through the SonarQube Cloud GitHub application).\
  Automatic member synchronization is supported.
* Import your GitHub organization and its repositories into SonarQube Cloud to easily set up SonarQube Cloud projects.
* Analyze projects with GitHub Actions.\
  SonarScanners running in GitHub Actions jobs can automatically detect branches or pull requests being built.\
  You can fail the job if the SonarQube quality gate fails.
* Report your quality gate status to your branches and pull requests.\
  You can see your quality gate and code metric results right in GitHub so you know if it’s safe to merge your changes. You can prevent pull request merges when the quality gate fails.
* Import your monorepo into SonarQube Cloud to easily manage the related projects.

### Bitbucket Cloud <a href="#bitbucket-cloud" id="bitbucket-cloud"></a>

With SonarQube Cloud’s integration with Bitbucket Cloud, you’ll be able to:

* Authenticate with Bitbucket Cloud (through OAuth authentication).
* Import your Bitbucket workspace and its repositories into SonarQube Cloud to easily set up SonarQube Cloud projects.
* Analyze projects with Bitbucket Pipelines.\
  SonarScanners running in Bitbucket Pipelines can automatically detect branches or pull requests being built.\
  You can fail the pipeline if the SonarQube quality gate fails.
* Report your quality gate status to your branches and pull requests.\
  You can see your quality gate and code metric results right in Bitbucket Cloud so you know if it’s safe to merge your changes. You can prevent pull request merges when the quality gate fails.
* Import your monorepo into SonarQube Cloud to easily manage the related projects.

### GitLab <a href="#gitlab" id="gitlab"></a>

With SonarQube Cloud’s integration with GitLab, you’ll be able to:

* Authenticate with GitLab (through OAuth authentication).
* Import your GitLab group and its repositories into SonarQube Cloud to easily set up SonarQube Cloud projects.
* Analyze projects with GitLab CI/CD.\
  SonarScanners running in GitLab CI/CD jobs can automatically detect branches or pull requests being built.\
  You can fail the job if the SonarQube quality gate fails.
* Report your quality gate status to your branches and pull requests.\
  You can see your quality gate and code metric results right in GitLab so you know if it’s safe to merge your changes. You can prevent pull request merges when the quality gate fails.
* Import your monorepo into SonarQube Cloud to easily manage the related projects.

### Azure DevOps <a href="#azure-devops" id="azure-devops"></a>

SonarQube Cloud’s integration is supported with Azure DevOps Services.

With this integration, you’ll be able to:

* Authenticate with Azure DevOps (through OAuth authentication).
* Import your Azure DevOps organization and its repositories into SonarQube Cloud to easily set up SonarQube Cloud projects.
* Analyze projects with Azure Pipelines.\
  SonarScanners running in Azure Pipelines can automatically detect branches or pull requests being built.\
  You can fail the pipeline if the SonarQube quality gate fails.
* Report your quality gate status to your branches and pull requests.\
  You can see your quality gate status right in Azure Pipeline’s Build Summary page. Issues detected on pull requests are displayed on the Azure DevOps pull request. You can prevent pull request merges when the quality gate fails.
* Import your monorepo into SonarQube Cloud to easily manage the related projects.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [github](https://docs.sonarsource.com/sonarqube-cloud/getting-started/github "mention")
* [bitbucket-cloud](https://docs.sonarsource.com/sonarqube-cloud/getting-started/bitbucket-cloud "mention")
* [gitlab](https://docs.sonarsource.com/sonarqube-cloud/getting-started/gitlab "mention")
* [azure-devops](https://docs.sonarsource.com/sonarqube-cloud/getting-started/azure-devops "mention")
