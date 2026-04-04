# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-security/troubleshooting-the-dependency-analysis.md

# Troubleshooting the dependency analysis

Advanced Security is an add-on that requires a separate subscription to your SonarQube Cloud's [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

### Issues with analysis results <a href="#issues-with-analysis-results" id="issues-with-analysis-results"></a>

Guidelines for troubleshooting analysis result issues.

#### I don't see any issues on my first PR analysis <a href="#i-dont-see-any-issues-on-my-first-pr-analysis" id="i-dont-see-any-issues-on-my-first-pr-analysis"></a>

If the first analysis for your project is on a pull request, the analysis will be unable to determine what dependencies and risks are new in your pull request, so you may not see the results you expect. We recommend running at least one analysis on the main branch before running analyses on pull requests.

#### I don't see any dependencies analyzed (No packages were found.)

Make sure that you have a supported manifest and lockfile (shown in the [Supported languages and package managers](https://docs.sonarsource.com/sonarqube-cloud/analyzing-projects-for-dependencies-sca#supported-languages-and-package-managers) section) available, not excluded from analysis, and not excluded by SCM exclusions (such as `.gitignore`). For example, if you exclude XML files (e.g. `sonar.exclusions=**/*.xml` ) for a Maven Java project or JSON files (e.g. `sonar.exclusions=**/*.json`) in JavaScript/TypeScript projects, then Sonar scanner will not find `pom.xml`, `package.json`, etc.

#### My SCA analysis takes too long <a href="#my-sca-analysis-takes-too-long" id="my-sca-analysis-takes-too-long"></a>

A properly configured analysis with a lockfile should take minimal time. Common causes of extended analysis time are:

**JavaScript**

Ensure the directory is excluded via `sonar.exclusions` or `sonar.sca.exclusions`. See [Analyzing projects for dependencies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/analyzing-projects-for-dependencies-sca) for more information.

**Pip / requirements.txt**

The Sonar analysis will run `pip install -r requirements.txt` in a temporary virtual environment for any discovered `requirements.txt`file. This may take significant memory or time if the installation process requires building core Python wheels.

**Maven/Gradle**

The Sonar analysis will run Maven or Gradle to resolve the dependencies of your project. If a wrapper is used, it will use the specified JVM memory configuration for maven/gradle, which may be more than what your analysis previously required.

Ensure that the memory parameters are set appropriately, or that your analysis runners have enough memory for your configured JVM memory parameters.

#### How do I see what the SCA analysis is doing? <a href="#how-do-i-see-what-the-sca-analysis-is-doing" id="how-do-i-see-what-the-sca-analysis-is-doing"></a>

You can see the commands being run by examining the scanner log and looking for `Running…` lines after the `----- Gather SCA dependencies on project` line. Running the scanner in debug mode `sonar.verbose`, or passing `-X` provides additional detail.

#### I see more dependencies than expected on my PNPM workspace projects <a href="#i-see-more-dependencies-than-expected-on-my-pnpm-workspace-projects" id="i-see-more-dependencies-than-expected-on-my-pnpm-workspace-projects"></a>

SonarQube's SCA support currently does not distinguish between workspaces in a PNPM monorepo setup. If run in a workspace of a monorepo, all dependencies in the monorepo are reported.

### Unknown lifecycle phase error <a href="#unknown-lifecycle-phase-error" id="unknown-lifecycle-phase-error"></a>

When analyzing some java projects, you may get an error that says "there was a problem running `mvn dependency:tree”`, and the following message in the details of the error:

`[ERROR] Unknown lifecycle phase "/some/path/.m2"`

This is due to a conflict between a `MAVEN_CONFIG` environment variable that was present during analysis and the `mvnw` maven wrapper in your project directory. You can solve this by doing one of the following:

* unset the `MAVEN_CONFIG` environment variable
* update the maven wrapper in your repository by running `./mvnw wrapper:wrapper`, and commit the result
* force the use of `mvn` instead of the wrapper by setting the `sonar.sca.mavenIgnoreWrapper` property to `true`

### No dependency chains found <a href="#no-dependency-chains-found" id="no-dependency-chains-found"></a>

Sonar uses lockfiles that contain a full dependency graph to determine how dependencies are used by your project. If a lockfile is missing, or cannot be generated, dependency chains will be missing.

You can fix this error by ensuring a lockfile is present when analysis is run. Sonar recommends committing the lockfile to your source control system. For examples, you can see the documentation for the [python dependency manager poetry](https://python-poetry.org/docs/basic-usage/#committing-your-poetrylock-file-to-version-control) and the [JavaScript dependency manager yarn](https://classic.yarnpkg.com/lang/en/docs/yarn-lock/).

### Errors in the dependency analysis <a href="#errors-in-dependency-analysis" id="errors-in-dependency-analysis"></a>

The scanner will warn you of any errors when processing your dependency files.

| **Error message**                                          | **Recommendation**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| No packages were found.                                    | Make sure that you have a supported manifest and lockfile shown in [Analyzing project for dependencies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/analyzing-projects-for-dependencies-sca) (see the "Supported languages and package managers" section).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| There was a problem parsing the manifests.                 | Same as above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| This type of file is not supported.                        | Same as above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| \<name> (\<platform>) has inexact version '\<requirement>' | <p>Certain manifest files (such as a NPM package.json file) list a range of allowable dependencies. When a dependency is specified as a range, Sonar uses a lockfile to determine the exact dependency in use.</p><p>When a lockfile is either not present, or cannot be properly generated, the scanner raises an error that the version specified is not exact and cannot be resolved to a specific software version.</p><p>You can fix this error by ensuring a lockfile is present when analysis is run.</p><p>For examples, see the documentation for the <a href="https://python-poetry.org/docs/basic-usage/#committing-your-poetrylock-file-to-version-control">python dependency manager poetry</a> and the <a href="https://classic.yarnpkg.com/lang/en/docs/yarn-lock/">JavaScript dependency manager yarn</a>.</p> |

### Related pages <a href="#related-pages" id="related-pages"></a>

* [Reviewing and fixing dependency risks](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/reviewing-and-fixing-dependency-risks)
* [Analyzing projects for dependencies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/analyzing-projects-for-dependencies-sca)
* [Managing license profiles and policies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/managing-license-profiles-and-policies)
* [Best practices for managing dependency risks](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/best-practices-for-managing-dependency-risks)
