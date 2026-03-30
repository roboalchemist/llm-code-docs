# Source: https://docs.firehydrant.com/docs/ai-meeting-transcription.md

# AI Meeting Transcription

## Overview

FireHydrant's meeting-aware context enriches your incidents with insights directly from meeting transcripts. This ensures comprehensive situational awareness for all team members, regardless of their physical presence in bridges. Never worry about scribing live calls again, FireHydrant will take care of that for you.

FireHydrant currently supports meeting transcription for our [Google Calendar](https://docs.firehydrant.com/docs/google-calendar-integration) and [Zoom](https://docs.firehydrant.com/docs/zoom-integration) integrations.

After enabling, the FireHydrant Scribe will be invited to your meetings to capture crucial discussions and decisions made during incident bridges, providing a richer, more nuanced overview of the incident's progression.

## Prerequisites

* You will need to have either the [Google Calendar](https://docs.firehydrant.com/docs/google-calendar-integration) or [Zoom](https://docs.firehydrant.com/docs/zoom-integration) integrations installed (requires <Glossary>Owner</Glossary> permissions)
* You'll need to have [enabled AI features for your org](https://docs.firehydrant.com/docs/ai-powered-incident-management) (requires <Glossary>Owner</Glossary> permissions)
* You'll need at least <Glossary>Member</Glossary> permissions to configure Runbooks

## Enabling transcripts

### For Zoom Users Before April 2024

If you're configuring Google Calendar or Zoom for the first time after April 2024, you can skip to the next section.

If you installed the Zoom integration before April 2024, you will need to **Reauthorize** to grant additional permissions for meeting recording and inviting our Zoom bot to a given bridge:

* Navigate to the FireHydrant [Integrations page](https://app.firehydrant.io/organizations/integrations)
* Select the Zoom integration and click "Reauthorize" button\*
* Accept the request for additional permissions to enable transcription services

> 🚧 \*Note:
>
> Ensure you are logged in as the Service/admin account in Zoom before doing so.

### Specify Transcription in Runbook Steps

<Image alt="Example Zoom Runbook step with &#x22;Transcribe Meeting?&#x22; option" align="center" width="650px" src="https://files.readme.io/103ed7c-zoom_transcribe.png">
  Example Zoom Runbook step with "Transcribe Meeting?" option
</Image>

The available Runbook steps for the two integrations are:

* [Create a Google Calendar Event](https://docs.firehydrant.com/docs/runbook-step-create-a-google-calendar-event)
* [Create a Zoom Meeting](https://docs.firehydrant.com/docs/runbook-step-create-a-zoom-meeting)

When configuring or updating Runbook steps that initiate Google Calendar or Zoom meetings for incidents, check the option to **Transcribe Meeting**.

#### Automatic Transcription (Zoom)

For Zoom meetings, you can enable automatic transcription, which allows the FireHydrant Zoom bot to begin recording automatically upon entering a meeting without requiring a host to start the recording manually. This feature can be enabled or disabled through the runbook step configuration:

* **When enabled**: The Zoom bot joins the meeting and immediately begins recording and transcription. A notification is automatically posted to the incident's Slack channel to inform participants that automatic recording is in progress.
* **When disabled**: The Zoom bot joins the meeting but requires manual prompting from a host to begin recording, following the traditional workflow.

This automatic recording behavior streamlines the transcription process during incident bridges, ensuring that discussions are captured from the moment the bot joins.

### FireHydrant Scribe Participation

For incidents with transcription enabled:

* The FireHydrant Scribe will automatically attempt to join the designated meeting. Someone on the call may be required to admit the Scribe depending on how your settings are configured
* Ensure recording permissions are granted to capture the meeting's context
* (Zoom) If a user has a different email in their FireHydrant than Zoom, ensure they have [linked their individual accounts](https://docs.firehydrant.com/docs/zoom-integration#linking-individual-accounts)

## Utilizing Transcribed Content

### Viewing and Editing Transcripts

<Image alt="Example view of the live transcription on a call" align="center" width="650px" src="https://files.readme.io/b768532-image.png">
  Example view of the live transcription on a call
</Image>

* In incidents where transcription is enabled, a dedicated button within the Summary Tab allows access to the meeting transcript.
* Team members can view the entire transcript to glean insights or review discussions during the meeting.
* **Note**: Direct editing of the transcript within FireHydrant is not currently supported. However, you can delete or remove specific snippets from the transcript using the trash can icon, and any subsequent summaries or inputs (re)generated will reflect removed information

### Automatic Inclusion in Key Areas

Transcribed meeting content is automatically incorporated into several areas of your incident:

* **Incident Summaries**: The incident summaries include key insights and discussions from the transcribed content, offering a richer narrative and a more comprehensive overview of the incident.
* **Incident Descriptions**: The description of an incident can be augmented with details from the meeting transcripts, providing a clearer understanding of the incident's scope and nature.
* **Customer Impact Summaries**: Insights regarding the incident's impact on customers, discussed during the call, are automatically captured and reflected in customer impact summaries.
* **Status Updates**: Relevant information from the meeting is included when drafting status updates to ensure accurate, up-to-date communication with stakeholders.
* **Retrospective Drafts**: AI-driven retrospective drafting benefits from meeting discussions, ensuring that retrospectives are aware of not just the Slack channel context but also the spoken conversation.