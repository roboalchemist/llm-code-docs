# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/various-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/various-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/various-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/various-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/various-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/various-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/various-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/various-features.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/various-features.md

# Using various features

This page explains features you may use when adding SonarQube analysis to your Azure build pipeline:

* Choosing the analysis configuration mode (only in the Standalone SonarScanner CLI mode).
* Using a specific version of the SonarScanner for .NET or CLI
* Using the cache feature

### Choosing the configuration mode <a href="#configuration-mode" id="configuration-mode"></a>

In the CLI mode of the Azure DevOps extension for SonarQube Server, you may:

* Either use the file configuration mode (default mode) which consists of setting analysis parameters in the `sonar-project.properties` file stored in the repository root (or another specified configuration file).
* Or use the manual configuration mode to define analysis parameters at the pipeline level.

{% hint style="info" %}
If you use the manual configuration mode, the scanner still checks the `sonar-project.properties` file. Parameters set through the manual configuration mode have precedence over parameters set in the `sonar-project.properties` file.
{% endhint %}

<details>

<summary>Using the file configuration mode</summary>

The file configuration mode is the default mode of the Azure DevOps extension for SonarQube.

**YAML pipeline for file configuration**

1. Make sure the `configMode` input of the `SonarQubePrepare` task is set to `file`.
2. To use a different configuration file than `sonar-project.properties`, add the `configFile` task input to the `SonarQubePrepare` task, with the path to the configuration file as the value. The path can be absolute, or relative to the repository root.

**Classic pipeline for file configuration**

In the Prepare Analysis Configuration task:

1. Make sure the **Store configuration with my source code** mode is selected.
2. In **Settings file**, you can define a different configuration file than `sonar-project.properties`. The path can be absolute, or relative to the repository root.

<div align="left"><figure><img src="broken-reference" alt="Select Store configuration with my source code"><figcaption></figcaption></figure></div>

</details>

<details>

<summary>Using the manual configuration mode</summary>

To define analysis parameters at the pipeline level in Standalone SonarScanner CLI mode, proceed as described below.

**YAML pipeline for manual configuration**

1. Make sure the `configMode` task input in the `SonarQubePrepare` task is set to `manual`.
2. Use the `extraProperties` task input in the `SonarQubePrepare` task to define the analysis parameters: define a new sonar property by adding `<propertyKey>=<propertyValue>` on a new line.

**Classic pipeline for manual configuration**

In the Prepare Analysis Configuration task:

1\. Select the **Manually provide configuration** mode and enter the required parameters.

<div align="left"><figure><img src="broken-reference" alt="Select the Manually provide configuration mode"><figcaption></figcaption></figure></div>

2\. In **Advanced section** > **Additional properties**, define a new sonar property by adding `<propertyKey>=<propertyValue>` on a new line.\
**Example**: `sonar.exclusions=**/*.bin`

</details>

For information about the required settings in the `SonarQubePrepare` task for either configuration mode, see the [#prepare-analysis-configuration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarqube-tasks#prepare-analysis-configuration "mention") article.

### Using a specific version of SonarScanner for .NET or CLI <a href="#specific-scanner-version" id="specific-scanner-version"></a>

The Azure DevOps extension for SonarQube Cloud embeds the latest compatible version of the SonarScanner for .NET and SonarScanner CLI. In very particular situations, you may want to use another scanner version. In such a case, you can configure the download of this specific version from the Sonar binaries site. In addition, you can use the Azure cache task (see below) in your pipeline to manage the caching of the SonarScanner.

The figure below shows the download process of a specific version of SonarScanner for .NET or SonarScanner CLI.

<figure><img src="broken-reference" alt="Download process of a specific version of SonarScanner for .NET or SonarScanner CLI"><figcaption></figcaption></figure>

Set up the download in the Prepare Analysis Configuration task of your pipeline as described below.

<details>

<summary>SonarScanner for .NET</summary>

You must specify the full version number, such as 10.1.2.114627 (and not 10.1.2). All of the available version numbers can be found [here](https://github.com/SonarSource/sonar-scanner-msbuild/tags).

**YAML pipeline to specify .NET scanner version**

Add the following input to the Prepare Analysis Configuration task:

* `dotnetScannerVersion`: The SonarScanner for .NET version to be downloaded.

The code snippet below shows a task configuration example. For more information about the task inputs, see the [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention") page.

```yaml
- task: SonarCloudPrepare@4
  inputs:
    SonarQube: '<YourSonarQubeServerEndpoint>'
    organization: '<YourOrganizationName>'
    scannerMode: 'dotnet'
    dotnetScannerVersion: '10.1.2.114627'
    projectKey: '<YourProjectKey>'
```

**Classic pipeline**

In **Scanner Version**, enter the version to be downloaded.

</details>

<details>

<summary>SonarScanner CLI</summary>

You must specify the full version number, such as 7.1.0.4889 (and not 7.1.0). All of the available version numbers can be found [here](https://github.com/SonarSource/sonar-scanner-cli/tags).

**YAML pipeline to specify CLI scanner version**

Add the following input to the Prepare Analysis Configuration task

* `cliScannerVersion`: The SonarScanner CLI version to be downloaded.

The code snippet below shows a task configuration example. For more information about the task inputs, see the [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention") page.

```yaml
- task: SonarCloudPrepare@4
  inputs:
    SonarQube: '<YourSonarQubeServiceEndpoint>'
    organization: '<YourOrganizationName>'
    scannerMode: 'cli'
    configMode: 'file'
    configFile: '<YourConfig.properties>'   
    cliScannerVersion: '7.1.0.4889'
    cliProjectKey: '<YourProjectKey>'
    cliSources: '.' 
```

**Classic pipeline**

In **Scanner CLI Version**, enter the version to be downloaded.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-484d0ad987af7d22b97f5cec5354436b27346171%2F46ca4aa974c5164f683c20b1ae49f3617f71ceba.png?alt=media" alt="When specifying a specific version of the SonarScanner CLI, select Use standalone SonarScanner CLI when setting up your pipeline, and give it the full version number." width="501"><figcaption></figcaption></figure></div>

</details>

### Using the cache feature <a href="#cache-feature" id="cache-feature"></a>

Azure DevOps allows [pipeline caching](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/caching?view=azure-devops) to improve build performance by facilitating the download of dependencies between pipeline runs. Currently, you can only cache the SonarScanner (bootstrapper) that is downloaded when you need a specific version of SonarScanner for .NET or CLI.

Proceed as follows:

* Add a [cache task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/cache-v2?view=azure-pipelines) to your Azure build pipeline before SonarQube’s **Prepare Analysis Configuration** task. See the code snippet below according to the extension mode.

<details>

<summary>.NET</summary>

```yaml
- task: Cache@2
  displayName: Cache SonarScanner
  inputs:
    key: '"SonarScanner" | ".NET" | "$(Agent.OS)"'
    path: '$(Agent.ToolsDirectory)/SonarScanner .NET
```

</details>

<details>

<summary>CLI</summary>

```yaml
- task: Cache@2
  displayName: Cache SonarScanner
  inputs:
    key: '"SonarScanner" | "CLI" | "$(Agent.OS)"'
    path: '$(Agent.ToolsDirectory)/SonarScanner CLI'
```

</details>

### Adding the quality gate status widget to your project <a href="#adding-quality-gate-widget" id="adding-quality-gate-widget"></a>

You can monitor the quality gate status of your projects directly in your Azure DevOps dashboard. Follow these steps to configure your widget:

1. Once the Azure DevOps extension is installed and your project has been successfully analyzed, go to one of your Azure DevOps dashboards (or create a new dashboard). Click on the **Pen** icon to edit, and then select **Add Widget**.
2. In the **Add Widget** list, select **Code Quality**, and then select **Add**. An empty **Configure widget** is added to your dashboard.
3. Select the widget’s **Cogwheel** icon to configure it.
   * *For public projects,* you can simply select your project from the dropdown. A search bar inside the drop-down will help you find it easily. Just select it and **Save**.
   * *For private projects*, log in using the links provided under the drop-down. Once logged in, your private projects will appear in the drop-down. Select the project you are interested in and **Save**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [gradle-or-maven-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/gradle-or-maven-project "mention")
* [dotnet-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/dotnet-project "mention")
* [c-family-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/c-family-project "mention")
* [js-ts-go-python-php](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/js-ts-go-python-php "mention")
* [monorepo-projects](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/monorepo-projects "mention")
* [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention")
