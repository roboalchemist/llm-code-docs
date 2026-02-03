# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/dotnet-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/dotnet-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/dotnet-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/dotnet-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/dotnet-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/dotnet-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/dotnet-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/dotnet-project.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/dotnet-project.md

# .NET project

Before starting, read [azure-pipelines-integration-overview](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/azure-pipelines-integration-overview "mention").

Once you have created your project in SonarQube Cloud, set up the project integration with your DevOps platform (see the [devops-platform-integration](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration "mention") pages) and with Azure pipelines (see the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page), you can add the SonarQube Cloud analysis to your Azure build pipeline.

To create your Azure build pipeline, you can use either YAML or the Azure Classic interface.

{% hint style="info" %}

* The use of the Classic interface is not always possible (e.g. if your code is stored on GitHub).
* If you use YAML, Sonar can provide you with YAML templates or code examples.
  {% endhint %}

If you need to use a specific scanner version, see the [various-features](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/various-features "mention") page.

{% hint style="info" %}
Make sure to enable the pull request and branch analysis in your pipeline. See the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page.
{% endhint %}

### About the analysis parameter setup <a href="#analysis-parameters" id="analysis-parameters"></a>

[analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") can be set at different levels. When creating your pipeline, you will have to enter the project key and you may also enter the project version and name. For more information about these task inputs, see the [#task-inputs-specific-to-the-.net-mode](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarqube-tasks#task-inputs-specific-to-the-.net-mode "mention") article. You may define additional parameters in this task. In that case, these parameters have precedence over parameters defined at the project or global level.

### Using YAML <a href="#yaml-pipeline" id="yaml-pipeline"></a>

Add the following SonarQube tasks to your YAML pipeline:

1. Before your build task, add a Prepare Analysis Configuration task.
2. After your build task, add a Run Code Analysis task.
3. After the Run Code Analysis task, add a Publish Quality Gate Result task.

See the YAML file example below. See also our [YAML pipeline templates](https://github.com/SonarSource/sonar-scanner-azdo/tree/master/its/fixtures). For information about the SonarQube task inputs, see the [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention") page.

{% hint style="info" %}
Make sure the SonarQube task version used in your YAML file is the correct one.\
For example, in `SonarCloudPrepare@3`, `@3` should correspond to the version of the [sonarcloud-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-azure-devops "mention") you’re using.
{% endhint %}

<details>

<summary>YAML file example</summary>

```yaml
trigger:
- main # or another name representing your main branch
- feature/*

steps:
 # Checkout the repository 
- checkout: self

 # Disable shallow fetch
  fetchDepth: 0

# Prepare Analysis Configuration task
- task: SonarCloudPrepare@4
  inputs:
    SonarCloud: '<YourSonarQubeServiceEndpoint>'
    organization: '<YourOrganizationName>'
    scannerMode: 'dotnet'
    projectKey: '<YourProjectKey>'

# Dotnet build task
- task: DotNetCoreCLI@2
  displayName: 'dotnet build'

# Run Code Analysis task
- task: SonarCloudAnalyze@4

# Publish Quality Gate Result task
- task: SonarCloudPublish@4
  inputs:
    pollingTimeoutSec: '300'
```

</details>

### Using the Classic interface <a href="#classic-pipeline" id="classic-pipeline"></a>

To add the analysis to your classic build pipeline:

1. In Azure DevOps Classic interface editor, create or update your build pipeline.
2. Add a **Prepare Analysis Configuration** task before your build task:
   * In **SonarQube Server Service Endpoint**, select the SonarQube service connection you created during setup. See the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page for more information about adding a connection.
   * Under **Choose a way to run the analysis**, select **Integrate with .NET**.
   * In the **Project key** field, enter your project key.
   * Optionally, enter the project name and version.
3. Add a new **Run Code Analysis** task after your build task.
4. Add a new **Publish quality gate Result** on your build pipeline summary.
5. Ensure that the pipeline runs automatically for all the branches you want:
   * Under the **Triggers** tab of your pipeline, select **Enable continuous integration** and select all the branches for which you want SonarQube Cloud analysis to run automatically.
6. Save your pipeline.

### Configuring your scanner

If you're using the .NET scanner to complete the analysis, see the [configuring](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/configuring "mention") for NET page for language-specific details.&#x20;

There's also an article about running [#multi-language-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/sonarscanner-for-dotnet/configuring#multi-language-analysis "mention") for select languages when the `sonar.scanner.scanAll` parameter is enabled via the `extraProperties` listed in your [#prepare-analysis-configuration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarqube-tasks#prepare-analysis-configuration "mention").

### .Net guides on the Sonar Community forum <a href="#dotnet-community-guides" id="dotnet-community-guides"></a>

We’ve prepared some guides on the Community Forum to help you with your .NET project.

#### .NET Configuration <a href="#net-configuration" id="net-configuration"></a>

* [Configuration of WarningAsErrors for .NET build](https://community.sonarsource.com/t/configuration-of-warningsaserrors-for-net-build/32393)
* [Investigating the performance of .NET analysis](https://community.sonarsource.com/t/the-sonar-guide-for-investigating-the-performance-of-net-analysis/47279)

#### .NET and Code coverage <a href="#net-and-code-coverage" id="net-and-code-coverage"></a>

* [Generate reports for C# and VB.net](https://community.sonarsource.com/t/coverage-test-data-generate-reports-for-c-vb-net/9871)
* [How to find logs about importing code coverage](https://community.sonarsource.com/t/how-to-find-logs-about-importing-code-coverage/73317)
* [Troubleshooting guide for .NET Code coverage import](https://community.sonarsource.com/t/coverage-troubleshooting-guide-for-net-code-coverage-import/37151)

### Related pages <a href="#related-pages" id="related-pages"></a>

* [gradle-or-maven-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/gradle-or-maven-project "mention")
* [c-family-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/c-family-project "mention")
* [js-ts-go-python-php](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/js-ts-go-python-php "mention")
* [monorepo-projects](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/monorepo-projects "mention")
* [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention")
