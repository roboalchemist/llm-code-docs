# Set organization-level policies for apps

By default, members of an Enterprise organization can [install any app](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace) to workspaces they belong to. Org Owners can set policies that apply to all workspaces in their organization to manage app installation and use.

## What to expect

* Setting an app management policy turns on [app approval](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#manage-app-approval) for every workspace in an org. When app approval is enabled, members can only use apps that have been approved for their workspaces.
* Org Owners can [approve or restrict apps](https://slack.com/help/articles/360000281563-Manage-apps-in-an-Enterprise-organization) for their entire org, but Workspace Owners and [app managers](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#appoint-app-managers) will be responsible for reviewing app requests for workspaces they manage.
* Org Owners can also set org policies to limit members to installing apps from the Slack Marketplace and determine whether Multi-Channel Guests can use [shortcuts](https://slack.com/help/articles/360057554553-Use-shortcuts-to-take-actions-in-Slack).

## Set an app management policy for your org

Follow the steps below to turn on app approval for all workspaces in your org:

1. From your desktop, click your **organization name** in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **_Settings_**, then select **Organization Policies**.
4. Click the **Apps** tab at the top of the page.
5. Next to **App Management**, click **Add Policy**.
6. Check the box next to **Require App Approval**.
7. Select **Save Policy**. Then, click **Create Policy**.

**Note:** If you don’t set an app management policy for your org, Workspace Owners can still choose to enable app approval for workspaces they manage.

### Manage Sign in with Slack permissions

Some third-party apps offer the option to sign in to their service with Slack account credentials. By default, Workspace Owners can choose whether members can [sign in to other services with their Slack account](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#sign-in-with-slack). If an app management policy has been set, Org Owners can remove Workspace Owners' ability to manage [Sign in with Slack permissions](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#sign-in-with-slack) and decide if apps with the [Sign in with Slack identity scope](https://api.slack.com/docs/sign-in-with-slack) require approval:

1. From your desktop, click your **organization name** in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **_Settings_**, then select **Organization Policies**.
4. Click the **Apps** tab at the top of the page.
5. Next to App Management, click **Add Policy**. If there’s already an app management policy in place, click the **_pencil icon_** to choose your **Sign in with Slack** permissions.
6. Under **People who can manage Sign in with Slack restrictions**, select **Org Owners** from the drop-down menu.
7. Check or uncheck the box next to **Don’t require pre-approval for Sign in with Slack Apps**.
8. Select **Save Policy**. Then, click **Create Policy**.

## Set other app installation policies

Org Owners can also choose to set two other app installation policies, whether app approval has been turned on for all workspaces in their org or not:

* **Slack Marketplace installations**: Only allow members to install apps from the [Slack Marketplace](https://slack.com/marketplace).
* **Guest app use restrictions**: Allow Multi-Channel Guests to use [slash commands](https://slack.com/help/articles/201259356) and [app shortcuts](https://slack.com/help/articles/360004063011) in channels they belong to.

1. From your desktop, click your **organization name** in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **_Settings_**, then select **Organization Policies**.
4. Click the **Apps** tab at the top of the page.
5. Next to the app policy you’d like to set, click **Add Policy**.
6. Check the box next to the policy description.
7. Select **Save Policy**. Then, click **Create Policy**.

**Who can use this feature?**

* **Org Owners** and **Org Admins**
* Available on **Enterprise** plans