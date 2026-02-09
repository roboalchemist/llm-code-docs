# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/js-ts-go-python-php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/js-ts-go-python-php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/js-ts-go-python-php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/js-ts-go-python-php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/js-ts-go-python-php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/js-ts-go-python-php.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/js-ts-go-python-php.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/js-ts-go-python-php.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/js-ts-go-python-php.md

# JS, TS, Go, Python, PHP, etc. project

This page explains how to add the SonarQube Cloud analysis to your Azure build pipeline for projects that are not Maven, Gradle, .NET, or C family projects.

Before starting, read the [azure-pipelines-integration-overview](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/azure-pipelines-integration-overview "mention") page.

Once you have created your project in SonarQube Cloud, set up the project integration with your DevOps platform (see the [devops-platform-integration](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration "mention") pages) and with Azure pipelines (see the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page), you can add the SonarQube Cloud analysis to your Azure build pipeline.

To create your Azure build pipeline, you can use either YAML or the Azure Classic interface.

{% hint style="info" %}

* The use of the Classic interface is not always possible (e.g. if your code is stored on GitHub).
* If you use YAML, Sonar can provide you with YAML templates or code examples.
  {% endhint %}

If you need to use a specific scanner version, see the [#specific-scanner-version](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/various-features#specific-scanner-version "mention") article for instructions.

{% hint style="info" %}
Make sure to enable the pull request and branch analysis in your pipeline. Instructions are on the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page.
{% endhint %}

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

<pre class="language-yaml"><code class="lang-yaml"><strong>trigger:
</strong>- main # or another name representing your main branch
- feature/*

steps:
 # Checkout the repository
 - checkout: self
 
 # Disable shallow fetch
   fetchDepth: 0

# Prepare Analysis Configuration task
- task: SonarCloudPrepare@4
  inputs:
    SonarCloud: '&#x3C;YourSonarQubeServiceEndpoint>'
    organization: '&#x3C;YourOrganizationName>'
    scannerMode: 'cli'
    configMode: 'manual'
    cliProjectKey: '&#x3C;YourProjectKey>'

# Add your build task(s) here

# Run Code Analysis task
- task: SonarCloudAnalyze@4
  inputs:
    jdkversion: 'JAVA_HOME_17_X64'

# Publish Quality Gate Result task
- task: SonarCloudPublish@4
  inputs:
    pollingTimeoutSec: '300'
</code></pre>

</details>

### Using the Classic interface <a href="#classic-pipeline" id="classic-pipeline"></a>

In the procedure below, the manual configuration mode is used to define analysis parameters at the pipeline level. You may use the `sonar-project.properties` file instead (or another specified configuration file). For more information, see the [various-features](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/various-features "mention") page.

Proceed as follows:

1. In Azure DevOps’ Classic interface editor, create or edit your build pipeline.
2. Add a **Prepare Analysis Configuration** task before your build task:
   * In **SonarQube Server Service Endpoint**, select the SonarQube service connection you created during setup. See the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page for more information about adding a connection.
   * Under **Choose a way to run the analysis**, select **Use Standalone SonarScanner CLI**.
   * Select the **Manually provide configuration** mode.
   * In the **Project key** field, enter your project key.
3. Add a new **Run Code Analysis** task after your build task.
4. Add a new **Publish quality gate Result** on your build pipeline summary.
5. Ensure that the pipeline runs automatically for all the branches you want:
   * Under the **Triggers** tab of your pipeline, select **Enable continuous integration** and select all the branches for which you want SonarQube Cloud analysis to run automatically.
6. Save your pipeline.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention")
* [gradle-or-maven-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/gradle-or-maven-project "mention")
* [dotnet-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/dotnet-project "mention")
* [c-family-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/c-family-project "mention")
* [monorepo-projects](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/monorepo-projects "mention")
* [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention")
