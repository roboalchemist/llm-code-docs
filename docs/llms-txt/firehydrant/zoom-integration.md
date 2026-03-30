# Source: https://docs.firehydrant.com/docs/zoom-integration.md

# Zoom

The Zoom integration lets you configure Runbooks to spin up a Zoom conference bridge for your team to use during incidents.

> 📘 Multi-Organization Support:
>
> The Zoom integration now supports installation across multiple FireHydrant organizations, allowing non-default organizations to install and configure their own Zoom integrations independently.

## Prerequisites

* You'll need <Glossary>Owner</Glossary>  or `manage_intergrations` permissions in FireHydrant to configure integrations
* You'll need a **service account**/**user** with **Developer** privileges in Zoom

> 📘 Note:
>
> FireHydrant recommends using a generic service account/user to authorize the integration with Zoom. This is to prevent potential problems with tethering to specific named users in the case their accounts are decommissioned from e.g., departure.

## Installing the Zoom OAuth integration

<Image align="center" alt="Zoom app tile in the integrations list" border={false} caption="Zoom app tile in the integrations list" src="https://files.readme.io/5b50eb6-Screenshot_2024-01-09_at_2.42.20_PM.png" width="650px" />

1. Go to FireHydrant's [Integrations page](https://app.firehydrant.io/organizations/integrations) search for the **Zoom** app. Click the '+'.
2. Click **Authorize Application**.  This will take you to the Zoom login page.
3. Check "Allow this app to use my shared access permissions." Follow through the rest of the on-screen prompts to authorize the FireHydrant integration.
4. You're all set!

### Linking Individual Accounts

With Zoom, meetings are created under individual users. This can sometimes cause problems if the default authorized user you set up the integration with doesn't have enough concurrent meeting licenses.

FireHydrant addresses this by attempting to create meeting bridges under each incident opener’s email or ID. Using individual user accounts to create meeting bridges—as opposed to using the default authorized user to create every bridge—also helps avoid triggering Zoom’s rate limits for your organization. However, for FireHydrant to do this, each user must go to their User Settings and link their Zoom account to their FireHydrant account. Each user should:

<Image align="center" alt="User Profile settings" border={false} caption="User Profile settings" src="https://files.readme.io/b1d34ff-CleanShot_2024-04-23_at_17.12.37.png" width="400px" />

1. Click their user profile dropdown on the top right corner and then **Profile**.
2. On this page, scroll down to the **Linked Accounts** section and locate the **Link Zoom** button. This will take the user to another screen where FireHydrant requests additional permissions in Zoom (e.g., to create meetings as them). Once this is done, they should see a checkmark indicating their user accounts have been linked between the two platforms.

<Image align="center" alt="User account linking page for a specific organization" border={false} caption="User account linking page for a specific organization" src="https://files.readme.io/0451996-CleanShot_2024-04-23_at_17.15.09.png" width="400px" />

When this is finished, FireHydrant will automatically create Zoom bridges with this user as the host if they open the incident. If this fails, FireHydrant will fall back to the Default Authorized User, which you can find in the Zoom integration settings.

> 📘 Note:
>
> We recommend considering [Zoom's Concurrent Meeting licenses](#zoom-concurrent-meetings-and-pricing-plans) for your Default Authorized User in the off-chance multiple incidents/Zooms are kicked off under this user.

## Recommended Zoom Settings

The following settings are recommended for the default authorized user and in some cases, for other users who may be creating incidents and spinning up Zoom meetings.

### Personal Meeting ID

To avoid meeting conflicts, ensure that the Zoom account of the default authorized user has the Personal Meeting ID scheduling option disabled. To disable it:

1. As the user, sign in to Zoom
2. Go to Settings
3. Make sure **Use Personal Meeting ID (PMI) when scheduling a meeting** and **Use Personal Meeting ID (PMI) when starting an instant meeting** are both DISABLED.

If these settings are enabled, the same Zoom meeting ID will be used for each incident, causing collisions if multiple incidents are in play simultaneously.

<Image align="center" alt="Ensure Personal Meeting ID is OFF for the default authorized user" border={false} caption="Ensure Personal Meeting ID is OFF for the default authorized user" src="https://files.readme.io/22e4e01-zoom-oauth-pmi.png" width="400px" />

### Waiting Room and Host

You'll also want to allow users to join the meeting before the host and turn off the **Waiting Room** feature in Zoom. If you don't do this, your incident responders may be stuck waiting for the meeting creator to join the meeting and admit them into the call.

<Image align="center" alt="Ensure participants are allowed to join the call before host" border={false} caption="Ensure participants are allowed to join the call before host" src="https://files.readme.io/1a8e3b5-zoom-join-before-host.png" width="650px" />

<Image align="center" alt="Ensure the waiting room is turned OFF" border={false} caption="Ensure the waiting room is turned OFF" src="https://files.readme.io/571da14-zoom-waiting-room.png" width="650px" />

## Zoom AI Transcription

FireHydrant's AI Copilot can join meetings automatically and transcribe conversation and audio happening on the bridge. This has a few prerequisites:

* [AI features](https://docs.firehydrant.com/docs/ai-powered-incident-management) must be turned on
* Your [Zoom Meeting Runbook step](https://docs.firehydrant.com/docs/runbook-step-create-a-zoom-meeting) must have the **Transcribe Meeting?** option set to **Yes**.

### Transcription settings

If you intend to utilize meeting transcription, the AI scribe relies on local recording permissions. Within your Zoom account settings, ensure that 'Record to computer files' is enabled and that external meeting participants can request permission to record.

We recommend enabling this on an organization level for the most consistent transcription experience.

<Image border={false} src="https://files.readme.io/a797cc7966ab6ff44db282cb4ad287eda971eedc3a837f815619faef609f84af-image.png" />

### Allowing the Scribe to join and record

FireHydrant’s Zoom transcription feature relies on a transcription bot provided by Recall.ai.

Once a meeting is created, this bot is invited to join the call. In order for the bot to begin recording, it must be granted recording permissions — a privilege that can only be granted by the meeting host.

To streamline this process, FireHydrant uses dynamic host assignment. As participants join the meeting, we check whether a host still needs to be assigned. If so, we make a series of requests to the Zoom API — first to retrieve user and meeting details, and then to assign a new host.

These API requests use an auth token from the same Zoom user account that created the meeting. Effectively, we act as this Zoom to facilitate host assignment. For the host assignment to complete successfully, this Zoom user must have the necessary permissions to make the relevant API requests.

Zoom’s API requires a Zoom user within the same Zoom account (Zoom organization)  to make these requests, therefore we have to rely on the integration and/or individual Zoom user accounts provided by the customer.

<Callout icon="📘" theme="info">
  **Note**:

  Since Zoom does not update host status in real time, newly assigned hosts must leave and rejoin the meeting for their updated status to be recognized. This step ensures that both the meeting and the bot can correctly detect the host.
</Callout>

To facilitate this, we have a notification process in place. If we’re able to retrieve a user’s Zoom details, we attempt to match their Zoom identity with their FireHydrant user account. If the match is successful, we send them a private Slack message (a "whisper") to inform them of their new host status and the need to rejoin the meeting. If we can’t resolve the corresponding Slack user, we post one success message and, if applicable, one failure message in the incident channel — both of which include guidance on what action is required.

Once the bot detects a valid host is present, it will request recording permissions. If granted, the bot will record the call and generate a transcription, which becomes available after the meeting ends.

## Uninstalling the Zoom integration

1. To remove the Zoom OAuth integration, navigate to the Zoom settings page in the integrations list and click **Uninstall Zoom**.
2. In addition, in Zoom, you will want to navigate to your app marketplace and then remove the FireHydrant app from your organization.

<Image align="center" alt="Removing the FireHydrant app from your Zoom marketplace" border={false} caption="Removing the FireHydrant app from your Zoom marketplace" src="https://files.readme.io/4f3fae3-Screenshot_2024-01-09_at_3.13.15_PM.png" width="650px" />

## Next Steps

* Now that your Zoom integration is configured, you can automate spinning up meeting bridges [via a Runbook step](https://docs.firehydrant.com/docs/runbook-step-create-a-zoom-meeting)
* Explore [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)

## Zoom Troubleshooting

### Org-Level Settings

Zoom allows meeting settings at multiple levels: individual, user group, and organization-wide.

If these settings above are not working as expected, or you cannot configure them for users, you may want to reach out to your Zoom administrator to understand if any group-level or organization-level settings override individual settings.

See [Zoom's documentation here](https://support.zoom.us/hc/en-us/articles/204519819-Managing-user-groups-and-settings).

### Breakout Rooms

Currently, Zoom's API [does not have breakout rooms capability](https://devsupport.zoom.us/hc/en-us/articles/360059893952-Breakout-Rooms-API), so FireHydrant cannot set this from our side programmatically.

**Users must manually configure and set up Breakout Rooms when they join the meeting.**

> 📘 Note:
>
> As mentioned in above documentation, FireHydrant will default to the host's settings, so if they have Breakout Rooms enabled, then the capability should be available once your responders have joined the meeting. If you're still not seeing this, check that there aren't org-level settings overriding your user-level settings in Zoom, and that you've [linked your FireHydrant and Zoom accounts](#linking-individual-accounts).

### Passcode Enforcement

FireHydrant requests a passcode when making the API call to Zoom. However, it is up to the organization in Zoom's settings to actually enforce this. If you are finding some users can join incident bridges without a passcode:

* Check that there aren't organization-level rules that allow users to join meetings without passcodes in Zoom
* Check that there aren't individual users who have been allowed to bypass these passcode requirements in Zoom

### Meeting Creation

On Zoom, all meetings must be created under a specific user (e.g., there's no generic meeting, as all meetings must have a primary Host). FireHydrant attempts to create Zoom meetings using the person who opened the incident on FireHydrant, but to use the incident opener as the host, they must have linked their FireHydrant account with their Zoom account (see screenshot below).

<Image align="center" border={false} caption="Where to link accounts on FireHydrant" src="https://files.readme.io/f23d17dcd35ddc7c25fde8be7d8c3b8283bd0a0eede8b237a1096b82dcd5d0e8-CleanShot_2025-10-01_at_12.38.00.jpg" width="650px" />

If the user who created the incident does not have a linked Zoom account, FireHydrant will default to the **Default Authorized User**, or whoever set up the initial Zoom integration, as a fallback.

### Zoom Concurrent Meetings & Pricing Plans

As mentioned above, Zoom meetings must be created for a specific host. This can sometimes cause issues, as Zoom only allows one (1) concurrent meeting per user on **Free** and **Pro** plans, and only up to two (2) concurrent meetings on **Business**, **Education**, and **Enterprise** pricing plans even if the host is not in the meeting(s).

However, concurrent meeting licenses can be purchased through your Zoom account team. We recommend reaching out to them to learn more about your options as they offer licenses that can support anywhere from 3-4 up to 20 concurrent meetings on a single user account.

Once procured, the license will appear in your Zoom account. Your Zoom admin can apply those concurrent licenses to an account by following these instructions:

1. Go to User Management > Users from the Zoom admin console
2. Click Edit next to the account they want to apply the license to
3. Select the checkbox next to "Concurrent Meeting"
4. Save

### "Waiting for Host"

If you encounter an error indicating that the Zoom meeting is waiting for the host, verify the following:

* That you are logged into your Zoom account
* That you've configured the [waiting room settings](#waiting-room-and-host) above
* That there aren't any [org-level settings](#org-level-settings) overriding the individual authorized user settings

### "The host has another meeting in progress"

If you encounter an error about the host having another meeting in progress, verify:

* That the host of this meeting is the person who opened the incident
  * If not, ensure that their email address in Zoom matches their email address in FireHydrant
* That you are on a Zoom pricing plan that allows for concurrent meetings