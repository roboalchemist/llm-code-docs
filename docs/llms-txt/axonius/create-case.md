# Source: https://docs.axonius.com/docs/create-case.md

# Axonius - Create case

**Axonius - Create case** automates Case creation. Each time the Enforcement Set runs, a new Case is created on the [Case Management page](/docs/case-management-page) for:

* Assets returned by the selected query or assets selected on the relevant asset page.

Creating a Case using this Enforcement Action helps you track, monitor, and remediate similar assets as they enter the system and match the query over time.

<Callout icon="📘" theme="info">
  Note

  * To learn more about Cases, see [Case Management Overview](/docs/case-management-overview).
  * For an asset to be processed only once by a Case, it is recommended to configure the Enforcement Set to create a Case only on the delta of assets returned from the current Enforcement Set query in comparison to those returned in the previous Enforcement Set run. To enable this, under **Select Schedule**, select the **Run on added entities only** scheduling option. Note that the Enforcement Set query is the **Base Query** of the Case.
  * You can view or edit Case details and monitor its progress from the [Case drawer](/docs/viewing-and-editing-case-details).
  * Learn [how Case progress tracking is based on the selected query results](/docs/viewing-and-editing-case-details#tracking-case-progress)
</Callout>

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Case Title** - Type a name for the Case. Recommended that it should be a meaningful name.

* **Type** - From the alphabetically ordered dropdown list, select the Case type that best describes the issue: **Application missing/installation**, **Data Breach Remediation**, **Groups Synchronization/Migration**, **IT  - General**, **Other Cases**, **Reduce Attack Surface**, **Security - General**, **Upgrades**, **Vulnerability Remediation**.

* **Priority** *(Default: P0)* - From the dropdown, select the priority of the Case, i.e., the urgency of the Case. Priorities range from **P0** (highest) to **P4** (lowest ).

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Description** - Type a short description of the Case.

* **Status** *(Default: To Do)* - From the dropdown, select the current status of the Case: **To Do**, **Backlog**, **In Progress**, **Done**.

* **Due date** *(optional; default: No due date)* - Set a deadline for resolving the Case using one of these options:
  * **No due date** (default) - There is no specific deadline.
  * **On** - Choose a specific date and time (optional) from the calendar. Click the calendar icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CalendarIcon.png) to open the calendar, select the desired due date and optionally, a time, and then click **Ok**.
  * **After** - Set a due date relative to the current date. In the first dropdown, select the number. In the second dropdown, select the unit of time: **Hours**, **Days**, **Weeks**, or **Months**. For example, '3 Days After' sets the due date to three days from the current date.

* **Assignee** - From the dropdown, select one user only to be responsible for the Case. The dropdown list only shows users within your data scope. Clicking the adjacent trashcan icon clears the selected assignee.
  * You can postpone assigning a Case to a user to some time after Case creation.

* **Additional Queries** - Link one or more optional queries to the Case.
  1. From the **Module** dropdown, select an asset type.
  2. From the **Select Query** dropdown, select an existing query for the selected asset type, or click **+ Add Query** to create a new query (if available for the chosen module). Learn more about [creating a new query](/docs/chart-query-configuration#creating-a-new-query).
  3. Click the `+` button to select an additional query. The Case does not track these queries. Clicking the adjacent trashcan icon deletes the added query.
  4. Hover over a selected Query and click the **View or Edit Query** icon to verify the query or if necessary,[modify the Query](/docs/chart-query-configuration#viewing-and-editing-a-query).

* **Linked Enforcements** - Link one or more Enforcement Sets to the Case.
  1. From the **Select Enforcement** dropdown, select a Enforcement Set to link to the Case.
  2. Click the `+` button to select each additional Enforcement Set to link.
  3. Click the adjacent trashcan icon to clear the selected Enforcement Set.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).