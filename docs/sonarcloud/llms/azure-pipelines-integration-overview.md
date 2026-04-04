# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/azure-pipelines-integration-overview.md

# Azure Pipelines integration overview

The Azure DevOps extension for SonarQube Cloud is used to manage the integration of SonarQube Cloud with Azure Pipelines. It allows:

* Integrating smoothly SonarQube analysis into your Azure build pipeline. This includes multi-branch analysis features.
* Reporting the analysis’ quality gate status right in Azure Pipeline’s Build Summary page.
* Checking the SonarQube quality gate status in your Azure release pipeline.
* Monitoring the quality gate status of your projects directly in your Azure DevOps dashboard with the quality gate status widget.

### Extension modes <a href="#extension-modes" id="extension-modes"></a>

The Azure DevOps extension for SonarQube Cloud can run in one of the following modes depending on your project type:

* **.NET**: for .NET projects. The [sonarscanner-for-dotnet](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet "mention") is used.
* **Maven or Gradle**: for Maven and Gradle projects. The [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention") or [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention") is used, respectively.
* **CLI**: for the other project types (C family, JavaScript, TypeScript, Go, Python, PHP, etc.). The [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention") is used.

The Azure DevOps extension for SonarQube Cloud embeds the last compatible version of the SonarScanner for .NET and SonarScanner CLI, which is used by default.

In Maven/Gradle mode, your build task downloads the SonarScanner for Maven or Gradle from the Sonar binaries site.

{% hint style="info" %}
In very particular situations, you may not want to use the extension’s default version but a specific previous version of the SonarScanner for .NET or CLI. In such a case, you can configure your Azure build pipeline to download this specific version from the Sonar binaries site (see [various-features](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/various-features "mention")).
{% endhint %}

### SonarQube tasks used in the pipeline definition <a href="#sonarqube-tasks" id="sonarqube-tasks"></a>

The SonarQube Cloud analysis is integrated into your Azure build pipeline by adding the following SonarQube tasks to your build pipeline definition:

* Prepare Analysis Configuration
* Run Code Analysis\
  This task starts the SonarScanner for .NET or CLI. In the Maven/Gradle mode, it is replaced by a Maven or Gradle task that downloads the SonarScanner for Maven or Gradle, respectively.
* Publish Quality Gate Result\
  With this task, the quality gate status and a link to SonarQube Cloud are shown in the Azure Pipeline’s Build Summary page.

### Analysis process overview <a href="#analysis-process-overview" id="analysis-process-overview"></a>

The figure below shows the analysis’s main steps with the example of a .NET project :

1. The **Prepare Analysis Configuration** task starts the Begin step: the SonarScanner for .NET prepares the analysis by gathering all of the parameters and resources needed to analyze your project.
2. The rules configured in your SonarQube quality profile are run during the build step. The SonarScanner for .NET collects the analysis data while your project is being built.
3. The **Run Code Analysis** task starts the End step: the SonarScanner for .NET collects and prepares the analysis results which will be sent to SonarQube.
4. The SonarScanner for .NET sends the analysis results to SonarQube for further processing.
5. SonarQube sends the quality gate status to Azure DevOps where it can be used in your pipeline through the **Publish Quality Gate Result** task.

<figure><img src="broken-reference" alt="The SonarScanner for .NET is invoked twice during the build pipeline in Azure DevOps."><figcaption></figcaption></figure>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [gradle-or-maven-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/gradle-or-maven-project "mention")
* [dotnet-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/dotnet-project "mention")
* [c-family-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/c-family-project "mention")
* [js-ts-go-python-php](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/js-ts-go-python-php "mention")
* [monorepo-projects](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/monorepo-projects "mention")
* [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention")
