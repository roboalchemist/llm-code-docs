# Source: https://docs.rootly.com/ai/ai-meeting-bot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rootly Meeting Scribe

> Automatically record, transcribe, and summarize incident bridge calls across supported meeting platforms, with built-in privacy protections and deep integration into Rootly workflows.

## Overview

Rootly Meeting Scribe helps capture and preserve critical incident context that would otherwise live only in live bridge calls. When enabled, Meeting Scribe automatically joins incident bridge meetings to record, transcribe, and summarize discussions—making incident communication more accessible, auditable, and actionable.

By continuously capturing meeting context, Rootly Meeting Scribe ensures responders who join late, stakeholders who weren’t on the call, and post-incident reviewers all have access to the same shared source of truth.

Meeting Scribe supports **Zoom, Google Meet, Webex, and Microsoft Teams**, and integrates directly with Incident Summarization, Incident Catchup, and retrospectives.

<Callout icon="check" color="#DBEAFE">
  Once enabled, Rootly Meeting Scribe automatically joins incident bridges and captures transcripts and summaries.
</Callout>

## Supported Platforms

The AI Meeting Bot supports the following virtual meeting platforms:

* **Zoom** (optional auto-join support)
* **Google Meet**
* **Webex**
* **Microsoft Teams**

Each platform must be integrated with Rootly before the Meeting Bot can be used.

## Configuration

To get started, integrate your meeting platform with Rootly. Refer to the [integration documentation](/integrations) for platform-specific setup instructions.

Once your meeting platform is integrated:

1. Navigate to **Integrations** and select your meeting platform
2. Toggle on **Meeting transcript and summary**
3. For Zoom, optionally enable **Auto-join bot** to allow the bot to join meetings without manual admission

<Frame>
  <img alt="Enable meeting transcript and summary" src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/ui/bot-1.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=640037feae64dea31f6fa536d83543e3" width="1632" height="190" data-path="images/ui/bot-1.webp" />
</Frame>

When enabled, the AI Meeting Bot is automatically created when a meeting URL is added to an incident.

<Note>
  **Important:** Always use the virtual meeting room created by Rootly when an incident starts. This meeting link is pinned at the top of the incident’s Slack channel. Using the Rootly-generated meeting URL ensures the bot can join successfully and associate recordings with the correct incident.
</Note>

## During Incident Bridges

Once admitted to the incident bridge, the AI Meeting Bot immediately begins capturing the call.

During the meeting, the bot will:

* Announce its presence to participants
* Begin **live transcription** in real time
* Record audio (and video when supported)
* Identify speakers in the transcript
* Stream transcription updates back to Rootly continuously

Live transcription is available during the meeting and is included in AI-powered features such as [Incident Catchup](/ai/incident-catchup). This allows new responders to quickly understand what has already been discussed without interrupting the bridge.

<Frame>
  <img alt="Meeting bot recording and transcription" src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/ui/bot-2.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=ffaf1300e2d7b05fc31e865180a16f08" width="879" height="573" data-path="images/ui/bot-2.webp" />
</Frame>

## After the Incident

After the meeting ends and the incident is resolved, the AI Meeting Bot processes the captured data and updates the incident with:

* **Full meeting transcript** with speaker labels
* **AI-generated meeting summary** highlighting key discussion points and decisions
* **Optional video recording**, when supported by the platform
* **Automatic PII redaction**, removing sensitive data such as emails, phone numbers, passwords, and personal identifiers

All artifacts are stored in the **Meeting** tab of the incident and are automatically incorporated into incident summaries, catchup responses, and retrospectives.

<Frame>
  <img alt="Meeting transcript and summary in incident" src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/ui/bot-3.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=0d141ff0ea4f121f454217c85339a714" width="1838" height="1218" data-path="images/ui/bot-3.webp" />
</Frame>

## How It Works

The AI Meeting Bot uses the Recall.ai platform to manage meeting participation, transcription, and post-meeting analysis.

When a meeting URL is added to an incident:

1. **Bot creation**\
   Rootly creates a meeting bot scoped to the incident and team.

2. **Bot joins the meeting**\
   The bot joins automatically or waits for admission, depending on platform and settings.

3. **Live transcription & recording**\
   Real-time transcription is captured during the call, with speaker identification and word-level timing.

4. **Post-meeting analysis**\
   After the meeting ends, the bot:
   * Generates a full transcript
   * Produces an AI-generated summary
   * Applies automatic PII redaction
   * Attaches recordings and artifacts to the incident

5. **Incident integration**\
   Meeting transcripts are included in Incident Summarization and Incident Catchup, ensuring meeting context is available across Rootly AI features.

The bot may automatically retry joining meetings in certain scenarios (for example, if the meeting has not started yet or the bot is waiting to be admitted), with safeguards in place to prevent excessive retries.

## Privacy and Security

The AI Meeting Bot is built with strong privacy and security controls:

* **Automatic PII redaction** across dozens of sensitive data categories
* **Encrypted storage** for transcripts and recordings
* **Incident- and team-scoped access** to all meeting data
* **Webhook signature verification** to ensure authenticity
* **No cross-customer data sharing**

Meeting data is used only to support your organization’s incident response workflows.

## Usage Limits

Teams have monthly usage limits for meeting recording time. Usage is tracked automatically and applies across all supported platforms.

If a usage limit is exceeded, the bot will not join new meetings until usage resets or limits are increased. Your Rootly admin can review usage and limits if this occurs.

## Best Practices

* Use the Rootly-generated meeting URL pinned in the incident Slack channel
* Enable auto-join for Zoom when possible
* Admit the bot promptly when it requests access
* Monitor the **Meeting** tab for bot status and artifacts
* Use Incident Catchup to onboard late responders efficiently

## Troubleshooting

<AccordionGroup>
  <Accordion title="Why isn’t the bot joining the meeting?" icon="circle-question">
    Ensure the meeting URL was generated by Rootly and that your meeting platform integration is enabled with **Meeting transcript and summary** turned on. For Zoom, confirm whether auto-join is enabled or manually admit the bot when prompted.
  </Accordion>

  <Accordion title="Why don’t I see a transcript or summary?" icon="circle-exclamation">
    Transcripts and summaries are generated after the meeting ends. Wait a few minutes, then check the **Meeting** tab of the incident. Confirm the bot successfully joined and recorded the call.
  </Accordion>

  <Accordion title="Why am I seeing a usage limit error?" icon="triangle-exclamation">
    Your team may have exceeded its monthly meeting recording limit. Contact your Rootly admin to review usage or adjust limits.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).