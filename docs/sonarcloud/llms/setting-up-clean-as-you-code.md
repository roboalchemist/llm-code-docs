# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/setting-up-clean-as-you-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/setting-up-clean-as-you-code.md

# Setting up Clean as You Code

As a project administrator, you set up Clean as You Code in three steps:

1. You set the quality standard for your project.
2. You set a new code definition.
3. You set up pull request and branch analysis.

### Setting your quality standard <a href="#setting-your-quality-standard" id="setting-your-quality-standard"></a>

We recommend using the default Sonar way quality profile and quality gate. For details and configuration options, see the [quality-profiles](https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/quality-profiles "mention") and [quality-gates](https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/quality-gates "mention") pages.

### Setting a new code definition <a href="#setting-a-new-code-definition" id="setting-a-new-code-definition"></a>

This section describes how to set up a new code definition for your project. To learn about new code, see [about-new-code](https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-as-you-code/about-new-code "mention").

For each project you create in SonarQube Server, you need to choose a new code definition.

#### Configuration levels <a href="#configuration-levels" id="configuration-levels"></a>

You can define new code at the global, project, or branch level:

* Global level: Set a global new code definition at **Administration** > **Configuration** > **General Settings** > **New Code**. What you define as new code at the global level will be the default for your projects.
* Project level: Set a new code definition for your project at **Project Settings** > **New Code.** If you’re using an edition that supports multiple branches (starting in [Developer Edition](https://www.sonarsource.com/plans-and-pricing/developer/)), what you define as new code at the project level will be the default for the project’s branches.
* Branch level: If you’re using an edition that supports multiple branches (starting in [Developer Edition](https://www.sonarsource.com/plans-and-pricing/developer/)) You can define new code for each branch:
  1. Go to *your project* > **Settings** > **New Code**.
  2. In the branches table, define your new code option in the Actions column.

Both project and branch-specific new code definitions can be reset to use the default setting (only if the default setting is configured to follow the Clean as You Code methodology).

#### Option-specific details <a href="#optionspecific-details" id="optionspecific-details"></a>

**Previous version**

Recommended for projects with regular versions or releases. Defines new code as any code that has changed since the most recent version increment of the project.

Available at the global, project, and branch levels.

The current version of a project is determined in different ways depending on the build system:

* If the analysis is done using the [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner-for-maven "mention"), then SonarQube Server reads the version from the `pom.xml` file.
* If the analysis is done with the [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner-for-gradle "mention") then SonarQube Server reads the version from the `build.gradle` file.
* In all other cases, the version must be explicitly specified by setting the analysis parameter `sonar.projectVersion`.

**Number of days**

Recommended for projects following continuous delivery. Available at the global, project, and branch levels. Defines new code as any code that has changed in the last X days.

For example, setting the Number of days to 30 creates a new code period beginning 30 days before the current date. If no action is taken on a new code issue after 30 days, this issue becomes part of the overall code.

The default value is 30 days, 7 or 14 days are other common values. The maximum possible value is 90 days.

**Specific analysis**

Available at the branch (Developer edition and above) and project levels. Defines new code as any changes made since that specific analysis.

To comply with the Clean as You Code methodology, this option cannot be set in the UI, as it would require frequent user action to keep it up to date. It can only be set via the Web API using the `api/new_code_periods`endpoint, with analysis `uuid`, `project` and `branch` keys as parameters.

**Reference branch**

Recommended for projects using feature branches. Available at the project and branch levels. Any differences between your branch and a selected reference branch (in the clone the scanner has access to at analysis time) are considered new code.

On the scanner side, it’s possible to use the `sonar.newCode.referenceBranch` property to apply the Reference branch option to the analysis of a branch, overriding the global new code definition set in the UI (see the [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/analysis-parameters "mention") page for more information about setting hierarchies).

This setting is particularly useful during the first analysis when the branch to be analyzed does not exist yet in SonarQube Server. The `sonar.newCode.referenceBranch` property specifies the reference branch value.

**Recommendations**

* To avoid reference errors when cloning a repository, we recommend cloning all its branches.
* The Reference branch new code definition is useful for short-lived branch analysis before a pull request is created, or for short-lived branch analysis where pull requests are not in use (e.g. trunk-based developments). For the latest, the setting will also allow issues on the reference branch to inherit their status from your short-lived branch after its merge (see [solution-overview](https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/issues/solution-overview "mention")).
* When using any new code period type other than Reference Branch, we recommend completing your merges using the fast-forward option without a merge commit; examples include GitHub’s squash and merge or rebase and merge options. In this way, the blame for the merged commits will always have a more recent commit date.

While choosing an option, you should take into account your development context. If you’re importing several projects at once (bulk project import) using the [web-api](https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/web-api "mention"), it’s important to know about the new code definition options and how they affect your analysis results.

### Setting up the analysis <a href="#setting-up-the-analysis" id="setting-up-the-analysis"></a>

To learn how to set up analysis in your IDE and with SonarQube Server, refer to the following links:

* SonarQube for [Intellij](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/NvI4wotPmITyM0mnsmtp/ "mention"), [Visual Studio](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/5CSDwdOaYoOAGYNiRqgl/ "mention"), [VS Code](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/6LPRABg3ubAJhpfR5K0Y/ "mention"), [Eclipse](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/kadXEH8HkykK7lKaDvVq/ "mention")
* [setting-up-the-branch-analysis](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis "mention")
* [setting-up-the-pull-request-analysis](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis "mention")

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction](https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-as-you-code/introduction "mention")
* [implementation](https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-as-you-code/implementation "mention")
