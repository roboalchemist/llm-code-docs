# Source: https://docs.rootly.com/ai/mitigation-and-resolution-summary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mitigation & Resolution

> Generate concise AI-powered summaries explaining how an incident was mitigated, resolved, cancelled, or closed using Rootly AI.

## Overview

Mitigation and Resolution Summary helps responders quickly document *how* an incident was handled at key status transitions. When an incident is marked as **mitigated**, **resolved**, **cancelled**, or **closed**, Rootly AI can generate a short, clear summary describing the actions taken and the outcome.

These summaries are intentionally brief—typically one to two sentences—and are designed to reduce manual write-ups while maintaining accurate incident records for timelines, retrospectives, and reporting.

## How to Generate a Summary

Mitigation and resolution summaries can be generated from both the web application and Slack when updating an incident’s status.

### Via the Web

When updating an incident’s status to **mitigated**, **resolved**, **cancelled**, or **closed**, click the **Generate with AI** button (or the genius pen icon) next to the status message field.

<Frame>
  <img alt="Generate mitigation or resolution summary in web UI" src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/ai/mitigation.gif?s=b9a9abe5664b320c70415b531e1c8e67" width="600" height="345" data-path="images/ai/mitigation.gif" />
</Frame>

### Via Slack

In an incident Slack channel, run `/rootly mitigate` or `/rootly resolve` (also accepts `/rootly mitigated` or `/rootly resolved`). This opens a status update dialog where you can click **Generate with AI** to generate the summary.

<Frame>
  <img alt="Generate mitigation or resolution summary in Slack" src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/ai/mitigation-1.webp?fit=max&auto=format&n=R81sNIO9rI160XHL&q=85&s=ea8ed9b8fd427877c8a1a2bb7191e02b" width="890" height="556" data-path="images/ai/mitigation-1.webp" />
</Frame>

You can review and edit the generated text before submitting the status update.

## What’s Included

Depending on the status transition, Rootly AI generates a concise explanation that focuses on the key actions and outcomes:

* **Mitigated** — What specific actions were taken to reduce impact
* **Resolved** — How the incident was fully resolved
* **Cancelled** — Why the incident was cancelled
* **Closed** — Why the incident was closed

All summaries are limited to one or two sentences and prioritize clarity and relevance over exhaustive detail. The AI identifies the most important actions from the incident timeline and communications to explain the status transition clearly and consistently.

## How It Works

Rootly AI analyzes the incident’s current context at the time of the status update. This may include timeline events, alerts, action items, mitigation or resolution notes, and communications associated with the incident.

Using this context, the AI identifies the most relevant actions taken and generates a concise status summary. If there is not enough information available, Rootly will indicate that *“The incident report does not provide enough information to determine how the incident was \[status]”* and additional incident context is required before a summary can be generated.

## Configuration

Mitigation and resolution summaries are available to all customers but must be explicitly enabled.

To enable this feature, navigate to **Rootly AI** and toggle on **Enable Rootly AI**, then ensure **Mitigation and resolution summarization** is enabled. Only Admins can configure Rootly AI features.

For best results, configure **Slack channel message visibility** to **All messages** or **All messages in Public + pinned in Private**. This allows Rootly AI to access sufficient context when generating summaries.

<Frame>
  <img alt="Rootly AI mitigation and resolution configuration" src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/ai/mitigation-2.webp?fit=max&auto=format&n=R81sNIO9rI160XHL&q=85&s=d87659758c1c8fa86dee979e13ba45d0" width="1493" height="1950" data-path="images/ai/mitigation-2.webp" />
</Frame>

<Note>
  Mitigation and resolution summary generation in private incidents depends on your Slack channel message visibility settings. For private incidents, AI features are available only when your channel history scope includes private messages.
</Note>

## Best Practices

* **Generate before finalizing**\
  Use the AI-generated summary as a starting point, then review and refine it to match your team’s documentation standards.

* **Add context first**\
  Ensure the incident includes sufficient timeline events, action items, or resolution notes before generating a summary for best results.

* **Edit as needed**\
  AI-generated summaries are suggestions—customize them as needed to accurately reflect your team’s incident response.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Why isn’t the Generate with AI button appearing?" icon="circle-question">
    Ensure Rootly AI is enabled and that **Mitigation and resolution summarization** is turned on. Verify that you have permission to update the incident status and that the status you’re selecting is supported (mitigated, resolved, cancelled, or closed).
  </Accordion>

  <Accordion title="Why does the generated summary seem incomplete?" icon="circle-exclamation">
    Summaries are intentionally brief and rely on existing incident context. If you see a message indicating insufficient information, add more detail to the incident—such as timeline events, action items, or resolution notes—and try again. You can always edit the generated summary before submitting it.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).