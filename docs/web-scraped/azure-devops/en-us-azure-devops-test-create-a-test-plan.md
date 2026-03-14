# Source: https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops

Title: Create test plans and suites - Azure Test Plans

URL Source: https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Create test plans and test suites to track manual testing for sprints or milestones. That way, you can see when the testing for a specific sprint or milestone is complete. For more information about manual testing, see [What is Azure Test Plans?](https://learn.microsoft.com/en-us/azure/devops/test/overview?view=azure-devops).

For example, you're building version 1.* of your product and you might create several test cases for that version. Each of these test cases can be updated, and more added, at any time. For each development cycle and release of your product, you create a test plan and import the existing test cases into that plan. You can also, if you wish, divide the test cases into separate test suites within the plan to enable easier management and monitoring of these separate sets of test cases.

After you create your test plan, you [assign test configurations](https://learn.microsoft.com/en-us/azure/devops/test/test-different-configurations?view=azure-devops) and [assign testers](https://learn.microsoft.com/en-us/azure/devops/test/create-test-cases?view=azure-devops#assign-testers) to cover the required test matrix. These testers [run the tests](https://learn.microsoft.com/en-us/azure/devops/test/run-manual-tests?view=azure-devops) and gauge the quality of the product. Testers continue testing until the product meets exit criteria. For the next development cycle and release, you can create a new test plan and reuse the same test cases. Repeat this development-test-release cycle by importing the same test cases into each new test plan.

Because test plans refer to test cases, updates to a test case automatically reflect in all the test plans and test suites that use it.

In the next version of the product, you can reuse the existing test cases. However, a better option might be to [copy or clone the test cases](https://learn.microsoft.com/en-us/azure/devops/test/copy-clone-test-items?view=azure-devops). A copy creates a new baseline. Changes to these new test cases don't affect your previous test plans.

| Category | Requirements |
| --- | --- |
| **Access levels** | - At least **Basic** access, with permissions to view work items under the corresponding Area Path. - To add test plans and test suites, delete test artifacts, and define test configurations: [Basic + Test Plans](https://marketplace.visualstudio.com/items?itemName=ms.vss-testmanager-web) access. Or, one of the following **Visual Studio subscriptions**: - [Enterprise](https://visualstudio.microsoft.com/vs/enterprise/) - [Test Professional](https://visualstudio.microsoft.com/vs/test-professional/) - [MSDN Platforms](https://visualstudio.microsoft.com/msdn-platforms/) |
| **Permissions** | - To add or modify test plans, test suites, test cases, or other test-based work item types: **Edit work items in this node** permission set to **Allow** under the corresponding **Area Path**. - To modify test plan properties such as build and test settings: **Manage test plans** permission set to **Allow** under the corresponding **Area Path**. - to create and delete test suites, add and remove test cases from test suites, change test configurations associated with test suites, and modify a test suite hierarchy (move a test suite): **Manage test suites** permission set to **Allow** under the corresponding **Area Path**. |

For more information, see [Manual test access and permissions](https://learn.microsoft.com/en-us/azure/devops/test/manual-test-permissions?view=azure-devops).

In general, you create test plans to test requirements. Before you create a test plan, [define your backlog of requirements](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops).

1.   Sign in to your Azure DevOps project and select **Test Plans**>**Test Plans**.

![Image 1: Screenshot of opening the list of test plans page for Azure DevOps Server 2020 and Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/open-test-plans.png?view=azure-devops)

2.   Select **+ New Test Plan**.

![Image 2: Screenshot of creating a new test plan for Azure DevOps Server 2020 and Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/new-test-plan.png?view=azure-devops)

3.   Enter a name for the test plan, verify that the area path and iteration are set correctly, and then select **Create**.

![Image 3: Screenshot of adding test plan details for Azure DevOps Server 2020 and Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/test-plan-name-path-iteration.png?view=azure-devops)

To rename a test plan, do the following steps.

1.   Select **Test Plans**.

2.   Next to the test plan name, select **More Actions**>**Edit**.

![Image 4: Screenshot shows option to edit a test plan.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/rename-edit-test-plan.png?view=azure-devops)

3.   Change the name and then select **Save & Close**.

You can make other changes to the test plan here.

To delete a test plan, do the following steps.

1.   Select **Test Plans**.

2.   Next to the test plan name, select **More Actions**>**Delete**.

3.   The **Permanently delete test artifacts** dialog box explains exactly what gets deleted. Enter the test plan ID to confirm that you want to delete, and then select **Permanently delete**.

![Image 5: Screenshot shows permanently delete test artifacts dialog box.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/permanently-delete-test-artifacts.png?view=azure-devops)

Now add test suites for the backlog items that need manual tests. These tests could be user stories, requirements, or other work items based your project.

Note

Requirement tracking is supported only for test cases linked through a **Requirement-based test suite**. Work items include a User Story ([Agile](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/agile-process?view=azure-devops)), Product Backlog Item ([Scrum](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/scrum-process?view=azure-devops)), Requirement ([CMMI](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/cmmi-process?view=azure-devops)), and Issue ([Basic](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops)). The association between a requirement work item and manual test execution is only formed when the test case is linked by using a **Requirement-based test suite**.

1.   To add a suite to a test plan, select **More options** for the test suite, and then select **New Suite**>**Requirement based suite**.

![Image 6: Screenshot shows creating a requirement-based test suite for Azure DevOps Server 2020 and Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/add-requirement-based-suite.png?view=azure-devops)

You use requirement-based suites to group your test cases together. That way, you can track the testing status of a backlog item. Each test case that you add to a requirement-based test suite is automatically linked to the backlog item.

2.   In **Create requirement-based suites**, add one or more clauses to filter your work items by the iteration path for the sprint. Run the query to view the matching backlog items.

![Image 7: Screenshot shows adding clauses to filter by iteration and running the query to view results for Azure DevOps Server 2020 and Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/add-clauses-run-query.png?view=azure-devops)

3.   In the list of work items returned by the query, select the backlog items you want to test in this sprint. Select **Create suites** to create a requirement-based suite for each one.

![Image 8: Screenshot shows adding requirement-based suites for your backlog items for Azure DevOps Server 2020 and Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/select-requirement-create-suite.png?view=azure-devops)

You can create a static test suite that can contain any type of test suites. Use these test suites like folders. Drag test suites to group them in a static test plan. Drag and drop tests to reorder them.

![Image 9: Screenshot shows using drag and drop to move a test.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/drag-drop-test.png?view=azure-devops)

You can track changes to test plans and test suites. Open the work item for the test plan or test suite, then view the work item history.

For test suites, other actions are tracked in the **Test Suite Audit** field. For example, adding and removing test cases from a test suite are tracked in this field.

Export test plans, test suites, and test cases.

Select **Export test cases to CSV**.

![Image 10: Screenshot shows a test plan selected and the Export test cases to CSV option.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/export-test-cases.png?view=azure-devops)

Change the test case fields in the report by adding or removing columns from the list view of the test suite.

Important

You can't' export more than 75 Test Suites in a single operation. The email supports up to 1MB of data.

In **Test Plans** for your test plan, use the ![Image 11](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/filter-icon.png?view=azure-devops) filter icon to show the search and filter list. It can help find the tests you want.

![Image 12: Screenshot shows finding a test plan for Azure DevOps Server 2020 and Azure DevOps Services.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-a-test-plan/filter-select-test-plan.png?view=azure-devops)

*   [Test objects and terms](https://learn.microsoft.com/en-us/azure/devops/test/test-objects-overview?view=azure-devops)
*   [FAQs for manual testing](https://learn.microsoft.com/en-us/azure/devops/test/reference-qa?view=azure-devops)
*   [End-to-end traceability](https://learn.microsoft.com/en-us/azure/devops/cross-service/end-to-end-traceability?view=azure-devops)
