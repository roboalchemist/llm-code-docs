# Source: https://docs.axonius.com/docs/configuring-an-action-condition.md

# Configuring Action Conditions

You can configure **Action Conditions** within your Axonius Workflows. An **Action Conditions** node allows you to control your Workflow's run path, branching it based on the outcome of the preceding **Action** node or based on a condition using data from any previous node.

## Action Condition Branches (IF/ELSE)

When you add an **Action Conditions** node after an **Action** node, it automatically creates **true** and **after** paths, and defaults to an **IF** condition structure:

* **true** path - Nodes in this path run if the defined condition is met. Otherwise, this path is bypassed.
* **after** path-
  * If the condition is met, nodes in this path run after all nodes in the **true** path have completed.
  * If the condition isn't met, the Workflow bypasses the **true** path entirely and proceeds directly to the nodes in this path.

The first node in the **after** path inherits the assets (meaning, 'Runs on') from the node immediately preceding the condition.
For example, if **Node X** is followed by a condition. and **Node Y** is the last node in the **true** path, the node following the condition in the **after** path will run on the assets resolved by **Node X**.
:::

## Building Complex Logic (ELSE IF / ELSE)

You can build advanced conditional logic by adding subsequent condition nodes on the **after** branch:

* **ELSE IF** - Add these nodes before an **ELSE** to define another specific condition that is checked only if the preceding **IF** or **ELSE IF** conditions failed.
* **ELSE** - This non-configurable branch runs only if none of the preceding **IF** or **ELSE IF** conditions were met.

If your logic requires a completely independent set of conditions, you can start a brand new **IF** condition further down the main Workflow path. This flexibility empowers you to create highly tailored and robust workflow branching.

## Types of Action Conditions

Event Conditions can be based on Workflow Data repository data, i.e., data from any previous node in the Workflow, or based on the data of the preceding **Action** node.
![ActionConditions.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionConditions.png)

### Condition is Based on Workflow Data Repository

This condition checks data stored anywhere in the **Workflow Data repository** (from any previous node) for specified criteria. This is typically used for data that is static or has been previously saved within the Workflow's run.
Example Logic: Variable.failed\_login\_count `>` 3 AND Variable.account\_status == "inactive"

### Preceding Action Node Conditions

These conditions evaluate the outcome or the resolved assets of the immediate preceding **Action** node. You can only select one or both of the following sub-types:

#### Condition Based on Action Result

The [**condition based on action result**](#adding-a-condition-based-on-action-result) directs the Workflow based on whether the preceding Action node succeeded or failed. This is critical for error handling and recovery paths.
Result Options: Success or Failure.

#### Conditions Based on Asset Criteria

[**Conditions based on asset criteria**](#adding-conditions-based-on-asset-criteria) checks if the assets resolved from the preceding **Action** node match a defined query.
Use Case: Verify if the asset affected by the action (e.g., a disabled user) still meets high-risk criteria defined by an existing query.

## Configuring Action Conditions

**To configure Action Conditions**

1. In the **Action Conditions** pane, choose either or both condition types:
   * **Condition based on data repository**.
   * **Condition based on action result** - Add a condition based on the success or failure of the action.  Proceed to [select the action result](#adding-a-condition-based-on-action-result).
   * **Condition based on asset criteria** - Add conditions to check if the asset resolved from the **Action** node matches a defined query. Proceed to [define the asset criteria](#adding-conditions-based-on-asset-criteria).
2. Build the **true** branch:
   1. Add the first node: At the end of the **true** branch, hover over the `+` icon and [add the first node](#adding-the-first-branch-node) to run if the defined conditions are met.
   2. Add more nodes: To add subsequent nodes, hover over the `+` icon following the last node in the **True** branch, and select from the available node types. Repeat this for each node you want to add to the branch.
3. Add additional conditions (**Else if** or **Else**):  Above the **after** label, hover over the `+` icon  and click one of these options:
   * **Else IF** - This opens an **Action Conditions** node for configuration, similar to a regular Condition node, allowing you to define another specific condition.
   * **Else** - This opens a non-configurable **Action Conditions** node. This branch will run if none of the preceding IF or ELSE IF conditions are met.
4. Build the **After** branch: At the end of the **after** branch, below the **after** branch label:
   1. Add the first node: At the end of the **after** branch, below the **after** branch label, hover over the `+` icon and [add the first node](#adding-the-first-branch-node). This node will run after the **true** branch completes (if the condition was met), or directly if the **true** condition wasn't met.
   2. Add more nodes: To add subsequent nodes, hover over the `+` icon following the last node in the **After** branch, and select from the available node types. Repeat this for each node you want to add to the branch.

<Callout icon="📘" theme="info">
  Note

  You must add a node to the end of either or both the **after** and **true** branches of an **Action Conditions** node. If a branch has no subsequent node and is evaluated, the Workflow will complete, and the Run History will show the Workflow status as **Completed**.
</Callout>

## Adding a Condition Based on Workflow Data Repository

You can configure an Action Condition on any previous node, using stored data from the Workflow Data repository.
For example: Variable.high\_risk\_users contains "Avi"

**To add a condition based on data from the Workflow Data repository**

1. Enable the **Condition is based on data repository** setting.
2. From a tab in the Workflow Data repository that opens, copy a variable, and paste it in the **Input** field of the condition.
3. From the **Func** dropdown, select a function or operator. Available functions and operators: **Equals**,  **Contains**, **Does not contain**, **Starts with**, **Ends with**, **Regex match**, `>`, `<`).
4. In the Field Value textbox, type a value or [copy data from a field in a previous node](/docs/using-workflow-data-from-previous-nodes) in the Workflow Data repository, and paste it.
5. To add an additional action criterion, click  `+` and repeat the process. All criteria in a single set are combined with an implicit AND logic.
6. To remove an action criterion, hover over it, and click the **x** . If it's the only criterion, its values are cleared; otherwise, it is removed.

## Adding a Condition Based on Action Result

This condition directs the workflow along either the **true** or **after** branch, depending on the Action's success or failure.

**To add an Action condition based on action result**

1. In the **Action Conditions** pane, select **Condition based on action result**.
2. From the dropdown, select **Success** or **Failure**. The chosen result appears in the **Action Conditions** box.

### Adding Conditions Based on Asset Criteria

**Asset criteria** check if the asset resolved from the **Action** node matches a defined query. For example, you can check if a  resolved Device asset has an Asset Unique ID containing a certain number. You can add an action condition based on one or more asset criteria by either creating a new query or using an existing one.

**To add a condition based on asset criteria**

1. Under the **Condition based on asset criteria** section, determine if the resolved asset matches specific criteria by doing one of the following:
   * [Define a new Query using the Query Wizard](/docs/query-wizard-and-query-filter)
   * Use an existing query - Select a predefined query to evaluate the resolved asset.
2. To add an additional asset criterion, click  `+` and repeat step 1.
3. To clear an asset criterion, hover over it and click the **x**. The criteria values are cleared.

#### Examples

* A newly created query that checks if the user resolved from the action has an Asset Unique ID containing 99.

  ![ActionConditionAssetCriteria](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionConditionAssetCriteria.png)

* An existing query that checks if the user resolved from the action is a non-admin user.

  ![ActionConditionBasedOnSavedQuery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionConditionBasedOnSavedQuery.png)

## Adding the First Branch Node

You can add any of the following nodes below the **True** and **After** branches:

* **Add Action** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddActionButton.png) - To add and [configure an Action node](/docs/configuring-a-workflow-action)
* **Add Event** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddEventButton.png) - To add and [configure another Event node](/docs/configuring-a-workflow-event)
* **Add Delay** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddDelayButton.png) - To add and [configure a Delay node](/docs/configuring-a-workflow-delay)
* **Repeat for Each** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RepeatForEachButtonB.png) - To add a **Repeat for Each** node to define a query and flow for returned assets.