# Source: https://docs.axonius.com/docs/teams-send-dm-to-channel.md

# Microsoft Teams - Send Direct Message to a Channel

**Microsoft Teams - Send Direct Message to a Channel** sends a direct message in Microsoft Teams to the designated channel for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

* **Use stored credentials from Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure an [Microsoft Entra ID (Azure AD)](/docs/microsoft-azure-active-directory-ad) adapter connection. Each asset is run using the connection that fetched the asset.
</Callout>

* **Recipient Team ID** - The Entra user ID of the user who will receive the message.
* **Recipient Channel ID** - The ID of the channel to which the message will be sent.
* **Custom message** - The text of the Microsoft Teams direct message.

## Additional Fields

These fields are optional.

* **Create list of predefined responses** - This field is only available in an action that is added to a Workflow. Enter a list of response buttons to be shown in the Microsoft Teams message in the order that they are added into this field. Click **Add** to add each possible response to the list. When a response button is clicked in a Microsoft Teams message that is sent, the workflow continues based on that button.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** - The Application ID of the Axonius application.

  * **Azure Client Secret** - Specify a non-expired key generated from the new client secret.

  * **Azure Tenant ID** - Microsoft Entra ID (Azure AD) ID.
</Callout>

* **Message title** - Provide your own message title. If you leave this field empty, the default title of the message will be "Axonius Integration".

## API

Axonius uses the [Azure AI Bot Service](https://learn.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0) API.

## Required Permissions

The following Microsoft Graph permissions are required for the action to work:

* AppCatalog.Read.All
* TeamsAppInstallation.ReadWriteForUser.All
* TeamsAppInstallation.ReadWriteForTeam.All

## Required Ports

Axonius must be able to communicate with Microsoft Teams via TCP port 443.

## Set Up the EC Action

To set up this EC Action, you need to first configure a new designated bot in Microsoft Teams and then create a new application in Microsoft Teams.

### Configure the Bot

1. Navigate to [https://dev.botframework.com/bots/new](https://dev.botframework.com/bots/new) and create a new bot.
2. Fill the following fields:
   * **Display name** - Any name you want for this bot.
   * **Bot handle** - The Client ID of the Azure application.
   * **Messaging endpoint** - Copy the "Webhook URL" from the Axonius configuration (Global settings - Workflows Events - Microsoft Teams). This is only necessary if you are using "Create list of predefined responses" configuration in the action.
   * **App type** - The tenancy type for the Azure app.
   * **Paste your app ID below to continue** - The Client ID of the Azure application.
   * **App Tenant ID** - The Azure Tenant ID (if single tenancy mode is selected).
3. Click **Register**.

### Set Up the App with the Developer Portal

1. In Microsoft Teams, from the side panel, click **Apps**.

2. Using the search bar, search for "developer portal".

3. From Microsoft Corporation, click **Developer Portal**.

4. Click Add (or **Open**).

5. In Developer Portal, click **Apps**.

6. Click **New app**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_NewApps.png)

7. Enter a name for the app and click **Add**.

8. On the Basic information page, fill the following fields:
   * Short description
   * Long description
   * Developer or company name
   * Website
   * Privacy policy
   * Terms of use

9. Click **Save**.

10. Click **App features**.

11. Click **Bot**.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_Bot.png)

12. Select **Select an existing bot**, and choose the bot you created earlier.

13. Under "Select the scopes in which people can use this command", select **Personal**, **Team**, and **Group Chat**.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_Scopes.png)

14. Click **Save**.

15. In Developer Portal, from the top toolbar, click **Tools**.

16. Click **Bot management**.

17. Click the bot you've created.

18. Click **Channels**.

19. Make sure **Microsoft Teams** is checked.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_Channels.png)

20. Click **Save**.

### Install the New App in Teams Through the Admin Center

After you set up the app there are two potential ways for installing the app. If this process for installing the app through the Teams portal doesn't work, see the next process for installing the app using a downloaded zip file.

1. In Developer Portal, from the top toolbar, click **Apps**.
2. Select the app you created.
3. On the top-right of the screen, click **Publish**.
4. Select **Publish to your org**.
5. Click **Publish your app**
6. Navigate to [Teams App Management](https://admin.teams.microsoft.com/policies/manage-apps).
7. Search for your app and click on it.
8. Click **Publish**.
9. When prompted, confirm in the pop up.

### Install the New App in Teams Through the Developer Portal

1. In Developer Portal, from the top toolbar, click **Apps**.
2. Select the app you created.
3. On the top-right of the screen, click **Publish**.
4. Select **Download the app package** to download a zip file containing the application.
5. Navigate to [Teams App Management](https://admin.teams.microsoft.com/policies/manage-apps).
6. On the top right, click **Actions**.
7. Click **Upload new app**.
8. Click **Upload**.
9. Choose the file you downloaded.

### Get the Channel ID and Team ID

1. Go to [Teams](https://teams.microsoft.com/v2/)
2. Click **More Options** (…) in the specific channel.
3. Click **Get a link to channel**.
4. The *Channel ID* is the value after `/channel/` and before the next `/`
5. The *Team ID* is the same as *groupId*

**For example:**

1. Go to the link: `https://teams.microsoft.com/l/channel/19%3Ade6df9ad68c4438080e31ee6181ccbc4%40thread.tacv2/IDM%20Tests%20Channel?groupId=a3d878fd-48f4-47d1-aae9-5ce72b4137c2&tenantId=d5d0rrss-195d-4675-1340-c1a4871a1118`

2. The ID is `19%3Ade6df9ad68c4438080e31ee6181ccbc4%40thread.tacv2`

3. Replace: `%3A` with a colon (:)

4. Replace `%40` with @

5. The final ID is `19:Ade6df9ad68c4438080e31ee6181ccbc4@thread.tacv2`
   The Team ID is the same as the groupId:
   Team ID: `a3d878fd-48f4-47d1-aae9-5ce72b4137c2`

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).