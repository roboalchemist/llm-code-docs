# Source: https://docs.pentaho.com/pdc-admin/manage-workflow-templates.md

# Manage workflow templates

Workflow templates define how workflows work in Pentaho Data Catalog. A workflow template specifies the workflow stages, the transitions between those stages, the actions users can perform, and the roles eligible to act at each stage. After you configure and apply a workflow template to an asset in a hierarchy, all assets under that hierarchy follow the governed review and approval lifecycle defined by the template.

Administrators and support teams use workflow templates to implement consistent governance rules across the hierarchical assets. Workflow templates help ensure that updates undergo the right levels of validation, support separation of duties, and prevent unapproved changes from being published.

Workflow templates are created using JSON and deployed through internal workflow APIs. In Data Catalog 10.2.10, workflow templates are created with the assistance of the Pentaho Support team. Once a template is created, administrators can apply it to glossary hierarchies from the Data Catalog user interface.

The following topics describe the workflow template structure, how to create templates using APIs, and how to apply them to assets.

***

### **Workflow template**

A workflow template defines how a workflow operates in Data Catalog. It includes the workflow stages, the transitions between them, the actions users can perform, and the roles eligible to act at each stage. In Data Catalog, workflow templates can be created and managed only through APIs using a JSON file. This topic describes the JSON structure, explains how each element works, and provides an annotated example to help administrators understand how workflows are defined.

A workflow template consists of three primary components:

* **Template metadata**: Name and description of the workflow
* **Nodes**: Workflow stages (initial, intermediate, final)
* **Edges**: Transitions between stages, including actions and role assignments

These components work together to define the full workflow lifecycle. For more information on the workflow components, see [Workflows #Key concepts of workflows](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/workflows#key-concepts-of-workflows "mention"). Data Catalog does not limit the number of workflow stages or transitions, and it allows you to implement simple approval flows or multi-stage review processes that involve different business roles. Administrators can define workflow templates to match governance requirements. When designing a template, consider:

* How many review stages are required
* Who must validate and approve changes
* Which transitions require role-based assignment
* Whether multiple branches (approve/reject) are needed
* The governance level appropriate for your organization

The following example template defines a three-stage workflow:

**Draft → In Review → Approved/Rejected**

```json
{
  "template": {
    "name": "Document Review Workflow",
    "description": "Three-step workflow: Draft → In Review → Approved/Rejected"
  },
  "nodes": [
    {
      "nodeKey": "draft",
      "name": "Draft",
      "state": "initial"
    },
    {
      "nodeKey": "in_review",
      "name": "In Review",
      "state": "intermediate"
    },
    {
      "nodeKey": "approved",
      "name": "Approved",
      "state": "final_positive"
    },
    {
      "nodeKey": "rejected",
      "name": "Rejected",
      "state": "final_negative"
    }
  ],
  "edges": [
    {
      "name": "Submit for Review",
      "fromNodeKey": "draft",
      "toNodeKey": "in_review",
      "actionKey": "submit_for_review",
      "availableAssignees": [
        {
          "type": "role",
          "id": "5b674086-b0a2-4dc2-a5f5-7d2ecad1ec79"
        },
        {
          "type": "role",
          "id": "8b49509c-7eeb-4013-83da-114af0ceb625"
        }
      ],
      "isAssigneeSelectionRequired": true
    },
    {
      "name": "Approve",
      "fromNodeKey": "in_review",
      "toNodeKey": "approved",
      "actionKey": "approve"
    },
    {
      "name": "Reject",
      "fromNodeKey": "in_review",
      "toNodeKey": "rejected",
      "actionKey": "reject"
    }
  ]
}
```

#### **Template metadata**

The template object identifies the workflow and provides a human-readable description.

```json
"template": {
  "name": "Document Review Workflow",
  "description": "Three-step workflow: Draft → In Review → Approved/Rejected"
}
```

Administrators use this information to identify the workflow template when applying it to an asset in the hierarchy.

#### **Nodes (Workflow stages)**

Nodes represent the [workflow stages](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/workflows#workflow-stages). Each node defines the name of the stage and whether it is the starting state, an intermediate stage, or a final state.

```json
"nodes": [
  { "nodeKey": "draft",     "name": "Draft",     "state": "initial" },
  { "nodeKey": "in_review", "name": "In Review", "state": "intermediate" },
  { "nodeKey": "approved",  "name": "Approved",  "state": "final_positive" },
  { "nodeKey": "rejected",  "name": "Rejected",  "state": "final_negative" }
]
```

<table><thead><tr><th width="147.3333740234375">Attribute</th><th>Description</th></tr></thead><tbody><tr><td><strong>nodeKey</strong></td><td>Unique identifier for the stage</td></tr><tr><td><strong>name</strong></td><td>Label displayed in the UI</td></tr><tr><td><strong>state</strong></td><td>Type of stage: initial, intermediate, final_positive, final_negative</td></tr></tbody></table>

A workflow template must contain one initial node and one or more final nodes, and you can add any number of intermediate nodes to design multi-stage workflows. Stage names are fully customizable.

#### **Edges (Transitions between stages)**

Edges define how the workflow moves from one stage to the next. Each edge includes the transition name, the action that triggers the transition, and the roles eligible to execute that action.

```json
"edges": [
  {
    "name": "Submit for Review",
    "fromNodeKey": "draft",
    "toNodeKey": "in_review",
    "actionKey": "submit_for_review",
    "availableAssignees": [
      { "type": "role", "id": "5b674086-b0a2-4dc2-a5f5-7d2ecad1ec79" },
      { "type": "role", "id": "8b49509c-7eeb-4013-83da-114af0ceb625" }
    ],
  },
  {
    "name": "Approve",
    "fromNodeKey": "in_review",
    "toNodeKey": "approved",
    "actionKey": "approve"
  },
  {
    "name": "Reject",
    "fromNodeKey": "in_review",
    "toNodeKey": "rejected",
    "actionKey": "reject"
  }
]
```

<table><thead><tr><th width="275.33331298828125">Attribute</th><th>Description</th></tr></thead><tbody><tr><td><strong>name</strong></td><td>Display name of the transition shown in the UI</td></tr><tr><td><strong>fromNodeKey</strong></td><td>Current workflow stage</td></tr><tr><td><strong>toNodeKey</strong></td><td>Next workflow stage</td></tr><tr><td><strong>actionKey</strong></td><td>Internal identifier for the user-triggered action</td></tr><tr><td><strong>availableAssignees</strong></td><td>PDC roles, communities, or users ID eligible to perform this transition</td></tr><tr><td><strong>isAssigneeSelectionRequired</strong></td><td>Whether the user must assign the next participant</td></tr></tbody></table>

When a user selects an action, the workflow follows the edge mapped to the corresponding actionKey. Transitions control the direction of the workflow, who can approve changes, and how the workflow ends. Edges implement the governance rules defined by your organization.

Once you have created a JSON, you can [create a workflow template using the workflows API](#create-a-workflow-template-using-the-workflows-api).

If you create a workflow template using the example template and apply it to an asset, the asset moves through the following transitions:

**Draft → In Review**

This transition occurs when the Author selects **Submit for Review** in the workflow dialog.

* The Author must assign a Reviewer if isAssigneeSelectionRequired is set to true.
* Only users whose roles match the entries in availableAssignees appear in the assignment list.
* After submission, the asset remains locked while the workflow moves to the **In Review** stage.

**In Review → Approved**

This transition occurs when the Reviewer selects **Approve**.

* The workflow moves to the **Approved** node, defined as the final\_positive state.
* The asset is unlocked, and the approved changes become visible to all users.
* No further workflow actions are available for this asset unless a new change is made.

**In Review → Rejected**

This transition occurs when the Reviewer selects **Reject**.

* The workflow transitions to the **Rejected** node, which is defined as the final\_negative state.
* The asset unlocks, allowing the Author to make further edits.
* Any new edit triggers a new workflow instance.

{% hint style="warning" %}
At all active workflow stages, the asset remains locked for editing and is only available for viewing. It unlocks only when the workflow reaches a final state, such as **Approved** or **Rejected**.
{% endhint %}

***

### **Create a workflow template using the workflows API**

This topic describes how to create a workflow template using the workflow APIs. A workflow template defines the lifecycle states, transitions, and role assignments that an asset must follow.

In PDC 10.2.10, workflow templates can be created only through APIs, with assistance from the Pentaho support team, and are managed by administrators.

Perform the following steps to create a workflow template using the API:

**Before you begin**

Ensure you have the Admin role in Data Catalog and access to the workflow APIs.

**Procedure**

1. Open the workflow templates API endpoint.

   ```bash
   POST /api/v1/workflows/workflow-templates
   ```
2. Prepare the workflow template JSON that defines the [workflow structure](#workflow-template).
3. Submit the POST request to create the workflow template.

   Example using curl:

   ```bash
   curl -X POST "https://<PDC_HOST>/api/v1/workflows/workflow-templates" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <ACCESS_TOKEN>" \
     -d @workflow-template.json
   ```
4. Verify the workflow template using the GET endpoint.

   ```bash
   GET /api/v1/workflows/workflow-templates
   ```

   Confirm that:

   * The template appears in the list
   * The states and transitions match your JSON
   * The assignable roles are correct

**Result**

You created a workflow template that defines the lifecycle states, transitions, and role assignments for the assets in a hierarchy. It is available to all assets in the hierarchy and can be applied.

**Next steps**

Apply the workflow template to an asset in a hierarchy, such as a glossary, category, or term. For more information, see [#apply-a-workflow-template-to-assets](#apply-a-workflow-template-to-assets "mention"). Additionally, you can retrieve workflow history using the Workflow APIs with the help of the [Pentaho Support](https://support.pentaho.com/hc/en-us) team.&#x20;

***

### **Apply a workflow template to assets**

Applying a workflow template enforces a governed lifecycle for all asset updates, including creation, modification, and deletion. When a workflow template is applied, every change must pass through the workflow states defined in the workflow template before it is published. This ensures that the correct users review the asset content, approve it through a consistent process, and record it with a complete audit history.

Perform the following steps to apply a workflow template to an asset. As an example, this process shows applying a workflow template to a Business Glossary:

**Before you begin**

* Ensure you have the Admin role or are the glossary creator.
* Ensure that a workflow template exists in the system and contains valid states, transitions, and role configurations.

**Procedure**

1. Click a hierarchy (**Glossary)** in the left navigation menu.

   The **Business Glossary** page opens.
2. Select an asset, such as a glossary, category, or term, where you want to apply the workflow.\
   When you apply a template to a parent, it is automatically applied to all child items. If required, you can also apply a different template at the individual level.
3. Click the **Actions** drop-down menu and select **Apply Template**.\
   The **Apply Template** dialog box opens.
4. In the **Template Name** field, select the workflow template you want to apply to the asset.\
   Only templates created through the workflow APIs appear in the list. If you don’t find the required workflow, request an admin to create it.
5. (Optional) In the **Workflow Description** box, add a description for the workflow, and click **Apply Template.**\
   The success message appears, and the applied workflow template icon is visible below the asset’s name.

**Result**

You applied a workflow template to the glossary. All changes to the glossary, its categories, and its terms now follow the workflow lifecycle defined in the template. Any future edit to a governed asset automatically starts a workflow instance in the Draft state.
