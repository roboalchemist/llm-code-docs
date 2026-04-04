Source: https://docs.slack.dev/reference/scopes/admin.chat.write

# admin.chat:write scope

Delete, restore, and update messages in conversations

## Facts

## Supported token types

[`User`](/authentication/tokens#user)

## Compatible API methods

[`oversight.chat.delete`](/reference/methods/oversight.chat.delete)

[`oversight.chat.restore`](/reference/methods/oversight.chat.restore)

[`oversight.chat.update`](/reference/methods/oversight.chat.update)

## Usage info {#usage-info}

This scope is exclusively usable with `admin.*` Web API methods and will not enable access to non-admin API equivalents of the same functionality.

This `admin` scope is obtained through [version two of the OAuth V2 flow](/authentication/installing-with-oauth), but there are a few additional requirements. The app requesting this scope **must** be [installed](/app-management/quickstart-app-settings#installing) by an _**Admin or Owner**_ of an Enterprise organization. Also, the app must be installed on the **entire** org, not on an individual workspace. See below for more details. '

If the app is installed by an Org Admin or Owner, ensure the Channel Management settings provide the appropriate permissions. In order to manage channels after they are created, you must update your token to enable permissions for Org Admins or Owners (not just the Primary Org Owner).

Admin API endpoints reach across **an entire Enterprise organization**, not individual workspaces.

For a token to be imbued with admin scopes, it must be obtained from installing an app on the **entire Enterprise org**, not just a workspace within the organization.

To configure and install an app supporting Admin API endpoints on your Enterprise organization:

1. [Create a new Slack app](https://api.slack.com/apps) . Your app will need to be able to handle a standard [OAuth 2 flow](/legacy/legacy-authentication/#flow).
2. In the app's settings, select **OAuth & Permissions** from the left navigation. Scroll down to the section titled **Scopes** and add the `admin.*` scope you want. Click the green **Save Changes** button.
3. In the app's settings, select **Manage Distribution** from the left navigation. Under the section titled **Share Your App with Other Workspaces**, make sure all four sections have the green check. Then click the green **Activate Public Distribution** button.
4. Under the **Share Your App with Your Workspace** section, copy the **Sharable URL** and paste it into a browser to initiate the OAuth handshake that will install the app on your organization. You must be logged in as an **Admin or Owner** of your Enterprise organization to install the app.
5. Check the dropdown in the upper right of the installation screen to make sure you are installing the app on the organization, not an individual workspace within the organization. See the image below for a visual.
6. Once your app completes the OAuth flow, you will be granted an OAuth token that can be used for calling Admin API methods for your organization.

![](/assets/images/workspace-v-org-audit-10f163aac79dc5f2c15e3ebe8267dbf4.png)

## When installing an app to use an Admin API endpoint, be sure to install it on your Enterprise organization, not a workspace within the organization.
