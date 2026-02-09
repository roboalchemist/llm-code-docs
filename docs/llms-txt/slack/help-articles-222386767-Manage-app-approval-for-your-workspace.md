# Manage app approval for your workspace

Apps connect third-party services to Slack, and by default, members can install them without approval from a Workspace Owner. If they'd like, Workspace Owners can [enable app approval](#h_01F29Z6B2ZN8PEXHG9N1GYDV6N) to pre-approve or restrict certain apps for their workspace. With app approval enabled, Workspace Owners can manage the following settings:

- Allow members to [request apps](#h_01F29Z6B2ZN8PEXHG9N1GYDV6N) and [Workflow Builder connector steps](https://slack.com/help/articles/16749280664595-Manage-access-to-Slack-Workflow-Builder-connectors) that have not been pre-approved
- Create custom rules to automate app requests
- [Grant members permission](#h_01F29Z6HFHN7ARSCM4ABVF99C9) to manage app requests
- Decide whether members can [sign in to other services](#h_01F29XF1TKT2JQJP2CJ19M4GJM) with their Slack accounts

**Note:** Workspace Owners can also [set other permissions](https://slack.com/help/articles/1500009181142-Manage-app-settings-and-permissions) to manage how apps work in Slack, whether app approval is enabled or not.

## Manage app approval

Workspace Owners can enable app approval to pre-approve and restrict certain apps for their workspace:

1. From your desktop, click **Admin** in the sidebar.
2. Select **Apps and workflows** from the menu to open the Slack Marketplace.
3. Click **App Management Settings** in the left sidebar.
4. Click **Edit** next to **Require approved apps**.
5. Check the box next to **Only allow pre-approved apps**, then click **Save**.

**Note:** If you're a Workspace Owner in an Enterprise organization, app approval will automatically be enabled for your workspace if an Org Owner has set an [app management policy](https://slack.com/help/articles/360038559694-Set-organization-level-policies-for-apps).

### Pre-approve or restrict apps

When app approval is enabled, members can install and start using pre-approved apps right away. They cannot install or [request](#h_01GRSNHBF901Z8KBT5AFA7W01F) any apps you choose to restrict.

#### Pre-approve apps

1. From your desktop, click **Admin** in the sidebar.
2. Select **Apps and workflows** from the menu to open the Slack Marketplace.
3. Click **Browse** in the top right.
4. Search for and select an app.
5. From the app page, click **Approve**.

Members can find pre-approved apps for your workspace from the [Pre-Approved category](https://my.slack.com/marketplace/category/approved) in the Slack Marketplace.

#### Restrict apps

1. From your desktop, click **Admin** in the sidebar.
2. Select **Apps and workflows** from the menu to open the Slack Marketplace.
3. Click **Browse** in the top right.
4. Search for and select an app.
5. From the app page, click **Restrict**.

If an app you restrict has already been installed to your workspace, members can continue using it. You can [uninstall any app](https://slack.com/help/articles/360003125231-Remove-apps-and-custom-integrations-from-your-workspace) you don't want people to use.

**Note:** When approving a request to install an app, you are approving the [scopes](https://api.slack.com/scopes) it will use to take actions in your workspace. An app's steps and workflows use the same scopes and can be added after an [internally developed app](https://api.slack.com/automation/create) is requested and approved.

## Choose how to manage app requests

### Allow members to request apps

When app approval is enabled, you can allow members to request apps that haven't been pre-approved (as long as they're not restricted). Here's how:

1. From your desktop, click **Admin** in the sidebar.
2. Select **Apps and workflows** from the menu to open the Slack Marketplace.
3. Click **App Management Settings** in the left sidebar.
4. Click **Edit** next to **Require approved apps**.
5. Check the box next to **Allow members to request apps for approval**. You can also require comments along with app requests.

### Create automation rules

If you'd like, you can configure rules that automatically review app requests. Requests can be approved, restricted, dismissed, or flagged for human review based on conditions your rules look out for. To learn more about automation rules, [read our guide](https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval), then follow the steps in [Configure automations for app approval](https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval).

### Select members to help manage app requests

By default, any app requests that need review are sent to Workspace Owners via direct messages from Slackbot. If you'd like a larger group to help review app requests, you can appoint other members as app managers:

1. From your desktop, click **Admin** in the sidebar.
2. Select **Apps and workflows** from the menu to open the Slack Marketplace.
3. Click **App Management Settings** in the left sidebar.
4. Click **Edit** next to **Require approved apps**.
5. Below **Select App Managers**, choose **Workspace Owners and selected members or groups**. Then, select specific members or [user groups](https://slack.com/help/articles/212906697-Create-a-user-group) from the drop-down menu.

**Tip:** If you're using [automation rules](https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval), you can create a rule to send app requests to a channel all of your app managers belong to for review.

## Manage Sign in with Slack permissions

Some third-party services offer the option to [sign in to their website or app using your Slack account credentials](https://slack.com/help/articles/218891278-Connect-to-other-services-using-your-Slack-account). By default, members cannot sign up for or sign in to other services with their Slack accounts. To grant this permission, follow the steps below:

1. From your desktop, click **Admin** in the sidebar.
2. Select **Apps and workflows** from the menu to open the Slack Marketplace.
3. Click **App Management Settings** in the left sidebar.
4. Click **Edit** next to **Require approved apps**.
5. Below **Sign in with Slack**, check the box to **Allow members to use their Slack account credentials to sign into 3rd party websites.**

**Who can use this feature?**

- **Workspace Owners**
- Available on [**all plans**](https://slack.com/pricing)