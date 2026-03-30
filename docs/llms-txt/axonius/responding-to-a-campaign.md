# Source: https://docs.axonius.com/docs/responding-to-a-campaign.md

# Responding to a Campaign

<Callout icon="📘" theme="info">
  Note

  This section is an explanation to Approvers (managers) on how to respond to a Campaign.
</Callout>

After a Campaign begins running, the system begins sending messages to all Approvers resulting from the query in the **Users and Applications** step using the **Message Method** selected (Slack or Teams) in the **Message and Response** step 2 of the Campaigns Wizard. The message to the Approver includes the **Message Content** configured in that step, as well as a link labeled *Click here to approve or revoke each individually*. Clicking the link opens the External Approval Form (one form per Campaign per Approver). The Approval form is also available to non-Axonius users.

## The External Approval Form

The Approval form allows individual approval/denial per-user per-application. The following is an example of the Approval form that opens when the Approver clicks the link in the message sent by the Campaign.

<Image alt="ApproveOrRevokeForm" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ApproveOrRevokeForm.png" />

The Approval form includes the following information:

* The name of the Approver and the message to the Approver that was configured in the **Message Content** field in the Campaign wizard - Step 2 (**Message and Response**).

* **Total Users** - The total number of users in the Campaign.

* **End Date** - The end date of the Campaign, if **Set Campaign End Date** has been toggled on and a date selected in the Campaign wizard - Step 3 (**Settings**).

* **Created By** - The Axonius user who created the Campaign.

* A table with one row per user - per application that the Approver is responsible to approve or revoke. The **Total** number of user-application approvals required of this Approver is displayed above the table.
  * **User** - The name of the user (under the Approver's management) whose right to access an application is being reviewed.
  * **Application** – The application that the Approver need to decide whether to approve or revoke user access to it.
  * **Action** - the **Approve** and **Revoke** buttons to be used by the Approver.

**To respond to a Campaign**

1. Under the **Action** column:
   * Click **Approve** to continue the user's access to the application, or **Revoke** to discontinue access.
   * Click **Approve All** above the table to approve access to all the applications to all users in the table.
   * Click **Revoke All** above the table to revoke access to all the applications to all users in the table.
   * Click **Clear All** to clear all your approved/revoked responses.
2. Click **Submit** to transmit your responses to Axonius.

<Callout icon="📘" theme="info">
  Note

  You can submit a partially answered form, and then submit again when you are ready with more responses.
</Callout>