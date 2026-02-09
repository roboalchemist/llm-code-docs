# Source: https://docs.sonarsource.com/sonarqube-server/8.9/project-administration/defining-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration/defining-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration/defining-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration/defining-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/project-administration/clean-as-you-code-settings/defining-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/project-administration/clean-as-you-code-settings/defining-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/project-administration/clean-as-you-code-settings/defining-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/project-administration/clean-as-you-code-settings/defining-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/clean-as-you-code-settings/defining-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/clean-as-you-code-settings/defining-new-code.md

# Defining new code

Each SonarQube project has a *new code definition* (NCD), that is, a setting that tells SonarQube which part of the code is considered *new code*. When you run an analysis, SonarQube uses the new code definition to identify new code, then highlights issues in the new code.

This helps you focus attention on the most recent changes to your codebase, helping you follow the [Clean as You Code](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/clean-as-you-code) methodology.

### Setting your new code definition <a href="#setting-your-new-code-definition" id="setting-your-new-code-definition"></a>

You can define new code at the global, project, or branch level.

* **Global level**: Set a global new code definition at **Administration** > **Configuration** > **General Settings** > **New Code**. What you define as new code at the global level will be the default for your projects.
* **Project level**: Set a new code definition for your project at **Project Settings** > **New Code**. What you define as new code at the project level will be the default for the project’s branches if you’re using an edition that supports multiple branches (starting in [Developer Edition](https://www.sonarsource.com/plans-and-pricing/developer/)).
* **Branch level**: You can define new code for each branch from the **Actions** column of the branches table on the project’s **New Code** settings page if you’re using an edition that supports multiple branches (starting in [Developer Edition](https://www.sonarsource.com/plans-and-pricing/developer/)).

Both project and branch-specific new code definitions can be reset to use the default setting (only if the default complies with the Clean as You Code methodology).

### New code definition options <a href="#new-code-definition-options" id="new-code-definition-options"></a>

Setting up the relevant new code definition for your project is an important step in getting the most out of SonarQube. You can choose from the following options:

* **Previous version**: Available at the global, project, and branch levels. Recommended for projects with regular versions or releases. Defines *new code* as any code that has changed since the most recent version increment of the project. The current version of a project is determined in different ways depending on the build system:
  * If the analysis is done using the [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/sonarscanner-for-maven "mention"), then SonarQube reads the version from the `pom.xml` file.
  * If the analysis is done with the [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/sonarscanner-for-gradle "mention") then SonarQube reads the version from the `build.gradle` file.
  * In all other cases, the version must be explicitly specified by setting the analysis parameter `sonar.projectVersion`.
* **Number of days**: Available at the global, project, and branch levels. Recommended for projects following continuous delivery. Defines new code as any code that has changed in the last X days (max 90). For example, setting the Number of Days to 30 creates a new code period beginning 30 days before the current date. If no action is taken on a new issue after 30 days, this issue becomes part of the overall code.

{% hint style="info" %}
Code that is older than 90 days cannot be considered new, and old issues should not be a priority. If this option is set to a higher value than 90 before upgrading to SonarQube 10.2 or later, it is automatically changed to 90. Some issues may move out of the new code as a consequence.
{% endhint %}

* **Specific analysis** (Web API only): Choose a previous analysis as your new code definition. Any changes made since that analysis are considered new code. For more compliance with the Clean as You Code methodology, this option cannot be set in the UI, as it would require frequent user action to be kept up to date. Available:
  * at the branch level in [Developer Edition](https://www.sonarsource.com/plans-and-pricing/developer/) and above
  * at the project level in Community Edition, as the edition doesn’t support multiple branches
* **Reference branch**: Available at the project and branch levels. Recommended for projects using feature branches. Choose a specific branch to define your new code. Any differences between your branch and the reference branch in the clone the scanner has access to at analysis time are considered new code. To avoid reference errors when cloning a repository, we recommend cloning all its branches.

  You can use on the scanner side the `sonar.newCode.referenceBranch` property to apply the Reference branch option to the analysis of a branch, overriding the global new code definition set in the UI (See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/analysis-parameters "mention") page for more information about setting hierarchies). This setting is particularly useful during the first analysis when the branch to be analyzed does not exist yet in SonarQube. The `sonar.newCode.referenceBranch` property specifies the reference branch value.

{% hint style="info" %}
The Reference branch new code definition is useful for short-lived branch analysis before a pull request is created, or for short-lived branch analysis where pull requests are not in use (e.g. trunk-based developments). For the latest, the setting will also allow issues on the reference branch to inherit their status from your short-lived branch after its merge (see [solution-overview](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/issues/solution-overview "mention")).
{% endhint %}

When using any new code period type other than **Reference Branch**, we recommend completing your merges using the *fast-forward* option without a merge commit; examples include GitHub’s *squash and merge* or *rebase and merge* options. In this way, the blame for the merged commits will always have a more recent commit date.

### How the new code definition affects your analysis results <a href="#how-the-new-code-definition-affects-your-analysis-results" id="how-the-new-code-definition-affects-your-analysis-results"></a>

During analysis of the main branch, what counts as a *new code issue* is determined by the following:

1. SonarQube determines how your code is compared:
   * For the *Reference branch* option, the analyzed branch is compared to the current state of the reference branch based on [scm-integration](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scm-integration "mention"). If the SCM is not available, the two branches are compared based on their current state in SonarQube.
   * For the other options, SonarQube uses the *start date of the new code period,* calculated as follows:
     * Previous version: Date when the project was first incremented to the version in question
     * Number of days: Current date minus the specified number of days
     * Specific analysis: Date of the past analysis
2. All lines of code in all files under analysis that are not in the reference branch or have changed since the start date of the new code period are marked (and displayed in yellow in the SonarQube interface).
3. All issues with one or more of the marked lines as primary or secondary locations are categorized as *new code issues*.

{% hint style="info" %}
For analysis of [introduction](https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/pull-request-analysis/introduction "mention"), the new code definition is not used. Instead, the *new code issues* are those introduced by the pull request itself.
{% endhint %}

The set of new code issues, in turn, affects many aspects of your results:

* The default [quality-gates](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/quality-gates "mention") applies conditions only to new code issues.
* New code metrics are separated from overall code metrics in the main branch overview and the overviews of the other branches.
* The **Measures** panel separates new code data vs overall code data.
* Selecting the **Issues in new code** filter found on the *Your Project* > **Issues** page allows you to quickly switch between issues in *new code* or issues in *overall code*.

The activity graphs separate activity in the *new code* from activity in the *overall code*.

### About new code definition and the WEB API <a href="#new-code-definition-web-api" id="new-code-definition-web-api"></a>

While choosing an option, you should take into account your development context. If you’re importing several projects at once (bulk project import) using the [WEB API](https://next.sonarqube.com/sonarqube/web_api/api/alm_integrations), knowing how the NCD options affect your analysis results can be helpful.
