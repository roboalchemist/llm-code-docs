# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/gradle-or-maven-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/gradle-or-maven-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/gradle-or-maven-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/gradle-or-maven-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/gradle-or-maven-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/gradle-or-maven-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/gradle-or-maven-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/gradle-or-maven-project.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/gradle-or-maven-project.md

# Gradle or Maven project

Before starting, read [azure-pipelines-integration-overview](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/azure-pipelines-integration-overview "mention").

Once you have created your project in SonarQube Cloud, set up the project integration with your DevOps platform (see the [devops-platform-integration](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration "mention") pages) and with Azure pipelines (see the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page), you can add the SonarQube Cloud analysis to your Azure build pipeline.

To create your Azure build pipeline, you can use either YAML or the Azure Classic interface.

{% hint style="info" %}

* The use of the Classic interface is not always possible (e.g. if your code is stored on GitHub).
* If you use YAML, Sonar can provide you with YAML templates or code examples.
  {% endhint %}

{% hint style="info" %}
Make sure to enable the pull request and branch analysis in your pipeline. See the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page.
{% endhint %}

### About the analysis parameter setup <a href="#analysis-parameters" id="analysis-parameters"></a>

[analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") can be set at different levels. You must define the project key in the Prepare Analysis Configuration task of your pipeline. You may define additional parameters in this task the same way. In that case, these parameters have precedence over parameters defined at the project or global level.

### Using YAML <a href="#yaml-pipeline" id="yaml-pipeline"></a>

1. Add the SonarQube analysis run to your build task.
2. Add the following SonarQube’s tasks:
   * Before your build task, add a Prepare Analysis Configuration task.
   * After your build task, add a Run Code Analysis task.
   * After the Rune Code Analysis task, add a Publish Quality Gate Result task.

{% hint style="info" %}
By default, the scanner version used will be the one specified in your Maven/Gradle build configuration (see the [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention") or [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention") pages). You can overwrite it by using the `sqMavenPluginVersionChoice` or `sonarQubeGradlePluginVersion` input in your pipeline’s Execute build task.
{% endhint %}

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
    scannerMode: 'other'
    extraProperties: 'sonar.projectKey=<YourProjectKey>'

# If you use Gradle: add the Execute Gradle build as shown below
- task: Gradle@3
   inputs:
      sonarQubeRunAnalysis: true

# If you use Maven: add the Execute Maven goal as shown below
 - task: Maven@4
      inputs:
      sonarQubeRunAnalysis: true

# Publish Quality Gate Result task
- task: SonarCloudPublish@4
  inputs:
    pollingTimeoutSec: '300'
```

</details>

### Using the Classic interface <a href="#classic-pipeline" id="classic-pipeline"></a>

1\. In Azure DevOps’ Classic interface editor, create or update your build pipeline.

2\. Add a **Prepare Analysis Configuration** task before your build task:

* In **SonarQube Server Service Endpoint**, select the SonarQube service connection you created during setup. See the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page for more information about adding a connection.
* Under **Choose a way to run the analysis**, select **Integrate with Maven or Gradle**.
* Expand the **Advanced** section and replace the **Additional Properties** with the following snippet:

```properties
# Additional properties that will be passed to the scanner,
# Put one key=value per line, example:
# sonar.exclusions=**/*.bin
sonar.projectKey=YourProjectKey
```

3\. Add a new Maven or Gradle task:

* Under **Code Analysis**, check **Run SonarQube or SonarCloud Analysis.**

4\. Add a new **Publish quality gate result** task on your build pipeline summary.

5\. Ensure that the pipeline runs automatically for all the branches you want: Under the **Triggers** tab of your pipeline, select **Enable continuous integration** and select all the branches for which you want SonarQube Cloud analysis to run automatically.

6\. Save your pipeline.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [dotnet-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/dotnet-project "mention")
* [c-family-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/c-family-project "mention")
* [js-ts-go-python-php](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/js-ts-go-python-php "mention")
* [monorepo-projects](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/monorepo-projects "mention")
* [quality-gate-status-in-release-pipeline](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/quality-gate-status-in-release-pipeline "mention")
* [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention")
