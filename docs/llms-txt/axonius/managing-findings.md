# Source: https://docs.axonius.com/docs/managing-findings.md

# Managing Findings

## Editing the Custom Finding Configuration

You can edit the configuration of any Custom Finding in the **Findings** table.

**To edit the Custom Finding configuration**

1. In the [**Findings** table](/docs/findings-center-page#findings-table), click a Finding.
2. In the **Finding Info** drawer that opens, in the header, click the **Go to Finding** ![PencilEditIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PencilEditIcon.png) icon.
3. In the **Finding Configuration** drawer that opens, update fields and settings, as required. Refer to [Creating a Finding](/docs/creating-a-finding) for field and setting explanations. The **Save Changes** button becomes enabled.
4. [Modify the external notification](#modifying-the-external-notification) or [Remove the external notification](#removing-the-external-notification), if required.
5. Click **Save Changes**.

<Callout icon="📘" theme="info">
  Note

  * When you modify a Finding's configuration, it might begin triggering alerts on different assets than before.
    For example, when you configure the Finding with a different query.
  * When you [pivot from the latest alert in the Alerts History tab to the list of assets that triggered the alert](/docs/viewing-alert-information#viewing-alert-assets), it opens the list of assets resulting from the alert based on the original rule (i.e., before the rule was modified). This is because the asset list is based on a historical snapshot of the assets at the time of the alert .
</Callout>

### Modifying the External Notification

In a Custom Finding, you can choose an alternate enforcement action for an external notification or modify the configuration of the existing one.

**To modify the external notification**

1. Hover over the defined external notification, and click the ![ChangeStatusIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeStatusIcon.png) Edit icon that appears (see figure below).
2. Modify the configuration of the external notification, by doing one of the following:
   * In **Select Action**, choose another enforcement action and fill in the required fields.
   * Modify the configuration of the current enforcement action.
3. Click **Apply**.

### Removing the External Notification

You can remove an external notification from a Findings Custom rule.

**To remove an external notification**

1. Hover over the defined external notification, and click the ![TrashcanIconBlackonWhite](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrashcanIconBlackonWhite.png) Trashcan icon that appears (see figure below). The external notification is removed.
2. Click **Apply**. The external notification is removed from the **Findings Notification Enforcements** folder in the Enforcement Center.

![ExternalNotificationsHover](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExternalNotificationsHover.png)

## Updating the Status of a Finding Alert

In the row of a Finding in the **Findings** table, you can manually change the status of its latest alert. Learn [how to change the alert status](/docs/findings-center-page#editing-the-status-of-the-latest-alert).
You can also change the status of a Finding's alert [in the **Alerts History** table - **Status** column](/docs/viewing-finding-information#viewing-the-alerts-of-a-finding).

## Deleting Findings

From the **Findings** table, you can delete one or more Findings (Custom).

**To delete one or more Findings**

1. In the [**Findings** table](/docs/findings-center-page#findings-table), hover over a row of a single Finding, and then at the end of the row, click the **Delete Finding** ![TrashcanIconBlackonWhite](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrashcanIconBlackonWhite.png) icon, or select the checkboxes of one or more Findings, and then on the top right of the table, click the **Delete Finding** action.
   ![DeleteFindingConfirmation](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteFindingConfirmation.png)
2. In the **Delete Finding** box, click **Delete Finding**. The selected Findings are totally removed from the system, they are deleted from the Findings table and **Total** decreases accordingly.

## Deactivating Findings

You can deactivate one or more Custom Findings from the Findings table or deactivate a single Custom Finding from its configuration drawer. A deactivated Finding stops running in the system, but keeps past alert data.

**To deactivate a Finding from its configuration drawer**

1. In the [**Findings configuration** drawer](#editing-the-custom-finding-configuration), toggle off **Activate** (default).
2. Click **Save Changes**. The Finding's **Activity Status** changes to **Inactive**.

**To deactivate one or more Findings from the Findings table**

1. In the [**Findings** table](/docs/findings-center-page#findings-table), hover over a row of a single Finding, and then at the end of the row, click the **Delete FInding** ![TrashcanIconBlackonWhite](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrashcanIconBlackonWhite.png) icon, or select the checkboxes of one or more Findings, and then on the top right of the table, click the **Delete Finding** action.
2. In the **Delete Finding** box that opens (see above), click **Deactivate Finding**. The Finding's **Activity Status** changes to **Inactive**.

## Activating a Finding

A rule runs only while it is activated. You can activate a single Custom Finding from its configuration.

**To activate a Finding**

1. In the [**Findings** table](/docs/findings-center-page#findings-table), click a Finding, and in the **Finding Configuration** drawer that opens, toggle on **Activate** (default).
2. Click **Save Changes**. The Finding's **Activity Status** changes to **Active**.