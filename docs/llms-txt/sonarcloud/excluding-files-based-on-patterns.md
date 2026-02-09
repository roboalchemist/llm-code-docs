# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/setting-analysis-scope/excluding-files-based-on-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/setting-analysis-scope/excluding-files-based-on-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/setting-analysis-scope/excluding-files-based-on-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/setting-analysis-scope/excluding-files-based-on-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/setting-analysis-scope/excluding-files-based-on-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/setting-analysis-scope/excluding-files-based-on-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/excluding-files-based-on-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-files-based-on-patterns.md

# Excluding based on path-matching patterns

You can adjust your project’s initial analysis scope by excluding files based on path-matching patterns. To exclude the files, you define file exclusion parameters based on directory and file name patterns.

{% hint style="info" %}
As the admin an Enterprise plan organization, you can perform these settings as the default settings for all projects of your organization. See [excluding-files-based-on-file-paths](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/excluding-files-based-on-file-paths "mention").
{% endhint %}

You can perform the setup in SonarQube UI (this requires that you have the project’s Administer permission) or on the CI/CD host. A parameter set on the CI/CD host has precedence over any UI setting of the same parameter.

### Example of an initial scope adjustment <a href="#initial-scope-adjustment-example" id="initial-scope-adjustment-example"></a>

We consider the following repository example where test files are contained in both `test/` directories. Source and test code files are contained in the same ancestor directory: `src/` which is chosen as the initial analysis scope for both source and test code. Therefore, a scope adjustment is necessary.

<figure><img src="broken-reference" alt="Both test directories in this example must be excluded from the source code&#x27;s analysis scope"><figcaption></figcaption></figure>

We adjust the initial scope as follows:

* For source files: by defining an exclusion parameter with the pattern `src/**/test/**/*`

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-bded742ba370e218909d6ce1710434a0bdbe5d9f%2Fa4f2d03740c239272339a6e89a586763dc4e2ad2.png?alt=media" alt="You can set your Source File Exclusions using the SonarQube Cloud property sonar.exclusions." width="401"><figcaption></figcaption></figure></div>

* For test files: by defining an inclusion parameter with the pattern `src/**/test/**/*`

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-cca692769eda0a90ecaf48eb1414a600d8dc0314%2Fd257e655eb3cf9fdeffc6c91bd3aeda177597045.png?alt=media" alt="You can set your Test file Inclusions using the SonarQube Cloud property sonar.test.inclusions." width="431"><figcaption></figcaption></figure></div>

### Principles governing the use of file exclusion parameters <a href="#principles" id="principles"></a>

A file exclusion parameter:

* Applies either to source code (also called main code) or to test code files.\
  The SonarScanner must identify the source code as well as the test code since they are processed differently by SonarQube. A code file is either a source or a test code; it cannot be both (If this is the case, the scanner will fail the analysis with an error message.).
* Contains:
  * Either exclusion patterns: to define files to be excluded from the analysis scope.
  * Or inclusion patterns: to define files to be included in the scope.\
    It means that the rest of the files is excluded from the analysis scope.

For a given code category (source or test), we strongly recommend that you use either exclusion-pattern or inclusion-pattern parameters, depending on what is simpler in your situation (If you do not and there is an overlapping, then exclusion patterns have precedence over inclusion patterns.).

The following applies:

* The parameter defined at the project level will override the same parameter defined at the organization level.\
  For example, if the organization administrator defines the exclusion pattern for source code `src/**/test1/**/*` at the organization level, then, if the project administrator sets the exclusion pattern for source code `src/**/test2/**/*` for their project, the scanner will consider only the pattern `src/**/test2/**/*` to compute source file exclusion.
* If *test file inclusion* patterns are used, the scanner will automatically set these patterns as *source file exclusion* patterns during project analysis. These source file exclusion patterns will apply in addition to the other configured source file exclusion patterns.\
  For example:
  * If the exclusion pattern for source code is `src/**/test5/**/*` and the inclusion pattern for test code is `src/**/test6/**/*`
  * Then the scanner will consider both patterns to compute the *source file exclusion*:\
    `src/**/test5/**/*` and `src/**/test6/**/*`.

{% hint style="info" %}
A file path definition is either relative to the `sonar.projectBaseDir` property, which is by default the directory from which the analysis was started, or absolute. For more information see [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").
{% endhint %}

### Defining a file exclusion parameter in the UI <a href="#defining-exclusion-parameter-in-ui" id="defining-exclusion-parameter-in-ui"></a>

1. Retrieve the project you wish to configure. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more information.
2. Go to **Administration** > **General Settings** > **Analysis Scope**.
3. In **Files**, choose the parameter to configure (source or test code, exclusion or inclusion patterns), and enter and save the first pattern. See [defining-matching-patterns](https://docs.sonarsource.com/sonarqube-cloud/appendices/defining-matching-patterns "mention") for more information.
4. Add additional patterns to the parameter if necessary.
5. Define other parameters if necessary. Make sure you use either **Source File Exclusions** or **Source File Inclusions**, and either **Test File Exclusions** or **Test File Inclusions**.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d8bf56383c0695ec96e56e8e2b1851bbf733c47d%2Fsonarcloud-analysis-scope-file-exclusion-parameter.png?alt=media" alt="Defining a file exclusion parameter in the UI"><figcaption></figcaption></figure>

{% hint style="info" %}
If a parameter is defined at the organization level, it will appear at the project level as "(default)". You can edit it for your project. Click **Reset** to reset the value to its default value.
{% endhint %}

### Defining a file exclusion parameter on the CI/CD host <a href="#defining-exclusion-parameter-on-ci-cd-host" id="defining-exclusion-parameter-on-ci-cd-host"></a>

The table below lists the properties you can use to define a file exclusion parameter by setting sonar properties on CI/CD host. For more information, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").

| **Property**          | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sonar.exclusions      | <p>Defines the source files (non-test files) to be excluded from the analysis.</p><p><strong>Possible values</strong>: Comma-separated list of <a data-mention href="../../../appendices/defining-matching-patterns">defining-matching-patterns</a>.</p>                                                                                                                                                                                                  |
| sonar.inclusions      | <p>Defines the source files (non-test files) to be included in the analysis. The other files will be excluded.</p><p><strong>Possible values</strong>: Comma-separated list of <a data-mention href="../../../appendices/defining-matching-patterns">defining-matching-patterns</a>.</p>                                                                                                                                                                  |
| sonar.test.exclusions | <p>Defines the test files to be excluded from the analysis.</p><p><strong>Possible values</strong>: Comma-separated list of <a data-mention href="../../../appendices/defining-matching-patterns">defining-matching-patterns</a>.</p><p><strong>Note</strong>: In this property key, the <code>test</code> string is in singular, unlike the <code>sonar.tests</code> property defining the analysis initial scope.</p>                                   |
| sonar.test.inclusions | <p>Defines the test files to be included from the analysis. The other files will be excluded.</p><p><strong>Possible values</strong>: Comma-separated list of <a data-mention href="../../../appendices/defining-matching-patterns">defining-matching-patterns</a>.</p><p><strong>Note</strong>: In this property key, the <code>test</code> string is in singular, unlike the <code>sonar.tests</code> property defining the analysis initial scope.</p> |

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-initial-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/setting-initial-scope "mention")
* [exclude-from-coverage-duplication](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/exclude-from-coverage-duplication "mention")
* [excluding-files-based-on-patterns](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-files-based-on-patterns "mention")
* [excluding-based-on-file-extension](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-based-on-file-extension "mention")
* [advanced-exclusions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/advanced-exclusions "mention")
* [other-adjustments](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/other-adjustments "mention")
* [verifying-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/verifying-analysis-scope "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/introduction "mention") to Adjusting analysis scope
