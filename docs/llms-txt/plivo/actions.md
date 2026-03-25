# Source: https://plivo.com/docs/aiagent/aistudio/nodereference/actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# App Actions

> Take actions on External Apps from the Agent flow

**App Action Nodes** allow your AI agent to interact with external applications during the flow to perform specific actions, such as creating rows in Google Sheets, updating Salesforce records, or managing customer data in HubSpot.

1. **Select an App Action Node**

   * In the node selection panel, you will find a tab called **External Apps**. Click on it to see the list of available external applications integrated with Plivo.
   * Choose the app you want to interact with, such as **Google Sheets**, **Salesforce**, **Zendesk**, **HubSpot**, and others.

   **Example**: If you choose **Google Sheets**, you'll see options for actions like **Create Sheet**, **Append Rows**, **Batch Update**, etc.

<Frame>
  <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/App-Action2.mp4?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=d4ecbdda734f93f333e2999f500c8b86" data-path="aiagent/images/App-Action2.mp4" />
</Frame>

1. **Choose an Action for the Selected App**

   * After selecting the app, a list of available actions will be presented. These are predefined tasks that the app can perform (e.g., creating a new sheet, appending rows, etc.).

   **Example**: If you select **Google Sheets**, available actions will include:

   * **Create Sheet**: Create a new Google Sheet.
   * **Append Rows**: Add rows of data to an existing sheet.
   * **Batch Update**: Update multiple rows at once.
2. **Configure the Action**

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/appaction2.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=1c7724f92417322a45c5375fbd1e0434" width="405" height="315" data-path="aiagent/images/appaction2.png" />
</Frame>

* Once you select an action, a configuration screen for that specific action will open. Here, you'll provide details such as:
  * **Connection**: Select or authenticate your connection to the external app (e.g., your Google Sheets account).
  * **Parameters**: Fill in the necessary parameters for the action, such as the specific **spreadsheet** and **row values** (for actions like appending rows).
* If the app isn’t yet authenticated, you’ll be prompted to set it up through the **Integrations** page.

3. **Use Variables**
   * You can pass dynamic **agent variables** from earlier in the conversation into these actions. For instance, you might collect user input and append it to a Google Sheet as part of your workflow.

### Troubleshooting

* **App Not Integrated**: If an external app isn't integrated yet, you’ll be prompted to authenticate it during the configuration of the App Action Node. Make sure the correct permissions are granted.
* **Incorrect Data**: If the app action isn't behaving as expected (e.g., incorrect data in Google Sheets), double-check that the correct variables are being passed, and verify the app's connection and authentication.
