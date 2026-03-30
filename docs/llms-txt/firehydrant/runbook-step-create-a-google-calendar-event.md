# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-google-calendar-event.md

# Create a Google Calendar Event

FireHydrant makes it easy to automatically spin up a meeting bridge and invite an AI incident scribe as part of the incident process. Once the calendar event is created, a link to it will automatically be included on the channel's pinned message and anywhere FireHydrant has posted a [templated notification](https://docs.firehydrant.com/docs/runbook-step-notify-channel).

This event link will then have the corresponding meeting bridge linked to it.

## Prerequisites

To use this step, you must have configured your [Google Calendar](https://docs.firehydrant.com/docs/google-calendar-integration) integration.

## Add Runbook step

<Image alt="Finding the Google Calendar Event step" align="center" width="650px" src="https://files.readme.io/bc2af3a-CleanShot_2024-05-28_at_17.22.03.png">
  Finding the Google Calendar Event step
</Image>

1. To add the step, edit or create a new Runbook and search for the Google Calendar step.
2. This step contains the following configurable fields:
   1. **Name**: An internal name provided for your step. This is what it will show as when viewing Runbook executions on incidents
   2. **Event Summary**: The name of the calendar event\*\*
   3. **Event Description**: A description for the calendar event\*\*
   4. **Transcribe Meeting?**: Enabling this will invite the FireHydrant AI Copilot to join the Google meeting and automatically transcribe the conversation, making it available as context to generate summaries and draft answers for inputs.
      1. **Note:** Requires AI capabilities to be enabled in your settings. To learn more about our AI features and enable them, visit [AI-Powered Incident Management](https://docs.firehydrant.com/docs/ai-powered-incident-management).

> 📘 \*\*Note:
>
> These fields support [Template Variables](https://docs.firehydrant.com/docs/template-variables) and [Markdown Support](https://docs.firehydrant.com/docs/markdown-support).

3. Once finished configuring, click "Next" and "Add Step" before saving the Runbook and persisting changes.

On your next incident with this Runbook step executing, you will now see a Google Meet link in the list of the incident's links:

<Image alt="Google Meeting link on the incident" align="center" width="400px" src="https://files.readme.io/346a3ab-CleanShot_2024-05-29_at_12.03.25.png">
  Google Meeting link on the incident
</Image>

If meeting transcription is enabled, once someone is on the call, they will receive a notification that someone would like to be admitted. That "user" will be called the **FireHydrant Scribe**. Admit them to the meeting to begin transcription.

<Image alt="Admitting the FireHydrant Scribe to the meeting" align="center" width="400px" src="https://files.readme.io/da0d6fe-CleanShot_2024-05-29_at_12.05.34.png">
  Admitting the FireHydrant Scribe to the meeting
</Image>

> 📘 Note:
>
> Google Meet has a 10 minute waiting room timeout. If someone doesn't join the meeting and admit the FireHydrant Scribe within 10 minutes of the meeting starting, the Scribe will not be able to join the meeting afterwards.