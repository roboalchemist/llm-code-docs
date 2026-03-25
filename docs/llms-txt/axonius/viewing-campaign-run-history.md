# Source: https://docs.axonius.com/docs/viewing-campaign-run-history.md

# Viewing Campaign Run History

From the **Campaign** drawer of a selected Campaign that is In *Progress*, *Scheduled*, *Terminated*, or *Completed*, select the **Campaign Run History** tab to view a summary the results of running the Campaign for each user per application.

<Callout icon="📘" theme="info">
  Note

  For a Scheduled campaign, the **Campaign Run History** tab becomes enabled only after the Campaign begins running.
</Callout>

<Image alt="CampaignRunHistoryTab" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-QIHLFEZ2.png" />

The **Campaign Run History** page consists of the following main elements:

* General Campaign Information - Same as in [Campaign Details](/docs/viewing-campaign-information) tab.
* [Run History table](#campaign-run-history-table) with **Total** runs displayed above it.

### Campaign Run History Table

The Campaign Run History table displays a list of Campaign runs, with one row representing each run (per user per application). The table includes the following fields, by default, for each Campaign:

* **User** - The name of the user whose access to an application is being reviewed by the Approver.
* **Application** – The application that the Approver must approve or revoke continued access for the user.
* **Approver** - The email address of the manager or user who was assigned to approve or revoke the user's continued access to the application. Can be an Axonius or non-Axonius user.
* **Response Status** – The response of the Approver to the sent message regarding the user's access to the Application. The possible statuses are:
  * **Pending Response** - The Approver did not yet respond.
  * **Message Delivery Failed**- The message was not delivered to the Approver due to missing or incorrect manager details.
  * **Approved** - Approver granted the user continued access to the Application.
  * **Revoked** - Approver revoked from the user continued access to the Application.
  * **Terminated** - The Campaign was manually terminated (using the **Terminate** action).
* **Action Time** – The date and time that the Approver responded.
* **Result** - The result of the run.
  * An **Approve** or **Revoke** (configured with **Update in Axonius**) response uses a Custom Data action to indicate this response on the dedicated Axonius Custom Field **Campaigns Approval**, and always succeeds, and hence the Result in this case is always **Success**.
  * A **Revoke** response configured with **Revoke** includes running an Enforcement Action to revoke the application from the user. When this Enforcement Action succeeds to remove the application from the user, the Result of the run is **Success**; otherwise it is **Failure**. For other response statuses (*Pending Response*, *Terminated*, or *Message Delivery Failed*), there is no value under **Result** (the run result is irrelevant).

## Export Campaign Run History to CSV

To export the Campaign Run History to a CSV file, select **Export CSV**. The CSV file contains the above details as well as the Campaign's Due Date, which is the expected End Date of the Campaign, as defined when the Campaign was created.

<Image alt="ExportCSVButton" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-WH1TR7Y7.png" />