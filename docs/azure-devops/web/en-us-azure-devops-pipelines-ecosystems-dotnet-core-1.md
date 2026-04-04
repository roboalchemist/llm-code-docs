# Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops

Title: Build, test, and deploy .NET Core projects - Azure Pipelines

URL Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops

Published Time: Tue, 20 Jan 2026 22:03:51 GMT

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

This article describes how to use Azure Pipelines to work with .NET Core projects. The article walks you through the following tasks:

*   Create a .NET Core web app and upload it to a GitHub repository.
*   Create an Azure DevOps project and an Azure Pipelines pipeline to build the project.
*   Set up your build environment with self-hosted agents.
*   Restore dependencies, build your project, and test with the **.NET Core** (`DotNetCoreCLI@2`) task or a script.
*   Use the **.NET Core** (`DotNetCoreCLI@2`) task to add other .NET SDK commands to your pipeline.
*   Use the **Publish Code Coverage Results** (`Publish code coverage results v2`) task to publish code coverage results.
*   Package and deliver your build output to your pipeline, a NuGet feed, a ZIP archive, or other targets.

*   Create a .NET Core web app and upload it to a GitHub repository.
*   Create an Azure DevOps project and an Azure Pipelines pipeline to build the project.
*   Set up your build environment with Microsoft-hosted or self-hosted agents.
*   Restore dependencies, build your project, and test with the **.NET Core** (`DotNetCoreCLI@2`) task or a script.
*   Use the **.NET Core** (`DotNetCoreCLI@2`) task to add other .NET SDK commands to your pipeline.
*   Use the **Publish Code Coverage Results** (`Publish code coverage results v2`) task to publish code coverage results.
*   Package and deliver your build output to your pipeline, a NuGet feed, a ZIP archive, or other targets.

To complete all the procedures in this article, you need the following prerequisites:

*   An Azure DevOps organization. You can [create one for free](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/pipelines-sign-up?view=azure-devops).
*   Membership in the organization [Project Administrators group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops#add-members-to-the-project-administrators-group), so you can create Azure DevOps projects and grant project access to pipelines. Azure DevOps organization owners automatically have this membership.
*   An Azure DevOps project in the organization. [Create a project in Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops).
*   The ability to run pipelines on Microsoft-hosted agents, by requesting a free tier of parallel jobs. This request can take several business days to process. For more information, see [Configure and pay for parallel jobs](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops).
*   The **Administrator** or **Creator** role for [service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/add-resource-protection?view=azure-devops), which you can assign as a Project Administrator.
*   A [GitHub](https://github.com/) account and repository.

To complete all the procedures in this article, you need the following prerequisites:

*   An Azure DevOps collection.
*   An Azure DevOps project created in the organization. For instructions, see [Create a project in Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops).
*   Membership in the [Project Administrators group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-project-level-permissions?view=azure-devops), so you can create Azure DevOps projects and grant project access to pipelines. Azure DevOps Organization owners automatically have this membership.
*   The **Administrator** or **Creator** role for [service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/add-resource-protection?view=azure-devops), which you can assign as a Project Administrator.
*   A [GitHub](https://github.com/) account and repository.

If you want to use a .NET project that's already in your GitHub repository, you can skip this section.

If you don't have a .NET project to work with, create a new one on your local machine as follows:

1.   Install the [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0), or make sure it's installed.
2.   Open a terminal window on your local machine.
3.   Create a project directory and navigate to it.
4.   Create a new .NET 8 web app by running `dotnet new webapp -f net8.0`.
5.   Build and run the application locally by using [`dotnet run`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-run).
6.   When the application starts, press Ctrl+C to shut it down.
7.   Upload or connect the local project to your GitHub repository.

If you have a pipeline you want to use, you can skip this section. Otherwise, you can use either the YAML pipeline editor or the classic editor to create a pipeline.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_1_yaml-editor)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_1_classic-editor)

1.   In your Azure DevOps project, select **Pipelines** from the left navigation menu.

2.   Select **New pipeline** or **Create pipeline** if this pipeline is the first in the project.

3.   On the **Where is your code** screen, select **GitHub**.

4.   You might be redirected to GitHub to sign in. If so, enter your GitHub credentials.

5.   On the **Select a repository** screen, select the repository your .NET app is in.

6.   You might be redirected to GitHub to install the Azure Pipelines app. If so, select **Approve & install**.

1.   On the **Configure** tab, select **Show more** and then select the [ASP.NET Core](https://github.com/Microsoft/azure-pipelines-yaml/blob/master/templates/asp.net-core.yml) pipeline template from the list. This template provides many of the steps and settings that this article describes.

You can also select **Starter pipeline** on the **Configure** tab to start with a minimal pipeline and add the steps and settings yourself.

2.   On the **Review** tab, examine the YAML code. You can customize the file for your requirements. For example, you can specify a different agent pool or add a task to install a different .NET SDK.

1.   In your Azure DevOps project, select **Pipelines** from the left navigation menu.

2.   Select **New pipeline** or **Create pipeline** if this pipeline is the first in the project.

3.   Select your source repository type. For this example, use **GitHub Enterprise Server**.

4.   On the next screen, enter the following information:

    *   The URL for your GitHub account, for example `https://github.com/myname`.
    *   Your GitHub personal access token (PAT).
    *   A service connection name, for example `my-github`.

5.   Select **Create**.

6.   Select your GitHub repository.

7.   On the **Configure** tab, select **Show more** and select the [ASP.NET Core](https://github.com/Microsoft/azure-pipelines-yaml/blob/master/templates/asp.net-core.yml) pipeline template from the list. This template provides many of the steps and settings that this article describes.

8.   Examine the new YAML pipeline code. You can customize the YAML file for your requirements. For example, you could add a [task to install a different .NET SDK](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#build-environment) or to test and publish your project.

1.   When you're ready, select **Save and run**.

![Image 1: Screenshot that shows the Save and run button in a new YAML pipeline.](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/media/save-and-run-button-new-yaml-pipeline.png?view=azure-devops)

2.   Optionally edit the **Commit message**, and then select **Save and run** again.

3.   On the **Summary** tab, select the job in the **Jobs** section to watch your pipeline in action.

You now have a working pipeline that's ready to customize.

Azure Pipelines uses [self-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops#install) to build your .NET Core project. You can use the .NET Core SDK and runtime on [Windows](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops), [Linux](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/linux-agent?view=azure-devops), [macOS](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/osx-agent?view=azure-devops), or [Docker](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/docker?view=azure-devops) agents. Make sure that you have the necessary version of the .NET Core SDK and runtime installed on the agents.

To install a specific version of the .NET SDK, add the `UseDotNet@2` task to a YAML pipeline file or the **Use .NET Core** task in the classic editor.

Note

For agents that run on physical systems, installing SDKs and tools through your pipeline alters the build environment on the agent's host.

The following example YAML snippet installs .NET SDK 8.0.x:

```
steps:
- task: UseDotNet@2
  inputs:
    version: '8.x'
```

To install a newer SDK, set `performMultiLevelLookup` to `true`.

```
steps:
- task: UseDotNet@2
  displayName: 'Install .NET Core SDK'
  inputs:
    version: 8.x
    performMultiLevelLookup: true
    includePreviewVersions: true # Required for preview versions
```

You can select the agent pool and agent for your build job. You can also specify agents based on their capabilities. For example, the following YAML pipeline snippet selects a pool and agent capabilities.

```
pool:
  name: myPrivateAgents
  demands:
  - agent.os -equals Darwin
  - anotherCapability -equals somethingElse
```

You can build your .NET Core projects by using the .NET Core SDK and runtime for Windows, Linux, or macOS. By default, your builds run on [Microsoft-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops), so you don't need to set up infrastructure.

Azure Pipelines Microsoft-hosted agents include several preinstalled versions of supported .NET Core SDKs. See [Microsoft-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops) for a complete list of available images and configuration examples.

The following YAML pipeline snippet sets Ubuntu OS for the agent pool.

```
pool:
  vmImage: 'ubuntu-latest'
```

Microsoft-hosted agents don't include some older versions of the .NET Core SDK, and they don't typically include prerelease versions. If you need these versions of the SDK on Microsoft-hosted agents, you can install them by using the **Use DotNet** ([UseDotNet@2](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/use-dotnet-v2)) task.

For example, the following code installs the .NET 8.0.x SDK:

```
steps:
- task: UseDotNet@2
  inputs:
    version: '8.x'
```

Windows agents already include a .NET Core runtime. To install a newer SDK, set `performMultiLevelLookup` to `true` as in the following snippet:

```
steps:
- task: UseDotNet@2
  displayName: 'Install .NET Core SDK'
  inputs:
    version: 8.x
    performMultiLevelLookup: true
    includePreviewVersions: true # Required for preview versions
```

Alternatively, you can use [self-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops#self-hosted-agents) to build your .NET Core projects. You can set up [Linux](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/linux-agent?view=azure-devops), [macOS](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/osx-agent?view=azure-devops), or [Windows](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops) self-hosted agents.

By using self-hosted agents, you can:

*   Avoid the cost of running the `UseDotNet@2` tool installer.
*   Decrease build time if you have a large repository.
*   Run incremental builds.
*   Use preview or private SDKs that Microsoft doesn't officially support.
*   Use SDKs available only in your corporate or on-premises environments.

For more information, see [Self-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops#self-hosted-agents).

NuGet packages provide a way for your project to depend on code that you don't build. Run the `dotnet restore` command to download NuGet packages and project-specific tools. You can run this command through the **.NET Core** (`DotNetCoreCLI@2`) task or as a script in your pipeline. The `dotnet restore` command uses the _NuGet.exe_ packaged with the .NET Core SDK and can only restore packages specified in the .NET Core project _*.csproj_ files.

Use the **.NET Core** (`DotNetCoreCLI@2`) task to download and restore NuGet packages from Azure Artifacts, NuGet.org, or another authenticated external or internal NuGet repository. If the NuGet feed is in the same project as your pipeline, you don't need to authenticate. For more information, see [.NET Core task (DotNetCoreCLI@2)](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/dotnet-core-cli-v2).

When you use Microsoft-hosted agents, you get a new machine every time you run a build, which restores the packages with each run. Restoration can take a significant amount of time. To mitigate this issue, use Azure Artifacts or a [self-hosted agent](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#self-hosted-agents) to take advantage of the package cache.

The following pipeline uses the `DotNetCoreCLI@2` task to restore an Azure Artifact feed.

```
trigger:
- main

pool:
  vmImage: 'windows-latest'

steps:
- task: UseDotNet@2
  displayName: 'Install .NET Core SDK'
  inputs:
    version: 8.x
    performMultiLevelLookup: true
    includePreviewVersions: true # Required for preview versions

variables:
  buildConfiguration: 'Release'

steps:
- task: DotNetCoreCLI@2
  inputs:
    command: 'restore'
    feedsToUse: 'select'
    vstsFeed: 'my-vsts-feed' # A series of numbers and letters

- task: DotNetCoreCLI@2
  inputs:
    command: 'build'
    arguments: '--configuration $(buildConfiguration)'
  displayName: 'dotnet build $(buildConfiguration)'
```

.NET automatically restores packages when you run commands such as `dotnet build`. You still need to use the **.NET Core** (`DotNetCoreCLI@2`) task to restore packages if you use an authenticated feed.

Manage the credentials for an authenticated feed by creating a NuGet service connection in **Project Settings**>**Pipelines**>**Service connections**. For more information about NuGet service connections, see [Publish NuGet packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/nuget?view=azure-devops).

To restore packages from NuGet.org, update your pipeline as follows.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_2_yaml-editor)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_2_classic-editor)

You can add the restore command to your pipeline by editing the YAML code directly or by using the task assistant.

Add the **.NET Core** (`DotNetCoreCLI@2`) task directly by inserting the following snippet into your _azure-pipelines.yml_ file before your build tasks.

```
steps:
- task: DotNetCoreCLI@2
  displayName: Restore
  inputs:
    command: restore
    projects: '**/*.csproj'
    feedsToUse: select
```

To use the task assistant:

1.   Go to the position in the YAML file where you want to insert the task.
2.   Select **.NET Core** from the task catalog.
3.   On the configuration screen, select **restore** from the **Command** dropdown list.
4.   In the **Path to project(s) or solution(s)** field, enter the path to your _*.csproj_ files. You can use the wildcard _**/*.csproj_ for all _*.csproj_ files in all subfolders.
5.   For **Feeds to add**, ensure that **Feed(s) I select here** and **Use packages from NuGet.org** are selected.
6.   Select **Add**.
7.   Select **Validate and save**, and then select **Save** to commit the change.

To specify an external NuGet repository, put the URL in a _NuGet.config_ file in your repository. Make sure any custom feed is specified in your _NuGet.config_ file, and that credentials are specified in a NuGet service connection.

To restore packages from an external feed, add the `restore` task as instructed in the previous section, but change the configuration settings as follows:

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_3_yaml-editor)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_3_classic-editor)

Add the **.NET Core** (`DotNetCoreCLI@2`) task directly by inserting the following snippet into your _azure-pipelines.yml_ file before your build tasks. Replace `<NuGet service connection>` with your service connection name.

```
steps:
- task: DotNetCoreCLI@2
  displayName: Restore
  inputs:
    command: restore
    projects: '**/*.csproj'
    feedsToUse: config
    nugetConfigPath: NuGet.config    # Relative to root of the repository
    externalFeedCredentials: <NuGet service connection>
```

To use the task assistant:

1.   Add the **.NET Core** task and select **restore** on the configuration screen as in the preceding procedure.
2.   For **Feeds to add**, select **Feeds in my NuGet.config**.
3.   Under **Path to NuGet.config**, enter the path to your _NuGet.config_ file, relative to the root of your repository. You can select the ellipsis **...** next to the field to browse to and select the location.
4.   Under **Credentials for feeds outside this organization/collection**, select credentials to use for external registries in the selected _NuGet.config_ file. For feeds in the same organization, leave this field blank. The build’s credentials are used automatically.

If your solution includes a .NET Framework project or you use _package.json_ to specify your dependencies, use the **NuGetCommand@2** task to restore those dependencies.

```
- task: NuGetCommand@2
  inputs:
    command: 'restore'
    restoreSolution: '**/*.sln'
    feedsToUse: 'select'
```

Note

For Ubuntu 24.04 or higher, you must use the **NuGetAuthenticate** task instead of the **NuGetCommand@2** task with the .NET CLI. For more information, see [Support for newer Ubuntu hosted images](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/nuget-command-v2#support-for-newer-ubuntu-hosted-images).

Build your .NET Core project by running the `dotnet build` command. You can add the command to your pipeline by using the **.NET Core** (`DotNetCoreCLI@2`) task or as a command line script.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_4_yaml-editor)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_4_classic-editor)

You can add a build task by using the YAML pipeline editor. You can directly edit the file or use the task assistant.

Add the **.NET Core** (`DotNetCoreCLI@2`) task directly by inserting the following snippet. Update the `arguments` to match your needs.

```
steps:
- task: DotNetCoreCLI@2
  displayName: Build
  inputs:
    command: build
    projects: '**/*.csproj'
    arguments: '--configuration $(buildConfiguration)'
```

To use the task assistant:

1.   Go to the position in the YAML file where you want to insert the task.
2.   Select the **.NET Core** (`DotNetCoreCLI@2`) task.
3.   Select **build** from the **Command** dropdown list.
4.   In the **Path to project(s) or solution(s)** field, enter the path to your _*.csproj_ files. You can use the wildcard _**/*.csproj_ for all _*.csproj_ files in all subfolders.
5.   Select **Add**.
6.   Select **Save** to commit the change.

You can also build using a command line script.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_5_yaml-editor)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_5_classic-editor)

To add a build command line by directly editing the YAML file, add the following code:

```
steps:
- script: dotnet build --configuration $(buildConfiguration)
  displayName: 'dotnet build $(buildConfiguration)'
```

You can also use the task assistant to add the [Command line](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/cmd-line-v2) task.

1.   Go to the position in the YAML file where you want to insert the task.
2.   Select the **Command line** (`CmdLine@2`) task from the list.
3.   In the **Script** field, enter the `dotnet build` command with parameters. For example, `dotnet build --configuration $(buildConfiguration)`.
4.   Under **Advanced**>**Working Directory**, enter the path to the _*.csproj_ file as the working directory. If you leave it blank, the working directory defaults to `$(Build.SourcesDirectory)`.
5.   Select **Add**.
6.   Select **Save** to commit the change.

You can add other .NET SDK commands to your pipeline by using the **.NET Core** (`DotNetCoreCLI@2`) task or as scripts.

The [.NET Core (DotNetCoreCLI@2)](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/dotnet-core-cli-v2) task lets you easily add .NET CLI commands to your pipeline. You can add **.NET Core** (`DotNetCoreCLI@2`) tasks by editing your YAML file or by using the classic editor.

*   [YAML](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_6_yaml-editor)
*   [Classic](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#tabpanel_6_classic-editor)

To add a .NET Core command by using the task assistant in the YAML pipeline editor, complete the following steps:

1.   Go to the position in the YAML file where you want to insert the task.
2.   Select **.NET Core** from the task catalog.
3.   Select the command you want to run from the dropdown list in the **Command** field.
4.   Configure any options needed.
5.   Select **Add**.
6.   Select **Save** to commit the change.

Add a .NET Core CLI command as a `script` in your _azure-pipelines.yml_ file. For example:

```
steps:
# ...
- script: dotnet test <test-project>
```

To install a .NET Core global tool like [dotnetsay](https://www.nuget.org/packages/dotnetsay/) in a build running on Windows, add a **.NET Core** task and set the following properties in the configuration:

*   **Command**: **custom**
*   **Path to projects**: leave empty
*   **Custom command**: `tool`
*   **Arguments**: `install -g dotnetsay`

To run the tool, add a **Command Line** task and enter `dotnetsay` in the **Script** field.

When your repository contains test projects, use the **.NET Core** (`DotNetCoreCLI@2`) task to run unit tests by using testing frameworks like MSTest, xUnit, and NUnit. The test project must reference [Microsoft.NET.Test.SDK](https://www.nuget.org/packages/Microsoft.NET.Test.SDK) version 15.8.0 or higher.

The service automatically publishes test results. You can see them in the build summary. Use the test results to troubleshoot failed tests and analyze test timing.

To add a test task to your pipeline, add the following snippet to your _azure-pipelines.yml_ file:

```
steps:
# ...
# do this after other tasks such as build
- task: DotNetCoreCLI@2
  inputs:
    command: test
    projects: '**/*Tests/*.csproj'
    arguments: '--configuration $(buildConfiguration)'
```

If you use the task assistant to add the **.NET Core** (`DotNetCoreCLI@2`) task, set the following properties:

*   **Command**: **test**
*   **Path to projects**: Set to the test projects in your solution
*   **Arguments**: `--configuration $(BuildConfiguration)`

Alternatively, run the `dotnet test` command with a specific logger and then use the `PublishTestResults@2` task:

```
steps:
# ...
# do this after your tests run
- script: dotnet test <test-project> --logger trx
- task: PublishTestResults@2
  condition: succeededOrFailed()
  inputs:
    testRunner: VSTest
    testResultsFiles: '**/*.trx'
```

When you build on the Windows platform, you can collect code coverage metrics by using the built-in coverage data collector. The test project must reference [Microsoft.NET.Test.SDK](https://www.nuget.org/packages/Microsoft.NET.Test.SDK) version 15.8.0 or higher.

When you use the **.NET Core** (`DotNetCoreCLI@2`) task to run tests, the pipeline automatically publishes coverage data to the server. You can download the _*.coverage_ file from the build summary to view in Visual Studio.

To collect code coverage, add the `--collect "Code Coverage"` argument when you add the test task to your pipeline.

```
steps:
# ...
# do this after other tasks such as build
- task: DotNetCoreCLI@2
  inputs:
    command: test
    projects: '**/*Tests/*.csproj'
    arguments: '--configuration $(buildConfiguration) --collect "Code Coverage"'
```

If you use the task assistant to add the **.NET Core** (`DotNetCoreCLI@2`) task, set the following properties:

*   **Command**: **test**
*   **Path to projects**: Set to the test projects in your solution
*   **Arguments**: `--configuration $(BuildConfiguration) --collect "Code Coverage"`

Ensure that the **Publish test results** option remains selected.

Alternatively, to collect code coverage results by using the `dotnet test` command with a specific logger and then run the [PublishTestResults@2](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/publish-test-results-v2) task, use the following code:

```
steps:
# ...
# do this after your tests run
- script: dotnet test <test-project> --logger trx --collect "Code Coverage"
- task: PublishTestResults@2
  inputs:
    testRunner: VSTest
    testResultsFiles: '**/*.trx'
```

If you build on Linux or macOS, use [Coverlet](https://github.com/tonerdo/coverlet) or a similar tool to collect code coverage metrics.

You can publish code coverage results to the server with the [Publish Code Coverage Results (PublishCodeCoverageResults@2)](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/publish-code-coverage-results-v2) task. You must configure the coverage tool to generate results in Cobertura or JaCoCo coverage format.

To run tests and publish code coverage with Coverlet:

1.   Add a reference to the `coverlet.collector` NuGet package.
2.   Add the following snippet to your _azure-pipelines.yml_ file. Don't add extra `DataCollectionRunSettings` arguments because the `XPlat Code Coverage` collector already produces a Cobertura report.

```
- task: DotNetCoreCLI@2
  displayName: 'dotnet test'
  inputs:
    command: 'test'
    arguments: '--configuration $(buildConfiguration) --collect:"XPlat Code Coverage"'
    publishTestResults: true
    projects: '<test project directory>'
  
- task: PublishCodeCoverageResults@2
  displayName: 'Publish code coverage report'
  inputs:
    codeCoverageTool: 'Cobertura'
    summaryFileLocation: '$(Agent.TempDirectory)/**/coverage.cobertura.xml'
```

To package and deliver your build output, you can:

*   Publish your build artifacts to Azure Pipelines.
*   Create a NuGet package and publish it to your NuGet feed.
*   Publish your NuGet package to Azure Artifacts.
*   Create a ZIP archive to deploy to a web app.
*   Publish symbols to an Azure Artifacts symbol server or a file share.

You can also [build an image](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/containers/build-image?view=azure-devops) for your app and [push it to a container registry](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/containers/push-image?view=azure-devops).

To publish the output of your .NET build to your pipeline, follow these steps:

1.   Run `dotnet publish --output $(Build.ArtifactStagingDirectory)` using the .NET CLI, or add the **.NET Core** (`DotNetCoreCLI@2`) task with the **publish** command.
2.   Use the [Publish Pipeline Artifact (PublishPipelineArtifact@1)](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/publish-pipeline-artifact-v1) task to publish the artifact. This task uploads all the files in `$(Build.ArtifactStagingDirectory)` as an artifact of your build.

Add the following code to your _azure-pipelines.yml_ file:

```
steps:

- task: DotNetCoreCLI@2
  inputs:
    command: publish
    publishWebProjects: True
    arguments: '--configuration $(BuildConfiguration) --output $(Build.ArtifactStagingDirectory)'
    zipAfterPublish: True

- task: PublishPipelineArtifact@1
  inputs:
    targetPath: '$(Build.ArtifactStagingDirectory)' 
    artifactName: 'myWebsite'
```

To copy more files to the build directory before publishing, use the [Copy Files (CopyFile@2)](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/copy-files-v2) task.

Note

The `publishWebProjects` input in the **.NET Core** (`DotNetCoreCLI@2`) task is set to `true` by default, and publishes all web projects in your repository. For more information, see the [azure-pipelines-tasks](https://github.com/microsoft/azure-pipelines-tasks) GitHub repository.

To publish the output of your .NET build to your pipeline, do the following tasks:

1.   Run `dotnet publish --output $(Build.ArtifactStagingDirectory)` using the .NET CLI or add the **.NET Core** (`DotNetCoreCLI@2`) task with the **publish** command.
2.   Publish the artifact by using the [Publish build artifact (PublishBuildArtifacts@1)](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/publish-pipeline-artifact-v1) task.

The following _azure-pipelines.yml_ code also publishes your build artifacts as a ZIP file. The `PublishBuildArtifacts@1` task uploads all the files in `$(Build.ArtifactStagingDirectory)` as an artifact of your build.

```
steps:

- task: DotNetCoreCLI@2
  inputs:
    command: publish
    publishWebProjects: true
    arguments: '--configuration $(BuildConfiguration) --output $(Build.ArtifactStagingDirectory)'
    zipAfterPublish: True

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)'
    ArtifactName: 'drop'
```

For more information, see [Publish and download build artifacts](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/build-artifacts?view=azure-devops).

To create a NuGet package and publish it to your NuGet feed, add the following snippet to your _azure-pipelines.yml_ file:

```
steps:
# ...
# do this near the end of your pipeline
- script: dotnet pack /p:PackageVersion=$(version)  # define the version variable elsewhere in your pipeline
- task: NuGetAuthenticate@1
  inputs:
    nuGetServiceConnections: '<NuGet service connection>'
- task: NuGetCommand@2
  inputs:
    command: push
    nuGetFeedType: external
    publishFeedCredentials: '<NuGet service connection>'
    versioningScheme: byEnvVar
    versionEnvVar: version
```

Note

The `NuGetAuthenticate@1` task doesn't support NuGet API key authentication. If you're using a NuGet API key, use the `NuGetCommand@2` task with the `command` input set to `push` and the `--api-key` argument. For example, `dotnet nuget push --api-key $(NuGetApiKey)`.

For more information about versioning and publishing NuGet packages, see [Publish NuGet packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/nuget?view=azure-devops).

You can publish your NuGet packages to your Azure Artifacts feed by using the [NuGetCommand@2](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/nuget-command-v2) task. For more information, see [Publish NuGet packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/nuget?view=azure-devops).

To create a ZIP file archive that's ready to publish to a web app, add the following snippet to _azure-pipelines.yml_. Run this task after you build your app, near the end of your pipeline in most cases. For example, run this task before you deploy to an Azure web app on Windows.

```
steps:
# ...
- task: DotNetCoreCLI@2
  inputs:
    command: publish
    publishWebProjects: True
    arguments: '--configuration $(BuildConfiguration) --output $(Build.ArtifactStagingDirectory)'
    zipAfterPublish: True
```

To publish this archive to a web app, see [Azure Web Apps deployment](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp?view=azure-devops).

You can use the `PublishSymbols@2` task to publish symbols to an Azure Artifacts symbol server or a file share. For more information, see [Publish symbols](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/symbols?view=azure-devops).

For example, to publish symbols to a file share, add the following snippet to your _azure-pipelines.yml_ file:

```
- task: PublishSymbols@2
  inputs:
    SymbolsFolder: '$(Build.SourcesDirectory)'
    SearchPattern: '**/bin/**/*.pdb'
    IndexSources: true
    PublishSymbols: true
    SymbolServerType: 'FileShare' 
    SymbolsPath: '\\<server>\<shareName>'
```

To use the classic editor, add the **Index sources and publish symbols** task to your pipeline.

If your project builds successfully on your local machine but not in Azure Pipelines, explore the following potential causes and corrective actions.

*   Microsoft-hosted agents don't have prerelease versions of the .NET Core SDK installed, and rolling out a new version of the SDK to all Azure Pipelines data centers can take a few weeks. Instead of waiting for a rollout to complete, use the [Use .NET Core](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#build-environment) task to install the .NET Core SDK version you want on Microsoft-hosted agents.

*   A new version of the .NET Core SDK or Visual Studio might break the build. For example, it might contain a newer version or feature of the NuGet tool. Make sure the .NET Core SDK versions and runtime on your development machine match the pipeline agent.

You can include a `dotnet --version` command-line script in your pipeline to print the version of the .NET Core SDK. Either use the [.NET Core Tool Installer](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops#build-environment) to deploy the same version on the agent, or update your projects and development machine to the pipeline version of the .NET Core SDK.

*   Connection problems can cause your builds to fail intermittently when you restore packages from NuGet.org. NuGet.org might be having problems, or there could be networking problems between the Azure data center and NuGet.org. You can explore whether using Azure Artifacts with [upstream sources](https://learn.microsoft.com/en-us/azure/devops/artifacts/concepts/upstream-sources?view=azure-devops) to cache the packages improves the reliability of your builds.

The pipeline automatically uses its credentials to connect to Azure Artifacts. These credentials typically come from the **Project Collection Build Service** account. To learn more about using Azure Artifacts to cache your NuGet packages, see [Connect to Azure Artifact feeds](https://learn.microsoft.com/en-us/azure/devops/artifacts/nuget/nuget-exe?view=azure-devops).

*   You might be using some logic in Visual Studio that isn't encoded in your pipeline. Azure Pipelines runs each command in a task sequentially in a new process. Examine the logs from the pipelines build to see the exact commands that ran in the build. To locate the problem, repeat the same commands in the same order on your development machine.

*   If you have a mixed solution that includes some .NET Core projects and some .NET Framework projects, use the **NuGet** task to restore packages specified in the _packages.config_ files. Add the **MSBuild** or **Visual Studio Build** task to build the .NET Framework projects.

*   [Azure Artifacts](https://learn.microsoft.com/en-us/azure/devops/artifacts/?view=azure-devops)
*   [Build and release tasks](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/?view=azure-devops)
*   [.NET Core CLI tools](https://learn.microsoft.com/en-us/dotnet/core/tools/)
*   [Unit testing in .NET Core projects](https://learn.microsoft.com/en-us/dotnet/core/testing/)
