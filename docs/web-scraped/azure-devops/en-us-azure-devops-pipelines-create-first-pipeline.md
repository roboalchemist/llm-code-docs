# Source: https://learn.microsoft.com/en-us/azure/devops//pipelines/create-first-pipeline

Title: Create your first pipeline - Azure Pipelines

URL Source: https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

This is a step-by-step guide to using Azure Pipelines to build a sample application from a Git repository. This guide uses YAML pipelines configured with the [YAML pipeline editor](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/yaml-pipeline-editor?view=azure-devops).

For more information on the different sections in a YAML pipeline, see [pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/pipeline) in the [Azure Pipelines YAML schema](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/) and [Customize your YAML pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/customize-pipeline?view=azure-devops).

If you'd like to use Classic pipelines instead, see [Define your Classic pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/define-multistage-release-process?view=azure-devops). For guidance on using TFVC, see [Build TFVC repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/tfvc?view=azure-devops).

Make sure you have the following items:

*   A GitHub account where you can create a repository. [Create one for free](https://github.com/).

*   An Azure DevOps organization. [Create one for free](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/pipelines-sign-up?view=azure-devops). If your team already has one, then make sure you're an administrator of the Azure DevOps project that you want to use.

*   An ability to run pipelines on Microsoft-hosted agents. To use Microsoft-hosted agents, your Azure DevOps organization must have access to Microsoft-hosted parallel jobs. You can either purchase a [parallel job](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops) or you can [request a free grant](https://learn.microsoft.com/en-us/azure/devops/pipelines/troubleshooting/troubleshoot-start?view=azure-devops#check-for-available-parallel-jobs).

*   [Java](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline#tabpanel_1_java)
*   [.NET](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline#tabpanel_1_net)
*   [Python](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline#tabpanel_1_python)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline#tabpanel_1_javascript)

To get started, fork the following repository into your GitHub account.

```
https://github.com/MicrosoftDocs/pipelines-java
```

1.   In your Azure DevOps project, select **Pipelines** from the left navigation menu.

2.   Select **New pipeline** or **Create pipeline** if this pipeline is the first in the project.

3.   On the **Where is your code** screen, select **GitHub**.

4.   You might be redirected to GitHub to sign in. If so, enter your GitHub credentials.

5.   On the **Select a repository** screen, select the repository your .NET app is in.

6.   You might be redirected to GitHub to install the Azure Pipelines app. If so, select **Approve & install**.

1.   Azure Pipelines will analyze your repository and recommend the **Maven** pipeline template.

2.   When your new pipeline appears, take a look at the YAML to see what it does. When you're ready, select **Save and run**.

3.   You're prompted to commit a new `azure-pipelines.yml` file to your repository. After you're happy with the message, select **Save and run** again.

If you want to watch your pipeline in action, select the build job.

You just created and ran a pipeline that we automatically created for you, because your code appeared to be a good match for the [Maven](https://github.com/microsoft/azure-pipelines-yaml/blob/master/templates/maven.yml) template.

You now have a working YAML pipeline (`azure-pipelines.yml`) in your repository that's ready for you to customize!

4.   When you're ready to make changes to your pipeline, select it in the **Pipelines** page, and then **Edit** the `azure-pipelines.yml` file.

Learn more about [working with Java](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java?view=azure-devops) in your pipeline.

You can view and manage your pipelines by choosing **Pipelines** from the left-hand menu to go to the pipelines landing page.

![Image 1: Screenshot of pipelines landing page.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/pipelines-overview.png?view=azure-devops)

From the pipelines landing page you can view pipelines and pipeline runs, create and import pipelines, manage security, and drill down into pipeline and run details.

Choose **Recent** to view recently run pipelines (the default view), or choose **All** to view all pipelines.

![Image 2: Screenshot of options for viewing pipeline runs on the pipelines landing page.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/view-pipelines.png?view=azure-devops)

Select a pipeline to manage that pipeline and [view the runs](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline#view-pipeline-details). Select the build number for the last run to view the results of that build, select the branch name to view the branch for that run, or select the context menu to run the pipeline and perform other management actions.

![Image 3: Screenshot of recently run pipelines.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/pipelines-overview-pipeline-context-menu.png?view=azure-devops)

Select **Runs** to view all pipeline runs. You can optionally filter the displayed runs.

![Image 4: Screenshot of pipeline runs.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/all-pipeline-runs.png?view=azure-devops)

Select a pipeline run to view information about that run.

You can choose to **Retain** or **Delete** a run from the context menu. For more information on run retention, see [Build and release retention policies](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/retention?view=azure-devops).

![Image 5: Screenshot of pipeline run context menu.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/pipeline-run-context-menu.png?view=azure-devops)

The details page for a pipeline allows you to view and manage that pipeline.

![Image 6: Screenshot of pipeline details page.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/pipeline-overview.png?view=azure-devops)

Choose **Edit** to edit your pipeline. For more information, see [YAML pipeline editor](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/yaml-pipeline-editor?view=azure-devops). You can also edit your pipeline by modifying the **azure-pipelines.yml** file directly in the repository that hosts the pipeline.

From the pipeline run summary you can view the status of your run, both while it is running and when it is complete.

![Image 7: Screenshot of pipeline run summary.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/pipeline-run-summary.png?view=azure-devops)

From the summary pane you can view job and stage details, download artifacts, and navigate to linked commits, test results, and work items.

The jobs pane displays an overview of the status of your stages and jobs. This pane may have multiple tabs depending on whether your pipeline has stages and jobs, or just jobs. In this example, the pipeline has two stages named **Build** and **Deploy**. You can drill down into the pipeline steps by choosing the job from either the **Stages** or **Jobs** pane.

![Image 8: Screenshot of pipeline jobs and stages.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/pipeline-jobs-pane.png?view=azure-devops)

Choose a job to see the steps for that job.

![Image 9: Screenshot of pipeline tasks.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/pipeline-steps-list.png?view=azure-devops)

From the steps view, you can review the status and details of each step. From the **More actions**![Image 10](https://learn.microsoft.com/en-us/azure/devops/media/icons/more-actions.png?view=azure-devops) you can toggle timestamps or view a raw log of all steps in the pipeline.

![Image 11: Screenshot of pipeline tasks content menu.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/pipeline-steps-context-menu.png?view=azure-devops)

If the pipeline is running, you can cancel it by choosing **Cancel**. If the run has completed, you can re-run the pipeline by choosing **Run new**.

![Image 12: Screenshot of cancelling a pipeline run.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/cancel-pipeline-run.png?view=azure-devops)

From the **More actions**![Image 13](https://learn.microsoft.com/en-us/azure/devops/media/icons/more-actions.png?view=azure-devops) menu you can download logs, add tags, edit the pipeline, delete the run, and configure [retention](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/retention?view=azure-devops) for the run.

![Image 14: Screenshot of pipeline run summary page more actions menu.](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/media/pipeline-run-summary-context-menu.png?view=azure-devops)

Note

You can't delete a run if the run is retained. If you don't see **Delete**, choose **Stop retaining run**, and then delete the run. If you see both **Delete** and **View retention releases**, one or more configured retention policies still apply to your run. Choose **View retention releases**, delete the policies (only the policies for the selected run are removed), and then delete the run.

Many developers like to show that they're keeping their code quality high by displaying a status badge in their repo.

![Image 15: Status badge shows Azure pipeline succeeded](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/azure-pipelines-succeeded.png?view=azure-devops)

To copy the status badge to your clipboard:

1.   In Azure Pipelines, go to the **Pipelines** page to view the list of pipelines. Select the pipeline you created in the previous section.

2.   Select ![Image 16](https://learn.microsoft.com/en-us/azure/devops/media/icons/more-actions.png?view=azure-devops) , and then select **Status badge**.

3.   Select **Status badge**.

4.   Copy the sample Markdown from the Sample markdown section.

Now with the badge Markdown in your clipboard, take the following steps in GitHub:

1.   Go to the list of files and select `Readme.md`. Select the pencil icon to edit.

2.   Paste the status badge Markdown at the beginning of the file.

3.   Commit the change to the `main` branch.

4.   Notice that the status badge appears in the description of your repository.

To configure anonymous access to badges for private projects:

1.   Navigate to **Project Settings** in the bottom left corner of the page

2.   Open the **Settings** tab under **Pipelines**

3.   Toggle the **Disable anonymous access to badges** slider under **General**

Note

Even in a private project, anonymous badge access is enabled by default. With anonymous badge access enabled, users outside your organization might be able to query information such as project names, branch names, job names, and build status through the badge status API.

Because you just changed the `Readme.md` file in this repository, Azure Pipelines automatically builds your code, according to the configuration in the `azure-pipelines.yml` file at the root of your repository. Back in Azure Pipelines, observe that a new run appears. Each time you make an edit, Azure Pipelines starts a new run.

We'll show you how to use the classic editor in Azure DevOps Server 2019 to create a build and release that prints "Hello world".

1.   Go to **Azure Repos**. (The **Code** hub in the previous navigation)

![Image 17: Repos files](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/create-first-pipeline/repos-files.png?view=azure-devops)

2.   If your project is empty, you will be greeted with a screen to help you add code to your repository. Choose the bottom choice to **initialize** your repo with a `readme` file:

![Image 18: Initialize repository](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/initialize-repo.png?view=azure-devops)

1.   Go to **Azure Repos**.

2.   Add a file.

![Image 19: On the Files tab, from the repo node, select the New File option](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/add-a-file-newnav-tfs-2018-2.png?view=azure-devops)

3.   In the dialog box, name your new file and create it.

```
HelloWorld.ps1
```
4.   Copy and paste this script.

```
Write-Host "Hello world"
```
5.   **Commit** (save) the file.

1.   Select **Azure Pipelines**, it should automatically take you to the **Builds** page.

![Image 20: Go to Builds tab](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/navigate-to-builds-tab-newnav-tfs-2018-2.png?view=azure-devops)

2.   Create a new pipeline.

![Image 21: Select the build tab button](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/builds-tab-mine-new-button-vsts-newnavon.png?view=azure-devops)

For new Azure DevOps users, this will automatically take you to the _YAML pipeline creation experience_. To get to the classic editor and complete this guide, you must turn off the **preview feature** for the _New YAML pipeline creation experience_:

![Image 22: Click settings in top right of screen and click preview features](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/preview-features.png?view=azure-devops)

![Image 23: Click toggle to turn yaml preview feature off](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/yaml-preview-feature-off.png?view=azure-devops)

3.   Make sure that the **source**, **project**, **repository**, and default **branch** match the location in which you created the script.

4.   Start with an **Empty job**.

5.   On the left side, select **Pipeline** and specify whatever **Name** you want to use. For the **Agent pool**, select **Hosted VS2017**.

6.   On the left side, select the plus sign **( + )** to add a task to **Job 1**. On the right side, select the **Utility** category, select the **PowerShell** task from the list, and then choose **Add**.

![Image 24: Add the build task to the job](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/builds-tab-add-task-azure-devops-newnavon.png?view=azure-devops)

7.   On the left side, select your new **PowerShell** script task.

8.   For the **Script Path** argument, select the ![Image 25](https://learn.microsoft.com/en-us/azure/devops/media/icons/more-actions.png?view=azure-devops) button to browse your repository and select the script you created.

![Image 26: Select your script](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/powershell-task-1-azure-devops-newnavon.png?view=azure-devops)

9.   Select **Save & queue**, and then select **Save**.

1.   On the **Tasks** tab, select the plus sign **( + )** to add a task to **Job 1**.

2.   Select the **Utility** category, select the **Publish Build Artifacts** task, and then select **Add**.

![Image 27: Add the publish artifact task](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/publish-artifact-task-tfs-2018-2.png?view=azure-devops)

**Path to publish**: Select the ![Image 28](https://learn.microsoft.com/en-us/azure/devops/media/icons/actions-icon.png?view=azure-devops) button to browse and select the script you created.

**Artifact name**: Enter `drop`.

**Artifact publish location**: Select **Azure Artifacts/TFS**.

1.   Select **Save & queue**, and then select **Save & queue**.

2.   On the dialog box, select **Save & queue** once more.

This queues a new build on the Microsoft-hosted agent.

3.   You see a link to the new build on the top of the page.

![Image 29: build console](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/build-console-link-to-new-build-azure-devops-newnavon.png?view=azure-devops)

Choose the link to watch the new build as it happens. Once the agent is allocated, you'll start seeing the live logs of the build. Notice that the PowerShell script is run as part of the build, and that "Hello world" is printed to the console.

![Image 30: Watch in the build console](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/build-console-azure-devops-newnavon.png?view=azure-devops)

4.   Go to the build summary. On the **Artifacts** tab of the build, notice that the script is published as an artifact.

![Image 31: Open the build console to see the artifact](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/artifacts-explorer-azure-devops-newnavon.png?view=azure-devops)

![Image 32: Open the PowerShell task in the build console](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/powershell-task-2-azure-devops-newnavon.png?view=azure-devops)

Now you can see the results of your changes. Go to **Azure Pipelines** and select **Queued**. Notice under the **Queued or running** section that a build is automatically triggered by the change that you committed.

![Image 33: Build a summary PowerShell script log](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/build-summary-powershell-script-log-azure-devops-newnav.png?view=azure-devops)

1.   Go to the **Pipelines** tab, and then select **Releases**.

2.   Select the action to create a **New pipeline**. If a release pipeline is already created, select the plus sign **( + )** and then select **Create a release pipeline**.

3.   Select the action to start with an **Empty job**.

4.   Name the stage **QA**.

5.   In the Artifacts panel, select **+ Add** and specify a **Source (Build pipeline)**. Select **Add**.

6.   Select the **Lightning bolt** to trigger continuous deployment and then enable the **Continuous deployment trigger** on the right.

![Image 34: Select lightning bolt to trigger continuous deployment](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/trigger-continuous-deployment-release-environment-azure-devops-newnavon.png?view=azure-devops)

7.   Select the **Tasks** tab and select your **QA** stage.

8.   Select the plus sign **( + )** for the job to add a task to the job.

9.   On the **Add tasks** dialog box, select **Utility**, locate the **PowerShell** task, and then select its **Add** button.

10.   On the left side, select your new **PowerShell** script task.

11.   For the **Script Path** argument, select the ![Image 35](https://learn.microsoft.com/en-us/azure/devops/media/icons/actions-icon.png?view=azure-devops) button to browse your artifacts and select the script you created.

12.   Add these **Arguments**:

```
-greeter "$(Release.RequestedFor)" -trigger "$(Build.DefinitionName)"
```
13.   On the **Pipeline** tab, select the **QA** stage and select **Clone**.

![Image 36: Clone the release environment in QA](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/clone-release-environment-azure-devops-newnavon.png?view=azure-devops)

14.   Rename the cloned stage **Production**.

15.   Rename the release pipeline **Hello world**.

![Image 37: Rename the release pipeline hello world](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/rename-release-pipeline-azure-devops-newnavon.png?view=azure-devops)

16.   Save the release pipeline.

1.   Create a new release.

![Image 38: Create release - DevOps 2019 and 2020](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/create-release-azure-devops-newnavon.png?view=azure-devops)

When **Create new release** appears, select **Create**.

2.   Open the release that you created.

![Image 39: release created - DevOps 2019 and 2020](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/release-created-azure-devops-newnavon.png?view=azure-devops)

3.   View the logs to get real-time data about the release.

![Image 40: release logs - DevOps 2019 and 2020](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/release-logs-azure-devops-newnavon.png?view=azure-devops)

![Image 41: release script step final log - DevOps 2019 and 2020](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/release-script-step-final-log-azure-devops-newnavon.png?view=azure-devops)

If you configure the [Azure DevOps MCP Server](https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops), you can get help creating, understanding, and troubleshooting your first pipeline using natural language.

| Task | Example prompt |
| --- | --- |
| Create a starter pipeline | `Create a basic pipeline YAML for this repo in project <Contoso>` |
| Minimal build pipeline | `What's the smallest pipeline that will build this project in <Contoso>?` |
| Explain pipeline YAML | `Explain each section of this pipeline YAML in <Contoso>` |
| Choose an agent pool | `Which agent pool should I use for this project in <Contoso>?` |
| Scaffolding help | `Help me create my first pipeline for this repo in <Contoso>` |

| Task | Example prompt |
| --- | --- |
| Check repo access | `Can this pipeline access the repo in project <Contoso>?` |
| Verify build service permissions | `Does the build service have permission to run pipelines in project <Contoso>?` |
| Artifact publishing access | `Will this pipeline be able to publish artifacts in <Contoso>?` |
| Agent requirements | `Does this repo require a Microsoft-hosted or self-hosted agent in <Contoso>?` |
| OS selection | `What OS should the pipeline run on for this project in <Contoso>?` |

| Task | Example prompt |
| --- | --- |
| Debug a first-run failure | `Why did my first pipeline fail in project <Contoso>?` |
| Explain an error | `Explain this pipeline error in plain English for project <Contoso>` |
| Identify the failing step | `What step failed and why in the latest run for <Contoso>?` |
| Permission error help | `Why would a new pipeline fail with a permission error in <Contoso>?` |
| Targeted fix | `How do I fix this error without changing the entire pipeline in <Contoso>?` |

| Task | Example prompt |
| --- | --- |
| Production readiness | `What's missing from this pipeline for a production repo in <Contoso>?` |
| PR validation | `Should I add PR validation to this pipeline in <Contoso>?` |
| Security scans | `What security scans are recommended for first pipelines in <Contoso>?` |
| Common next steps | `What steps are commonly added after the initial pipeline in <Contoso>?` |
| Trigger recommendations | `What triggers should I use for my first pipeline in <Contoso>?` |
| Agent capabilities | `Do we already have custom agent capabilities this pipeline needs in <Contoso>?` |
| Suggest improvements | `Suggest improvements to this pipeline in <Contoso>` |

Tip

If you're using Visual Studio Code, [agent mode](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context#agent-mode) is especially helpful for scaffolding new pipelines and troubleshooting first-run failures.

You learned how to create your first pipeline in Azure. Now, Learn more about configuring pipelines in the language of your choice:

*   [.NET Core](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops)
*   [Go](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/go?view=azure-devops)
*   [Java](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/java?view=azure-devops)
*   [Node.js](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/javascript?view=azure-devops)
*   [Python](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python?view=azure-devops)
*   [Containers](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/containers/build-image?view=azure-devops)

Or, you can proceed to [customize the pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/customize-pipeline?view=azure-devops) you created.

To run your pipeline in a container, see [Container jobs](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/container-phases?view=azure-devops).

For details about building GitHub repositories, see [Build GitHub repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops).

To learn how to publish your Pipeline Artifacts, see [Publish Pipeline Artifacts](https://learn.microsoft.com/en-us/azure/devops/pipelines/publish-pipeline-artifact?view=azure-devops).

To find out what else you can do in YAML pipelines, see [YAML schema reference](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema).

If you created any test pipelines, they're easy to delete when you finish with them.

*   [Azure Pipelines UI](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline#tabpanel_1_browser)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline#tabpanel_1_azure-devops-cli)

To delete a pipeline, navigate to the summary page for that pipeline, and choose **Delete** from the **...** menu at the top-right of the page. Type the name of the pipeline to confirm, and choose **Delete**.

![Image 42: Delete pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-yaml/delete-pipeline.png?view=azure-devops)

[What is Continuous Integration?](https://learn.microsoft.com/en-us/devops/develop/what-is-continuous-integration)

[What is Continuous Delivery?](https://learn.microsoft.com/en-us/devops/deliver/what-is-continuous-delivery)

[What is DevOps?](https://azure.microsoft.com/overview/what-is-devops/)

When you're ready to get going with CI/CD for your app, you can use the version control system of your choice:

*   Clients

    *   [Visual Studio Code for Windows, macOS, and Linux](https://code.visualstudio.com/)
    *   [Visual Studio with Git for Windows](https://learn.microsoft.com/en-us/azure/devops/repos/git/share-your-code-in-git-vs?view=azure-devops) or [Visual Studio for Mac](https://visualstudio.microsoft.com/vs/visual-studio-mac/)
    *   [Eclipse](https://learn.microsoft.com/en-us/azure/devops/repos/git/share-your-code-in-git-eclipse?view=azure-devops)
    *   [Xcode](https://learn.microsoft.com/en-us/azure/devops/repos/git/share-your-code-in-git-xcode?view=azure-devops)
    *   [IntelliJ](https://learn.microsoft.com/en-us/previous-versions/azure/devops/all/java/download-intellij-plug-in)
    *   [Command line](https://learn.microsoft.com/en-us/azure/devops/repos/git/share-your-code-in-git-cmdline?view=azure-devops)

*   Services

    *   [Azure Pipelines](https://visualstudio.microsoft.com/team-services/)
    *   Git service providers such as Azure Repos Git, GitHub, and Bitbucket Cloud
    *   Subversion

If your pipeline has a pattern that you want to replicate in other pipelines, clone it, export it, or save it as a template.

![Image 43: all-definitions-build-action-menu-replicate-actions](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/all-definitions-build-action-menu-replicate-actions-newnav.png?view=azure-devops)

After you clone a pipeline, you can make changes and then save it.

After you export a pipeline, you can import it from the **All pipelines** tab.

After you create a template, your team members can use it to follow the pattern in new pipelines.

Tip

If you're using the **New Build Editor**, then your custom templates are shown at the bottom of the list.

If you're editing a build pipeline and you want to test some changes that are not yet ready for production, you can save it as a draft.

![Image 44: save-as-draft](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/save-as-draft-newnav.png?view=azure-devops)

![Image 45: edit draft - DevOps 2019 and 2020](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/edit-draft-newnav.png?view=azure-devops)

![Image 46: publish draft - DevOps 2019 and 2020](https://learn.microsoft.com/en-us/azure/devops/pipelines/media/get-started-designer/publish-draft-newnav.png?view=azure-devops)

To delete a pipeline, navigate to the summary page for that pipeline, and choose **Delete** from the **...** menu in the top-right of the page. Type the name of the pipeline to confirm, and choose **Delete**.

You can queue builds [automatically](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops) or manually.

When you manually queue a build, you can, for a single run of the build:

*   Specify the [pool](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/pools-queues?view=azure-devops) into which the build goes.

*   Add and modify some [variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops).

*   Add [demands](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/pool-demands).

*   In a Git repository

    *   Build a [branch](https://learn.microsoft.com/en-us/azure/devops/repos/git/create-branch?view=azure-devops) or a [tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging).

    *   Build a [commit](https://learn.microsoft.com/en-us/azure/devops/repos/git/commits?view=azure-devops).
