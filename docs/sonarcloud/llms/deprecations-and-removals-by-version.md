# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/deprecations-and-removals-by-version.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/release-notes-and-notices/deprecations-and-removals-by-version.md

# Deprecations and removals

This page contains information on the deprecation and removal of SonarQube features and API endpoints.

* Each deprecated feature or API endpoint will be removed in a future release. We recommend to start using its replacement (if any) as soon as possible.
* To check for breaking changes before you upgrade, read the [release-upgrade-notes](https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/release-notes-and-notices/release-upgrade-notes "mention") for all the versions between your current version and the target version.
* [plugin-basics](https://docs.sonarsource.com/sonarqube-server/10.7/extension-guide/developing-a-plugin/plugin-basics "mention") deprecations are announced in the [sonar-plugi-api GitHub repository](https://github.com/SonarSource/sonar-plugin-api/releases).

**Deprecation time frame**

If a feature or API endpoint is deprecated in version X.Y, it is planned to be dropped in version (X+1).0. For example, a feature deprecated in the 10.x version is kept until the 10.x LTA (Long-Term Active) version and dropped in the 11.0 version or later.

A backward-incompatible change or dropping of a public API endpoint, a workflow, or a feature can be considered deprecation. Once deprecated, they will be removed in a future version.

### SonarQube 10.6 <a href="#sonarqube-106" id="sonarqube-106"></a>

#### Deprecated build wrapper output property <a href="#deprecated-build-wrapper-output-property" id="deprecated-build-wrapper-output-property"></a>

* Announced in SonarQube 10.6 (June 2024)
* Removal in SonarQube 11.0 or later

Build Wrapper collects information from the build in two separate JSON formats: `compile_commands.json` and `build-wrapper-dump.json`. Both these files are generated in the specified output directory. The `build-wrapper-dump.json` format and its associated property `sonar.cfamily.build-wrapper-output` are deprecated. The `sonar.cfamily.compile-commands` property should be used instead to specify the path to the `compile_commands.json` file.
