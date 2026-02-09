# Manage app requests for your workspace

If [app approval](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace) is turned on for a workspace, members have the option to request apps and workflow [connector steps](https://slack.com/help/articles/20155812595219-Slack-connectors-for-Workflow-Builder) they’d like to use in Slack. By default, only Workspace Owners can review app requests, but they can also allow other members to do so by [appointing them as app managers](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#appoint-app-managers).

**Tip:** Workspace Owners can use [app approval automations](https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval) to approve app requests based on a series of pre-determined conditions.

## What to expect

- App requests are sent to all Workspace Owners and app managers. Depending on a workspace's settings, requests may be delivered via direct messages from Slackbot or routed to a channel.
- Workspace Owners and app managers can approve apps for all members of a workspace to use, or restrict them.
- Members may need to request apps already installed to a workspace if the app’s developer changes the scopes.

## Review app requests

App requests will include the name of the app, the requester, a list of the [permissions (or scopes)](https://slack.com/help/articles/115003461503-Understand-app-permissions) the app can access in Slack if it’s approved for use, and additional comments if available. To review requests, follow the steps below:

1. When you receive a request, open your direct message with Slackbot, or the channel that requests are sent to.
2. Review the request. Select **Approve for Workspace** or **Restrict for Workspace**. Choosing **Restrict for Workspace** will prevent all members from requesting or installing the app.

![Direct message from Slackbot with an app request, including the app details and buttons for approving or restricting the app for your workspace](https://slack.zendesk.com/hc/article_attachments/32816142481427)

When the status of a request is changed, Slack will update the original request message to reflect the action for all app managers to see.

**Tip:** Workspace Owners and app managers can also approve, restrict, or cancel any pending requests from the **Requests to install** tab on the [Apps page](https://app.slack.com/apps-manage) in the Slack Marketplace.

## Apps and scopes

Scopes are a [set of permissions](https://slack.com/help/articles/115003461503-Understand-app-permissions) that govern what an app can do and access when installed to a Slack workspace.

If an app’s developer changes the scopes of an app after it was installed to your workspace, members may need to request the app again so that someone with permission can review the new scopes. If an app manager restricts an app’s new scopes, members can continue using the existing version of the app, but cannot install or use the updated version.

**Note:** In an Enterprise organization, [org-level app requests](https://slack.com/help/articles/360000281563-Manage-apps-in-an-Enterprise-organization#manage-app-requests) for apps with scope changes will be sent to Org Owners and Org Admins in a DM from Slackbot.

### Who can use this feature?

- **Workspace Owners** and **members** with permission to manage apps
- Available on [**all plans**](https://slack.com/pricing)