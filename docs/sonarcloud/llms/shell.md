# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/shell.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/shell.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/shell.md

# Shell

### Language-specific properties

You can discover and update the Shell-specific [properties](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters) in: **Administration** > **General Settings** > **Languages** > **Shell.**

### Supported languages and syntaxes

The analyzer is designed to analyze Bash and POSIX shell scripts, which are the only officially supported shell flavors.

However, analysis for other shell flavors (e.g. `ksh`, `zsh`) is also possible. This support is partial, and the analyzer will perform best on scripts that use syntax compatible with or similar to POSIX and Bash. You may encounter parsing errors when analyzing scripts that rely on features or syntaxes specific to other shells. This may lead to raising issues unrelated to your shell flavor.

### Troubleshooting

**Some files are not analyzed or issues are missing**

The Shell analyzer processes files in size-based batches, and each batch is given an adaptive timeout to ensure the overall project analysis completes in a timely manner. If you notice that some files are not being analyzed or issues are missing, it is likely that one or more of these batches has timed out. When a batch times out, the analysis of files within that specific batch is skipped, and the scan continues with the next batch.

You can increase the baseline timeout value, which gives each batch more time to complete. This property can be adjusted in the UI:

1. Go to **Administration** > **General Settings** > **Declarative Rule Engine**.
2. Find the `sonar.dre.baselineTimeout` property and increase its value.

The property can be specified during the scanner invocation as well.
