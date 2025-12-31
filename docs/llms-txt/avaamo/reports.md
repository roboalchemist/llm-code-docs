# Source: https://docs.avaamo.com/user-guide/live-agent-console/supervisor/reports.md

# Reports

Reports enable supervisors to view the historical data of the live agents and provide insights into past interactions and performance of your Live Agent support team. These reports help you analyze trends, monitor historical performance, and make informed decisions based on past data.

{% hint style="success" %}
**Key Point**: If you require to view real-time information on the customer wait time and conversation durations of all the active and queued chat requests within the company, then see [Live Sessions](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/live-sessions) page for detailed information and insights.
{% endhint %}

### View reports for a date range

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Analytics and Reporting icon -> Reports` page in the left navigation pane of the Supervisor interface to view real-time live agent reports in your organization.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FiHXvYZ0mx7OAELKDtDM9%2Fimage.png?alt=media&#x26;token=ce8c2c18-e49d-4c0c-8120-7dcee1a7b526" alt=""><figcaption></figcaption></figure>

* By default, the report for the current day is displayed.&#x20;
  * By default, in the **Reports** page, all the queued requests are displayed first, followed by the active requests, and finally, all the ended requests are displayed:
    * Within queued requests, the requests are displayed in the descending order of wait time which implies that the request with the maximum wait time is displayed first.&#x20;
    * Within active requests, the requests are displayed in the descending order of conversation duration which implies that the request with the maximum conversation duration is displayed first.&#x20;
  * Click the date range to select different date options as per your requirements.
  * You can also view the reports for Yesterday, Today, Last 7 Days, and Last 30 Days.
  * Click **Custom range** to pick your own date range by selecting the start and end dates. You can view upto 6 months of data in the Reports page.&#x20;
* Each row is a chat request by the user and in the `Reports` page, you can view the following details about each chat conversation:
  * Conversations status: Indicates the current status of the conversation.
    * **Queued**: The conversation that is yet to be accepted by a live agent.
    * **Active**: The ongoing conversation between live agent and user.
    * **Ended**: The conversation is terminated or completed.&#x20;
  * **User name**: Indicates the end user with whom the live agent is/was interacting.
  * **Live agent name**: Indicates the name of the live agent conversing with the user.
  * **Wait time**: Indicates the time the request was in the queue before a live agent accepted the request.&#x20;
    * The wait time becomes static when a live agent accepts a chat and starts chatting with the user.&#x20;
    * When the request is transferred to another team, the wait time is reset with a new entry in the `Reports` page, and the original conversation status is marked as ended.
  * **Conversation duration**: Indicates the amount of time the current live agent is/was having a conversation with the user until the chat is terminated or transferred by the live agent to another team.
    * When the request is transferred to another team, the conversation duration is reset with a new entry in the `Reports` page and the original conversation status is marked as ended.&#x20;
    * However, in the exported CSV, you can view the total conversation duration including transfers. See [Export reports](#export-reports), for more information.
  * **Channel**: Indicates the channel used by the user to converse with a live agent.
  * **Team**: Indicates the team the request was routed to.
  * **Agent**: Indicates the agent (bot) name.
* Click the refresh option next to the date range to refresh the page and view the latest real-time status of the conversations in your organization.

### Export reports

You can export upto 6 months of data at a time based on your search criteria from the `Reports` page.

* Specify the date range required for export.
* Click the `Export` option to export data based on the criteria
* When you click `Continue`, an export job is created.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FsgbMrUeVjHnz3iGMo6oB%2Fimage.png?alt=media&#x26;token=890bf48d-cc72-4e74-b263-b03cbf3bf053" alt=""><figcaption></figcaption></figure>

Click the `View export jobs` option to view the last 10 export jobs.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FiW9LmIeFv4Swu7uBUPH8%2Fimage.png?alt=media&#x26;token=0cb15387-f596-4193-8f54-b68b7b2c6b0d" alt=""><figcaption></figcaption></figure>

You can view the following details in the `View Export Jobs` pop-up:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fi7CF6Vqfc04uxGiVeBuM%2Fimage.png?alt=media&#x26;token=18c6e97c-eade-4b14-af38-db4162bdb405" alt=""><figcaption></figcaption></figure>

* **Request time**: Time of data export request.
* **Export data**: The search criteria used to export data.&#x20;
* **Status**: Indicates the status of the export job. The status can have the following values:
  * **Complete**: The export job is completed without any errors. Click the `Download` link to download the exported data based on the search criteria.&#x20;
  * **Failed**: The export job has failed with errors. Contact Avaamo Support for further assistance.
  * **In-Progress**: The export job is still in progress. An email notification is sent to you upon completion. You can still delete a job that is in progress, however, you can download the export file only after the job is completed.
* **Actions**: You can download the exported data or delete the jobs that are no longer required. You can use this for further analysis and reporting. See [Columns in the downloaded CSV report](#columns-in-the-downloaded-csv-report), for more information on the different columns available in the downloaded CSV file.
* Click `Refresh` to view the latest status of `In-Progress` export jobs.

### Columns in the downloaded CSV report

In the downloaded CSV report a supervisor can view the following details:

* **Conversation UUID**: When a live agent chats with a user, a unique conversation identifier is created by the Platform that helps to identify the conversation between the live agent and the user. This can be used to view the conversation in the [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents#using-conversation-history) page. This can also be used in the [Conversation REST API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/conversation-message-api), if required.
* **Total Time**: Total conversation duration between the live agent and the users including the transfers to teams (if any) during the conversation.&#x20;
* **Requested At (UTC)**: UTC time of the live agent chat request by the user.
* **Accepted At (UTC)**: UTC time of when the chat request was accepted by the live agent.
* **Ended At (UTC)**: UTC time of when the chat request was ended.
* **Conversation Status**: The conversation status at the time of download.
* **User Name**: The user who requested to chat with the live agent.
* **Live agent name**: The current live agent in conversation with the user or with whom the chat was ended.
* **User email**: The email of the user, if available. Certain user details such as first name, last name, email, or other custom user properties can be set or collected from the user. See [View user information](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/view-user-information), for more information on how to set user details and how the user details can be useful for live agents.
* **Wait Time**: The time the request was in the queue before a live agent accepted the request. The wait time becomes static when a live agent accepts a chat and starts chatting with the user.&#x20;
* **Conversation Duration**: The amount of time the current live agent is/was having a conversation with the user until the chat is terminated or transferred by the live agent to another team.
* **Channel Name**: The channel used by the user to converse with a live agent.
* **Channel Type**: The type of channel used by the user to converse with a live agent.
* **Team**: The team the request was routed to.
* **Routing Rule**: Name of the routing rule applied, if any.&#x20;
* **Agent Name**: The agent (bot) name.
* **Agent ID**: The agent identifier.
