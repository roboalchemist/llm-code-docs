# Source: https://docs.axonius.com/docs/teams-send-dm-to-user.md

# Microsoft Teams - Send Direct Message to a User

**Microsoft Teams - Send Direct Message to a User** sends a direct message in Microsoft Teams to user assets returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

This Enforcement Action requires initial setup in Microsoft Teams before you can configure and run it. See [Set Up the EC Action](/docs/teams-send-dm-to-user#set-up-the-ec-action) for the required setup steps.

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

* **Recipient Entra User ID** - The Entra user ID of the user who will receive the message.
* **Custom message** - The text of the Microsoft Teams direct message.

## Additional Fields

These fields are optional.

* **Create list of predefined responses** - This field is only available in an action that is added to a Workflow. Enter a list of response buttons to be shown in the Microsoft Teams message in the order that they are added into this field. Click **Add** to add each possible response to the list. When a response button is clicked in a Microsoft Teams message that is sent, the workflow continues based on that button.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** - The Application ID of the Axonius application.

  * **Azure Client Secret** - Specify a non-expired key generated from the new client secret.

  * **Azure Tenant ID** - Microsoft Entra ID (Azure AD) ID.
</Callout>

## API

Axonius uses the [Azure AI Bot Service](https://learn.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0) API.

## Required Permissions

The following Graph API Application permissions are required for the action to work:

* AppCatalog.Read.All
* TeamsAppInstallation.ReadWriteForUser.All

## Required Ports

Axonius must be able to communicate with Microsoft Teams via TCP port 443.

## Set Up the EC Action

To set up this EC Action, follow these steps:

### Set Up the App with the Developer Portal

1. In Microsoft Teams, from the side panel, click **Apps**.

2. Using the search bar, search for "developer portal".

3. From Microsoft Corporation, click **Developer Portal**.

4. Click Add (or **Open**).

5. In the Developer Portal, click **Apps**.

6. Click **New app**.
   ![Teams\_NewApps](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_NewApps.png)

7. Enter a name for the app and click **Add**.

8. On the Basic information page, fill the following fields:
   * Short description
   * Long description
   * Developer or company name
   * Website
   * Privacy policy
   * Terms of use
   * Application (client) ID *(Optional)* - You can link this Teams App to an existing App Registration, which will be used to grant Graph API permissions. This step is optional.  See more information under [Check and Configure the App Registration](/docs/teams-send-dm-to-user#check-and-configure-the-app-registration).

<Callout icon="📘" theme="info">
  Note

  Due to updates to this integration by Microsoft, there is no guarantee that the App Registration link will function as expected.
</Callout>

9. Click **Save**.

10. Click **App features**.

11. Click **Bot**.
    ![Teams\_Bot](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_Bot.png)

12. Select **Select an existing bot** or create a new one. To create a new bot:
    1. Click **Create a new bot**.
    2. Enter a bot name and click **Create Bot**.

13. Under "Select the scopes in which people can use this command", select **Personal**, **Team**, and **Group Chat**.
    ![Teams\_Scopes](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_Scopes.png)

14. Click **Save**.

15. In the Developer Portal, from the top toolbar, select **Tools**.

16. Click **Bot management**.

17. Click the bot you've created.

18. Click **Channels**.

19. Make sure **Microsoft Teams** is checked.
    ![Teams\_Channels](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_Channels.png)

20. (Optional) If you want to use Axonius Workflows:
    1. In Axonius, go to **Global setting**s `>` **Workflows Events** `>` **Microsoft Teams**.
    2. Copy the **Webhook URL**.

![copy webhook](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/copy%20webhook.png)

4. In the Developer Portal, go to the **Configure** tab.
5. Paste the Webhook URL under **Endpoint Address**.

![paste webhook](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/paste%20webhook.png)

21. Click **Save**.

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

### Check and Configure the App Registration

1. Navigate to **App Registration** `>` **All Applications**.
2. Search for the name you used when you registered your Teams App.
   * If a new application appears, it means that Microsoft has created a new App Registration - even if you provided an Application (Client) ID when creating the Teams App. In this case, you must use this newly created application to configure the Graph API permissions.
   * If no new application appears, and you provided an Application (Client) ID - you can continue to use the existing App Registration.
3. Add the following Graph API Application Permissions:
   * AppCatalog.Read.All

   * TeamsAppInstallation.ReadWriteForUser.All

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).