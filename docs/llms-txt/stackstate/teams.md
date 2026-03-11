# Source: https://archivedocs.stackstate.com/monitors-and-alerts/notifications/channels/teams.md

# Teams

## Configure Teams notifications

To send notifications to Slack follow these steps:

1. [Create a Power Automate Flow](#create-a-power-automate-flow)
2. [Add and test the channel](#add-and-test-the-channel)

### Create a Power Automate Flow

In Teams, create a new Flow from the "Webhook" template. ![Create Flow from Webhook template](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-921b8397c6134158f10113068cd4d6b11977c09b%2Fnotifications-teams-webhook-template.png?alt=media)

Select the Team and Channel you want the notification pasted to and save the flow.

Edit the flow and click the "When a Teams webhook request is received" box.\
Copy the HTTP URL parameter.

![Select URL from Flow](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-fe7e7207c26fafccdf357b0efbec5c26ae72f59b%2Fnotifications-teams-select-url.png?alt=media)

## Add and test the channel

![Configure Teams Channe](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-4dcbdf8bd163bcaaf2ac946bfd16d3777f52e2c8%2Fconfigure-teams-channel.png?alt=media)

Back in StackState you can now use the Webhook URL to create a notification channel.

## Teams messages for notifications

When a notification is opened or closed a new Teams message is created in the channel.

<figure><img src="https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-b0b7d7205baf8cd7c7eaa4880299b6d894b169a8%2Fnotifications-teams-example.png?alt=media" alt="Teams example" width="75%"><figcaption><p>Teams messages for an open and close notification</p></figcaption></figure>

## Related

* [Troubleshooting](https://archivedocs.stackstate.com/monitors-and-alerts/notifications/troubleshooting)
