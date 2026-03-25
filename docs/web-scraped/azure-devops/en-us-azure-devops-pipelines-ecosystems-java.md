# Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java?view=azure-devops

Title: Build Java apps - Azure Pipelines

URL Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Use Azure Pipelines to automate the build, test, and deployment of Java applications. This article explains how to set up a pipeline for Java projects using tools like Maven, Gradle, or Ant. You also learn how to deploy your app to Azure services like App Service, Functions, or Kubernetes.

Use a pipeline to:

*   Build your project with [Maven](https://maven.apache.org/), [Gradle](https://gradle.org/), or [Ant](https://ant.apache.org/).
*   Run tests and code analysis tools.
*   Publish your app using a pipeline and Azure Artifacts.
*   Deploy your app to [Azure App Service](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java-webapp?view=azure-devops), [Azure Functions](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java-function?view=azure-devops), or [Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/aks-template?view=azure-devops).

If you work on an Android projects, see [Build, test, and deploy Android apps](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/android?view=azure-devops).

| **Product** | **Requirements** |
| --- | --- |
| **Azure DevOps** | - An [Azure DevOps project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops). - An ability to run pipelines on Microsoft-hosted agents. You can either purchase a [parallel job](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops) or you can request a free tier. - Basic knowledge of YAML and Azure Pipelines. For more information, see [Create your first pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops). - **Permissions:** - To create a pipeline: you must be in the **Contributors** group and the group needs to have _Create build pipeline_ permission set to Allow. Members of the [Project Administrators group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops) can manage pipelines. - To create service connections: You must have the _Administrator_ or _Creator_ role for [service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/add-resource-protection?view=azure-devops). |
| **GitHub** | - A [GitHub](https://github.com/) account. - A [GitHub service connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops) to authorize Azure Pipelines. |
| **Azure** | An [Azure subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn). |

| **Product** | **Requirements** |
| --- | --- |
| **Azure DevOps** | - An [Azure DevOps project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops). - A self-hosted agent. To create one, see [Self-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops#self-hosted-agents). - Basic knowledge of YAML and Azure Pipelines. For more information, see [Create your first pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops). - **Permissions:** - To create a pipeline: you must be in the **Contributors** group and the group needs to have _Create build pipeline_ permission set to Allow. Members of the [Project Administrators group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops) can manage pipelines. - To create service connections: You must have the _Administrator_ or _Creator_ role for [service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/add-resource-protection?view=azure-devops). |
| **GitHub** | - A [GitHub](https://github.com/) account. - A [GitHub service connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops) to authorize Azure Pipelines. |
| **Azure** | An [Azure subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn). |

Fork the following repository to your GitHub account:

```
https://github.com/MicrosoftDocs/pipelines-java
```

1.   Sign in to your Azure DevOps organization, and go to your project.

2.   Go to **Pipelines**, and then select **New pipeline** or **Create pipeline** if creating the first pipeline in the project.

3.   Follow the wizard steps, starting by selecting **GitHub** as the location of your source code. You might be redirected to GitHub to sign in. If so, enter your GitHub credentials.

4.   Select your repository. You might be redirected to GitHub to install the Azure Pipelines app. If so, select **Approve & install** to proceed.

5.   When you see the **Configure your pipeline** tab, select **Maven**, **Gradle**, or **Ant** depending on how you want to [build your code](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java?view=azure-devops#build-your-code).

6.   An `azure-pipelines.yml` file containing your pipeline definition is created in your repository and opened in the YAML editor. You can customize the pipeline by adding more tasks or modifying the existing tasks. For more information about the build tasks, see [Build your code](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java?view=azure-devops#build-your-code).

7.   When you're finished editing the `azure-pipelines.yml`, select **Save and run**.

8.   To commit the `azure-pipelines.yml` file to your repo, select **Save and run** again.

Select **Job** to watch your pipeline in action.

1.   Go to your collection and select your project.

2.   Select **Pipelines**, and then select **New pipeline** or **Create pipeline** if creating the first pipeline in the project.

3.   Perform the steps of the wizard by first selecting **GitHub Enterprise Server** as the location of your source code.

4.   Use an existing GitHub service connection or create a new one.

To create a service connection:

    1.   Select **Connect to GitHub Enterprise Server**.
    2.   Enter your GitHub Enterprise Server URL.
    3.   Enter your GitHub Enterprise Server personal access token. If you don't have a personal access token, you can create one in your GitHub Enterprise Server account. For more information, see [Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

5.   Select your repository. You might be redirected to GitHub to install the Azure Pipelines app. If so, select **Approve & install**.

6.   When you see the **Configure your pipeline** tab, select **Maven**, **Gradle**, or **Ant** depending on how you want to [build your code](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java?view=azure-devops#build-your-code).

7.   An `azure-pipelines.yml` file containing your pipeline definition is created in your repository and opened in the YAML editor. You can customize the pipeline by adding more tasks or modifying the existing tasks. For more information about the build tasks, see [Build your code](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java?view=azure-devops#build-your-code).

8.   When you're finished editing the `azure-pipelines.yml`, select **Save and run**.

9.   To commit the `azure-pipelines.yml` file to your repo, select **Save and run** again.

You can select **Job** to watch your pipeline in action.

You now have a working YAML pipeline (`azure-pipelines.yml`) in your repository that's ready for you to customize! To make changes to your pipeline, select it in the **Pipelines** page, and then **Edit** the `azure-pipelines.yml` file.

Use Azure Pipelines to build Java apps without setting up infrastructure. Build on Windows, Linux, or macOS images. Microsoft-hosted agents in Azure Pipelines have modern JDKs and other tools for Java preinstalled. To check which versions of Java are installed, see [Microsoft-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops).

Select the appropriate image by updating the following snippet in your `azure-pipelines.yml` file.

```
pool:
  vmImage: 'ubuntu-latest' # other options: 'macOS-latest', 'windows-latest'
```

See [Microsoft-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops) for a complete list of images.

As an alternative to Microsoft-hosted agents, set up [self-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops#install) with Java installed. Use self-hosted agents to save time if you have a large repo or run incremental builds.

Builds run on a [self-hosted agent](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops#install). Ensure Java and the tools required for your chosen build method are installed on the agent's host.

You can select your agent pool and the agent capabilities in the **Agent pool** and **Agent Specification** sections of the **Options** tab in the pipeline editor.

For example, specify the agent pool and an agent with the Maven capability by adding the following snippet to your `azure-pipelines.yml` file.

```
pool: 
  name: MyPool
  demands: maven
```

You can build your Java app with Maven, Gradle, Ant, or a script. The following sections show you how to add a build step to your pipeline for each method.

For a Maven build, add the following tasks to the `azure-pipelines.yml` file. Replace the values to match your project. For more information about the task options, see the [Maven task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/maven-v3).

```
steps:
- task: Maven@4
  inputs:
    mavenPomFile: 'pom.xml'
    mavenOptions: '-Xmx3072m'
    javaHomeOption: 'JDKVersion'
    jdkVersionOption: 'default'
    jdkArchitectureOption: 'x64'
    publishJUnitResults: true
    testResultsFiles: '**/TEST-*.xml'
    goals: 'package'
```

For [Spring Boot](https://spring.io/projects/spring-boot), you can use the [Maven](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/maven-v3) task as well. Make sure that your `mavenPomFile` value reflects the path to your `pom.xml` file. For example, if you're using the [Spring Boot sample repo](https://github.com/spring-guides/gs-spring-boot), your path is `complete/pom.xml`.

Set the `mavenPomFile` value if the `pom.xml` file isn't in the root of the repo. The file path value must be relative to the root of the repo, such as `IdentityService/pom.xml` or `$(system.defaultWorkingDirectory)/IdentityService/pom.xml`.

Set the **goals** value to a space-separated list of goals for Maven to execute, such as `clean package`. For details about common Java phases and goals, see [Apache's Maven documentation](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html).

For a Gradle build, add the following task to the `azure-pipelines.yml` file. For more information about these options, see the [Gradle](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/gradle-v3) task.

```
steps:
- task: Gradle@3
  inputs:
    workingDirectory: ''
    gradleWrapperFile: 'gradlew'
    gradleOptions: '-Xmx3072m'
    javaHomeOption: 'JDKVersion'
    jdkVersionOption: 'default'
    jdkArchitectureOption: 'x64'
    publishJUnitResults: true
    testResultsFiles: '**/TEST-*.xml'
    tasks: 'build'
```

Ensure the `gradlew` file is in the repo. If it isn't, generate it by running `gradle wrapper` in the project's root directory. For information about creating a Gradle wrapper, see the [Gradle](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/gradle-v3#how-do-i-generate-a-wrapper-from-my-gradle-project).

The version of Gradle installed on the agent machine is used unless your repo's `gradle/wrapper/gradle-wrapper.properties` file has a `distributionUrl` property that specifies a different Gradle version to download and use during the build.

Set the `workingDirectory` value if the `gradlew` file isn't in the root of the repo. The directory value should be relative to the root of the repo, such as `IdentityService` or `$(system.defaultWorkingDirectory)/IdentityService`.

Adjust the `gradleWrapperFile` value if your `gradlew` file isn't in the root of the repo. The file path value should be relative to the root of the repo, such as `IdentityService/gradlew` or `$(system.defaultWorkingDirectory)/IdentityService/gradlew`.

Adjust the **tasks** value for the tasks that Gradle should execute, such as `build` or `check`. For more information about common Java Plugin tasks for Gradle, see [Gradle's documentation](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_tasks).

With Ant build, add the following task to your `azure-pipelines.yml` file. Change values, such as the path to your `build.xml` file, to match your project configuration. For more information about these options, see the [Ant](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/ant-v1) task. If using the sample repo, you need to provide a `build.xml` file in your repo.

```
steps:
- task: Ant@1
  inputs:
    workingDirectory: ''
    buildFile: 'build.xml'
    javaHomeOption: 'JDKVersion'
    jdkVersionOption: 'default'
    jdkArchitectureOption: 'x64'
    publishJUnitResults: false
    testResultsFiles: '**/TEST-*.xml'
```

To build with a command line or script, add one of these snippets to the `azure-pipelines.yml` file.

The `script:` step runs an inline script using Bash on Linux and macOS, and Command Prompt on Windows. For details, see the [Bash](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/bash-v3) or [Command line](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/cmd-line-v2) task.

```
steps:
- script: |
    echo Starting the build
    mvn package
  displayName: 'Build with Maven'
```

This task runs a script file that is in your repo. For details, see the [Shell Script](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/shell-script-v2), [Batch script](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/batch-script-v1), or [PowerShell](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/powershell-v2) task.

```
steps:
- task: ShellScript@2
  inputs:
    scriptPath: 'build.sh'
```

Publish your build output to your pipeline. Package and publish your app in a Maven package or a _.war/jar_ file to deploy it to a web application.
