# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/setting-analysis-scope/setting-initial-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/setting-analysis-scope/setting-initial-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/setting-analysis-scope/setting-initial-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/setting-analysis-scope/setting-initial-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/setting-analysis-scope/setting-initial-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/setting-analysis-scope/setting-initial-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/setting-initial-scope.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/setting-initial-scope.md

# Setting initial scope

The initial analysis scope of a project must be defined for source code (also called main code) on one side and for test code on the other side.

{% hint style="info" %}

* Test and source code are distinguished because test files must be excluded from the source-related metrics and different analysis rules are applied to each category.
* Additionally, test code does not count toward your lines of code (LOC) usage in SonarQube accounts and does not count toward coverage (you don’t have to test your test code).
  {% endhint %}

The initial analysis scope of a project is controlled by the following sonar properties:

* For source code (non-test code): `sonar.sources`
* For test code (test code): `sonar.tests`

which define that:

* Files outside the initial scope will not be analyzed at all.
* Files within the initial scope will be analyzed unless excluded by further adjustments.

Each project’s initial scope is defined by default. If it doesn’t suit you, you can set it explicitly.

### Default initial scope <a href="#default-initial-scope" id="default-initial-scope"></a>

{% tabs %}
{% tab title="MAVEN" %}
If you are analyzing code using the SonarScanner for Maven, the `sonar.sources` and `sonar.tests` parameters are automatically determined based on information in your project configuration. You do not have to explicitly set the parameters.

If you do explicitly set the parameters, for example in your *pom.xml* file, they will override the automatically determined values.

See [#analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven#analysis-scope "mention") for more details.
{% endtab %}

{% tab title="GRADLE" %}
If you are analyzing code using the SonarScanner for Gradle, the `sonar.sources` and `sonar.tests` parameters are automatically determined based on information in your project configuration. You do not have to explicitly set the parameters.

If you do explicitly set the parameters, for example in your *gradle.properties* file, they will override the automatically determined values.

See [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention") for details about customizing your analysis.
{% endtab %}

{% tab title=".NET" %}
The `sonar.sources` and `sonar.tests` parameters are not compatible with the SonarScanner for .NET. They are automatically detected and cannot be changed.

If you are analyzing code using the SonarScanner for .NET v8.0.1 or earlier, the `sonar.sources` and `sonar.tests` parameters are automatically determined based on information in your project configuration. The SonarScanner for .NET does not support user-defined values for `sonar.sources` and `sonar.tests`.

See [configuring](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/configuring "mention") for details about customizing your analysis.
{% endtab %}

{% tab title="OTHER SCENARIOS" %}
In cases other than Maven, Gradle or .NET (including both CI-based analysis and automatic analysis):

* By default, `sonar.sources` is set to the value of `sonar.projectBaseDir` property, which is, by default, the current working directory (i.e.: the path `.`).
* `sonar.tests` defaults to `null`, meaning there is assumed to be no test code.
  {% endtab %}
  {% endtabs %}

### Setting the initial scope explicitely <a href="#setting-initial-scope-explicitely" id="setting-initial-scope-explicitely"></a>

If the default initial scope is not suitable (see example below), you must set the initial scope explicitly.

<details>

<summary>Example where an explicit setting of the initial scope is necessary</summary>

We consider the following repository example where the `src` and `test` directories are clearly separated.

<div align="center"><figure><img src="broken-reference" alt="When you define the directories containing all source code, and define a separate directory for all of your test code, setting up the analysis scope is clear and straight-forward." width="563"><figcaption></figcaption></figure></div>

If the SonarScanner CLI is used, the corresponding code below can be used in the `sonar-project.properties` file to change the default initial scope (for an integrated scanner, the configuration can be done in the build’s project definition file).

```css-79elbk
# Define separate root directories for main and test sources
sonar.sources = src
sonar.tests = test
```

</details>

The parameters `sonar.sources` and `sonar.tests` are only settable by key on the CI/CD host (mainly in configuration files or on the command line), not in the SonarQube Cloud UI. For more information, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").

To set `sonar.sources` and `sonar.tests`:

* Use a comma-delimited list of directories or files.
* The entries in the list are simple paths. Wildcard patterns are not allowed.
* A directory in the list means that all analyzable files and directories recursively below it are included. An individual file in the list means that the file is included.
* The paths are interpreted relative to the project base directory which is defined through the `sonar.projectBaseDir` property. In most cases, this is the root directory of the project. For more information about this property, see [#analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters#analysis-scope "mention") for more details.

{% hint style="warning" %}
The C/C++/Objective-C analyzer doesn’t currently support `sonar.tests`. See **Analyzing test files** in [customizing-the-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/customizing-the-analysis "mention").
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [exclude-from-coverage-duplication](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/exclude-from-coverage-duplication "mention")
* [excluding-files-based-on-patterns](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-files-based-on-patterns "mention")
* [excluding-based-on-file-extension](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-based-on-file-extension "mention")
* [advanced-exclusions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/advanced-exclusions "mention")
* [other-adjustments](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/other-adjustments "mention")
* [verifying-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/verifying-analysis-scope "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/introduction "mention") to Adjusting the analysis scope.
