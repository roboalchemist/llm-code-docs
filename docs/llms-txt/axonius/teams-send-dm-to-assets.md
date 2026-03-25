# Source: https://docs.axonius.com/docs/teams-send-dm-to-assets.md

# Microsoft Teams - Send Direct Message to Assets

**Microsoft Teams - Send Direct Message to Assets** sends a direct message in Microsoft Teams to:

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
* **Use stored credentials from Microsoft Entra ID (formerly Azure Active Directory) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure an [Microsoft Entra ID (Azure AD)](/docs/microsoft-azure-active-directory-ad) adapter connection. Each asset is run using the the connection that fetched the asset.
</Callout>

* **Custom message** - The text of the Microsoft Teams direct message.

## Additional Fields

These fields are optional.

* **Create list of predefined responses** - This field is only available in an action that is added to a Workflow. Enter a list of response buttons to be shown in the Microsoft Teams message in the order that they are added into this field. Click **Add** to add each possible response to the list. When a response button is clicked in a Microsoft Teams message that is sent, the workflow continues based on that button.

<Callout icon="💡" theme="warn">
  ### Connection Parameters

  If **Use adapter connection**  is not enabled, these fields need to be configured. To access the values for these fields, see the Microsoft Entra ID (Azure AD) adapter configuration page.

  * **Azure Client ID** - The Application ID of the Axonius application.

  * **Azure Client Secret** - Specify a non-expired key generated from the new client secret.

  * **Azure Tenant ID** - Microsoft Entra ID (Azure AD) ID.

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  * **Account Sub Domain** - The Microsoft account's sub domain (.onmicrosoft.com).

  * **Username** and **Password** - The credentials for a user account that has the permissions needed to fetch SaaS data.

  * **2FA Secret Key** - The secret generated in Microsoft Entra ID (Azure AD) for setting up 2-factor authentication for the Microsoft user.

  * **SSO Provider** - If your organization uses Microsoft Entra ID (Azure AD) for SSO, you can select this check box.
    For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).
</Callout>

* **Send asset details in message** - Select this option to include asset details in the direct message sent by Teams.

<Callout icon="📘" theme="info">
  Notes

  These options can all be selected together. The message is sent to the indicated user if supported by the query results.

  * **Send to manager** - Select this option to also send the direct message to the relevant manager for that asset.

  * **Send to the last user that used the asset** - Select this option to send the direct message to the last user that used the asset. This option is usually related to device assets.

  * **Send to the device owner** - Select this option to send the direct message to the asset owner.  This option is usually related to device assets.
</Callout>

<EC_Set_Scheduling />

## API

Axonius uses the [Azure AI Bot Service](https://learn.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0) API.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* AppCatalog.Read.All
* TeamsAppInstallation.ReadWriteForUser.All

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
   ![Teams\_NewApps](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_NewApps.png)

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
    ![Teams\_Bot](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_Bot.png)

12. Select **Select an existing bot**, and choose the bot you created earlier.

13. Under "Select the scopes in which people can use this command", select **Personal**, **Team**, and **Group Chat**.
    ![Teams\_Scopes](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_Scopes.png)

14. Click **Save**.

15. In Developer Portal, from the top toolbar, click **Tools**.

16. Click **Bot management**.

17. Click the bot you've created.

18. Click **Channels**.

19. Make sure **Microsoft Teams** is checked.
    ![Teams\_Channels](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teams_Channels.png)

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

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).