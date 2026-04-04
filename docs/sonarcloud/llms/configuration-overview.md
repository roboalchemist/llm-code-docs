# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/analysis-parameters/configuration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/analysis-parameters/configuration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/analysis-parameters/configuration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters/configuration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters/configuration-overview.md

# Configuration overview

### Settings hierarchy <a href="#settings-hierarchy" id="settings-hierarchy"></a>

You can configure project analysis settings mainly in the UI, in scanner configuration files, and as scanner arguments on the command line. Here is the hierarchy in order of precedence:

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-eea3af3a29c1b9d2fbfed1da67c0190b4949ce27%2Fsettings-hierarchy.png?alt=media" alt="Analysis parameters can be set in (from the lowest to the highest priority) : project properties, scanner configuration files, scanner arguments on the command line."><figcaption></figcaption></figure>

1. **Organization properties** (Enterprise only): As an organization admin, you can define analysis scope adjustments at the organization level in the SonarQube UI by going to *Your Organization* > **Administration** > **Analysis Scope**.
2. **Project properties:** As a project admin, you can change these properties in the SonarQube UI and apply them to your project by going to *Your Organization* > *Your Project* > **Administration** > **General Settings**.
3. **Scanner configuration files**: You can configure scanner parameters in a configuration file within your project or a build framework. Values set in the configuration file will override organization and project properties set in the UI. See the individual scanner pages for more information.
4. **Scanner arguments**: For CI-based analysis, you can also set parameters on the command line. This can be done with the standalone command-line tool sonar-scanner or with any of the build-tool-specific variants such as SonarScanner for Maven and SonarScanner for Gradle. Scanner arguments override the scanner configuration files.

If you use environment variables, which are available for some properties, they will be overridden by scanner arguments.

### General configuration guidelines

Consider the following:

* Most of the analysis parameters you can set in the UI can also be set in scanner configuration files or as scanner arguments by using the corresponding sonar properties (a sonar property is a key/value pair in which the key has the `sonar.<property>` syntax) .
* Sonar property keys are case-sensitive.
* Some analysis parameters cannot be set in the UI; they are listed in [parameters-not-settable-in-ui](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters/parameters-not-settable-in-ui "mention").
* Only parameters you set through the UI are stored in the SonarQube Cloud database. Parameters set in the command line or in the scanner configuration files will only be effective for the current analysis and *not* for subsequent analyses or analyses in SonarQube for IDE with connected mode. For example, if you override the `sonar.exclusions` parameter via the command line for a specific project, it will not be stored in the database. Subsequent analyses without the `sonar.exclusions` parameter in the command line or scanner configuration file, or analyses in SonarQube for IDE, will be executed with the exclusions stored in the database.
* See the corresponding SonarScanner section in this documentation for general information about the configuration of analysis parameters in scanner configuration files or as scanner arguments:
  * [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention")
  * [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention")
  * SonarScanner for NPM: [configuring](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-npm/configuring "mention")
  * SonarScanner for .NET: [using](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/using "mention")
  * [sonarscanner-for-python](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-python "mention")
  * [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention")
* If you use PowerShell, you need to wrap any parameter value that includes a dot (`.`) in either single or double quotes to prevent misinterpretation.
* To adjust the analysis scope of your project, see [setting-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope "mention").
* To include test coverage in your project analysis, see the [test-coverage](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage "mention") pages.
* To import issues generated by third-party analyzers, see the [external-analyzer-reports](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports "mention") page.
