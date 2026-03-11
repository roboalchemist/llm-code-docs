# Source: https://docs.axonius.com/docs/azure-ad-user-removed-from-group.md

# Microsoft Entra ID (formerly Azure AD) User removed from group

Axonius supports **Microsoft Entra ID (formerly Azure AD) User removed from group** as an event in a Workflow.

Users can remove users from Microsoft Entra ID groups using the following Enforcement Action:

* [Microsoft Entra ID (formerly Azure AD) - Add or Remove Assets in Group](/docs/add-users-or-devices-to-azure-ad-group) with **Group Member Operation`=`Remove assets from group** - Removes from a Microsoft Entra ID group all selected users or users returned from the query.

Whenever a user is removed from the Microsoft Entra ID (Azure Active Directory)  group, Microsoft Entra ID triggers an event. All Workflows configured with this event are then triggered.

## Configuring Microsoft Entra ID to Send Events to Axonius

Before including the **Microsoft Entra ID User removed from group** event in a Workflow the first time, you need to do the following:

* In the [Microsoft Entra ID adapter - Advanced Configuration](/docs/microsoft-azure-active-directory-ad#microsoft-entra-id-advanced-settings), enable the **Enable real-time asset updates (Supported events: New users, New groups, Group members changes)** advanced option.
* Enable events in the Microsoft Entra ID adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.

![MicrosoftSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MicrosoftSettings.png)

## Adding the Microsoft Entra ID User removed from group Event to the Workflow

Add **Microsoft Entra ID User removed from group** as the triggering event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Microsoft Entra ID User removed from group event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Group Created or Updated**, click the **Microsoft Entra ID User removed from group** tile. The **Microsoft Entra ID User removed from group** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventTriggerMicrosoftEntraIDUserRemovedFromGroup.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventTriggerMicrosoftEntraIDUserRemovedFromGroup.png)

The Workflow is triggered each time a user is removed from a Microsoft Entra ID group. The next node runs on the retrieved user.

**To select Microsoft Entra ID User removed from group as a non-triggering event**

1. In the **Event** pane, under **Group Created or Updated**, click the **Microsoft Entra ID User removed from group** tile. The **Microsoft Entra ID User removed from group** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventMicrosoftEntraIDUserRemovedFromGroup.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventMicrosoftEntraIDUserRemovedFromGroup.png)

In this case, when the user retrieved from the previous node is removed from a Microsoft Entra ID group, an event occurs and the Workflow continues running.