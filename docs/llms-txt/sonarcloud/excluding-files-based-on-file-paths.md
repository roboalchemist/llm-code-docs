# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/analysis-functions/analysis-scope/excluding-files-based-on-file-paths.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/analysis-functions/analysis-scope/excluding-files-based-on-file-paths.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/analysis-functions/analysis-scope/excluding-files-based-on-file-paths.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/analysis-scope/excluding-files-based-on-file-paths.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/analysis-functions/analysis-scope/excluding-files-based-on-file-paths.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/analysis-scope/excluding-files-based-on-file-paths.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/analysis-scope/excluding-files-based-on-file-paths.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/excluding-files-based-on-file-paths.md

# Excluding files based on file paths

This feature is only available in the [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

As an organization admin, you can exclude, at the organization level, files from the project’s analysis scope based on file paths. It means that this analysis scope adjustment applies to all projects in the organization. However, they can be overridden at the project level in the UI or through [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") set on the CI/CD host. For more information about setting your scope at the project level, see the [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/introduction "mention") page in the [setting-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope "mention") section.

To exclude the files, you define file exclusion parameters based on directory and file name patterns.

### Example of an initial scope adjustment <a href="#initial-scope-adjustment-example" id="initial-scope-adjustment-example"></a>

We consider the following repository example where test files are contained in both `test/` directories. Source and test code files are contained in the same ancestor directory: `src/` which is chosen as the initial analysis scope for both source and test code. Therefore, a scope adjustment is necessary.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-729a14af93b700a5bc210b642223dc32a87ce423%2F0c03347ba168dcb52539f597eb0d88dd320480e6.png?alt=media" alt="When a clear separation between source and test code does not exist, you must adjust the analysis scope using path matching patterns recognized by SonarQube Cloud."><figcaption></figcaption></figure>

We adjust the initial scope as follows:

* For source files: by defining an exclusion parameter with the pattern `src/**/test/**/*`

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-bded742ba370e218909d6ce1710434a0bdbe5d9f%2Fa4f2d03740c239272339a6e89a586763dc4e2ad2.png?alt=media" alt="You can set your Source File Exclusions using the SonarQube Cloud property sonar.exclusions."><figcaption></figcaption></figure></div>

* For test files: by defining an inclusion parameter with the pattern `src/**/test/**/*`

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-cca692769eda0a90ecaf48eb1414a600d8dc0314%2Fd257e655eb3cf9fdeffc6c91bd3aeda177597045.png?alt=media" alt="You can set your Test file Inclusions using the SonarQube Cloud property sonar.test.inclusions."><figcaption></figcaption></figure></div>

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
A file path definition is either relative to the `sonar.projectBaseDir` property (which is by default the directory from which the analysis was started, for more information see [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention")) or absolute.
{% endhint %}

### Defining a file exclusion parameter <a href="#defining-exclusion-parameter" id="defining-exclusion-parameter"></a>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Analysis scope**.
3. In **Files**, choose the parameter to configure (source or test code; exclusion or inclusion patterns), and enter and save the first pattern. See [defining-matching-patterns](https://docs.sonarsource.com/sonarqube-cloud/appendices/defining-matching-patterns "mention") for more details.
4. Add additional patterns to the parameter if necessary.
5. Define other parameters if necessary. Make sure you use either **Source File Exclusions** or **Source File Inclusions**, and either **Test File Exclusions** or **Test File Inclusions**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-544cb31b0910be15991b116800930e54e5a66e56%2Fd8a59ba93779154cc3769d4f4d3f373627770bf8.png?alt=media" alt="SonarQube Cloud offers you a place to add your source and test file exclusions and inclusions in the UI, at a global level. Navigate to Your Organization > Administration > Analysis Scope > Files to define your analysis scope at the global level." width="563"><figcaption></figcaption></figure></div>
