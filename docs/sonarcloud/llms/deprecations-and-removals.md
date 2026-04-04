# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/release-notes-and-notices/deprecations-and-removals.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/deprecations-and-removals.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/deprecations-and-removals.md

# Deprecations and removals

### Deprecation policy <a href="#deprecation-policy" id="deprecation-policy"></a>

A backward-incompatible change or dropping of a public API endpoint, a workflow, or a feature can be considered deprecation. Once deprecated, they will be removed after a defined period of time.

Before making a backward-incompatible change or dropping a public API endpoint, it is marked as obsolete or deprecated. Once deprecated, they will be removed after a defined period of time.

#### Deprecation timeframe <a href="#deprecation-timeframe" id="deprecation-timeframe"></a>

* When a public API endpoint is to be dropped, Sonar will announce this at least **180 days** before to the users.
* When a feature is to be dropped, Sonar will announce this at least **90 days** before to the users.
* The feature or API endpoint will be removed on the expiry of the deprecation period.

#### Deprecation communication <a href="#deprecation-communication" id="deprecation-communication"></a>

1. Deprecation notices will be published in SonarCloud documentation under the dedicated *Deprecation announcements* section below.
2. Users will be notified about an API endpoint deprecation in the [Sonar community](https://community.sonarsource.com/c/announce/20) (future deprecation announcements will be available at this link).
3. Users (organization owner and token owner if the endpoint is used by the organization) will be notified about the deprecation of an API endpoint via email. If you have used the API endpoint that is about to be deprecated within the last 30 days prior to deprecation, you will receive an email announcing the deprecation.
4. A reminder of the deprecation will be delivered through email 90, 60, and 30 days prior to the removal of the endpoint.
5. Deprecation of a feature or workflow will be communicated to existing users within the product UI.
6. Notification will include the scope of deprecation, timeframe of deprecation, and alternative solution (if available).

### Deprecation announcements <a href="#deprecation-announcements" id="deprecation-announcements"></a>

#### Deprecated SonarCloud with Travis CI add-on <a href="#deprecated-build-wrapper-output-property" id="deprecated-build-wrapper-output-property"></a>

Support for the Travis CI add-on will end on March 9th, 2026. Please see [this page](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/other-cis) for information on alternative options.

#### Deprecated Amazon CodeCatalyst <a href="#deprecated-build-wrapper-output-property" id="deprecated-build-wrapper-output-property"></a>

On October 7th, 2025, AWS announced the retirement of CodeCatalyst. Starting November 7th, 2025, no new spaces can be created, and access is limited to existing customers. As a consequence, [this tool](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/amazon-codecatalyst) won't be maintained anymore starting December 16th, 2025.&#x20;

* Your code is built with Maven: run `org.sonarsource.scanner.maven:sonar-maven-plugin:3.11.0.3922:sonar` during the build (more info in the [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention") documentation)
* Your code is built with Gradle: use the [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention") during the build
* You want to analyze a .NET solution: follow our interactive tutorial for other CI's
* You want to analyze C and C++ code: rely on our [SonarQube Cloud Scan for C and C++](https://github.com/marketplace/actions/sonarcloud-scan-for-c-and-c) and look at [our sample C and C++ project](https://github.com/sonarsource-cfamily-examples?q=gh-actions-sc\&type=all\&language=\&sort=)
* Your code uses another language or ecosystem: use [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention")

#### Deprecated Design and Architecture features <a href="#deprecated-build-wrapper-output-property" id="deprecated-build-wrapper-output-property"></a>

* Announced in October 2025
* Removal after January 17 2026

The Design and Architecture features are deprecated and will be removed in the future.

#### Deprecated build wrapper output property <a href="#deprecated-build-wrapper-output-property" id="deprecated-build-wrapper-output-property"></a>

* Announced in May 2024
* Removal after July 10 2024

Build Wrapper collects information from the build in two separate JSON formats: `compile_commands.json` and `build-wrapper-dump.json`. Both these files are generated in the specified output directory. The `build-wrapper-dump.json` format and its associated property `sonar.cfamily.build-wrapper-output` are deprecated. The `sonar.cfamily.compile-commands` property should be used instead to specify the path to the `compile_commands.json` file.

### Additional API updates <a href="#api-updates" id="api-updates"></a>

When querying rules or issues, INFO and BLOCKER may appear as statuses at the quality level (i.e. a rule might have a reliability severity of BLOCKER). It is also possible to create rules/issues with these additional severities.

The affected APIs:

* api/issues/\*
* api/rules/\*
* api/projects/export\_findings
* api/qualityprofiles/compare
* api/qualityprofiles/changelog
