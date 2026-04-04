# Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp

Title: Configure CI/CD with Azure Pipelines - Azure App Service

URL Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp

Markdown Content:
**Azure DevOps Services** | **Azure DevOps Server 2022**

This article explains how to use [Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/) to automatically build, test, and deploy your web app to [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/overview). You can set up a continuous integration and continuous delivery (CI/CD) pipeline that runs whenever you check in a code change to a designated branch of your repository.

Pipelines consist of _stages_, _jobs_, and _steps_. A step is the smallest building block of a pipeline and can be a _script_ or a _task_, which is a prepackaged script. For more information about the key concepts and components that make up a pipeline, see [Key Azure Pipelines concepts](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/key-pipelines-concepts).

You can use the [Azure Web App](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app) task in your pipeline to deploy to App Service. For more complex scenarios, like using XML parameters in deployments, you can use the [Azure App Service deploy](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app-deployment) task.

*   A working Azure App Service app with code hosted on [GitHub](https://docs.github.com/get-started/quickstart/create-a-repo) or [Azure Repos](https://learn.microsoft.com/en-us/azure/devops/repos/git/creatingrepo). You can use any of the following quickstart articles to create a sample app:

    *   ASP.NET Core: [Create an ASP.NET Core web app in Azure](https://learn.microsoft.com/en-us/azure/app-service/quickstart-dotnetcore)
    *   ASP.NET: [Create an ASP.NET Framework web app in Azure](https://learn.microsoft.com/en-us/azure/app-service/quickstart-dotnetcore?tabs=netframework48)
    *   JavaScript: [Create a Node.js web app in Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-nodejs)
    *   Java: [Create a Java app in Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-java)
    *   Python: [Create a Python app in Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python)

*   An Azure DevOps organization that has the ability to run pipelines on Microsoft-hosted agents. You need to request a free tier of parallel jobs or purchase parallel jobs. For more information, see [Configure and pay for parallel jobs](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs).

*   A project created in the Azure DevOps organization where you have permission to create and authorize pipelines and Azure service connections. [Create a project in Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project).

Important

During GitHub procedures, you might be prompted to create a [GitHub service connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints#github-service-connection) or be redirected to GitHub to sign in, install the [Azure Pipelines](https://github.com/apps/azure-pipelines) GitHub app, authorize Azure Pipelines, or authenticate to GitHub organizations. Follow the onscreen instructions to complete the necessary processes. For more information, see [Access to GitHub repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/github#access-to-github-repositories).

The code examples in this section are for an ASP.NET Core web app. You can adapt the instructions for other frameworks. For more information about Azure Pipelines ecosystem support, see [Azure Pipelines ecosystem examples](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/ecosystems).

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_1_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_1_classic)

Define a pipeline by creating an _azure-pipelines.yml_ YAML file in your code repository.

1.   On the left navigation menu for your Azure DevOps project, select **Pipelines**.
2.   On the **Pipelines** page, select **New pipeline**, or **Create pipeline** if this pipeline is the first in the project.
3.   On the **Where is your code** screen, select the location of your source code, either **Azure Repos Git** or **GitHub**. If necessary, sign in to GitHub.
4.   On the **Select a repository** screen, select your code repository.
5.   On the **Configure your pipeline** screen, select **Starter pipeline**.

Add the [.NET Core (DotNetCoreCLI@2)](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/dotnet-core-cli-v2) task to the pipeline, and build and publish your app.

1.   On the **Review your pipeline YAML** screen, delete all the code after the `steps:` line.
2.   Select the end of the file, and then select **Show assistant** at right.
3.   Under **Tasks**, select **.NET Core**.
4.   On the **.NET Core** configuration screen, under **Azure Resource Manager connection**, select your Azure subscription, and then select **Authorize** to create the required service connection.
5.   Under **Command**, select **publish**.
6.   Ensure that the **Publish web projects** and **Zip published projects** check boxes are selected, and then select **Add**.
7.   The task appears in your YAML pipeline. Review the YAML code to see what it does. When you're ready, select **Save and run**, and then select **Save and run** again.
8.   On the build **Summary** screen, under **Jobs**, select the **Permission needed** link. On the **Checks** screen, select **Permit**, and then select **Permit** again. Granting permission here permits use of the service connection you authorized for all runs of this pipeline.

The pipeline publishes the deployment ZIP file as an Azure artifact for the deployment task to use in the next step.

After the pipeline runs successfully, add the deployment task.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_2_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_2_classic)

1.   On the pipeline run **Summary** screen, select the **More actions** icon at upper right, and then select **Edit pipeline**.
2.   Select the end of the YAML file, and select **Show assistant** if the **Tasks** list isn't showing.
3.   In the **Tasks** list, search for and select the [Azure Web App](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app) task. Alternatively, you can use the [Azure App Service deploy](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app-deployment) task.
4.   On the **Azure Web App** configuration screen, under **Azure subscription**, select the same service connection you set up for the previous step. You don't need to reauthorize this connection.
5.   For **App type**, select **Azure Web App on Linux** or **Azure Web App on Windows**, depending on your code.
6.   For **App name**, select or enter your App Service app name.
7.   Select **Add**.
8.   Select **Validate and save**, and then select **Save**.
9.   Select **Run**, and then select **Run** again.

The complete YAML pipeline should look like the following code:

```
trigger:
- <branch-specification>

pool:
  vmImage: <agent-specification>

steps:
- task: DotNetCoreCLI@2
  inputs:
    azureSubscription: '<your-authorized-service-connection>'
    command: 'publish'
    publishWebProjects: true

- task: AzureWebApp@1
  inputs:
    azureSubscription: '<your-authorized-service-connection>'
    appType: 'webApp'
    appName: '<your-app-name>'
    package: '$(System.DefaultWorkingDirectory)/**/*.zip'
    deploymentMethod: 'auto'
```

*   `azureSubscription`: Name of the authorized service connection to your Azure subscription.
*   `appName`: Name of your existing app.
*   `package`: File path to the package or folder containing your App Service contents. Wildcards are supported.

The following sections discuss creating different kinds of build and release pipelines.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_3_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_3_classic)

The [Azure Web App](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app) task deploys to the root application in the Azure web app. You can deploy to a specific virtual application by using the `VirtualApplication` property of the [Azure App Service deploy](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app-deployment) task.

```
- task: AzureRmWebAppDeployment@5
  inputs:
    VirtualApplication: '<name of virtual application>'
```

`VirtualApplication` is the name of the virtual application configured in the Azure portal. For more information, see [Configure an App Service app in the Azure portal](https://learn.microsoft.com/en-us/azure/app-service/configure-common).

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_4_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_4_classic)

The following example shows how to deploy to a staging slot, and then swap to a production slot:

```
- task: AzureWebApp@1
  inputs:
    azureSubscription: '<service-connection-name>'
    appType: webAppLinux
    appName: '<app-name>'
    deployToSlotOrASE: true
    resourceGroupName: '<name of resource group>'
    slotName: staging
    package: '$(Build.ArtifactStagingDirectory)/**/*.zip'

- task: AzureAppServiceManage@0
  inputs:
    azureSubscription: '<service-connection-name>'
    WebAppName: '<app-name>'
    ResourceGroupName: '<name of resource group>'
    SourceSlot: staging
    SwapWithProduction: true
```

*   `azureSubscription`: Your Azure service connection.
*   `appType`: Optional app type such as `webAppLinux` to deploy to a web app on Linux.
*   `appName`: The name of your existing app.
*   `deployToSlotOrASE`: Boolean. Whether to deploy to an existing deployment slot or App Service environment.
*   `resourceGroupName`: Name of the resource group to deploy to, required if `deployToSlotOrASE` is true.
*   `slotName`: Name of the slot to deploy to, required if `deployToSlotOrASE` is true. Defaults to `production`.
*   `package`: File path to the package or folder containing your app contents. Wildcards are supported.
*   `SourceSlot`: Slot sent to production when `SwapWithProduction` is true.
*   `SwapWithProduction`: Boolean. Whether to swap the traffic of source slot with production.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_5_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_5_classic)

You can use [jobs](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/phases) in your YAML file to set up a pipeline of deployments. By using jobs, you can control the order of deployment to multiple web apps.

```
jobs:
- job: buildandtest
  pool:
    vmImage: ubuntu-latest
 
  steps:
  # publish an artifact called drop
  - task: PublishPipelineArtifact@1
    inputs:
      targetPath: '$(Build.ArtifactStagingDirectory)' 
      artifactName: drop
  
  # deploy to Azure Web App staging
  - task: AzureWebApp@1
    inputs:
      azureSubscription: '<service-connection-name>'
      appType: <app type>
      appName: '<staging-app-name>'
      deployToSlotOrASE: true
      resourceGroupName: <group-name>
      slotName: 'staging'
      package: '$(Build.ArtifactStagingDirectory)/**/*.zip'

- job: deploy
  dependsOn: buildandtest
  condition: succeeded()

  pool: 
    vmImage: ubuntu-latest
  
  steps:
    # download the artifact drop from the previous job
  - task: DownloadPipelineArtifact@2
    inputs:
      source: 'current'
      artifact: 'drop'
      path: '$(Pipeline.Workspace)'

  - task: AzureWebApp@1
    inputs:
      azureSubscription: '<service-connection-name>'
      appType: <app type>
      appName: '<production-app-name>'
      resourceGroupName: <group-name>
      package: '$(Pipeline.Workspace)/**/*.zip'
```

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_6_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_6_classic)

To deploy conditionally in YAML, use one of the following techniques:

*   Add a condition to the step.
*   Isolate the deployment steps into a separate job, and add a condition to that job.

The following example shows how to use step conditions to deploy only successful builds that originate from the main branch:

```
- task: AzureWebApp@1
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
  inputs:
    azureSubscription: '<service-connection-name>'
    appName: '<app-name>'
```

For more information about conditions, see [Specify conditions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/conditions).

The [Azure App Service deploy](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app-deployment) task can deploy to App Service by using Web Deploy.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_7_yaml)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#tabpanel_7_classic)

```
trigger:
- main

pool:
  vmImage: windows-latest

variables:
  buildConfiguration: 'Release'

steps:
- task: DotNetCoreCLI@2
  inputs:
    command: 'publish'
    publishWebProjects: true
    arguments: '--configuration $(buildConfiguration)'
    zipAfterPublish: true

- task: AzureRmWebAppDeployment@5
  inputs:
    ConnectionType: 'AzureRM'
    azureSubscription: '<service-connection-name>'
    appType: 'webApp'
    WebAppName: '<app-name>'
    packageForLinux: '$(System.DefaultWorkingDirectory)/**/*.zip'
    enableCustomDeployment: true
    DeploymentType: 'webDeploy'
```

The [Azure Web App](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app) task is the simplest way to deploy to an Azure web app. By default, you deploy the root application in the Azure web app.

The [Azure App Service deploy](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app-deployment) task can handle more custom scenarios, such as:

*   [Deploy with Web Deploy](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#deploy-using-web-deploy), if you usually use the Internet Information Services (IIS) deployment process.
*   [Deploy to virtual applications](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp#deploy-to-a-virtual-application).
*   Deploy to other app types, like container apps, function apps, WebJobs, or API and mobile apps.

Note

The separate [File Transform](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/file-transform) task also supports file transforms and variable substitution to use in Azure Pipelines. You can use the **File Transform** task to apply file transformations and variable substitutions on any configuration and parameters files.

In YAML pipelines, there could be a mismatch between where your built web package is saved and where the deploy task is looking for it. The default **AzureWebApp** task picks up the web package for deployment from `$(System.DefaultWorkingDirectory)/**/*.zip`. If the web package is deposited elsewhere, modify the value of the `package` parameter.

This error occurs in the **AzureRmWebAppDeployment** task when you configure the task to deploy using **Web Deploy**, but your agent isn't running Windows. Verify that your YAML `vmImage` parameter specifies Windows.

```
pool:
  vmImage: windows-latest
```

For troubleshooting information on getting Microsoft Entra ID authentication to work with the [Azure App Service deploy](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app-deployment) task, see [I can't Web Deploy to my Azure App Service using Microsoft Entra ID authentication from my Windows agent](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-rm-web-app-deployment#i-cant-web-deploy-to-my-azure-app-service-using-microsoft-entra-id-authentication-from-my-windows-agent).

*   [Customize your pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/customize-pipeline)
*   [Build and deploy Python web apps](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp)
