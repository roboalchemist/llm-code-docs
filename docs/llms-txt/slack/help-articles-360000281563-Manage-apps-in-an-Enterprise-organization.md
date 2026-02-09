# Manage apps in an Enterprise organization

Org Owners, Org Admins, and Integrations Admins can view and manage apps for their Enterprise organization from the **Integrations** section of the admin dashboard.

## How it works

- View and install [certain apps](https://slack.com/marketplace/category/At01EB3C3VKK) at the org level, then add them to workspaces.
- Approve apps for Workspace Owners to install when they’d like.
- Restrict apps so that they cannot be installed to workspaces on your org.

**Note:** Apps using the [admin](https://api.slack.com/admins), [Discovery](https://slack.com/help/articles/360002079527-A-guide-to-Slacks-Discovery-APIs), or [SCIM](https://api.slack.com/scim) APIs can access the data they need in an org once they’re installed at the org level. They don’t need to be explicitly added to any workspaces.

## View apps in your org

Use the **Integrations** section of the admin dashboard to see apps across workspaces in your org. Select **Installed apps** to see org-level and workspace-level app installations, along with the following information:

| **Installed on** | If an app is installed to one workspace, you’ll see the workspace name. If an app is installed to more than one workspace, you’ll see the total number of workspaces. Click on an app’s name to see a full list of workspaces it’s installed to, when it was installed, and who installed it. |
| --- | --- |
| **Source** | The source tells you where an app originated. Apps can be from the **[Slack Marketplace](https://slack.com/marketplace)**, **Internal** if built by someone in your organization, or **Distributed** if a developer hasn't submitted it to the Slack Marketplace for review. |
| **Access level** | An app’s access level tells you how it’s been installed. Apps are installed at either the **Organization** or **Workspace** level. |
| **App resolution** | This tells you if an app is available to your org. **Approved** apps can be installed to any workspace, and **Restricted** apps can’t be. Apps with a **Set by workspace** policy can be approved or restricted by individual Workspace Owners. |

**Tip:** To export a list of apps installed across your org from the admin dashboard, click **Export CSV** in the top-left corner of the **Installed Apps** section.

## Install an app at the org level

### Step 1: Choose and install an app

1. From your desktop, click your organization name in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **_Integrations_**.
4. Click **Manage Apps** in the top right, then select **Install an app**.
5. Search for and select the app you’d like to install.
6. Click **Continue**. Depending on the app you’re installing, you may be prompted to complete additional steps before proceeding.
7. Click **Allow** to grant the app access to your org.

Slackbot will send a [direct message (DM)](https://slack.com/help/articles/212281468-Understand-direct-messages) to all Org Owners and Org Admins letting them know that the app has been installed. Once you’ve granted the app access to your org, you can return to the admin dashboard to add the app to workspaces.

**Note:** If you install an app at the org level that has already been added to workspaces, members of those workspaces can continue using it without interruption.

### Step 2: Add an app to workspaces

1. From the **_Integrations_** section of the admin dashboard, click the **Installed Apps** tab.
2. Find the app you’d like to add to workspaces.
3. Click the **_three dots icon_** to the right of the app.
4. Select **Add to more workspaces**.
5. Check the box next to any workspaces you’d like to add the app to. To automatically add the app to any new workspaces created in your org, check the box next to **Default for future workspaces**.
6. Click **Next**.
7. Check the box next to **I’m ready to add this app**.
8. Click **Add App**.

Slackbot will send a DM to all Org Owners and Org Admins when the app has been added to the workspaces you selected. Once an app has been added to workspaces, members can connect their accounts to use it.

## Approve or restrict an app at the org level

### Approve an app for your org

1. From your desktop, click your organization name in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **_Integrations_**.
4. Click **Manage Apps** in the top right, then select **Approve an app**.
5. Search for and select the app you’d like to approve.
6. Review the app’s scopes, then click **Approve**.

**Tip:** To undo this action, click **Resolutions** in the admin dashboard then view the **Approved Apps** tab. Click the **_three dots icon_** to the right of the app and select **Unapprove app**.

### Restrict an app for your org

Restricting an app will not remove any existing installations of the app from workspaces in your org. A Workspace Owner or [app manager](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#appoint-app-managers) will need to [remove the app](https://slack.com/help/articles/360003125231-Remove-apps-and-custom-integrations-from-your-workspace#remove-an-app) from their workspace.

1. From your desktop, click your organization name in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **_Integrations_**.
4. Click **Manage Apps** in the top right, then select **Restrict an app**.
5. Search for and select the app you’d like to restrict.
6. Click **Restrict**.

**Tip:** To undo this action, click **Resolutions** in the admin dashboard then view the **Restricted Apps** tab. Click the **_three dots icon_** to the right of the app and select **Unrestrict app**.

## Manage app requests at the org level

If an app’s developer changes the scopes of an app after it was approved or restricted for your org, members may need to request the app again so you can review the new scopes. App requests will be sent to Org Owners and Org Admins in a DM from Slackbot. To review requests, follow the steps below:

1. When you receive a request, open your direct message with Slackbot.
2. Review the request. Select **Approve for Organization** or **Restrict for Organization**. Choosing **Restrict for Organization** will prevent all members from installing the app.

![An app review request in a message from Slackbot.](https://slack.zendesk.com/hc/article_attachments/32814972431251)

When a request is approved or denied, Slack will update the original request message so all admins can see the status. If you decide to restrict an app’s new scopes, members can continue using the existing version of the app, but cannot install or use the updated version.

**Tip:** Org Owners and Org Admins can view and manage app upgrade requests from the **Requests** tab in the **Integrations** section of the admin dashboard, where you can also configure [automations for app requests](https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval).

## Remove or uninstall an app

There are two options for removing apps installed at the org level:

- Remove the app from workspaces that no longer need to use it.
- Uninstall the app from your org to remove it from all workspaces.

**Note:** Apps that are not installed at the org level cannot be removed from workspaces or uninstalled from the admin dashboard. A Workspace Owner or app manager will need to [remove the app](https://slack.com/help/articles/360003125231-Remove-apps-and-custom-integrations-from-your-workspace#remove-an-app).

### Remove an app from a workspace

1. From your desktop, click your organization name in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **_Integrations_**, then select **Installed Apps**.
4. Click the **_three dots icon_** to the right of the app you’d like to remove.
5. Select **Remove from a workspace**.
6. Check the boxes next to any workspaces you’d like to remove the app from.
7. Click **Next**.
8. Check the box next to **I’m ready to remove this app**, then click **Remove App**.

Slackbot will send a DM to all Org Owners and Org Admins when the app has been removed from the workspaces you selected.

### Uninstall an app from your org

1. From your desktop, click your organization name in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **_Integrations_**, then select **Installed Apps**.
4. Click the **_three dots icon_** to the right of the app you’d like to uninstall.
5. Select **Uninstall from your org**.
6. Check the box next to **I want to uninstall this app from my org**, then click **Uninstall**.

Slackbot will send a DM to all Org Owners and Org Admins when the app has been uninstalled from your org.

**Who can use this feature?**

- **Org Owners**, **Org Admins**, and members with the **Integrations Admin** [system role](https://slack.com/help/articles/360018112273-Types-of-roles-in-Slack#system-roles)
- Available on **Enterprise** plans