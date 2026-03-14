# Source: https://learn.microsoft.com/en-us/azure/devops/test/create-test-cases?view=azure-devops

Title: Create and Manage Manual Test Cases - Azure Test Plans

URL Source: https://learn.microsoft.com/en-us/azure/devops/test/create-test-cases?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Create manual test cases to check that each deliverable meets your users' needs. Manual test cases define individual steps that testers perform, including shared steps across test cases. To test different data, specify parameters for the test steps. Organize your test cases by adding them to [test plans and test suites](https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops), and then assign testers to run the tests.

For more information, see [Share steps between test cases](https://learn.microsoft.com/en-us/azure/devops/test/share-steps-between-test-cases?view=azure-devops), [Repeat a test with different data](https://learn.microsoft.com/en-us/azure/devops/test/repeat-test-with-different-data?view=azure-devops), and [Test objects and terms](https://learn.microsoft.com/en-us/azure/devops/test/test-objects-overview?view=azure-devops).

Note

Test iterations support data-driven scenarios, not workflow-driven scenarios. As a best practice, if you have two test scenarios where the workflows differ, create separate test cases. For more information, see [FAQs for manual testing](https://learn.microsoft.com/en-us/azure/devops/test/reference-qa?view=azure-devops#test-cases).

| Category | Requirements |
| --- | --- |
| **Access levels** | - At least **Basic** access, with permissions to view work items under the corresponding Area Path. - To add test plans and test suites, delete test artifacts, and define test configurations: [Basic + Test Plans](https://marketplace.visualstudio.com/items?itemName=ms.vss-testmanager-web) access. Or, one of the following **Visual Studio subscriptions**: - [Enterprise](https://visualstudio.microsoft.com/vs/enterprise/) - [Test Professional](https://visualstudio.microsoft.com/vs/test-professional/) - [MSDN Platforms](https://visualstudio.microsoft.com/msdn-platforms/) |
| **Permissions** | - To add or modify test plans, test suites, test cases, or other test-based work item types: **Edit work items in this node** permission set to **Allow** under the corresponding **Area Path**. - To modify test plan properties such as build and test settings: **Manage test plans** permission set to **Allow** under the corresponding **Area Path**. - to create and delete test suites, add and remove test cases from test suites, change test configurations associated with test suites, and modify a test suite hierarchy (move a test suite): **Manage test suites** permission set to **Allow** under the corresponding **Area Path**. |

For more information, see [Manual test access and permissions](https://learn.microsoft.com/en-us/azure/devops/test/manual-test-permissions?view=azure-devops).

1.   If you haven't already, [create a test plan and requirement-based test suites](https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops).

2.   Select a requirement-based test suite and select **New Test Case**.

![Image 1: Screenshot showing test cases with New Test Case button highlighted.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/new-test-case-button.png?view=azure-devops)

Note

The [test suite](https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops) shown here comes from a User Story work item in the team's backlog board. When you add a test case to this kind of suite, you automatically link the test case to the backlog item. To create test cases this way, open the context menu for the work item and choose **Add test**. 
3.   Enter a title and select **Click or type here to add a step**.

![Image 2: Screenshot showing the steps entered for a test case.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/test-case-steps.png?view=azure-devops)

4.   Add test steps that describe the action to perform and the expected results. You can add attachments to any step. Repeat until you add all the steps for the test.

For more information, see [Share steps](https://learn.microsoft.com/en-us/azure/devops/test/share-steps-between-test-cases?view=azure-devops) and [Copy or clone stories, issues, and other work items](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/copy-clone-work-items?view=azure-devops).

You can specify configurations, such as different operating systems, web browsers, and other variations for your tests.

*   Select the test suite, select **More options**>**Assign configurations**, and in the dialog box, select your configurations.

![Image 3: Screenshot showing the Assign configurations to test suite dialog box with some options selected.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/assign-configurations-test-suite.png?view=azure-devops)

You can also assign configurations to individual test cases. Select one or more test cases > select **More options**>**Assign configuration**.

*   Make your changes and then **Save**.

For more information, see [Test different configurations](https://learn.microsoft.com/en-us/azure/devops/test/test-different-configurations?view=azure-devops).

Caution

*   **Configuration inheritance**: Changing configurations at a child suite breaks inheritance from its parent suites. The change still propagates down to lower child suites, unless a child suite already overrides it.
*   **Hidden test points**: Unassigning a configuration hides its related test points. To restore them, reassign the configuration.

How you reorder test cases depends on the suite type:

| Suite type | How to reorder |
| --- | --- |
| **Static suite** | Drag and drop test cases into the desired order in the test case list. |
| **Requirement-based suite** | Backlog priority determines the order. To change it, reorder the backlog items in the [backlog view](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops). |
| **Query-based suite** | Query sort criteria determine the order. To change it, modify the [query's sort columns](https://learn.microsoft.com/en-us/azure/devops/boards/queries/using-queries?view=azure-devops). |

When you edit a test case, you can reorder test steps to adjust the sequence of actions:

*   Select a test step, and then use the **up** and **down** arrows to move it to the desired position.
*   You can also select multiple steps and move them together.

![Image 4: Screenshot showing the arrows used to move test steps up or down.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/change-step-order.png?view=azure-devops)

Tip

If several test cases share the same steps, consider using [shared steps](https://learn.microsoft.com/en-us/azure/devops/test/share-steps-between-test-cases?view=azure-devops) to keep them in sync. When you update a shared step, the change applies to all test cases that reference it.

Add existing test cases to a test suite by using the following steps.

1.   Select a test suite. From the **New Test Case** menu, select **Add existing test cases**.

![Image 5: Screenshot showing the Add existing test cases option to select.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/add-existing-test-cases.png?view=azure-devops)

2.   Add search clauses, as needed, and then select **Run query**.

![Image 6: Screenshot showing the Add test cases to suite dialog box with the Run query button highlighted.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/add-test-case-suite.png?view=azure-devops)

3.   When you find the test cases you want, select them and choose **Add test cases**.

Tip

You can create a test case that automatically links to a requirement - User Story ([Agile](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/agile-process?view=azure-devops)), Product Backlog Item ([Scrum](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/scrum-process?view=azure-devops)), Requirement ([CMMI](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/cmmi-process?view=azure-devops)), or Issue ([Basic](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops)) - when you create a test from the board. For more information, see [Add, run, and update inline tests](https://learn.microsoft.com/en-us/azure/devops/boards/boards/add-run-update-tests?view=azure-devops).

Follow these steps to copy and paste test cases into the **Grid** view.

1.   Select the **Grid View** icon.

![Image 7: Screenshot showing the Grid View button used to open the Grid view.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/grid-view-button.png?view=azure-devops)

2.   Select one to several test cases, and then select **Edit test case(s) in grid**.

![Image 8: Screenshot showing several test cases selected with the context menu open and Edit test case(s) in grid selected.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/edit-multiple-test-cases-grid.png?view=azure-devops)

3.   Add, delete, or clear rows.

![Image 9: Screenshot showing the Grid context menu to insert, delete, or clear rows.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/grid-context-menu.png?view=azure-devops)

4.   To add multiple test cases to the test suite, select **Add test cases using grid**.

![Image 10: Screenshot showing option to add test cases using the Grid view.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/add-test-cases-grid.png?view=azure-devops)

    *   In the **List** view, use the column options to select the fields in the test case work item.

![Image 11: Screenshot showing the Column Options button.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/column-options.png?view=azure-devops)

You can view and edit these fields when you switch to the **Grid** view.

You can copy test cases and test steps from an existing Excel worksheet. Copy the columns from Excel that you want to use for the title, action, and expected results fields. This action doesn't copy column formatting, other than multiline, from the worksheet. Paste these columns into the **Grid** view, edit if necessary, and save them.

![Image 12: Screenshot showing the save option for steps copied from Excel to the Grid view.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/save-test-cases-grid.png?view=azure-devops)

You can copy data from the **Grid** view and paste it into your Excel worksheet. This action doesn't copy test step formatting, other than multiline, into the worksheet.

Note

Don't use the Teams plugin for Excel to add or update test case work items. Excel can't parse the format that stores test steps, and this limitation can affect test case work item formatting.

Assign test cases so that different testers can run them. You can assign all test cases in a test suite to multiple testers, which is useful for acceptance testing.

Testers need [Basic + Test Plans access](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops) to run tests from Azure Test Plans.

1.   In the context menu for a test suite, select **Assign testers to run all tests**.

![Image 13: Screenshot showing the Assign testers to run all tests option in a test suite context menu.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/assign-testers-all-tests.png?view=azure-devops)

The **Select testers to run all the tests in suite** dialog box opens.

2.   Add or remove testers from the list. After you select the testers, select **Send email** and edit the message so they know that tests are ready for them to run.

![Image 14: Screenshot showing Assigning testers to run all tests dialog box with Search users and Send email called out.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/select-testers-dialog-box.png?view=azure-devops)

The email contains a link that testers can open to see the list of assigned tests.

Assign an individual test case to a tester.

1.   In the **Execute** tab for a test suite, select a test, and then open the context menu.

![Image 15: Screenshot showing the context menu for a test case with the Assign tester option selected.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/assign-tester-test-case.png?view=azure-devops)

2.   Select **Assign tester**. Search for and select a tester.

You can open a test case to view it or edit it.

1.   To open a test case in a test suite, in the **Define** tab, double-click the name of the test case.
2.   In the **Execute** tab, select a test case, open its context menu, and select **Edit test case**.

![Image 16: Screenshot showing the Edit test case option for a test case in the context menu.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/open-test-case-edit.png?view=azure-devops)

You can link a test case to test suites, requirements, and bugs. To see linked items, in the **Define** tab, open the context menu for a test case, and select **View Linked Items**.

![Image 17: Screenshot showing the Linked Items dialog box for a test case with options to view Test Suites, Requirements, and Bugs.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/view-linked-items.png?view=azure-devops)

You can edit more than one test case at a time. Select several test cases in a test suite and select **Edit test case(s)**.

![Image 18: Screenshot showing the Edit work items dialog box where you can select fields and values for several test cases.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/bulk-edit-work-items.png?view=azure-devops)

Select a **Field** and enter a **Value**. Select **Add new field** to add another field-value pair.

You can tag test cases and view only the ones with specific tags. For example, tag all the tests related to signing in so that you can rerun these tests if a bug is fixed for that page. You can filter on that tag from the **Test Plans** web portal.

To add new tags to work items, have at least **Basic** access and have the project-level **Create new tag definition** permission set to **Allow**. For more information, see [Add work item tags](https://learn.microsoft.com/en-us/azure/devops/boards/queries/add-tags-to-work-items?view=azure-devops).

You can add and edit tags when you edit a test case, or bulk edit tags in the **Grid** view. You can also create suites based on queries when you use tags.

![Image 19: Screenshot showing tags for a test case.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/test-case-tags.png?view=azure-devops)

You can rename or remove test cases from a test suite.

**Rename a test case**: Open the test case from the context menu, and then edit the name.

![Image 20: Screenshot showing a test case with its context menu with Open test case selected.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/open-test-case-option.png?view=azure-devops)

![Image 21: Screenshot showing a test case with its name selected to edit.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/change-test-case-name.png?view=azure-devops)

**Remove a test case**: From the context menu for the test case, select **Remove**.

![Image 22: Screenshot showing removed test case.](https://learn.microsoft.com/en-us/azure/devops/test/media/create-test-cases/remove-test-case.png?view=azure-devops)

To permanently delete test plans and test suites, be a member of the Project Administrators group or have the Area Path node-level [**Manage test plans** or **Manage test suites**](https://learn.microsoft.com/en-us/azure/devops/organizations/security/set-permissions-access-work-tracking?view=azure-devops#manage-test-artifacts) permission set to **Allow**. To manage or delete test artifacts, you must also have your [access level](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops) set to **Basic + Test Plans** or **Visual Studio Enterprise**. For more information, see [Delete test artifacts in Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/delete-test-artifacts?view=azure-devops).

*   [Copy or clone stories, issues and other work items](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/copy-clone-work-items?view=azure-devops)
*   [Delete test artifacts in Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/delete-test-artifacts?view=azure-devops)
*   [FAQs for manual testing](https://learn.microsoft.com/en-us/azure/devops/test/reference-qa?view=azure-devops#test-cases)
*   [Repeat a test with different data](https://learn.microsoft.com/en-us/azure/devops/test/repeat-test-with-different-data?view=azure-devops)
*   [Share steps between test cases](https://learn.microsoft.com/en-us/azure/devops/test/share-steps-between-test-cases?view=azure-devops)
*   [Test different configurations](https://learn.microsoft.com/en-us/azure/devops/test/test-different-configurations?view=azure-devops)
*   [Test objects and terms](https://learn.microsoft.com/en-us/azure/devops/test/test-objects-overview?view=azure-devops)
