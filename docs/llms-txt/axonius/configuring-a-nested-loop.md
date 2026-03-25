# Source: https://docs.axonius.com/docs/configuring-a-nested-loop.md

# Configuring a Nested Loop

This feature enables Loop Runs, allowing a Workflow to process a collection of assets sequentially within a single run. This is essential for complex automation, consolidated reporting, and multi-entity tasks.
When a Workflow is triggered by data (a query or Event) that returns multiple assets, Axonius offers two distinct processing methods:

* **Split Run** (default) - Each asset triggers a separate, independent Workflow run. While this ensures specific handling of each asset, it can limit data sharing across individual runs, making consolidated reporting and multi-asset Workflows more complex. This is best for simple, single-asset actions where consolidated reporting isn't critical.
* **Loop Run** (via **Repeat for Each**) - The Workflow processes all assets sequentially within a single run by iterating through them. This method allows for seamless data sharing and collective handling across all assets, giving you greater control over how your Workflows process multiple assets. All assets are processed by the Nested Loop before the main Workflow continues. This method is useful for complex, multi-asset automation and consolidated reporting.

You can implement Loop Runs by configuring Nested Loops within your main Workflows. A Nested Loop enables you to run a group of tasks on each asset returned from a query or on assets resolved from a previous node. This makes your Workflows more robust and versatile, especially for scenarios requiring iteration over lists or multiple objects.

## Key Features

The **Repeat for Each** node defines a Nested Loop that iterates over a specified set of assets before exiting back to the main Workflow path.

* Each Nested Loop supports up to 100,000 assets.
* When the Nested Loop completes running on all specified assets, the run continues on the left branch of the **Repeat for Each** node.
* Nodes within a Nested Loop can use assets from previous nodes, both within the Nested Loop itself and from the main Workflow.
* Nodes in the main Workflow cannot run on assets from nodes within a previous Nested Loop.
* You can place one Repeat For Each node inside another (nesting), enabling multi-layered iteration for complex, multi-entity automation tasks.
* Nodes within a Nested Loop can access data from all preceding nodes in the parent workflow, including the data bank of the parent loop.
* The data bank and references generated within the Nested Loop cannot be accessed by the parent loop or by any nodes outside of the Nested Loop's execution path. This execution logic will also be clearly reflected in the run history.
* The Repeat For Each node can be placed immediately after a Workflow trigger (manual or scheduled) to start iterating over the initial data set.

## Use Case: Software Management (SM)

This example demonstrates multi-layered iteration to enforce application policies:

1. Main Workflow: Run a query for all unapproved/unmanaged applications.
2. Outer loop (Repeat for Each): Loop over each unapproved application.
3. Inner loop (Repeat for Each): For each app, run a Nested Loop over all users with access to it.
4. Action (inside inner loop): Send each user a message asking if usage is personal or business.
5. Action/Condition (inside inner loop): Based on the answer, either remove the app or do nothing.
6. Exit loop (main Workflow path): Send a final, consolidated report on all apps that were blocked.

## Creating a Nested Loop

**To create a Nested Loop**

1. Below an existing node in your Workflow, click the **Repeat for Each** button. This adds a **Repeat for Each** node to your Workflow, with two branches.
2. In the **Repeat for Each** node configuration, \[select the assets on which to run the Nested Loop]\(#selecting-assets-for-a-nested loop).
3. In the Nested Loop path (right branch), \[add the nodes]\(#building-the-nested loop) that define the tasks to be run for each asset (must start with an Action node).
4. In the main Workflow path (left branch), add nodes that the main Workflow will proceed to after the loop completes running on all assets specified in the **Repeat for Each** node. You can start this branch with an **Action**, **Delay**, or another **Repeat for Each** node.

### Selecting Assets for a Nested Workflow

In the **Repeat For Each** node configuration, you specify the assets that the Nested Loop will run on. There are two methods for asset selection:

* **Assets resolved from previous nodes** - From the Run action on resolved assets from previous nodes dropdown, select the desired set of resolved assets. The Nested Loop will run on assets that were identified or processed by a prior node in the main Workflow.
* **Assets returned from a query** - Click **Select Asset Using the Query Wizard**, and then define a specific set of assets for the Nested Loop to run on by building a query using the query wizard.

<Callout icon="📘" theme="info">
  Note

  You can modify the Nested Loop assets at any time by clicking the **Edit Asset** pencil icon  ![PencilEditIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PencilEditIcon.png) next to the **Runs on** action within the **Repeat for Each** node configuration.

  ![ModifySubWFassets.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ModifySubWFassets.png)
</Callout>

#### Running on Assets from Previous Nodes

**To configure the Nested Loop to run on assets resolved by a preceding node**

1. From the **Run action on resolved assets from previous nodes** dropdown (open by default; if not, click **Select Resolved Assets From Previous Nodes**), select the desired set of resolved assets.

<Callout icon="📘" theme="info">
  Note

  * You can expand the Workflow Data repository and [view the resolved assets per Event node and Action node](/docs/using-workflow-data-from-previous-nodes#viewing-assets-resolved-from-a-previous-node). However, you can only choose a resolved asset from the dropdown in the **Repeat For Each** drawer; you can't paste an asset from the Workflow Data repository.

  * Data from bulk action nodes is not available in the Workflow Data repository for selection.
</Callout>

#### Running on Assets from a Query

**To configure the Nested Loop to run on assets defined by a query**

1. Click **Select Asset Using the Query Wizard**.
2. Under **Run action on asset that matches the query**,[configure your desired query using the Query Wizard](/docs/query-wizard-and-query-filter#working-with-the-query-wizard).
3. Click **Apply**.

### Building the Nested Loop

The Nested Loop always starts with an **Action** node. Subsequent nodes within the Nested Loop support all standard workflow features, allowing you to add any node type (Condition, Action, Event, Delay, or another Repeat For Each) after any node in the Nested Loop.

**To build the Nested Loop**

1. Configure the first **Action** node for the Nested Loop, similar to [how you would configure any non-triggering workflow action](/docs/configuring-a-workflow-action).
2. Continue adding subsequent nodes to the Nested Loop, similar to [how you add nodes to the main Workflow](/docs/creating-a-workflow#adding-nodes-to-the-workflow).