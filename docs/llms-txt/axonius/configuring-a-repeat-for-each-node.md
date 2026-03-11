# Source: https://docs.axonius.com/docs/configuring-a-repeat-for-each-node.md

# Configuring a Repeat For Each Node

Use the Repeat For Each node to create a loop that processes each asset within the same workflow.

Many workflow triggers and actions return multiple assets. By default, the workflow is run for each asset returned. Using the Repeat For Each node, a single workflow is run to process all the returned assets. This requires fewer resources than running the workflow for each asset.

When you add a Repeat For Each node, a second execution branch is created, allowing you to add nodes that will run on each returned asset. Assets returned in a previous node/step are passed to the Repeat For Each node and processed one by one.

<Image align="center" alt="Repeat For Each Loop" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/RFELoopInit.png" />

You can add a Repeat For Each node after any other node type. You can also use conditions inside a Repeat For Each node.

<Image align="center" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/ConditionWithinRFELoop.png" />

**To add and configure a Repeat For Each node:**

1. After any other node type, hover over the + and click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/RepeatForEachIcon-50.png) Repeat For Each. The Workflow Data dialog and the configuration drawer open.

   <Image align="center" border={false} width="650px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/RFEConfigAndWFDataDialog.png" />
2. Configure what assets the loop will run on. See [Selecting the Assets for the Repeat For Each Node](#selecting-assets-for-the-repeat-for-each-node).
3. Add the nodes you want to execute on each asset. During a run, each node is executed on each asset passed from a previous node.
4. When execution of the last node is completed, or an Exit Repeat node is encountered, execution returns to the main branch.

   <Image align="center" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/ExecutionAfterLoop.png" />

## Selecting Assets for the Repeat For Each Node

You must configure which assets the Repeat For Each loop will run on. The loop can run on:

* Assets returned by a selected query
* A group of assets that have been returned from any previous non-variable node within the workflow
* A list of assets from a previous node or variable within the workflow

### To run the Repeat For Each loop on assets from previous nodes or a query:

1. Select **Run on Assets**. This is the default method.
2. To run the loop on assets returned by one or more queries, click **Select assets using the Query Wizard**. Then use the Query Wizard to create one or more queries that define on which assets the loop is executed. Click **Apply**.

   <Image align="center" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/RunOnAssetsFromQuery.png" />
3. To run the loop on assets returned by a previous node in the workflow, click **Select resolved assets from previous nodes**, select the node from the **Run action on resolved assets from previous nodes** list, and click **Apply**.

   <Image align="center" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/RunOnInternalListAssetFromPreviousNode.png" />

### To run the Repeat For Each loop on a list of assets from a previous node (not a Variable node):

1. Click **Run on internal list object** and then **An asset from a previous node**
2. In **Available asset to run on from previous nodes**, select the asset that has a list field with assets.
3. In **Available list from the chosen asset**, select the specific field that contains the list of assets on which to run the loop.

   <Image align="center" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/RunOnInternalListAssetFromPreviousNode.png" />
4. Click **Apply**.

### To run the Repeat For Each loop on a list of assets from a Variable node:

1. Click **Previous variable node**.
2. In **Available variables with lists**, select the variable that contains the list of assets on which you want to run the loop.

   <Image align="center" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/RunOnInternalListAssetFromPreviousVariableNode.png" />
3. Click **Apply**.