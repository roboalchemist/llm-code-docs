# Source: https://docs.pentaho.com/pdc-use/workflows.md

# Workflows

In Pentaho Data Catalog, a workflow is a controlled sequence of steps, such as Draft, Review, and Approval, that an asset must follow before changes are published. Workflows are integrated with governed assets, so every update passes through the appropriate roles and actions before it becomes final.

Workflows promote collaborative decision-making and prevent unilateral changes to governed assets. They increase visibility into who is responsible for each step, what actions were taken, and when changes were approved. This reduces reliance on a single individual and helps ensure that updates align with your organization’s governance and business objectives.

A typical workflow follows a pattern such as:

1. An Author edits an asset, and the change enters the initial state, such as **Draft**.
2. A Reviewer validates the change, for example, checking whether definitions, classifications, or domains are correct, and moves the workflow to the next stage.
3. An Approver makes the final decision on whether to publish the change.

Although the example above uses Draft, Review, and Approval, workflow templates are fully customizable. You can define any number of intermediate stages and name them to align with your organization’s terminology and governance requirements.

Workflows help organizations enforce quality and data governance by requiring appropriate validation before changes are published. They also ensure accountability by capturing who made each change and who approved it. Once enabled, workflows support repeatable processes, maintain audit trails, and reduce the risk of incorrect or unauthorized updates being published.

## **Key concepts of workflows**

This section describes the foundational terms and concepts used in workflows. Understanding these concepts helps you work effectively with workflow-driven updates to Data Catalog assets.

### **Workflow**

A workflow defines how an asset progresses from an initial change to a final approved version. In Data Catalog, every workflow begins when an Author edits an asset within a hierarchy where workflow governance is enabled. The change places the asset into the initial state, such as **Draft**, and the workflow continues through a series of stages until the update is approved and published. All workflows end in a final state, such as **Approved**, although the stage names and number of intermediate steps may vary based on your workflow template.

The workflow lifecycle ensures that each update is reviewed, validated, and approved before it becomes visible to all users. Organizations can configure workflows with any number of stages to match their governance needs. For example, a template might include a simple two-stage flow from Draft to Approved or multiple intermediate stages for review, validation, or additional controls.

### **Workflow template**

A workflow template defines the stages, transitions, and user assignments that govern how a workflow operates in Data Catalog. When a workflow template is applied to a hierarchy, every asset in that hierarchy follows the defined workflow whenever it is created, updated, or deleted. Templates provide the foundation for enforcing consistent governance and routing changes to the right users for review and approval.

Workflow templates are highly flexible. Administrators can configure templates with any number of workflow stages to match their organizational processes. Every workflow must include a starting state, typically **Draft**, and an ending state, typically **Approved**, although the stage names can be customized. Between these start and end points, you can create one or more intermediate stages, such as Review, Approval, Legal Review, or Data Quality Check.

{% hint style="info" %}
Administrators, with the help of the Pentaho support team, can [create workflow templates using APIs](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-workflow-templates#create-a-workflow-template-using-the-workflows-api). Once published, these templates can be applied to assets to enforce lifecycle control. For more information, see [Manage workflow templates](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-workflow-templates).
{% endhint %}

A workflow template contains the following elements:

#### **Workflow stages**

Workflow stages represent the individual steps an asset moves through during its lifecycle. These stages are defined in the **Node** parameter of the workflow template. Each node corresponds to a state in the workflow, such as Draft, Review, Approval, or Approved. Administrators can configure any number of nodes to reflect the organization’s governance process. The only requirement is that the template includes a starting node (typically Draft) and a final node (typically Approved). The names of these stages can be customized to match organizational terminology.

#### **Transitions between stages**

Transitions define how a workflow moves from one stage to the next. In a workflow template, transitions are configured as **Edges** that connect one workflow stage (node) to another. Each edge represents a possible path the workflow can take, determined by the user’s action at that stage. For example, an edge may connect the Review node to the Approval node when a Reviewer determines that the update is ready for final validation.

Each edge in the template corresponds to a user action in the workflow dialog, such as submitting a draft, marking a change as ready for approval, approving an update, or rejecting it. When the user selects an action, the workflow follows the edge mapped to that action and moves to the next node defined in the template.

#### **Actions**

Actions represent the tasks that users perform to move a workflow from one stage to another. In the workflow template, actions are linked directly to **Edges**, which define the transitions between **Nodes** (the workflow stages). Each action corresponds to a specific edge in the template, and selecting that action in the UI triggers the workflow to follow that edge to the next stage.

Actions appear to users in the workflow dialog and determine how the workflow progresses. When a user selects an action, such as submitting a draft, marking a change as ready for approval, approving the update, or rejecting it. The system evaluates the edge associated with that action and transitions the workflow to the next node defined in the template. Action examples include:

* Submitting a draft
* Marking a change as ready for approval
* Approving or rejecting a change
* Refusing a task
* Assigning the next participant

#### **Roles and user assignments**

In a workflow template, roles and user assignments are defined on the **Edges**, which represent the transitions between workflow stages. Each edge specifies which roles are eligible to act when the workflow moves from one node to the next. This determines who can perform the action associated with that transition, such as submitting a draft, performing a review, or approving a change. Additionally, some role restrictions apply. For example, the Author cannot act as the Reviewer or Approver, and the Reviewer and Approver must be two separate users.

Each edge includes an **availableAssignees** list that contains the roles and communities permitted to act on that transition. When a workflow reaches a point where an action is required, Data Catalog reads the availableAssignees for the current edge and displays the corresponding users in the **Assign To** dropdown. For more information about individual roles in Data Catalog, see [pdc-user-roles-and-permissions](https://docs.pentaho.com/pdc-use/pdc-user-roles-and-permissions "mention").

#### **Workflow triggers**

A trigger defines the event that starts a workflow. In Data Catalog, assets would be governed once a workflow template is applied. The workflow becomes active when a user makes changes to the governed asset, such as creating, updating, or deleting it. Applying a workflow template simply enables governance for that hierarchy; the template becomes active only when a user makes a change to a governed asset.

When a workflow is triggered, the system immediately creates a workflow instance and moves the asset to the first workflow stage, defined as the initial node in the template. In most templates, this stage is named **Draft**, although the name can vary. From this point onward, the asset follows the lifecycle defined by the template’s nodes, edges, and actions until it reaches the final approved state.

#### **Decisions**

Decisions determine how a workflow progresses when multiple transition paths are available from a given workflow stage. In Data Catalog, when multiple transitions are available from a stage, the user’s choice determines the workflow's path. For example, from the **In Review** node, the user may have two possible decisions:

* Move forward to the **Approved** node
* End the workflow at the **Rejected** node

### **Workflow instance**

A workflow instance is a runnable version of a workflow template that is created for an asset. For example, an instance is created when a template is applied to a glossary, and an author creates, updates, or deletes an asset within that glossary. Each workflow instance tracks all actions, assignments, comments, timestamps, and decisions made throughout the lifecycle. It also determines the asset's current state and who is responsible for the next action.

### **Asset locking**

During all active workflow stages, the asset is locked for editing but remains viewable. It unlocks only when the workflow reaches a final state, such as Approved or Rejected. This prevents conflicting updates, unauthorized changes, and accidental overwrites during the workflow lifecycle.

Asset locking applies to all assets within the hierarchy where workflow governance is enabled.

### **Role restrictions and governance rules**

The workflow applies specific restrictions to ensure governance, separation of duties, and consistent lifecycle control across all workflows. These rules define what each participant can and cannot do and ensure that the review and approval process follows a compliant, auditable structure. The workflow enforces the following restrictions to maintain governance:

* Templates are configured by role, not by individual users.
* The Author cannot be assigned to review or approve their own changes.
* Only eligible assignees, as defined in the workflow template, appear in assignment lists.
* Actions are visible only to users responsible for the current workflow state.

### **Notifications**

Any change to the workflow state triggers a notification to the next assigned participant. Notifications appear in the Data Catalog notification panel and include the workflow status, asset name, and the user who performed the previous action.
