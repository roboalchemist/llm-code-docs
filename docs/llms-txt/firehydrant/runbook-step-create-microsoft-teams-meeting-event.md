# Source: https://docs.firehydrant.com/docs/runbook-step-create-microsoft-teams-meeting-event.md

# Create Microsoft Teams Meeting (Event)

Microsoft Teams has built-in online meetings in the application. FireHydrant supports automatically creating a meeting via the Events API and including this link in the incident and any [Notify Microsoft Teams Channel](https://docs.firehydrant.com/docs/notify-microsoft-teams-channel-copy) cards posted to other channels, making it easy for anyone to jump straight to the meeting to collaborate.

## Configuration

<Image alt="Create a MS Teams meeting (event) step" align="center" width="650px" src="https://files.readme.io/8c4e549-CleanShot_2024-05-22_at_17.19.45.png">
  Create a MS Teams meeting (event) step
</Image>

This step comes with the following configurable fields:

* **Name** - A configurable name for the step. This shows up in the Runbook details tab for each incident and has no impact on actual execution
* **Meeting Topic** - Sets the meeting name/topic in MS Teams\*\*
* **Meeting Agenda** - Sets the meeting agenda in MS Teams \*\*
* **Meeting Provider** - Usually one option, "Teams for Business." There may be other options depending on your Office365 administrator or IT admin. **If there are no options, you must also speak with your IT admin.**

> 📘 \*\*Note:
>
> These fields support both [Markdown](https://docs.firehydrant.com/docs/markdown-support) and [Template Variables](https://docs.firehydrant.com/docs/template-variables). MS Teams supports standard Markdown and has an [approximate limit of 28 KB per message](https://learn.microsoft.com/en-us/microsoftteams/limits-specifications-teams#chat).

## Tracking Meeting Messages in Incident Timeline

<Image alt="Start Meeting button within an MS Teams incident channel" align="center" width="650px" src="https://files.readme.io/b604e70-CleanShot_2024-07-03_at_17.10.142x.png">
  Start Meeting button within an MS Teams incident channel
</Image>

If you create a Meeting via this Runbook step, it is ***separate*** and detached from the incident due to API limitations in Microsoft Teams.

However, if you manually start a Meeting from within the incident channel, all chat messages on that Meeting are posted into the channel by default, and in turn, will automatically replicate to the FireHydrant timeline.

If this is important to you, we suggest using a [Notify Microsoft Teams Incident Channel w/ Custom Message](https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-incident-channel-w-custom-message) step to tell your responder(s) to manually start the meeting by the clicking the button.