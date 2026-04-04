# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/c-family-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/c-family-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/c-family-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/c-family-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/c-family-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/c-family-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/c-family-project.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/c-family-project.md

# C family project

Before starting, read the [Azure Pipelines integration overview](https://app.gitbook.com/s/4FzELVjsPO4ijRo3jtBV/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview "mention") page.

Once you have [Creating and configuring your project](https://app.gitbook.com/s/4FzELVjsPO4ijRo3jtBV/devops-platform-integration/azure-devops-integration/creating-your-project "mention") in SonarQube Cloud, and set up feature integration for your project (see the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page), you can add the SonarQube Cloud analysis to your Azure build pipeline.

In your build pipeline, insert the following steps in the order they appear here. These steps can be interweaved with other steps of your build as long as the following order is followed. All steps have to be executed on the same agent.

To create your Azure build pipeline, you can use either YAML or the Azure Classic interface.

{% hint style="info" %}

* The use of the Classic interface is not always possible (e.g. if your code is stored on GitHub).
* If you use YAML, Sonar can provide you with YAML templates or code examples.
  {% endhint %}

{% hint style="info" %}
Make sure to enable the pull request and branch analysis in your pipeline. See the [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration "mention") page.
{% endhint %}

### Step 1: Make the Build Wrapper available on the build agent. <a href="#make-build-wrapper-available" id="make-build-wrapper-available"></a>

Download and unzip the Build Wrapper on the build agent, as explained below, according to your build agent type. See also the CFamily [Prerequisites](https://app.gitbook.com/s/4FzELVjsPO4ijRo3jtBV/analyzing-source-code/languages/c-family/prerequisites "mention") page. The archive to download and unzip depends on the host’s platform.

<details>

<summary>Microsoft-hosted build agent</summary>

You will need to make the Build Wrapper available on the build agent every time (as part of the build pipeline). To accomplish this, you can add a PowerShell script task (on Windows) or a Bash task (on Linux and macOS) by inserting a Command Line task. See the examples below.

**PowerShell commands on a Windows host**\
`Invoke-WebRequest -Uri 'https://sonarcloud.io/static/cpp/build-wrapper-win-x86.zip' -OutFile 'build-wrapper.zip'`\
`Expand-Archive -Path 'build-wrapper.zip' -DestinationPath '.'`

**Bash commands on a Linux host**\
`curl 'https://sonarcloud.io/static/cpp/build-wrapper-linux-x86.zip' --output build-wrapper.zip`\
`unzip build-wrapper.zip`

**Bash commands on a Linux ARM64 host**\
`curl 'https://sonarcloud.io/static/cpp/build-wrapper-linux-aarch64.zip' --output build-wrapper.zip`\
`unzip build-wrapper.zip`

**Bash commands on a macos host**\
`curl 'https://sonarcloud.io/static/cpp/build-wrapper-macosx-x86.zip' --output build-wrapper.zip`\
`unzip build-wrapper.zip`

</details>

<details>

<summary>Self-hosted build agent</summary>

You can either download it every time (using the same scripts) or only once (as part of the manual setup of your build agent).

</details>

### Step 2: Add a Prepare Analysis Configuration task <a href="#prepare-analysis-config-task" id="prepare-analysis-config-task"></a>

If you want to use a specific scanner version, see the [#specific-scanner-version](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/various-features#specific-scanner-version "mention") article.

<details>

<summary>Using YAML</summary>

Add a SonarQube’s Prepare Analysis Configuration task before your build task. See the YAML file example below.

</details>

<details>

<summary>Using the Classic interface</summary>

In the procedure below, the manual configuration mode is used to define analysis parameters at the pipeline level. You may use the `sonar-project.properties` file instead (or another specified configuration file). For more information, see the [#configuration-mode](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/various-features#configuration-mode "mention") article.

Add a SonarQube’s **Prepare analysis configuration** task and configure it as follows:

1. In SonarQube Cloud Service Endpoint, select the SonarQube Cloud service connection you created in **Adding the SonarQube service connection to your AzDO project**. More information is available on the[azure-devops](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/azure-devops "mention") page.
2. In **Choose the way to run the analysis**, select **Use SonarScanner CLI** (even if you build with *Visual Studio*/*MSBuild*).
3. Select the **Manually provide configuration** mode.
4. In the **Project Key** field, enter your project key.
5. In **Advanced section > Additional properties**, add the following property:
   * key: `sonar.cfamily.compile-commands`
   * Value: the path to the `compile_commands.json` file inside the Build Wrapper output directory: `sonar.cfamily.compile-commands=<output directory>/compile_commands.json`.

</details>

### Step 3: Add a Command Line task to run your build <a href="#add-run-task" id="add-run-task"></a>

For the analysis to happen, your build has to be run through a command line so that it can be wrapped-up by the build-wrapper.

To do so, run **Build wrapper** executable and pass in as the arguments:

1. The output directory configured in the previous task.
2. The command that runs a clean build of your project (not an incremental build): see the command examples below.

**PowerShell commands on a Windows host with an MSBuild build** `build-wrapper-win-x86/build-wrapper-win-x86-64.exe --out-dir <outputDirectory> MSBuild.exe /t:Rebuild`

**Bash commands on a Linux host with a make build** `build-wrapper-linux-x86/build-wrapper-linux-x86-64 --out-dir <outputDirectory> make clean all`

**Bash commands on a Linux ARM64 host with a make build** `build-wrapper-linux-aarch64/build-wrapper-linux-aarch64 --out-dir <outputDirectory> make clean all`

**Example of bash commands on a macos host with a xcodebuild build** `build-wrapper-macosx-x86/build-wrapper-macos-x86 --out-dir <outputDirectory> xcodebuild -project myproject.xcodeproj -configuration Release clean build`

### Step 4: Add a Run code analysis task <a href="#add-run-code-analysis-task" id="add-run-code-analysis-task"></a>

Add a SonarQube’s **Run code analysis** task to run the code analysis and make the results available to SonarQube. Consider running this task right after step 3’s Command line task as the build environment should not be significantly altered before running the analysis.

### Step 5: Add a Publish quality gate result task. <a href="#add-publish-quality-gate-result-task" id="add-publish-quality-gate-result-task"></a>

Add a new SonarQube’s **Publish quality gate result** task.

### YAML file example <a href="#yaml-file-example" id="yaml-file-example"></a>

If you use YAML to create your Azure build pipeline, see the example below and also our [YAML pipeline templates](https://github.com/SonarSource/sonar-scanner-azdo/tree/master/its/fixtures). For information about the SonarQube task inputs, see the [SonarQube tasks for Azure Pipelines](https://app.gitbook.com/s/4FzELVjsPO4ijRo3jtBV/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/sonarqube-tasks "mention") page.

{% hint style="info" %}
Make sure the SonarQube task version used in your YAML file is the correct one.\
For example, in `SonarCloudPrepare@3`, `@3` should correspond to the version of the [sonarcloud-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-azure-devops "mention") you’re using.
{% endhint %}

```yaml
trigger:
- main # or another name representing your main branch
- feature/*

steps:
- checkout: self
  # disable shallow fetch
  fetchDepth: 0

# Make Build Wrapper available
- task: Bash@3
  displayName: Download Build Wrapper
  inputs:
    targetType: inline
    script: |
      curl  'https://sonarcloud.io/static/cpp/build-wrapper-linux-x86.zip' --output build-wrapper.zip
      unzip build-wrapper.zip

# Prepare Analysis Configuration task
- task: SonarCloudPrepare@4
  inputs:
    SonarCloud: '<YourSonarQubeServiceEndpoint>'
    organization: '<YourOrganizationName>'
    scannerMode: 'cli'
    configMode: 'manual'
    cliProjectKey: '<YourProjectKey>'
    extraProperties:  |
      "sonar.cfamily.compile-commands=bw_output/compile_commands.json"

# Command Line task to run your build.
- task: Bash@3
  displayName: Bash Script
  inputs:
    targetType: inline
    script: |
      ./build-wrapper-linux-x86/build-wrapper-linux-x86-64 --out-dir bw_output <Your build command>

# Run Code Analysis task
- task: SonarCloudAnalyze@4

# Publish Quality Gate Result task
- task: SonarCloudPublish@4
  inputs:
    pollingTimeoutSec: '300'
```

### Related pages <a href="#related-pages" id="related-pages"></a>

* [gradle-or-maven-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/gradle-or-maven-project "mention")
* [dotnet-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/dotnet-project "mention")
* [js-ts-go-python-php](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/js-ts-go-python-php "mention")
* [monorepo-projects](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/monorepo-projects "mention")
* [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention")
* [sonarcloud-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-azure-devops "mention")
