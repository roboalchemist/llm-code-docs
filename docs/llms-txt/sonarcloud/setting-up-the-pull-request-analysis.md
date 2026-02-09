# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md

# Setting up the pull request analysis

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

The pull request analysis must be integrated into a CI pipeline. For more information, see **Integration into your CI pipeline** on the [analysis-overview](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-overview "mention") page.

Before analyzing your pull requests, make sure that:

* The pull request source branch is checked out in the CI/CD host’s local repository.
* The branch being targeted by the pull request (target branch) is fetched in the CI/CD host’s local repository (This is usually done through the cloning of the remote repository by the CI pipeline).
* The CI/CD host’s local repository contains valid repository metadata (e.g. the `.git` folders have not been removed). Avoid any attempt at previewing the merge or actions involving your main branch.\
  See [verifying-code-checkout-step](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step "mention").
* The code in the CI/CD host’s local repository matches the code in the remote repository (e.g once a pull request is issued, no code is added to the local branch on the CI side before analysis).
* If you use AWS CodeBuild, the `LOCAL_SOURCE_CACHE` feature must be disabled for accurate pull request analysis (otherwise, new code won’t be properly detected).

### Setting up the pull request analysis <a href="#setup-analysis" id="setup-analysis"></a>

1. Add the SonarQube Server analysis step to your pull request CI pipeline. See the corresponding section of your CI tool in this documentation:
   * [add-analysis-to-job](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job "mention")
   * [introduction](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/introduction "mention")
   * [bitbucket-cloud-integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration "mention")
   * [codemagic-integration](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/codemagic-integration "mention")
   * [adding-analysis-to-github-actions-workflow](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow "mention")
   * [adding-analysis-to-gitlab-ci-cd](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd "mention")
2. Make sure that the SonarScanner gets the pull request parameters required for the project analysis: see **Setting up the pull request parameters** below.
3. In addition, you can configure the pull request decoration: see **Configuring the quality gate status report** below.

### Setting up the pull request parameters <a href="#setup-pull-request-parameters" id="setup-pull-request-parameters"></a>

The SonarScanner can automatically detect the pull request parameters when running on the following CI services (you don’t need to perform any additional setup):

* Azure Pipelines
* Bitbucket Pipelines
* Cirrus CI
* Codemagic
* GitHub Actions
* GitLab CI/CD
* Jenkins (with the Branch Source plugin configured)

The table below lists the analysis parameters specific to the pull request analysis that are required by the SonarScanner. See Analysis parameters for information about the setup of analysis parameters for the scanner.

| **Parameter Name**       | **Description**                                                                                                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sonar.pullrequest.key    | <p>Unique identifier of your pull request. Must correspond to the key of the pull request in your DevOps Platform.</p><p><strong>Example</strong>: <code>sonar.pullrequest.key=5</code></p>        |
| sonar.pullrequest.branch | <p>The name of the branch that contains the changes to be merged.</p><p><strong>Example</strong>: <code>sonar.pullrequest.branch=feature/my-new-feature</code></p>                                 |
| sonar.pullrequest.base   | <p>The branch into which the pull request will be merged (target branch).</p><p><strong>Default</strong>: main branch</p><p><strong>Example</strong>: <code>sonar.pullrequest.base=main</code></p> |

{% hint style="warning" %}
Manually setting pull request parameters overrides automatic detection.
{% endhint %}

### Configuring the quality gate status report <a href="#configure-quality-gate-report" id="configure-quality-gate-report"></a>

You can report the pull request analysis and quality gate status directly in your DevOps platform’s interface (pull request decoration). For projects bound in SonarQube Server to their DevOps platform repository (this requires the integration setup of your DevOps platform with SonarQube Server), the quality gate status report is automatically set up. For more information, see the DevOps platform integration page that corresponds with your DevOps platform:

* [introduction](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/introduction "mention")
* [bitbucket-server-integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration "mention")
* [bitbucket-cloud-integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/introduction "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/introduction "mention")
