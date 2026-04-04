# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates.md

# Understanding quality gates

A quality gate consists of a set of conditions against which the code is measured during analysis. A condition is defined on either new code or overall code. Depending on the result, the code will pass or fail the quality gate, giving developers indications on whether to fix issues or merge the code.

The quality gate status (**Passed** or **Failed**) appears with analysis results of the main branch, other branches, and pull requests in the respective project’s page as illustrated below.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ef3bfbae8f1d679ac12bfe8a6af754ca610231ee%2Faf768ec73f0e62101745c719efe4f9c243d94143.png?alt=media" alt="SonarQube Cloud&#x27;s Main Branch Summary page tells you immediately if the analysis meets your quality standards.."><figcaption></figcaption></figure>

{% hint style="info" %}

* Any user can subscribe to email notifications on quality gate change for a project or all projects. See [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention").
* For pull requests, the quality gate status will also be displayed in the repository platform as a pull request decoration. It can be used to block the merge of the pull request if the quality gate fails.
* The quality gate status can be reported to your CI pipeline. It can be used to fail your CI pipeline if the quality gate fails.
* If you are using [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention"), changes to your main branch quality gate will also appear as notifications in your IDE (this only works if you have configured SonarQube for IDE to connect to your SonarQube Cloud account).
  {% endhint %}

### Basic principles <a href="#basic-principles" id="basic-principles"></a>

Each project is assigned a quality gate. A default quality gate is defined in your organization and applied to all projects not explicitly assigned to a quality gate.

You may have to use several quality gates depending on your projects:

* The technological implementation differs from one application to another. For example, you might not require the same code coverage on new code for web applications as you would for Java applications.
* You want to ensure stronger requirements on some of your applications, for example, internal frameworks.
* You should use a quality gate qualified for AI Code Assurance if your project contains AI code.

Two built-in quality gates are provided: **Sonar way** which is used by default as the default quality gate, and **Sonar way for AI Code** which is recommended for projects containing AI code. See **Quality gates for AI code** below.

With the Team and Enterprise plans, you can create your own quality gates, called custom quality gates.

To create and update custom quality gates, the Administer Quality Gates permission is required. With this permission, you can also associate projects with quality gates. As a project manager, you can associate your project with a quality gate.

{% hint style="info" %}
Quality gates can be managed in the UI or through the [Web API](https://sonarcloud.io/web_api/api/qualitygates?query=qualitygates\&deprecated=false).
{% endhint %}

### Quality gate definition based on conditions <a href="#definition-based-on-conditions" id="definition-based-on-conditions"></a>

A quality gate is defined through a set of conditions on metrics calculated during the analysis. Each condition applies to a given metric applying either to new code or overall code. If one of the conditions is met, the quality gate fails. See [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") for more information.

{% hint style="info" %}
In case of a pull request analysis, only the quality gate conditions applying to new code are used.
{% endhint %}

Metrics you can use include:

* Statistics and ratings on detected security, maintainability, and reliability issues.
* Statistics on test coverage.
* Code cyclomatic and cognitive complexities.
* Statistics and ratings on reviewed security hotspots.
* Statistics on duplicated lines and blocks.
* Statistics on code size (the number of various code elements).
* Global statistics on issues.

Each quality gate condition is a combination of:

* A metric
* A comparison operator
* An error value

For instance, a condition might be

* Metric: Blocker issue
* Comparison operator: >
* Error value: 0

Which can be stated as: No blocker issues.

For more information on the metrics, see [metric-definitions](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions "mention").

### Sonar way, the recommended quality gate <a href="#sonar-way-recommended-quality-gate" id="sonar-way-recommended-quality-gate"></a>

The **Sonar way** quality gate is Sonar’s recommended quality gate for your new code, helping you achieve high quality code. It is provided by Sonar, activated by default, and read-only.

This quality gate focuses on keeping high quality standards for new code, rather than spending a lot of effort remediating old code.

The Sonar way quality gate has four conditions:

* No new bugs are introduced (Reliability rating is A).
* No new vulnerabilities are introduced (Security rating is A).
* New code has limited technical debt (Maintainability rating is A).
* All new Security Hotspots are reviewed.
* New code test coverage is greater than or equal to 80.0%.
* Duplication in the new code is less than or equal to 3.0%.

### Quality gates for AI code <a href="#quality-gates-for-ai-code" id="quality-gates-for-ai-code"></a>

Sonar recognizes that AI-generated code requires additional quality standards, and we’ve created a series of tools to bring AI Code Assurance to your projects. One of these tools includes the [#use-the-sonar-way-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/ai-code-assurance/quality-gates-for-ai-code#use-the-sonar-way-for-ai-code "mention") quality gate and the option to create your own custom quality gates, specifically qualified for AI code.

For more information about using all of the Sonar tools for AI Code Assurance, see the [overview](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview "mention") page.

### Quality gate computation <a href="#quality-gate-computation" id="quality-gate-computation"></a>

Within a specific project, the same quality gate definition is always used for all quality gate status computations. However, the way that the calculations are done differs somewhat between the branches and pull requests. In addition, a fudge factor is used by default during quality gate calculation. In some cases, the quality gate cannot be computed.

#### Computation for the main branch and long-lived branches <a href="#computation-for-the-main-branch-and-longlived-branches" id="computation-for-the-main-branch-and-longlived-branches"></a>

* Both the conditions defined on *overall code* and conditions defined on *new code* are applied.
* What counts as *new code* is determined by the prevailing new code definition setting for the branch, as described on the [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") page.

#### Computation for short-lived branches and pull requests <a href="#computation-for-shortlived-branches-and-pull-requests" id="computation-for-shortlived-branches-and-pull-requests"></a>

* Only conditions defined on *new code* are applied.
* And, *new code* is defined as whatever has changed relative to the target branch, as described on the [branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis "mention") and [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention") pages.

#### Quality gate fudge factor <a href="#quality-gate-fudge-factor" id="quality-gate-fudge-factor"></a>

The quality gate fudge factor refers to a mechanism where conditions on duplication and coverage are ignored until the number of new lines is at least 20. This is used to avoid overly strict enforcement when dealing with small changes, as minor issues might disproportionately impact the overall quality gate status.

The fudge factor is enabled by default in your organization. This organization’s setting is applied to all new projects. Project administrators can override it for their project.

#### Not computed status <a href="#not-computed-status" id="not-computed-status"></a>

There are two main reasons why the quality gate may not be computed:

* You have performed only one analysis on your code (the quality gate is computed after the second analysis).
* No new code definition is set up for the project.\
  This may only occur for projects created a long time ago since in the current version of SonarQube Server you cannot create a new project without setting up the new code definition.

If the quality gate has not been computed then the **Not computed** message is displayed in the place where the quality gate status usually appears as illustrated below.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e6278f5731d367bcc10206df16751b6251a5163c%2F700624709bc9524ba843caa9797629feabc37b3c.png?alt=media" alt="You will see this banner when the SonarQube Cloud quality gate has not been computed." width="563"><figcaption></figcaption></figure></div>

The **Set New Code Definition** button is displayed as well in case no new code definition is set up. To fix this, click the button. For more details on setting up the definition, see the [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") page.

### Quality gate and new code <a href="#quality-gate-and-new-code" id="quality-gate-and-new-code"></a>

To ensure that developers are not introducing issues in their code, all built-in quality gates are configured to prevent introducing issues in new code.

**No new issues are introduced**

This is implemented through the following failing condition(s) *on new code*:

* Either:
  * The Number of issues is higher than 0.
* Or:
  * Reliability Rating is worse than A.
  * Security Rating is worse than A.
  * Maintainability Rating is worse than A.

Note that while the three rating conditions help improve the quality of new code, they still allow some technical debt to sneak into your codebase. Instead, using the 0 issues condition will ensure that your new code is completely free from any issues.

**All new security hotspots have been reviewed**

This is implemented through the following failing condition *on new code*:

* Security Hotspots Reviewed is less than 100%.

**New code has sufficient test coverage**

This is implemented through the following failing condition *on new code*:

* Coverage is less than X%, where X is configurable.

**New code has limited duplications**

This is implemented through the following failing condition *on new code*:

* The duplicated lines density is greater than X%, where X is configurable.

For information on the metrics, see the [metric-definitions](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions "mention") page.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [viewing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/viewing-quality-gate "mention")
* [managing-custom-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/managing-custom-quality-gates "mention")
* [changing-default-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/changing-default-quality-gate "mention")
* [quality-standards](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/quality-standards "mention")
* [associating-projects-with-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/associating-projects-with-quality-gate "mention")
* [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention")
* [quality-gates-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gates-for-ai-code "mention")
* [changing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate "mention")

**DevOps platform integration features:**

* [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/introduction "mention") to the integration of your project with your DevOps platform
* Failing your CI pipeline on quality gate failure:
  * [pipeline-pause](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/pipeline-pause "mention") in Jenkins
  * [github-actions-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/github-actions-for-sonarcloud "mention")
  * [bitbucket-pipelines-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/bitbucket-pipelines-for-sonarcloud "mention")
  * [gitlab-ci](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/gitlab-ci "mention")
