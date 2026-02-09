# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/core-concepts/clean-as-you-code/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-as-you-code/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code.md

# Quality standards and new code

SonarQube Cloud warns you whenever issues are detected in your new code. When you add new code to your projects, you usually touch a portion of the old code in the process. As a consequence, analyzing and cleaning new code allows you to fix issues in your old code and gradually improve the overall quality of your codebase.

### Defining a quality standard <a href="#defining-quality-standard" id="defining-quality-standard"></a>

First, you define the code quality standard for your project:

* With a quality profile, you define the set of rules to be applied during analysis. We recommend using the built-in quality profile, called Sonar way. See [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention").
* With a quality gate, you define a set of conditions that the code must meet. By default, SonarQube implements a recommended quality gate called the Sonar way. See [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention").

Then, you define what is considered new code in your project, adapting your configuration to the nature of your project: versioned, continuous delivery, etc.

Finally, you ensure your code is analyzed frequently and at different stages of its journey, in your IDE and your DevOps platforms. See *SonarQube for IDE* documentation.

### Focus on new code <a href="#focus-on-new-code" id="focus-on-new-code"></a>

New code is code that you’ve recently added or modified. Different options can be used to define new code on a branch, project, or at global level. The new code definition tells SonarQube which part of the code is considered new during analysis.

SonarQube Cloud differentiates the analysis results on new code from overall code (overall code includes new and old code). To ensure you focus your efforts on new code, SonarQube highlights the status of new code in the UI.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-0da0fc2e879ea51fac51b60ae40d15117e40d0d3%2F8553157cb3de0bd0123a41573cb77b49064baea8.png?alt=media" alt="Your project overview page in SonarQube Cloud provides an overview of issues found in New Code or in your Overall Code." width="563"><figcaption></figcaption></figure></div>

Likewise, the built-in [quality-gates](https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates "mention") Sonar Way defines conditions applying to new code only.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-645975c2d0c3b901622985000b6bf5c57b51b195%2F3f16cd2d9e69c597431cbcbea2bf8d96e917018e.png?alt=media" alt="When defining your quality gate in SonarQube Cloud, you can apply different conditions to new code and overall code." width="563"><figcaption></figcaption></figure></div>

### New code definitions <a href="#new-code-definitions" id="new-code-definitions"></a>

SonarQube Cloud supports the following options for new code definition: Previous version, Number of days, Specific version, and Specific date.

SonarQube Cloud calculates a new code period *with a start and end date*. All the code that falls between the date of your last analysis and the start date is considered new code. The way the start date is calculated depends on the applying new code definition option (for information about the issue date calculation, see the [solution-overview](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/solution-overview "mention") overview page).

#### Previous version <a href="#previous-version" id="previous-version"></a>

Any code that has changed since the most recent version increment of the project is considered new code.

With this option, the new code period’s start date is the date of the first analysis performed for the current project version.

#### Number of days <a href="#number-of-days" id="number-of-days"></a>

Any code that has changed in the last X days is considered new code.

With this option, the new code period’s start date is the current date minus X days.

For example, setting the Number of days to 30 creates a new code period beginning 30 days before the current date. If no action is taken on a new code issue after 30 days, this issue becomes part of the overall code. The default value is 30 days, 7 or 14 days are other common values. The maximum possible value is 90 days.

#### Specific version <a href="#specific-version" id="specific-version"></a>

{% hint style="info" %}
Specific version can only be configured as the new code definition via the [web-api](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api "mention").
{% endhint %}

Any code that has changed since a specific, defined version of the project is considered new code.

With this option, the new code period’s start date is the date of the first analysis performed for the specific project version.

This option gives you more control over your new code than the **Number of days** option. For example, for a project that follows a continuous delivery model, it allows you to mark the start of a new cycle, where a number of days would not be accurate enough.

#### Specific date <a href="#specific-date" id="specific-date"></a>

{% hint style="info" %}
Specific date can only be configured as the new code definition via the [web-api](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api "mention").
{% endhint %}

Any code that has changed since a specific, defined date is considered new code.

With this option, the new code period’s start date is the specific date.

### Recommended option depending on project type <a href="#recommended-option-depending-on-project-type" id="recommended-option-depending-on-project-type"></a>

Depending on the type of project you’re working on, the best option to use will vary. Here are general use cases for various types of projects:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-5d739f2c2f7a7165710298c04542f4515dc9c187%2Fece7c158cf0fce483170d2c030b01cb51283d966.png?alt=media" alt="Use cases for new code definition option in SonarQube." width="375"><figcaption></figcaption></figure></div>

### Configuration levels <a href="#configuration-levels" id="configuration-levels"></a>

The new code definition can be set at the organization and project levels with the following restriction:

* ​Only the Previous version and Number of days options can be set at the organization level.

The following applies:

* The new code option defined at the organization level (if any) is applied by default to all *new* projects.
* The project-level definition has precedence over the organization-level definition.
* By default, no organization-level new code definition is set.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-41f00e111e24c27b82a465df8c793ab21af25e80%2F68364d81c977ca1173363bccac813bd05bc16fd0.png?alt=media" alt="When setting your new code period, Organization-level definitions have priority over Project-level definitions."><figcaption></figcaption></figure></div>

### Focus on new code in the IDE <a href="#new-code-in-the-ide" id="new-code-in-the-ide"></a>

Focusing on new code can be a helpful strategy to avoid introducing new issues into your code base. SonarQube for IDE allows you to focus on *new code* by filtering issues shown in the IDE, as determined by your new code definition.

The **Focus on new code** feature highlights only new code and works when SonarQube for IDE is running in either [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention") or standalone mode and must be enabled manually. Please see these instructions according to the IDE you’re using:

* See [Investigating issues #Focusing on new code](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/using/investigating-issues#focusing-on-new-code "mention") in SonarQube for VS Code
* See [Investigating issues #Focusing on new code](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/using/investigating-issues#focusing-on-new-code "mention") in SonarQube for IntelliJ
* See [Investigating issues #Focusing on new code](https://app.gitbook.com/s/kadXEH8HkykK7lKaDvVq/using/investigating-issues#focusing-on-new-code "mention") in SonarQube for Eclipse

### Three stages of SonarQube code review and analysis <a href="#three-stages-code-review-analysis" id="three-stages-code-review-analysis"></a>

1. The first base layer is code analysis in your SonarQube for IDE. This allows issues to be fixed as soon as they are introduced.
2. The pull request analysis layer ensures that all code to be merged is clean.
3. The branch analysis layer guarantees that the main branch or another branch is ready for release or deployment.

Each layer has advantages in terms of speed and depth of analysis. We recommend implementing all three for the most comprehensive experience.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-new-code-definition-at-organization-level](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/setting-new-code-definition-at-organization-level "mention")
* [configuring-new-code-calculation](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/configuring-new-code-calculation "mention")
