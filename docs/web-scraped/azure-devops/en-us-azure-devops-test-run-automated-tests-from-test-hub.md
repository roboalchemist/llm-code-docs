# Source: https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops

Title: Run automated tests from test plans - Azure Test Plans

URL Source: https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Automate test cases in your test plans and run them directly from **Azure Test Plans**. Automated tests provide you with the following benefits:

*   A user-friendly process for testers who might not be well versed in running tests in build or release workflows.
*   The flexibility to run selected tests on demand, rather than scheduled testing in build or release workflows where all tests meeting the filter criteria are run.
*   The ability to rerun a few tests that failed due to test infrastructure problems, or when you have a new build that includes fixes for failed tests.

| Category | Requirements |
| --- | --- |
| **Access levels** | - At least **Basic** access, with permissions to view work items under the corresponding Area Path. - To add test plans and test suites, delete test artifacts, and define test configurations: [Basic + Test Plans](https://marketplace.visualstudio.com/items?itemName=ms.vss-testmanager-web) access. Or, one of the following **Visual Studio subscriptions**: - [Enterprise](https://visualstudio.microsoft.com/vs/enterprise/) - [Test Professional](https://visualstudio.microsoft.com/vs/test-professional/) - [MSDN Platforms](https://visualstudio.microsoft.com/msdn-platforms/) |
| **Permissions** | - To add or modify test plans, test suites, test cases, or other test-based work item types: **Edit work items in this node** permission set to **Allow** under the corresponding **Area Path**. - To modify test plan properties such as build and test settings: **Manage test plans** permission set to **Allow** under the corresponding **Area Path**. - To create and delete test suites, add and remove test cases from test suites, change test configurations associated with test suites, and modify a test suite hierarchy (move a test suite): **Manage test suites** permission set to **Allow** under the corresponding **Area Path**. - Permissions to create and manage releases, edit a release environment, and manage deployment. For more information, see [Release permissions](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/permissions?view=azure-devops#release-pipeline-permissions) |
| **Tools and configurations** | - A [test plan](https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops) that contains your automated tests associated with automated test methods using [Visual Studio 2017](https://learn.microsoft.com/en-us/azure/devops/test/associate-automated-test-with-test-case?view=azure-devops) or [Visual Studio 2015 or earlier](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2013/dd380741(v=vs.120)). - A [build pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/apps/aspnet/build-aspnet-4?view=azure-devops) that generates builds containing the test binaries. - An app to test. You can deploy the app as part of the [build and release workflow](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops) and also use it for on-demand testing. |

1.   In **Test Plans**, choose your test plan, open the shortcut menu, and then select **Test plan settings**.

![Image 1: Screenshot shows choosing Test plan settings.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/test-plan-settings.png?view=azure-devops)
2.   In the **Test plan settings** dialog, select the build pipeline that generates builds that contain the test binaries. Both Classic and YAML build pipelines are supported. You can then select a specific build number to test, or let the system automatically use the latest build when tests run.

![Image 2: Screenshot shows selecting the build and build number.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/test-plan-settings-modal-build-selection.png?view=azure-devops)
3.   To run tests from test plans in **Azure Test Plans**, you need a release pipeline that was created from the **Run automated tests from Test Manager** template. If you have an existing release pipeline created by using this template, select it and then select the existing stage in the release pipeline for the test execution. Both Classic and YAML release pipelines are supported. Otherwise, select **Create new** in the dialog to create a new release pipeline that contains a single stage with the **Visual Studio Test** task already added.

![Image 3: Screenshot shows selecting a release pipeline or creating a new one.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/test-plan-settings-modal-build-new-release-pipeline.png?view=azure-devops)
[How do I pass parameters to my test code from a build or release pipeline?](https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops#pass-params)

4.   Assign meaningful names to the release pipeline and stage as required.

5.   If Visual Studio is already installed on the agent computer, skip this step. If not, add the [Visual Studio Test Platform Installer task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/deploy-visual-studio-test-agent-v2) to the pipeline definition.

6.   Add the [Visual Studio Test task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/vstest-v2) to the release pipeline and configure it as follows:

    *   Verify that you're using version 3 of the Visual Studio Test task.

    *   Verify that **Select tests using** is set to **Test run**. [What does this setting mean?](https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops#faq-ondemandruns)

    *   For the **vsTestVersion**, select **toolsInstaller**.

    *   If you have UI tests that run on **physical browsers** or **thick clients**, ensure that the agent is set to run as an interactive process with autologon enabled. You must set up an agent to run interactively before you queue the build or release. The **Test mix contains UI tests** checkbox doesn't configure the agent in interactive mode automatically. The checkbox is used only as a reminder to configure the agent appropriately to avoid failures.

    *   If you're running UI tests on a **headless browser**, the interactive process configuration isn't required.

    *   Select how the test platform gets provisioned, and the version of Visual Studio or the location of the test platform that is installed on the test machines.

    *   If your tests need **input parameters** such as app URLs or database connection strings, select the relevant settings file from the build artifacts. You can use the **Publish build artifacts** tasks in your build pipeline to publish the settings file in a drop location if the file isn't included in the artifacts. In the following example, the application URL is exposed in the run settings file, and is overridden to set it to a staging URL by using the **Override test run parameters** setting.

![Image 4: Screenshot shows checking the task version number setting.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/vstest-configuration.png?view=azure-devops)

For information about the option settings of the Visual Studio Test task, see [Visual Studio Test task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/vstest-v3).

7.   Choose the **Agent job** item and verify that the deployment queue is set to the one containing the machines where you want to run the tests. If your tests require special machines from the agent pool, you can add demands that select at runtime.

You might be able to minimize test times by distributing tests across multiple agents by setting **Parallelism** to **Multiple executions** and specifying the number of agents.

Note

If you're running UI tests such as Coded UI or Selenium on physical browsers such as IE, Firefox, or Chrome, the agent on the machines must be running in interactive mode and not as a service. [More details](https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops#faq-agentmode). 
8.   In the **Pipeline** page of the release pipeline, verify that the build pipeline containing the test binaries links to this release pipeline as an artifact source.

![Image 5: Screenshot shows verifying the linked build artifacts.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/run-auto-tests-from-hub-106.png?view=azure-devops)

9.   **Save** the release pipeline.

10.   If you chose **Create new** in the **Test plan settings** dialog, return to the browser page that contains your test plan settings. In the **Test plan settings** dialog, select the release pipeline and stage you saved.

![Image 6: Screenshot shows selecting the release pipeline and stage.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/run-auto-tests-from-hub-107.png?view=azure-devops)

1.   In the **Test Plans** web portal, open the test plan and select a test suite that contains the automated tests.

2.   Select the test cases you want to run, and then select **Run for web application**.

![Image 7: Screenshot shows selecting Run test.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/executing-automated-tests.png?view=azure-devops)

The build artifacts generated by your build pipeline must include the test binaries for these tests.

3.   The system checks that you selected only automated tests and ignores any manual tests. It validates the stage to ensure the Visual Studio Test task is present and has valid settings, checks your permission to create a release for the selected release pipeline, creates a test run, and then triggers the creation of a release to the selected stage.

![Image 8: Screenshot shows starting the test execution.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/test-results.png?view=azure-devops)
4.   Select **View test run** to view the test progress and analyze the failed tests. Test results include relevant information for debugging failed tests such as the error message, stack trace, console logs, and attachments.

5.   After test execution completes, the **Runs** page of the **Azure Test Plans** shows the test results. The **Run summary** page shows an overview of the run.

![Image 9: Screenshot shows the test run summary.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/run-summary.png?view=azure-devops)

The **Release** link makes it easy to find the release that ran the tests if you need to come back later and analyze the results. You can also use this link to open the release and view the release logs.

Note

Manually attaching files isn't supported for automated test results.

[What are the typical error scenarios or issues I should look out for if my tests don't run?](https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops#faq-errors)

1.   The **Test results** page lists the results for each test in the test run. Select a test to see debugging information for failed tests such as the error message, stack trace, console logs, and attachments.

![Image 10: Screenshot shows viewing the test results details.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/test-run-results.png?view=azure-devops)

2.   In **Test Plans**, go to the **Runs** page where you can find an overview of all your test runs. From here, you can open the detailed view of each test run.

![Image 11: Screenshot shows viewing the test plan.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/test-results-overview.png?view=azure-devops)

See the following frequently asked questions (FAQs) about Azure Test Plans.

**A:** Be a Project Contributor, or have the following permissions:

*   Create releases
*   Manage releases
*   Edit release stage
*   Manage deployment

For more information, see [Release permissions](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/permissions?view=azure-devops#release-pipeline-permissions).

**A:** Yes, you can override the build or stage set at the test plan level. Use the **Run with options** command. Open the shortcut menu for the test suite in the left column and select **Run with options**.

![Image 12: Screenshot shows configuring the Run with options dialog.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/run-with-options.png?view=azure-devops)

Enter the following values in the Run with options dialog and then select **OK**:

*   **Test type and runner**: Select **Automated tests using Release Stage**.
*   **Build**: Select the build that has the test binaries. The test results are associated with this build.
*   **Release Pipeline**: Select a pipeline from the list of release pipelines that can consume the selected build artifact.
*   **Release Stage**: Select the name of the stage configured in your release pipeline.

![Image 13: Screenshot shows configured Run with options dialog.](https://learn.microsoft.com/en-us/azure/devops/test/media/run-automated-tests-from-test-hub/run-with-options-configuration-modal.png?view=azure-devops)

**A:** Azure Pipelines offers a compelling orchestration workflow to obtain test binaries as artifacts and run tests. This workflow shares the same concepts used in the scheduled testing workflow, so users running tests in scheduled workflow find it easy to adapt. For example, you can clone an existing scheduled testing release pipeline.

Another major benefit is the availability of a rich set of tasks in the task catalog that enable a range of activities before and after running tests. Examples include preparing and cleaning test data, and creating and cleaning configuration files.

**A:** The test management subsystem uses the test run object to pass the list of tests selected for execution. The test task looks up the test run identifier, extracts the test execution information such as the container and test method names, runs the tests, updates the test run results, and sets the test points associated with the test results in the test run.

From an auditing perspective, the Visual Studio task provides a trace from the historical releases and the test run identifiers to the tests that were submitted for on-demand test execution.

**A:** If you run UI tests such as [coded UI](https://learn.microsoft.com/en-us/visualstudio/test/use-ui-automation-to-test-your-code) or [Selenium](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/continuous-test-selenium?view=azure-devops) tests, the agent on the test machines must be running in interactive mode with autologon enabled, not as a service, to allow the agent to launch a web browser. If you're using a headless browser such as [PhantomJS](https://phantomjs.org/), the agent can be run as a service or in interactive mode. For more information, see [Build and release agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops), [Deploy an agent on Windows](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops), and [Agent pools](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/pools-queues?view=azure-devops).

**A:** See [Get started with Selenium testing](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/continuous-test-selenium?view=azure-devops).

**A:** Currently, the on-demand workflow isn't configuration-aware.

**A:** The current capability is optimized for a single team build to be tested on-demand using an Azure Pipelines workflow. Support for multi-artifact releases, including non-Azure Pipelines artifacts such as Jenkins, is evaluated based on user feedback.

**A:** We recommend you use a separate release pipeline and stage for on-demand automated testing from Azure Test Plans because:

*   You might not want to deploy the app every time you want to run a few on-demand tests. Scheduled testing stages are typically set up to deploy the product and then run tests.

*   New releases are triggered for every on-demand run. If you have many testers who execute a few on-demand test runs every day, your scheduled testing release pipeline could be overloaded with releases for these runs. The high volume of releases makes it difficult to find releases that trigger for the pipeline that contains scheduled testing and deployment to production.

*   You might want to configure the Visual Studio Test task with a Test run identifier as an input so that you can trace what triggered the release. For more information, see [How does selecting "Test run (for on-demand runs)" in the Visual Studio Test task work?](https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops#faq-ondemandruns).

**A:** No. Microsoft Test Manager doesn't support running automated tests against Team Foundation builds. Microsoft Test Manager only works in the web-based interface for Azure Pipelines. All new manual and automated testing product development investments are in the web-based interface. No further development is planned for Microsoft Test Manager. See [Guidance on Microsoft Test Manager usage](https://learn.microsoft.com/en-us/previous-versions/azure/devops/test/mtm/guidance-mtm-usage).

**A:** They can use the same release pipeline to trigger multiple test runs in parallel if:

*   The agent pool associated with the stage has enough agents to handle parallel requests. If enough agents aren't available, runs can still be triggered but releases queue for processing until agents become available.

*   You have enough jobs to enable parallel jobs. For more information, see [Parallel jobs in Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops) or [Parallel jobs in Azure DevOps Server](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-pipelines-tfs?view=azure-devops).

*   Testers don't run the same tests in parallel. Doing so might cause results to be overwritten depending on the order of execution.

To enable multiple different test runs to execute in parallel, set the Azure Pipelines stage trigger option for [behavior when multiple releases are waiting to be deployed](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/triggers?view=azure-devops) as follows:

*   If your application supports tests running in parallel from different sources, set this option to **Allow multiple releases to be deployed at the same time**.

*   If your application doesn't support tests running in parallel from different sources, set this option to **Allow only one active deployment at a time**.

**A:** Use a [runsettings](https://learn.microsoft.com/en-us/visualstudio/test/configure-unit-tests-by-using-a-dot-runsettings-file) file to pass values as parameters to your test code. For example, in a release that contains several stages, you can pass the appropriate app URL to the test tasks in each stage. You specify the runsettings file and matching parameters in the [Visual Studio Test task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/vstest-v2).

![Image 14: Screenshot shows passing parameters to test code from a build or release pipeline.](https://learn.microsoft.com/en-us/azure/devops/test/media/pass-params-to-test-code.png?view=azure-devops)

**A:** Check and resolve issues as follows:

*   The release pipeline and stage in which I want to run tests aren't shown after I select the build.

    *   Make sure the build pipeline that's generating the build is linked as the primary artifact in the **Artifacts** tab of the release pipeline.

*   I get an error that I don't have sufficient permission to trigger a release.

    *   Configure **Create releases** and **Manage deployments** permissions for the user in the **Security** menu of the release pipeline. See [Release permissions](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/permissions?view=azure-devops#release-pipeline-permissions).

*   I get an error that no automated tests were found.

    *   Check the automation status of the selected tests. Do so in the work item for the test case, or use the **Column options** link in **Azure Test Plans** to add the **Automation status** column to the list of tests. For more information, see the [prerequisites section](https://learn.microsoft.com/en-us/azure/devops/test/run-automated-tests-from-test-hub?view=azure-devops#prerequisites).

*   My tests didn't execute, and I suspect the release pipeline is incorrect.

    *   Use the link in the **Run summary** page to access the release instance used to run the tests, and view the release logs.

*   My tests go into the error state, or remain "in-progress" even after release to the stage is triggered.

    *   Check if the release stage that you selected has the correct task and version selected. You must use version 2 or higher of the **Visual Studio Test** task. Version 1 of the task, and the **Run Functional Tests** task, aren't supported.

*   [Associate automated tests with test cases](https://learn.microsoft.com/en-us/azure/devops/test/associate-automated-test-with-test-case?view=azure-devops)
*   [Associate automated test results with requirements](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/requirements-traceability?view=azure-devops)
*   [Continuous testing scenarios and capabilities](https://learn.microsoft.com/en-us/azure/devops/test/?view=azure-devops)
