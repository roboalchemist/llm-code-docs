# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/pull-request-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis.md

# Pull request analysis

A pull request code review and analysis is your second line of defense in keeping your code clean. Your first line of defense is using SonarQube for IDE to find issues right in your IDE. Once you have addressed those issues, you can go ahead and create a pull request to merge your changes into the main branch of your project. SonarQube Cloud will automatically analyze the code changes it introduces and report the result, both in the SonarQube Cloud interface and in the pull requests view of your DevOps platform. This step can find issues that are not detectable inside the IDE with SonarQube for IDE, giving you the opportunity to address them before you merge the pull request.

In the SonarQube Cloud Free plan, pull request analysis is available only when the pull request is merged into the main branch. Please see the [#comparison-table](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans#comparison-table "mention") for plan details.

{% hint style="info" %}
The term *pull request* is used by most repository providers. GitLab, however, uses the term "merge request". Both terms refer to the same functionality and are handled equivalently in Sonar products. In our documentation, any use of the term *pull request* applies equally to GitLab merge requests.
{% endhint %}

### Understanding your pull request analysis <a href="#understanding-your-pull-request-analysis" id="understanding-your-pull-request-analysis"></a>

From your project's main page, select **Pull Requests** to see a list of all pull requests for which an analysis has been completed:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-aeadfaf1c744ca77334d15d5ad94cc7b93419ddd%2F90ffe4fae5335d2c74ff40614ab596f2977561c4.png?alt=media" alt="The Pull Requests page shows you a list of all PR analyses that have been made on your project."><figcaption></figcaption></figure></div>

For each pull request in the list, the name of the pull request, the commit at which the latest analysis was performed, and the resulting quality gate status on that pull request are displayed. To see more details, select your pull request by name:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-f11cd5759f117a2adcb340cfff030c2905b79b62%2F956b194c04879f17ac3639e59192215d3f80056e.png?alt=media" alt="Selecting your Pull Request analysis by name will open a summary page where you can look at the potential issues that PR is about to introduce."><figcaption></figcaption></figure></div>

### Pull request decoration <a href="#pull-request-decoration" id="pull-request-decoration"></a>

In addition to appearing in the SonarQube Cloud interface, the quality gate status and a summary of the results also appear in your DevOps platform interface (that is, in the pull request view of GitHub, Bitbucket Cloud, Azure DevOps or GitLab). This is referred to as pull request decoration. But, it is not just decorative! It also integrates with your DevOps platform to block the merge of the pull request if the quality gate fails. In this way, you can benefit from SonarQube Cloud code review and analysis without even leaving the environment of your DevOps platform.

A pull request decoration summary comment will look like this (it is similar on the supported platforms):

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-4b3b11ff9993ec957f4df5625fc41d84b38ea46e%2Fb150f4342c45de178ad0652526e8e7280b75f23a.png?alt=media" alt="Summary of the results and the quality gate status on a PR." width="375"><figcaption></figcaption></figure></div>

In addition, depending on your platform, issues may be reported as inline annotations. For more information, see [in-devops-platform](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/in-devops-platform "mention").

### Quality gate and metrics <a href="#quality-gate-and-metrics" id="quality-gate-and-metrics"></a>

Pull request analysis differs from main branch (and other long-lived branch) analysis in two important ways:

* Pull request analysis only reports issues that were introduced by the pull request itself. When SonarQube Cloud analyzes a pull request **P** for the merge of branch **B** into base branch **T** it scans the HEAD commit of **B** and compares the result with the most recent scan of **T**. Only issues that appear in **B** but not in **T** are reported in the analysis results. In cases where **T** includes new issues added since the most recent scan (in other words the scan is outdated) those additional issues will appear as part of the pull request analysis, even though they were not introduced by the pull request. Therefore, an up-to-date analysis of **T** is required to correctly detect which issues are new.
* The quality gate for the pull request is computed based on this analysis. The quality gate used is the one set at the project level, however, *only the conditions on new code within the quality gate are applied*.

{% hint style="info" %}
As outlined above, the scanner starts by analyzing the HEAD commit, the most recent commit in your current branch. If the head commit is not defined, it scans the remote branch and, if that is not available, the upstream branch.
{% endhint %}

Above you can see that on the **Summary** tab, the quality gate and the five quality metrics are displayed. In addition, the other tabs, **Issues**, **Measures**, and **Code** let you see more details about the analysis.

### Enabling pull request analysis <a href="#enabling-pull-request-analysis" id="enabling-pull-request-analysis"></a>

Pull request analysis is available on all supported repository providers. Of course, to see an analysis result, an analysis must be performed on the pull request. If you are using automatic analysis (which is only available on GitHub) then this happens without any further configuration on pull request creation and on every push to the pull request branch. If you are using build analysis then you must make sure that your build script is configured to build on pull request creation and push.

### Prerequisites for CI-based analysis <a href="#prerequisites-for-ci-based-analysis" id="prerequisites-for-ci-based-analysis"></a>

Before analyzing your pull requests, make sure that:

* The pull request source branch is checked out in CI/CD host’s local repository.
* The branch being targeted by the pull request is fetched and present in the local repository (This is usually done through the cloning of the remote repository by the CI pipeline).
* The local repository contains valid repository metadata (e.g. the `.git` folders have not been removed). See [verifying-code-checkout-step](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/scanner-environment/verifying-code-checkout-step "mention").
* The code in the local repository matches the code in the remote repository (e.g once a pull request is issued, no code is added to the local branch on the CI side before analysis).

### Existing pull requests on first automatic analysis <a href="#existing-pull-requests-on-first-automatic-analysis" id="existing-pull-requests-on-first-automatic-analysis"></a>

When a project is first imported into SonarQube Cloud and analyzed by automatic analysis the first analysis behaves differently from subsequent analyses. On the first analysis not only will the main branch be analyzed, but, also *the most recently active pull requests, up to a maximum of five*. The main branch and pull request results will appear on the [project overview](https://docs.sonarsource.com/sonarqube-cloud/improving/main-branch-analysis), as usual. Subsequent analyses will occur normally, on pushes to the main branch and on pushes to pull request branches.

### SonarQube Remediation agent

{% hint style="success" %}
The SonarQube Remediation Agent is a [Beta](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#beta) feature available with Enterprise plan accounts. It is free during the beta phase and will be a paid feature when it moves to [General Availability](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#general-availability). To learn more about the terms & conditions, please see our legal page about features in [Early Access](https://www.sonarsource.com/legal/early-access/).

If your SonarQube Cloud organization is not on an Enterprise plan, please see the [getting-started-with-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise "mention") pages to get the process started.
{% endhint %}

The SonarQube Remediation agent can generate fix suggestions for certain types of issues found during a pull request analysis of your GitHub repository. AI-generated fix suggestions offered by the agent that are reviewed and accepted by users, can be included as new commits to the pull request before merging.

See the [sonarqube-remediation-agent](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/sonarqube-remediation-agent "mention") page for the full list of requirements and instructions to install and enable the agent. If your agent is already enabled and you're ready to engage, check out the [agents-in-your-github-pull-request](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/with-ai-features/agents-in-your-github-pull-request "mention") page to understand how the agent's behavior.

### Pull request analysis and SonarQube for IDE <a href="#pull-request-analysis-and-sonarlint" id="pull-request-analysis-and-sonarlint"></a>

The [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention") extension works well with pull request analysis. When running [SonarQube for IDE](https://www.sonarsource.com/products/sonarlint/), issues will be highlighted even before you create your pull request.

If SonarQube for IDE shows your code as clean, you can open a pull request and SonarQube Cloud will perform the pull request analysis to detect more complex issues that were not detectable by SonarQube for IDE.

In this way SonarQube for IDE together with pull request analysis give you two levels of protection to help keep your code clean.

### Incremental analysis <a href="#incremental-analysis" id="incremental-analysis"></a>

[incremental-analysis-mechanisms](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/incremental-analysis-mechanisms "mention") are used to shorten the pull request analysis.
