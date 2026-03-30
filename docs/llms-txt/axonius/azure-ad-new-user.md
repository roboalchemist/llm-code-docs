# Source: https://docs.axonius.com/docs/azure-ad-new-user.md

# Microsoft Entra ID (formerly Azure AD) New User

Axonius supports **Microsoft Entra ID (formerly Azure AD) New User** as an event in a Workflow.
Users can create users in Microsoft Entra ID using the following Enforcement Action:

* [Microsoft Entra ID (formerly Azure AD) - Create Users](/docs/azure-ad-create-users) - Creates Entra ID user accounts for assets returned by the selected query or assets selected on the relevant asset page.

Whenever a user account is added to Microsoft Entra ID (Azure Active Directory), Microsoft Entra ID triggers an event. All Workflows configured with this event are then triggered.

## Configuring Microsoft Entra ID to Send Events to Axonius

Before including the **Microsoft Entra ID New User** event in a Workflow the first time, you need to do the following:

* In the [Microsoft Entra ID adapter - Advanced Configuration](/docs/microsoft-azure-active-directory-ad#microsoft-entra-id-advanced-settings), enable the **Enable real-time asset updates (Supported events: New users, New groups, Group members changes)** advanced option.
* Enable events in the Microsoft Entra ID adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.

![MicrosoftSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MicrosoftSettings.png)

## Adding the Microsoft Entra ID New User Event to the Workflow

Add **Microsoft Entra ID New User** as the triggering event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Microsoft Entra ID New User event as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Microsoft Entra ID New User** tile. The **Microsoft Entra ID New User** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventTriggerMicrosoftEntraIDNewUser.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventTriggerMicrosoftEntraIDNewUser.png)

The Workflow is triggered each time a user is added as a Microsoft Entra ID new hire. The next node runs on the retrieved user.

**To select Microsoft Entra ID New User as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Microsoft Entra ID New User** tile. The **Microsoft Entra ID New User** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventMicrosoftEntraIDNewUser.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventMicrosoftEntraIDNewUser.png)

In this case, when a user asset retrieved from the previous node is added to Microsoft Entra ID as a new user, an event occurs and the Workflow continues running.