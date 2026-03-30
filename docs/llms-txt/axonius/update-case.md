# Source: https://docs.axonius.com/docs/update-case.md

# Axonius - Update case

**Axonius - Update case** automates Case updating (for example, bulk changing case priority or case status) for:

* Assets returned by the selected query or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  * To learn more about Cases, see [Case Management Overview](/docs/case-management-overview).
  * For an asset to be processed only once, it is recommended to configure the Enforcement Set to update a Case only on the delta of assets returned from the current Enforcement Set query in comparison to those returned in the previous Enforcement Set run. To enable this, under **Select Schedule**, select the **Run on added entities only** scheduling option. Note that the Enforcement Set query is the **Base Query** of the Case.
  * You can view or edit Case details and monitor its progress from the [Case drawer](/docs/viewing-and-editing-case-details).
  * Learn [how Case progress tracking is based on the selected query results](/docs/viewing-and-editing-case-details#tracking-case-progress)
</Callout>

Each time this action runs, relevant Cases are updated on assets that match the query. You can open the [Case Management page](/docs/case-management-page) to view the updates to these Cases. You can view or edit the Case details and monitor its progress from the [Case drawer](/docs/viewing-and-editing-case-details).

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Select which cases to update** - For each asset matching the selected query, select which cases to update:

  * **All related cases** - Updates all cases associated with the asset.
  * **Last created related case** - From all cases associated with the asset, only updates the most recently created case.
  * **Specific cases** - From all cases associated with the asset, only updates the cases with the specified Case IDs.
    * **Case IDs to Update** - From the dropdown that opens, select the IDs of the cases to update.
  * **This case** - Relevant only when you run this Enforcement Action on asset type=Cases. Updates the Case that the enforcement action is running on.
  * **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
    <br />

## Additional Fields

These are optional fields. Any changes you make here (e.g., to priority or status) will override the existing values in the relevant Case fields. If no changes are made, the Case field values will remain as is.

* **Type** - From the alphabetically ordered dropdown list, select the Case type that best describes the issue: **Application missing/installation**, **Data Breach Remediation**, **Groups Synchronization/Migration**, **IT  - General**, **Other Cases**, **Reduce Attack Surface**, **Security - General**, **Upgrades**, **Vulnerability Remediation**.

* **Priority** *(Default: P0)* - From the dropdown, select the priority of the Case, i.e., the urgency of the Case. Available priorities: **P0** (highest priority), **P1**, **P2**, **P3**, or **P4** (lowest priority).

* **Description** - Type a short description of the Case.

* **Status** *(Default: To Do)* - From the dropdown, select one of the following priorities: **To Do**, **Backlog**, **In Progress**, **Done**.

* **Due Date** - Click **Select Date** to open a calendar from which to select the date and time (optional) that the Case is due, and then click **Ok**.

* **Assignee** - From the dropdown, select one user only to take care of the Case. The dropdown list shows users only from your data scope. Clicking the adjacent trashcan icon clears the selected assignee.
  * You can postpone assigning a Case to a user to some time after Case creation.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).