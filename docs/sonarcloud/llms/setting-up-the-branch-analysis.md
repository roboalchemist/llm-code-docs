# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md

# Setting up the branch analysis

To set up branch analysis:

1. Add the analysis step to your multi-branch CI pipeline. See the corresponding section of your CI tool in this documentation:
   * [add-analysis-to-job](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job "mention")
   * [introduction](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/introduction "mention")
   * [bitbucket-cloud-integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration "mention")
   * [codemagic-integration](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/codemagic-integration "mention")
   * [adding-analysis-to-github-actions-workflow](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow "mention")
   * [adding-analysis-to-gitlab-ci-cd](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd "mention")
2. Make sure the branch to be analyzed is properly checked out in the CI repository: see [verifying-code-checkout-step](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step "mention").
3. Make sure that the SonarScanner gets the branch name parameter (otherwise the analysis will be performed on the main branch): see **Setting up the branch name parameter** below.
4. Limit the analysis to the relevant branches: see **Limiting the analysis to the relevant branches** below.
5. Configure the Clean as You Code settings for the branches: see **Configuring the CaYC settings for branches** below.

### Setting up the branch name parameter <a href="#setup-branch-name" id="setup-branch-name"></a>

The SonarScanner can automatically detect the branch name parameters when running on the following CI services (you don’t need to perform any additional setup):

* Azure Pipelines
* Bitbucket Pipelines
* Cirrus CI
* Codemagic
* GitHub Actions
* GitLab CI/CD
* Jenkins (with the Branch Source plugin configured, see the [global-setup](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/global-setup "mention") page)

The table below shows the branch name parameter. See Analysis parameters for information about the setup of analysis parameters for the scanner.

|                    |                                        |
| ------------------ | -------------------------------------- |
| **Parameter Name** | **Description**                        |
| sonar.branch.name  | Name of the branch (visible in the UI) |

### Limiting the analysis to the relevant branches <a href="#limit-to-relevant-branches" id="limit-to-relevant-branches"></a>

You need to add a condition to your pipeline script to ensure that only the relevant branches are analyzed. For example, you wouldn’t want to run analysis on feature branches that won’t need analysis until they have pull requests.

In the following example, analysis would be limited to branches named `main` or `release/*`.

```css-79elbk
if [[ "$CI_BRANCH_NAME" == main ]] || [[ "$CI_BRANCH_NAME" == release/* ]]; then
  ./gradlew sonarqube
fi
```

### Configuring the CaYC settings for branches <a href="#configure-cayc-settings" id="configure-cayc-settings"></a>

See [about-new-code](https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code "mention") to learn how to implement this best practice.

The quality gate cannot be configured at the branch level, only at the project level. And ideally, all projects will use the same quality gate: see [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates "mention").

You can set a new code definition for each branch. This is especially helpful if you are likely to develop and release multiple versions from the branch. See the the [about-new-code](https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code "mention") page for more information.

{% hint style="info" %}
When using any new code period type other than Reference branch, we recommend completing your merges using the fast-forward option without a merge commit; examples include GitHub’s squash and merge or rebase and merge options. In this way, the blame for the merged commits will always have a more recent commit date.
{% endhint %}
