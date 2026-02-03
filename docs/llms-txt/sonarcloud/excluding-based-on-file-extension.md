# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/setting-analysis-scope/excluding-based-on-file-extension.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/setting-analysis-scope/excluding-based-on-file-extension.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/setting-analysis-scope/excluding-based-on-file-extension.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/setting-analysis-scope/excluding-based-on-file-extension.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/setting-analysis-scope/excluding-based-on-file-extension.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/setting-analysis-scope/excluding-based-on-file-extension.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/excluding-based-on-file-extension.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-based-on-file-extension.md

# Excluding based on file extension

You can define for each programming language a set of extensions (file suffixes) to be analyzed. The other extensions will be ignored.

You can perform the setup in SonarQube UI (this requires that you have the project’s Administer permission) or on the CI/CD host. A parameter set on the CI/CD host has precedence over any UI setting of the same parameter.

### Defining file suffix parameters in the UI <a href="#in-the-ui" id="in-the-ui"></a>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Go to **Administration** > **General Settings** > **Languages**.
3. In the drop-down list, select the language you want to configure.
4. In the **General** > **File suffixes** parameter, define the extensions to be analyzed (default values are provided).

### Defining file suffix parameters on the CI/CD host <a href="#on-ci-cd-host" id="on-ci-cd-host"></a>

The table below lists the properties you can use to define on the CI/CD host file suffixes to be analyzed for a given language. For more information, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").

| **Property**                    | **Description**                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| sonar.\<language>.file.suffixes | <p>Defines for a given programming language a set of extensions (file suffixes) to be analyzed (The other extensions will be ignored.).</p><p><strong>Possible values</strong>: Comma-separated list of file extensions.</p><p><strong>Note</strong>: You can see the exact property key syntax on the UI: see <strong>Defining file suffix parameters in the UI</strong> above.</p> |

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-initial-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/setting-initial-scope "mention")
* [exclude-from-coverage-duplication](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/exclude-from-coverage-duplication "mention")
* [excluding-files-based-on-patterns](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-files-based-on-patterns "mention")
* [excluding-based-on-file-extension](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-based-on-file-extension "mention")
* [advanced-exclusions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/advanced-exclusions "mention")
* [other-adjustments](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/other-adjustments "mention")
* [verifying-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/verifying-analysis-scope "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/introduction "mention") to Adjusting analysis scope
