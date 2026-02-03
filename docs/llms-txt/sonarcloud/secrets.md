# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/secrets.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/secrets.md

# Secrets

Secrets are pieces of user-specific or system-level credentials that should be protected and accessible to legitimate users only.

### Configuring secret-specific parameters (general procedure) <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the Secret-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Secrets**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Adjusting the secret detection scope <a href="#detection-scope" id="detection-scope"></a>

By default, SonarQube Cloud detects exposed secrets in all files processed by the language analyzers. You can refine the scope of the secret detection by:

* Excluding hidden files from the analysis.
* Adding files based on path-matching patterns.
* Adjusting the binary file exclusion setup.

#### Analysis of hidden files <a href="#analysis-of-hidden-files" id="analysis-of-hidden-files"></a>

Depending on which scanner is used, additional hidden files tracked by Git are included in the secrets analysis.

This behavior can be disabled by setting the `sonar.scanner.excludeHiddenFiles` analysis parameter to `true`.

{% hint style="warning" %}
Analyzing additional hidden files is currently only partially supported with the SonarScanner for Maven and Gradle. Additional hidden files are only analyzed if they’re inside the `src/main/java` or `src/test/java` folder in the root or module directories.

Analyzing additional hidden files is currently not supported with SonarScanner for .NET.
{% endhint %}

#### Adding files based on path-matching patterns <a href="#adding-files-based-on-pathmatching-patterns" id="adding-files-based-on-pathmatching-patterns"></a>

If you’re using a git repository, you can add files to the secret detection scope by defining path-matching patterns: the files matching the patterns will be included **provided they are tracked by git**.

To add additional files to the secret detection:

1. In the SonarQube Cloud UI, go to *Your Organization > Your Project* > **Administration** > **General Settings** > **Languages** > **Secrets**.
2. Enable the **Activate inclusion of custom file path patterns** option.
3. In the **List of file path patterns to include**, adjust the default path-matching patterns if necessary. See the [defining-matching-patterns](https://docs.sonarsource.com/sonarqube-cloud/appendices/defining-matching-patterns "mention") page for instructions.

Alternatively, configure the parameters listed below on the CI/CD host (see the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information).

| **Property**                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sonar.text.inclusions.activate` | Enables the inclusion of files to the secret detection according to the path-matching patterns defined in `sonar.text.inclusions`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `sonar.text.inclusions`          | <p>Comma-separated list of path-matching patterns.</p><p><strong>Possible values:</strong> A path can be relative (to the <code>sonar.projectBaseDir</code> property, which is by default the directory from which the analysis was started) or absolute. See also the <a data-mention href="../../appendices/defining-matching-patterns">defining-matching-patterns</a> page.</p><p><strong>Default value</strong>: <strong>/*.sh,</strong>/<em>.bash,\*\*/</em>.zsh,<strong>/*.ksh,</strong>/<em>.ps1,**/</em>.properties,<strong>/\*.conf,</strong>/<em>.pem,**/</em>.config,.env,.aws/config,\*\*/\*.key</p> |

#### Adjusting the binary file exclusion setup <a href="#adjusting-the-binary-file-exclusion-setup" id="adjusting-the-binary-file-exclusion-setup"></a>

SonarQube Cloud excludes binary files from the analysis. In case binary file types are still included in your analysis, you can exclude these additional files.

To do so:

1. In the SonarQube Cloud UI, go to *Your Organization > Your Project >* **Administration > General Settings > Languages > Secrets**.
2. In **Additional binary file suffixes**, enter the list of suffixes to be excluded.

Alternatively, configure the parameter below on the CI/CD host (see the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information).

| **Property**                        | **Description**                                                         |
| ----------------------------------- | ----------------------------------------------------------------------- |
| `sonar.text.excluded.file.suffixes` | Comma-separated list of additional binary file suffixes to be excluded. |

### Parallel code scan <a href="#parallel-code-scan" id="parallel-code-scan"></a>

By default, the analyzer tries to parallelize the analysis of compilation units; it spawns as many jobs as logical CPUs available on the machine.

If required, it is possible to customize the number of scheduled parallel jobs by configuring the property `sonar.text.threads=n` at the scanner level, where `n` is an integer indicating the maximum number of parallel jobs.

You should consider setting the `sonar.text.threads` property only when the automatic detection of the number of logical CPUs cannot detect the desired number. A typical example is when the analysis should not consume all the available computing resources to leave room for other tasks running in parallel on the same machine.

When setting the `sonar.text.threads` property, you should set it to a value less or equal to the number of logical CPUs available. Over-committing does not accelerate the analysis and can even slow it down.

### Analysis of files that don't contain code <a href="#analysis-of-files-that-dont-contain-code" id="analysis-of-files-that-dont-contain-code"></a>

Files that don’t contain code (for example, `build.gradle` and `sonar-project.properties`) are scanned durning analysis and displayed in the SonarQube Cloud UI after an issue is detected in them. If no secrets are detected in those files, they are not displayed in the UI.

### Deactivating secrets analysis <a href="#deactivating-secrets-analysis" id="deactivating-secrets-analysis"></a>

You can deactivate the analysis of secrets by setting the `sonar.text.activate` property to `false`.

### Related pages <a href="#related-pages" id="related-pages"></a>

* See Sonar's [Secrets rules](https://rules.sonarsource.com/secrets/) for static code analysis
