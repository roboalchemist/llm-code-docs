# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/advanced-security/analyzing-projects-for-dependencies.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/advanced-security/analyzing-projects-for-dependencies.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/advanced-security/analyzing-projects-for-dependencies.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/advanced-security/analyzing-projects-for-dependencies.md

# Source: https://docs.sonarsource.com/sonarqube-server/advanced-security/analyzing-projects-for-dependencies.md

# Analyzing projects for dependencies (SCA)

*Advanced Security is only available in SonarQube Server, as an add-on starting in* [*Enterprise edition*](https://www.sonarsource.com/plans-and-pricing/sonarqube/)*.*

With Software Composition Analysis (SCA), SonarQube analyzes your built project and returns information on:

* vulnerabilities in your third-party open source dependencies
* where your open source dependencies may conflict with your organization’s license policies

Here are things to check out for to ensure that you get fast and accurate dependency analysis.

### Enabling the SCA service <a href="#enabling-the-sca-service" id="enabling-the-sca-service"></a>

By default, SCA is not enabled on your instance. To turn on the Sonar SCA service as an admin:

1. Make sure your SonarQube Server license includes Advanced Security.
2. Go to **Administration** > **Configuration** > **General Settings** > **Advanced Security** and activate the **Software Composition analysis (SCA)** option.

You can choose whether all projects will be scanned using SCA by default, by adjusting the **Analyze all projects checkbox**. If you disable dependency analysis by default, you will need to enable analysis on a project-by-project basis at the scanner level by passing `sonar.sca.enabled=true` as a scanner parameter.

A connectivity test is available after SCA is enabled to test your Internet access.

### Internet connection <a href="#internet-connection" id="internet-connection"></a>

Detecting and remediating third-party vulnerabilities requires a constantly updated source of data. New vulnerabilities are discovered every day, and new releases of software that fix them soon follow. Sonar’s researchers are constantly checking to ensure that our license data is accurate, and for details on how reported vulnerabilities may actually affect your code.

As a result, an internet connection is required to always provide the most up-to-date information on your third-party dependencies, including:

* what licenses you have
* what issues you are affected by
* what workarounds maintainers have published as being available

Your SonarQube Server instance must be able to reach the following servers:

* [api.sonarcloud.io](http://api.sonarcloud.io/)
* [scanner.sonarcloud.io](http://scanner.sonarcloud.io/)

See [#marketplace](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties#marketplace "mention") for more information about configuring system properties and environment variables.

You can use the connectivity check under **Administration** > **Configuration** > **General Settings** > **Advanced Security** to test your network access.

#### What data is collected <a href="#what-data-is-collected" id="what-data-is-collected"></a>

Whenever you run an analysis, data is sent to a Sonar cloud service for analysis. The Sonar scanner collects the *manifests* of your projects. Manifests are language-specific files that define your projects’ dependencies, such as `pom.xml` for Java, or `requirements.txt` for Python. The scanner also collects any relevant lockfiles that describe the fully-resolved set of dependencies, such as `package-lock.json` for a JavaScript project.

These manifests and lockfiles are assembled into an archive file and sent to a Sonar cloud service for analysis. All data is sent over a secure HTTPS connection. Information on your dependencies and their issues is returned to your SonarQube Server instance. No source code is sent to Sonar.

Manifests and lockfiles are not stored persistently in Sonar. Sonar may collect aggregate data, and other service telemetry on open source package usage in an anonymized way.

The manifest and lockfiles that are processed contain a list of all dependencies of your project, which could include internally-developed library names. The Sonar service compares dependency names against a set of known open source components; any internally-developed library name would not match, and therefore would not have any license or vulnerability data returned for that library.

### Supported languages and package managers <a href="#supported-languages-and-package-managers" id="supported-languages-and-package-managers"></a>

SonarQube evaluates your third-party open source code usage by matching dependencies defined in your project’s dependency files to known open source code on upstream package managers. It currently supports the following languages, package managers, and package manager files:

| Language                   | <p>Package manager<br>/Build tool</p> | Package repository                                                   | Manifest file names                                                                                | Lock file names                                                                                                   |
| -------------------------- | ------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Java                       | Maven                                 | <p><a href="https://central.sonatype.com/">Maven Central</a><br></p> | pom.xml                                                                                            | Generated at the time of analysis                                                                                 |
| Java                       | Gradle                                | <p><a href="https://central.sonatype.com/">Maven Central</a><br></p> | <ul><li>build.gradle</li><li>build.gradle.kts</li></ul>                                            | Generated at the time of analysis                                                                                 |
| JavaScript                 | NPM                                   | [NPM](https://npmjs.com/)                                            | package.json                                                                                       | <ul><li>package-lock.json</li><li>npm-shrinkwrap.json</li></ul>                                                   |
| JavaScript                 | Yarn                                  | [NPM](https://npmjs.com/)                                            | package.json                                                                                       | yarn.lock                                                                                                         |
| JavaScript                 | PNPM                                  | [NPM](https://npmjs.com/)                                            | package.json                                                                                       | pnpm-lock.yaml                                                                                                    |
| JavaScript                 | Bun                                   | [NPM](https://npmjs.com/)                                            | package.json                                                                                       | bun.lock                                                                                                          |
| Kotlin                     | Maven                                 | [Maven Central](https://central.sonatype.com/)                       | pom.xml                                                                                            | Generated at the time of analysis                                                                                 |
| Kotlin                     | Gradle                                | [Maven Central](https://central.sonatype.com/)                       | <ul><li>build.gradle</li><li>build.gradle.kts</li></ul>                                            | Generated at the time of analysis                                                                                 |
| PHP                        | Composer                              | [Packagist](https://packagist.org/)                                  | composer.json                                                                                      | composer.lock                                                                                                     |
| Python                     | Pip                                   | [PyPI](https://pypi.org/)                                            | requirements.txt                                                                                   | Generated at the time of analysis                                                                                 |
| Python                     | Pipenv                                | [PyPI](https://pypi.org/)                                            | Pipfile                                                                                            | Pipfile.lock                                                                                                      |
| Python                     | Poetry                                | [PyPI](https://pypi.org/)                                            | pyproject.toml                                                                                     | poetry.lock                                                                                                       |
| Scala                      | Maven                                 | [Maven Central](https://central.sonatype.com/)                       | pom.xml                                                                                            | Generated at the time of analysis                                                                                 |
| Scala                      | Gradle                                | [Maven Central](https://central.sonatype.com/)                       | build.gradle                                                                                       | Generated at the time of analysis                                                                                 |
| Golang                     | go                                    | [pkg.go.dev](https://pkg.go.dev/)                                    | go.mod                                                                                             | Generated at the time of analysis                                                                                 |
| C#                         | NuGet                                 | <p><a href="https://www.nuget.org/">NuGet Gallery</a><br></p>        | <ul><li><em>.csproj</em></li><li><em>Project.json</em></li><li>.nuspec</li></ul>                   | <ul><li>packages.lock.json<br></li><li>project.assets.json</li><li>Project.lock.json</li><li>paket.lock</li></ul> |
| Ruby                       | Rubygems                              | [Rubygems](https://rubygems.org/)                                    | Gemfile                                                                                            | Gemfile.lock                                                                                                      |
| Rust                       | Cargo                                 | [Crates.io](https://crates.io/)                                      | Cargo.toml                                                                                         | Cargo.lock                                                                                                        |
| C/C++ (beta)​              | Conan                                 | ​[conan.io](https://conan.io/)                                       | conanfile.py                                                                                       | conan.lock                                                                                                        |
| C/C++ (beta)​              | VCPkg                                 | ​[vcpkg.io](https://vcpkg.io/)                                       | vcpkg.json                                                                                         | Generated at the time of analysis                                                                                 |
| Generic SBOM (CycloneDX)   | N/A                                   | N/A                                                                  | <p></p><ul><li>cyclonedx.json</li><li>cyclonedx.xml</li><li>*.cdx.json</li><li>*.cdx.xml</li></ul> | N/A                                                                                                               |
| Generic SBOM (SPDX) (beta) | N/A                                   | N/A                                                                  | <p></p><ul><li>*.spdx</li><li>*.spdx.json</li></ul>                                                | N/A                                                                                                               |

### Ensure the analysis is run in an appropriate environment <a href="#appropriate-environment" id="appropriate-environment"></a>

To correctly analyze both your direct and transitive dependencies on projects where there is not a lockfile that contains all dependencies, SonarQube executes commands using your build tools to get a full dependency list.

#### Note on security <a href="#note-on-security" id="note-on-security"></a>

To run a dependency analysis, the SonarQube scanner might install the dependencies required to build your application. This could pull in untrusted artifacts, similar to while you’re building the application. Ensure the analysis will run in a secure environment before proceeding.

#### Notes on specific build tools and language ecosystems <a href="#notes-on-specific-build-tools-and-language-ecosystems" id="notes-on-specific-build-tools-and-language-ecosystems"></a>

**Maven**

The Maven binary (`mvn`) or maven wrapper (`mvnw`) must be located in the project directory, the manifest file’s directory, or in the execution path.

**Gradle**

The Gradle binary (`gradle`) or Gradle wrapper (`gradlew`) must be in the project directory, the manifest file’s directory, or in the execution path.

**pip**

The analysis must be run with the same Python runtime that your application is built on. The SonarQube analysis will create a virtual environment to resolve dependencies, and a C compiler and development libraries may be required, based on your python dependencies.

**Go**

The go runtime that matches the version in `go.mod` must be present.

**Internal artifact repositories**

If your application build configuration includes internal or private artifacts, the analysis process must have network access to your artifact server.

If the analysis is not run in the proper environment, it will cause degraded analysis results and potential analysis failures. You can see more information in analysis warnings in the UI and in the scanner log. See the [Troubleshooting](https://docs.sonarsource.com/sonarqube-server/advanced-security/troubleshooting) section for some common scenarios.

#### Note on pull request analysis <a href="#appropriate-files" id="appropriate-files"></a>

To get valuable results when performing a pull request analysis, the target branch should have been analyzed first.

### Ensure the analysis includes the appropriate files <a href="#appropriate-files" id="appropriate-files"></a>

The SCA analysis recursively searches for appropriate package files for your project. In some cases, this may analyze more files than what your project actually uses. Common cases to look out for include:

* Package manager files in test code and data directories

If you have package manager files present in test directories, ensure these locations are properly excluded from analysis. This can be done in multiple ways:

* Add paths to the common `sonar.exclusions` configuration option. Example: `sonar.exclusions="tests/**"`
* Use the specific `sonar.sca.exclusions` configuration option. Example `sonar.sca.exclusions="tests/**"`
* As long as SonarQube's SCM support is enabled (the default), add the paths to a source control ignore file, such as `.gitignore`

### Customizing the dependency analysis <a href="#customizing-the-dependency-analysis" id="customizing-the-dependency-analysis"></a>

The following parameters influence the results of the dependency analysis.

| `sonar.sca.enabled`                    | Boolean | true            | Indicates whether to perform Software Composition Analysis (SCA) on this project. Set it to false to disable SCA for this project.                                                                                                                                                                                                              |
| -------------------------------------- | ------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sonar.sca.exclusions`                 | String  | <p><br></p>     | <p>A comma-separated list of global patterns of paths to exclude as part of analysis.</p><p>For example, to ignore all manifests under the tests/ and fixtures/ directories, set:</p><p><code>sonar.sca.exclusions = "tests/</code><strong><code>, fixtures/</code></strong><code>"</code></p>                                                  |
| `sonar.sca.allowManifestFailures`      | Boolean | true            | <p>When performing analysis, SonarQube attempts to run your build tools (such as Maven or Gradle) to create a full dependency graph.</p><p>By default, SonarQube does not fail the analysis if these tools fail, and returns information on a limited set of dependencies. Set this parameter to false to force a failure in this scenario.</p> |
| `sonar.sca.goNoResolve`                | Boolean | false           | Disables automatic generation of a Go lock file. This results in degraded dependency information.                                                                                                                                                                                                                                               |
| `sonar.sca.mavenNoResolve`             | Boolean | false           | <p>Disables automatic generation of a Maven lock file and dependency graph file.</p><p>This results in degraded dependency information.</p>                                                                                                                                                                                                     |
| `sonar.sca.mavenForceDepPlugin`        | Boolean | true            | Ensures Maven Dependency Plugin is installed even when it’s not available in the environment.                                                                                                                                                                                                                                                   |
| `sonar.sca.mavenIgnoreWrapper`         | Boolean | false           | Disables a search for a Maven wrapper script `mvnw.` Set this to true if the default Maven wrapper in your `PATH` is not functioning.                                                                                                                                                                                                           |
| `sonar.sca.mavenOptions`               | String  | <p><br></p>     | Sends additional options to any Maven commands used to generate the lock file and dependency graph file.                                                                                                                                                                                                                                        |
| `sonar.sca.gradleNoResolve`            | Boolean | false           | Disables automatic generation of a Gradle dependencies lock file. This results in degraded dependency information.                                                                                                                                                                                                                              |
| `sonar.sca.gradleConfigurationPattern` | String  | <p><br></p>     | Java regex of configurations to include. This is passed to gradle via `-PconfigurationPattern`. When unset, all configurations will be resolved.                                                                                                                                                                                                |
| `sonar.sca.pythonBinary`               | String  | /usr/bin/python | Path to a specific Python binary that should be used if lock files need to be generated.                                                                                                                                                                                                                                                        |
| `sonar.sca.pythonNoResolve`            | Boolean | false           | Disables automatic generation of a Python lock file. This results in degraded dependency information.                                                                                                                                                                                                                                           |
| `sonar.sca.pythonResolveLocal`         | Boolean | false           | When generating a python lockfile, dependency resolution is done in a temporary virtual environment. Set this to true to skip creation of the virtual environment and resolve against the local python environment.                                                                                                                             |
| `sonar.sca.npmNoResolve`               | Boolean | false           | Disables automatic generation of a lock file for an NPM project when a supported lockfile (`yarn.lock`, `package-lock.json`, `pnpm-lock.yaml`, `bun.lock`) is not present.                                                                                                                                                                      |
| `sonar.sca.npmEnableScripts`           | Boolean | false           | By default, when generating a lockfile, the `--ignore-scripts NPM/Yarn` option is passed to ignore any lifecycle scripts. If lifecycle scripts are needed to properly generate dependencies, enable this option.                                                                                                                                |
| `sonar.sca.nugetNoResolve`             | Boolean | false           | Disables automatic generation of a lock file for a Nuget project.                                                                                                                                                                                                                                                                               |
| `sonar.scanner.keepReport`             | Boolean | false           | Not specific to SCA. Keeps the scanner work directory after analysis, including the `dependency-files.tar.xz` that contains dependency files to analyze. Useful if you have access to [commercial support](https://www.sonarsource.com/support/), as the Sonar support team may ask for this file to assist with resolving issues.              |
| `sonar.sca.cfamily`                    | Boolean | false           | When set to true, enables support for C/C++ dependency analysis (beta)                                                                                                                                                                                                                                                                          |
| `sonar.sca.sbomImportPaths`            | String  |                 | Comma-separated list of SBOM files to import and analyze. See “Supported languages and package managers” for supported file types and required file naming.                                                                                                                                                                                     |

### Troubleshooting the dependency analysis <a href="#troubleshooting-the-dependency-analysis" id="troubleshooting-the-dependency-analysis"></a>

See [troubleshooting](https://docs.sonarsource.com/sonarqube-server/advanced-security/troubleshooting "mention") for guidance on how to troubleshoot the dependency analysis.

### Continual analysis <a href="#continual-analysis" id="continual-analysis"></a>

Once SCA analysis has been performed on a permanent branch, Sonar automatically re-analyzes your branch for new dependency risks. This analysis runs once per day. Any newly discovered vulnerability or license risks will be added to the list of dependency risks for your project, any changes to risk factors and scoring will cause any needed severity updates, and any quality gate will be recomputed. For more information on project branches, see [maintaining-the-branches-of-your-project](https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/maintaining-the-branches-of-your-project "mention").

You can change how often your branches are re-analyzed and disable re-analysis from the SonarQube Server UI. To do this, go to **Administration** > **Configuration** > **Advanced Security** > **Configure Branch Rescanning.**

From there, you can set the following:

* **Branch rescan frequency**: Daily, weekly, or never
* **Target branch types**: Main branch only, kept branches only, or all branches

### Related pages <a href="#related-pages" id="related-pages"></a>

* [viewing-dependencies](https://docs.sonarsource.com/sonarqube-server/advanced-security/viewing-dependencies "mention")
* [reviewing-and-fixing-dependency-risks](https://docs.sonarsource.com/sonarqube-server/advanced-security/reviewing-and-fixing-dependency-risks "mention")
* [managing-license-profiles-and-policies](https://docs.sonarsource.com/sonarqube-server/advanced-security/managing-license-profiles-and-policies "mention")
* [troubleshooting](https://docs.sonarsource.com/sonarqube-server/advanced-security/troubleshooting "mention")
* [best-practices-for-managing-dependency-risks](https://docs.sonarsource.com/sonarqube-server/advanced-security/best-practices-for-managing-dependency-risks "mention")
