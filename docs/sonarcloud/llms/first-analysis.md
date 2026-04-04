# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started/first-analysis.md

# Viewing your first analysis' results

If you have successfully followed the in-product tutorial, SonarQube Cloud will run its first analysis on your project.

The first analysis is always a *main branch analysis,* an analysis of the default branch of your repository.

From now on, a new analysis will be triggered every time you make a change to the main branch by direct push, pull request merge, or branch merge.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-2842bf2d399bb8db495ab341947105ad07b3faa5%2F0990580234f9925176b53952bb2ef3ecc234b5d2.png?alt=media" alt="Your first analysis in SonarQube Cloud."><figcaption></figcaption></figure></div>

### Main Branch Status <a href="#main-branch-status" id="main-branch-status"></a>

The **Main Branch Status** is the quality gate of your main branch, indicating whether it meets your quality requirements and is ready to be released.

{% hint style="info" %}
**The quality gate displays Not Computed because it needs to be configured.**

We strongly recommend that you set up your main branch quality gate. To do so, you must set a *new code definition*. Select **Set New Code Definition** to get started.

See the [quality-gates](https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates "mention") and [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") pagesfor more details. Once you set it up, push a change to the main branch. A new analysis will run, and the quality gate status will display either **Passed** or **Failed**.
{% endhint %}

### Main Branch Evolution <a href="#main-branch-evolution" id="main-branch-evolution"></a>

The **Main Branch Evolution** displays a summary of the code quality results from the main branch analysis. In this section, you will find tabs that display different metrics:

* **Issues** displays the number of issues found in the main branch.
* **Coverage** displays the percentage of testable code in the main branch that is covered by your test cases.
* **Duplications** displays the percentage of main branch code that is duplicated.

{% hint style="info" %}
**Coverage displays zero percent because it needs to be configured.**

Initially, your coverage will display zero percent because it requires configuration. To set it up, see the [overview](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/overview "mention") section.

Once it’s configured, push a change to the main branch to update the analysis. After the a new analysis is run, the coverage percentage will be displayed.
{% endhint %}

The **historical data** chart shows the progress of your code quality.

{% hint style="info" %}
**To see historical data, you must have run at least two analyses.**

Push a change to your main branch. A new analysis will run, and the historical data will be displayed. In the **Main Branch Evolution** section, select **See full history** to the project’s **Activity** page.
{% endhint %}

### Latest Activity <a href="#latest-activity" id="latest-activity"></a>

Scroll down to find the **Latest Activity** section; it displays a feed of all analyses that have been run, including all main branch analyses, pull request analyses, and branch analyses.

### Project navigation <a href="#project-navigation" id="project-navigation"></a>

The project navigation on the left lets you move between the four views: **Overview**, **Main Branch**, **Pull Requests**, and **Branches**.

![](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-82dcdf298eff5994140d75214be39406ab84cc93%2F09573323c42558c17db79982004e34ad0b8cdbed.png?alt=media)

### Main Branch <a href="#main-branch" id="main-branch"></a>

Select **Branches** > **MAIN BRANCH** to see a more fine-grained view of your most recent [main-branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/main-branch-analysis "mention")

### Pull Requests <a href="#pull-requests" id="pull-requests"></a>

In addition to analyzing your main branch every time it changes, SonarQube Cloud also analyzes individual pull requests. These analyses run when a pull request is opened and on each change to the pull request branch. This all happens *before* you merge, letting you catch problems before they even get to the main branch. The results of pull request analysis are displayed in the **Pull Requests** view of your SonarQube Cloud project and the pull request view of your DevOps Platform (GitHub, Bitbucket Cloud, Azure DevOps, or GitLab).

See the [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention") page for more details.

### Branches <a href="#branches" id="branches"></a>

The **Branches** view displays all the non-pull request branches for which you have set up analysis. Initially, only the main branch is listed here. But, you can configure other branches to be analyzed. Once a branch is configured, an analysis is run on every change to that branch.

See [branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis "mention") and [branch-analysis-setup](https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis-setup "mention").
