# Source: https://docs.rootly.com/integrations/microsoft-teams-meeting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Teams Meeting

> Create or join Microsoft Teams meetings directly from incidents and get meeting links in notifications.

## Installation

You can setup this integration as a **logged in admin user** in the integrations page.

<Note>
  We recommend you integrating with a **service account** to make sure the integration doesn't break if a user leaves your company.
</Note>

## Oauth Permissions

Your selected workspace needs the following oauth permissions:

* offline\_access
  * This permission is needed for to perform OAuth authentication.
* User.Read
  * Allows Rootly to have user information about who integrated the account. This permission is needed for our OAuth strategy.
* OnlineMeetings.ReadWrite
  * Allows an app to create online meetings on behalf of the integrated user account. The permission is needed for our app to access onlineMeeting resource.

## Join a meeting

Create or join a Microsoft Teams meeting is now just one click away ! Click on a incident and you should now see **Create a Microsoft meeting** in the header.

## Uninstall

1. Login to your **Microsoft Teams Meeting** account.
2. Click **Manage > Installed Apps** or search for the **Rootly** App.
3. Click the **Rootly** app.
4. Click **Uninstall**.


Built with [Mintlify](https://mintlify.com).