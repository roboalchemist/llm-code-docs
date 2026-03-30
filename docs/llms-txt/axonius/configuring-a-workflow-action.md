# Source: https://docs.axonius.com/docs/configuring-a-workflow-action.md

# Configuring an Action Node

You can set up an Action node within a workflow that executes an Enforcement Action from the **Select Action** pane. For detailed information on each Enforcement Action and its fields, refer to the [Enforcement Actions Library](/docs/action-library).

**To select and configure a workflow Action**

1. **Select the Enforcement Action**: Click the **Action** node, and in the **Select Action** right pane,[choose the desired Enforcement Action](/docs/create-ec-set#selecting-the-enforcement-set-action) for your Workflow's Action node.
   * The selected action appears in the **Action** node on the Workflow canvas.
   * The **Action Setup** pane automatically opens.

2. **Name and configure the Action**:
   * The default **Action name** begins with *workflow*\_. You can either use this default name or enter a custom name.
   * (Optional)[Configure dynamic values for this action](/docs/configuring-dynamic-value-statements-for-workflow-actions) with values from Adapter fields, Event fields, and/or Action fields.
   * Fill in all **Required Fields** and any optional additional fields for the action. Click the **?** icon next to the Enforcement Action name to access detailed documentation on these fields.

3. If the selected Enforcement Action is of the Create Issue/Incident/Ticket category, a **Link with a Case** button appears. Click it to open the **Create A Case Set** wizard and [create a Case Set](/docs/create-a-case-set#creating-a-case-set-using-the-wizard).

4. If the selected Enforcement Action is [**Create new case**](/docs/create-case), a **Link with a Ticket** button appears. Click it to open the **Create A Case Set** wizard and [create a Case Set](/docs/create-a-case-set#creating-a-case-set-using-the-wizard).

5. **Configure Action assets**: By default, a non-triggering Action operates on assets resolved from the previous node.[You can modify the Action to run on other assets](#modifying-the-action-assets) as needed.
   * If this Action runs on **All Assets** and follows an **Action Condition** node, by default, it only runs on assets that match the latest condition. This can be optionally disabled. Learn more about [this option](#running-action-on-assets-matching-latest-condition).

## Stopping a Workflow when an Action Fails

You can configure Action nodes to stop a workflow from further processing when the action fails.

In the Action settings, enable **Stop the workflow when this action fails**. When the action fails, the workflow is exited immediately.

<Image align="center" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/WFActionStopOnFail.png" />

## Modifying the Action Assets

By default, an action is set to run on the asset resolved by the node directly preceding it:

* An Action following an Event node runs on the asset resolved by that Event.
* An Action following another Action node runs on the single or all assets resolved from that previous Action node.
* If an action that runs on **All Assets** follows an **Action Condition** node (anywhere above it in the Workflow path), it defaults to running only on resolved assets that match the latest Action Condition.

You can change this default behavior to run the action on:

* Assets resolved by any previous node in the Workflow (either the first or all assets).
* The results of a new query (either the first or all assets).
* The default asset (reverting to the previous node's asset).
* Resolved assets that do not match the latest condition when following an Action Condition (anywhere above it in the Workflow path).

**To modify the asset that the Action runs on**

1. Next to the **Runs on** action (see above screen), click the **Edit Asset** pencil icon  ![PencilEditIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PencilEditIcon.png)

   ![EditActionAsset](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditActionAsset.png)

2. Choose one of the following options for the action asset:
   * [A resolved asset from any previous node in the Workflow](#running-action-on-resolved-assets-from-previous-nodes).
     * [The first or all assets that meet the criteria of a Query](#running-action-on-first-or-all-assets-resulting-from-a-query).
     * [The asset(s) resolved from the previous node](#resetting-action-to-run-on-default-assets).

3. Click **Apply**.
   * If subsequent nodes exist, a warning message appears, stating that the asset change will propagate to all subsequent actions in the same path.
   * Click **Change Asset** to confirm.
   * The name of the new asset is preceded by 'Custom'.

### Running the Action on Resolved Assets from Previous Nodes

Workflow data, including resolved assets, is stored in the Workflow Data repository. Resolved assets are identified as:

* *Action\[node UUI].* (for actions)
* *Event\[node UUI].* (for events)

**To select resolved assets from a previous node**

1. From the **Run action on resolved assets from previous nodes** dropdown (open by default; if not, click **Select Resolved Assets From Previous Nodes**), select a resolved asset.
   * **Example:** You can choose to run the action on User assets from a previous Event node or Vulnerability assets from a previous Action node.
     ![RunActionResolvedAssetsPrevNodes](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunActionResolvedAssetsPrevNodes.png)

<Callout icon="📘" theme="info">
  Note

  * You can expand the Workflow Data repository and [view resolved assets per Event node and Action node](/docs/using-workflow-data-from-previous-nodes#viewing-assets-resolved-from-a-previous-node). However, you can only choose a resolved asset from the dropdown in the Action Setup drawer; direct pasting from the Workflow Data repository is not supported.

  * Data from bulk action nodes is not available in the Workflow Data repository.

  * In the screen below, you can see in **Event Data** the User asset resolved from the Slack Message event.

  ![WFEventDataResolvedAssets](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WFEventDataResolvedAssets.png)
</Callout>

When an Action running on All Assets follows an Action Condition node (anywhere above it in the workflow path), you can disable the default option so that it also runs on resolved assets that do not match the Action Condition. See [Running the Action on Assets Matching Latest Condition](#running-action-on-assets-matching-latest-condition).

### Running the Action on Assets Matching Latest Condition

When an Action node running on All Assets follows a Condition node, its configuration includes the **Only assets that match the latest condition** option, which is enabled by default.

![OnlyAssetsThatMatchLatestConditionOption.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OnlyAssetsThatMatchLatestConditionOption.png)

An orange icon ![ActionAssetsLatestCondition.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionAssetsLatestCondition.png) indicates this in both:

* The **Action Setup** pane, above the Action Configuration.
  ![ActionRunsLatestCond.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionRunsLatestCond.png)

* The **Action** node following the **Action Conditions** node in the Workflow.

![NodeWithLatestCondIcon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NodeWithLatestCondIcon.png)

This option is only available if previous Action nodes (above this Action node) following this Action Condition node also have this option enabled.

* If you add an Action node above or below a filtered Action node, it is filtered by default.
* If you remove filtering from an Action node following a Condition node, filtering is removed from all its child nodes.
* You can't add filtering to an Action node if it follows an Action node without filtering.
* If you add filtering to an Action node following a Condition node, filtering is added to the Action nodes that follow it. Similarly, if an Action below an Action Condition does not have filtering enabled, filtering is not available for nested Action Conditions.

Clear the checkbox to disable this option. In this case, the action runs on all resolved assets, even those that do not match the latest condition. All nodes in the same path following this Action node will have this checkbox disabled automatically.

### Running Action on First or All Assets Resulting From a Query

You can configure the action to run on different assets by using the Query Wizard and selecting a new or existing query.

You can choose whether to run the action on either:

* **First Asset** (default): The first asset that the query returns at the time that it runs (a split run). The Workflow runs once per asset, and then proceeds to the next node after it runs on this single asset.
* **All Assets**: All assets returned from the query at the time it runs (a bulk run). In this case, the Workflow proceeds to the next node only after it runs on all assets returned from the query.

Bulk runs enable automating tasks that require processing multiple assets, supporting a wider range of scenarios and use cases. They allow you to run actions across all assets in a query.

* **Condition-Based Segmentation** - You can dynamically filter assets based on conditions, allowing for split paths in Workflows.
* **Group by segmentation (Dynamic Values)** - Aggregate assets based on a field.

<Callout icon="📘" theme="info">
  Note

  * Triggering actions can only run on the first asset returned from a query.
  * Events cannot follow Bulk actions; they can only follow Actions set to run on a first asset.
  * Bulk action data is unavailable in the Workflow Data repository.
</Callout>

The Bulk run feature supports the following use cases:

* IDM (joiner/mover/leaver) - For example, In an offboarding workflow, you could run a disable action on all service accounts owned by a user.
* Disabling service accounts in an offboarding workflow.
* Sending one user a list of assets from a query.
* Sending one Slack channel a list of 100 users.
* Case management - Ability to unify to a single Workflow.
* Unifying multiple Enforcement Actions - Running multiple Enforcement Actions on different queries in a single Workflow.

When an **Action Condition** node follows a bulk **Action** node, the assets list is split based on the defined criteria. Each child node in each of the paths (True and After) runs on every asset returned from the inherited query.

**To select assets using the Query Wizard**

1. **Open Query Wizard**: Click **Select Asset Using the Query Wizard**.
2. Under **Run action on assets that match the query**, from the **Module** dropdown, select an asset type.
3. **Configure query**: In the Query Wizard that opens,[configure your desired query using the Query Wizard](/docs/query-wizard-and-query-filter#working-with-the-query-wizard). In the Field Value box, you can type a value or [copy a field value from the Workflow Data dialog](/docs/using-workflow-data-from-previous-nodes#selecting-a-field-from-the-workflow-data-bank).
4. **Set Asset count**: In the **Additional Settings** section, under **Number of Assets**, set how many assets the action runs on:
   * **First Asset** (default) - The first asset that the query returns when it runs. The Workflow runs once per asset.
   * **All Assets** - All assets that the query returns when it runs. In this case, the Workflow proceeds to the next node only after it runs on all assets returned from the query.

### Resetting an Action to Run on Default Assets

Click **Reset to default** from either tab to reset an action that was configured to run on resolved assets from any previous node or on query results. This will revert it to run on its default assets (those resolved in the previous node).

This reset applies to the current node and all subsequent nodes in the same path.