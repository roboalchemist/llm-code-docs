# Source: https://docs.axonius.com/docs/viewing-campaign-information.md

# Viewing Campaign Details

From the Campaigns page, select any *In Progress*, *Scheduled*, or *Completed* Campaign  to open its Campaign drawer and view the **Campaign Details**.

* From an *In Progress*  Campaign drawer header, you can terminate the Campaign, if required.
* From a *Scheduled*  Campaign drawer header, you can delete the Campaign, if required.

**To view Campaign information**
Select a campaign from the table on the [Access Reviews page](/docs/campaigns-page). The **Campaign Details** tab opens, showing the details of the campaign. The Campaign name is displayed in the header of the Campaign drawer.

<Image alt="CampaignDetails" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CampaignDetails.png" />

The following are the details of the Campaign:

* **Status** - The Campaign status. Available statuses: In Progress, Draft, Scheduled, Terminated, Completed.
* **Start Time** - The date and time that the Campaign started or the date that it is scheduled to start.
* **End Time** - This field is visible for a *Scheduled* or *In Progress* Campaign that is configured with an **End Date**, and shows the date that the Campaign has been configured to end. For a *Terminated* or *Completed* Campaign, is shows the date and time that the Campaign ended.
* **Created By** - The user who created the Campaign.
* **Users Query** - The query used to determine the Campaign target audience, applications, permissions, roles, and approvers.
* **Total Users** - The number of users (returned by the query) whose access to the Applications is being reviewed.
* **Applications** - The name and icons of the applications (returned by the query) being reviewed.
* **Total Approvers** - The number of approvers (returned by the query) who are reviewing the users' access to applications.
* **Message Method** - The method used to send the [message to the approvers about the campaign](/docs/responding-to-a-campaign). For example: Slack, Teams.
* **Message Content** - The text of the message sent to Approvers.
* **Forced End Date** - Visible if the Campaign is configured with an End Date.
* **Reminder** - Visible if the Campaign is configured with a reminder.
* **Response Actions** - The action that is to be taken in Axonius when the Approver approves or revokes user access to an application.
  * The **Approve** action is always configured to **Update in Axonius**, meaning, when the Approver approves user access to the application, an Enforcement Action marks the user's Axonius custom field as Approved for that application.
  * The **Revoke** action can be configured to either of the following:
    * **Update in Axonius**, i.e., when the Approver revokes access of the application for the user, an Enforcement Action marks the user's Axonius custom field as Revoked for that application.
    * **Revoke Access**, which in addition to marking the Axonius custom field as Revoked, also runs an Enforcement Action to actually revoke access to the application from the user.

<Callout icon="📘" theme="info">
  Note

  Not all the above fields are displayed in all Campaigns. The fields displayed in Campaign Details are according to the status of the Campaign and its configuration.
</Callout>