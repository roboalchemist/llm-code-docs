# Source: https://docs.axonius.com/docs/slack.md

# Slack

Slack is a chat and collaboration hub used to connect people, information, tools, and services.

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_extensions.svg) Application Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Admin_Managed_Extensions.svg) Admin Managed Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/User_initiated_extensions.svg) User Initiated Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Add-ons.svg) Application Add-On | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | Licenses | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_settings.svg) Application Settings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Extension_Instances.svg) Application Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Admin_Managed_Extension_Instances.svg) Admin Managed Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/User_initiated_extensions_instances.svg) User Initiated Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Add-on_instances.svg) Application Add-On Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_keys.svg) Application Keys | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts_Tenants.svg) Accounts/Tenants | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_resources.svg) Application Resources

## Before You Begin

### APIs

Axonius uses the [Slack Web API](https://api.slack.com/apis).
To fetch conversations, Axonius uses the following APIs:

* [https://api.slack.com/methods/conversations.list](https://api.slack.com/methods/conversations.list)

* [https://api.slack.com/methods/conversations.members](https://api.slack.com/methods/conversations.members)

### Adapter Integration Setup

#### Step 1 - Create a User Account

1. Login to Slack as a Workspace or Org Owner.
2. Navigate to **Settings & administration > Manage members** and then click **Invite People**.
3. In the modal window, add an email, set *Invite as* to *Member* and click **Send**.
4. Copy the **email**.
5. Back in Axonius, paste the email in the **Username** field.
6. In Slack, complete the process required to activate the user. When setting the password, ensure its length is at least 32 characters long.
7. Copy the password.
8. Back in Axonius, paste the copied password in the **Password** field.
9. Return to Slack's Manage Members pane. Find the newly created user, click the ellipsis button, and then click **Change account type**.
10. Select either *Workspace Owner* or *Org Owner*, and then click **Save**.
11. Ensure that the user has access to the following URLs:

* `https://{sub_domain}.slack.com/admin/billing`
* `https://{sub_domain}.slack.com/admin/settings`
* `https://{sub_domain}slack.com/admin/auth`
* `https://{sub_domain}.slack.com/apps/manage/settings`

#### Step 2 - Set Permissions

<Callout icon="📘" theme="info">
  Note

  This adapter supports all editions of Slack, but some of the steps outlined below are only relevant for accounts with the Enterprise plan. Non-Enterprise accounts don't require permissions to fetch Teams data.
</Callout>

1. Login to Slack as a Workspace or Org Admin.
2. [Create a new Slack app](https://api.slack.com/apps). Your app will need to be able to handle a standard OAuth 2 flow.
   1. Click **Create New App**.
   2. In the new app window, click **From scratch**.
   3. Enter an App Name and select your workspace.
3. In the app's settings, select **OAuth & Permissions** from the left navigation panel. Scroll down to the section titled **Scopes** and add the **User Token Scopes** listed under [Slack Permissions](https://docs.axonius.com/axonius-help-docs/docs/slack-permissions).

#### Step 3 - Create an Authentication Token

1. In the app's settings, select **Manage Distribution** from the left navigation.
2. Under the **Share Your App with Other Workspaces** section:
   1. Expand the **Add OAuth Redirect URLs** section, and add `https://localhost` as the redirect URL.
   2. Expand the **Remove Hard Coded Information** section, and select the checkbox to confirm that any hard-coded information has been removed.
3. Click **Activate Public Distribution** or **Activate Private Distribution**.
4. In the **Share Your App with Your Workspace** section, copy the **Sharable URL** and paste it into a browser to initiate the OAuth handshake that will install the app on your organization.
   If you are running Slack Enterprise Grid Organization, you must be logged in as an Admin or Owner of your to install the app.
5. Check the dropdown in the upper right of the installation screen to make sure you are installing the app on the organization, and **not** on an individual workspace within the organization.
6. Once the application is authorized, the URL in the address bar contains a **code** parameter. Copy the value of that parameter.

<Callout icon="📘" theme="info">
  Note

  The code expires ten minutes after it's generated. For more information, see [Exchanging a temporary authorization code for an access token](https://api.slack.com/authentication/oauth-v2#exchanging).
</Callout>

7. From the **General Information** section, retrieve the Client ID and Client Secret for the application.
8. Enter the **code** value you copied in step 6 and the retrieved Client ID and Client Secret values into the following curl command:
   `curl -vLk -F code=CODE_VALUE -F client_id=CLIENT_ID_VALUE -F client_secret=CLIENT_SECRET_VALUE https://slack.com/api/oauth.v2.access`
9. Copy the resulting token.
10. Back in Axonius, paste the token in the **Authentication Token** field.

#### Step 4 - Grant Access on Specific Workspaces

<Callout icon="📘" theme="info">
  **Note**

  This process is specific for Slack Enterprise Grid Organization Solution to enable fetching conversations from Slack.
</Callout>

1. Go to the following link, where `{GRID_SUBDOMAIN}` is the actual Grid subdomain: `https://{GRID_SUBDOMAIN}.enterprise.slack.com/manage/organization/apps/profile/{{APP_ID}}`
2. From the upper-right corner, click **Manage** and select **Add to more workspaces**.
3. Check the **Default for future workspaces** option.
4. On the left, select **ALL** the workspaces.
5. Click **Next**.
6. Click **Next** again.
7. Select the **I’m ready to add this app** checkbox, and then click **Add**.
   It may take a few minutes to add the app to all the Grid workspaces.