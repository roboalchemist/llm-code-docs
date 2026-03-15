# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-zoom-meeting.md

# Create a Zoom Meeting

<Image alt="Example incident with a Zoom bridge" align="center" src="https://files.readme.io/01294d1-Screenshot_2023-12-20_at_5.31.56_PM.png">
  Example incident with a Zoom bridge
</Image>

As part of [Runbook automation](https://docs.firehydrant.com/docs/runbook-basics), FireHydrant can spin up a Zoom meeting bridge for your incident responders.

## Prerequisites

This requires that you have configured the [Zoom](https://docs.firehydrant.com/docs/zoom-integration) integration.

## Adding the Runbook step

After you have set up the Zoom integration, you can add a **Create Meeting** step to any incident type Runbook in FireHydrant.

1. Go to Edit or create a Runbook, click "+ Add step", and then search for Zoom.
2. Specify the **meeting topic** and **agenda** (these fields support [template variables](https://docs.firehydrant.com/docs/template-variables) and the following options:
   1. **Record Meeting** - Allows recording to cloud, desktop, or no recording
   2. **Automatically attach links to cloud recordings** - FireHydrant can automatically attach a link to the Zoom recording after processing. This only works when **Record to cloud** is selected for the above option
   3. **Transcribe Meeting (requires AI)** - Enables FireHydrant's [AI Meeting Transcription](https://docs.firehydrant.com/docs/ai-meeting-transcription) bot to join the call and transcribe the meeting for contextual use in summaries and response generations
3. Configure step conditions as needed. The default behavior is always and automatically when the incident kicks off.

With these settings configured, your team can access an incident-specific Zoom meeting whenever this Runbook step is executed.

<Image alt="Zoom bridge link visible on the pinned message in the incident channel" align="center" width="650px" src="https://files.readme.io/7c92be1-image.png">
  Zoom bridge link visible on the pinned message in the incident channel
</Image>

## Meeting Host

By default, FireHydrant will attempt to create the meeting with the **user who creates the incident**. If for some reason their FireHydrant and Zoom accounts have not been linked, FireHydrant falls back to using the default authorizing account.

For more information, visit [Zoom](https://docs.firehydrant.com/docs/zoom-integration) integration docs.