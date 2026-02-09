# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis.md

# Automatic analysis

When you first import a project that is compatible with automatic analysis, the initial analysis behaves differently from subsequent analyses. During this first analysis, not only is the default branch (typically *main* branch) analyzed, but also the five most recently active pull requests. Subsequently, automatic analysis will trigger a new analysis on each push to the default branch and on each push to any pull request branch.

### Considerations <a href="#considerations" id="considerations"></a>

Currently, automatic analysis has the following limitations:

* It is only available for GitHub repositories.
* [branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis "mention") (analysis of non-pull request branches other than *main* branch) is not supported.
* Automatic analysis does not support monorepos (the *monorepo* strategy). See the [monorepo-support](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/monorepo-support "mention") page for more details.
* Code coverage information is not supported.
* Import of external rule engine reports is not supported.
* SCA in SonarQube Advanced Security is not supported.
* Automatic analysis logs are not available.

If you experience prolonged analysis times or need to review the analysis logs, consider onboarding your project using a CI-based analysis. See the [overview-of-integrated-cis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/overview-of-integrated-cis "mention") page for more information.

{% hint style="warning" %}
**Analyzing Gradle files**

If you are analyzing Gradle files, your Gradle build file must be located in the root of your repository in order to be detected by the scanner because SonarScanner checks for the presence of a \`pom.xml\`, \`build.gradle\`, or \`build.gradle.kts\` file.

If your Gradle build file is located in sub-directory, you have to use CI-based analysis instead. For more information, see [Analyzing multi-project builds](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports).
{% endhint %}

### Supported languages <a href="#supported-languages" id="supported-languages"></a>

Automatic analysis is available for nearly all of SonarQube Cloud's [overview](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/overview "mention"). However, the Objective-C, Dart, and Rust languages are not eligible for automatic analysis at this time.

For Java, there are some known limitations. See the dedicated sections below for the details.

{% hint style="info" %}
Automatic analysis now also supports Azure Resource Manager and its two formats, JSON and Bicep.
{% endhint %}

### Activating automatic analysis <a href="#activating-automatic-analysis" id="activating-automatic-analysis"></a>

For new projects:

* After importing a project from GitHub, SonarQube Cloud will automatically check whether your project is eligible for automatic analysis. This should take a few seconds.
  * SonarQube Cloud will deem a project *eligible* for automatic analysis only if *at least 20%* of the lines of code in the project are in a *supported language*.
  * For a Java project to be eligible, the amount of Java code cannot exceed 10MB.
* If your project is eligible, SonarQube Cloud will automatically trigger the first analysis. On this first analysis, the system will analyze the default branch of the project and the five most recently active pull requests. All you have to do is wait for the analysis to finish.
* If your project is not compatible, SonarQube Cloud will suggest other analysis methods such as using a CI tool.
* You can force automatic analysis on an initially non-eligible project. *However, doing this is not recommended as it will typically not provide useful information*. To force automatic analysis, do one of the following:
  * From your project’s homepage, click the *Force Automatic Analysis* button.
  * From your project’s **Administration** > **Analysis Method** page, turn on **Automatic Analysis**.

For existing projects:

* Go to your project’s **Administration** > **Analysis Method** page and turn on **Automatic Analysis**.
* The **Analysis Method** page will display a compatibility check, so you are aware of our recommendations for your specific project.

### Presence of a properties file <a href="#presence-of-a-properties-file" id="presence-of-a-properties-file"></a>

If you import a project that already contains a `sonar-project.properties` file, SonarQube Cloud will ignore the parameters in your `sonar-project.properties` file. To analyze your code with the settings defined in this file, you can disable Autoscan and configure a CI/CD analysis. See the [#deactivating-automatic-analysis](#deactivating-automatic-analysis "mention") article for instructions.

### Analysis method indicator <a href="#analysis-method-indicator" id="analysis-method-indicator"></a>

If a project uses automatic analysis, then in the project **Overview** > **Information** under **Last analysis method** the system will display *Analyzed by SonarQube Cloud*:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ab92a049f2f454d686243288f7529b56133dad42%2Fa9efe404873838f85e7f0817585ebe7a1f62514b.png?alt=media" alt="The last analysis method is clearly shown on your project&#x27;s Information page."><figcaption></figcaption></figure></div>

### Conflict with CI-based analysis <a href="#conflict-with-ci-based-analysis" id="conflict-with-ci-based-analysis"></a>

Automatic analysis is not intended to be used in conjunction with CI-based analysis.

If you enable automatic analysis, you must ensure that you do not have any CI-based analyses configured. If you do then these CI-based analyses will fail and *cause a failure in your build process*.

Similarly, if you wish to use a CI-based analysis on a project, you must ensure that automatic analysis is disabled for that project.

This is done to prevent duplicate analyses from being sent to SonarQube Cloud that would cause problems in your project activity reports.

### Deactivating automatic analysis <a href="#deactivating-automatic-analysis" id="deactivating-automatic-analysis"></a>

Go to your project’s **Administration** > **Analysis Method** page and unselect **Enabled for this project**.

From the same page, you can then follow one of our tutorials for configuring SonarQube Cloud analyses with another method.

{% hint style="info" %}
As an organization admin, you can disable automatic analyses in your Enterprise plan organization. See the [disabling-automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/disabling-automatic-analysis "mention") page for details.
{% endhint %}

### Additional analysis configuration <a href="#additional-analysis-configuration" id="additional-analysis-configuration"></a>

You can refine the configuration of your analyses by adding a `.sonarcloud.properties` file to your repository’s default branch. *Note that this is different from the `sonar-project.properties` file used for CI-based analysis*.

Below are the supported optional settings for the `.sonarcloud.properties` file. Wildcard patterns are not allowed. Read more on the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page.

```properties
# Path to sources
# sonar.sources=
# sonar.exclusions=
# sonar.inclusions=

# Path to tests
# sonar.tests=
# sonar.test.exclusions=
# sonar.test.inclusions=

# Source encoding
# sonar.sourceEncoding=

# Exclusions for copy-paste detection
# sonar.cpd.exclusions=

# Python version (for python projects only)
# sonar.python.version=

# C++ standard version (for C++ projects only)
# If not specified, it defaults to the latest supported standard
# sonar.cfamily.reportingCppStandardOverride=c++98|c++11|c++14|c++17|c++20
```

Not all properties work with all scanner versions. Be sure to review the [#analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/analysis-parameters#analysis-scope "mention") and check which are available for your scanner and scanner version.

Some of these settings can also be configured from the SonarQube Cloud UI. In your project’s **Administration** > **General Settings** > **Analysis Scope** > **Files** section, you can define source and test file exclusions and inclusions. If you have different options set in the UI than are defined in your `.sonarcloud.properties` file, SonarQube Cloud will only take into account the value from the `.sonarcloud.properties` file.

{% hint style="info" %}

* This feature works for any project, public or private.
* It can be activated at no extra cost.
* If you were previously using the *Automatic Analysis Beta*, removing the `.sonarcloud.properties` file will no longer disable automatic analysis. It will only disable the additional configuration settings you might have defined in it. You will still have to disable automatic analysis from the SonarQube Cloud UI, in the **Administration** > **Analysis Method** page.
  {% endhint %}

### Automatic analysis for Java, Kotlin, and Scala <a href="#automatic-analysis-for-java-projects" id="automatic-analysis-for-java-projects"></a>

Automatic analysis provides the quickest way to get your Java, Kotlin, and Scala projects up and running on SonarQube Cloud and see code analysis results fast.&#x20;

To be eligible for automatic analysis, your Java project must:

* Use either Maven or Gradle
* Have less than 10MB in total amount of code

Automatic analysis for Java has the following limitations:

* XSS (Cross-Site Scripting) issues can’t be detected: to get the full power of Sonar analyzers, it’s required to switch to CI-based analysis.
* For Gradle-based projects, there are less security issues detected: to get the full power of Sonar analyzers, it’s required to switch to CI-based analysis.
* Rules that belong to [this list](https://github.com/SonarSource/sonar-java/blob/3c8b11346c6cc84e3bc936a2b1a5487dd1c0ee1e/check-list/src/main/java/org/sonar/java/CheckListGenerator.java#L177C64-L177C100) are not supported because the results that they currently produce are not accurate enough (see the line with `JAVA_CHECKS_NOT_WORKING_FOR_AUTOSCAN`)
* Not all properties are supported (see below).

{% hint style="warning" %}
Java automatic analysis does not support the following properties:

* sonar.sources
* sonar.tests
* sonar.inclusions
* sonar.test.inclusions

This is because we assume that your files will follow the standard directory layout that is expected by Maven and Gradle (`**/src/main/**/*` and `**/src/test/**/*`) for Java projects.
{% endhint %}

With these limitations in mind, the next step in your Java project onboarding is to set up CI-based analysis to get the most out of SonarQube Cloud analysis. See the [overview-of-integrated-cis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/overview-of-integrated-cis "mention") page for more information.

### Automatic analysis for .NET projects <a href="#automatic-analysis-for-net-projects" id="automatic-analysis-for-net-projects"></a>

SonarQube Cloud automatic analysis now also supports .NET projects. .NET Framework, .NET Core, .NET 5 and .NET 6 projects can be analyzed but are subject to some limitations:

* Projects must contain at least 20% code in a supported language. The amount of .NET code for automatic analysis is calculated by adding the sum of \*.cs and \*.vb files together.
* Projects must contain at least one XML file - \*.csproj or \*.vbproj. A combination of both file types is acceptable.

With these limitations in mind, the next step in your .NET project onboarding is to set up CI-based analysis to get the most out of SonarQube Cloud analysis. See the [overview-of-integrated-cis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/overview-of-integrated-cis "mention") page for more information.

### Automatic analysis for C and C++ projects <a href="#automatic-analysis-for-c-and-c-projects" id="automatic-analysis-for-c-and-c-projects"></a>

There are no additional requirements for [C and C++ projects](https://www.sonarsource.com/products/sonarcloud/features/auto-analysis-for-c-and-cpp/), apart from the standard [#considerations](#considerations "mention") for automatic analysis.

* C & C++ automatic analysis does not have any toolchain or project structural requirements.
* C & C++ can be analyzed in combination with all other supported languages (including Java and .NET.)

SonarQube Cloud automatic analysis for C and C++ is already available and ready to analyze. The quality of analysis is very similar to a CI-based analysis and, for most users, it is the only analysis you really need.

For other users, there are a few cases where a CI-based analysis remains a better option.

* If your project is so big that the analysis cannot be completed before the analysis times out, automatic analysis will fail.
* If you require faster analysis. You should run the analysis using self-hosted resources with an increased hardware capacity. It would also allow you to keep full control of the analysis cache if needed.
* If your project uses generated code that you want to analyze. For example, this can happen in some custom build systems.
* If you need control over the configuration of your code. For example, with automatic analysis, you cannot analyze a specific build variant. Automatic analysis uses a configuration that maximizes the amount of code analyzed and the OS and architecture used for this can differ from your own configuration.
* If your project is experiencing missing issues. In rare cases, automatic analysis can lead to such limitations.

See [overview-of-integrated-cis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/overview-of-integrated-cis "mention") page for more information.
