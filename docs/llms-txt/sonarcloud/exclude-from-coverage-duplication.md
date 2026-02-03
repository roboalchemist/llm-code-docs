# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/setting-analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/setting-analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/setting-analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/setting-analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/setting-analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/setting-analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/exclude-from-coverage-duplication.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/exclude-from-coverage-duplication.md

# Excluding from coverage or duplication

You can exclude specific files from your project’s code coverage analysis or duplication check analysis (detection of identical lines of code).

{% hint style="info" %}
As the admin an Enterprise plan organization, you can perform this setting as the default setting for all projects of your organization. See [exclude-from-coverage-duplication](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/exclude-from-coverage-duplication "mention").
{% endhint %}

### Excluding specific files from the code coverage analysis <a href="#from-coverage" id="from-coverage"></a>

You can perform the setup in SonarQube UI (this requires that you have the project’s Administer permission) or on the CI/CD host. A parameter set on the CI/CD host has precedence over any UI setting of the same parameter.

<details>

<summary>In the UI</summary>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Go to **Administration** > **General Settings** > **Analysis scope**.
3. In **Code coverage** > **Coverage Exclusions**, enter and save a path-matching pattern to define files to be excluded from the code coverage analysis. See [defining-matching-patterns](https://docs.sonarsource.com/sonarqube-cloud/appendices/defining-matching-patterns "mention") for details.

</details>

<details>

<summary>On the CI/CD host</summary>

The table below lists the sonar properties you can use to exclude specific files from the code coverage analysis. For more information, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").

| **Property**              | **Description**                                                                                                                                                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sonar.coverage.exclusions | <p>Defines the source files to be excluded from the code coverage analysis.</p><p><strong>Possible values</strong>: comma-separated list of path-matching patterns. See <a data-mention href="../../../appendices/defining-matching-patterns">defining-matching-patterns</a> for details.</p> |

</details>

### Excluding specific files from the duplication check <a href="#from-duplication" id="from-duplication"></a>

You can perform the setup in SonarQube UI (this requires that you have the project’s Administer permission) or on the CI/CD host. A parameter set on the CI/CD host has precedence over any UI setting of the same parameter.

<details>

<summary>In the UI</summary>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Go to **Administration** > **General Settings** > **Analysis scope**.
3. In **Duplication > Duplication Exclusions**, enter and save a path-matching pattern to define files to be excluded from the duplication check. See [defining-matching-patterns](https://docs.sonarsource.com/sonarqube-cloud/appendices/defining-matching-patterns "mention") for details.

</details>

<details>

<summary>On the CI/CD host</summary>

The table below lists the sonar properties you can use to exclude specific files from the duplication check. For more information, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").

|                      |                                                                                                                                                                                                                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Property**         | **Description**                                                                                                                                                                                                                                                                         |
| sonar.cpd.exclusions | <p>Defines the source files to be excluded from the duplication check.</p><p><strong>Possible values</strong>: comma-separated list of path-matching patterns. See<a data-mention href="../../../appendices/defining-matching-patterns">defining-matching-patterns</a> for details.</p> |

</details>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-initial-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/setting-initial-scope "mention")
* [excluding-files-based-on-patterns](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-files-based-on-patterns "mention")
* [excluding-based-on-file-extension](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-based-on-file-extension "mention")
* [advanced-exclusions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/advanced-exclusions "mention")
* [other-adjustments](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/other-adjustments "mention")
* [verifying-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/verifying-analysis-scope "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/introduction "mention") to Adjusting analysis scope
