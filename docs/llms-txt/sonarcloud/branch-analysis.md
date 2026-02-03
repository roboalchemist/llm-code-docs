# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/branches/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/branches/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/branches/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/branches/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/branches/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/branches/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/branches/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/branches/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/branches/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/branch-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis.md

# Branch analysis

*This feature is only available in the Team and Enterprise plans. Only the main branch analysis is available in the Free plan. See* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") *for more information.*

Branch analysis in SonarQube Cloud lets you analyze branches of your project other than pull request branches and the main branch.

### What is branch analysis for? <a href="#what-is-branch-analysis-for" id="what-is-branch-analysis-for"></a>

In most projects, SonarQube Cloud is configured to do two kinds of analyses:

* [main-branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/main-branch-analysis "mention"): This occurs every time a change is pushed to the main branch. The analysis is done on the current state of the main branch, that is, the state recorded in the `HEAD` commit of the main branch, with a special focus on new code. The results of this analysis track the quality of the whole project and are used (via the quality gate) to ensure that the project is always in a releasable state.
* [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention"): This occurs when a pull request is opened and every time a change is pushed to the pull request branch. Analysis results only include issues that have been introduced by the pull request itself. A quality gate on the pull request uses these results to ensure that the code changes introduced are always clean.

**Branch analysis**, in contrast, allows you to trigger an analysis on a push to *any specified branch* (not just the main branch) *without involving pull requests*. This capability can be useful in the following situations:

* If your project has **long-living branches** other than the main branch that you want to analyze. One use-case is having branches for older versions of your software that you still periodically update with critical fixes. Another is having separate branches for *development* and *production* in your project.
* If you use **short-lived branches** (for example, "feature" branches) to introduce changes to your main branch but do not use them with a pull request mechanism in a supported CI.

To support these use-cases, SonarQube Cloud lets you specify whether a branch is short- or long-lived using a naming convention. Based on this distinction, it will then analyze the two types of branches differently. For full details on setting up branch analysis and how it works, see [branch-analysis-setup](https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis-setup "mention"). But first, an understanding of the results of the branch analysis will help.

In the SonarQube Cloud Free plan, branch analysis is available only on the main branch. Please see the *Comparison table* on the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for plan details.

### Branch analysis results <a href="#what-is-branch-analysis-for" id="what-is-branch-analysis-for"></a>

Assuming that you have set up your branch analysis properly, every time you push to the branch in question, SonarQube Cloud will analyze and report the result in the SonarQube Cloud interface. To see the analysis result, go to the project and select **Branches** from the left menu sidebar.

This view displays the main branch, as well as any other long-lived or short-lived branches that have been analyzed. It does not include branches that have been used for pull requests.

![](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-2879af7f9e3aa307515f3af81d2fb17d4a04141e%2F5a22c53973c9551a4ea033a25acc100471840ed6.png?alt=media)

As we can see here, the view is organized into *long-lived branches* and *short-lived branches.*

SonarQube Cloud knows which is which based on the naming convention mentioned above. In this case, `branch-a` is considered a long-lived branch because its name matches the pattern `(branch|release)-.*` and the short branch is considered a short-lived branch because its name does not. The *main branch* is always considered a long-lived branch.

### Short-lived branch analysis <a href="#short-lived-branch-analysis" id="short-lived-branch-analysis"></a>

If you click on a short-lived branch, you will be taken to the short-lived branch analysis page:

![](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-becd933cc5fa5a7fc423767c0a74818ef99b775a%2F792f00899f1b3afb70d28f8517867e0f431435b6.png?alt=media)

You will notice that it is very similar to the **Pull Requests** analysis page. This is because it is based on the same principles. Like pull request analysis, short-lived branch analysis has two significant features:

* *Short-lived branch analysis only reports issues that were introduced by the branch itself*. When SonarQube Cloud analyzes a short-lived branch **B** with target branch **T** it scans the HEAD commit of **B** and compares the result with the most recent scan of **T**. Only issues that appear in **B** but not in **T** are reported in the analysis results. In cases where **T** includes new issues added since the most recent scan (in other words, the scan is outdated) those additional issues will appear as part of the short-lived branch analysis, even though they were not introduced by that branch. To understand how the target branch is determined see the [branch-analysis-setup](https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis-setup "mention") page.
* The quality gate for the short-lived branch is computed based on this analysis. The quality gate used is the one set at the project level, however, *only the conditions on new code within the quality gate are applied*.

When selecting a **Short-lived branch** from the list of branches, you can see that on the **Summary** tab, the quality gate and the six quality metrics are displayed. In addition, the other tabs, **Issues**, **Security Hotspots**, **Measures**, and **Code** let you see more details about the analysis.

### Long-lived branch analysis <a href="#long-lived-branch-analysis" id="long-lived-branch-analysis"></a>

If you select a branch from the **Long-lived branches** list you will be taken to the **Summary** page for that branch, much like we described above for the **Short-lived branches**:

![](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e00135d96e8800b65051bf7e0d1700236b3151e2%2Faf0f1732e97f9e9da321728bfa78bd259c84d94c.png?alt=media)

As you can see, this page is very similar to the **Main Branch** analysis page. Again, this is because it is based on the same principles:

* At the top of the branches page, the [quality-gates](https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates "mention") shows the "releasability" status of the long-lived branch. It answers the question "Can I release this branch today?"
* There are two tabs: One for **New Code** and one for **Overall Code**, just as in the **Main Branch** view.
* The metrics displayed and the tabs available are identical to those found on the main branch analysis page, except that they apply to this long-lived branch.
* You can download regulatory reports for a long-lived branch by clicking on **Downloadable reports** and selecting **Download Regulatory report (.zip)** from the drop down menu. See [viewing-project-regulatory-reports](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/viewing-project-regulatory-reports "mention") for more details.

See the [main-branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/main-branch-analysis "mention") page for details about working with the **Main Branch**.

### Incremental analysis <a href="#incremental-analysis" id="incremental-analysis"></a>

Some analyzers use the [incremental-analysis-mechanisms](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/incremental-analysis-mechanisms "mention") to shorten the branch analysis.
