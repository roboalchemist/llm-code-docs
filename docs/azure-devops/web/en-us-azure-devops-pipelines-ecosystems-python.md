# Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python

Title: Build and publish a Python app - Azure Pipelines

URL Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

In this quickstart, you create a pipeline that builds and tests a Python app. You see how to use Azure Pipelines to build, test, and deploy Python apps and scripts as part of your continuous integration and continuous delivery (CI/CD) system.

Python is preinstalled on [Microsoft-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops) for Linux, macOS, and Windows. You don't have to set up anything more to build Python projects. To see which Python versions are preinstalled, see [Software](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops#software).

| **Product** | **Requirements** |
| --- | --- |
| **Azure DevOps** | - An [Azure DevOps project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops). - An ability to run pipelines on Microsoft-hosted agents. You can either purchase a [parallel job](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops) or you can request a free tier. - Basic knowledge of YAML and Azure Pipelines. For more information, see [Create your first pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops). - **Permissions:** - To create a pipeline: you must be in the **Contributors** group and the group needs to have _Create build pipeline_ permission set to Allow. Members of the [Project Administrators group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops) can manage pipelines. - To create service connections: You must have the _Administrator_ or _Creator_ role for [service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/add-resource-protection?view=azure-devops). |
| **GitHub** | - A [GitHub](https://github.com/) account. - A [GitHub service connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops) to authorize Azure Pipelines. |

| **Product** | **Requirements** |
| --- | --- |
| **Azure DevOps** | - An [Azure DevOps project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops). - A self-hosted agent with Python 3.12 or other Python version installed. To create one, see [Self-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops#self-hosted-agents). - Basic knowledge of YAML and Azure Pipelines. For more information, see [Create your first pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops). - **Permissions:** - To create a pipeline: you must be in the **Contributors** group and the group needs to have _Create build pipeline_ permission set to Allow. Members of the [Project Administrators group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops) can manage pipelines. - To create service connections: You must have the _Administrator_ or _Creator_ role for [service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/add-resource-protection?view=azure-devops). |
| **GitHub** | - A [GitHub](https://github.com/) account. - A [GitHub service connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops) to authorize Azure Pipelines. |

Important

GitHub procedures might require you to take one or more of the following actions in GitHub:

*   Sign in.
*   Authorize Azure Pipelines.
*   Authenticate to GitHub organizations.
*   Install the Azure Pipelines app.

Follow instructions to complete the required processes. For more information, see [Access to GitHub repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops#access-to-github-repositories).

Fork the sample Python repository to your GitHub account.

1.   Go to the [python-sample-vscode-flask-tutorial](https://github.com/Microsoft/python-sample-vscode-flask-tutorial) repository.
2.   Select **Fork** at upper right.
3.   Make sure your GitHub account name is selected under **Owner**, and select **Create fork**. The fork is named the same as the parent repository by default, but you can name it something different.

1.   In your Azure DevOps project, select **Pipelines** from the left navigation menu and then select **New pipeline**, or **Create Pipeline** if this pipeline is the first in the project.
2.   On the **Where is your code** screen, select **GitHub** as the location of your source code.
3.   On the **Select a repository** screen, select your forked Python sample repository.
4.   On the **Configure your pipeline** screen, select **Starter pipeline**.

On the **Review your pipeline YAML** screen, replace the contents of the generated _azure-pipelines.yml_ file with the following code. The code does the following actions on three different versions of Python:

1.   Installs required Python version and dependencies.
2.   Packages build artifacts to a ZIP archive.
3.   Publishes the archive to your pipeline.
4.   Runs tests.

```
trigger:
- main

pool:
  vmImage: ubuntu-latest

strategy:
  matrix:
    Python310:
      python.version: '3.10'
    Python311:
      python.version: '3.11'
    Python312:
      python.version: '3.12'

steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '$(python.version)'
    displayName: 'Use Python $(python.version)'

  - script: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
    displayName: 'Install dependencies'

  - task: ArchiveFiles@2
    displayName: 'Archive files'
    inputs:
      rootFolderOrFile: $(System.DefaultWorkingDirectory)
      includeRootFolder: false
      archiveType: zip
      archiveFile: $(Build.ArtifactStagingDirectory)/$(Build.BuildId)-$(python.version).zip
      replaceExistingArchive: true

  - task: PublishBuildArtifacts@1
    inputs:
      PathtoPublish: '$(Build.ArtifactStagingDirectory)'
      ArtifactName: 'drop'
      publishLocation: 'Container'

  - script: |
      pip install pytest pytest-azurepipelines
      pytest
    displayName: 'pytest'
```

On the **Review your pipeline YAML** screen, replace the contents of the generated _azure-pipelines.yml_ file with the following code. The code does the following actions:

1.   Installs required Python version and dependencies.
2.   Packages build artifacts to a ZIP archive.
3.   Publishes the archive to your pipeline.
4.   Runs tests.

Customize _azure-pipelines.yml_ to match your project configuration.

*   If you have a different agent pool, replace the pool `name` placeholder with your pool name or `default`.
*   If necessary, change the Python `versionSpec` to a version installed on your self-hosted agent.

```
trigger:
  - main

  pool: 
    name: '<your-pool-name or default>'

  steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.12'
    displayName: 'Use Python 3.12'  

  - script: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
    displayName: 'Install dependencies'

  - task: ArchiveFiles@2
    displayName: 'Archive files'
    inputs:
      rootFolderOrFile: $(System.DefaultWorkingDirectory)
      includeRootFolder: false
      archiveType: zip
      archiveFile: $(Build.ArtifactStagingDirectory)/$(Build.BuildId).zip
      replaceExistingArchive: true

  - task: PublishBuildArtifacts@1
    inputs:
      PathtoPublish: '$(Build.ArtifactStagingDirectory)'
      ArtifactName: 'drop'
      publishLocation: 'Container'

  - script: |
      pip install pytest pytest-azurepipelines
      pytest
    displayName: 'pytest'
```

Select **Save and run**, and then select **Save and run** again. You can select **Job** on the **Summary** screen to see your job in action.

The job runs three times, once for each specified Python version. The three versions can run in parallel on different agents.

![Image 1: Screenshot of completed Python job with multiple versions.](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/media/pipeline-summary-multiple.png?view=azure-devops)

![Image 2: Screenshot of completed single Python job.](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/media/pipeline-summary-page-single-job.png?view=azure-devops)

To view your build artifacts, select the **[N] published** link on the **Summary** tab.

![Image 3: Screenshot of published build artifacts link.](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/media/published-artifacts-link.png?view=azure-devops)

The **Artifacts** page shows the published build artifacts.

![Image 4: Screenshot of published build artifacts.](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/media/pipeline-artifacts-list.png?view=azure-devops)

![Image 5: Screenshot of published build artifacts for a single job.](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/media/pipeline-artifacts-list-single-file.png?view=azure-devops)

To view the test results, select the **Tests** tab.

![Image 6: Screenshot of pipeline test results.](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/media/pipeline-test-results.png?view=azure-devops)

If you're done using the pipeline you created, you can delete it.

1.   Select **Pipelines** from your project's left navigation menu.

2.   In the pipeline list, hover over the pipeline you created, select the **More actions** icon at right, and then select **Delete**.

Or select the pipeline, and on the pipeline page, select the **More actions** icon at upper right, and then select **Delete**.

3.   Enter the pipeline name, and then select **Delete** again.

You successfully created and ran a pipeline that built and tested a Python app. You can now use Azure Pipelines to build, test, and deploy Python apps and scripts as part of your CI/CD process.

*   [Configure Python](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/customize-python?view=azure-devops)
*   [Build GitHub repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops)
