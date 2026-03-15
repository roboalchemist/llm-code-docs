# Source: https://docs.firehydrant.com/docs/microsoft-teams-integration.md

# Microsoft Teams

This article details setting up the FireHydrant MS Teams bot v2, allowing you to take control of incidents from Microsoft Teams end-to-end.

## Features and capabilities

* Automatically create channels, group chats, and meetings for incidents (via [Microsoft Teams](https://docs.firehydrant.com/docs/runbooks-microsoft-teams) runbook steps)
* Automatically post notifications or update notes to other channels in MS Teams (also via runbook steps)
* Fully drive incidents end-to-end from Microsoft Teams without leaving the app (via MS Teams bot, see instructions below for setup)
* All features of platform are available in MS Teams (except for some [Signals/alerting](https://docs.firehydrant.com/docs/signals-introduction) capabilities still on roadmap)

## Prerequisites

* **You will need <Glossary>Owner</Glossary> permissions in FireHydrant**
* **You will need admin permissions in Microsoft to configure a Service Account with the right permissions and install the FireHydrant bot**

## Authorize the Integration on FireHydrant

Installing Microsoft Teams with FireHydrant involves two steps: 1) Authorizing the integration and 2) Installing the bot in your Teams instance. You'll need to go through both steps to enable FireHydrant in Microsoft Teams.

### Office365 Service Account

Before installing the integration on FireHydrant, you'll need a Service Account that FireHydrant can act as when acting in Microsoft Teams. Messages posted in MS Teams will appear as this user, so we recommend something descriptive like "FireHydrant User" or "FireHydrant," etc. to disambiguate from real team members.

> 📘 Note:
>
> As with other FireHydrant integrations, we recommend authorizing Microsoft Teams with a Service Account in your Office ecosystem. This prevents problems if named users leave your organization and can help differentiate automated messages from messages posted by a real user.

This Office365 user will also require the following capabilities/entitlements:

* Microsoft 365 Apps for Business
* Microsoft Teams Essentials
* Exchange Online
* Added as a member to every Team you expect Runbooks to post notifications/messages into

Once the user is provisioned in Microsoft Teams, any Team that will be conducting incidents in FireHydrant will need to allow its members the following permissions:

* Add and edit channels
* Add, edit, or remove tabs

<Image align="center" alt="Permissions needed for FireHydrant service account to function for Teams managing incidents" border={false} caption="Permissions needed for FireHydrant service account to function for Teams managing incidents" src="https://files.readme.io/68c0501-CleanShot_2024-06-27_at_09.46.31_Annotated.png" width="650px" />

### Install the integration on FireHydrant

**Logged in as the Service User you created above, follow the instructions below:**

1. Go to [FireHydrant's integrations page](https://app.firehydrant.io/organizations/integrations). Search for and click "Microsoft Teams".
2. To initiate the integration, click "Authorize Application." This action will redirect you to your Microsoft login page for authentication. Please ensure you're logged into a Service Account with proper permissions, and follow the on-screen prompts to complete the process.

This connects FireHydrant to your Microsoft Teams instance and allows us to post messages into channels across any teams the authorizing user can access and create incident channels in specific Teams.

## Installing the FireHydrant bot in Teams

<Image align="center" alt="Installing FireHydrant from app marketplace" border={false} caption="Installing FireHydrant from app marketplace" src="https://files.readme.io/62a99da-CleanShot_2024-06-27_at_12.05.48.png" width="650px" />

Installing the FireHydrant bot is required to enable all capabilities, including creating incident channels, posting into channels, executing commands, and conducting incidents from Microsoft Teams.

The FireHydrant bot will request the following scopes:

| Scope                              |
| :--------------------------------- |
| `Channel.Create`                   |
| `Channel.ReadBasic.All`            |
| `ChannelMessage.Read.All`          |
| `ChannelMessage.Send`              |
| `OnlineMeetings.ReadWrite`         |
| `openid`                           |
| `email`                            |
| `profile`                          |
| `User.Read`                        |
| `offline_access`                   |
| `TeamsTab.Create`                  |
| `TeamsTab.Read.All`                |
| `TeamsTab.ReadWrite.All`           |
| `TeamsTab.ReadWrite.Chat`          |
| `TeamsTab.ReadWriteSelfForTeam`    |
| `TeamsAppInstallation.ReadForTeam` |

**To install the FireHydrant teams bot**:

1. After authorizing the integration on FireHydrant, switch to Microsoft Teams. On the left-hand side, go to "+ Apps" search for FireHydrant in the store and click "Add".
2. On this screen. click the dropdown next to "Add" and choose a primary channel for the Team you'd like to install the bot

   <Image align="center" alt="Add bot to Team/channel" border={false} caption="Add bot to Team/channel" src="https://files.readme.io/372f67a-CleanShot_2024-06-27_at_12.08.07.png" width="400px" />
3. On this page, click on the dropdown to the right of "Add" and click "Add to a team." Select a Team and primary channel (we recommend **General**) to install the bot and the FireHydrant tab. Click "Set Up."
   1. **Note:** You must install the bot for each Team that needs to access a FireHydrant tab and execute FireHydrant commands, like creating new incidents and managing incidents.
4. Once you click "Set Up", the modal should confirm the app has been configured and then direct you to press "Save" to mount the app. You can optionally post to the channel about the new FireHydrant tab installed.

### Adding FireHydrant Bot to More Teams

<Image align="center" alt="Adding the FireHydrant bot to more Teams" border={false} caption="Adding the FireHydrant bot to more Teams" src="https://files.readme.io/60e5779-CleanShot_2024-07-03_at_09.17.182x.png" width="650px" />

To add the bot to more teams, you'll want to navigate to your directory of installed applications and then click the ellipses next to the installed app. From there, you'll be presented with the same page/modal as the previous section, where you can add the bot to a specific Team, Chat, or Meeting.

## User Logins

Finally, once the bot has been installed, users must log in to FireHydrant twice: once when executing commands, and the other when clicking into the Tab view.

### Command Login

<Image align="center" alt="Logging in to execute bot commands" border={false} caption="Logging in to execute bot commands" src="https://files.readme.io/a5c96b0-CleanShot_2024-05-22_at_15.26.49.png" width="400px" />

A user can initiate command login by executing `@FireHydrant login`. Alternatively, if they attempt to run any other commands, FireHydrant will automatically prompt for a login if they are not already.

Clicking the "Log in" button will open a browser window for the user to log into FireHydrant. Once they do so, their user account will be linked, and any `@FireHydrant` commands should start working.

**Bot logins persist across all instances of MS Teams**. So you only need to log in once via Command and you will be able to execute FireHydrant commands from e.g., MS Teams on your phone, MS Teams on desktop, web, etc.

### Tab Login

<Image align="center" alt="FireHydrant Tab view" border={false} caption="FireHydrant Tab view" src="https://files.readme.io/1924af4-CleanShot_2024-05-22_at_15.30.37.png" width="650px" />

The Tab view is each user's personal view of FireHydrant. It can be thought of as an additional portal into their FireHydrant account. So even though the Tab is installed on a shared channel, each user's view of it differs, and subsequently, they must log in to FireHydrant.

Like the above command flow, users can click the "Log in" button and follow the on-screen prompts to link to their user in the chosen FireHydrant organization.

They will see the list of all incidents they have access to, and if the tab exists in an incident channel, will be able to see and interact with the incident in that Tab as themselves.

**Unlike Bot logins, Tab logins are local sessions and remain local to the device you log in with.** To view FireHydrant incidents on the Tab on a different device, you must log in again on that device.

### Multiple Organization Support

FireHydrant offers multiple [Organizations](https://docs.firehydrant.com/docs/organizations) to logically separate different business units, sandboxes from prod, etc. Users can log out of existing connections and log back in, authorizing the different organization they would like to switch to.

## Enabling Non-Licensed users to Declare Incidents

<Image align="center" alt="Explanation/help for the `@FireHydrant add bot token` command" border={false} caption="Explanation/help for the `@FireHydrant add bot token` command" src="https://files.readme.io/2aa1b57-CleanShot_2024-06-06_at_20.57.19.png" width="400px" />

By default, the FireHydrant bot works for licensed users (who have FireHydrant accounts). To allow non-licensed users to execute basic commands like declaring incidents and seeing who's on call, you'll first need to set an API key for non-licensed executions.

1. First, [create API Keys](https://docs.firehydrant.com/docs/api-keys) in FireHydrant and then copy the value.
2. Run the `@FireHydrant add bot token` command in Microsoft Teams and paste the API key you created in.

Once done, any non-licensed users should be able to run basic, non-state-changing commands like `new`, `help`, `on-call`, and `page`.

## To remove your Teams integration

1. Go to [FireHydrant's integrations page](https://app.firehydrant.io/organizations/integrations) and click Microsoft Teams.
2. Edit the MS Teams integration
3. Select Uninstall
4. Remove the bot from your Team/Workspace in Microsoft Teams

## Next Steps

* See what automation steps are available for the v2 MS Teams integration:
  * [Create Incident Channel](https://docs.firehydrant.com/docs/runbook-step-create-microsoft-teams-incident-channel)
  * [Notify Channel](https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-channel)
  * [Notify Channel w/ Custom Message](https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-channel-w-custom-message)
  * [Notify Incident Channel w/ Custom Message](https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-incident-channel-w-custom-message)
* Browse [all available Microsoft Teams Actions](https://docs.firehydrant.com/docs/microsoft-teams-commands)