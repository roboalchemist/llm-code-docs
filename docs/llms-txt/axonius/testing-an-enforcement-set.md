# Source: https://docs.axonius.com/docs/testing-an-enforcement-set.md

# Testing an Enforcement Set

When creating an Enforcement Set, you can use **Test Run** to test an Enforcement Set on *one* asset to verify the outcome before running it on *all* matching assets during a regular run. You can then view the results of the run and edit the Enforcement Set if necessary.

<Callout icon="📘" theme="info">
  Note

  * All required fields must be filled in to use Test Run.

  * The asset used by Test Run is randomly selected by Axonius.
</Callout>

**To perform a test run of an Enforcement Set**

1. Configure the Enforcement Set.

2. At the bottom of the **Create Enforcement Set** drawer, click **Test Run**.

3. The **Test Run** dialog lists the selected asset to be used for the test. Click **Asset Info** to display detailed information about the selected asset in a new browser tab.

4. Click **Test Run**. A progress dialog is displayed while the test is running. To close the Test Run dialog without running the test, click **Close**.

   ![ECSetTestRunVerify.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECSetTestRunVerify.png)

   When Test Run completes, the results of each Enforcement Action are displayed in the Test Run dialog.

   ![ECSetTestRunComplete.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECSetTestRunComplete.png)

5. To view information about an Action, click one of the links to the right. The link opens in a new browser tab.

6. Click **Close** to close the **Test Run** dialog and return to the **Create Enforcement Set** drawer.