# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops

Title: Continuously update function app code using Azure Pipelines

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops

Markdown Content:
Use [Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/) to automatically deploy your code project to a function app in Azure. Azure Pipelines lets you build, test, and deploy with continuous integration (CI) and continuous delivery (CD) using [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/).

YAML pipelines are defined using a YAML file in your repository. A step is the smallest building block of a pipeline and can be a script or task (prepackaged script). [Learn about the key concepts and components that make up a pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/key-pipelines-concepts).

You use the `AzureFunctionApp` task to deploy your code. There are now two versions of `AzureFunctionApp`, which are compared in this table:

| Comparison/version | [AzureFunctionApp@2](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/azure-function-app-v2) | [AzureFunctionApp@1](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/azure-function-app-v1) |
| --- | --- | --- |
| Supports the [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan) | ✔ | ❌ |
| Includes enhanced validation support* | ✔ | ❌ |
| When to use... | Recommended for new app deployments | Maintained for legacy deployments |

* Enhanced validation support makes pipelines less likely to fail because of errors.

Choose your task version at the top of the article.

Note

Upgrade from `AzureFunctionApp@1` to `AzureFunctionApp@2` for access to new features and long-term support.

*   An Azure DevOps organization. If you don't have one, you can [create one for free](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/pipelines-sign-up). If your team already has one, then make sure you're an administrator of the Azure DevOps project that you want to use.

*   An ability to run pipelines on Microsoft-hosted agents. You can either purchase a [parallel job](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs) or you can request a free tier.

*   If you plan to use GitHub instead of Azure Repos, you also need a GitHub repository. If you don't have a GitHub account, you can [create one for free](https://github.com/).

*   An existing function app in Azure that has its source code in a supported repository. If you don't yet have an Azure Functions code project, you can create one by completing the following language-specific article:

Remember to upload the local code project to your GitHub or Azure Repos repository after you publish it to your function app.

1.   Sign in to your Azure DevOps organization and navigate to your project.
2.   In your project, navigate to the **Pipelines** page. Then choose the action to create a new pipeline.
3.   Walk through the steps of the wizard by first selecting **GitHub** as the location of your source code.
4.   You might be redirected to GitHub to sign in. If so, enter your GitHub credentials.
5.   When the list of repositories appears, select your sample app repository.
6.   Azure Pipelines will analyze your repository and recommend a template. Select **Save and run**, then select **Commit directly to the main branch**, and then choose **Save and run** again.
7.   A new run is started. Wait for the run to finish.

The following language-specific pipelines can be used for building apps.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_2_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_2_javascript)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_2_python)
*   [PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_2_powershell)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_2_java)

You can use the following sample to create a YAML file to build a .NET app:

```
pool:
  vmImage: 'windows-latest'
steps:
  - task: UseDotNet@2
    displayName: 'Install .NET 8.0 SDK'
    inputs:
      packageType: 'sdk'
      version: '8.0.x'
      installationPath: $(Agent.ToolsDirectory)/dotnet
  - script: |
      dotnet restore
      dotnet build --configuration Release
  - task: DotNetCoreCLI@2
    displayName: 'dotnet publish'
    inputs:
      command: publish
      arguments: '--configuration Release --output $(System.DefaultWorkingDirectory)/publish_output'
      projects: 'csharp/*.csproj'
      publishWebProjects: false
      modifyOutputPath: false
      zipAfterPublish: false
  - task: ArchiveFiles@2
    displayName: "Archive files"
    inputs:
      rootFolderOrFile: "$(System.DefaultWorkingDirectory)/publish_output"
      includeRootFolder: false
      archiveFile: "$(System.DefaultWorkingDirectory)/build$(Build.BuildId).zip"
  - task: PublishBuildArtifacts@1
    inputs:
      PathtoPublish: '$(System.DefaultWorkingDirectory)/build$(Build.BuildId).zip'
      artifactName: 'drop'
```

1.   Sign in to your Azure DevOps organization and navigate to your project.
2.   In your project, navigate to the **Pipelines** page. Then select **New pipeline**.
3.   Select one of these options for **Where is your code?**: 
    *   **GitHub**: You might be redirected to GitHub to sign in. If so, enter your GitHub credentials. When this connection is your first GitHub connection, the wizard also walks you through the process of connecting DevOps to your GitHub accounts.
    *   **Azure Repos Git**: You're immediately able to choose a repository in your current DevOps project.

4.   When the list of repositories appears, select your sample app repository.
5.   Azure Pipelines analyzes your repository and in **Configure your pipeline** provides a list of potential templates. Choose the appropriate **function app** template for your language. If you don't see the correct template select **Show more**.
6.   Select **Save and run**, then select **Commit directly to the main branch**, and then choose **Save and run** again.
7.   A new run is started. Wait for the run to finish.

The following language-specific pipelines can be used for building apps.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_3_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_3_javascript)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_3_python)
*   [PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_3_powershell)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_3_java)

You can use the following sample to create a YAML file to build a .NET app.

If you see errors when building your app, verify that the version of .NET that you use matches your Azure Functions version. For more information, see [Azure Functions runtime versions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions).

```
pool:
  vmImage: 'windows-latest'
steps:
  - task: UseDotNet@2
    displayName: 'Install .NET 8.0 SDK'
    inputs:
      packageType: 'sdk'
      version: '8.0.x'
      installationPath: $(Agent.ToolsDirectory)/dotnet
  - script: |
      dotnet restore
      dotnet build --configuration Release
  - task: DotNetCoreCLI@2
    displayName: 'dotnet publish'
    inputs:
      command: publish
      arguments: '--configuration Release --output $(System.DefaultWorkingDirectory)/publish_output'
      projects: 'csharp/*.csproj'
      publishWebProjects: false
      modifyOutputPath: false
      zipAfterPublish: false
  - task: ArchiveFiles@2
    displayName: "Archive files"
    inputs:
      rootFolderOrFile: "$(System.DefaultWorkingDirectory)/publish_output"
      includeRootFolder: false
      archiveFile: "$(System.DefaultWorkingDirectory)/build$(Build.BuildId).zip"
  - task: PublishBuildArtifacts@1
    inputs:
      PathtoPublish: '$(System.DefaultWorkingDirectory)/build$(Build.BuildId).zip'
      artifactName: 'drop'
```

You'll deploy with the [Azure Function App Deploy v2](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/azure-function-app-v2) task. This task requires an [Azure service connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints) as an input. An Azure service connection stores the credentials to connect from Azure Pipelines to Azure. You should create a connection that uses [workload identity federation](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/connect-to-azure#create-an-azure-resource-manager-service-connection-that-uses-workload-identity-federation).

To deploy to Azure Functions, add this snippet at the end of your `azure-pipelines.yml` file, depending on whether your app runs on Linux or Windows:

*   [Windows App](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_4_windows)
*   [Linux App](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_4_linux)

```
trigger:
- main

variables:
  # Azure service connection established during pipeline creation
  azureSubscription: <Name of your Azure subscription>
  appName: <Name of the function app>
  # Agent VM image name
  vmImageName: 'ubuntu-latest'

- task: AzureFunctionApp@2 # Add this at the end of your file
  inputs:
    azureSubscription: <Name of your Azure subscription>
    appType: functionAppLinux # This specifies a Linux-based function app
    #isFlexConsumption: true # Uncomment this line if you are deploying to a Flex Consumption app
    appName: $(appName)
    package: $(System.DefaultWorkingDirectory)/build$(Build.BuildId).zip
    deploymentMethod: 'auto' # 'auto' | 'zipDeploy' | 'runFromPackage'. Required. Deployment method. Default: auto.
```

The default `appType` is Windows (`functionApp`). You can specify Linux by setting the `appType` to `functionAppLinux`. A [Flex Consumption](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan) app runs on Linux, and you to must set both `appType: functionAppLinux` and `isFlexConsumption: true`.

The snippet assumes that the build steps in your YAML file produce the zip archive in the `$(System.ArtifactsDirectory)` folder on your agent.

You deploy using the [Azure Function App Deploy](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-function-app) task. This task requires an [Azure service connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints) as an input. An Azure service connection stores the credentials to connect from Azure Pipelines to Azure.

Important

Deploying to a Flex Consumption app isn't supported using @v1 of the `AzureFunctionApp` task.

To deploy to Azure Functions, add this snippet at the end of your `azure-pipelines.yml` file:

```
trigger:
- main

variables:
  # Azure service connection established during pipeline creation
  azureSubscription: <Name of your Azure subscription>
  appName: <Name of the function app>
  # Agent VM image name
  vmImageName: 'ubuntu-latest'

- task: DownloadBuildArtifacts@1 # Add this at the end of your file
  inputs:
    buildType: 'current'
    downloadType: 'single'
    artifactName: 'drop'
    itemPattern: '**/*.zip'
    downloadPath: '$(System.ArtifactsDirectory)'
- task: AzureFunctionApp@1
  inputs:
    azureSubscription: $(azureSubscription)
    appType: functionAppLinux # default is functionApp
    appName: $(appName)
    package: $(System.ArtifactsDirectory)/**/*.zip
```

This snippet sets the `appType` to `functionAppLinux`, which is required when deploying to an app that runs on Linux. The default `appType` is Windows (`functionApp`).

The example assumes that the build steps in your YAML file produce the zip archive in the `$(System.ArtifactsDirectory)` folder on your agent.

When deploying a containerized function app, the deployment task you use depends on the specific hosting environment.

*   [Azure Container Apps hosting](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_5_container-apps)
*   [Azure Functions hosting](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_5_azure-functions)

You can use the [Azure Container Apps Deploy](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/azure-container-apps-v1) task (`AzureContainerApps`) to deploy a function app image to an Azure Container App instance that is optimized for Azure Functions.

This code deploys the base image for a .NET 8 isolated process model function app:

```
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: AzureContainerApps@1
  inputs:
    azureSubscription: <Name of your Azure subscription>
    imageToDeploy: 'mcr.microsoft.com/azure-functions/dotnet-isolated:4-dotnet-isolated8.0'
    containerAppName: <Name of your container app>
    resourceGroup: <Name of the resource group>
```

Ideally, you would build your own custom container in the pipeline instead of using a base image, as shown in this example. For more information, see [Deploy to Azure Container Apps from Azure Pipelines](https://learn.microsoft.com/en-us/azure/container-apps/azure-pipelines).

*   [Windows App](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_6_windows)
*   [Linux App](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops#tabpanel_6_linux)

```
trigger:
- main

variables:
  # Azure service connection established during pipeline creation
  azureSubscription: <Name of your Azure subscription>
  appName: <Name of the function app>
  # Agent VM image name
  vmImageName: 'ubuntu-latest'

- task: AzureFunctionApp@2 # Add this at the end of your file
  inputs:
    azureSubscription: <Name of your Azure subscription>
    appType: functionAppLinux # This specifies a Linux-based function app
    #isFlexConsumption: true # Uncomment this line if you are deploying to a Flex Consumption app
    appName: $(appName)
    package: $(System.DefaultWorkingDirectory)/build$(Build.BuildId).zip
    deploymentMethod: 'auto' # 'auto' | 'zipDeploy' | 'runFromPackage'. Required. Deployment method. Default: auto.
    deployToSlotOrASE: true
    resourceGroupName: '<RESOURCE_GROUP>'
    slotName: '<SLOT_NAME>'
```

You can configure your function app to have multiple slots. Slots allow you to safely deploy your app and test it before making it available to your customers.

The following YAML snippet shows how to deploy to a staging slot, and then swap to a production slot:

```
- task: AzureFunctionApp@1
  inputs:
    azureSubscription: <Azure service connection>
    appType: functionAppLinux
    appName: <Name of the function app>
    package: $(System.ArtifactsDirectory)/**/*.zip
    deployToSlotOrASE: true
    resourceGroupName: <Name of the resource group>
    slotName: staging

- task: AzureAppServiceManage@0
  inputs:
    azureSubscription: <Azure service connection>
    WebAppName: <name of the function app>
    ResourceGroupName: <name of resource group>
    SourceSlot: staging
    SwapWithProduction: true
```

When using [deployment slots](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-slots), you can also add the following task to perform a slot swap as part of your deployment.

```
- task: AzureAppServiceManage@0
  inputs:
    azureSubscription: <AZURE_SERVICE_CONNECTION>
    WebAppName: <APP_NAME>
    ResourceGroupName: <RESOURCE_GROUP>
    SourceSlot: <SLOT_NAME>
    SwapWithProduction: true
```

To create a build pipeline in Azure, use the `az functionapp devops-pipeline create`[command](https://learn.microsoft.com/en-us/cli/azure/functionapp/devops-pipeline#az-functionapp-devops-pipeline-create). The build pipeline is created to build and release any code changes that are made in your repo. The command generates a new YAML file that defines the build and release pipeline and then commits it to your repo. The prerequisites for this command depend on the location of your code.

*   If your code is in GitHub:

    *   You must have **write** permissions for your subscription.

    *   You must be the project administrator in Azure DevOps.

    *   You must have permissions to create a GitHub personal access token (PAT) that has sufficient permissions. For more information, see [GitHub PAT permission requirements.](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/github#repository-permissions-for-personal-access-token-pat-authentication)

    *   You must have permissions to commit to the main branch in your GitHub repository so you can commit the autogenerated YAML file.

*   If your code is in Azure Repos:

    *   You must have **write** permissions for your subscription.

    *   You must be the project administrator in Azure DevOps.

*   Review the [Azure Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview).
*   Review the [Azure DevOps overview](https://learn.microsoft.com/en-us/azure/devops/pipelines/).
