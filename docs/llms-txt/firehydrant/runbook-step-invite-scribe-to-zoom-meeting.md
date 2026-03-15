# Source: https://docs.firehydrant.com/docs/runbook-step-invite-scribe-to-zoom-meeting.md

# Invite Scribe to Zoom Meeting

<Image align="center" alt="End Linked Zoom Meetings step" border={false} caption="Invite Scribe to Meeting step" src="https://files.readme.io/fc77b5c6ace17c008dea4b4c44981829ce0449b0ee89a212530c9e47edcb325d-CleanShot_2024-09-06_at_09.56.172x.png" width="650px" />

This Runbook step is useful for when you'd like to invite FireHydrant's [AI Scribe](https://docs.firehydrant.com/docs/ai-meeting-transcription) for Zoom to a meeting bridge that it isn't already on.

> 🚧 Note:
>
> This step is not needed if you are creating and starting a Zoom call for the first time with Runbooks - simply use the [Create a Zoom Meeting](https://docs.firehydrant.com/docs/runbook-step-create-a-zoom-meeting) step and make sure you have "Transcribe meeting?" option set to **Yes**.
>
> This step is intended for inviting the scribe to a meeting *again* or for inviting the scribe to a meeting that is not created/managed by FireHydrant.

**Prerequisites**

The AI scribe relies on local recording permissions. Within your Zoom account settings, ensure that 'Record to computer files' is enabled and that external meeting participants can request permission to record.

We recommend enabling this on an organization level for the most consistent transcription experience.

<Image border={false} src="https://files.readme.io/a797cc7966ab6ff44db282cb4ad287eda971eedc3a837f815619faef609f84af-image.png" />

<br />

<br />

This step comes with the following parameters:

* **Name** - A name for the Runbook step. This largely doesn't matter except for when you're browsing step status in incidents
* **Meeting URL** (optional) - If nothing is specified here, FireHydrant will invite the scribe to the latest meeting on the incident. If you have a specific meeting you want to invite it to, you'll need to put the value or insert Liquid templating here.

If necessary, users can for example configure this Runbook step to be repeated on an interval and set to manual execution - this allows responders to essentially stop a meeting bridge and reconvene at a later date as many times as needed and manually re-invite the Incident Scribe to the bridge by triggering the step in [The Command Center](https://docs.firehydrant.com/docs/the-command-center).

<Image align="center" alt="Example of re-executing the Invite Scribe step manually from Command Center" border={false} caption="Example of re-executing the Invite Scribe step manually from Command Center" src="https://files.readme.io/c1684c09a4b1080e68a546395d75c5186c30dba086e24f894727f17f4cf78b43-CleanShot_2024-09-06_at_10.29.032x.png" width="650px" />

<br />