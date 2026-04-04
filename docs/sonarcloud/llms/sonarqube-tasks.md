# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/sonarqube-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/sonarqube-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/sonarqube-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/sonarqube-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/sonarqube-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/sonarqube-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/sonarqube-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/sonarqube-tasks.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks.md

# List of SonarQube tasks

Examples of each SonarQube task described on this page can be found in code samples located on pages in this section of the docs. Select your project type from the pages listed on the [adding-analysis-to-build-pipeline](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline "mention") page, then read through the setup instructions to locate the example pipeline to reference.

For more information about customizing your Azure pipeline with the task inputs listed below, please see the [various-features](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/various-features "mention") page.

### Prepare Analysis Configuration task <a href="#prepare-analysis-configuration" id="prepare-analysis-configuration"></a>

This task configures the required settings before executing the build. For .NET solutions or Java projects, it helps integrate seamlessly with MSBuild, Maven, and Gradle tasks.

The Prepare Analysis Configuration task shows up in your Azure pipeline as task: `SonarCloudPrepare@X`&#x20;

* where `X` = the current version of the [sonarcloud-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-azure-devops "mention") for SonarQube Cloud.

<details>

<summary>Task inputs common to all modes</summary>

The table below lists the **Prepare Analysis Configuration** task inputs common to all modes of the Azure DevOps extension for SonarQube Cloud.

<table><thead><tr><th width="186.07421875">Task input</th><th width="397.51171875">Description</th><th>Required in YAML file</th></tr></thead><tbody><tr><td><code>SonarCloud</code></td><td>Name of the SonarQube service connection(s) (SonarQube Service Endpoint) to your Azure DevOps project. See the <a data-mention href="../setting-up-project-integration#adding-sonarqube-service-connection">#adding-sonarqube-service-connection</a> article for more details.</td><td><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt=""></td></tr><tr><td><code>scannerMode</code></td><td><p>The running mode of the Azure DevOps extension for SonarQube Cloud.</p><p>Possible values:</p><p>• dotnet: .NET mode, for .NET projects.</p><p>• other: Maven / Gradle mode, for Maven and Gradle projects.</p><p>• cli: CLI mode, for other projects.</p></td><td><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt=""></td></tr></tbody></table>

</details>

<details>

<summary>Task inputs specific to the Maven / Gradle mode</summary>

The table below lists the **Prepare Analysis Configuration** task inputs specific to the Maven / Gradle mode of the Azure DevOps Extension for SonarQube Cloud.

<table><thead><tr><th width="185.90234375">Task input</th><th width="398.05078125">Description</th><th>Required in YAML file</th></tr></thead><tbody><tr><td><code>extraProperties</code></td><td><p>Additional sonar properties to be passed to the scanner. A property is defined through a [key, value] pair.</p><p><strong>Format</strong>: One [key, value] pair per line as follows:<br><code>&#x3C;key>=&#x3C;value></code><br>For example: <code>sonar.exclusions=**/*.bin</code></p></td><td><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt=""> (to set the project key)</td></tr></tbody></table>

</details>

<details>

<summary>Task inputs specific to the .NET mode</summary>

The table below lists the **Prepare Analysis Configuration** task inputs specific to the .NET mode of the Azure DevOps extension for SonarQube Cloud. The **Corresponding sonar property** column indicates the sonar property that SonarQube Cloud will set with the input value. See the sonar property description in [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") for more information on the possible values and default-from-build values.

<table><thead><tr><th width="185.90234375">Task input</th><th width="211.59765625">Description</th><th width="186.08203125">Corresponding sonar property</th><th>Required in YAML file</th></tr></thead><tbody><tr><td><code>projectKey</code></td><td><p>• If the project exists already in SonarQube Cloud (It is highly recommended to create your project first: see Creating your project): the project’s unique key (is displayed in SonarQube UI).</p><p>• If the project doesn’t exist yet in SonarQube Cloud, it will be created with this key. Allowed characters are letters, numbers, -, _, ., and :, with at least one non-digit.</p></td><td><code>sonar.projectKey</code></td><td><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt=""></td></tr><tr><td><code>projectName</code></td><td><p>The name of the SonarQube Cloud project that will be displayed on the web interface.</p><p><strong>Default</strong>: <code>projectKey</code> input value (if no default-from-build value applies).</p></td><td><code>sonar.projectName</code></td><td><br></td></tr><tr><td><code>projectVersion</code></td><td>The version of the SonarQube Cloud project.</td><td><code>sonar.projectVersion</code></td><td><br></td></tr><tr><td><code>dotnetScannerVersion</code></td><td><p>The version of the SonarScanner for .NET to be downloaded; see the <a data-mention href="../adding-analysis-to-build-pipeline/various-features#specific-scanner-version">#specific-scanner-version</a>article for more details.</p><p><strong>Default</strong>: The extension’s default version of the SonarScanner for .NET (the latest compatible version).</p></td><td><br></td><td><br></td></tr><tr><td><code>extraProperties</code></td><td><p>Additional sonar properties to be passed to the scanner. A property is defined through a [key, value] pair.</p><p><strong>Format</strong>: One [key, value] pair per line as follows:<br><code>&#x3C;key>=&#x3C;value></code><br>For example: <code>sonar.scanner.scanAll=false</code></p></td><td></td><td></td></tr></tbody></table>

</details>

<details>

<summary>Task inputs specific to the CLI mode</summary>

The table below lists the **Prepare Analysis Configuration** task inputs specific to the CLI mode of the Azure DevOps Extension for SonarQube Cloud. The **Corresponding sonar property** column indicates the sonar property that SonarQube Cloud will set with the input value. See the sonar property description found on the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about the possible values and default-from-build values.

<table><thead><tr><th width="186.00390625">Task input</th><th width="211.5390625">Description</th><th width="185.87109375">Corresponding sonar property</th><th>Required in YAML file</th></tr></thead><tbody><tr><td><code>cliSources</code></td><td><p>The path to the root directory containing source files. The path can be absolute, or relative to the repository root.</p><p><strong>Warning</strong>: The possible values are different from the <code>sonar.sources</code> property:</p><p>• You can only set a single path.</p><p>• The relative path must be relative to the repository root (and not the to the sonar.projectBaseDir property).</p><p>• If you want to set a list of paths, define instead sonar.sources in the extraProperties input or in sonar-project.properties (See Choosing your configuration mode)</p><p><strong>Default</strong>: <strong>.</strong></p></td><td><code>sonar.sources</code></td><td><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt=""></td></tr><tr><td><code>configMode</code></td><td><p>Specifies the configuration mode.</p><p>Possible values:</p><p>• file (default): The configuration is stored in the file defined through the configFile input.</p><p>• manual: The configuration is defined through the extraProperties input.</p></td><td><br></td><td><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt=""></td></tr><tr><td><code>cliScannerVersion</code></td><td><p>Version of the SonarScanner CLI to be downloaded; see the <a data-mention href="../adding-analysis-to-build-pipeline/various-features#specific-scanner-version">#specific-scanner-version</a>article for more details.</p><p><strong>Default</strong>: The extension’s default version of the SonarScanner CLI (the last available version).</p></td><td><br></td><td><br></td></tr><tr><td><code>configFile</code></td><td><p>Is used if <code>configMode</code>is set to <code>file</code>.<br>The path to the file containing your analysis configuration. Path can be absolute or relative to the repository root.</p><p><strong>Default</strong>: sonar-project.properties</p></td><td><br></td><td><br></td></tr><tr><td><code>cliProjectKey</code></td><td><p>Is used if <code>configMode</code> is set to <code>manual</code>.</p><p>• If the project exists already in SonarQube Cloud (It is highly recommended to create your project first: see Creating your project): the project’s unique key (is displayed in SonarQube UI).</p><p>• If the project doesn’t exist yet in SonarQube Cloud, it will be created with this key. Allowed characters are letters, numbers, -, _, ., and :, with at least one non-digit.</p></td><td><code>sonar.projectKey</code></td><td><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-51435de4153f60f46883a8cb66af53e3ff29d70c%2Fgreen-check.svg?alt=media" alt=""></td></tr><tr><td><code>cliProjectName</code></td><td><p>Is used if <code>configMode</code> is set to <code>manual</code>.</p><p>The name of the SonarQube Cloud project that will be displayed on the web interface.</p><p><strong>Default</strong>: <code>cliProjectKey</code> input value (if no default-from-build value applies).</p></td><td><code>sonar.projectName</code></td><td><br></td></tr><tr><td><code>cliProjectVersion</code></td><td>Is used if <code>configMode</code> is set to <code>manual</code>.<br>The version of the SonarQube Cloud project.</td><td><code>sonar.projectVersion</code></td><td><br></td></tr><tr><td><code>extraProperties</code></td><td><p>Is used if <code>configMode</code> is set to <code>manual</code>.</p><p>Additional sonar properties to be passed to the scanner. A property is defined through a [key, value] pair.</p><p><strong>Format</strong>: One [key, value] pair per line as follows:<br><code>&#x3C;key>=&#x3C;value></code><br>For example: <code>sonar.exclusions=**/*.bin</code></p></td><td><br></td><td><br></td></tr></tbody></table>

</details>

### Run Code Analysis task <a href="#run-code-analysis" id="run-code-analysis"></a>

This task executes the analysis of the source code. It is not used in the Gradle / Maven mode of the Azure DevOps Extension for SonarQube Cloud.

The Run Code Analysis task shows up in your Azure pipeline as task: `SonarCloudAnalyze@X`&#x20;

* where `X` = the current version of the [sonarcloud-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-azure-devops "mention") for SonarQube Cloud.

The table below lists the task inputs.

| Task input                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><code>jdkversion</code></p><p><br></p> | <p>The version of Java used by the scanner for analysis.</p><p>If you select a value other than JAVA\_HOME, the analyze task will revert to using JAVA\_HOME if the selected environment variable does not exist.</p><p>Possible values:</p><p>• JAVA\_HOME: Use the value of the JAVA\_HOME environment variable on the system.</p><p>• JAVA\_HOME\_17\_X64: Use the value of the JAVA\_HOME\_17\_X64 environment variable on the system, if available. This environment variable is already set when running on Microsoft-hosted agents.</p><p>• JAVA\_HOME\_21\_X64: Use the value of the JAVA\_HOME\_17\_X64 environment variable on the system. This environment variable is already set when running on Microsoft-hosted agents.</p><p><strong>Default</strong>: <code>JAVA\_HOME</code></p> |

### Publish Quality Gate Result task <a href="#publish-quality-gate-result" id="publish-quality-gate-result"></a>

This task allows you to report the quality gate status directly to your Azure Pipeline’s Build Summary page. It is not mandatory but highly recommended.

{% hint style="info" %}
The Publish Quality Gate Result task can significantly increase the overall build time because it will poll SonarQube until the analysis is complete.
{% endhint %}

The Publish Quality Gate Result task shows up in your Azure pipeline as task: `SonarCloudPublish@X`&#x20;

* where `X` = the current version of the [sonarcloud-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-azure-devops "mention") for SonarQube Cloud.

The table below lists the task inputs.

| Task input          | Description                                                                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `pollingTimeoutSec` | <p>The maximum time (in seconds) for the task to wait for the analysis results sent by SonarQube Cloud.</p><p><strong>Default</strong>: 300</p> |

### Related pages <a href="#related-pages" id="related-pages"></a>

* [gradle-or-maven-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/gradle-or-maven-project "mention")
* [dotnet-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/dotnet-project "mention")
* [c-family-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/c-family-project "mention")
* [js-ts-go-python-php](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/js-ts-go-python-php "mention")
* [monorepo-projects](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/monorepo-projects "mention")
